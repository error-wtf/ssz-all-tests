#!/usr/bin/env python3
"""Fix test files where literal \\n was stored instead of real newlines."""
from pathlib import Path
import re

broken = [
    "repos/ssz-full-metric/tests/test_energy_conditions.py",
    "repos/ssz-full-metric/tests/test_metric_core.py",
    "repos/ssz-full-metric/tests/test_ppn.py",
]

for fp_str in broken:
    fp = Path(fp_str)
    raw = fp.read_text(encoding="utf-8")
    lines_before = len(raw.splitlines())

    # Replace literal \n \t \r with real chars
    fixed = raw.replace("\\n", "\n").replace("\\t", "\t").replace("\\r", "\r")
    # Also fix escaped quotes if present
    fixed = fixed.replace('\\"', '"').replace("\\'", "'")

    lines_after = len(fixed.splitlines())
    print(f"{fp_str}: {lines_before} lines → {lines_after} lines")

    if lines_after > lines_before:
        fp.write_text(fixed, encoding="utf-8")
        print(f"  FIXED")
    else:
        print(f"  UNCHANGED (no improvement)")

# Also check ssz-paper-plots - find_data_directory missing
# Just create a minimal stub that makes the import work
pp = Path("repos/ssz-paper-plots")
master = pp / "generate_all_real_data_plots_master.py"
if master.exists():
    content = master.read_text(encoding="utf-8", errors="replace")
    if "find_data_directory" not in content:
        stub = '\n\ndef find_data_directory():\n    """Stub for missing function."""\n    import os\n    return os.getcwd()\n'
        master.write_text(content + stub, encoding="utf-8")
        print(f"ssz-paper-plots: added find_data_directory stub to {master.name}")

print("\nDone.")
