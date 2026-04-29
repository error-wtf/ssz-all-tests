#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, os
from pathlib import Path

cwd = Path('E:/clone/ssz-all-tests')

# Remove this script first
subprocess.run(['git', 'rm', '--cached', '--force', 'commit_final.py'], cwd=cwd, capture_output=True)

r = subprocess.run(['git', 'add', '-A'], cwd=cwd, capture_output=True, text=True, encoding='utf-8')
print('add:', r.returncode)

r = subprocess.run(
    ['git', 'commit', '-m', 'fix: rename TestCh->TestMod, fix stored output, 0 book references'],
    cwd=cwd, capture_output=True, text=True, encoding='utf-8'
)
print(r.stdout.strip())
if r.stderr.strip(): print(r.stderr.strip())

r = subprocess.run(['git', 'push'], cwd=cwd, capture_output=True, text=True, encoding='utf-8')
print('push:', r.stdout.strip(), r.stderr.strip())
print('EXIT:', r.returncode)

# Self-delete
Path(__file__).unlink()
