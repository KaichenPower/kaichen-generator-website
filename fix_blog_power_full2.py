# -*- coding: utf-8 -*-
import os, re, glob, yaml as y

locales = {
    'ru': ('кВт', 'кВА'),
    'ar': ('كيلوواط', 'كيلو فولت أمبير'),
    'th': ('กิโลวัตต์', 'กิโลโวลต์แอมแปร์'),
}

base = 'content/blog'
total_fixed = 0

for loc, (kw_word, kva_word) in locales.items():
    files = glob.glob(os.path.join(base, loc, '*.md'))
    for fp in files:
        raw = open(fp, encoding='utf-8').read()
        orig = raw

        # Protect image markdown
        images = []
        def stash_img(m):
            images.append(m.group(0))
            return f'@@IMG{len(images)-1}@@'
        protected = re.sub(r'!\[[^\]]*\]\([^)]+\)', stash_img, raw)

        # Replace kVA first, then kW. No \b — use negative lookahead for latin letters only.
        # Match: number + optional spaces + kVA/kW, NOT followed by a latin letter (to avoid kVAx or kWxyz)
        protected = re.sub(
            r'(\d[\d,.]*)\s*kVA(?![a-zA-Z])',
            lambda m: f'{m.group(1)} {kva_word}',
            protected, flags=re.IGNORECASE
        )
        protected = re.sub(
            r'(\d[\d,.]*)\s*kW(?![a-zA-Z])',
            lambda m: f'{m.group(1)} {kw_word}',
            protected, flags=re.IGNORECASE
        )

        # Restore images
        for i, img in enumerate(images):
            protected = protected.replace(f'@@IMG{i}@@', img)

        if protected != orig:
            open(fp, 'w', encoding='utf-8').write(protected)
            total_fixed += 1
            parts = protected.split('---', 2)
            if len(parts) >= 3:
                fm = y.safe_load(parts[1])
                title = fm.get('title', '')[:90]
                print(f'  {os.path.basename(fp)}: {title}')

print(f'\nDone! {total_fixed} files updated.')
