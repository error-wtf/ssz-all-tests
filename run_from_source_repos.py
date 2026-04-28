#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RUN ALL REPOS - Direct Source Execution
Führt Tests direkt in den Original-Repos aus (nicht aggregated!)
"""

import subprocess
import sys
import json
import os
from pathlib import Path
from datetime import datetime
import time

os.environ['PYTHONIOENCODING'] = 'utf-8:replace'

BASE_DIR = Path("E:/clone")
OUTPUT_DIR = BASE_DIR / "ssz-all-tests-test" / "COMPLETE_TEST_OUTPUTS_V2"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Repos mit ihren Test-Verzeichnissen
REPOS = [
    ("ssz-qubits", BASE_DIR / "ssz-qubits", "tests/"),
    ("ssz-metric-pure", BASE_DIR / "ssz-metric-pure", "tests/"),
    ("ssz-schuhman-experiment", BASE_DIR / "ssz-schuhman-experiment", ""),
    ("ssz-lagrange", BASE_DIR / "ssz-lagrange", ""),
    ("segmented-calculation-suite", BASE_DIR / "segmented-calculation-suite", ""),
    ("ssz-lensing", BASE_DIR / "ssz-lensing", ""),
    ("Unified-Results", BASE_DIR / "Segmented-Spacetime-Mass-Projection-Unified-Results", "tests/"),
    ("ssz-trajectories", BASE_DIR / "ssz-trajectories", ""),
    ("segmented-energy", BASE_DIR / "segmented-energy", ""),
    ("g79-cygnus-test", BASE_DIR / "g79-cygnus-test", ""),
    ("ssz-full-metric", BASE_DIR / "ssz-full-metric", "tests/"),
]

def run_repo(name, path, test_dir):
    """Run tests in original repo location"""
    print(f"\n{'='*70}")
    print(f"RUNNING: {name}")
    print(f"{'='*70}")
    
    try:
        start = time.time()
        
        # Bestimme Test-Pfad
        if test_dir:
            test_path = str(path / test_dir)
        else:
            test_path = str(path)
        
        # Setze PYTHONPATH
        env = os.environ.copy()
        env['PYTHONPATH'] = f"{path};{env.get('PYTHONPATH', '')}"
        
        # Führe Tests aus
        cmd = [sys.executable, "-m", "pytest", "-v", "--tb=short", "-x"]
        if test_dir:
            cmd.append(test_dir)
        
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
        
        duration = time.time() - start
        
        # Parse Ergebnisse
        stdout = result.stdout
        stderr = result.stderr
        
        # Zähle passed/failed
        passed = 0
        failed = 0
        for line in stdout.split('\n'):
            if 'passed' in line.lower():
                try:
                    passed = int(line.split()[0])
                except:
                    pass
            if 'failed' in line.lower():
                try:
                    failed = int(line.split()[0])
                except:
                    pass
        
        print(f"{'✅' if result.returncode == 0 else '❌'} {name}: "
              f"{passed} passed, {failed} failed ({duration:.1f}s)")
        
        return {
            "repo": name,
            "exit_code": result.returncode,
            "duration": duration,
            "stdout": stdout,
            "stderr": stderr,
            "passed": passed,
            "failed": failed,
            "success": result.returncode == 0
        }
        
    except subprocess.TimeoutExpired:
        print(f"⏱️  {name}: TIMEOUT")
        return {"repo": name, "error": "TIMEOUT", "duration": 300}
    except Exception as e:
        print(f"💥 {name}: ERROR - {e}")
        return {"repo": name, "error": str(e), "duration": 0}

def main():
    all_results = []
    start_time = time.time()
    
    print("="*70)
    print("SSZ COMPLETE TEST SUITE - RUNNING FROM SOURCE REPOS")
    print("="*70)
    
    for name, path, test_dir in REPOS:
        if not path.exists():
            print(f"⚠️  {name}: Not found at {path}")
            continue
        result = run_repo(name, path, test_dir)
        all_results.append(result)
    
    total_duration = time.time() - start_time
    
    # Erstelle Summary
    total_passed = sum(r.get('passed', 0) for r in all_results)
    total_failed = sum(r.get('failed', 0) for r in all_results)
    
    summary = {
        "timestamp": datetime.now().isoformat(),
        "duration": total_duration,
        "repositories": len(all_results),
        "total_tests_passed": total_passed,
        "total_tests_failed": total_failed,
        "results": all_results
    }
    
    # Speichere JSON
    json_path = OUTPUT_DIR / "all_repo_outputs.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    # Speichere Markdown
    md_path = OUTPUT_DIR / "ALL_REPO_TEST_OUTPUTS.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# SSZ Complete Test Outputs (Source Repos)\n\n")
        f.write(f"**Generated:** {summary['timestamp']}\n")
        f.write(f"**Total Duration:** {total_duration:.1f}s\n")
        f.write(f"**Repositories:** {len(all_results)}\n")
        f.write(f"**Total Tests Passed:** {total_passed}\n")
        f.write(f"**Total Tests Failed:** {total_failed}\n\n")
        
        for r in all_results:
            f.write(f"## {r['repo']}\n\n")
            
            if 'error' in r:
                f.write(f"**ERROR:** {r['error']}\n\n")
            else:
                status = "✅ PASS" if r.get('success') else "❌ FAIL"
                f.write(f"**Status:** {status}\n")
                f.write(f"**Tests:** {r.get('passed', 0)} passed, {r.get('failed', 0)} failed\n")
                f.write(f"**Duration:** {r['duration']:.1f}s\n")
                f.write(f"**Exit Code:** {r['exit_code']}\n\n")
                
                f.write("### STDOUT\n\n```\n")
                # Limit output to prevent huge files
                output = r['stdout']
                if len(output) > 15000:
                    output = output[:7500] + "\n\n... [OUTPUT TRUNCATED] ...\n\n" + output[-7500:]
                f.write(output)
                f.write("\n```\n\n")
                
                if r.get('stderr'):
                    f.write("### STDERR\n\n```\n")
                    f.write(r['stderr'][:5000])
                    f.write("\n```\n\n")
            
            f.write("---\n\n")
    
    print(f"\n{'='*70}")
    print("COMPLETE!")
    print(f"Results saved to:")
    print(f"  JSON: {json_path}")
    print(f"  Markdown: {md_path}")
    print(f"{'='*70}")
    print(f"\nTotal: {total_passed} passed, {total_failed} failed")
    
    return summary

if __name__ == "__main__":
    main()
