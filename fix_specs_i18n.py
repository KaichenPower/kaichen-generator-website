import json, os

# 1. Add dimensions & weight to specLabels in all locales
spec_label_translations = {
    'en': {'dimensions': 'Dimensions', 'weight': 'Weight'},
    'ru': {'dimensions': 'Габариты', 'weight': 'Масса'},
    'es': {'dimensions': 'Dimensiones', 'weight': 'Peso'},
    'fr': {'dimensions': 'Dimensions', 'weight': 'Poids'},
    'de': {'dimensions': 'Abmessungen', 'weight': 'Gewicht'},
    'pt': {'dimensions': 'Dimensões', 'weight': 'Peso'},
    'ar': {'dimensions': 'الأبعاد', 'weight': 'الوزن'},
    'tr': {'dimensions': 'Boyutlar', 'weight': 'Ağırlık'},
    'th': {'dimensions': 'ขนาด', 'weight': 'น้ำหนัก'},
    'vi': {'dimensions': 'Kích thước', 'weight': 'Trọng lượng'},
    'id': {'dimensions': 'Dimensi', 'weight': 'Berat'},
}

# 2. Add new spec values to specValues
spec_value_translations = {
    'en': {
        'stamfordLeroyBrushless': 'Stamford / Leroy-Somer brushless',
        'deepseaComApAmf': 'Deepsea or ComAp AMF controller',
        'voltage3phase': '400/230V, 50Hz, 3-phase',
        'tank120': '120L built-in',
        'noiseLe68': '≤68 dB(A) @ 7m',
        'engine4bt': 'Cummins 4BT3.9-G2',
    },
    'ru': {
        'stamfordLeroyBrushless': 'Stamford / Leroy-Somer бесщёточный',
        'deepseaComApAmf': 'Контроллер Deepsea или ComAp с АВР',
        'voltage3phase': '400/230В, 50Гц, 3-фазы',
        'tank120': 'Встроенный 120л',
        'noiseLe68': '≤68 дБ(A) на 7м',
        'engine4bt': 'Cummins 4BT3.9-G2',
    },
    'es': {
        'stamfordLeroyBrushless': 'Stamford / Leroy-Somer sin escobillas',
        'deepseaComApAmf': 'Controlador Deepsea o ComAp AMF',
        'voltage3phase': '400/230V, 50Hz, trifásico',
        'tank120': '120L integrado',
        'noiseLe68': '≤68 dB(A) @ 7m',
        'engine4bt': 'Cummins 4BT3.9-G2',
    },
    'fr': {
        'stamfordLeroyBrushless': 'Stamford / Leroy-Somer sans balais',
        'deepseaComApAmf': 'Contrôleur Deepsea ou ComAp AMF',
        'voltage3phase': '400/230V, 50Hz, triphasé',
        'tank120': '120L intégré',
        'noiseLe68': '≤68 dB(A) @ 7m',
        'engine4bt': 'Cummins 4BT3.9-G2',
    },
    'de': {
        'stamfordLeroyBrushless': 'Stamford / Leroy-Somer bürstenlos',
        'deepseaComApAmf': 'Deepsea oder ComAp AMF Steuergerät',
        'voltage3phase': '400/230V, 50Hz, 3-phasig',
        'tank120': '120L integriert',
        'noiseLe68': '≤68 dB(A) @ 7m',
        'engine4bt': 'Cummins 4BT3.9-G2',
    },
    'pt': {
        'stamfordLeroyBrushless': 'Stamford / Leroy-Somer sem escovas',
        'deepseaComApAmf': 'Controlador Deepsea ou ComAp AMF',
        'voltage3phase': '400/230V, 50Hz, trifásico',
        'tank120': '120L integrado',
        'noiseLe68': '≤68 dB(A) @ 7m',
        'engine4bt': 'Cummins 4BT3.9-G2',
    },
    'ar': {
        'stamfordLeroyBrushless': 'Stamford / Leroy-Somer بدون فرش',
        'deepseaComApAmf': 'جهاز تحكم Deepsea أو ComAp AMF',
        'voltage3phase': '400/230V, 50Hz, ثلاثي الطور',
        'tank120': '120 لتر مدمج',
        'noiseLe68': '≤68 ديسيبل @ 7م',
        'engine4bt': 'Cummins 4BT3.9-G2',
    },
    'tr': {
        'stamfordLeroyBrushless': 'Stamford / Leroy-Somer fırçasız',
        'deepseaComApAmf': 'Deepsea veya ComAp AMF kontrol cihazı',
        'voltage3phase': '400/230V, 50Hz, 3 fazlı',
        'tank120': '120L dahili',
        'noiseLe68': '≤68 dB(A) @ 7m',
        'engine4bt': 'Cummins 4BT3.9-G2',
    },
    'th': {
        'stamfordLeroyBrushless': 'Stamford / Leroy-Somer ไม่มีแปรงถ่าน',
        'deepseaComApAmf': 'เครื่องควบคุม Deepsea หรือ ComAp AMF',
        'voltage3phase': '400/230V, 50Hz, 3 เฟส',
        'tank120': '120 ลิตรในตัว',
        'noiseLe68': '≤68 dB(A) @ 7 ม.',
        'engine4bt': 'Cummins 4BT3.9-G2',
    },
    'vi': {
        'stamfordLeroyBrushless': 'Stamford / Leroy-Somer không chổi than',
        'deepseaComApAmf': 'Bộ điều khiển Deepsea hoặc ComAp AMF',
        'voltage3phase': '400/230V, 50Hz, 3 pha',
        'tank120': '120L tích hợp',
        'noiseLe68': '≤68 dB(A) @ 7m',
        'engine4bt': 'Cummins 4BT3.9-G2',
    },
    'id': {
        'stamfordLeroyBrushless': 'Stamford / Leroy-Somer brushless',
        'deepseaComApAmf': 'Pengontrol Deepsea atau ComAp AMF',
        'voltage3phase': '400/230V, 50Hz, 3 fasa',
        'tank120': '120L terintegrasi',
        'noiseLe68': '≤68 dB(A) @ 7m',
        'engine4bt': 'Cummins 4BT3.9-G2',
    },
}

locales = ['en','ru','es','fr','de','pt','ar','tr','th','vi','id']

for loc in locales:
    path = f'content/i18n/{loc}.json'
    with open(path, 'r', encoding='utf-8') as f:
        d = json.load(f)
    # Add specLabels
    if 'specLabels' not in d:
        d['specLabels'] = {}
    d['specLabels']['dimensions'] = spec_label_translations[loc]['dimensions']
    d['specLabels']['weight'] = spec_label_translations[loc]['weight']
    # Add specValues
    if 'specValues' not in d:
        d['specValues'] = {}
    for k, v in spec_value_translations[loc].items():
        d['specValues'][k] = v
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f'Updated {loc}')
