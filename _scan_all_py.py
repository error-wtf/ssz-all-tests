from pathlib import Path
import re, sys

repos = {
    'ssz-qubits':                  Path('E:/clone/ssz-qubits'),
    'ssz-metric-pure':             Path('E:/clone/ssz-metric-pure'),
    'segmented-calculation-suite': Path('E:/clone/segmented-calculation-suite'),
    'ssz-schumann':                Path('E:/clone/ssz-schuhman-experiment'),
    'ssz-lensing':                 Path('E:/clone/ssz-lensing'),
    'Unified-Results':             Path('E:/clone/Segmented-Spacetime-Mass-Projection-Unified-Results'),
    'ssz-trajectories':            Path('E:/clone/ssz-trajectories'),
    'segmented-energy':            Path('E:/clone/segmented-energy'),
    'frequency-curvature-validation': Path('E:/clone/frequency-curvature-validation'),
    'g79-cygnus-test':             Path('E:/clone/g79-cygnus-test'),
    'ssz-lagrange':                Path('E:/clone/ssz-lagrange'),
}

SKIP = {'.venv', 'venv', '__pycache__', '.git', 'node_modules', '.tox', 'site-packages'}

out = []
for name, path in repos.items():
    out.append(f'\n=== {name} ===')
    for f in sorted(path.rglob('*.py')):
        if any(p in f.parts for p in SKIP):
            continue
        try:
            txt = f.read_text(encoding='utf-8', errors='replace')
        except Exception as e:
            out.append(f'  ERROR reading {f}: {e}')
            continue
        n_pytest   = len(re.findall(r'^def test_',        txt, re.MULTILINE))
        n_class    = len(re.findall(r'^class Test',       txt, re.MULTILINE))
        n_assert   = txt.count('assert ')
        has_main   = bool(re.search(r'if __name__.*__main__', txt))
        has_pass   = bool(re.search(r'PASS|print.*pass|print.*ok', txt, re.I))
        lines      = txt.count('\n')
        rel        = f.relative_to(path)

        tags = []
        if n_pytest > 0:
            tags.append(f'pytest:{n_pytest}')
        if n_class > 0 and n_pytest == 0:
            tags.append(f'class-test:{n_class}')
        if has_main:
            tags.append('__main__')
        if n_assert > 0 and n_pytest == 0:
            tags.append(f'assert:{n_assert}')
        if has_pass and n_pytest == 0:
            tags.append('prints-PASS')

        tag_str = ' | '.join(tags) if tags else '-'
        out.append(f'  {str(rel):<65} {tag_str}')

report = '\n'.join(out)
Path('E:/clone/ssz-all-tests/scan_report.txt').write_text(report, encoding='utf-8')
print(report)
