#!/usr/bin/env python3
"""Generate docs landing pages from the canonical AGENTS.md."""
from pathlib import Path
from html import escape
import shutil

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / 'docs'
contract = (ROOT / 'AGENTS.md').read_text()
paragraphs = '\n'.join('<p>' + escape(p) + '</p>' for p in contract.strip().split('\n\n')[1:])
for name in ('index.html', 'ko.html'):
    template = (ROOT / 'templates' / name).read_text()
    page = template.replace('@@PARAGRAPHS@@', paragraphs).replace('@@CONTRACT@@', contract)
    (DOCS / name).write_text(page)
    print(f'Generated docs/{name}')
shutil.copyfile(ROOT / 'AGENTS.md', DOCS / 'AGENTS.md')
for archive in (ROOT / 'archive').glob('*.md'):
    shutil.copyfile(archive, DOCS / 'archive' / archive.name)
(DOCS / '.nojekyll').touch()
# Keep the old corridor URL reachable as an explicitly archived experience.
(DOCS / 'level.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=archive/level.html"><title>Previous prompt</title><a href="archive/level.html">Open the archived seven-step experience</a></html>\n')
