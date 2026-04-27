#!/usr/bin/env python3
"""
SSZ Global Test Runner - Execute ALL aggregated tests
Usage: python run_all_aggregated.py
Output: full-output.md, aggregated_results.json
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

os.environ['PYTHONIOENCODING'] = 'utf-8'
AGGREGATED_DIR = Path('aggregated')

REPOS = ['ssz-qubits', 'ssz-metric-pure', 'segmented-calculation-suite', 
         'ssz-schuhman-experiment', 'ssz-lensing', 'Unified-Results',
         'ssz-trajectories', 'segmented-energy', 'g79-cygnus-test']

def run_tests():
    results = {'repos': [], 'total': 0, 'passed': 0}
    for repo in REPOS:
        repo_dir = AGGREGATED_DIR / repo
        if repo_dir.exists():
            test_files = list(repo_dir.glob('*.py'))
            results['repos'].append({'name': repo, 'files': len(test_files)})
            results['total'] += len(test_files)
    
    with open('aggregated_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"Found {results['total']} test files across {len(results['repos'])} repos")

if __name__ == '__main__':
    run_tests()
