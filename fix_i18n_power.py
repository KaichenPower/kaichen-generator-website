# -*- coding: utf-8 -*-
"""Fix localized power units in all i18n JSON files."""
import json, glob

# Localized power units to revert to English
replacements = {
    'кВт': 'kW',
    'кВА': 'kVA',
    'КВТ': 'kW',
    'КВА': 'kVA',
    'كيلوواط': 'kW',
    'كيلو فولت أمبير': 'kVA',
    'كيلووفولت أمبير': 'kVA',
    'กิโลวัตต์': 'kW',
    'กิโลโวลต์แอมแปร์': 'kVA',
}

count = 0
for f in sorted(glob.glob('content/i18n/*.json')):
    raw = open(f, encoding='utf-8').read()
    orig = raw
    for old, new in replacements.items():
        raw = raw.replace(old, new)
    if raw != orig:
        open(f, 'w', encoding='utf-8').write(raw)
        count += 1
        print(f'Fixed: {f}')

print(f'\nTotal files fixed: {count}')
