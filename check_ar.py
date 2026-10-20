import json
with open('content/i18n/ar.json','r',encoding='utf-8') as f:
    d = json.load(f)
priv = d.get('privacy',{})
print("lastUpdated:", priv.get('lastUpdated',''))
for k,v in priv.get('sections',{}).items():
    print(f"\nSection {k}: {v.get('heading','')}")
    for j,p in v.get('paragraphs',{}).items():
        print(f"  [{j}] {p[:100]}")
