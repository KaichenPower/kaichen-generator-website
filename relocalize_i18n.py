# -*- coding: utf-8 -*-
"""Re-localize kVA/kW in i18n JSON files for ru/ar/th."""
import json

locale_map = {
    'ru': {'kVA': 'кВА', 'kW': 'кВт'},
    'ar': {'kVA': 'كيلو فولت أمبير', 'kW': 'كيلوواط'},
    'th': {'kVA': 'กิโลโวลต์แอมแปร์', 'kW': 'กิโลวัตต์'},
}

for loc, units in locale_map.items():
    p = f'content/i18n/{loc}.json'
    d = json.load(open(p, encoding='utf-8'))
    s = json.dumps(d, ensure_ascii=False)
    for en, localized in units.items():
        s = s.replace(en, localized)
    d2 = json.loads(s)
    json.dump(d2, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f'Re-localized {loc}')

print('Done!')
