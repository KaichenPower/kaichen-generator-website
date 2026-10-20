import json, os

for loc in os.listdir('content/i18n'):
    if not loc.endswith('.json'): continue
    path = f'content/i18n/{loc}'
    with open(path,'r',encoding='utf-8') as f:
        d = json.load(f)
    priv = d.get('privacy',{})
    for k,v in priv.get('sections',{}).items():
        paras = v.get('paragraphs',{})
        if isinstance(paras, dict):
            for j in paras:
                paras[j] = paras[j].replace('www.cnkcpower.com', 'www.dgsetmanufacturer.com')
        elif isinstance(paras, list):
            v['paragraphs'] = [p.replace('www.cnkcpower.com', 'www.dgsetmanufacturer.com') for p in paras]
    with open(path,'w',encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"Updated {loc}")
