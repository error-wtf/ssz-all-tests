#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SSZ FULL OUTPUT PARSER
Extrahiert strukturierte Informationen aus dem Full-Output der Test-Suite.
Erzeugt: understanding-map.json, pattern-analysis.md
"""

import json
import re
from pathlib import Path
from datetime import datetime

BASE_DIR = Path("E:/clone/ssz-all-tests-test")
FULL_OUTPUT = BASE_DIR / "full-output.md"
OUTPUT_DIR = BASE_DIR / "UNDERSTANDING_SYNC"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def parse_full_output():
    if not FULL_OUTPUT.exists():
        print(f"ERROR: {FULL_OUTPUT} not found. Run run_all_live.py first.")
        return None

    text = FULL_OUTPUT.read_text(encoding='utf-8', errors='replace')

    # Extract test results
    tests = []
    for m in re.finditer(r'(PASSED|FAILED|ERROR)\s+(.+?)(?:\s+\[[\d.]+s\])?$', text, re.MULTILINE):
        tests.append({
            'status': m.group(1),
            'name': m.group(2).strip(),
        })

    # Extract repo sections
    repos = re.findall(r'## REPO: (.+?)$', text, re.MULTILINE)

    # Extract numerical values
    numbers = re.findall(r'(?:Xi|Ξ|phi|φ|D_min)\s*[=≈]\s*([\d.e+-]+)', text)

    summary = {
        'timestamp': datetime.now().isoformat(),
        'total_tests': len(tests),
        'passed': sum(1 for t in tests if t['status'] == 'PASSED'),
        'failed': sum(1 for t in tests if t['status'] == 'FAILED'),
        'repos': repos,
        'tests': tests[:200],  # first 200 for index
    }

    out = OUTPUT_DIR / 'understanding-map.json'
    out.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"Parsed: {len(tests)} tests from {len(repos)} repos → {out}")
    return summary


if __name__ == '__main__':
    parse_full_output()
