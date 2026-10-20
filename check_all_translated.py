import json
locales = ['ru','es','fr','de','pt','ar','tr','th','vi','id']
for loc in locales:
    with open(f'content/i18n/{loc}.json','r',encoding='utf-8') as f:
        d = json.load(f)
    p = d.get('privacy',{}).get('sections',{}).get('1',{}).get('paragraphs',{}).get('0','')
    is_en = p.startswith('Welcome to')
    print(f"{loc}: {'ENGLISH' if is_en else 'TRANSLATED'} - {p[:60]}")
