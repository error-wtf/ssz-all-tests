#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SSZ Global Test Runner - Execute ALL 87+ aggregated tests
=========================================================

Runs all aggregated tests from all repositories and generates full-output.md

Usage:
    python run_all_aggregated.py

Output:
    - full-output.md (complete test results)
    - aggregated_results.json (structured data)
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
import time

# UTF-8 for Windows
os.environ['PYTHONIOENCODING'] = 'utf-8'
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except:
        pass

AGGREGATED_DIR = Path('e:/clone/ssz-all-tests-test/aggregated')
OUTPUT_DIR = Path('e:/clone/ssz-all-tests-test')

REPOS = [
    'ssz-qubits',
    'ssz-metric-pure',
    'segmented-calculation-suite',
    'ssz-schuhman-experiment',
    'ssz-lensing',
    'Unified-Results',
    'ssz-trajectories',
    'segmented-energy',
    'g79-cygnus-test',
]


class TestRunner:
    def __init__(self):
        self.results = []
        self.start_time = None
        self.end_time = None
        self.total_passed = 0
        self.total_failed = 0
        self.total_errors = 0

    def run_tests_for_repo(self, repo_name):
        repo_dir = AGGREGATED_DIR / repo_name
        if not repo_dir.exists():
            return None

        test_files = list(repo_dir.glob('*.py'))
        if not test_files:
            return None

        print(f"\n{'='*80}")
        print(f"[REPO] {repo_name}")
        print(f"Tests: {len(test_files)} files")
        print(f"{'='*80}")

        repo_result = {
            'name': repo_name,
            'test_files': [],
            'total_tests': 0,
            'passed': 0,
            'failed': 0,
            'errors': 0,
            'start_time': datetime.now().isoformat(),
            'duration': 0
        }

        start = time.time()

        for test_file in sorted(test_files):
            file_result = self.run_single_test(test_file, repo_name)
            if file_result:
                repo_result['test_files'].append(file_result)
                repo_result['total_tests'] += file_result.get('tests', 0)
                repo_result['passed'] += file_result.get('passed', 0)
                repo_result['failed'] += file_result.get('failed', 0)
                repo_result['errors'] += file_result.get('errors', 0)

        repo_result['duration'] = time.time() - start
        repo_result['end_time'] = datetime.now().isoformat()

        self.total_passed += repo_result['passed']
        self.total_failed += repo_result['failed']
        self.total_errors += repo_result['errors']

        print(f"\n[SUMMARY] {repo_name}: {repo_result['passed']}/{repo_result['total_tests']} passed")

        return repo_result

    def run_single_test(self, test_file, repo_name):
        print(f"  Running: {test_file.name}")

        result = {
            'file': test_file.name,
            'tests': 0,
            'passed': 0,
            'failed': 0,
            'errors': 0,
            'stdout': '',
            'stderr': '',
            'exit_code': None
        }

        try:
            # Try pytest first
            cmd = [sys.executable, '-m', 'pytest', str(test_file), '-v', '--tb=short', '-x']
            process = subprocess.run(
                cmd,
                cwd=str(test_file.parent),
                capture_output=True,
                text=True,
                timeout=60,
                encoding='utf-8',
                errors='replace'
            )

            if process.returncode in [0, 1, 2, 3, 4, 5]:  # pytest exit codes
                result['stdout'] = process.stdout
                result['stderr'] = process.stderr
                result['exit_code'] = process.returncode

                # Parse pytest output
                if 'passed' in process.stdout:
                    import re
                    m = re.search(r'(\d+) passed', process.stdout)
                    if m:
                        result['passed'] = int(m.group(1))
                        result['tests'] = result['passed']

                    m = re.search(r'(\d+) failed', process.stdout)
                    if m:
                        result['failed'] = int(m.group(1))
                        result['tests'] += result['failed']

                    m = re.search(r'(\d+) error', process.stdout)
                    if m:
                        result['errors'] = int(m.group(1))
                        result['tests'] += result['errors']

                print(f"    -> {result['passed']}/{result['tests']} passed")
                return result

        except subprocess.TimeoutExpired:
            print(f"    -> TIMEOUT")
            result['errors'] = 1
            result['stderr'] = 'Timeout after 60s'
            return result

        except Exception as e:
            print(f"    -> ERROR: {e}")
            result['errors'] = 1
            result['stderr'] = str(e)
            return result

    def run_all(self):
        print("="*80)
        print("SSZ GLOBAL TEST RUNNER")
        print("="*80)
        print(f"Start: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Repositories: {len(REPOS)}")
        print("="*80)

        self.start_time = time.time()

        for repo in REPOS:
            repo_result = self.run_tests_for_repo(repo)
            if repo_result:
                self.results.append(repo_result)

        self.end_time = time.time()

        print("\n" + "="*80)
        print("GLOBAL RUN COMPLETE")
        print("="*80)
        print(f"Duration: {self.end_time - self.start_time:.1f}s")
        print(f"Total: {self.total_passed + self.total_failed + self.total_errors} tests")
        print(f"Passed: {self.total_passed}")
        print(f"Failed: {self.total_failed}")
        print(f"Errors: {self.total_errors}")

    def generate_full_output(self):
        output_file = OUTPUT_DIR / 'full-output.md'

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# SSZ Full Test Output\n\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n\n")

            f.write("## Summary\n\n")
            total = self.total_passed + self.total_failed + self.total_errors
            f.write(f"- **Total Tests:** {total}\n")
            f.write(f"- **Passed:** {self.total_passed}\n")
            f.write(f"- **Failed:** {self.total_failed}\n")
            f.write(f"- **Errors:** {self.total_errors}\n")
            f.write(f"- **Success Rate:** {100*self.total_passed/total if total > 0 else 0:.1f}%\n")
            f.write(f"- **Duration:** {self.end_time - self.start_time:.1f}s\n")
            f.write(f"- **Repositories:** {len(self.results)}\n\n")

            # Summary table
            f.write("## Summary by Repository\n\n")
            f.write("| Repository | Files | Tests | Passed | Failed | Errors | Duration |\n")
            f.write("|------------|-------|-------|--------|--------|--------|----------|\n")
            for r in self.results:
                files = len(r['test_files'])
                f.write(f"| {r['name']} | {files} | {r['total_tests']} | {r['passed']} | {r['failed']} | {r['errors']} | {r['duration']:.1f}s |\n")
            f.write("\n")

            # Detailed results
            for r in self.results:
                f.write(f"---\n\n## {r['name']}\n\n")
                f.write(f"**Files:** {len(r['test_files'])}\n")
                f.write(f"**Tests:** {r['total_tests']}\n")
                f.write(f"**Passed:** {r['passed']}\n")
                f.write(f"**Failed:** {r['failed']}\n")
                f.write(f"**Duration:** {r['duration']:.1f}s\n\n")

                for tf in r['test_files']:
                    f.write(f"### {tf['file']}\n\n")
                    f.write(f"Status: {'PASS' if tf['failed'] == 0 and tf['errors'] == 0 else 'FAIL'}\n")
                    f.write(f"Tests: {tf['tests']}\n")
                    f.write(f"Passed: {tf['passed']}, Failed: {tf['failed']}, Errors: {tf['errors']}\n\n")

                    if tf['stdout']:
                        f.write("Output:\n```\n")
                        stdout = tf['stdout'][-3000:] if len(tf['stdout']) > 3000 else tf['stdout']
                        f.write(stdout)
                        f.write("\n```\n\n")

                    if tf['stderr']:
                        f.write("Errors:\n```\n")
                        stderr = tf['stderr'][-1500:] if len(tf['stderr']) > 1500 else tf['stderr']
                        f.write(stderr)
                        f.write("\n```\n\n")

        print(f"\n[OUTPUT] full-output.md written")

    def save_json(self):
        json_file = OUTPUT_DIR / 'aggregated_results.json'
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump({
                'metadata': {
                    'generated': datetime.now().isoformat(),
                    'duration': self.end_time - self.start_time,
                    'total_tests': self.total_passed + self.total_failed + self.total_errors,
                    'passed': self.total_passed,
                    'failed': self.total_failed,
                    'errors': self.total_errors
                },
                'results': self.results
            }, f, indent=2)
        print(f"[OUTPUT] aggregated_results.json written")


def main():
    runner = TestRunner()
    runner.run_all()
    runner.generate_full_output()
    runner.save_json()

    print("\n" + "="*80)
    print("ALL OUTPUTS GENERATED")
    print("="*80)
    print("- full-output.md (complete results)")
    print("- aggregated_results.json (structured data)")


if __name__ == '__main__':
    main()
