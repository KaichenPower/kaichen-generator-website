import json

translations = {
    "en": "All", "ru": "Все", "es": "Todos", "fr": "Tous",
    "de": "Alle", "pt": "Todos", "ar": "الكل", "tr": "Tümü",
    "th": "ทั้งหมด", "vi": "Tất cả", "id": "Semua",
}

for loc, label in translations.items():
    path = f'content/i18n/{loc}.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data['aboutPage']['certAllLabel'] = label
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'{loc}: {label}')
