import os

base_dir = "D:/projects/kaichen-generator-website/content/blog"
slug = "generator-wont-start-7-causes"

# 各语言的标题和描述翻译
translations = {
    "ru": {
        "title": "Почему ваш дизельный генератор не запускается: 7 распространённых причин и решений",
        "excerpt": "Генератор, который отказывается запускаться — одна из самых неприятных проблем для управляющих объектами. Вот 7 самых распространённых причин и как их исправить."
    },
    "es": {
        "title": "Por qué su generador diésel no arranca: 7 causas comunes y soluciones",
        "excerpt": "Un generador diésel que se niega a arrancar es uno de los problemas más frustrantes. Aquí están las 7 causas más comunes y cómo solucionarlas."
    },
    "fr": {
        "title": "Pourquoi votre groupe électrogène diesel ne démarre pas : 7 causes courantes et solutions",
        "excerpt": "Un groupe électrogène diesel qui refuse de démarrer est l'un des problèmes les plus frustrants. Voici les 7 causes les plus courantes et comment les résoudre."
    },
    "de": {
        "title": "Warum Ihr Dieselgenerator nicht startet: 7 häufige Ursachen und Lösungen",
        "excerpt": "Ein Dieselgenerator, der nicht startet, ist eines der frustrierendsten Probleme. Hier sind die 7 häufigsten Ursachen und Lösungen."
    },
    "pt": {
        "title": "Por que seu gerador a diesel não liga: 7 causas comuns e soluções",
        "excerpt": "Um gerador a diesel que se recusa a ligar é um dos problemas mais frustrantes. Aqui estão as 7 causas mais comuns e como resolvê-las."
    },
    "ar": {
        "title": "لماذا لا يعمل مولد الديزل الخاص بك: 7 أسباب شائعة وحلول",
        "excerpt": "المولد الذي يرفض العمل هو أحد أكثر المشاكل إحباطًا. إليك 7 أسباب شائعة وكيفية إصلاحها."
    },
    "tr": {
        "title": "Dizel Jeneratörünüz Neden Çalışmıyor: 7 Yaygın Neden ve Çözümler",
        "excerpt": "Çalışmayı reddeden bir dizel jeneratör, saha yöneticilerinin karşılaştığı en sinir bozucu sorunlardan biridir. İşte en yaygın 7 neden ve çözümleri."
    },
    "th": {
        "title": "ทำไมเครื่องกำเนิดไฟฟ้าดีเซลของคุณไม่ทำงาน: 7 สาเหตุที่พบบ่อยและวิธีแก้ไข",
        "excerpt": "เครื่องกำเนิดไฟฟ้าที่ไม่ยอมสตาร์ทเป็นปัญหาที่น่าหงุดหงิดที่สุดอย่างหนึ่ง นี่คือ 7 สาเหตุที่พบบ่อยและวิธีแก้ไข"
    },
    "vi": {
        "title": "Tại sao máy phát điện diesel của bạn không khởi động: 7 nguyên nhân phổ biến và cách khắc phục",
        "excerpt": "Máy phát điện diesel không chịu khởi động là một trong những vấn đề khó chịu nhất. Đây là 7 nguyên nhân phổ biến và cách khắc phục."
    },
    "id": {
        "title": "Mengapa Genset Diesel Anda Tidak Menyala: 7 Penyebab Umum dan Solusi",
        "excerpt": "Genset diesel yang menolak untuk menyala adalah salah satu masalah paling frustrating. Berikut 7 penyebab umum dan cara mengatasinya."
    }
}

for lang, trans in translations.items():
    filepath = os.path.join(base_dir, lang, f"{slug}.md")
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 替换 frontmatter 里的 title 和 excerpt
        lines = content.split('\n')
        new_lines = []
        in_frontmatter = False
        fm_count = 0
        
        for line in lines:
            if line.strip() == '---':
                fm_count += 1
                new_lines.append(line)
                continue
            
            if fm_count == 1:
                if line.startswith('title:'):
                    new_lines.append(f'title: "{trans["title"]}"')
                elif line.startswith('excerpt:'):
                    new_lines.append(f'excerpt: "{trans["excerpt"]}"')
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        
        new_content = '\n'.join(new_lines)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Updated {lang} frontmatter")

print("Done!")
