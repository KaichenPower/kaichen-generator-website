import json
import os

base_dir = "D:/projects/kaichen-generator-website/content/i18n"

# 各页面的 description 翻译
descriptions = {
    "en": {
        "aboutPage": {
            "description": "Learn about Kaichen Power - a professional diesel generator set manufacturer in Yangzhou, China since 2013, with 36,000 m² factory and 8,000 units annual capacity."
        },
        "legal": {
            "privacyDescription": "Privacy Policy of Kaichen Power - how we collect, use and protect your personal information when you visit our website or submit enquiries.",
            "termsDescription": "Terms of Service of Kaichen Power - the terms and conditions for using our website and purchasing diesel generator sets."
        }
    },
    "ru": {
        "aboutPage": {
            "description": "Узнайте о Kaichen Power - профессиональном производителе дизель-генераторных установок в Янчжоу, Китай, с 2013 года, завод 36 000 м² и 8 000 единиц в год."
        },
        "legal": {
            "privacyDescription": "Политика конфиденциальности Kaichen Power - как мы собираем, используем и защищаем вашу личную информацию при посещении нашего сайта.",
            "termsDescription": "Условия использования Kaichen Power - положения и условия использования нашего сайта и покупки дизель-генераторных установок."
        }
    },
    "es": {
        "aboutPage": {
            "description": "Conozca Kaichen Power - fabricante profesional de grupos electrógenos diésel en Yangzhou, China desde 2013, fábrica de 36.000 m² y 8.000 unidades anuales."
        },
        "legal": {
            "privacyDescription": "Política de privacidad de Kaichen Power - cómo recopilamos, utilizamos y protegemos su información personal cuando visita nuestro sitio web.",
            "termsDescription": "Términos de servicio de Kaichen Power - los términos y condiciones para usar nuestro sitio web y comprar grupos electrógenos diésel."
        }
    },
    "fr": {
        "aboutPage": {
            "description": "Découvrez Kaichen Power - fabricant professionnel de groupes électrogènes diesel à Yangzhou, Chine depuis 2013, usine de 36 000 m² et 8 000 unités par an."
        },
        "legal": {
            "privacyDescription": "Politique de confidentialité de Kaichen Power - comment nous collectons, utilisons et protégeons vos informations personnelles lorsque vous visitez notre site web.",
            "termsDescription": "Conditions d'utilisation de Kaichen Power - les termes et conditions pour utiliser notre site web et acheter des groupes électrogènes diesel."
        }
    },
    "de": {
        "aboutPage": {
            "description": "Erfahren Sie mehr über Kaichen Power - professioneller Dieselgenerator-Hersteller in Yangzhou, China seit 2013, 36.000 m² Fabrik und 8.000 Einheiten jährlich."
        },
        "legal": {
            "privacyDescription": "Datenschutzrichtlinie von Kaichen Power - wie wir Ihre persönlichen Daten sammeln, verwenden und schützen, wenn Sie unsere Website besuchen.",
            "termsDescription": "Nutzungsbedingungen von Kaichen Power - die Bedingungen für die Nutzung unserer Website und den Kauf von Dieselgeneratoren."
        }
    },
    "pt": {
        "aboutPage": {
            "description": "Conheça a Kaichen Power - fabricante profissional de geradores a diesel em Yangzhou, China desde 2013, fábrica de 36.000 m² e 8.000 unidades por ano."
        },
        "legal": {
            "privacyDescription": "Política de Privacidade da Kaichen Power - como coletamos, usamos e protegemos suas informações pessoais quando você visita nosso site.",
            "termsDescription": "Termos de Serviço da Kaichen Power - os termos e condições para usar nosso site e comprar geradores a diesel."
        }
    },
    "ar": {
        "aboutPage": {
            "description": "تعرف على شركة Kaichen Power - شركة محترفة لتصنيع مولدات الديزل في يانغتشو، الصين منذ عام 2013، مصنع 36000 متر مربع و 8000 وحدة سنوياً."
        },
        "legal": {
            "privacyDescription": "سياسة الخصوصية لشركة Kaichen Power - كيف نجمع ونستخدم ونحمي معلوماتك الشخصية عند زيارة موقعنا الإلكتروني.",
            "termsDescription": "شروط الخدمة لشركة Kaichen Power - الشروط والأحكام الخاصة باستخدام موقعنا الإلكتروني وشراء مولدات الديزل."
        }
    },
    "tr": {
        "aboutPage": {
            "description": "Kaichen Power hakkında bilgi edinin - 2013'ten beri Yangzhou, Çin'de profesyonel dizel jeneratör üreticisi, 36.000 m² fabrika ve yılda 8.000 ünite."
        },
        "legal": {
            "privacyDescription": "Kaichen Power Gizlilik Politikası - web sitemizi ziyaret ettiğinizde kişisel bilgilerinizi nasıl topladığımızı, kullandığımızı ve koruduğumuzu öğrenin.",
            "termsDescription": "Kaichen Power Hizmet Şartları - web sitemizi kullanmak ve dizel jeneratör satın almak için şartlar ve koşullar."
        }
    },
    "th": {
        "aboutPage": {
            "description": "ทำความรู้จักกับ Kaichen Power - ผู้ผลิตเครื่องกำเนิดไฟฟ้าดีเซลมืออาชีพในเมืองหยางโจว ประเทศจีน ตั้งแต่ปี 2013 โรงงาน 36,000 ตารางเมตร และ 8,000 ยูนิตต่อปี"
        },
        "legal": {
            "privacyDescription": "นโยบายความเป็นส่วนตัวของ Kaichen Power - วิธีที่เราเก็บรวบรวม ใช้ และปกป้องข้อมูลส่วนบุคคลของคุณเมื่อคุณเยี่ยมชมเว็บไซต์ของเรา",
            "termsDescription": "ข้อกำหนดการให้บริการของ Kaichen Power - ข้อกำหนดและเงื่อนไขสำหรับการใช้งานเว็บไซต์ของเราและการซื้อเครื่องกำเนิดไฟฟ้าดีเซล"
        }
    },
    "vi": {
        "aboutPage": {
            "description": "Tìm hiểu về Kaichen Power - nhà sản xuất máy phát điện diesel chuyên nghiệp tại Yangzhou, Trung Quốc từ năm 2013, nhà máy 36.000 m² và 8.000 đơn vị mỗi năm."
        },
        "legal": {
            "privacyDescription": "Chính sách bảo mật của Kaichen Power - cách chúng tôi thu thập, sử dụng và bảo vệ thông tin cá nhân của bạn khi bạn truy cập trang web của chúng tôi.",
            "termsDescription": "Điều khoản dịch vụ của Kaichen Power - các điều khoản và điều kiện để sử dụng trang web của chúng tôi và mua máy phát điện diesel."
        }
    },
    "id": {
        "aboutPage": {
            "description": "Pelajari tentang Kaichen Power - produsen genset diesel profesional di Yangzhou, Tiongkok sejak 2013, pabrik 36.000 m² dan 8.000 unit per tahun."
        },
        "legal": {
            "privacyDescription": "Kebijakan Privasi Kaichen Power - bagaimana kami mengumpulkan, menggunakan, dan melindungi informasi pribadi Anda saat Anda mengunjungi situs web kami.",
            "termsDescription": "Ketentuan Layanan Kaichen Power - syarat dan ketentuan untuk menggunakan situs web kami dan membeli genset diesel."
        }
    }
}

for lang, data in descriptions.items():
    filepath = os.path.join(base_dir, f"{lang}.json")
    with open(filepath, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    
    # Update aboutPage
    if 'aboutPage' in json_data:
        json_data['aboutPage']['description'] = data['aboutPage']['description']
    
    # Update legal
    if 'legal' in json_data:
        json_data['legal']['privacyDescription'] = data['legal']['privacyDescription']
        json_data['legal']['termsDescription'] = data['legal']['termsDescription']
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    
    print(f"Updated {lang}")
