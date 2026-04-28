#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SSZ COMPLETE TEST RUNNER - Full Output with Integrity Check
Führt ALLE 1100+ Tests aus allen Repositories aus
Erstellt: full-output.md, integrity-check.md, analysis-index.json

STRICT: Kein Skip, keine Simulation, keine Kürzung
"""

import subprocess
import sys
import json
import os
import time
from datetime import datetime
from pathlib import Path
import shutil

os.environ['PYTHONIOENCODING'] = 'utf-8'

BASE_DIR = Path("E:/clone")
OUTPUT_DIR = BASE_DIR / "ssz-all-tests-test" / "COMPLETE_TEST_OUTPUTS_FINAL"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

REPOS = {
    "ssz-qubits": {"path": BASE_DIR / "ssz-qubits", "tests": "tests/", "expected": 184},
    "ssz-metric-pure": {"path": BASE_DIR / "ssz-metric-pure", "tests": "tests/", "expected": 46},
    "ssz-schuhman-experiment": {"path": BASE_DIR / "ssz-schuhman-experiment", "tests": "", "expected": 191},
    "ssz-lagrange": {"path": BASE_DIR / "ssz-lagrange", "tests": "", "expected": 54},
    "segmented-calculation-suite": {"path": BASE_DIR / "segmented-calculation-suite", "tests": "", "expected": 158},
    "ssz-lensing": {"path": BASE_DIR / "ssz-lensing", "tests": "tests/", "expected": 279},
    "Unified-Results": {"path": BASE_DIR / "Segmented-Spacetime-Mass-Projection-Unified-Results", "tests": "tests/", "expected": 139},
    "ssz-trajectories": {"path": BASE_DIR / "ssz-trajectories", "tests": "", "expected": 63},
    "segmented-energy": {"path": BASE_DIR / "segmented-energy", "tests": "", "expected": 6},
    "g79-cygnus-test": {"path": BASE_DIR / "g79-cygnus-test", "tests": "", "expected": 5},
}

def run_repo(repo_name, repo_info):
    """Führe ein Repository aus und capture alles"""
    print(f"\n{'='*70}")
    print(f"REPO: {repo_name}")
    print(f"{'='*70}")
    
    path = repo_info["path"]
    test_dir = repo_info["tests"]
    
    if not path.exists():
        return {
            "repo": repo_name,
            "status": "MISSING",
            "error": f"Path not found: {path}"
        }
    
    start_time = time.time()
    
    # Setze PYTHONPATH
    env = os.environ.copy()
    env['PYTHONPATH'] = f"{path};{BASE_DIR / 'ssz-all-tests-test'};{env.get('PYTHONPATH', '')}"
    
    # Bestimme Test-Pfad
    if test_dir:
        test_path = str(path / test_dir)
    else:
        test_path = str(path)
    
    # Führe Tests aus
    cmd = [sys.executable, "-m", "pytest", "-v", "--tb=long", test_path]
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',
            timeout=300,
            cwd=str(path),
            env=env
        )
        
        duration = time.time() - start_time
        
        # Parse Ergebnisse
        stdout = result.stdout
        stderr = result.stderr
        
        # Zähle Tests
        passed = stdout.count("PASSED")
        failed = stdout.count("FAILED")
        errors = stdout.count("ERROR")
        
        # Suche nach gesamter Test-Anzahl
        total_tests = passed + failed + errors
        for line in stdout.split('\n'):
            if 'passed' in line and 'failed' in line:
                # Extrahiere Gesamtzahl
                parts = line.split()
                for i, part in enumerate(parts):
                    if part.isdigit():
                        total_tests = int(part)
                        break
        
        print(f"  Duration: {duration:.1f}s")
        print(f"  Exit Code: {result.returncode}")
        print(f"  Tests: {passed} passed, {failed} failed, {errors} errors")
        
        return {
            "repo": repo_name,
            "status": "SUCCESS" if result.returncode == 0 else "FAILED",
            "exit_code": result.returncode,
            "duration": duration,
            "passed": passed,
            "failed": failed,
            "errors": errors,
            "total_tests": total_tests,
            "stdout": stdout,
            "stderr": stderr,
            "expected": repo_info["expected"]
        }
        
    except subprocess.TimeoutExpired:
        return {
            "repo": repo_name,
            "status": "TIMEOUT",
            "duration": 300,
            "error": "Execution timeout"
        }
    except Exception as e:
        return {
            "repo": repo_name,
            "status": "ERROR",
            "error": str(e)
        }

def main():
    print("="*70)
    print("SSZ COMPLETE TEST RUNNER - FULL OUTPUT")
    print("="*70)
    print(f"Start: {datetime.now().isoformat()}")
    print(f"Expected Tests: 1128+")
    print(f"Repositories: {len(REPOS)}")
    print("="*70)
    
    all_results = []
    start_time = time.time()
    
    # Führe alle Repos aus
    for repo_name, repo_info in REPOS.items():
        result = run_repo(repo_name, repo_info)
        all_results.append(result)
    
    total_duration = time.time() - start_time
    
    # Berechne Gesamtsummen
    total_passed = sum(r.get("passed", 0) for r in all_results)
    total_failed = sum(r.get("failed", 0) for r in all_results)
    total_errors = sum(r.get("errors", 0) for r in all_results)
    total_tests = sum(r.get("total_tests", 0) for r in all_results)
    
    # Erstelle FULL OUTPUT
    full_output_file = OUTPUT_DIR / "full-output.md"
    with open(full_output_file, 'w', encoding='utf-8') as f:
        f.write("# SSZ COMPLETE TEST OUTPUT\n\n")
        f.write(f"**Generated:** {datetime.now().isoformat()}\n")
        f.write(f"**Total Duration:** {total_duration:.1f}s\n")
        f.write(f"**System:** {os.name}\n")
        f.write(f"**Python:** {sys.version}\n\n")
        
        f.write("## GLOBAL SUMMARY\n\n")
        f.write(f"- Total Repositories: {len(REPOS)}\n")
        f.write(f"- Total Tests: {total_tests}\n")
        f.write(f"- Passed: {total_passed}\n")
        f.write(f"- Failed: {total_failed}\n")
        f.write(f"- Errors: {total_errors}\n")
        f.write(f"- Pass Rate: {total_passed/max(total_tests,1)*100:.1f}%\n\n")
        
        for result in all_results:
            f.write(f"---\n\n")
            f.write(f"## REPO: {result['repo']}\n\n")
            
            f.write(f"### EXECUTION META\n")
            f.write(f"- Status: {result.get('status', 'UNKNOWN')}\n")
            f.write(f"- Duration: {result.get('duration', 0):.1f}s\n")
            f.write(f"- Exit Code: {result.get('exit_code', 'N/A')}\n")
            f.write(f"- Passed: {result.get('passed', 0)}\n")
            f.write(f"- Failed: {result.get('failed', 0)}\n")
            f.write(f"- Errors: {result.get('errors', 0)}\n")
            f.write(f"- Expected: {result.get('expected', 'N/A')}\n\n")
            
            if 'stdout' in result:
                f.write(f"### STDOUT (RAW)\n\n")
                f.write("```\n")
                # Keine Kürzung!
                f.write(result['stdout'])
                f.write("\n```\n\n")
            
            if 'stderr' in result and result['stderr']:
                f.write(f"### STDERR (RAW)\n\n")
                f.write("```\n")
                f.write(result['stderr'])
                f.write("\n```\n\n")
    
    # Erstelle INTEGRITY CHECK
    integrity_file = OUTPUT_DIR / "integrity-check.md"
    with open(integrity_file, 'w', encoding='utf-8') as f:
        f.write("# SSZ TEST INTEGRITY CHECK\n\n")
        f.write(f"**Generated:** {datetime.now().isoformat()}\n\n")
        
        # Prüfe Integrität
        integrity_passed = True
        issues = []
        
        # 1. Test-Anzahl prüfen
        expected_total = sum(r["expected"] for r in REPOS.values())
        if total_tests < expected_total:
            integrity_passed = False
            issues.append(f"Tests missing: {total_tests}/{expected_total}")
        
        # 2. Repo-Vollständigkeit
        for result in all_results:
            if result.get("status") == "MISSING":
                integrity_passed = False
                issues.append(f"Repo missing: {result['repo']}")
        
        # 3. Fehler prüfen
        if total_failed > 0:
            issues.append(f"Failed tests: {total_failed}")
        
        if total_errors > 0:
            issues.append(f"Test errors: {total_errors}")
        
        f.write(f"## INTEGRITY STATUS: {'PASS' if integrity_passed and total_failed == 0 else 'FAIL'}\n\n")
        
        f.write("## REPO STATUS\n\n")
        f.write("| Repo | Status | Passed | Failed | Expected | Match |\n")
        f.write("|------|--------|--------|--------|----------|-------|\n")
        for result in all_results:
            repo = result['repo']
            status = result.get('status', 'UNKNOWN')
            passed = result.get('passed', 0)
            failed = result.get('failed', 0)
            expected = result.get('expected', 0)
            match = "YES" if (passed + failed) >= expected else "NO"
            f.write(f"| {repo} | {status} | {passed} | {failed} | {expected} | {match} |\n")
        
        if issues:
            f.write("\n## ISSUES\n\n")
            for issue in issues:
                f.write(f"- ❌ {issue}\n")
    
    # Erstelle JSON Export
    json_file = OUTPUT_DIR / "test-results.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "total_duration": total_duration,
            "total_tests": total_tests,
            "total_passed": total_passed,
            "total_failed": total_failed,
            "total_errors": total_errors,
            "pass_rate": total_passed/max(total_tests,1),
            "results": all_results
        }, f, indent=2, ensure_ascii=False)
    
    # Finaler Output
    print(f"\n{'='*70}")
    print("COMPLETE!")
    print(f"{'='*70}")
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {total_passed}")
    print(f"Failed: {total_failed}")
    print(f"Errors: {total_errors}")
    print(f"Pass Rate: {total_passed/max(total_tests,1)*100:.1f}%")
    print(f"\nFiles saved to:")
    print(f"  {full_output_file}")
    print(f"  {integrity_file}")
    print(f"  {json_file}")
    print(f"{'='*70}")
    
    return integrity_passed and total_failed == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
