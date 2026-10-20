"""Extract all product content and batch-translate to 10 locales."""
import yaml, os, json, sys

LOCALES = ['ru','es','fr','de','pt','ar','tr','th','vi','id']

# Load all products
products = []
for f in sorted(os.listdir('content/products')):
    if not f.endswith('.yaml'): continue
    with open(f'content/products/{f}', encoding='utf-8') as fh:
        p = yaml.safe_load(fh)
        p['_file'] = f.replace('.yaml','')
        products.append(p)

print(f'Total: {len(products)} products')

# Build translation map: for each product slug, collect all strings to translate
# We'll output a JSON file with all English strings grouped by product
todo = {}
for p in products:
    slug = p['_file']
    todo[slug] = {
        'description': p.get('description') or '',
        'features': p.get('features') or [],
        'applications': p.get('applications') or [],
        'problems': p.get('problems') or [],
    }

with open('content/_product_todo.json', 'w', encoding='utf-8') as f:
    json.dump(todo, f, ensure_ascii=False, indent=2)

# Print summary
total_strings = 0
for slug, data in todo.items():
    n = 1 + len(data['features']) + len(data['applications']) + len(data['problems'])
    total_strings += n
    print(f'  {slug}: {n} strings')
print(f'Total strings to translate: {total_strings} x 10 locales = {total_strings*10}')
