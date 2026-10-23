import json
import os

base_dir = "D:/projects/kaichen-generator-website/content/i18n"

# 11个语言的锚文本翻译
cta_translations = {
    "en": {
        "workshopCta": "Visit Our Factory",
        "aboutPreviewCta": "Learn About Kaichen Power"
    },
    "ru": {
        "workshopCta": "Посетите наш завод",
        "aboutPreviewCta": "Подробнее о Kaichen Power"
    },
    "es": {
        "workshopCta": "Visite nuestra fábrica",
        "aboutPreviewCta": "Conozca Kaichen Power"
    },
    "fr": {
        "workshopCta": "Visitez notre usine",
        "aboutPreviewCta": "En savoir plus sur Kaichen Power"
    },
    "de": {
        "workshopCta": "Besuchen Sie unser Werk",
        "aboutPreviewCta": "Mehr über Kaichen Power erfahren"
    },
    "pt": {
        "workshopCta": "Visite nossa fábrica",
        "aboutPreviewCta": "Saiba mais sobre a Kaichen Power"
    },
    "ar": {
        "workshopCta": "زر مصنعنا",
        "aboutPreviewCta": "اعرف المزيد عن Kaichen Power"
    },
    "tr": {
        "workshopCta": "Fabrikamızı ziyaret edin",
        "aboutPreviewCta": "Kaichen Power hakkında bilgi edinin"
    },
    "th": {
        "workshopCta": "เยี่ยมชมโรงงานของเรา",
        "aboutPreviewCta": "เรียนรู้เพิ่มเติมเกี่ยวกับ Kaichen Power"
    },
    "vi": {
        "workshopCta": "Thăm nhà máy của chúng tôi",
        "aboutPreviewCta": "Tìm hiểu thêm về Kaichen Power"
    },
    "id": {
        "workshopCta": "Kunjungi pabrik kami",
        "aboutPreviewCta": "Pelajari tentang Kaichen Power"
    }
}

for lang, cta in cta_translations.items():
    filepath = os.path.join(base_dir, f"{lang}.json")
    with open(filepath, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    
    # Add to home namespace
    if 'home' not in json_data:
        json_data['home'] = {}
    json_data['home']['workshopCta'] = cta['workshopCta']
    json_data['home']['aboutPreviewCta'] = cta['aboutPreviewCta']
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    
    print(f"Updated {lang}")
