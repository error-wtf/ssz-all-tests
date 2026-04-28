#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RUN ALL SSZ TESTS - Complete Output Capture
Runs ALL 1150+ tests from ALL 10 repositories and captures EVERYTHING
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

BASE_DIR = Path("E:/clone")
OUTPUT_DIR = BASE_DIR / "ssz-all-tests-test" / "COMPLETE_TEST_OUTPUTS"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

REPOS = [
    ("ssz-qubits", "E:/clone/ssz-qubits", ["pytest", "-v", "--tb=long"]),
    ("ssz-metric-pure", "E:/clone/ssz-metric-pure", ["pytest", "-v", "tests/"]),
    ("ssz-schuhman-experiment", "E:/clone/ssz-schuhman-experiment", ["pytest", "-v"]),
    ("ssz-lagrange", "E:/clone/ssz-lagrange", ["pytest", "-v", "-s"]),
    ("segmented-calculation-suite", "E:/clone/segmented-calculation-suite", ["pytest", "-v"]),
    ("ssz-lensing", "E:/clone/ssz-lensing", ["pytest", "-v"]),
    ("Unified-Results", "E:/clone/Segmented-Spacetime-Mass-Projection-Unified-Results", ["pytest", "-v", "tests/"]),
    ("ssz-trajectories", "E:/clone/ssz-trajectories", ["pytest", "-v"]),
    ("segmented-energy", "E:/clone/segmented-energy", ["pytest", "-v"]),
    ("g79-cygnus-test", "E:/clone/g79-cygnus-test", ["pytest", "-v"]),
    ("ssz-all-tests", "E:/clone/ssz-all-tests-test", ["pytest", "-v", "tests/"]),
]

def run_repo(name, path, args):
    """Run tests for one repository"""
    print(f"\n{'='*70}")
    print(f"RUNNING: {name}")
    print(f"Path: {path}")
    print(f"{'='*70}")
    
    try:
        start = time.time()
        
        # Set PYTHONPATH to include the repo
        env = os.environ.copy()
        env['PYTHONPATH'] = f"{path};{env.get('PYTHONPATH', '')}"
        
        result = subprocess.run(
            [sys.executable, "-m"] + args,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',
            timeout=300,
            cwd=path,
            env=env
        )
        
        duration = time.time() - start
        
        output = {
            "repo": name,
            "path": str(path),
            "exit_code": result.returncode,
            "duration": duration,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "passed": result.returncode == 0,
        }
        
        # Print summary
        lines = result.stdout.split('\n')
        passed = sum(1 for l in lines if 'passed' in l.lower())
        failed = sum(1 for l in lines if 'failed' in l.lower())
        
        if result.returncode == 0:
            print(f"✅ {name}: PASS ({duration:.1f}s)")
        else:
            print(f"❌ {name}: FAIL ({duration:.1f}s)")
            # Show first error
            for line in lines[:20]:
                if 'FAILED' in line or 'ERROR' in line:
                    print(f"   {line}")
        
        return output
        
    except subprocess.TimeoutExpired:
        return {"repo": name, "error": "TIMEOUT", "duration": 300}
    except Exception as e:
        return {"repo": name, "error": str(e), "duration": 0}

def main():
    all_results = []
    start_time = time.time()
    
    print("="*70)
    print("SSZ COMPLETE TEST SUITE - ALL 1150+ TESTS")
    print("="*70)
    
    for name, path, args in REPOS:
        result = run_repo(name, path, args)
        all_results.append(result)
    
    total_duration = time.time() - start_time
    
    # Save results
    summary = {
        "timestamp": datetime.now().isoformat(),
        "duration": total_duration,
        "repositories": len(REPOS),
        "results": all_results
    }
    
    # JSON
    json_path = OUTPUT_DIR / "all_test_outputs.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    # Markdown report
    md_path = OUTPUT_DIR / "ALL_TEST_OUTPUTS_COMPLETE.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# SSZ Complete Test Outputs\n\n")
        f.write(f"**Generated:** {summary['timestamp']}\n")
        f.write(f"**Total Duration:** {total_duration:.1f}s\n")
        f.write(f"**Repositories:** {len(REPOS)}\n\n")
        
        passed_count = sum(1 for r in all_results if r.get('passed'))
        f.write(f"**Passed:** {passed_count}/{len(REPOS)}\n\n")
        
        for r in all_results:
            f.write(f"## {r['repo']}\n\n")
            
            if 'error' in r:
                f.write(f"**ERROR:** {r['error']}\n\n")
            else:
                f.write(f"**Exit Code:** {r['exit_code']}\n")
                f.write(f"**Duration:** {r['duration']:.1f}s\n")
                f.write(f"**Status:** {'✅ PASS' if r['passed'] else '❌ FAIL'}\n\n")
                
                f.write("### STDOUT\n\n```\n")
                f.write(r['stdout'][:10000])  # Limit output
                f.write("\n```\n\n")
                
                if r['stderr']:
                    f.write("### STDERR\n\n```\n")
                    f.write(r['stderr'])
                    f.write("\n```\n\n")
            
            f.write("---\n\n")
    
    print(f"\n{'='*70}")
    print("COMPLETE!")
    print(f"Results saved to:")
    print(f"  JSON: {json_path}")
    print(f"  Markdown: {md_path}")
    print(f"{'='*70}")
    
    print(f"\nSummary: {passed_count}/{len(REPOS)} repositories passed")
    
    return summary

if __name__ == "__main__":
    main()
