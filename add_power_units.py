# -*- coding: utf-8 -*-
"""Add powerUnits namespace to all i18n JSON files."""
import json

power_units = {
    'en': {'kw': 'kW', 'kva': 'kVA'},
    'ru': {'kw': 'кВт', 'kva': 'кВА'},
    'es': {'kw': 'kW', 'kva': 'kVA'},
    'fr': {'kw': 'kW', 'kva': 'kVA'},
    'de': {'kw': 'kW', 'kva': 'kVA'},
    'pt': {'kw': 'kW', 'kva': 'kVA'},
    'ar': {'kw': 'كيلوواط', 'kva': 'كيلو فولت أمبير'},
    'tr': {'kw': 'kW', 'kva': 'kVA'},
    'th': {'kw': 'กิโลวัตต์', 'kva': 'กิโลโวลต์แอมแปร์'},
    'vi': {'kw': 'kW', 'kva': 'kVA'},
    'id': {'kw': 'kW', 'kva': 'kVA'},
}

for loc, units in power_units.items():
    p = f'content/i18n/{loc}.json'
    d = json.load(open(p, encoding='utf-8'))
    d['powerUnits'] = units
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f'Added powerUnits to {loc}')

print('Done!')
