"""
gen_really_full_output.py
Generates really-full-output.md with complete untruncated test output
from every repo, using verbose flags wherever applicable.
"""
import sys
import os
import re
import subprocess
from pathlib import Path
from datetime import datetime

BASE = Path('E:/clone')
SELF = Path(__file__).parent
OUT = SELF

# Same runner table as run_all_live.py — keep in sync
REPOS = [
    ('ssz-qubits',                                        'ssz-qubits',              184, 'pytest_tests'),
    ('ssz-metric-pure',                                   'ssz-metric-pure',          36,  'script_multi'),
    ('segmented-calculation-suite',                       'segmented-calculation-suite', 158, 'pytest'),
    ('ssz-schuhman-experiment',                           'ssz-schumann',            178, 'schumann'),
    ('ssz-lensing',                                       'ssz-lensing',             279, 'pytest_tests'),
    ('Segmented-Spacetime-Mass-Projection-Unified-Results', 'Unified-Results',       147, 'unified'),
    ('ssz-trajectories',                                  'ssz-trajectories',         63,  'pytest_tests'),
    ('g79-cygnus-test',                                   'g79-cygnus-tests',          5,  'script:RUN_ALL_VALIDATED_TESTS.py'),
    ('ssz-lagrange',                                      'ssz-lagrange',             54,  'script:test_lagrange_ssz.py'),
    ('segmented-energy',                                  'segmented-energy',          7,  'segmented_energy'),
    ('frequency-curvature-validation',                    'frequency-curvature-validation', 82, 'pytest_run:run_all_tests.py'),
]


def make_env(path):
    e = os.environ.copy()
    e['PYTHONPATH'] = (str(path) + os.pathsep
                       + str(path / 'src') + os.pathsep
                       + e.get('PYTHONPATH', ''))
    e['PYTHONIOENCODING'] = 'utf-8'
    e['PYTHONUTF8'] = '1'
    return e


def run_pytest_verbose(path, env, subdir=None):
    target = str(path / subdir) if subdir and (path / subdir).exists() else str(path)
    r = subprocess.run(
        [sys.executable, '-m', 'pytest', target, '-v',
         '--tb=long', '--no-header', '--color=no',
         '--ignore=.venv', '--ignore=__pycache__'],
        capture_output=True, text=True, encoding='utf-8', errors='replace',
        timeout=600, env=env, cwd=str(path)
    )
    return r.stdout + r.stderr


def run_script_full(path, script_name, env):
    script = path / script_name
    if not script.exists():
        return f'ERROR: {script_name} not found\n'
    r = subprocess.run(
        [sys.executable, str(script)],
        capture_output=True, text=True, encoding='utf-8', errors='replace',
        timeout=300, env=env, cwd=str(path)
    )
    return r.stdout + r.stderr


def collect_repo_output(folder, display, mode, path, env):
    """Return full output string for a repo."""
    sections = []

    if mode == 'pytest_tests':
        sections.append(('pytest tests/ (verbose)', run_pytest_verbose(path, env, subdir='tests')))

    elif mode == 'pytest':
        sections.append(('pytest root (verbose)', run_pytest_verbose(path, env)))

    elif mode == 'script_multi':
        # ssz-metric-pure: pytest tests/ + ssz_validator.py
        sections.append(('pytest tests/ (verbose)', run_pytest_verbose(path, env, subdir='tests')))
        sections.append(('ssz_validator.py', run_script_full(path, 'src/ssz_metric_pure/ssz_validator.py', env)))

    elif mode == 'schumann':
        sections.append(('pytest tests/ (verbose)', run_pytest_verbose(path, env, subdir='tests')))
        sections.append(('run_all_ssz_tests.py', run_script_full(path, 'run_all_ssz_tests.py', env)))

    elif mode == 'unified':
        sections.append(('pytest tests/ (verbose)', run_pytest_verbose(path, env, subdir='tests')))
        sections.append(('pytest scripts/tests/ (verbose)', run_pytest_verbose(path, env, subdir='scripts/tests')))
        sections.append(('smoke_test_all.py', run_script_full(path, 'smoke_test_all.py', env)))

    elif mode == 'segmented_energy':
        sections.append(('pytest test_on_complete_dataset.py', run_pytest_verbose(path, env, subdir=None)))
        sections.append(('FINAL_PERFECT_TEST.py', run_script_full(path, 'FINAL_PERFECT_TEST.py', env)))

    elif mode.startswith('script:'):
        script = mode[len('script:'):]
        sections.append((script, run_script_full(path, script, env)))

    elif mode.startswith('pytest_run:'):
        script = mode[len('pytest_run:'):]
        sections.append((script, run_script_full(path, script, env)))

    else:
        sections.append(('pytest (verbose)', run_pytest_verbose(path, env)))

    return sections


def count_from_output(txt):
    """Count pass/fail totals from pytest and custom SSZ runners."""
    # Pytest summaries are the most reliable where present.
    p = int(m.group(1)) if (m := re.search(r'(\d+) passed', txt)) else 0
    f = int(m.group(1)) if (m := re.search(r'(\d+) failed', txt)) else 0
    f += int(m.group(1)) if (m := re.search(r'(\d+) error', txt)) else 0
    if p > 0 or f > 0:
        return p, f

    # Custom SSZ runner formats.
    m = re.search(r'ERGEBNIS:\s*(\d+)/(\d+)\s*PASS,\s*(\d+)\s*FAIL', txt, re.I)
    if m:
        return int(m.group(1)), int(m.group(3))

    m = re.search(r'OVERALL:\s*(\d+)/(\d+)\s*(?:tests?\s*)?passed', txt, re.I)
    if m:
        return int(m.group(1)), int(m.group(2)) - int(m.group(1))

    m = re.search(r'OVERALL:\s*(\d+)/(\d+)\s*test\s*suites?\s*passed', txt, re.I)
    if m:
        return int(m.group(1)), int(m.group(2)) - int(m.group(1))

    m = re.search(r'Results:\s*(\d+)/(\d+)\s*passed', txt, re.I)
    if m:
        return int(m.group(1)), int(m.group(2)) - int(m.group(1))

    m = re.search(r'Total:\s*(\d+)/(\d+)\s*passed', txt, re.I)
    if m:
        return int(m.group(1)), int(m.group(2)) - int(m.group(1))

    m = re.search(r'(\d+)/(\d+)\s*PASS', txt, re.I)
    if m:
        return int(m.group(1)), int(m.group(2)) - int(m.group(1))

    # segmented-energy FINAL_PERFECT_TEST.py reports five validation checks.
    explicit = len(re.findall(r'^\d+\.\s+\S.*PASS', txt, re.MULTILINE | re.I))
    if explicit:
        return explicit, 0

    p = len(re.findall(r'\[PASS\]|✅\s*PASS|\bPASSED\b', txt))
    f = len(re.findall(r'\[FAIL\]|❌\s*FAIL|\bFAILED\b', txt))
    return p, f


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
print('=' * 65)
print('GENERATING really-full-output.md')
print(f'Running {len(REPOS)} repositories (verbose mode)')
print('=' * 65)

lines = [
    '# SSZ ALL-TESTS — REALLY FULL OUTPUT\n\n',
    f'**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  \n',
    f'**Mode:** verbose — complete untruncated output  \n',
    f'**Repos:** {len(REPOS)} + chord-partition (local)  \n\n',
    '---\n\n',
]

grand_passed = 0
grand_failed = 0

for folder, display, expected, mode in REPOS:
    path = BASE / folder
    print(f'\n[{display}]  expected={expected}')

    if not path.exists():
        lines.append(f'# {display}\n\n**STATUS: MISSING** — path not found: `{path}`\n\n---\n\n')
        print('  -> MISSING')
        continue

    env = make_env(path)
    try:
        sections = collect_repo_output(folder, display, mode, path, env)
    except Exception as ex:
        sections = [(f'ERROR: {ex}', '')]

    # Aggregate pass/fail counts.
    # ssz-metric-pure runs a validator in addition to pytest; the validator is
    # qualitative coverage and must not inflate the expected 36-test total.
    repo_p = repo_f = 0
    for section_name, txt in sections:
        p, f = count_from_output(txt)
        if mode == 'script_multi' and 'ssz_validator.py' in section_name:
            repo_f += f
            if 'Traceback' in txt or re.search(r'\bFAIL(?:ED)?\b', txt):
                repo_f += 1
            continue
        repo_p += p
        repo_f += f

    grand_passed += repo_p
    grand_failed += repo_f
    status = 'PASS' if repo_f == 0 and repo_p == expected else 'FAIL'
    print(f'  -> passed={repo_p}  failed={repo_f}  {status}')

    lines.append(f'# {display}\n\n')
    lines.append(f'- **Expected:** {expected}  \n')
    lines.append(f'- **Passed:** {repo_p}  \n')
    lines.append(f'- **Failed:** {repo_f}  \n')
    lines.append(f'- **Status:** {"✅ PASS" if status == "PASS" else "❌ FAIL"}  \n\n')

    for section_name, txt in sections:
        lines.append(f'## [{display}] {section_name}\n\n')
        lines.append(f'```\n{txt}\n```\n\n')

    lines.append('---\n\n')


# Chord-partition (local)
cp_file = SELF / 'test_chord_partition_modes.py'
display_cp = 'chord-partition (local)'
print(f'\n[{display_cp}]  expected=103')
if cp_file.exists():
    env_cp = make_env(SELF)
    try:
        r = subprocess.run(
            [sys.executable, '-m', 'pytest', str(cp_file), '-v',
             '--tb=long', '--no-header', '--color=no'],
            capture_output=True, text=True, encoding='utf-8', errors='replace',
            timeout=120, env=env_cp, cwd=str(SELF)
        )
        txt = r.stdout + r.stderr
        p = int(m.group(1)) if (m := re.search(r'(\d+) passed', txt)) else 0
        f = int(m.group(1)) if (m := re.search(r'(\d+) failed', txt)) else 0
        grand_passed += p
        grand_failed += f
        status = 'PASS' if f == 0 and p > 0 else 'FAIL'
        print(f'  -> passed={p}  failed={f}  {status}')
        lines.append(f'# {display_cp}\n\n')
        lines.append(f'- **Expected:** 103  \n')
        lines.append(f'- **Passed:** {p}  \n')
        lines.append(f'- **Failed:** {f}  \n')
        lines.append(f'- **Status:** {"✅ PASS" if status == "PASS" else "❌ FAIL"}  \n\n')
        lines.append(f'## [{display_cp}] pytest -v\n\n```\n{txt}\n```\n\n---\n\n')
    except Exception as ex:
        print(f'  ERROR: {ex}')

# Summary
grand_expected = sum(expected for _, _, expected, _ in REPOS) + 103
rate = (f'{grand_passed / grand_expected * 100:.1f}%'
        if grand_expected > 0 else 'N/A')
verdict = '✅ VERIFIED' if grand_failed == 0 and grand_passed == grand_expected else '❌ FAIL'

lines.append('# SUMMARY\n\n')
lines.append(f'| Metric | Value |\n|--------|-------|\n')
lines.append(f'| Total Expected | {grand_expected} |\n')
lines.append(f'| Total Passed | {grand_passed} |\n')
lines.append(f'| Total Failed | {grand_failed} |\n')
lines.append(f'| Pass Rate | {rate} |\n')
lines.append(f'| Verdict | {verdict} |\n\n')

print('\n' + '=' * 65)
print(f'Grand total: passed={grand_passed}  failed={grand_failed}  rate={rate}')
print('=' * 65)

out_path = OUT / 'really-full-output.md'
with open(out_path, 'w', encoding='utf-8') as fh:
    fh.write(''.join(lines))

print(f'\nWritten: {out_path}')
print(f'File size: {out_path.stat().st_size / 1024:.1f} KB')
