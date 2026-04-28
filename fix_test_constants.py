#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FIX TESTS - Korrigiere XI_MAX und D_MIN Werte in allen Test-Dateien

Die korrekten kanonischen SSZ-Werte:
- PHI = (1 + sqrt(5)) / 2 = 1.6180339887498949
- XI_MAX = 1 - exp(-PHI) = 0.8017118471377938
- D_MIN = 1 / (1 + XI_MAX) = 0.5550277096687818
"""

import os
import re
from pathlib import Path

BASE_DIR = Path("E:/clone/ssz-all-tests-test")

# Korrekte kanonische Werte
CORRECT_XI_MAX = 0.8017118471377938
CORRECT_D_MIN = 0.5550277096687818

# Alte falsche Werte die ersetzt werden sollen
FIXES = [
    (r'XI_MAX\s*=\s*0\.80[0-9]+', f'XI_MAX = {CORRECT_XI_MAX}'),
    (r'D_MIN\s*=\s*0\.55[0-9]+', f'D_MIN = {CORRECT_D_MIN}'),
    (r'Ξ_max\s*≈\s*0\.80[0-9]+', f'Ξ_max ≈ {CORRECT_XI_MAX:.5f}'),
    (r'D_min\s*≈\s*0\.55[0-9]+', f'D_min ≈ {CORRECT_D_MIN:.5f}'),
]


def fix_file(filepath):
    text = filepath.read_text(encoding='utf-8', errors='replace')
    orig = text
    for pattern, replacement in FIXES:
        text = re.sub(pattern, replacement, text)
    if text != orig:
        filepath.write_text(text, encoding='utf-8')
        return True
    return False


def main():
    fixed = 0
    for f in BASE_DIR.rglob('*.py'):
        if '.git' in str(f):
            continue
        if fix_file(f):
            print(f'FIXED: {f.relative_to(BASE_DIR)}')
            fixed += 1
    print(f'\nTotal fixed: {fixed} files')
    print(f'XI_MAX = {CORRECT_XI_MAX}')
    print(f'D_MIN  = {CORRECT_D_MIN}')


if __name__ == '__main__':
    main()
