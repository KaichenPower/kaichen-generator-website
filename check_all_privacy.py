import json, os
locales = ['en','ru','es','fr','de','pt','ar','tr','th','vi','id']
for loc in locales:
    path = f'content/i18n/{loc}.json'
    with open(path,'r',encoding='utf-8') as f:
        d = json.load(f)
    priv = d.get('privacy',{})
    sections = priv.get('sections',{})
    total_paras = 0
    for k,v in sections.items():
        paras = v.get('paragraphs',{})
        total_paras += len(paras) if isinstance(paras,dict) else 0
    print(f"{loc}: {len(sections)} sections, {total_paras} paragraphs")
