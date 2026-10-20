# -*- coding: utf-8 -*-
import os, re, glob

# Map locale -> (kw_replacement, kva_replacement)
locales = {
    'ar': ('كيلوواط', 'كيلو فولت أمبير'),
    'th': ('กิโลวัตต์', 'กิโลโวลต์แอมแปร์'),
}

base = 'content/blog'
for loc, (kw_word, kva_word) in locales.items():
    files = glob.glob(os.path.join(base, loc, '*.md'))
    for fp in files:
        raw = open(fp, encoding='utf-8').read()
        # Split frontmatter and body
        parts = raw.split('---', 2)
        if len(parts) < 3:
            continue
        fm = parts[1]
        body = parts[2]
        orig_body = body
        # Replace kVA first (longer pattern), then kW
        # Pattern: number + optional space + kVA
        body = re.sub(r'(\d[\d,.]*)\s*kVA', lambda m: f'{m.group(1)} {kva_word}', body, flags=re.IGNORECASE)
        body = re.sub(r'(\d[\d,.]*)\s*kW', lambda m: f'{m.group(1)} {kw_word}', body, flags=re.IGNORECASE)
        if body != orig_body:
            out = f'---{fm}---{body}'
            open(fp, 'w', encoding='utf-8').write(out)
            print(f'Fixed {loc}/{os.path.basename(fp)}')
print('Done!')
