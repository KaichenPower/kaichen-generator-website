import json
import os

base_dir = "D:/projects/kaichen-generator-website/content/i18n"

# Doosan 在各语言中的名称（用于匹配）
doosan_names = {
    "en": "Doosan",
    "ru": "Doosan",
    "es": "Doosan",
    "fr": "Doosan",
    "de": "Doosan",
    "pt": "Doosan",
    "ar": "Doosan",
    "tr": "Doosan",
    "th": "Doosan",
    "vi": "Doosan",
    "id": "Doosan",
}

for lang in doosan_names:
    filepath = os.path.join(base_dir, f"{lang}.json")
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    
    # 1. 从产品分类中移除 Doosan
    if 'productsPage' in data and 'categories' in data['productsPage']:
        categories = data['productsPage']['categories']
        new_categories = [c for c in categories if c.get('name') != 'Doosan' and 'Doosan' not in c.get('name', '')]
        if len(new_categories) != len(categories):
            data['productsPage']['categories'] = new_categories
            modified = True
            print(f"  {lang}: Removed Doosan category")
    
    # 2. 从 features 文本中移除 Doosan
    if 'home' in data and 'features' in data['home']:
        for i, feat in enumerate(data['home']['features']):
            if 'Doosan' in feat.get('text', ''):
                feat['text'] = feat['text'].replace(', Doosan', '').replace('Doosan, ', '').replace('Doosan', '')
                modified = True
                print(f"  {lang}: Removed Doosan from home feature text")
    
    # 3. 从 about 页面文本中移除 Doosan
    if 'aboutPage' in data:
        for key in ['body2', 'body3']:
            if key in data['aboutPage'] and 'Doosan' in data['aboutPage'][key]:
                data['aboutPage'][key] = data['aboutPage'][key].replace(', Doosan', '').replace('Doosan, ', '').replace('Doosan', '')
                modified = True
                print(f"  {lang}: Removed Doosan from about page {key}")
    
    # 4. 移除 Doosan 产品相关的 i18n 键
    if 'productDetails' in data:
        keys_to_remove = [k for k in data['productDetails'] if 'doosan' in k.lower()]
        for k in keys_to_remove:
            del data['productDetails'][k]
            modified = True
            print(f"  {lang}: Removed productDetails.{k}")
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Updated {lang}")
    else:
        print(f"No changes in {lang}")
