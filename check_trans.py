import json, os
locales = ['en','ru','es','fr','de','pt','ar','tr','th','vi','id']
print("=== Product translation check ===")
for loc in locales:
    d = json.load(open(f'content/i18n/{loc}.json','r',encoding='utf-8'))
    p = d.get('products',{}).get('cummins-50-silent',{})
    if p:
        name = p.get('name','MISSING')[:60]
        print(f'{loc}: {name}')
    else:
        print(f'{loc}: MISSING')

print("\n=== Blog translation check ===")
for loc in locales:
    path = f'content/blog/{loc}/generator-maintenance-checklist.md'
    exists = os.path.exists(path)
    print(f'{loc}: {"EXISTS" if exists else "MISSING"}')
