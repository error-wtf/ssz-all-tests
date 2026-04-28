#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SSZ Book Enrichment Script
==========================
Adds missing DE chapters to EN and IT without deleting anything.
DE = mathematical master (974 equations, 42 chapters)

Authors: Carmen N. Wrede & Lino P. Casu
"""
import re, sys, os, shutil
from pathlib import Path
from datetime import datetime

os.environ['PYTHONIOENCODING'] = 'utf-8'
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

BASE = Path('H:/SSZ_BOOK_PROJECT/05_OUTPUT')
BACKUP = BASE / 'BACKUPS'
BACKUP.mkdir(exist_ok=True)

DE_FILE = BASE / 'SSZ_BOOK_DE.tex'
EN_FILE = BASE / 'SSZ_BOOK_EN.tex'
IT_FILE = BASE / 'SSZ_BOOK_IT_V43.tex'

ts = datetime.now().strftime('%Y%m%d_%H%M%S')

print('Creating backups...')
shutil.copy2(EN_FILE, BACKUP / f'SSZ_BOOK_EN_backup_{ts}.tex')
shutil.copy2(IT_FILE, BACKUP / f'SSZ_BOOK_IT_V43_backup_{ts}.tex')

de_text = DE_FILE.read_text(encoding='utf-8', errors='replace')
en_text = EN_FILE.read_text(encoding='utf-8', errors='replace')
it_text = IT_FILE.read_text(encoding='utf-8', errors='replace')

def extract_chapters(text):
    parts = re.split(r'(\\chapter\{[^}]+\})', text)
    chapters = []
    i = 1
    while i < len(parts) - 1:
        title_cmd = parts[i]
        body = parts[i + 1] if i + 1 < len(parts) else ''
        title = re.search(r'\\chapter\{([^}]+)\}', title_cmd)
        if title:
            chapters.append((title.group(1), title_cmd + body))
        i += 2
    return chapters

def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())[:30]

de_chapters = extract_chapters(de_text)
en_chapters = extract_chapters(en_text)
it_chapters = extract_chapters(it_text)

de_norm = {norm(c[0]): c for c in de_chapters}
en_norm = {norm(c[0]): c for c in en_chapters}
it_norm = {norm(c[0]): c for c in it_chapters}

de_missing_in_en = [(k, v) for k, v in de_norm.items() if k not in en_norm]
de_missing_in_it = [(k, v) for k, v in de_norm.items() if k not in it_norm]

print(f'DE: {len(de_chapters)} | EN before: {len(en_chapters)} | IT before: {len(it_chapters)}')
print(f'Missing in EN: {len(de_missing_in_en)} | Missing in IT: {len(de_missing_in_it)}')

def enrich_book(text, missing_chapters, lang_note):
    if not missing_chapters:
        return text, 0
    block = f'\n\n%% ENRICHMENT FROM DE MASTER ({ts})\n'
    block += f'%% {len(missing_chapters)} chapters added\n'
    block += f'%% Note: {lang_note}\n\n'
    for key, (title, body) in missing_chapters:
        block += f'%% --- {title[:60]} ---\n' + body + '\n\n'
    if r'\end{document}' in text:
        text = text.replace(r'\end{document}', block + r'\end{document}', 1)
    else:
        text += block
    return text, len(missing_chapters)

en_new, en_added = enrich_book(en_text, de_missing_in_en, 'German - needs EN translation')
it_new, it_added = enrich_book(it_text, de_missing_in_it, 'German - needs IT translation')

assert len(en_new) > len(en_text)
assert len(it_new) > len(it_text)

EN_FILE.write_text(en_new, encoding='utf-8')
IT_FILE.write_text(it_new, encoding='utf-8')

print(f'EN: {len(en_chapters)} -> {len(en_chapters)+en_added} chapters')
print(f'IT: {len(it_chapters)} -> {len(it_chapters)+it_added} chapters')
print('DONE. NO DELETIONS.')
