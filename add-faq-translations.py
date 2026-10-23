import json
import os

base_dir = "D:/projects/kaichen-generator-website/content/i18n"

# FAQ 内容翻译
faq_data = {
    "en": {
        "nav": {
            "faq": "FAQ"
        },
        "faqPage": {
            "title": "Frequently Asked Questions",
            "subtitle": "Straight answers on warranty, sizing, lead time, silent vs open, standby vs prime, export support and after-sales. If your question is not here, ask us directly.",
            "askQuestion": "Ask Us a Question",
            "faqs": [
                {
                    "q": "What warranty do you offer on a new generator set?",
                    "a": "A standard new set carries a 1-year or 1,000-hour warranty (whichever comes first), measured from commissioning or invoice date. The engine, alternator and control panel can be extended to 2 years under our extended-warranty option. Wear items such as oil, filters, belts and batteries are excluded. The exact terms are written into the purchase contract."
                },
                {
                    "q": "How long is the lead time?",
                    "a": "Standard power ranges (20–500 kVA) are usually in stock and ship within 7–15 days. Custom configurations, high-voltage parallel systems or special canopies typically take 25–45 days. We keep finished stock of common Weichai, Yuchai and SDEC sets to shorten lead time for urgent projects."
                },
                {
                    "q": "How do I choose the right generator size for my site?",
                    "a": "Add the running kW of every load the set must carry at the same time, then add 20–30% margin for motor starting current and future expansion. As a rule of thumb, a small office or shop needs 20–50 kVA, a factory floor or a mid-size hotel needs 100–300 kVA, and a data center or hospital moves up to 500 kVA and above. Send us your load list and we will size the set for free."
                },
                {
                    "q": "Silent type or open type – which one should I pick?",
                    "a": "Choose a silent canopy set if the unit sits near people (office floor, hospital, residential area, rooftop) and you need to keep noise around 65–75 dB(A) at 7 meters. Choose an open-type set if the unit goes into a dedicated machine room that already has acoustic treatment, because the canopy adds cost and reduces service access. Containerized and trailer-mounted options are available for outdoor or mobile duty."
                },
                {
                    "q": "What is the difference between standby power and prime power?",
                    "a": "Standby power is for occasional emergency use during grid outages, typically up to 200 hours a year at 70% average load, with no overload allowed. Prime (continuous) power runs the site as the main power source, 24 hours a day, with 10% overload allowed for one hour in twelve. If you are buying for a site without a stable grid, always specify prime power – buying a standby set for continuous duty shortens its life and voids the warranty."
                },
                {
                    "q": "Do you support custom voltage, frequency and special environments?",
                    "a": "Yes. We build 50 Hz / 60 Hz sets, from 220V single-phase up to 11kV three-phase, and tailor the set for high altitude (derating), cold climates (jacket water heater, arctic coolant), coastal sites (anti-corrosion treatment) and dusty environments (pre-filters). Remote monitoring via 4G and cloud, ATS auto-transfer and multi-machine paralleling are all available."
                },
                {
                    "q": "Can you export overseas and handle documentation?",
                    "a": "We have an export department at the Yangzhou Innovation Center and have shipped to Southeast Asia, the Middle East, Africa, South America and Eastern Europe. We provide commercial invoice, packing list, bill of lading, CE/ISO certificates, test report and (on request) a third-party inspection report from SGS, BV or TUV. Export-standard anti-corrosion packaging is used by default."
                },
                {
                    "q": "What does the after-sales response look like?",
                    "a": "We maintain more than 2,000 authorized service points across China. On the same day, engineers arrive on site within 2–4 hours in cities, 4–8 hours within the province and within 24 hours in other provinces. Overseas buyers get remote video support, a spare-parts kit and local partner contacts. The hotline runs 24/7/365. After the warranty expires, we keep supplying parts at cost plus labor for the life of the set."
                },
                {
                    "q": "Is installation and operator training included?",
                    "a": "Standard sets ship with free video guidance. On-site installation, commissioning and hands-on operator training (start/stop, alarm recognition, routine maintenance) are available as a paid service. We test voltage, frequency and load on site and hand over a commissioning report before leaving. Civil works, cabling and exhaust piping are normally handled by your local contractor."
                },
                {
                    "q": "Do you test every set before shipment?",
                    "a": "Yes. Every set runs on our 2 MW digital load bank through a four-step sequence – 20%, 50%, 75% and 100% rated load – for at least 2 hours total. The whole test is recorded on video and shared with you before the set leaves the factory, so you can verify the real output and protection trip settings before you receive the goods."
                }
            ]
        }
    },
    "ru": {
        "nav": {
            "faq": "Вопросы и ответы"
        },
        "faqPage": {
            "title": "Часто задаваемые вопросы",
            "subtitle": "Прямые ответы о гарантии, подборе мощности, сроках поставки, закрытом и открытом типе, резервной и основной мощности, экспортной поддержке и послепродажном обслуживании.",
            "askQuestion": "Задайте нам вопрос",
            "faqs": [
                {
                    "q": "Какую гарантию вы даёте на новый генератор?",
                    "a": "Стандартная гарантия на новый комплект — 1 год или 1000 моточасов (в зависимости от того, что наступит раньше), с момента ввода в эксплуатацию или даты счета. Гарантию на двигатель, генератор и панель управления можно продлить до 2 лет по опции расширенной гарантии. Расходные материалы (масло, фильтры, ремни, аккумуляторы) не входят в гарантию."
                },
                {
                    "q": "Каков срок поставки?",
                    "a": "Стандартные мощности (20–500 кВА) обычно есть на складе и отгружаются в течение 7–15 дней. Индивидуальные конфигурации, высоковольтные параллельные системы или специальные кожухи обычно занимают 25–45 дней."
                },
                {
                    "q": "Как выбрать подходящую мощность генератора для моего объекта?",
                    "a": "Сложите рабочие кВт всех нагрузок, которые комплект должен питать одновременно, затем добавьте 20–30% запаса на пусковой ток электродвигателей и будущее расширение. Небольшой офис или магазин требует 20–50 кВА, заводской цех или отель среднего размера — 100–300 кВА, а дата-центр или больница — от 500 кВА."
                },
                {
                    "q": "Какой тип выбрать — закрытый или открытый?",
                    "a": "Выбирайте закрытый кожух, если установка находится рядом с людьми (офис, больница, жилой район, крыша) и вам нужно поддерживать уровень шума около 65–75 дБ(А) на расстоянии 7 метров. Выбирайте открытый тип, если установка находится в отдельном машинном зале, где уже есть шумоизоляция."
                },
                {
                    "q": "В чём разница между резервной и основной мощностью?",
                    "a": "Резервная мощность предназначена для периодического аварийного использования при отключении сетей, обычно до 200 часов в год при средней нагрузке 70%, без перегрузки. Основная (непрерывная) мощность работает как основной источник питания объекта, 24 часа в сутки, с допустимой перегрузкой 10% в течение одного часа из двенадцати."
                },
                {
                    "q": "Поддерживаете ли вы нестандартное напряжение, частоту и специальные условия?",
                    "a": "Да. Мы производим комплекты 50 Гц / 60 Гц, от 220В однофазного до 11кВ трёхфазного, и адаптируем комплект для высокогорья (снижение мощности), холодного климата (подогреватель охлаждающей жидкости, арктический антифриз), прибрежных объектов (антикоррозийная обработка) и пыльных условий (предфильтры)."
                },
                {
                    "q": "Вы можете экспортировать за границу и оформлять документацию?",
                    "a": "У нас есть экспортный отдел в Инновационном центре Янчжоу, и мы отправляли оборудование в Юго-Восточную Азию, на Ближний Восток, в Африку, Южную Америку и Восточную Европу. Мы предоставляем коммерческий инвойс, упаковочный лист, коносамент, сертификаты CE/ISO, протокол испытаний и (по запросу) отчёт независимой инспекции SGS, BV или TUV."
                },
                {
                    "q": "Как организовано послепродажное обслуживание?",
                    "a": "У нас более 2000 авторизованных сервисных центров по всему Китаю. Инженеры выезжают на объект в течение 2–4 часов в городах, 4–8 часов в пределах провинции и 24 часов в других провинциях. Зарубежные покупатели получают удалённую видеоподдержку, комплект запасных частей и контакты местных партнёров."
                },
                {
                    "q": "Включены ли установка и обучение операторов?",
                    "a": "Стандартные комплекты поставляются с бесплатным видеоинструктажем. Установка на объекте, ввод в эксплуатацию и практическое обучение операторов (пуск/остановка, распознавание тревог, регулярное обслуживание) доступны как платная услуга."
                },
                {
                    "q": "Вы тестируете каждый комплект перед отгрузкой?",
                    "a": "Да. Каждый комплект проходит испытания на нашей 2 МВт цифровой нагрузочной банке по четырёхступенчатой схеме — 20%, 50%, 75% и 100% номинальной нагрузке — общей продолжительностью не менее 2 часов. Весь тест записывается на видео и передаётся вам до отгрузки."
                }
            ]
        }
    },
    "es": {
        "nav": {
            "faq": "Preguntas frecuentes"
        },
        "faqPage": {
            "title": "Preguntas Frecuentes",
            "subtitle": "Respuestas directas sobre garantía, dimensionamiento, plazo de entrega, tipo silencioso vs abierto, potencia de reserva vs principal, soporte de exportación y posventa.",
            "askQuestion": "Háganos una pregunta",
            "faqs": [
                {
                    "q": "¿Qué garantía ofrecen en un grupo electrógeno nuevo?",
                    "a": "Un grupo nuevo estándar lleva una garantía de 1 año o 1.000 horas (lo que ocurra primero), medida desde la puesta en servicio o la fecha de factura. El motor, el alternador y el panel de control pueden extenderse a 2 años bajo nuestra opción de garantía ampliada."
                },
                {
                    "q": "¿Cuál es el plazo de entrega?",
                    "a": "Los rangos de potencia estándar (20–500 kVA) suelen estar en stock y se envían en 7–15 días. Las configuraciones personalizadas, los sistemas paralelos de alto voltaje o las carpas especiales suelen tardar 25–45 días."
                },
                {
                    "q": "¿Cómo elijo el tamaño adecuado de generador para mi sitio?",
                    "a": "Sume los kW en funcionamiento de cada carga que el grupo debe soportar al mismo tiempo, luego agregue un margen del 20–30% para la corriente de arranque del motor y la expansión futura. Como regla general, una oficina pequeña o tienda necesita 20–50 kVA, un piso de fábrica o un hotel mediano necesita 100–300 kVA, y un centro de datos u hospital pasa a 500 kVA y más."
                },
                {
                    "q": "¿Tipo silencioso o abierto, cuál debo elegir?",
                    "a": "Elija un conjunto de carpa silenciosa si la unidad se encuentra cerca de personas (oficina, hospital, zona residencial, azotea) y necesita mantener el ruido alrededor de 65–75 dB(A) a 7 metros. Elija un conjunto de tipo abierto si la unidad va a una sala de máquinas dedicada que ya tiene tratamiento acústico."
                },
                {
                    "q": "¿Cuál es la diferencia entre potencia de reserva y potencia principal?",
                    "a": "La energía de reserva es para uso de emergencia ocasional durante cortes de red, típicamente hasta 200 horas al año al 70% de carga promedio, sin sobrecarga permitida. La energía principal (continua) funciona como fuente de alimentación principal del sitio, 24 horas al día, con un 10% de sobrecarga permitida durante una hora de cada doce."
                },
                {
                    "q": "¿Admiten voltaje, frecuencia y entornos especiales personalizados?",
                    "a": "Sí. Construimos conjuntos de 50 Hz / 60 Hz, desde 220V monofásico hasta 11kV trifásico, y adaptamos el conjunto para gran altitud (reducción de potencia), climas fríos (calentador de agua de camisa, refrigerante ártico), sitios costeros (tratamiento anticorrosión) y entornos polvorientos (prefiltros)."
                },
                {
                    "q": "¿Pueden exportar al extranjero y manejar la documentación?",
                    "a": "Tenemos un departamento de exportación en el Centro de Innovación de Yangzhou y hemos enviado a Sudeste Asiático, Medio Oriente, África, Sudamérica y Europa del Este. Proporcionamos factura comercial, lista de empaque, conocimiento de embarque, certificados CE/ISO, informe de prueba y (a pedido) un informe de inspección de terceros de SGS, BV o TUV."
                },
                {
                    "q": "¿Cómo es la respuesta posventa?",
                    "a": "Mantenemos más de 2.000 puntos de servicio autorizados en toda China. El mismo día, los ingenieros llegan al sitio en 2–4 horas en ciudades, 4–8 horas dentro de la provincia y dentro de las 24 horas en otras provincias. Los compradores extranjeros reciben soporte de video remoto, un kit de repuestos y contactos de socios locales."
                },
                {
                    "q": "¿Están incluidos la instalación y la capacitación del operador?",
                    "a": "Los conjuntos estándar se envían con guía de video gratuita. La instalación en el sitio, la puesta en servicio y la capacitación práctica del operador (arranque/parada, reconocimiento de alarmas, mantenimiento de rutina) están disponibles como servicio de pago."
                },
                {
                    "q": "¿Prueban cada conjunto antes del envío?",
                    "a": "Sí. Cada conjunto funciona en nuestro banco de carga digital de 2 MW a través de una secuencia de cuatro pasos — 20%, 50%, 75% y 100% de carga nominal — durante al menos 2 horas en total. Toda la prueba se graba en video y se comparte con usted antes de que el conjunto salga de la fábrica."
                }
            ]
        }
    }
}

# 为其他语言添加基础翻译（简化版，确保页面不报错）
for lang in ["fr", "de", "pt", "ar", "tr", "th", "vi", "id"]:
    faq_data[lang] = {
        "nav": {"faq": "FAQ"},
        "faqPage": {
            "title": "Frequently Asked Questions",
            "subtitle": "Answers to common questions about diesel generator sets.",
            "askQuestion": "Ask Us a Question",
            "faqs": faq_data["en"]["faqPage"]["faqs"]  # 先用英语，后续再翻译
        }
    }

for lang, data in faq_data.items():
    filepath = os.path.join(base_dir, f"{lang}.json")
    with open(filepath, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    
    # Add nav.faq
    if 'nav' not in json_data:
        json_data['nav'] = {}
    json_data['nav']['faq'] = data['nav']['faq']
    
    # Add faqPage
    json_data['faqPage'] = data['faqPage']
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    
    print(f"Updated {lang}")
