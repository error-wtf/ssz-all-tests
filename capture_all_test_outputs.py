#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SSZ COMPLETE TEST OUTPUT CAPTURE
Runs ALL 1150+ aggregated tests and captures EVERYTHING
"""

import subprocess
import sys
import json
import os
from pathlib import Path
from datetime import datetime
import time

# UTF-8 for Windows
os.environ['PYTHONIOENCODING'] = 'utf-8:replace'

BASE_DIR = Path("E:/clone/ssz-all-tests-test")
AGGREGATED_DIR = BASE_DIR / "aggregated"
OUTPUT_DIR = BASE_DIR / "COMPLETE_TEST_OUTPUTS"
OUTPUT_DIR.mkdir(exist_ok=True)

# All test directories with expected test counts
TEST_REPOS = [
    ("ssz-qubits", 27),
    ("ssz-metric-pure", 36),
    ("segmented-calculation-suite", 158),
    ("ssz-schuhman-experiment", 191),
    ("ssz-lagrange", 54),  # NEW
    ("ssz-lensing", 279),
    ("Unified-Results", 48),  # 40 + 8
    ("ssz-trajectories", 63),
    ("segmented-energy", 6),
    ("g79-cygnus-test", 5),
]


def run_test_file(test_file, repo_name):
    """Run a single test file and capture all output"""
    print(f"\n{'='*70}")
    print(f"Running: {repo_name}/{test_file.name}")
    print(f"{'='*70}")
    
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(test_file), "-v", "--tb=long", "-s"],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',
            timeout=300,  # 5 minute timeout per file
            cwd=str(AGGREGATED_DIR / repo_name)
        )
        
        output = {
            "file": test_file.name,
            "repo": repo_name,
            "exit_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "passed": result.returncode == 0,
        }
        
        # Print preview
        print(result.stdout[:2000] if len(result.stdout) > 2000 else result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr[:500])
        
        return output
        
    except subprocess.TimeoutExpired:
        return {"file": test_file.name, "repo": repo_name, "error": "TIMEOUT"}
    except Exception as e:
        return {"file": test_file.name, "repo": repo_name, "error": str(e)}


def run_all_tests():
    """Run ALL aggregated tests and capture outputs"""
    all_results = []
    total_tests = 0
    total_passed = 0
    
    start_time = time.time()
    
    for repo_name, expected_tests in TEST_REPOS:
        repo_dir = AGGREGATED_DIR / repo_name
        
        if not repo_dir.exists():
            print(f"⚠️  {repo_name}: Directory not found")
            continue
        
        print(f"\n{'#'*70}")
        print(f"# REPOSITORY: {repo_name} (expected: {expected_tests} tests)")
        print(f"{'#'*70}")
        
        # Find all test files
        test_files = list(repo_dir.glob("test*.py"))
        
        for test_file in test_files:
            result = run_test_file(test_file, repo_name)
            all_results.append(result)
            
            if result.get("passed"):
                total_passed += 1
            total_tests += 1
    
    duration = time.time() - start_time
    
    # Save complete results
    summary = {
        "timestamp": datetime.now().isoformat(),
        "duration": duration,
        "total_test_files": total_tests,
        "passed": total_passed,
        "failed": total_tests - total_passed,
        "results": all_results
    }
    
    # Save as JSON
    json_path = OUTPUT_DIR / "complete_test_results.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    # Save as Markdown
    md_path = OUTPUT_DIR / "ALL_TEST_OUTPUTS_COMPLETE.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# SSZ COMPLETE TEST OUTPUTS\n\n")
        f.write(f"**Generated:** {summary['timestamp']}\n")
        f.write(f"**Duration:** {duration:.1f}s\n")
        f.write(f"**Test Files:** {total_tests}\n")
        f.write(f"**Passed:** {total_passed}\n")
        f.write(f"**Failed:** {total_tests - total_passed}\n\n")
        
        for result in all_results:
            f.write(f"## {result['repo']}/{result['file']}\n\n")
            
            if "error" in result:
                f.write(f"**ERROR:** {result['error']}\n\n")
            else:
                f.write(f"**Exit Code:** {result['exit_code']}\n")
                f.write(f"**Status:** {'✅ PASS' if result['passed'] else '❌ FAIL'}\n\n")
                f.write("### STDOUT\n\n```\n")
                f.write(result['stdout'])
                f.write("\n```\n\n")
                
                if result['stderr']:
                    f.write("### STDERR\n\n```\n")
                    f.write(result['stderr'])
                    f.write("\n```\n\n")
            
            f.write("---\n\n")
    
    print(f"\n{'='*70}")
    print("COMPLETE! Results saved to:")
    print(f"  JSON: {json_path}")
    print(f"  Markdown: {md_path}")
    print(f"{'='*70}")
    
    return summary


if __name__ == "__main__":
    print("="*70)
    print("SSZ COMPLETE TEST OUTPUT CAPTURE")
    print("Running ALL 1150+ tests with full output capture")
    print("="*70)
    
    results = run_all_tests()
    
    print(f"\nSUMMARY:")
    print(f"  Test Files: {results['total_test_files']}")
    print(f"  Passed: {results['passed']}")
    print(f"  Failed: {results['failed']}")
    print(f"  Duration: {results['duration']:.1f}s")
