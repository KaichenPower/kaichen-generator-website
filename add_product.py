import json, os

# New product translations
product_en = {
    "name": "Cummins 50kW Silent Diesel Generator",
    "description": "Compact 50kW (63kVA) Cummins soundproof diesel generator set, designed for small offices, clinics, retail stores and light commercial standby power where quiet operation and reliability matter.",
    "features": [
        "Cummins 4-cylinder diesel engine with proven global service network",
        "Acoustic canopy reducing noise to below 68 dB(A) at 7 meters",
        "Automatic voltage regulation (AVR) with digital control panel",
        "Integrated baseframe fuel tank for 8+ hours continuous running",
        "Automatic mains failure (AMF) start-up within 10 seconds",
        "CE, ISO9001 and emission-compliant package"
    ],
    "applications": [
        "Small offices & clinics",
        "Retail stores & shops",
        "Light commercial standby"
    ],
    "problems": [
        "Quiet backup power near offices and residences",
        "Reliable start-up when the grid fails",
        "Compact size for tight plant rooms"
    ]
}

translations = {
    'ru': {
        "name": "Дизель-генератор Cummins 50 кВт в кожухе",
        "description": "Компактный дизель-генератор Cummins 50 кВт (63 кВА) в шумозащитном кожухе для небольших офисов, клиник, магазинов и коммерческого резервирования, где важны тихая работа и надежность.",
        "features": [
            "4-цилиндровый двигатель Cummins с глобальной сервисной сетью",
            "Шумозащитный кожух снижает шум до уровня ниже 68 дБ(A) на расстоянии 7 метров",
            "Автоматический регулятор напряжения (AVR) с цифровой панелью управления",
            "Встроенный топливный бак на 8+ часов непрерывной работы",
            "Автоматический запуск при отключении сети (AMF) за 10 секунд",
            "Соответствие CE, ISO9001 и экологическим нормам"
        ],
        "applications": ["Небольшие офисы и клиники", "Розничные магазины", "Коммерческое резервирование"],
        "problems": ["Тихое резервное питание рядом с офисами", "Надежный запуск при отключении сети", "Компактный размер для узких помещений"]
    },
    'es': {
        "name": "Generador Diesel Silencioso Cummins 50kW",
        "description": "Generador diesel Cummins compacto de 50kW (63kVA) en cabina insonorizada, diseñado para pequeñas oficinas, clínicas, tiendas y reserva comercial ligera donde la operación silenciosa y la fiabilidad son importantes.",
        "features": [
            "Motor Cummins de 4 cilindros con red de servicio global probada",
            "Cabina acústica que reduce el ruido por debajo de 68 dB(A) a 7 metros",
            "Regulador automático de voltaje (AVR) con panel de control digital",
            "Depósito de combustible integrado para 8+ horas de funcionamiento continuo",
            "Arranque automático por fallo de red (AMF) en 10 segundos",
            "Paquete conforme a CE, ISO9001 y emisiones"
        ],
        "applications": ["Oficinas pequeñas y clínicas", "Tiendas minoristas", "Reserva comercial ligera"],
        "problems": ["Energía de reserva silenciosa cerca de oficinas", "Arranque fiable cuando falla la red", "Tamaño compacto para cuartos estrechos"]
    },
    'fr': {
        "name": "Générateur Diesel Silencieux Cummins 50kW",
        "description": "Générateur diesel Cummins compact de 50kW (63kVA) en capot insonorisé, conçu pour les petits bureaux, cliniques, magasins et secours commercial léger où le fonctionnement silencieux et la fiabilité comptent.",
        "features": [
            "Moteur Cummins 4 cylindres avec réseau de service mondial éprouvé",
            "Capot acoustique réduisant le bruit en dessous de 68 dB(A) à 7 mètres",
            "Régulateur automatique de tension (AVR) avec panneau de contrôle numérique",
            "Réservoir intégré pour 8+ heures de fonctionnement continu",
            "Démarrage automatique sur coupure secteur (AMF) en 10 secondes",
            "Package conforme CE, ISO9001 et émissions"
        ],
        "applications": ["Petits bureaux et cliniques", "Magasins de détail", "Secours commercial léger"],
        "problems": ["Énergie de secours silencieuse près des bureaux", "Démarrage fiable en cas de coupure", "Taille compacte pour les salles étroites"]
    },
    'de': {
        "name": "Cummins 50kW Schalldichter Dieselgenerator",
        "description": "Kompakter Cummins-Dieselgenerator 50kW (63kVA) im schalldichten Gehäuse für kleine Büros, Kliniken, Geschäfte und leichte kommerzielle Notstromversorgung, wo leiser Betrieb und Zuverlässigkeit zählen.",
        "features": [
            "Cummins 4-Zylinder-Motor mit bewährtem globalem Servicenetz",
            "Schallschutzhaube reduziert Geräusch auf unter 68 dB(A) auf 7 Meter",
            "Automatischer Spannungsregler (AVR) mit digitalem Bedienpanel",
            "Integrierter Kraftstofftank für 8+ Stunden Dauerbetrieb",
            "Automatischer Netzausfallstart (AMF) innerhalb von 10 Sekunden",
            "CE-, ISO9001- und emissionskonformes Paket"
        ],
        "applications": ["Kleine Büros und Kliniken", "Einzelhandelsgeschäfte", "Leichte kommerzielle Notstromversorgung"],
        "problems": ["Leise Notstromversorgung nahe Büros", "Zuverlässiger Start bei Netzausfall", "Kompakte Größe für enge Räume"]
    },
    'pt': {
        "name": "Gerador Diesel Silencioso Cummins 50kW",
        "description": "Gerador diesel Cummins compacto de 50kW (63kVA) em cabine acústica, projetado para pequenos escritórios, clínicas, lojas e reserva comercial leve onde operação silenciosa e confiabilidade importam.",
        "features": [
            "Motor Cummins 4 cilindros com rede de serviço global comprovada",
            "Cabine acústica reduz ruído para abaixo de 68 dB(A) a 7 metros",
            "Regulador automático de tensão (AVR) com painel digital",
            "Tanque integrado para 8+ horas de operação contínua",
            "Partida automática por falha de rede (AMF) em 10 segundos",
            "Pacote conforme CE, ISO9001 e emissões"
        ],
        "applications": ["Pequenos escritórios e clínicas", "Lojas de varejo", "Reserva comercial leve"],
        "problems": ["Energia reserva silenciosa perto de escritórios", "Partida confiável quando a rede falha", "Tamanho compacto para salas estreitas"]
    },
    'ar': {
        "name": "مولد ديزل كاتم للصوت Cummins 50 كيلوواط",
        "description": "مولد ديزل Cummins مدمج 50 كيلوواط (63 كيلو فولت أمبير) في كابينة عازلة للصوت، مصمم للمكاتب الصغيرة والعيادات والمتاجر والاحتياط التجاري الخفيف حيث يهم التشغيل الهادئ والموثوقية.",
        "features": [
            "محرك Cummins رباعي الأسطوانات مع شبكة خدمة عالمية موثوقة",
            "كابينة عازلة للصوت تخفض الضوضاء إلى أقل من 68 ديسيبل على بعد 7 أمتار",
            "منظم جهد تلقائي (AVR) مع لوحة تحكم رقمية",
            "خزان وقود مدمج لـ 8+ ساعات من التشغيل المستمر",
            "تشغيل تلقائي عند انقطاع التيار (AMF) خلال 10 ثوانٍ",
            "حزمة متوافقة مع CE و ISO9001 والانبعاثات"
        ],
        "applications": ["مكاتب وعيادات صغيرة", "متاجر التجزئة", "احتياط تجاري خفيف"],
        "problems": ["طاقة احتياطية هادئة بالقرب من المكاتب", "تشغيل موثوق عند انقطاع التيار", "حجم مدمج للغرف الضيقة"]
    },
    'tr': {
        "name": "Cummins 50kW Sessiz Dizel Jeneratör",
        "description": "Sessiz çalışma ve güvenilirliğin önemli olduğu küçük ofisler, klinikler, mağazalar ve hafif ticari yedek güç için kompakt 50kW (63kVA) Cummins ses yalıtımlı dizel jeneratör seti.",
        "features": [
            "Kanıtlanmış küresel servis ağına sahip Cummins 4 silindirli motor",
            "Ses yalıtımlı kapak, gürültüyü 7 metrede 68 dB(A)'nın altına düşürür",
            "Dijital kontrol paneli ile otomatik voltaj regülasyonu (AVR)",
            "8+ saat kesintisiz çalışma için entegre yakıt deposu",
            "Şebeke kesintisinde 10 saniyede otomatik çalışma (AMF)",
            "CE, ISO9001 ve emisyon uyumlu paket"
        ],
        "applications": ["Küçük ofisler ve klinikler", "Perakende mağazaları", "Hafif ticari yedek güç"],
        "problems": ["Ofisler yakınında sessiz yedek güç", "Şebeke kesildiğinde güvenilir çalışma", "Dar odalar için kompakt boyut"]
    },
    'th': {
        "name": "เครื่องกำเนิดไฟฟ้าดีเซล Cummins 50kW แบบเงียบ",
        "description": "เครื่องกำเนิดไฟฟ้าดีเซล Cummins ขนาดกะทัดรัด 50kW (63kVA) ในตู้เก็บเสียง สำหรับสำนักงานขนาดเล็ก คลินิก ร้านค้า และระบบสำรองไฟเชิงพาณิชย์เบาที่เน้นความเงียบและความน่าเชื่อถือ",
        "features": [
            "เครื่องยนต์ Cummins 4 สูบ พร้อมเครือข่ายบริการทั่วโลกที่ได้รับการพิสูจน์",
            "ตู้เก็บเสียงลดเสียงรบกวนต่ำกว่า 68 dB(A) ที่ระยะ 7 เมตร",
            "ระบบควบคุมแรงดันอัตโนมัติ (AVR) พร้อมแผงควบคุมดิจิทัล",
            "ถังน้ำมันในตัวสำหรับการทำงานต่อเนื่อง 8+ ชั่วโมง",
            "สตาร์ทอัตโนมัติเมื่อไฟดับ (AMF) ภายใน 10 วินาที",
            "เป็นไปตามมาตรฐาน CE, ISO9001 และการปล่อยมลพิษ"
        ],
        "applications": ["สำนักงานและคลินิกขนาดเล็ก", "ร้านค้าปลีก", "ระบบสำรองไฟเชิงพาณิชย์เบา"],
        "problems": ["ไฟสำรองเงียบใกล้สำนักงาน", "สตาร์ทได้เชื่อถือเมื่อไฟดับ", "ขนาดกะทัดรัดสำหรับห้องแคบ"]
    },
    'vi': {
        "name": "Máy Phát Điện Diesel Cummins 50kW Chống Ồn",
        "description": "Máy phát diesel Cummins nhỏ gọn 50kW (63kVA) trong vỏ cách âm, thiết kế cho văn phòng nhỏ, phòng khám, cửa hàng và dự phòng thương mại nhẹ, nơi hoạt động yên tĩnh và độ tin cậy là quan trọng.",
        "features": [
            "Động cơ Cummins 4 xi-lanh với mạng lưới dịch vụ toàn cầu đã được kiểm chứng",
            "Vỏ cách âm giảm tiếng ồn xuống dưới 68 dB(A) ở khoảng cách 7 mét",
            "Bộ điều chỉnh điện áp tự động (AVR) với bảng điều khiển kỹ thuật số",
            "Bể nhiên liệu tích hợp cho 8+ giờ hoạt động liên tục",
            "Khởi động tự động khi mất điện (AMF) trong 10 giây",
            "Đóng gói tuân thủ CE, ISO9001 và khí thải"
        ],
        "applications": ["Văn phòng nhỏ và phòng khám", "Cửa hàng bán lẻ", "Dự phòng thương mại nhẹ"],
        "problems": ["Nguồn dự phòng yên tĩnh gần văn phòng", "Khởi động đáng tin cậy khi mất điện", "Kích thước nhỏ gọn cho phòng hẹp"]
    },
    'id': {
        "name": "Genset Diesel Cummins 50kW Silent",
        "description": "Genset diesel Cummins ringkas 50kW (63kVA) dalam kanopi peredam suara, dirancang untuk kantor kecil, klinik, toko, dan daya cadangan komersial ringan di mana operasi tenang dan keandalan penting.",
        "features": [
            "Mesin Cummins 4 silinder dengan jaringan layanan global teruji",
            "Kanopi akustik mengurangi kebisingan di bawah 68 dB(A) pada 7 meter",
            "Regulasi tegangan otomatis (AVR) dengan panel kontrol digital",
            "Tangki bahan bakar terintegrasi untuk 8+ jam operasi berkelanjutan",
            "Start otomatis saat listrik mati (AMF) dalam 10 detik",
            "Paket sesuai CE, ISO9001, dan emisi"
        ],
        "applications": ["Kantor kecil dan klinik", "Toko ritel", "Daya cadangan komersial ringan"],
        "problems": ["Daya cadangan tenang dekat kantor", "Start andal saat listrik mati", "Ukuran ringkas untuk ruang sempit"]
    }
}

for loc in ['en'] + list(translations.keys()):
    path = f'content/i18n/{loc}.json'
    with open(path, 'r', encoding='utf-8') as f:
        d = json.load(f)
    if 'products' not in d:
        d['products'] = {}
    d['products']['cummins-50-silent'] = translations.get(loc, product_en)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"Updated {loc}")
