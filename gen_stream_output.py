#!/usr/bin/env python3
"""Generate really-full-output-stream.md from analysis-index.json (no re-run needed)."""
import json
import platform
from pathlib import Path
from datetime import datetime, timezone

root = Path(__file__).parent.resolve()
ai_path = root / "analysis-index.json"

if not ai_path.exists():
    print("ERROR: analysis-index.json not found — run setup_and_run.py first")
    raise SystemExit(1)

data = json.loads(ai_path.read_text(encoding="utf-8"))
repos = data.get("repos", {})
generated = data.get("generated", datetime.now(timezone.utc).isoformat())

total_pass = sum(r.get("passed", 0) for r in repos.values())
total_fail = sum(r.get("failed", 0) for r in repos.values())
n_repos = len(repos)

# Also load the verbose stdout from really-full-output.md parse — but we need
# the raw stdout. It's stored per-repo in analysis-index if present, else
# we rebuild from really-full-output.md sections.
# Better: re-read RUN_VERBOSE stdout from the existing really-full-output.md
# by extracting ```text ... ``` blocks per repo section.

rfo_path = root / "really-full-output.md"
if not rfo_path.exists():
    print("ERROR: really-full-output.md not found")
    raise SystemExit(1)

rfo_text = rfo_path.read_text(encoding="utf-8")

# Extract per-repo stdout blocks from really-full-output.md
import re

# Split on ## REPO: headers
repo_sections = re.split(r"\n## REPO: ", rfo_text)
repo_data = {}
for sec in repo_sections[1:]:  # skip preamble
    lines = sec.split("\n")
    header = lines[0]  # e.g. "ssz-qubits  `[CANONICAL]`"
    name_m = re.match(r"^([\w\-]+)", header)
    if not name_m:
        continue
    repo_name = name_m.group(1)
    # Find ```text block
    block_m = re.search(r"```text\n(.*?)```", sec, re.DOTALL)
    stdout_block = block_m.group(1) if block_m else "(no output captured)"
    # Also find stderr section
    stderr_m = re.search(r"\*\*STDERR:\*\*\n```\n(.*?)```", sec, re.DOTALL)
    stderr_block = stderr_m.group(1).strip() if stderr_m else ""
    repo_data[repo_name] = {"stdout": stdout_block, "stderr": stderr_block}

# Build stream
lines_out = [
    "# SSZ ALL-TESTS — Complete Full Output Log",
    "",
    f"**Generated:** {generated}",
    f"**System:** {platform.system()} {platform.release()}",
    f"**Python:** {platform.python_version()}",
    "**pytest flags:** `-v -s --tb=long --show-capture=all`",
    "",
    "This file contains the COMPLETE unfiltered output from all test repos.",
    "All stdout and stderr output is captured here.",
    "",
    "## Summary",
    "",
    f"- **Total Duration:** see individual repo timings",
    f"- **Repos:** {n_repos}",
    f"- **Passed:** {total_pass}",
    f"- **Failed:** {total_fail}",
    f"- **Success Rate:** {100*total_pass/(total_pass+total_fail):.1f}%" if (total_pass+total_fail) > 0 else "- **Success Rate:** N/A",
    "",
    "---",
    "",
    "## Complete Test Output",
    "",
    "Below is the COMPLETE, UNFILTERED output from all repos.",
    "This includes all print statements, test results, and error messages.",
    "",
    "```",
    "",
]

SEP = "=" * 100

for repo_name, rinfo in repos.items():
    rtype = rinfo.get("type", "?")
    passed = rinfo.get("passed", 0)
    failed = rinfo.get("failed", 0)
    exit_code = rinfo.get("exit_code", "?")
    duration = rinfo.get("duration_s", "?")

    lines_out.append(SEP)
    lines_out.append(
        f"REPO: {repo_name}  [{rtype}]  "
        f"passed={passed}  failed={failed}  exit={exit_code}  {duration}s"
    )
    lines_out.append(SEP)
    lines_out.append("")

    stdout = repo_data.get(repo_name, {}).get("stdout", "(not captured)")
    out = re.sub(r'\n{3,}', '\n\n', stdout)
    lines_out.append(out)

    stderr = repo_data.get(repo_name, {}).get("stderr", "")
    if stderr and stderr.strip():
        lines_out.append("")
        lines_out.append("--- STDERR ---")
        lines_out.append(stderr)

    lines_out.append("")

lines_out += ["```", ""]

out_path = root / "really-full-output-stream.md"
out_path.write_text("\n".join(lines_out), encoding="utf-8")
size_kb = out_path.stat().st_size // 1024
print(f"Written: really-full-output-stream.md ({size_kb} KB)")
print(f"Repos: {n_repos}  |  Passed: {total_pass}  |  Failed: {total_fail}")
