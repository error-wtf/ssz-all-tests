#!/usr/bin/env python3
"""
SSZ Test Aggregator - Copy tests with source headers
Usage: python aggregate_tests.py
"""

import os
from pathlib import Path
from datetime import datetime

REPOS = [
    {'name': 'ssz-qubits', 'path': 'e:/clone/ssz-qubits', 'test_dirs': ['tests']},
    {'name': 'ssz-metric-pure', 'path': 'e:/clone/ssz-metric-pure', 'test_dirs': ['tests']},
]

OUTPUT_BASE = Path('aggregated')

def create_header(repo_name, original_path):
    return f'''# SOURCE: {repo_name}
# ORIGINAL PATH: {original_path}
# AGGREGATED: {datetime.now().isoformat()}
# This file was automatically aggregated from the SSZ repository.

'''

def main():
    print("SSZ Test Aggregation")
    for repo in REPOS:
        print(f"Processing: {repo['name']}")
        output_dir = OUTPUT_BASE / repo['name']
        output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Output: {OUTPUT_BASE}")

if __name__ == '__main__':
    main()
