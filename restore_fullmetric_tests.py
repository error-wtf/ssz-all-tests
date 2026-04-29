#!/usr/bin/env python3
"""Restore broken ssz-full-metric test files from GitHub raw content."""
import urllib.request
from pathlib import Path

files = {
    "repos/ssz-full-metric/tests/test_ppn.py":
        "https://raw.githubusercontent.com/error-wtf/ssz-full-metric/master/tests/test_ppn.py",
    "repos/ssz-full-metric/tests/test_energy_conditions.py":
        "https://raw.githubusercontent.com/error-wtf/ssz-full-metric/master/tests/test_energy_conditions.py",
    "repos/ssz-full-metric/tests/test_metric_core.py":
        "https://raw.githubusercontent.com/error-wtf/ssz-full-metric/master/tests/test_metric_core.py",
}

for local, url in files.items():
    fp = Path(local)
    with urllib.request.urlopen(url) as resp:
        content = resp.read().decode("utf-8")
    fp.write_text(content, encoding="utf-8")
    lines = len(content.splitlines())
    print(f"Restored {local}: {lines} lines")

print("Done.")
