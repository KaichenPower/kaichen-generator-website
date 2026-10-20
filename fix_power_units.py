# -*- coding: utf-8 -*-
"""Fix power units in translated blog files: revert localized kW/kVA back to English."""
import glob, re

# Patterns to replace in translated blog files
# These are localized versions of kW/kVA that should be reverted to English
replacements = [
    # Russian
    ('кВт', 'kW'),
    ('кВА', 'kVA'),
    # Arabic
    ('كيلوواط', 'kW'),
    ('كيلو فولت أمبير', 'kVA'),
    ('كيلووفولت أمبير', 'kVA'),
    # Thai
    ('กิโลวัตต์', 'kW'),
    ('กิโลโวลต์แอมแปร์', 'kVA'),
    # Vietnamese
    ('kW', 'kW'),  # already correct
    # Indonesian
    ('kW', 'kW'),  # already correct
    # Spanish
    ('kW', 'kW'),  # already correct
    # French
    ('kW', 'kW'),  # already correct
    # German
    ('kW', 'kW'),  # already correct
    # Portuguese
    ('kW', 'kW'),  # already correct
    # Turkish
    ('kW', 'kW'),  # already correct
]

count = 0
for f in glob.glob('content/blog/*/*.md'):
    raw = open(f, encoding='utf-8').read()
    orig = raw
    for old, new in replacements:
        if old != new:
            raw = raw.replace(old, new)
    if raw != orig:
        open(f, 'w', encoding='utf-8').write(raw)
        count += 1
        print(f'Fixed: {f}')

print(f'\nTotal files fixed: {count}')
