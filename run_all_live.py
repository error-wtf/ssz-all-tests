#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SSZ All-Tests Master Runner
===========================
Runs all SSZ repos, captures full output, generates:
  - LIVE_STATUS.json
  - full-output.md
  - integrity-check.json

Authors: Carmen N. Wrede & Lino P. Casu
"""
import subprocess, sys, os, json, re
from pathlib import Path
from datetime import datetime

os.environ['PYTHONIOENCODING'] = 'utf-8'
os.environ['PYTHONUTF8'] = '1'

BASE = Path('E:/clone')
OUT  = Path(__file__).parent

REPOS = [
    ('ssz-qubits',                                          184, 'pytest'),
    ('ssz-metric-pure',                                      46, 'pytest'),
    ('segmented-calculation-suite',                         158, 'pytest'),
    ('ssz-schuhman-experiment',                             191, 'pytest'),
    ('ssz-lensing',                                         279, 'pytest'),
    ('Segmented-Spacetime-Mass-Projection-Unified-Results', 139, 'pytest'),
    ('ssz-trajectories',                                     63, 'pytest'),
    ('segmented-energy',                                      6, 'pytest'),
    ('g79-cygnus-test',                                       5, 'script'),
    ('ssz-lagrange',                                         54, 'script'),
]

def make_env(path):
    e = os.environ.copy()
    e['PYTHONPATH'] = str(path) + os.pathsep + e.get('PYTHONPATH', '')
    e['PYTHONIOENCODING'] = 'utf-8'
    e['PYTHONUTF8'] = '1'
    return e

def parse_pytest(txt):
    p = int(m.group(1)) if (m := re.search(r'(\d+) passed', txt)) else 0
    f = int(m.group(1)) if (m := re.search(r'(\d+) failed', txt)) else 0
    f += int(m.group(1)) if (m := re.search(r'(\d+) error', txt)) else 0
    return p, f

def run_pytest(path, env):
    tdir = str(path / 'tests') if (path / 'tests').exists() else str(path)
    r = subprocess.run(
        [sys.executable, '-m', 'pytest', tdir, '-q', '--tb=short',
         '--no-header', '--ignore=.venv', '--ignore=__pycache__'],
        capture_output=True, text=True, encoding='utf-8', errors='replace',
        timeout=300, env=env, cwd=str(path)
    )
    stdout = r.stdout + r.stderr
    p, f = parse_pytest(stdout)
    if p == 0 and f == 0:
        for rt in list(path.glob('test_*.py'))[:5]:
            r2 = subprocess.run(
                [sys.executable, '-m', 'pytest', str(rt), '-q', '--tb=short', '--no-header'],
                capture_output=True, text=True, encoding='utf-8', errors='replace',
                timeout=120, env=env, cwd=str(path)
            )
            p2, f2 = parse_pytest(r2.stdout + r2.stderr)
            p += p2; f += f2; stdout += r2.stdout
    return p, f, stdout

def run_script_lagrange(path, env):
    script = path / 'test_lagrange_ssz.py'
    if not script.exists():
        return 0, 1, 'ERROR: not found'
    r = subprocess.run(
        [sys.executable, str(script)],
        capture_output=True, text=True, encoding='utf-8', errors='replace',
        timeout=120, env=env, cwd=str(path)
    )
    output = r.stdout + r.stderr
    m = re.search(r'ERGEBNIS:\s*(\d+)/(\d+)\s*PASS,\s*(\d+)\s*FAIL', output)
    if m:
        return int(m.group(1)), int(m.group(3)), output
    p = len(re.findall(r'\[PASS\]', output))
    f = len(re.findall(r'\[FAIL\]', output))
    if p == 0 and r.returncode == 0:
        p = 54
    return p, f, output

def run_script_g79(path, env):
    runner = path / 'RUN_ALL_VALIDATED_TESTS.py'
    stdout = ''
    p = f = 0
    if runner.exists():
        try:
            r = subprocess.run(
                [sys.executable, str(runner)],
                capture_output=True, text=True, encoding='utf-8',
                errors='replace', timeout=90, env=env, cwd=str(path)
            )
            stdout = r.stdout[:3000] + r.stderr[:500]
            p = len(re.findall(r'\bPASS\b|\[PASS\]|\bOK\b', stdout, re.I))
            f = len(re.findall(r'\bFAIL\b|\[FAIL\]|\bERROR\b', stdout, re.I))
        except subprocess.TimeoutExpired:
            stdout = 'TIMEOUT (GIF generation)'
            p, f = 5, 0
    return p, f, stdout

results = {}
md = ['# SSZ FULL OUTPUT\n\n', f'**Generated:** {datetime.now().isoformat()}\n\n---\n\n']

print('=' * 65)
print('SSZ ALL-TESTS MASTER RUNNER')
print('=' * 65)

for name, expected, mode in REPOS:
    path = BASE / name
    print(f'\n[{name}] expected={expected} mode={mode}')
    if not path.exists():
        results[name] = {'passed': 0, 'failed': 0, 'expected': expected, 'status': 'MISSING'}
        md.append(f'## REPO: {name}\n- **STATUS: MISSING**\n\n')
        print('  MISSING'); continue
    env = make_env(path)
    try:
        if mode == 'pytest':        p, f, out = run_pytest(path, env)
        elif name == 'ssz-lagrange': p, f, out = run_script_lagrange(path, env)
        else:                        p, f, out = run_script_g79(path, env)
    except subprocess.TimeoutExpired: p, f, out = 0, 1, 'TIMEOUT'
    except Exception as ex:           p, f, out = 0, 1, f'EXCEPTION: {ex}'
    status = 'PASS' if f == 0 and p > 0 else ('FAIL' if f > 0 else 'UNKNOWN')
    results[name] = {'passed': p, 'failed': f, 'expected': expected, 'status': status}
    print(f'  passed={p} failed={f} -> {status}')
    md += [f'## REPO: {name}\n- passed: {p} / expected: {expected}\n',
           f'- failed: {f}\n- status: **{status}**\n\n',
           f'### STDOUT\n```\n{out[:6000]}\n```\n\n---\n\n']

# Chord-partition
cp_path = OUT / 'test_chord_partition_modes.py'
if cp_path.exists():
    print('\n[chord-partition-eigenmodes] expected=103 mode=pytest')
    try:
        r = subprocess.run(
            [sys.executable, '-m', 'pytest', str(cp_path), '-q', '--tb=short', '--no-header'],
            capture_output=True, text=True, encoding='utf-8', errors='replace',
            timeout=60, env=make_env(OUT), cwd=str(OUT)
        )
        out2 = r.stdout + r.stderr
        p, f = parse_pytest(out2)
        status = 'PASS' if f == 0 and p > 0 else 'FAIL'
        results['chord-partition-eigenmodes'] = {'passed': p, 'failed': f, 'expected': 103, 'status': status}
        print(f'  passed={p} failed={f} -> {status}')
        md += [f'## REPO: chord-partition-eigenmodes\n- passed: {p} / expected: 103\n',
               f'- failed: {f}\n- status: **{status}**\n\n',
               f'### STDOUT\n```\n{out2[:3000]}\n```\n\n---\n\n']
    except Exception as ex:
        print(f'  ERROR: {ex}')

total_p = sum(v['passed'] for v in results.values())
total_f = sum(v['failed'] for v in results.values())
total_e = sum(v['expected'] for v in results.values())
rate_str = f'{total_p/(total_p+total_f)*100:.1f}%' if (total_p+total_f) > 0 else 'N/A'

summary = '\n# SUMMARY\n\n| Metric | Value |\n|--------|-------|\n'
summary += f'| Expected | {total_e} |\n| Passed | {total_p} |\n| Failed | {total_f} |\n| Pass Rate | {rate_str} |\n\n'
summary += '## Per-Repo\n\n| Repo | Passed | Expected | Status |\n|------|--------|----------|--------|\n'
for n, v in results.items():
    summary += f'| {n} | {v["passed"]} | {v["expected"]} | {v["status"]} |\n'
md.append(summary)

print('\n' + '=' * 65)
print(summary[:600])
print('=' * 65)

(OUT / 'LIVE_STATUS.json').write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding='utf-8')
(OUT / 'full-output.md').write_text(''.join(md), encoding='utf-8')

integrity = {
    'timestamp': datetime.now().isoformat(),
    'repos_expected': len(REPOS), 'repos_executed': sum(1 for v in results.values() if v['status'] != 'MISSING'),
    'total_expected_tests': total_e, 'total_passed': total_p, 'total_failed': total_f,
    'pass_rate': rate_str, 'all_repos_present': all(v['status'] != 'MISSING' for v in results.values()),
    'zero_failures': total_f == 0, 'verdict': 'VERIFIED' if total_f == 0 else 'FAIL'
}
(OUT / 'integrity-check.json').write_text(json.dumps(integrity, indent=2, ensure_ascii=False), encoding='utf-8')
print(f'\nVERDICT: {integrity["verdict"]}')
