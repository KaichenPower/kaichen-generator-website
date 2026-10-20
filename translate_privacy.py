"""Fix privacy sections to object format for next-intl."""
import json

privacy_en = {
  "lastUpdated": "Last Updated: October 2026",
  "sections": {
    "1": {
      "heading": "1. Introduction",
      "paragraphs": {
        "0": "Welcome to www.cnkcpower.com (hereinafter referred to as \"we\", \"us\", \"our\", or the \"Site\"). We are committed to protecting your privacy and ensuring you have a positive experience when browsing our Site.",
        "1": "This Cookie Privacy Policy explains what cookies are, how we use them, the types of cookies we use, and how you can control or delete them. This Policy is part of our broader Privacy Policy.",
        "2": "By using our Site, you consent to the use of cookies in accordance with this Policy. If you do not agree to our use of cookies, please adjust your browser settings accordingly or discontinue use of the Site."
      }
    },
    "2": {
      "heading": "2. What Are Cookies?",
      "paragraphs": {
        "0": "Cookies are small text files that are placed on your device when you visit a website. They are widely used to make websites work more efficiently, enhance user experience, and provide information to the owners of the site.",
        "1": "Cookies can be session cookies (temporary, expire when you close your browser), persistent cookies (remain on your device for a set period), first-party cookies (set by the website you are visiting), or third-party cookies (set by a third party such as advertisers or analytics services through our Site)."
      }
    },
    "3": {
      "heading": "3. How We Use Cookies",
      "paragraphs": {
        "0": "Strictly Necessary Cookies: These are essential for the Site to function properly (e.g., security features and language preference). These cookies do not store personally identifiable information and cannot be disabled.",
        "1": "Performance and Analytics Cookies: These help us understand how visitors interact with our Site by collecting anonymous information. This helps us improve our Site performance. They are only loaded after you give your consent.",
        "2": "Functionality Cookies: These allow the Site to remember choices you make (e.g., language preference and region) to provide a more personalized experience.",
        "3": "Targeting and Advertising Cookies: These are used to deliver advertisements relevant to you and your interests. They may also be used to limit the number of times you see an advertisement and help measure the effectiveness of advertising campaigns. They are only set after your explicit consent."
      }
    },
    "4": {
      "heading": "4. Third-Party Cookies",
      "paragraphs": {
        "0": "We partner with third-party service providers who may set cookies on your device when you visit our Site. These may include analytics providers, advertising networks, social media platforms, and video hosting services.",
        "1": "These third parties have their own privacy policies and cookie policies. We recommend reviewing their policies to understand how they use your data. We do not control the placement of these third-party cookies, and they are only activated after your consent."
      }
    },
    "5": {
      "heading": "5. Your Rights and Choices",
      "paragraphs": {
        "0": "For users in the European Economic Area (EEA) and the United Kingdom under GDPR, you have the right to give or withdraw consent for non-essential cookies at any time. You may request access to the personal data we hold about you, request deletion of your data, and manage your preferences via the Cookie Consent Banner or your browser settings.",
        "1": "For users in California, USA under CCPA/CPRA, you have the right to know what personal information is collected, used, or shared; the right to request deletion; and the right to opt-out of sale or sharing of your personal information. We do not sell your personal data.",
        "2": "You can control and delete cookies through the Cookie Consent Banner that appears when you first visit our Site, or through your browser settings."
      }
    },
    "6": {
      "heading": "6. Changes to This Policy",
      "paragraphs": {
        "0": "We may update this Cookie Privacy Policy from time to time to reflect changes in technology, legislation, or our business operations. Any updates will be posted on this page with an updated date. We encourage you to review this policy periodically."
      }
    },
    "7": {
      "heading": "7. Contact Us",
      "paragraphs": {
        "0": "Jiangsu Kaichen Power Equipment Co., Ltd.",
        "1": "Address: Dinghuo Industrial Park, Jiangdu District, Yangzhou City, Jiangsu, China.",
        "2": "Email: cnkcpower@163.com  |  Tel: +86-18012341322"
      }
    }
  }
}

# Russian translation
ru_sections = {
  "1": {"heading": "1. Введение", "paragraphs": {
    "0": "Добро пожаловать на www.cnkcpower.com. Мы стремимся защищать вашу конфиденциальность и обеспечивать положительный опыт при посещении нашего сайта.",
    "1": "Настоящая Политика использования файлов cookie объясняет, что такое файлы cookie, как мы их используем, типы используемых файлов cookie и как вы можете управлять ими или удалять их.",
    "2": "Используя наш сайт, вы соглашаетесь на использование файлов cookie в соответствии с настоящей Политикой. Если вы не согласны с использованием файлов cookie, настройте параметры браузера или прекратите использование сайта."
  }},
  "2": {"heading": "2. Что такое файлы cookie?", "paragraphs": {
    "0": "Файлы cookie — это небольшие текстовые файлы, которые размещаются на вашем устройстве при посещении веб-сайта. Они широко используются для более эффективной работы сайтов и улучшения пользовательского опыта.",
    "1": "Файлы cookie могут быть сеансовыми (временными), постоянными (остаются на устройстве), основными или сторонними (устанавливаемыми третьей стороной)."
  }},
  "3": {"heading": "3. Как мы используем файлы cookie", "paragraphs": {
    "0": "Строго необходимые файлы cookie: необходимы для правильной работы сайта (функции безопасности, выбор языка). Не могут быть отключены.",
    "1": "Файлы cookie производительности и аналитики: помогают нам понять, как посетители взаимодействуют с сайтом. Загружаются только после вашего согласия.",
    "2": "Функциональные файлы cookie: позволяют сайту запоминать сделанные вами выборы (язык, регион).",
    "3": "Рекламные файлы cookie: используются для показа релевантной рекламы. Устанавливаются только после вашего явного согласия."
  }},
  "4": {"heading": "4. Сторонние файлы cookie", "paragraphs": {
    "0": "Мы сотрудничаем со сторонними поставщиками услуг, которые могут устанавливать файлы cookie на ваше устройство. Это аналитические сервисы, рекламные сети, социальные платформы.",
    "1": "Эти третьи стороны имеют собственные политики конфиденциальности. Мы не контролируем размещение этих сторонних файлов cookie, и они активируются только после вашего согласия."
  }},
  "5": {"heading": "5. Ваши права и выбор", "paragraphs": {
    "0": "Для пользователей из ЕЭЗ и Великобритании в соответствии с GDPR вы имеете право в любой момент дать или отозвать согласие на использование необязательных файлов cookie.",
    "1": "Для пользователей из Калифорнии в соответствии с CCPA/CPRA вы имеете право знать, какая личная информация собирается, и запросить её удаление. Мы не продаём ваши персональные данные.",
    "2": "Вы можете управлять и удалять файлы cookie через Баннер согласия или настройки вашего браузера."
  }},
  "6": {"heading": "6. Изменения в Политике", "paragraphs": {
    "0": "Мы можем периодически обновлять настоящую Политику. Все обновления будут размещаться на этой странице. Рекомендуем периодически просматривать эту политику."
  }},
  "7": {"heading": "7. Свяжитесь с нами", "paragraphs": {
    "0": "Jiangsu Kaichen Power Equipment Co., Ltd.",
    "1": "Адрес: Dinghuo Industrial Park, Jiangdu District, Yangzhou, Jiangsu, China.",
    "2": "Email: cnkcpower@163.com  |  Tel: +86-18012341322"
  }}
}

privacy_ru = {"lastUpdated": "Последнее обновление: октябрь 2026", "sections": ru_sections}

# Write en
with open('content/i18n/en.json', encoding='utf-8') as f:
    data = json.load(f)
data['privacy'] = privacy_en
with open('content/i18n/en.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Write ru
with open('content/i18n/ru.json', encoding='utf-8') as f:
    data = json.load(f)
data['privacy'] = privacy_ru
with open('content/i18n/ru.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Other locales fallback to en
for loc in ['es','fr','de','pt','ar','tr','th','vi','id']:
    p = f'content/i18n/{loc}.json'
    with open(p, encoding='utf-8') as f:
        data = json.load(f)
    data['privacy'] = privacy_en
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print('Privacy i18n fixed')
