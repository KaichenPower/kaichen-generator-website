# -*- coding: utf-8 -*-
import glob, yaml
for f in sorted(glob.glob('content/blog/*/*.md')):
    try:
        raw = open(f, encoding='utf-8').read()
        parts = raw.split('---', 2)
        if len(parts) < 3:
            print(f'BAD PARTS: {f}')
            continue
        fm = yaml.safe_load(parts[1])
        if not fm or 'title' not in fm:
            print(f'NO TITLE: {f}')
    except Exception as e:
        print(f'ERROR {f}: {e}')
print('check done')
