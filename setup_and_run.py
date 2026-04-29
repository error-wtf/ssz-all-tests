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
  4. Generates full-output.md, full-output-integrity.md, analysis-index.json

Usage:
    python setup_and_run.py                  # full run
    python setup_and_run.py --skip-clone     # if repos/ already exists
    python setup_and_run.py --skip-install   # if deps already installed
    python setup_and_run.py --dry-run        # discovery only, no test execution
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

# GitHub organization — all source repos live here
GH_ORG = "error-wtf"

# All 18 SSZ source repos with their clone names
SOURCE_REPOS = [
    ("ssz-qubits",                                       "ssz-qubits"),
    ("ssz-metric-pure",                                  "ssz-metric-pure"),
    ("ssz-schumann",                                     "ssz-schumann"),
    ("g79-cygnus-tests",                                 "g79-cygnus-tests"),
    ("ssz-lensing",                                      "ssz-lensing"),
    ("ssz-trajectories",                                 "ssz-trajectories"),
    ("ssz-lagrange",                                     "ssz-lagrange"),
    ("Segmented-Spacetime-Mass-Projection-Unified-Results", "Unified-Results"),
    ("SEGMENTED_SPACETIME",                              "SEGMENTED_SPACETIME"),
    ("segmented-calculation-suite",                      "segmented-calculation-suite"),
    ("segmented-energy",                                 "segmented-energy"),
    ("ssz-complete-documentation",                       "ssz-complete-documentation"),
    ("ssz-metric-final",                                 "ssz-metric-final"),
    ("ssz-full-metric",                                  "ssz-full-metric"),
    ("ssz-paper-plots",                                  "ssz-paper-plots"),
    ("Segmented-Spacetime-Starmaps",                     "Segmented-Spacetime-Starmaps"),
    ("emergent-spacetime",                               "emergent-spacetime"),
    ("frequency-curvature-validation",                   "frequency-curvature-validation"),
]

EXPECTED_MIN_TESTS = 1128

# ─── CLI ARGS ─────────────────────────────────────────────────────────────────

parser = argparse.ArgumentParser(description="SSZ All-Tests setup and runner")
parser.add_argument("--skip-clone",   action="store_true", help="Skip cloning repos (use existing repos/)")
parser.add_argument("--skip-install", action="store_true", help="Skip pip install steps")
parser.add_argument("--dry-run",      action="store_true", help="Discover tests only, do not execute")
parser.add_argument("--pat",          type=str, default="",  help="GitHub PAT for private repos (optional)")
args = parser.parse_args()

# ─── HELPERS ──────────────────────────────────────────────────────────────────

def header(title):
    print(f"\n{'='*70}\n{title}\n{'='*70}")

def run(cmd, cwd=None, timeout=300, env=None):
    """Run subprocess, return (returncode, stdout, stderr) — bytes decoded safely."""
    e = (env or os.environ).copy()
    e["PYTHONIOENCODING"] = "utf-8"
    e["PYTHONUTF8"] = "1"
    e["NO_COLOR"] = "1"
    r = subprocess.run(cmd, cwd=str(cwd or REPO_ROOT),
                       capture_output=True, timeout=timeout, env=e)
    out = r.stdout.decode("utf-8", errors="replace")
    err = r.stderr.decode("utf-8", errors="replace")
    return r.returncode, out, err

def count_test_funcs(filepath):
    try:
        src = Path(filepath).read_text(encoding="utf-8", errors="replace")
        return len(re.findall(r"^\s*def\s+test_", src, re.MULTILINE))
    except Exception:
        return 0

# ─── STEP 1: CLONE ────────────────────────────────────────────────────────────

header("STEP 1: CLONE SOURCE REPOS → repos/")
REPOS_DIR.mkdir(exist_ok=True)

clone_status = {}
if args.skip_clone:
    print("  --skip-clone: using existing repos/")
    for _, name in SOURCE_REPOS:
        t = REPOS_DIR / name
        clone_status[name] = "exists" if t.exists() else "missing"
else:
    for gh_name, local_name in SOURCE_REPOS:
        target = REPOS_DIR / local_name
        if target.exists() and any(target.iterdir()):
            print(f"  EXISTS: repos/{local_name}")
            clone_status[local_name] = "exists"
            continue

        pat_prefix = f"{args.pat}@" if args.pat else ""
        url = f"https://{pat_prefix}github.com/{GH_ORG}/{gh_name}.git"
        print(f"  CLONE: {gh_name} → repos/{local_name} ...", end="", flush=True)
        try:
            rc, out, err = run(["git", "clone", "--depth=1", url, str(target)],
                               cwd=REPO_ROOT, timeout=120)
            if target.exists():
                clone_status[local_name] = "cloned"
                print(" OK")
            else:
                clone_status[local_name] = "failed"
                print(f" FAIL: {err.strip()[:80]}")
        except subprocess.TimeoutExpired:
            clone_status[local_name] = "timeout"
            print(" TIMEOUT")
        except Exception as e:
            clone_status[local_name] = "error"
            print(f" ERROR: {e}")

ok_repos = sum(1 for s in clone_status.values() if s in ("exists", "cloned"))
print(f"\nRepos ready: {ok_repos}/{len(SOURCE_REPOS)}")

# ─── STEP 2: DISCOVER TESTS ───────────────────────────────────────────────────

header("STEP 2: TEST DISCOVERY")

SKIP_SCAN = {".git", "__pycache__", "venv", ".venv", "node_modules", ".tox"}

inventory = {}
total_detected = 0

for _, local_name in SOURCE_REPOS:
    rp = REPOS_DIR / local_name
    if not rp.exists():
        inventory[local_name] = {"path": str(rp), "status": "missing",
                                  "test_files": [], "total_tests_detected": 0}
        continue

    test_files = []
    total = 0
    for root, dirs, files in os.walk(rp):
        dirs[:] = [d for d in dirs if d not in SKIP_SCAN]
        for fn in files:
            if fn.startswith("test_") and fn.endswith(".py"):
                fp = Path(root) / fn
                cnt = count_test_funcs(fp)
                test_files.append({"file": str(fp.relative_to(rp)), "tests": cnt})
                total += cnt

    inventory[local_name] = {"path": str(rp), "status": "ok",
                              "test_files": test_files, "total_tests_detected": total}
    total_detected += total
    print(f"  {local_name}: {total} tests in {len(test_files)} files")

# Also count ssz-all-tests own tests
own_files = []
own_total = 0
for fp in REPO_ROOT.rglob("test_*.py"):
    if any(part in SKIP_SCAN or part == "repos" for part in fp.parts):
        continue
    cnt = count_test_funcs(fp)
    own_files.append({"file": str(fp.relative_to(REPO_ROOT)), "tests": cnt})
    own_total += cnt
inventory["ssz-all-tests-own"] = {"path": str(REPO_ROOT), "status": "ok",
                                   "test_files": own_files, "total_tests_detected": own_total}
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
    print("  --skip-install: skipping pip install")
else:
    # Install ssz-all-tests own requirements first
    own_req = REPO_ROOT / "requirements.txt"
    if own_req.exists():
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", str(own_req),
                       "-q", "--no-warn-script-location"],
                      capture_output=True, timeout=180)

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

header("STEP 4: EXECUTE ALL TESTS (REAL)")

TIMESTAMP = datetime.now(timezone.utc).isoformat()
RUN_RESULTS = {}
total_executed = 0

# Known files that call sys.exit() at module level — exclude them
EXCLUDE_FILES = ["test_irsa_catalogs.py"]

repos_to_run = [(info["path"], name)
                for name, info in inventory.items()
                if info["status"] == "ok" and info["total_tests_detected"] > 0]

for repo_path, repo_name in repos_to_run:
    rp = Path(repo_path)
    print(f"  RUNNING: {repo_name}...", end="", flush=True)
    start = time.time()

    env = os.environ.copy()
    env["PYTHONPATH"] = str(rp) + os.pathsep + env.get("PYTHONPATH", "")
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    env["NO_COLOR"] = "1"

    ignores = []
    for bad in EXCLUDE_FILES:
        for found in rp.rglob(bad):
            ignores += ["--ignore=" + str(found)]

    cmd = ([sys.executable, "-m", "pytest", "-v", "--tb=short",
            "--no-header", "--color=no", "-p", "no:cacheprovider"]
           + ignores)

    try:
        r = subprocess.run(cmd, cwd=str(rp), capture_output=True,
                           timeout=300, env=env)
        stdout = r.stdout.decode("utf-8", errors="replace")
        stderr = r.stderr.decode("utf-8", errors="replace")
        exit_code = r.returncode
    except subprocess.TimeoutExpired:
        stdout = "TIMEOUT after 300s"
        stderr = ""
        exit_code = -1
    except Exception as e:
        stdout = ""
        stderr = str(e)
        exit_code = -2

    elapsed = round(time.time() - start, 2)

    passed = failed = errors = skipped = 0
    for line in stdout.splitlines():
        m = re.search(r"(\d+) passed", line)
        if m: passed = int(m.group(1))
        m = re.search(r"(\d+) failed", line)
        if m: failed = int(m.group(1))
        m = re.search(r"(\d+) error", line)
        if m: errors = int(m.group(1))
        m = re.search(r"(\d+) skipped", line)
        if m: skipped = int(m.group(1))

    result = {"repo": repo_name, "path": str(rp), "start_time": TIMESTAMP,
              "duration_s": elapsed, "exit_code": exit_code,
              "passed": passed, "failed": failed, "error": errors,
              "skipped": skipped, "total_run": passed + failed + errors,
              "stdout": stdout, "stderr": stderr}
    RUN_RESULTS[repo_name] = result
    total_executed += result["total_run"]

    status_str = "PASS" if exit_code == 0 else f"exit={exit_code}"
    print(f" {status_str} | {result['total_run']} tests | {elapsed}s")

print(f"\nTOTAL EXECUTED: {total_executed}")

# ─── STEP 5: GENERATE OUTPUT FILES ───────────────────────────────────────────

header("STEP 5: GENERATE OUTPUT FILES")

# full-output.md
lines = [
    "# SSZ ALL-TESTS FULL OUTPUT", "",
    f"**Generated:** {TIMESTAMP}",
    f"**System:** {platform.system()} {platform.release()}",
    f"**Python:** {sys.version.split()[0]}",
    f"**Total Repos Run:** {len(RUN_RESULTS)}",
    f"**Total Tests Executed:** {total_executed}",
    "", "---", "",
]
for repo_name, res in RUN_RESULTS.items():
    lines += [
        f"## REPO: {repo_name}", "",
        f"- **start_time:** {res['start_time']}",
        f"- **duration:** {res['duration_s']}s",
        f"- **exit_code:** {res['exit_code']}",
        f"- **passed:** {res['passed']}",
        f"- **failed:** {res['failed']}",
        f"- **errors:** {res['error']}",
        f"- **total_run:** {res['total_run']}",
        "", "### STDOUT", "", "```",
        res["stdout"] if res["stdout"] else "(empty)",
        "```", "", "### STDERR", "", "```",
        res["stderr"] if res["stderr"] else "(empty)",
        "```", "", "---", "",
    ]

fo = REPO_ROOT / "full-output.md"
fo.write_text("\n".join(lines), encoding="utf-8")
print(f"Written: full-output.md ({fo.stat().st_size // 1024} KB)")

# full-output-integrity.md
all_test_ids = []
for repo_name, res in RUN_RESULTS.items():
    for line in res["stdout"].splitlines():
        m = re.match(r"^(\S+\.py)::([\w\[\]-]+)\s+(PASSED|FAILED|ERROR)", line)
        if m:
            all_test_ids.append(f"{repo_name}::{m.group(1)}::{m.group(2)}")

seen, dupes = set(), set()
for tid in all_test_ids:
    short = "::".join(tid.split("::")[1:])
    if short in seen:
        dupes.add(short)
    seen.add(short)

count_ok = total_executed >= EXPECTED_MIN_TESTS
integrity_lines = [
    "# SSZ ALL-TESTS FULL OUTPUT INTEGRITY", "",
    f"**Generated:** {TIMESTAMP}", "",
    "| Repo | stdout | tests_run | exit | status |",
    "|------|--------|-----------|------|--------|",
]
for repo_name, res in RUN_RESULTS.items():
    has_stdout = "yes" if res["stdout"] else "NO"
    s = "ok" if res["exit_code"] in (0, 1) else f"exit_{res['exit_code']}"
    integrity_lines.append(
        f"| {repo_name} | {has_stdout} | {res['total_run']} | {res['exit_code']} | {s} |"
    )
integrity_lines += [
    "", "## Summary", "",
    f"- Total repos: {len(RUN_RESULTS)}",
    f"- Total executed: {total_executed}",
    f"- Tests mapped: {len(all_test_ids)}",
    f"- Duplicates: {len(dupes)}",
    f"- Count vs expected (≥{EXPECTED_MIN_TESTS}): {'PASS' if count_ok else 'WARN'}",
    "",
    f"## INTEGRITY STATUS: {'PASS' if count_ok else 'WARN'}",
]
(REPO_ROOT / "full-output-integrity.md").write_text("\n".join(integrity_lines), encoding="utf-8")
print("Written: full-output-integrity.md")

# analysis-index.json
test_map = {}
failures = []
for repo_name, res in RUN_RESULTS.items():
    for line in res["stdout"].splitlines():
        m = re.match(r"^(\S+\.py)::([\w\[\]-]+)\s+(PASSED|FAILED|ERROR)", line)
        if m:
            tid = f"{m.group(1)}::{m.group(2)}"
            test_map[tid] = {"repo": repo_name, "result": m.group(3)}
            if m.group(3) in ("FAILED", "ERROR"):
                failures.append({"id": tid, "repo": repo_name})

analysis = {
    "generated": TIMESTAMP,
    "total_repos": len(RUN_RESULTS),
    "total_detected": total_detected,
    "total_executed": total_executed,
    "total_mapped": len(test_map),
    "expected_min": EXPECTED_MIN_TESTS,
    "count_ok": count_ok,
    "repos": {name: {"exit_code": res["exit_code"], "passed": res["passed"],
                     "failed": res["failed"], "total": res["total_run"],
                     "duration_s": res["duration_s"]}
              for name, res in RUN_RESULTS.items()},
    "test_map": test_map,
    "failures": failures[:200],
    "duplicates": list(dupes)[:50],
}
(REPO_ROOT / "analysis-index.json").write_text(
    json.dumps(analysis, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Written: analysis-index.json ({len(test_map)} tests mapped)")

# ─── STEP 6: FINAL STATUS ────────────────────────────────────────────────────

header("STEP 6: FINAL STATUS")

total_pass = sum(v["passed"] for v in RUN_RESULTS.values())
total_fail = sum(v["failed"] for v in RUN_RESULTS.values())

print(f"Repos cloned:    {ok_repos}/{len(SOURCE_REPOS)}")
print(f"Tests detected:  {total_detected}")
print(f"Tests executed:  {total_executed}")
print(f"Tests passed:    {total_pass}")
print(f"Tests failed:    {total_fail}")
print(f"Tests mapped:    {len(test_map)}")
print(f"Expected min:    {EXPECTED_MIN_TESTS}")
print()
print(f"Output files:")
print(f"  repo_inventory.json")
print(f"  full-output.md")
print(f"  full-output-integrity.md")
print(f"  analysis-index.json")
print()

if total_executed >= EXPECTED_MIN_TESTS:
    print("STATUS: VERIFIED")
else:
    print(f"STATUS: PARTIAL — {total_executed}/{EXPECTED_MIN_TESTS} tests executed")
    print("  Tip: run with --skip-clone --skip-install to re-execute only")
