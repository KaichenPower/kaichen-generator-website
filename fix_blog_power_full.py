# -*- coding: utf-8 -*-
import os, re, glob, yaml as y

# Comprehensive power unit localization in ALL blog files.
# Process: protect image paths -> replace kW/kVA everywhere (frontmatter title/excerpt + body) -> restore image paths.

locales = {
    'ru': ('кВт', 'кВА'),
    'ar': ('كيلوواط', 'كيلو فولت أمبير'),
    'th': ('กิโลวัตต์', 'กิโลโวลต์แอมแปร์'),
}

# Other locales (es/fr/de/pt/tr/vi/id) keep kW/kVA as-is (international notation)

base = 'content/blog'
total_fixed = 0

for loc, (kw_word, kva_word) in locales.items():
    files = glob.glob(os.path.join(base, loc, '*.md'))
    for fp in files:
        raw = open(fp, encoding='utf-8').read()
        orig = raw

        # Step 1: Protect image paths by replacing them with placeholders
        images = []
        def stash_img(m):
            images.append(m.group(0))
            return f'@@IMG{len(images)-1}@@'
        protected = re.sub(r'!\[[^\]]*\]\([^)]+\)', stash_img, raw)

        # Step 2: Replace kVA first, then kW (case insensitive, with optional space)
        protected = re.sub(r'(\d[\d,.]*)\s*kVA\b', lambda m: f'{m.group(1)} {kva_word}', protected, flags=re.IGNORECASE)
        protected = re.sub(r'(\d[\d,.]*)\s*kW\b', lambda m: f'{m.group(1)} {kw_word}', protected, flags=re.IGNORECASE)

        # Step 3: Restore image paths
        for i, img in enumerate(images):
            protected = protected.replace(f'@@IMG{i}@@', img)

        if protected != orig:
            open(fp, 'w', encoding='utf-8').write(protected)
            total_fixed += 1
            # Show what changed in title for logging
            parts = protected.split('---', 2)
            if len(parts) >= 3:
                fm = y.safe_load(parts[1])
                title = fm.get('title', '')[:80]
                print(f'  {os.path.basename(fp)}: {title}')

print(f'\nDone! {total_fixed} files updated across {list(locales.keys())} locales.')
