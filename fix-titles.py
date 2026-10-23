import json
import os

base_dir = "D:/projects/kaichen-generator-website/content/i18n"

# 缩短后的品牌名（从49字符缩短到约35字符）
new_brand = {
    "en": "Kaichen Power | Diesel Generator Manufacturer",
    "ru": "Kaichen Power | Производитель дизель-генераторов",
    "es": "Kaichen Power | Fabricante de generadores diésel",
    "fr": "Kaichen Power | Fabricant de groupes électrogènes diesel",
    "de": "Kaichen Power | Dieselgenerator Hersteller",
    "pt": "Kaichen Power | Fabricante de geradores a diesel",
    "ar": "Kaichen Power | الشركة المصنعة لمولدات الديزل",
    "tr": "Kaichen Power | Dizel Jeneratör Üreticisi",
    "th": "Kaichen Power | ผู้ผลิตเครื่องกำเนิดไฟฟ้าดีเซล",
    "vi": "Kaichen Power | Nhà sản xuất máy phát điện diesel",
    "id": "Kaichen Power | Produsen Genset Diesel"
}

for lang, brand in new_brand.items():
    filepath = os.path.join(base_dir, f"{lang}.json")
    with open(filepath, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    
    json_data['meta']['title'] = brand
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    
    print(f"Updated {lang}: {brand} ({len(brand)} chars)")
