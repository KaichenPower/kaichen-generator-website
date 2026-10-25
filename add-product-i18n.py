import json
import os

base_dir = "D:/projects/kaichen-generator-website/content/i18n"

# 产品数据（英语）
product_data = {
    "name": "Weichai 500kW Silent Diesel Generator",
    "description": "Heavy-duty 500kW (625kVA) Weichai soundproof diesel generator set for large factories, data centers, hospitals and commercial buildings needing reliable standby or prime power with low noise and easy maintenance.",
    "features": [
        "Weichai WP13 series 6-cylinder turbocharged engine",
        "Heavy-duty acoustic canopy reducing noise to 72–78 dB(A) at 7 meters",
        "Deep Sea digital control panel with remote monitoring option",
        "Integrated baseframe fuel tank for 6+ hours continuous running",
        "Automatic mains failure (AMF) start within 10 seconds",
        "Parallel operation capability for N+1 redundancy"
    ],
    "applications": [
        "Large factories & manufacturing plants",
        "Data centers & critical infrastructure",
        "Hospitals & healthcare facilities"
    ],
    "problems": [
        "Reliable standby power for large critical loads",
        "Low noise operation in urban and suburban areas",
        "Scalable N+1 redundancy for mission-critical facilities"
    ]
}

# 各语言的产品名称和描述（简化翻译）
translations = {
    "ru": {
        "name": "Дизельный генератор Weichai 500 кВт в шумозащитном кожухе",
        "description": "Мощный дизельный генератор Weichai 500 кВт (625 кВА) в шумозащитном кожухе для крупных заводов, дата-центров, больниц и коммерческих зданий.",
    },
    "es": {
        "name": "Generador diesel Weichai 500kW silencioso",
        "description": "Generador diesel Weichai de 500 kW (625 kVA) con cabina insonorizada para grandes fábricas, centros de datos, hospitales y edificios comerciales.",
    },
    "fr": {
        "name": "Groupe électrogène diesel Weichai 500kW silencieux",
        "description": "Groupe électrogène diesel Weichai 500kW (625kVA) insonorisé pour grandes usines, centres de données, hôpitaux et bâtiments commerciaux.",
    },
    "de": {
        "name": "Weichai 500kW schallisolierter Dieselgenerator",
        "description": "Leistungsstarker Weichai 500kW (625kVA) Dieselgenerator im Schallschutzgehäuse für große Fabriken, Rechenzentren, Krankenhäuser und Gewerbebauten.",
    },
    "pt": {
        "name": "Gerador diesel Weichai 500kW silencioso",
        "description": "Gerador diesel Weichai de 500 kW (625 kVA) com cabine acústica para grandes fábricas, centros de dados, hospitais e edifícios comerciais.",
    },
    "ar": {
        "name": "مولد ديزل Weichai 500 كيلوواط كاتم للصوت",
        "description": "مولد ديزل Weichai قوي بقدرة 500 كيلوواط (625 كيلو فولت أمبير) في كابينة عازلة للصوت للمصانع الكبيرة ومراكز البيانات والمستشفيات والمباني التجارية.",
    },
    "tr": {
        "name": "Weichai 500kW Sessiz Dizel Jeneratör",
        "description": "Büyük fabrikalar, veri merkezleri, hastaneler ve ticari binalar için ağır hizmet tipi Weichai 500kW (625kVA) sessiz dizel jeneratör seti.",
    },
    "th": {
        "name": "เครื่องกำเนิดไฟฟ้าดีเซล Weichai 500 กิโลวัตต์ แบบเงียบ",
        "description": "เครื่องกำเนิดไฟฟ้าดีเซล Weichai ขนาดใหญ่ 500 กิโลวัตต์ (625 กิโลโวลต์แอมแปร์) ในตู้กันเสียง สำหรับโรงงานขนาดใหญ่ ศูนย์ข้อมูล โรงพยาบาล และอาคารพาณิชย์",
    },
    "vi": {
        "name": "Máy phát điện diesel Weichai 500kW siêu êm",
        "description": "Máy phát điện diesel Weichai công suất lớn 500kW (625kVA) trong buồng cách âm cho nhà máy lớn, trung tâm dữ liệu, bệnh viện và tòa nhà thương mại.",
    },
    "id": {
        "name": "Genset diesel Weichai 500kW silent",
        "description": "Genset diesel Weichai heavy duty 500kW (625kVA) dengan kanopi peredam suara untuk pabrik besar, data center, rumah sakit dan gedung komersial.",
    }
}

for lang in ["en", "ru", "es", "fr", "de", "pt", "ar", "tr", "th", "vi", "id"]:
    filepath = os.path.join(base_dir, f"{lang}.json")
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if "products" not in data:
        data["products"] = {}
    
    if lang == "en":
        data["products"]["weichai-500-silent"] = product_data
    else:
        trans = translations[lang]
        data["products"]["weichai-500-silent"] = {
            "name": trans["name"],
            "description": trans["description"],
            "features": product_data["features"],  # 简化版：features 保持英文
            "applications": product_data["applications"],
            "problems": product_data["problems"]
        }
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Updated {lang}")

print("Done!")
