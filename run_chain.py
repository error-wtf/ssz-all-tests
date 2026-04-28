#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SSZ FULL CHAIN EXECUTION - run_chain.py
Führt ALLE Repos in Kette aus, erkennt vorhandene Orchestrierung, 
sammelt kompletten Output, erstellt Gap-Analyse.

STRICT: Keine Kürzung, keine Abkürzungen, existierende Runner bevorzugen.
"""

import subprocess
import sys
import os
import json
import time
import glob
from datetime import datetime
from pathlib import Path

os.environ['PYTHONIOENCODING'] = 'utf-8'

BASE_DIR = Path("E:/clone")
OUTPUT_DIR = BASE_DIR / "ssz-all-tests-test" / "CHAIN_OUTPUT"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Chain-Reihenfolge wie im Prompt definiert
REPO_CHAIN = [
    ("ssz-qubits", BASE_DIR / "ssz-qubits"),
    ("ssz-metric-pure", BASE_DIR / "ssz-metric-pure"),
    ("segmented-calculation-suite", BASE_DIR / "segmented-calculation-suite"),
    ("ssz-schuhman-experiment", BASE_DIR / "ssz-schuhman-experiment"),
    ("ssz-lensing", BASE_DIR / "ssz-lensing"),
    ("Unified-Results", BASE_DIR / "Segmented-Spacetime-Mass-Projection-Unified-Results"),
    ("ssz-trajectories", BASE_DIR / "ssz-trajectories"),
    ("segmented-energy", BASE_DIR / "segmented-energy"),
    ("g79-cygnus-test", BASE_DIR / "g79-cygnus-test"),
    ("ssz-all-tests", BASE_DIR / "ssz-all-tests-test"),
]

def detect_orchestration(repo_path):
    """
    Erkenne vorhandene Orchestrierung im Repo.
    Priorität: run*.py > orchestrator*.py > main.py > test_runner.py > scripts/
    """
    if not repo_path.exists():
        return None, "Path does not exist"
    
    # Priorität 1: run*.py
    run_files = list(repo_path.glob("run*.py"))
    if run_files:
        return run_files[0], "run_script"
    
    # Priorität 2: orchestrator*.py
    orch_files = list(repo_path.glob("orchestrator*.py"))
    if orch_files:
        return orch_files[0], "orchestrator"
    
    # Priorität 3: main.py
    if (repo_path / "main.py").exists():
        return repo_path / "main.py", "main"
    
    # Priorität 4: test_runner.py
    if (repo_path / "test_runner.py").exists():
        return repo_path / "test_runner.py", "test_runner"
    
    # Priorität 5: scripts/ Verzeichnis
    scripts_dir = repo_path / "scripts"
    if scripts_dir.exists():
        script_files = list(scripts_dir.glob("*.py"))
        if script_files:
            return script_files[0], "script"
    
    return None, "none_found"

def execute_repo(repo_name, repo_path, runner_info):
    """
    Führe ein Repo aus mit erkanntem Runner oder Fallback.
    """
    print(f"\n{'='*80}")
    print(f"CHAIN STEP: {repo_name}")
    print(f"Path: {repo_path}")
    print(f"{'='*80}")
    
    start_time = time.time()
    
    # Environment setup
    env = os.environ.copy()
    env['PYTHONPATH'] = f"{repo_path};{env.get('PYTHONPATH', '')}"
    
    # Bestimme Ausführungskommando
    if runner_info[0]:
        # Vorhandener Runner gefunden
        runner_path = runner_info[0]
        runner_type = runner_info[1]
        
        print(f"Runner detected: {runner_path.name} ({runner_type})")
        
        cmd = [sys.executable, str(runner_path)]
        cwd = str(runner_path.parent)
    else:
        # Fallback: pytest
        print(f"No runner found -> using pytest fallback")
        
        # Finde Test-Verzeichnis
        if (repo_path / "tests").exists():
            test_path = str(repo_path / "tests")
        else:
            test_path = str(repo_path)
        
        cmd = [sys.executable, "-m", "pytest", "-v", "-s", "--tb=long", test_path]
        cwd = str(repo_path)
    
    print(f"Command: {' '.join(cmd)}")
    print(f"Working Dir: {cwd}")
    print("-" * 80)
    
    # Ausführung
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',
            timeout=600,
            cwd=cwd,
            env=env
        )
        
        duration = time.time() - start_time
        
        # Parse Test-Ergebnisse
        stdout = result.stdout
        stderr = result.stderr
        
        # Zähle Tests
        passed = stdout.count("PASSED") + stdout.count("passed")
        failed = stdout.count("FAILED") + stdout.count("failed")
        errors = stdout.count("ERROR") + stdout.count("error")
        
        # Extrahiere Gesamtzahl aus "X passed in Ys"
        total_tests = 0
        for line in stdout.split('\n'):
            if 'passed' in line.lower() and ('items' in line.lower() or 'test' in line.lower()):
                # Versuche Zahl zu extrahieren
                parts = line.split()
                for i, part in enumerate(parts):
                    if part.isdigit():
                        total_tests = int(part)
                        break
        
        if total_tests == 0:
            total_tests = passed + failed + errors
        
        print(f"OK Completed in {duration:.1f}s")
        print(f"  Exit Code: {result.returncode}")
        print(f"  Tests: {passed} passed, {failed} failed, {errors} errors")
        
        return {
            "repo": repo_name,
            "path": str(repo_path),
            "runner_used": str(runner_info[0]) if runner_info[0] else "pytest (fallback)",
            "runner_type": runner_info[1],
            "exit_code": result.returncode,
            "duration": duration,
            "passed": passed,
            "failed": failed,
            "errors": errors,
            "total_tests": total_tests,
            "stdout": stdout,
            "stderr": stderr,
            "status": "SUCCESS" if result.returncode == 0 else "FAILED"
        }
        
    except subprocess.TimeoutExpired:
        return {
            "repo": repo_name,
            "status": "TIMEOUT",
            "runner_used": str(runner_info[0]) if runner_info[0] else "pytest",
            "runner_type": runner_info[1],
            "duration": 600,
            "stdout": "",
            "stderr": "Execution timeout (600s)",
            "exit_code": -2
        }
    except Exception as e:
        return {
            "repo": repo_name,
            "status": "ERROR",
            "runner_used": str(runner_info[0]) if runner_info[0] else "pytest",
            "runner_type": runner_info[1],
            "stdout": "",
            "stderr": str(e),
            "exit_code": -3
        }

def main():
    print("="*80)
    print("SSZ FULL CHAIN EXECUTION")
    print("="*80)
    print(f"Start: {datetime.now().isoformat()}")
    print(f"Repos in Chain: {len(REPO_CHAIN)}")
    print("="*80)
    
    chain_results = []
    global_start = time.time()
    
    # Phase 1: Orchestrierung erkennen
    print("\n" + "="*80)
    print("PHASE 1: ORCHESTRATION DETECTION")
    print("="*80)
    
    orchestration_map = {}
    for repo_name, repo_path in REPO_CHAIN:
        runner, runner_type = detect_orchestration(repo_path)
        orchestration_map[repo_name] = (runner, runner_type)
        status = "OK" if runner else "NO"
        print(f"{status} {repo_name}: {runner_type}")
        if runner:
            print(f"   -> {runner.name}")
    
    # Phase 2: Chain-Ausführung
    print("\n" + "="*80)
    print("PHASE 2: CHAIN EXECUTION")
    print("="*80)
    
    for repo_name, repo_path in REPO_CHAIN:
        runner_info = orchestration_map[repo_name]
        result = execute_repo(repo_name, repo_path, runner_info)
        chain_results.append(result)
    
    global_duration = time.time() - global_start
    
    # Phase 3: Full Output generieren
    print("\n" + "="*80)
    print("PHASE 3: FULL OUTPUT GENERATION")
    print("="*80)
    
    # Master Output File
    full_output_file = OUTPUT_DIR / "full-output.md"
    with open(full_output_file, 'w', encoding='utf-8') as f:
        f.write("# SSZ FULL CHAIN OUTPUT\n\n")
        f.write(f"**Generated:** {datetime.now().isoformat()}\n")
        f.write(f"**Total Duration:** {global_duration:.1f}s\n")
        f.write(f"**System:** {os.name}\n")
        f.write(f"**Python:** {sys.version}\n\n")
        
        f.write("="*80 + "\n")
        f.write("GLOBAL SUMMARY\n")
        f.write("="*80 + "\n\n")
        
        total_passed = sum(r.get("passed", 0) for r in chain_results)
        total_failed = sum(r.get("failed", 0) for r in chain_results)
        total_errors = sum(r.get("errors", 0) for r in chain_results)
        total_tests = sum(r.get("total_tests", 0) for r in chain_results)
        success_count = sum(1 for r in chain_results if r["status"] == "SUCCESS")
        
        f.write(f"- **Total Repositories:** {len(REPO_CHAIN)}\n")
        f.write(f"- **Successful:** {success_count} ✅\n")
        f.write(f"- **Failed/Timeout/Error:** {len(REPO_CHAIN) - success_count}\n")
        f.write(f"- **Total Tests Executed:** {total_tests}\n")
        f.write(f"- **Tests Passed:** {total_passed}\n")
        f.write(f"- **Tests Failed:** {total_failed}\n")
        f.write(f"- **Errors:** {total_errors}\n")
        f.write(f"- **Overall Pass Rate:** {total_passed/max(total_tests,1)*100:.1f}%\n\n")
        
        # Tabelle
        f.write("| Repository | Status | Runner | Tests | Passed | Failed | Duration |\n")
        f.write("|------------|--------|--------|-------|--------|--------|----------|\n")
        for r in chain_results:
            runner_name = Path(r['runner_used']).name if r['runner_used'] and r['runner_used'] != "pytest (fallback)" else r['runner_type']
            f.write(f"| {r['repo']} | {r['status']} | {runner_name} | {r['total_tests']} | {r['passed']} | {r['failed']} | {r['duration']:.1f}s |\n")
        
        f.write("\n")
        
        # JEDES REPO - KOMPLETTER OUTPUT
        for i, result in enumerate(chain_results):
            f.write("="*80 + "\n")
            f.write(f"REPO: {result['repo']}\n")
            f.write("="*80 + "\n\n")
            
            f.write("### Execution Info\n\n")
            f.write(f"- **Runner Used:** `{result['runner_used']}`\n")
            f.write(f"- **Runner Type:** {result['runner_type']}\n")
            f.write(f"- **Exit Code:** {result['exit_code']}\n")
            f.write(f"- **Duration:** {result['duration']:.1f}s\n")
            f.write(f"- **Status:** {result['status']}\n")
            f.write(f"- **Tests:** {result['total_tests']} total, {result['passed']} passed, {result['failed']} failed, {result['errors']} errors\n\n")
            
            # KOMPLETTER STDOUT - KEINE KÜRZUNG
            f.write("### STDOUT (COMPLETE)\n\n")
            f.write("```\n")
            f.write(result['stdout'])
            f.write("\n```\n\n")
            
            # KOMPLETTER STDERR - KEINE KÜRZUNG
            if result['stderr']:
                f.write("### STDERR (COMPLETE)\n\n")
                f.write("```\n")
                f.write(result['stderr'])
                f.write("\n```\n\n")
            
            f.write("---\n\n")
    
    print(f"✓ Full output saved: {full_output_file}")
    print(f"  Size: {full_output_file.stat().st_size / 1024 / 1024:.2f} MB")
    
    # JSON Export für Analyse
    json_file = OUTPUT_DIR / "chain_results.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "total_duration": global_duration,
            "total_repos": len(REPO_CHAIN),
            "total_tests": total_tests,
            "total_passed": total_passed,
            "total_failed": total_failed,
            "total_errors": total_errors,
            "pass_rate": total_passed / max(total_tests, 1),
            "orchestration": {k: {"runner": str(v[0]) if v[0] else None, "type": v[1]} for k, v in orchestration_map.items()},
            "results": chain_results
        }, f, indent=2, ensure_ascii=False)
    
    print(f"✓ JSON results saved: {json_file}")
    
    # Zusammenfassung
    print("\n" + "="*80)
    print("CHAIN EXECUTION COMPLETE")
    print("="*80)
    print(f"Total Duration: {global_duration:.1f}s")
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {total_passed}")
    print(f"Failed: {total_failed}")
    print(f"Errors: {total_errors}")
    print(f"Success Rate: {success_count}/{len(REPO_CHAIN)} repos")
    print(f"\nOutput Directory: {OUTPUT_DIR}")
    print("="*80)
    
    return chain_results

if __name__ == "__main__":
    results = main()
