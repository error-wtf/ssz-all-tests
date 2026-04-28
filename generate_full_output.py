#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SSZ FULL OUTPUT GENERATOR - NO TRUNCATION
Captures EVERYTHING: all tests, all stdout, all stderr, all repos
"""

import subprocess
import sys
import os
import json
import time
from datetime import datetime
from pathlib import Path

os.environ['PYTHONIOENCODING'] = 'utf-8'

BASE_DIR = Path("E:/clone")
OUTPUT_DIR = BASE_DIR / "ssz-all-tests-test" / "COMPLETE_TEST_OUTPUTS_FINAL"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

REPOS = {
    "ssz-qubits": {"path": BASE_DIR / "ssz-qubits", "tests": "tests/"},
    "ssz-metric-pure": {"path": BASE_DIR / "ssz-metric-pure", "tests": "tests/"},
    "segmented-calculation-suite": {"path": BASE_DIR / "segmented-calculation-suite", "tests": ""},
    "ssz-schuhman-experiment": {"path": BASE_DIR / "ssz-schuhman-experiment", "tests": ""},
    "ssz-lagrange": {"path": BASE_DIR / "ssz-lagrange", "tests": ""},
    "ssz-lensing": {"path": BASE_DIR / "ssz-lensing", "tests": "tests/"},
    "Unified-Results": {"path": BASE_DIR / "Segmented-Spacetime-Mass-Projection-Unified-Results", "tests": "tests/"},
    "ssz-trajectories": {"path": BASE_DIR / "ssz-trajectories", "tests": ""},
    "segmented-energy": {"path": BASE_DIR / "segmented-energy", "tests": ""},
    "g79-cygnus-test": {"path": BASE_DIR / "g79-cygnus-test", "tests": ""},
}

def run_repo_full(repo_name, repo_info):
    """Run repo and capture EVERYTHING unfiltered"""
    print(f"\n{'='*80}")
    print(f"EXECUTING: {repo_name}")
    print(f"{'='*80}")
    
    path = repo_info["path"]
    test_dir = repo_info["tests"]
    
    if not path.exists():
        return {
            "repo": repo_name,
            "status": "MISSING",
            "stdout": "",
            "stderr": f"Path not found: {path}",
            "exit_code": -1
        }
    
    # Set PYTHONPATH
    env = os.environ.copy()
    env['PYTHONPATH'] = f"{path};{env.get('PYTHONPATH', '')}"
    
    # Determine test path
    if test_dir:
        test_path = str(path / test_dir)
    else:
        test_path = str(path)
    
    # Build command - verbose, show ALL output
    cmd = [
        sys.executable, "-m", "pytest",
        "-v",           # verbose
        "-s",           # show stdout
        "--tb=long",    # full tracebacks
        "--capture=no", # don't capture output
        test_path
    ]
    
    print(f"Command: {' '.join(cmd)}")
    print(f"Working Dir: {path}")
    print("-" * 80)
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',
            timeout=600,  # 10 minutes per repo
            cwd=str(path),
            env=env
        )
        
        print(f"Exit Code: {result.returncode}")
        print(f"Stdout Length: {len(result.stdout)} chars")
        print(f"Stderr Length: {len(result.stderr)} chars")
        
        return {
            "repo": repo_name,
            "status": "SUCCESS" if result.returncode == 0 else "FAILED",
            "exit_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "path": str(path)
        }
        
    except subprocess.TimeoutExpired:
        return {
            "repo": repo_name,
            "status": "TIMEOUT",
            "stdout": "",
            "stderr": "Execution timeout (600s)",
            "exit_code": -2
        }
    except Exception as e:
        return {
            "repo": repo_name,
            "status": "ERROR",
            "stdout": "",
            "stderr": str(e),
            "exit_code": -3
        }

def main():
    print("="*80)
    print("SSZ FULL OUTPUT GENERATOR - NO TRUNCATION")
    print("="*80)
    print(f"Start: {datetime.now().isoformat()}")
    print(f"Repos: {len(REPOS)}")
    print("="*80)
    
    all_results = []
    start_time = time.time()
    
    # Run ALL repos
    for repo_name, repo_info in REPOS.items():
        result = run_repo_full(repo_name, repo_info)
        all_results.append(result)
        
        # Also save individual repo output
        repo_file = OUTPUT_DIR / f"{repo_name}_full_output.txt"
        with open(repo_file, 'w', encoding='utf-8') as f:
            f.write(f"="*80 + "\n")
            f.write(f"REPO: {repo_name}\n")
            f.write(f"Status: {result['status']}\n")
            f.write(f"Exit Code: {result['exit_code']}\n")
            f.write(f"="*80 + "\n\n")
            f.write("STDOUT:\n")
            f.write("-"*80 + "\n")
            f.write(result['stdout'])
            f.write("\n\nSTDERR:\n")
            f.write("-"*80 + "\n")
            f.write(result['stderr'])
        
        print(f"Saved: {repo_file}")
    
    total_duration = time.time() - start_time
    
    # Create MASTER full-output.md with EVERYTHING
    master_file = OUTPUT_DIR / "full-output-complete.md"
    with open(master_file, 'w', encoding='utf-8') as f:
        f.write("# SSZ COMPLETE FULL OUTPUT - ALL REPOS, ALL TESTS, NO TRUNCATION\n\n")
        f.write(f"**Generated:** {datetime.now().isoformat()}\n")
        f.write(f"**Total Duration:** {total_duration:.1f}s\n")
        f.write(f"**System:** {os.name}\n")
        f.write(f"**Python:** {sys.version}\n")
        f.write(f"**Command:** `pytest -v -s --tb=long --capture=no`\n\n")
        
        f.write("="*80 + "\n")
        f.write("GLOBAL SUMMARY\n")
        f.write("="*80 + "\n\n")
        
        success_count = sum(1 for r in all_results if r['status'] == 'SUCCESS')
        f.write(f"- Total Repositories: {len(REPOS)}\n")
        f.write(f"- Successful: {success_count}\n")
        f.write(f"- Failed/Error: {len(REPOS) - success_count}\n\n")
        
        # EACH REPO - FULL OUTPUT
        for result in all_results:
            f.write("="*80 + "\n")
            f.write(f"REPO: {result['repo']}\n")
            f.write(f"Status: {result['status']}\n")
            f.write(f"Exit Code: {result['exit_code']}\n")
            f.write("="*80 + "\n\n")
            
            f.write("## STDOUT (COMPLETE - NO TRUNCATION)\n\n")
            f.write("```\n")
            f.write(result['stdout'])
            f.write("\n```\n\n")
            
            if result['stderr']:
                f.write("## STDERR (COMPLETE - NO TRUNCATION)\n\n")
                f.write("```\n")
                f.write(result['stderr'])
                f.write("\n```\n\n")
            
            f.write("\n---\n\n")
    
    # Also create analysis JSON
    json_file = OUTPUT_DIR / "full_output_analysis.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "duration": total_duration,
            "repos": len(REPOS),
            "results": [
                {
                    "repo": r["repo"],
                    "status": r["status"],
                    "exit_code": r["exit_code"],
                    "stdout_length": len(r["stdout"]),
                    "stderr_length": len(r["stderr"])
                }
                for r in all_results
            ]
        }, f, indent=2)
    
    print("\n" + "="*80)
    print("COMPLETE - ALL OUTPUTS SAVED")
    print("="*80)
    print(f"Master File: {master_file}")
    print(f"Size: {master_file.stat().st_size / 1024:.1f} KB")
    print(f"\nIndividual Repo Files:")
    for repo_name in REPOS.keys():
        repo_file = OUTPUT_DIR / f"{repo_name}_full_output.txt"
        if repo_file.exists():
            size_kb = repo_file.stat().st_size / 1024
            print(f"  {repo_file.name}: {size_kb:.1f} KB")
    print(f"\nAnalysis JSON: {json_file}")
    print("="*80)

if __name__ == "__main__":
    main()
