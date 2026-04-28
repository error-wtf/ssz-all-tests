#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SSZ ABSOLUTE FULL OUTPUT GENERATOR
Wirklich ALLE 1100+ Tests aus ALLEN Repos in EINEM ungekürzten Output.
Keine Filter. Keine Zusammenfassungen. 100% komplett.

Repositories (10):
1. ssz-qubits (184 tests)
2. ssz-metric-pure (46 tests)
3. segmented-calculation-suite (158 tests)
4. ssz-schuhman-experiment (191 tests)
5. ssz-lagrange (54 tests)
6. ssz-lensing (279 tests)
7. Unified-Results (139 tests)
8. ssz-trajectories (63 tests)
9. segmented-energy (6 tests)
10. g79-cygnus-test (5 tests)

Expected: 1125+ tests
"""

import subprocess
import sys
import os
import json
import time
from datetime import datetime
from pathlib import Path

os.environ['PYTHONIOENCODING'] = 'utf-8'
os.environ['PYTHONUTF8'] = '1'

BASE_DIR = Path("E:/clone")
OUTPUT_FILE = BASE_DIR / "ssz-all-tests-test" / "FULL_OUTPUT_1100_TESTS.md"
JSON_FILE = BASE_DIR / "ssz-all-tests-test" / "ALL_TEST_DATA.json"

# ALLE Repositories
REPOS = [
    ("ssz-qubits", BASE_DIR / "ssz-qubits", "pytest tests/ -v --tb=long 2>&1"),
    ("ssz-metric-pure", BASE_DIR / "ssz-metric-pure", "pytest tests/ -v --tb=long 2>&1"),
    ("segmented-calculation-suite", BASE_DIR / "segmented-calculation-suite", "pytest -v --tb=long 2>&1"),
    ("ssz-schuhman-experiment", BASE_DIR / "ssz-schuhman-experiment", "pytest -v --tb=long 2>&1"),
    ("ssz-lagrange", BASE_DIR / "ssz-lagrange", "pytest -v --tb=long 2>&1"),
    ("ssz-lensing", BASE_DIR / "ssz-lensing", "pytest tests/ -v --tb=long 2>&1"),
    ("Unified-Results", BASE_DIR / "Segmented-Spacetime-Mass-Projection-Unified-Results", "pytest tests/ -v --tb=long 2>&1"),
    ("ssz-trajectories", BASE_DIR / "ssz-trajectories", "pytest -v --tb=long 2>&1"),
    ("segmented-energy", BASE_DIR / "segmented-energy", "pytest -v --tb=long 2>&1"),
    ("g79-cygnus-test", BASE_DIR / "g79-cygnus-test", "pytest -v --tb=long 2>&1"),
]

def run_repo(repo_name, repo_path, cmd_str):
    """Führe Repo aus und capture 100% des Outputs"""
    
    print(f"\n{'='*80}")
    print(f"RUNNING: {repo_name}")
    print(f"Path: {repo_path}")
    print(f"{'='*80}\n")
    
    if not repo_path.exists():
        return {
            "repo": repo_name,
            "status": "PATH_NOT_FOUND",
            "stdout": "",
            "stderr": f"Repository not found: {repo_path}",
            "exit_code": -1
        }
    
    env = os.environ.copy()
    env['PYTHONPATH'] = f"{repo_path};{env.get('PYTHONPATH', '')}"
    
    start_time = time.time()
    
    try:
        # Split command
        if 'tests/' in cmd_str:
            cmd = [sys.executable, "-m", "pytest", "tests/", "-v", "--tb=long"]
        else:
            cmd = [sys.executable, "-m", "pytest", "-v", "--tb=long"]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',
            timeout=600,
            cwd=str(repo_path),
            env=env
        )
        
        duration = time.time() - start_time
        
        return {
            "repo": repo_name,
            "status": "SUCCESS" if result.returncode == 0 else "FAILED",
            "exit_code": result.returncode,
            "duration": duration,
            "stdout": result.stdout,
            "stderr": result.stderr
        }
        
    except subprocess.TimeoutExpired:
        return {
            "repo": repo_name,
            "status": "TIMEOUT",
            "duration": 600,
            "stdout": "",
            "stderr": "Execution timeout after 600 seconds"
        }
    except Exception as e:
        return {
            "repo": repo_name,
            "status": "ERROR",
            "stdout": "",
            "stderr": str(e)
        }

def main():
    global_start = time.time()
    
    print("="*80)
    print("SSZ ABSOLUTE FULL OUTPUT GENERATOR")
    print("Capturing ALL 1100+ Tests from ALL Repositories")
    print("="*80)
    print(f"Start: {datetime.now().isoformat()}")
    print(f"Expected Tests: 1125+")
    print(f"Repositories: {len(REPOS)}")
    print("="*80)
    
    all_results = []
    
    # Führe ALLE Repos aus
    for repo_name, repo_path, cmd in REPOS:
        result = run_repo(repo_name, repo_path, cmd)
        all_results.append(result)
        
        # Sofort in File schreiben (append mode)
        if not OUTPUT_FILE.exists():
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                f.write("# SSZ ABSOLUTE FULL OUTPUT - ALL 1100+ TESTS\n\n")
                f.write(f"**Generated:** {datetime.now().isoformat()}\n")
                f.write(f"**Command:** pytest -v --tb=long\n\n")
        
        # Append dieses Repo
        with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
            f.write(f"\n{'='*80}\n")
            f.write(f"REPO: {repo_name}\n")
            f.write(f"{'='*80}\n\n")
            f.write(f"**Status:** {result['status']}\n")
            f.write(f"**Exit Code:** {result.get('exit_code', 'N/A')}\n")
            f.write(f"**Duration:** {result.get('duration', 0):.1f}s\n\n")
            
            if result['stdout']:
                f.write("## STDOUT (COMPLETE - NO FILTER)\n\n")
                f.write("```\n")
                f.write(result['stdout'])
                f.write("\n```\n\n")
            
            if result['stderr']:
                f.write("## STDERR (COMPLETE)\n\n")
                f.write("```\n")
                f.write(result['stderr'])
                f.write("\n```\n\n")
        
        print(f"  -> Saved output for {repo_name}")
    
    total_duration = time.time() - global_start
    
    # JSON Output
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "total_duration": total_duration,
            "total_repos": len(REPOS),
            "results": all_results
        }, f, indent=2, ensure_ascii=False)
    
    # Final Summary in Markdown
    with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
        f.write("\n" + "="*80 + "\n")
        f.write("GLOBAL SUMMARY\n")
        f.write("="*80 + "\n\n")
        
        f.write(f"- **Total Duration:** {total_duration:.1f}s\n")
        f.write(f"- **Repositories:** {len(REPOS)}\n")
        f.write(f"- **Output File:** {OUTPUT_FILE}\n")
        f.write(f"- **JSON File:** {JSON_FILE}\n\n")
        
        f.write("| Repo | Status | Duration |\n")
        f.write("|------|--------|----------|\n")
        for r in all_results:
            f.write(f"| {r['repo']} | {r['status']} | {r.get('duration', 0):.1f}s |\n")
    
    print("\n" + "="*80)
    print("COMPLETE - ALL OUTPUTS SAVED")
    print("="*80)
    print(f"Full Output: {OUTPUT_FILE}")
    print(f"  Size: {OUTPUT_FILE.stat().st_size / 1024 / 1024:.1f} MB")
    print(f"JSON Data: {JSON_FILE}")
    print("="*80)

if __name__ == "__main__":
    main()
