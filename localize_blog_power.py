# -*- coding: utf-8 -*-
"""Revert power units in translated blog files back to localized forms."""
import glob

# Per-locale power units
locale_units = {
    'ru': {'kW': 'кВт', 'kVA': 'кВА'},
    'ar': {'kW': 'كيلوواط', 'kVA': 'كيلو فولت أمبير'},
    'th': {'kW': 'กิโลวัตต์', 'kVA': 'กิโลโวลต์แอมแปร์'},
    # es/fr/de/pt/tr/vi/id/en keep English
}

count = 0
for f in sorted(glob.glob('content/blog/*/*.md')):
    loc = f.split('\\')[1] if '\\' in f else f.split('/')[1]
    if loc not in locale_units:
        continue
    units = locale_units[loc]
    raw = open(f, encoding='utf-8').read()
    orig = raw
    # Replace standalone kW/kVA (with word boundary)
    import re
    for en, localized in units.items():
        # Replace "XXX kW" pattern (number followed by space then kW)
        raw = re.sub(r'(\d+)\s*' + en + r'\b', r'\1 ' + localized, raw)
    if raw != orig:
        open(f, 'w', encoding='utf-8').write(raw)
        count += 1
        print(f'Localized: {f}')

print(f'\nTotal files: {count}')
