import json
with open('content/i18n/en.json','r',encoding='utf-8') as f:
    d = json.load(f)
priv = d.get('privacy',{})
print("Sections count:", len(priv.get('sections',{})))
for k,v in priv.get('sections',{}).items():
    paras = v.get('paragraphs',{})
    print(f"  Section {k}: heading={v.get('heading','')[:50]}, paras type={type(paras).__name__}, count={len(paras) if isinstance(paras,(dict,list)) else 'N/A'}")
