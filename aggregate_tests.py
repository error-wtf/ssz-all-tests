#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SSZ Test Aggregator - Copy all tests to ssz-all-tests-test
===========================================================
"""

import os
from pathlib import Path
from datetime import datetime

REPOS = [
    {'name': 'ssz-qubits', 'path': 'e:/clone/ssz-qubits', 'test_dirs': ['tests']},
    {'name': 'ssz-metric-pure', 'path': 'e:/clone/ssz-metric-pure', 'test_dirs': ['tests']},
    {'name': 'segmented-calculation-suite', 'path': 'e:/clone/segmented-calculation-suite', 'test_dirs': ['tests', 'segcalc/tests']},
    {'name': 'ssz-schuhman-experiment', 'path': 'e:/clone/ssz-schuhman-experiment', 'test_dirs': ['tests']},
    {'name': 'ssz-lensing', 'path': 'e:/clone/ssz-lensing', 'test_dirs': ['tests']},
    {'name': 'Unified-Results', 'path': 'e:/clone/Segmented-Spacetime-Mass-Projection-Unified-Results', 'test_dirs': ['tests', 'scripts/tests']},
    {'name': 'ssz-trajectories', 'path': 'e:/clone/ssz-trajectories', 'test_dirs': ['tests']},
    {'name': 'segmented-energy', 'path': 'e:/clone/segmented-energy', 'test_dirs': ['.']},
    {'name': 'g79-cygnus-test', 'path': 'e:/clone/g79-cygnus-test', 'test_dirs': ['.']},
]

OUTPUT_BASE = Path('e:/clone/ssz-all-tests-test')


def create_header(repo_name, original_path):
    return f'''# -*- coding: utf-8 -*-
# =============================================================================
# SOURCE: {repo_name}
# ORIGINAL PATH: {original_path}
# AGGREGATED: {datetime.now().isoformat()}
# =============================================================================
# This file was automatically aggregated from the SSZ repository.
# Do not modify - changes will be lost on next aggregation.
# =============================================================================

'''


def find_test_files(repo_path, test_dirs):
    test_files = []
    repo = Path(repo_path)

    for test_dir in test_dirs:
        full_path = repo / test_dir
        if not full_path.exists():
            continue

        for py_file in full_path.rglob('*.py'):
            name = py_file.name
            if name.startswith('test_') or name.startswith('TEST'):
                test_files.append(py_file)

    return test_files


def copy_with_header(src, dest_dir, repo_name):
    try:
        dest = dest_dir / src.name

        counter = 1
        original_dest = dest
        while dest.exists():
            stem = original_dest.stem
            suffix = original_dest.suffix
            dest = original_dest.parent / f"{stem}_{counter}{suffix}"
            counter += 1

        with open(src, 'r', encoding='utf-8', errors='replace') as f:
            original_content = f.read()

        with open(dest, 'w', encoding='utf-8') as f:
            f.write(create_header(repo_name, str(src)))
            f.write(original_content)

        return True

    except Exception as e:
        print(f"  [ERROR] {src}: {e}")
        return False


def main():
    print("=" * 80)
    print("SSZ TEST AGGREGATION")
    print("=" * 80)

    total_files = 0
    copied_files = 0

    for repo in REPOS:
        repo_name = repo['name']
        repo_path = repo['path']

        print(f"\n[REPO] {repo_name}")

        if not Path(repo_path).exists():
            print(f"  [SKIP] Not found: {repo_path}")
            continue

        output_dir = OUTPUT_BASE / 'aggregated' / repo_name
        output_dir.mkdir(parents=True, exist_ok=True)

        test_files = find_test_files(repo_path, repo['test_dirs'])
        print(f"  Found: {len(test_files)} files")

        for test_file in test_files:
            total_files += 1
            if copy_with_header(test_file, output_dir, repo_name):
                copied_files += 1
                print(f"  [OK] {test_file.name}")

    print("\n" + "=" * 80)
    print("AGGREGATION COMPLETE")
    print("=" * 80)
    print(f"Total found: {total_files}")
    print(f"Copied: {copied_files}")
    print(f"Output: {OUTPUT_BASE / 'aggregated'}")

    manifest = OUTPUT_BASE / 'aggregated' / 'MANIFEST.md'
    with open(manifest, 'w', encoding='utf-8') as f:
        f.write("# SSZ Test Aggregation Manifest\n\n")
        f.write(f"Generated: {datetime.now().isoformat()}\n\n")
        f.write("## Repositories\n\n")
        for repo in REPOS:
            repo_dir = OUTPUT_BASE / 'aggregated' / repo['name']
            if repo_dir.exists():
                count = len(list(repo_dir.glob('*.py')))
                f.write(f"- **{repo['name']}**: {count} files\n")
        f.write(f"\n## Total\n\n{copied_files} test files aggregated\n")

    print(f"[MANIFEST] {manifest}")


if __name__ == '__main__':
    main()
