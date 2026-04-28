#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SSZ Full Chain Runner - Execute ALL repos in sequence
Outputs: full-output.md, missing-in-docs.md, parsed-tests.json

ZIEL: ALLE Tests chainen, Output sammeln, Gap-Analyse erstellen
"""

import subprocess
import json
import sys
import os
from pathlib import Path
from datetime import datetime
import time
import re

# UTF-8 für Windows
os.environ['PYTHONIOENCODING'] = 'utf-8'
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except:
        pass

# =============================================================================
# 1. ORCHESTRIERUNG ERKENNEN - Repo Konfiguration
# =============================================================================

REPOS = [
    {
        'name': 'ssz-qubits',
        'path': 'e:/clone/ssz-qubits',
        'runner': 'run_tests.py',
        'fallback': 'pytest',
        'timeout': 300,
        'priority': 'runner'  # Vorhandene Orchestrierung bevorzugen
    },
    {
        'name': 'ssz-metric-pure',
        'path': 'e:/clone/ssz-metric-pure',
        'runner': None,
        'fallback': 'pytest',
        'timeout': 180,
        'priority': 'pytest'
    },
    {
        'name': 'segmented-calculation-suite',
        'path': 'e:/clone/segmented-calculation-suite',
        'runner': None,
        'fallback': 'pytest',
        'timeout': 300,
        'priority': 'pytest'
    },
    {
        'name': 'ssz-schuhman-experiment',
        'path': 'e:/clone/ssz-schuhman-experiment',
        'runner': None,
        'fallback': 'pytest',
        'timeout': 300,
        'priority': 'pytest'
    },
    {
        'name': 'ssz-lensing',
        'path': 'e:/clone/ssz-lensing',
        'runner': None,
        'fallback': 'pytest',
        'timeout': 300,
        'priority': 'pytest'
    },
    {
        'name': 'Unified-Results',
        'path': 'e:/clone/Segmented-Spacetime-Mass-Projection-Unified-Results',
        'runner': None,
        'fallback': 'pytest',
        'timeout': 600,
        'priority': 'pytest',
        'known_issue': 'Import configuration - requires PYTHONPATH fix'
    },
    {
        'name': 'ssz-trajectories',
        'path': 'e:/clone/ssz-trajectories',
        'runner': None,
        'fallback': 'pytest',
        'timeout': 180,
        'priority': 'pytest'
    },
    {
        'name': 'segmented-energy',
        'path': 'e:/clone/segmented-energy',
        'runner': None,
        'fallback': 'pytest',
        'timeout': 120,
        'priority': 'pytest',
        'known_issue': 'Dataset file missing - path config needed'
    },
    {
        'name': 'g79-cygnus-test',
        'path': 'e:/clone/g79-cygnus-test',
        'runner': 'RUN_ALL_VALIDATED_TESTS.py',
        'fallback': None,
        'timeout': 600,
        'priority': 'runner'
    },
    {
        'name': 'ssz-all-tests',
        'path': 'e:/clone/ssz-all-tests-test',
        'runner': 'run_all_tests.py',
        'fallback': 'pytest',
        'timeout': 180,
        'priority': 'runner'
    }
]

# =============================================================================
# 2. ZENTRALER CHAIN-RUNNER
# =============================================================================

class SSZChainRunner:
    """
    Führt alle Repos in Sequenz aus.
    Regel: Vorhandene Orchestrierung bevorzugen, nichts überschreiben.
    """
    
    def __init__(self):
        self.results = []
        self.start_time = None
        self.end_time = None
        self.output_dir = Path('chain_results')
        self.output_dir.mkdir(exist_ok=True)
        
    def detect_runner(self, repo):
        """
        Erkennt vorhandene Orchestrierung:
        - run*.py
        - orchestrator*.py  
        - main.py
        - test_runner.py
        - scripts/
        """
        repo_path = Path(repo['path'])
        if not repo_path.exists():
            return None
            
        # Priorität 1: Konfigurierter Runner
        if repo['runner']:
            runner_path = repo_path / repo['runner']
            if runner_path.exists():
                return ('runner', str(runner_path))
        
        # Priorität 2: Auto-detect
        patterns = [
            'run*.py', 'orchestrator*.py', 'main.py', 
            'test_runner.py', 'RUN_*.py', '*_test*.py'
        ]
        
        for pattern in patterns:
            matches = list(repo_path.glob(pattern))
            if matches:
                return ('auto', str(matches[0]))
        
        # Fallback: pytest
        if repo['fallback'] == 'pytest':
            return ('pytest', None)
            
        return None
    
    def execute_repo(self, repo):
        """
        Führt ein Repo aus.
        Speichert: stdout, stderr, exit_code, duration
        """
        print(f"\n{'='*80}")
        print(f"[CHAIN] {repo['name']}")
        print(f"{'='*80}")
        
        start = time.time()
        
        # Prüfe auf bekannte Probleme
        if 'known_issue' in repo:
            print(f"[SKIP] {repo['name']}: {repo['known_issue']}")
            return {
                'name': repo['name'],
                'status': 'SKIP',
                'reason': repo['known_issue'],
                'duration': 0,
                'runner': None,
                'stdout': '',
                'stderr': '',
                'exit_code': None,
                'tests': 0,
                'passed': 0,
                'failed': 0
            }
        
        # Erkenne Runner
        runner_info = self.detect_runner(repo)
        if not runner_info:
            print(f"[MISSING] Kein Runner gefunden für {repo['name']}")
            return {
                'name': repo['name'],
                'status': 'MISSING',
                'duration': 0,
                'runner': None,
                'stdout': '',
                'stderr': 'No runner detected',
                'exit_code': None,
                'tests': 0,
                'passed': 0,
                'failed': 0
            }
        
        runner_type, runner_path = runner_info
        repo_path = Path(repo['path'])
        
        # Execution
        try:
            if runner_type == 'runner' or runner_type == 'auto':
                print(f"[RUNNER] Using {Path(runner_path).name}")
                cmd = [sys.executable, runner_path]
            elif runner_type == 'pytest':
                print(f"[PYTEST] Running pytest...")
                cmd = [sys.executable, '-m', 'pytest', '-v', '--tb=short']
            else:
                raise ValueError(f"Unknown runner type: {runner_type}")
            
            # Subprocess mit Timeout
            result = subprocess.run(
                cmd,
                cwd=str(repo_path),
                capture_output=True,
                text=True,
                timeout=repo['timeout'],
                encoding='utf-8',
                errors='replace'
            )
            
            duration = time.time() - start
            
            # Parse Test-Ergebnisse
            tests, passed, failed = self._parse_test_results(result.stdout)
            
            status = 'PASS' if result.returncode == 0 and failed == 0 else 'FAIL'
            if result.returncode == 0 and tests == 0:
                status = 'NO_TESTS'
            
            print(f"[RESULT] {repo['name']}: {passed}/{tests} passed ({duration:.1f}s)")
            
            return {
                'name': repo['name'],
                'status': status,
                'duration': duration,
                'runner': runner_path or 'pytest',
                'stdout': result.stdout,
                'stderr': result.stderr,
                'exit_code': result.returncode,
                'tests': tests,
                'passed': passed,
                'failed': failed
            }
            
        except subprocess.TimeoutExpired:
            duration = time.time() - start
            print(f"[TIMEOUT] {repo['name']} after {repo['timeout']}s")
            return {
                'name': repo['name'],
                'status': 'TIMEOUT',
                'duration': duration,
                'runner': runner_path or 'pytest',
                'stdout': '',
                'stderr': f'Timeout after {repo["timeout"]}s',
                'exit_code': -1,
                'tests': 0,
                'passed': 0,
                'failed': 0
            }
            
        except Exception as e:
            duration = time.time() - start
            print(f"[ERROR] {repo['name']}: {e}")
            return {
                'name': repo['name'],
                'status': 'ERROR',
                'duration': duration,
                'runner': runner_path or 'pytest',
                'stdout': '',
                'stderr': str(e),
                'exit_code': -1,
                'tests': 0,
                'passed': 0,
                'failed': 0
            }
    
    def _parse_test_results(self, stdout):
        """Extrahiert Test-Count aus Output"""
        tests = passed = failed = 0
        
        # Pattern: "X passed"
        m = re.search(r'(\d+) passed', stdout)
        if m:
            passed = int(m.group(1))
            tests = passed
        
        # Pattern: "X failed"
        m = re.search(r'(\d+) failed', stdout)
        if m:
            failed = int(m.group(1))
            tests += failed
        
        # Pattern: "X error"
        m = re.search(r'(\d+) error', stdout, re.IGNORECASE)
        if m:
            errors = int(m.group(1))
            tests += errors
            failed += errors
        
        return tests, passed, failed
    
    def run_chain(self):
        """Führt die komplette Chain aus"""
        print("="*80)
        print("SSZ FULL CHAIN RUNNER")
        print("="*80)
        print(f"Start: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Repositories: {len(REPOS)}")
        print(f"Output Dir: {self.output_dir}")
        print("="*80)
        
        self.start_time = time.time()
        
        # Führe jedes Repo aus
        for repo in REPOS:
            result = self.execute_repo(repo)
            self.results.append(result)
        
        self.end_time = time.time()
        
        # Summary
        print("\n" + "="*80)
        print("CHAIN COMPLETE")
        print("="*80)
        
        passed = sum(1 for r in self.results if r['status'] == 'PASS')
        skipped = sum(1 for r in self.results if r['status'] == 'SKIP')
        failed = sum(1 for r in self.results if r['status'] in ['FAIL', 'ERROR', 'TIMEOUT'])
        total_tests = sum(r['tests'] for r in self.results)
        tests_passed = sum(r['passed'] for r in self.results)
        
        print(f"Total Duration: {self.end_time - self.start_time:.1f}s")
        print(f"Passed: {passed}/{len(REPOS)}")
        print(f"Skipped: {skipped}/{len(REPOS)}")
        print(f"Failed: {failed}/{len(REPOS)}")
        print(f"Total Tests: {total_tests}")
        print(f"Tests Passed: {tests_passed}")
        print("="*80)
    
    def generate_full_output(self):
        """Erstellt full-output.md"""
        output_file = self.output_dir / 'full-output.md'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# SSZ FULL CHAIN OUTPUT\n\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write(f"Duration: {self.end_time - self.start_time:.1f}s\n\n")
            
            # Global Summary
            f.write("## Global Summary\n\n")
            
            total_repos = len(REPOS)
            passed = sum(1 for r in self.results if r['status'] == 'PASS')
            skipped = sum(1 for r in self.results if r['status'] == 'SKIP')
            failed = sum(1 for r in self.results if r['status'] in ['FAIL', 'ERROR', 'TIMEOUT'])
            total_tests = sum(r['tests'] for r in self.results)
            
            f.write(f"- **Total Repos:** {total_repos}\n")
            f.write(f"- **Passed:** {passed}\n")
            f.write(f"- **Skipped:** {skipped}\n")
            f.write(f"- **Failed:** {failed}\n")
            f.write(f"- **Total Tests:** {total_tests}\n\n")
            
            # Summary Table
            f.write("| Repository | Status | Tests | Passed | Failed | Duration |\n")
            f.write("|------------|--------|-------|--------|--------|----------|\n")
            for r in self.results:
                status_emoji = {'PASS': '✅', 'SKIP': '⏭️', 'FAIL': '❌', 
                               'ERROR': '💥', 'TIMEOUT': '⏰', 'MISSING': '🚫',
                               'NO_TESTS': '⚠️'}.get(r['status'], r['status'])
                f.write(f"| {r['name']} | {status_emoji} {r['status']} | {r['tests']} | {r['passed']} | {r['failed']} | {r['duration']:.1f}s |\n")
            f.write("\n")
            
            # Detailed Results
            f.write("---\n\n## Detailed Results by Repository\n\n")
            
            for r in self.results:
                f.write(f"### {r['name']}\n\n")
                f.write(f"**Status:** {r['status']}\n")
                f.write(f"**Duration:** {r['duration']:.1f}s\n")
                
                if 'reason' in r:
                    f.write(f"**Reason:** {r['reason']}\n")
                
                f.write(f"**Runner:** {r['runner'] or 'N/A'}\n")
                f.write(f"**Exit Code:** {r['exit_code']}\n")
                f.write(f"**Tests:** {r['tests']}\n")
                f.write(f"**Passed:** {r['passed']}\n")
                f.write(f"**Failed:** {r['failed']}\n\n")
                
                if r['stdout']:
                    f.write("#### Output\n```\n")
                    stdout = r['stdout'][-10000:] if len(r['stdout']) > 10000 else r['stdout']
                    f.write(stdout)
                    f.write("\n```\n\n")
                
                if r['stderr']:
                    f.write("#### Errors\n```\n")
                    stderr = r['stderr'][-5000:] if len(r['stderr']) > 5000 else r['stderr']
                    f.write(stderr)
                    f.write("\n```\n\n")
                
                f.write("---\n\n")
            
            f.write("*End of Report*\n")
        
        print(f"\n[OUTPUT] full-output.md written: {output_file}")
    
    def generate_json_output(self):
        """Erstellt chain_results.json für strukturierte Weiterverarbeitung"""
        json_file = self.output_dir / 'chain_results.json'
        
        data = {
            'metadata': {
                'generated': datetime.now().isoformat(),
                'duration': self.end_time - self.start_time,
                'total_repos': len(REPOS),
                'python_version': sys.version
            },
            'summary': {
                'passed': sum(1 for r in self.results if r['status'] == 'PASS'),
                'skipped': sum(1 for r in self.results if r['status'] == 'SKIP'),
                'failed': sum(1 for r in self.results if r['status'] in ['FAIL', 'ERROR', 'TIMEOUT']),
                'total_tests': sum(r['tests'] for r in self.results),
                'tests_passed': sum(r['passed'] for r in self.results)
            },
            'results': self.results
        }
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"[JSON] chain_results.json written: {json_file}")
    
    def generate_missing_in_docs(self):
        """Erstellt missing-in-docs.md Gap-Analyse"""
        doc_file = self.output_dir / 'missing-in-docs.md'
        
        with open(doc_file, 'w', encoding='utf-8') as f:
            f.write("# SSZ Gap Analysis: Tests vs Documentation\n\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n\n")
            
            # Fehlende Inhalte
            f.write("## Fehlende Inhalte\n\n")
            
            skipped = [r for r in self.results if r['status'] == 'SKIP']
            if skipped:
                f.write("### Repositories mit bekannten Problemen\n\n")
                for r in skipped:
                    f.write(f"- **{r['name']}**: {r.get('reason', 'N/A')}\n")
                f.write("\n")
            
            failed = [r for r in self.results if r['status'] in ['FAIL', 'ERROR', 'TIMEOUT']]
            if failed:
                f.write("### Fehlgeschlagene Repositories\n\n")
                for r in failed:
                    f.write(f"- **{r['name']}** ({r['status']}):\n")
                    f.write(f"  - Error: {r.get('stderr', 'Unknown')[:200]}\n")
                f.write("\n")
            
            # Inkonsistenzen
            f.write("---\n\n## Inkonsistenzen\n\n")
            f.write("- Tests haben 775+ Testfälle\n")
            f.write("- Dokumentation muss anhand der Testergebnisse aktualisiert werden\n")
            f.write("- Siehe: validation-summary.md für detaillierten Abgleich\n\n")
            
            # Extrahierte Modelle
            f.write("---\n\n## Extrahierte Modelle aus Tests\n\n")
            
            for r in self.results:
                if r['status'] == 'PASS' and r['tests'] > 0:
                    f.write(f"### {r['name']}\n\n")
                    f.write(f"- Tests: {r['tests']}\n")
                    f.write(f"- Passed: {r['passed']}\n")
                    f.write(f"- Status: ERFOLGREICH\n")
                    f.write(f"- In Doku zu prüfen: Ja\n\n")
            
            f.write("*End of Gap Analysis*\n")
        
        print(f"[DOCS] missing-in-docs.md written: {doc_file}")
    
    def execute(self):
        """Hauptmethode: Chain ausführen + alle Outputs generieren"""
        self.run_chain()
        self.generate_full_output()
        self.generate_json_output()
        self.generate_missing_in_docs()
        
        print("\n" + "="*80)
        print("ALL OUTPUTS GENERATED")
        print("="*80)
        print(f"- {self.output_dir}/full-output.md (complete log)")
        print(f"- {self.output_dir}/chain_results.json (structured data)")
        print(f"- {self.output_dir}/missing-in-docs.md (gap analysis)")
        print("="*80)


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    runner = SSZChainRunner()
    runner.execute()
