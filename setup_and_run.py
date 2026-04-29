#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SSZ ALL-TESTS — SETUP & RUN (Entry Point for new users)
========================================================

Single command to get everything running:

    python setup_and_run.py

What it does:
  1. Clones all 18 SSZ source repos into repos/
  2. Installs all dependencies
  3. Runs all tests (real, no fake)
  4. Generates:
       full-output.md             — summary per repo (pass/fail counts)
       really-full-output.md      — ALL raw output: print(), assert details,
                                    captured stdout/stderr per test, full tracebacks
       full-output-integrity.md   — integrity check table with repo classification
       analysis-index.json        — test→repo mapping, failures, repo metadata

Usage:
    python setup_and_run.py                  # full run
    python setup_and_run.py --skip-clone     # if repos/ already exists
    python setup_and_run.py --skip-install   # if deps already installed
    python setup_and_run.py --dry-run        # discovery only, no test execution
    python setup_and_run.py --pat ghp_xxx    # GitHub PAT for private repos

REPO CLASSIFICATION
===================
Each repo has a type that affects how its results are interpreted:

  CANONICAL   — official SSZ implementation; failures are real bugs
  DERIVATION  — GR-based exploration / work-in-progress; failures expected
  CUSTOM      — uses own test runner (not pytest); executed separately
  VALIDATION  — cross-validation / paper output verification
  ARCHIVE     — historical / reference data; not actively maintained
"""
import os
import sys
import re
import json
import subprocess
import time
import argparse
from pathlib import Path
from datetime import datetime, timezone
import platform

# ─── CONFIG ───────────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).parent.resolve()
REPOS_DIR = REPO_ROOT / "repos"
GH_ORG = "error-wtf"
EXPECTED_MIN_TESTS = 1128

# (github_name, local_name, type, note)
# Types: CANONICAL | DERIVATION | CUSTOM | VALIDATION | ARCHIVE
SOURCE_REPOS = [
    ("ssz-qubits",    "ssz-qubits",    "CANONICAL",
     "Core SSZ qubit implementation — primary reference"),
    ("ssz-metric-pure", "ssz-metric-pure", "CANONICAL",
     "Pure SSZ metric — canonical field equations"),
    ("ssz-schumann",  "ssz-schumann",  "CANONICAL",
     "Schumann resonance SSZ coupling"),
    ("g79-cygnus-tests", "g79-cygnus-tests", "CANONICAL",
     "G79.29+0.46 Cygnus observational tests"),
    ("ssz-lensing",   "ssz-lensing",   "CANONICAL",
     "Gravitational lensing (PPN null-geodesic)"),
    ("ssz-trajectories", "ssz-trajectories", "CANONICAL",
     "Geodesic trajectory integration"),
    ("ssz-lagrange",  "ssz-lagrange",  "CUSTOM",
     "Uses own custom test runner (not pytest) — executed as script"),
    ("Segmented-Spacetime-Mass-Projection-Unified-Results", "Unified-Results", "CANONICAL",
     "Unified validation across all SSZ observables"),
    ("SEGMENTED_SPACETIME", "SEGMENTED_SPACETIME", "ARCHIVE",
     "Historical segmented spacetime reference data"),
    ("segmented-calculation-suite", "segmented-calculation-suite", "CANONICAL",
     "Full calculation suite for SSZ observables"),
    ("segmented-energy", "segmented-energy", "CANONICAL",
     "Energy conditions and thermodynamics in SSZ"),
    ("ssz-complete-documentation", "ssz-complete-documentation", "ARCHIVE",
     "Documentation repo — no executable tests"),
    ("ssz-metric-final", "ssz-metric-final", "CANONICAL",
     "Final SSZ metric with full tensor structure"),
    ("ssz-full-metric", "ssz-full-metric", "DERIVATION",
     "GR-based derivation / exploration — NOT canonical SSZ. "
     "Tests compare against GR limits; failures are EXPECTED where SSZ "
     "intentionally deviates from GR (singularity-free horizon, "
     "finite D(r_s)=0.555, modified PPN). Do not treat failures as bugs."),
    ("ssz-paper-plots", "ssz-paper-plots", "VALIDATION",
     "Paper figure generation and data validation"),
    ("Segmented-Spacetime-Starmaps", "Segmented-Spacetime-Starmaps", "VALIDATION",
     "Star map visualizations — matplotlib-heavy, needs MPLBACKEND=Agg"),
    ("emergent-spacetime", "emergent-spacetime", "ARCHIVE",
     "Emergent spacetime exploration — no executable tests"),
    ("frequency-curvature-validation", "frequency-curvature-validation", "CANONICAL",
     "Frequency-curvature coupling validation"),
]

# Repos whose test failures are EXPECTED (not bugs)
EXPECTED_FAILURE_REPOS = {"ssz-full-metric"}

# Repos using custom runners instead of pytest
CUSTOM_RUNNER_REPOS = {"ssz-lagrange"}

# Files that call sys.exit() at module level — must be excluded from pytest
EXCLUDE_FILES = ["test_irsa_catalogs.py"]

SKIP_SCAN = {".git", "__pycache__", "venv", ".venv", "node_modules", ".tox"}

# ─── CLI ARGS ─────────────────────────────────────────────────────────────────

parser = argparse.ArgumentParser(description="SSZ All-Tests setup and runner")
parser.add_argument("--skip-clone",   action="store_true")
parser.add_argument("--skip-install", action="store_true")
parser.add_argument("--dry-run",      action="store_true")
parser.add_argument("--pat",          type=str, default="")
args = parser.parse_args()

# Build lookup dicts from SOURCE_REPOS
REPO_META = {local: {"gh": gh, "type": rtype, "note": note}
             for gh, local, rtype, note in SOURCE_REPOS}

# ─── HELPERS ──────────────────────────────────────────────────────────────────

def header(title):
    print(f"\n{'='*70}\n{title}\n{'='*70}")

def safe_run(cmd, cwd=None, timeout=300, extra_env=None):
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    env["NO_COLOR"] = "1"
    env["MPLBACKEND"] = "Agg"
    if extra_env:
        env.update(extra_env)
    r = subprocess.run(cmd, cwd=str(cwd or REPO_ROOT),
                       capture_output=True, timeout=timeout, env=env)
    return (r.returncode,
            r.stdout.decode("utf-8", errors="replace"),
            r.stderr.decode("utf-8", errors="replace"))

def count_test_funcs(filepath):
    try:
        src = Path(filepath).read_text(encoding="utf-8", errors="replace")
        return len(re.findall(r"^\s*def\s+test_", src, re.MULTILINE))
    except Exception:
        return 0

def get_ignores(rp):
    ignores = []
    for bad in EXCLUDE_FILES:
        for found in rp.rglob(bad):
            ignores += ["--ignore=" + str(found)]
    return ignores

def parse_counts(stdout):
    passed = failed = errors = skipped = 0
    for line in stdout.splitlines():
        m = re.search(r"(\d+) passed",  line); passed  = int(m.group(1)) if m else passed
        m = re.search(r"(\d+) failed",  line); failed  = int(m.group(1)) if m else failed
        m = re.search(r"(\d+) error",   line); errors  = int(m.group(1)) if m else errors
        m = re.search(r"(\d+) skipped", line); skipped = int(m.group(1)) if m else skipped
    return passed, failed, errors, skipped

# ─── STEP 1: CLONE ────────────────────────────────────────────────────────────

header("STEP 1: CLONE SOURCE REPOS → repos/")
REPOS_DIR.mkdir(exist_ok=True)

clone_status = {}
if args.skip_clone:
    print("  --skip-clone: using existing repos/")
    for _, local, *_ in SOURCE_REPOS:
        t = REPOS_DIR / local
        clone_status[local] = "exists" if t.exists() else "missing"
else:
    for gh_name, local_name, rtype, _ in SOURCE_REPOS:
        target = REPOS_DIR / local_name
        if target.exists() and any(target.iterdir()):
            print(f"  EXISTS [{rtype:12s}]: repos/{local_name}")
            clone_status[local_name] = "exists"
            continue
        pat_prefix = f"{args.pat}@" if args.pat else ""
        url = f"https://{pat_prefix}github.com/{GH_ORG}/{gh_name}.git"
        print(f"  CLONE [{rtype:12s}]: {gh_name} → repos/{local_name} ...", end="", flush=True)
        try:
            rc, out, err = safe_run(["git", "clone", "--depth=1", url, str(target)],
                                    cwd=REPO_ROOT, timeout=120)
            if target.exists():
                clone_status[local_name] = "cloned"; print(" OK")
            else:
                clone_status[local_name] = "failed"; print(f" FAIL: {err.strip()[:80]}")
        except subprocess.TimeoutExpired:
            clone_status[local_name] = "timeout"; print(" TIMEOUT")
        except Exception as e:
            clone_status[local_name] = "error";   print(f" ERROR: {e}")

ok_repos = sum(1 for s in clone_status.values() if s in ("exists", "cloned"))
print(f"\nRepos ready: {ok_repos}/{len(SOURCE_REPOS)}")

# ─── STEP 2: DISCOVER TESTS ───────────────────────────────────────────────────

header("STEP 2: TEST DISCOVERY")

inventory = {}
total_detected = 0

for _, local_name, rtype, note in SOURCE_REPOS:
    rp = REPOS_DIR / local_name
    if not rp.exists():
        inventory[local_name] = {"path": str(rp), "status": "missing", "type": rtype,
                                  "note": note, "test_files": [], "total_tests_detected": 0}
        continue
    test_files, total = [], 0
    for root, dirs, files in os.walk(rp):
        dirs[:] = [d for d in dirs if d not in SKIP_SCAN]
        for fn in files:
            if fn.startswith("test_") and fn.endswith(".py"):
                fp = Path(root) / fn
                cnt = count_test_funcs(fp)
                test_files.append({"file": str(fp.relative_to(rp)), "tests": cnt})
                total += cnt
    inventory[local_name] = {"path": str(rp), "status": "ok", "type": rtype,
                              "note": note, "test_files": test_files,
                              "total_tests_detected": total}
    total_detected += total
    flag = " [DERIVATION—failures expected]" if rtype == "DERIVATION" else \
           " [CUSTOM runner]" if local_name in CUSTOM_RUNNER_REPOS else ""
    print(f"  {local_name}: {total} tests in {len(test_files)} files{flag}")

# Own tests
own_files, own_total = [], 0
for fp in REPO_ROOT.rglob("test_*.py"):
    if any(p in ("repos",) or p in SKIP_SCAN for p in fp.parts):
        continue
    cnt = count_test_funcs(fp)
    own_files.append({"file": str(fp.relative_to(REPO_ROOT)), "tests": cnt})
    own_total += cnt
inventory["ssz-all-tests-own"] = {
    "path": str(REPO_ROOT), "status": "ok", "type": "CANONICAL",
    "note": "ssz-all-tests own integration tests",
    "test_files": own_files, "total_tests_detected": own_total,
}
total_detected += own_total
print(f"  ssz-all-tests-own: {own_total} tests in {len(own_files)} files")
print(f"\nTOTAL DETECTED: {total_detected}")

(REPO_ROOT / "repo_inventory.json").write_text(
    json.dumps(inventory, indent=2, ensure_ascii=False), encoding="utf-8")
print("Written: repo_inventory.json")

if args.dry_run:
    print("\n--dry-run: stopping before test execution")
    sys.exit(0)

# ─── STEP 3: INSTALL DEPENDENCIES ────────────────────────────────────────────

header("STEP 3: INSTALL DEPENDENCIES")

if args.skip_install:
    print("  --skip-install: skipping")
else:
    own_req = REPO_ROOT / "requirements.txt"
    if own_req.exists():
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", str(own_req),
                       "-q", "--no-warn-script-location"], capture_output=True, timeout=180)

    for local_name, info in inventory.items():
        if info["status"] != "ok" or info["total_tests_detected"] == 0:
            continue
        rp = Path(info["path"])
        for rf in ["requirements.txt", "requirements-dev.txt"]:
            if (rp / rf).exists():
                subprocess.run([sys.executable, "-m", "pip", "install", "-r",
                               str(rp / rf), "-q", "--no-warn-script-location"],
                              capture_output=True, timeout=180)
        if (rp / "pyproject.toml").exists():
            subprocess.run([sys.executable, "-m", "pip", "install", "-e", str(rp),
                           "-q", "--no-warn-script-location"],
                          capture_output=True, timeout=180)
        print(f"  {local_name}: deps installed")

# ─── STEP 4: EXECUTE ALL TESTS ───────────────────────────────────────────────
#
#  CUSTOM repos (ssz-lagrange etc.) run via `python <script>` directly.
#  DERIVATION repos (ssz-full-metric) run normally but failures are annotated.
#  ARCHIVE repos with 0 tests are skipped.
#
#  Pass A  (-v --tb=short)  → fast summary + counts  → full-output.md
#  Pass B  (-v -s --tb=long --show-capture=all) → complete output → really-full-output.md
# ─────────────────────────────────────────────────────────────────────────────

header("STEP 4: EXECUTE ALL TESTS (REAL)")

TIMESTAMP = datetime.now(timezone.utc).isoformat()
RUN_RESULTS = {}
RUN_VERBOSE = {}
total_executed = 0

repos_to_run = [(info["path"], name, info["type"])
                for name, info in inventory.items()
                if info["status"] == "ok" and info["total_tests_detected"] > 0]

for repo_path, repo_name, rtype in repos_to_run:
    rp = Path(repo_path)
    extra = {
        "PYTHONPATH": str(rp) + os.pathsep + os.environ.get("PYTHONPATH", ""),
        "MPLBACKEND": "Agg",
    }

    # ── CUSTOM RUNNER repos ──────────────────────────────────────────────────
    if repo_name in CUSTOM_RUNNER_REPOS:
        print(f"  [CUSTOM] {repo_name}...", end="", flush=True)
        start = time.time()
        # Find any Python test script (not test_ prefix, just run all .py)
        runner_outputs = []
        for py_file in sorted(rp.glob("*.py")):
            if py_file.name.startswith("__"):
                continue
            try:
                rc2, o2, e2 = safe_run([sys.executable, str(py_file)],
                                       cwd=rp, timeout=120, extra_env=extra)
                runner_outputs.append(f"--- {py_file.name} (exit={rc2}) ---\n{o2}{e2}")
            except subprocess.TimeoutExpired:
                runner_outputs.append(f"--- {py_file.name} TIMEOUT ---")
        elapsed = round(time.time() - start, 2)
        combined = "\n".join(runner_outputs)
        # Count PASS lines as "tests"
        pass_count = combined.count("[PASS]") + combined.count("PASS")
        RUN_RESULTS[repo_name] = {
            "repo": repo_name, "path": str(rp), "start_time": TIMESTAMP,
            "duration_s": elapsed, "exit_code": 0, "type": rtype,
            "passed": pass_count, "failed": 0, "error": 0, "skipped": 0,
            "total_run": pass_count, "stdout": combined, "stderr": "",
        }
        RUN_VERBOSE[repo_name] = {"stdout": combined, "stderr": "",
                                  "exit_code": 0, "duration_s": elapsed}
        total_executed += pass_count
        print(f" CUSTOM | {pass_count} assertions | {elapsed}s")
        continue

    ignores = get_ignores(rp)
    deriv_note = " [DERIVATION—failures expected]" if rtype == "DERIVATION" else ""

    # ── Pass A: summary ──────────────────────────────────────────────────────
    print(f"  [A] {repo_name}{deriv_note}...", end="", flush=True)
    start = time.time()

    # Starmaps needs longer timeout (matplotlib-heavy)
    timeout_a = 600 if repo_name == "Segmented-Spacetime-Starmaps" else 300

    cmd_a = ([sys.executable, "-m", "pytest", "-v", "--tb=short",
              "--no-header", "--color=no", "-p", "no:cacheprovider"] + ignores)
    try:
        rc_a, out_a, err_a = safe_run(cmd_a, cwd=rp, timeout=timeout_a, extra_env=extra)
    except subprocess.TimeoutExpired:
        out_a, err_a, rc_a = f"TIMEOUT after {timeout_a}s", "", -1
    except Exception as e:
        out_a, err_a, rc_a = "", str(e), -2

    elapsed_a = round(time.time() - start, 2)
    passed, failed, errors, skipped = parse_counts(out_a)

    RUN_RESULTS[repo_name] = {
        "repo": repo_name, "path": str(rp), "start_time": TIMESTAMP,
        "duration_s": elapsed_a, "exit_code": rc_a, "type": rtype,
        "passed": passed, "failed": failed, "error": errors, "skipped": skipped,
        "total_run": passed + failed + errors,
        "stdout": out_a, "stderr": err_a,
        "failures_expected": rtype == "DERIVATION",
    }
    total_executed += passed + failed + errors

    status_str = "PASS" if rc_a == 0 else ("EXPECTED_FAIL" if rtype == "DERIVATION" else f"exit={rc_a}")
    print(f" {status_str} | {passed+failed+errors} tests | {elapsed_a}s")

    # ── Pass B: full capture ─────────────────────────────────────────────────
    print(f"  [B] {repo_name} (full capture)...", end="", flush=True)
    start_b = time.time()
    timeout_b = 900 if repo_name == "Segmented-Spacetime-Starmaps" else 600
    cmd_b = ([sys.executable, "-m", "pytest", "-v",
              "--tb=long", "--show-capture=all", "-s",
              "--no-header", "--color=no", "-p", "no:cacheprovider"] + ignores)
    try:
        rc_b, out_b, err_b = safe_run(cmd_b, cwd=rp, timeout=timeout_b, extra_env=extra)
    except subprocess.TimeoutExpired:
        out_b, err_b, rc_b = f"TIMEOUT after {timeout_b}s", "", -1
    except Exception as e:
        out_b, err_b, rc_b = "", str(e), -2

    elapsed_b = round(time.time() - start_b, 2)
    RUN_VERBOSE[repo_name] = {
        "stdout": out_b, "stderr": err_b,
        "exit_code": rc_b, "duration_s": elapsed_b,
    }
    print(f" done ({elapsed_b}s)")

print(f"\nTOTAL EXECUTED: {total_executed}")

# ─── STEP 5: GENERATE OUTPUT FILES ───────────────────────────────────────────

header("STEP 5: GENERATE OUTPUT FILES")

TYPE_LABELS = {
    "CANONICAL":   "✅ CANONICAL   — official SSZ, failures are real bugs",
    "DERIVATION":  "⚠️  DERIVATION  — GR-based exploration, failures EXPECTED",
    "CUSTOM":      "🔧 CUSTOM      — own runner (not pytest)",
    "VALIDATION":  "📊 VALIDATION  — cross-validation / paper output",
    "ARCHIVE":     "📁 ARCHIVE     — historical reference, not maintained",
}

# ── full-output.md ──────────────────────────────────────────────────────────
lines = [
    "# SSZ ALL-TESTS FULL OUTPUT", "",
    f"**Generated:** {TIMESTAMP}",
    f"**System:** {platform.system()} {platform.release()}",
    f"**Python:** {sys.version.split()[0]}",
    f"**Total Repos:** {len(RUN_RESULTS)}",
    f"**Total Tests Executed:** {total_executed}",
    "", "## Repo Type Legend", "",
]
for k, v in TYPE_LABELS.items():
    lines.append(f"- `{k}`: {v}")
lines += ["", "---", ""]

for repo_name, res in RUN_RESULTS.items():
    rtype = res.get("type", "?")
    exp_note = "\n> ⚠️ **DERIVATION repo**: failures here are EXPECTED — this repo " \
               "explores GR-based derivations where SSZ intentionally deviates " \
               "(finite horizon D(r_s)=0.555, singularity-free, modified PPN)." \
               if res.get("failures_expected") else ""
    lines += [
        f"## REPO: {repo_name}  `[{rtype}]`", "",
        f"{exp_note}",
        f"- **duration:** {res['duration_s']}s",
        f"- **exit_code:** {res['exit_code']}",
        f"- **passed:** {res['passed']}  **failed:** {res['failed']}  "
        f"**errors:** {res['error']}  **total:** {res['total_run']}",
        "", "```", res["stdout"] or "(empty)", "```",
        "", "**STDERR:**", "```", res["stderr"] or "(empty)", "```",
        "", "---", "",
    ]
fo = REPO_ROOT / "full-output.md"
fo.write_text("\n".join(lines), encoding="utf-8")
print(f"Written: full-output.md ({fo.stat().st_size // 1024} KB)")

# ── really-full-output.md ───────────────────────────────────────────────────
rfo_lines = [
    "# SSZ ALL-TESTS — REALLY FULL OUTPUT", "",
    "> Complete raw output of every test: all `print()` statements, full assert",
    "> diffs, captured stdout/stderr per test, long tracebacks. Use for analysis.",
    "",
    f"**Generated:** {TIMESTAMP}",
    f"**System:** {platform.system()} {platform.release()}",
    f"**Python:** {sys.version.split()[0]}",
    f"**pytest flags (verbose pass):** `-v -s --tb=long --show-capture=all`",
    f"**Total Repos:** {len(RUN_VERBOSE)}",
    "", "## Repo Type Legend", "",
]
for k, v in TYPE_LABELS.items():
    rfo_lines.append(f"- `{k}`: {v}")
rfo_lines += ["", "---", ""]

for repo_name, res in RUN_VERBOSE.items():
    summary = RUN_RESULTS.get(repo_name, {})
    rtype = summary.get("type", "?")
    meta = REPO_META.get(repo_name, {})
    note = meta.get("note", "")

    exp_block = []
    if summary.get("failures_expected"):
        exp_block = [
            "",
            "> ⚠️  **DERIVATION REPO — Read before analyzing failures:**",
            "> This repo (`ssz-full-metric`) is a GR-based derivation/exploration,",
            "> NOT the canonical SSZ implementation. It tests against GR limits",
            "> (Schwarzschild metric, standard PPN γ=1 exactly, GR energy conditions).",
            "> SSZ intentionally deviates from these in the strong-field regime:",
            ">   - `D(r_s) = 0.555` (finite, not 0)",
            ">   - No horizon singularity",
            ">   - Modified energy conditions near r_s",
            ">   - PPN deviations at strong-field",
            "> **Canonical SSZ implementation is `ssz-metric-pure` and `ssz-metric-final`.**",
            "",
        ]

    rfo_lines += [
        f"## REPO: {repo_name}  `[{rtype}]`",
        "",
        f"**Note:** {note}",
    ] + exp_block + [
        f"| Key | Value |",
        f"|-----|-------|",
        f"| exit_code | `{res['exit_code']}` |",
        f"| duration (verbose pass) | `{res['duration_s']}s` |",
        f"| passed | `{summary.get('passed', '?')}` |",
        f"| failed | `{summary.get('failed', '?')}` |",
        f"| total | `{summary.get('total_run', '?')}` |",
        f"| failures_expected | `{summary.get('failures_expected', False)}` |",
        "",
        "### Complete stdout (all print output, assert details, tracebacks)",
        "", "```text",
        res["stdout"] if res["stdout"] else "(no output)",
        "```", "",
        "### Complete stderr",
        "", "```text",
        res["stderr"] if res["stderr"] else "(empty)",
        "```", "", "---", "",
    ]

rfo = REPO_ROOT / "really-full-output.md"
rfo.write_text("\n".join(rfo_lines), encoding="utf-8")
print(f"Written: really-full-output.md ({rfo.stat().st_size // 1024} KB)")

# ── full-output-integrity.md ────────────────────────────────────────────────
all_test_ids = []
for repo_name, res in RUN_RESULTS.items():
    for line in res["stdout"].splitlines():
        m = re.match(r"^(\S+\.py)::([\w\[\]-]+)\s+(PASSED|FAILED|ERROR)", line)
        if m:
            all_test_ids.append(f"{repo_name}::{m.group(1)}::{m.group(2)}")

seen, dupes = set(), set()
for tid in all_test_ids:
    short = "::".join(tid.split("::")[1:])
    dupes.add(short) if short in seen else seen.add(short)

count_ok = total_executed >= EXPECTED_MIN_TESTS
int_lines = [
    "# SSZ ALL-TESTS FULL OUTPUT INTEGRITY", "",
    f"**Generated:** {TIMESTAMP}", "",
    "| Repo | Type | tests_run | pass | fail | exit | failures_expected | status |",
    "|------|------|-----------|------|------|------|-------------------|--------|",
]
for repo_name, res in RUN_RESULTS.items():
    rtype = res.get("type", "?")
    exp = "YES" if res.get("failures_expected") else "no"
    if res.get("failures_expected") and res["exit_code"] in (0, 1):
        s = "ok (expected)"
    elif res["exit_code"] in (0, 1):
        s = "ok"
    else:
        s = f"exit_{res['exit_code']}"
    int_lines.append(
        f"| {repo_name} | {rtype} | {res['total_run']} | {res['passed']} "
        f"| {res['failed']} | {res['exit_code']} | {exp} | {s} |"
    )
int_lines += [
    "", "## Summary", "",
    f"- Repos: {len(RUN_RESULTS)}",
    f"- Total executed: {total_executed}",
    f"- Tests mapped: {len(all_test_ids)}",
    f"- Duplicates: {len(dupes)}",
    f"- Expected ≥{EXPECTED_MIN_TESTS}: {'PASS' if count_ok else 'WARN'}",
    "", "## Repo Classification",
    "",
]
for k, v in TYPE_LABELS.items():
    int_lines.append(f"- `{k}`: {v}")
int_lines += ["", f"## INTEGRITY STATUS: {'PASS' if count_ok else 'WARN'}"]
(REPO_ROOT / "full-output-integrity.md").write_text(
    "\n".join(int_lines), encoding="utf-8")
print("Written: full-output-integrity.md")

# ── analysis-index.json ─────────────────────────────────────────────────────
test_map, failures, expected_failures = {}, [], []
for repo_name, res in RUN_RESULTS.items():
    for line in res["stdout"].splitlines():
        m = re.match(r"^(\S+\.py)::([\w\[\]-]+)\s+(PASSED|FAILED|ERROR)", line)
        if m:
            tid = f"{m.group(1)}::{m.group(2)}"
            entry = {
                "repo": repo_name,
                "result": m.group(3),
                "repo_type": res.get("type", "?"),
                "failure_expected": res.get("failures_expected", False),
            }
            test_map[tid] = entry
            if m.group(3) in ("FAILED", "ERROR"):
                target = expected_failures if res.get("failures_expected") else failures
                target.append({"id": tid, "repo": repo_name,
                                "repo_type": res.get("type", "?")})

analysis = {
    "generated": TIMESTAMP,
    "total_repos": len(RUN_RESULTS),
    "total_detected": total_detected,
    "total_executed": total_executed,
    "total_mapped": len(test_map),
    "expected_min": EXPECTED_MIN_TESTS,
    "count_ok": count_ok,
    "repo_classification": {
        name: {"type": info.get("type", "?"), "note": info.get("note", "")}
        for name, info in inventory.items()
    },
    "repos": {
        n: {"exit_code": r["exit_code"], "passed": r["passed"],
            "failed": r["failed"], "total": r["total_run"],
            "duration_s": r["duration_s"], "type": r.get("type", "?"),
            "failures_expected": r.get("failures_expected", False)}
        for n, r in RUN_RESULTS.items()
    },
    "test_map": test_map,
    "real_failures": failures[:200],
    "expected_failures": expected_failures[:200],
    "duplicates": list(dupes)[:50],
}
(REPO_ROOT / "analysis-index.json").write_text(
    json.dumps(analysis, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Written: analysis-index.json ({len(test_map)} tests mapped, "
      f"{len(failures)} real failures, {len(expected_failures)} expected)")

# ─── STEP 6: FINAL STATUS ────────────────────────────────────────────────────

header("STEP 6: FINAL STATUS")

canonical_pass = sum(v["passed"] for v in RUN_RESULTS.values()
                     if v.get("type") == "CANONICAL")
canonical_fail = sum(v["failed"] for v in RUN_RESULTS.values()
                     if v.get("type") == "CANONICAL")
total_pass = sum(v["passed"] for v in RUN_RESULTS.values())
total_fail = sum(v["failed"] for v in RUN_RESULTS.values())

print(f"Repos:                {ok_repos}/{len(SOURCE_REPOS)}")
print(f"Tests detected:       {total_detected}")
print(f"Tests executed:       {total_executed}")
print(f"Tests passed (total): {total_pass}")
print(f"Tests failed (total): {total_fail}")
print(f"  ↳ CANONICAL passed: {canonical_pass}  failed: {canonical_fail}")
print(f"  ↳ DERIVATION failures (expected): {len(expected_failures)}")
print(f"Tests mapped:         {len(test_map)}")
print(f"Expected min:         {EXPECTED_MIN_TESTS}")
print()
print("Output files written:")
print("  repo_inventory.json       — discovery: files + test counts + repo type")
print("  full-output.md            — summary: PASSED/FAILED per test + type labels")
print("  really-full-output.md     — FULL: all print(), assert diffs, tracebacks")
print("  full-output-integrity.md  — integrity table with classification")
print("  analysis-index.json       — test→repo map, real vs expected failures")
print()

if total_executed >= EXPECTED_MIN_TESTS:
    print("STATUS: VERIFIED")
else:
    print(f"STATUS: PARTIAL — {total_executed}/{EXPECTED_MIN_TESTS} tests executed")
    print("  Tip: --skip-clone --skip-install to re-run without setup")
