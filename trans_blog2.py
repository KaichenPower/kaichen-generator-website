import os

# Compact translations for fr/de/pt/ar/tr/th/vi/id
data = {
    'fr': {
        'title': 'Checklist de Maintenance du Générateur : 12 Tâches Mensuelles',
        'excerpt': 'Un générateur de secours ne fonctionne que si vous l entretenez. Voici la checklist mensuelle pratique que suit notre équipe de service.',
        'intro': 'Un générateur diesel est une machine qui reste inactive 99% du temps. Les 1% restants, quand le réseau tombe en panne, il doit démarrer, prendre la charge et fonctionner sans accroc. Cela ne se produit qu avec un entretien approprié.',
        'why': 'Un générateur qui ne tourne jamais se dégrade quand même. Le carburant vieillit, les batteries se déchargent, les durites en caoutchouc se fissurent. Une inspection mensuelle de 10 minutes évite 90% des dépannages d urgence.',
        'items': [
            'Démarrez et testez le générateur sous charge d au moins 30% pendant 30 minutes.',
            'Vérifiez la batterie : tension de charge ~27V pour un système 24V. Une batterie HS est la cause n°1 de panne de démarrage.',
            'Contrôlez le niveau et la qualité de l huile. Si elle semble laiteuse ou sent le carburant, prévoyez une vidange.',
            'Vérifiez le niveau du liquide de refroidissement et la concentration antigel avant l hiver.',
            'Inspectez le bâti, les filtres et les conduites de carburant pour des traces humides.',
            'Contrôlez le filtre à air et son indicateur.',
            'Vérifiez la tension de la courroie du ventilateur (flèche de 10-15 mm).',
            'Inspectez l échappement : absence de suie noire, pas de corrosion sur le raccord flexible.',
            'Testez l ATS : simulez une coupure secteur et confirmez le démarrage, le transfert et l arrêt.',
            'Nettoyez le radiateur et les ailettes avec de l air basse pression.',
            'Enregistrez les heures de fonctionnement et la charge moyenne.',
            'Inspectez le capot et l environnement : retirez feuilles, nids, eau stagnante.'
        ],
        'quarterly': 'Tous les 3 mois : filtres à gasoil, densité de la batterie, serrage des connexions. Tous les 12 mois : vidange complète, jeu aux soupapes, injecteurs, test de charge.',
        'bottom': 'Un générateur de secours est une assurance. Vous ne savez s il fonctionne que quand vous en avez besoin. Dix minutes par mois maintiennent cette assurance valide.',
        'cta': 'Si vous achetez un nouveau générateur et souhaitez un plan de maintenance inclus, [contactez notre équipe d ingénierie](/contact).'
    },
    'de': {
        'title': 'Wartungscheckliste für Generatoren: 12 Monatliche Aufgaben',
        'excerpt': 'Ein Notstromgenerator funktioniert nur, wenn Sie ihn warten. Hier ist die praktische monatliche Checkliste, der unser Serviceteam folgt.',
        'intro': 'Ein Dieselgenerator ist eine Maschine, die 99% der Zeit stillsteht. Das andere 1% – wenn das Netz ausfällt – muss er starten, die Last übernehmen und reibungslos laufen. Das gelingt nur bei richtiger Wartung.',
        'why': 'Ein Generator, der nie läuft, verschleißt trotzdem. Kraftstoff wird alt, Batterien verlieren Ladung, Gummischläuche reißen. Ein 10-minütiger monatlicher Rundgang verhindert 90% der Notfalleinsätze.',
        'items': [
            'Starten und testen Sie den Generator unter mindestens 30% Last für 30 Minuten.',
            'Prüfen Sie die Batterie: Ladespannung ~27V bei 24V-System. Eine leere Batterie ist Grund Nr. 1 für Startausfälle.',
            'Kontrollieren Sie Ölstand und Qualität. Bei milchigem Öl oder Kraftstoffgeruch: Ölwechsel.',
            'Prüfen Sie Kühlmittelstand und Frostschutzkonzentration vor dem Winter.',
            'Untersuchen Sie Rahmen, Filter und Leitungen auf nasse Stellen.',
            'Prüfen Sie den Luftfilter und die Anzeige.',
            'Prüfen Sie den Riemen: 10-15 mm Durchbiegung.',
            'Prüfen Sie die Abgasanlage auf Ruß und Korrosion.',
            'Testen Sie den ATS: simulieren Sie Netzausfall und bestätigen Sie Start, Umschaltung und Abschaltung.',
            'Reinigen Sie Kühler und Rippen mit Niederdruckluft.',
            'Notieren Sie Betriebsstunden und Lastdaten.',
            'Prüfen Sie die Haube und Umgebung: entfernen Sie Blätter, Nester, stehendes Wasser.'
        ],
        'quarterly': 'Alle 3 Monate: Kraftstofffilter, Batteriedichte, elektrische Verbindungen. Alle 12 Monate: kompletter Ölwechsel, Ventilspiel, Einspritzdüsen, Lasttest.',
        'bottom': 'Ein Notstromgenerator ist eine Versicherung. Sie merken erst, ob er funktioniert, wenn Sie ihn brauchen. Zehn Minuten pro Monat halten diese Versicherung gültig.',
        'cta': 'Wenn Sie einen neuen Generator kaufen und einen Wartungsplan wünschen, [kontaktieren Sie unser Ingenieurteam](/contact).'
    },
    'pt': {
        'title': 'Checklist de Manutenção do Gerador: 12 Tarefas Mensais',
        'excerpt': 'Um gerador reserva só funciona se você o mantiver. Aqui está a checklist mensal prática que nossa equipe de serviço segue.',
        'intro': 'Um gerador a diesel é uma máquina que fica inativa 99% do tempo. O outro 1%, quando a rede falha, ele precisa ligar, assumir a carga e continuar funcionando sem problemas. Isso só acontece com manutenção adequada.',
        'why': 'Um gerador que nunca funciona também se degrada. O combustível estraga, as baterias perdem carga, as mangueiras de borracha racham. Uma inspeção mensal de 10 minutos evita 90% das chamadas de emergência.',
        'items': [
            'Ligue e teste o gerador com pelo menos 30% de carga por 30 minutos.',
            'Verifique a bateria: tensão de carga ~27V para sistema 24V. Bateria morta é a causa nº1 de falha de partida.',
            'Verifique o nível e a qualidade do óleo. Se parecer leitoso ou cheirar a combustível, troque o óleo.',
            'Verifique o nível do líquido de arrefecimento e a concentração do anticongelante antes do inverno.',
            'Inspecione a base, filtros e tubagens em busca de manchas úmidas.',
            'Verifique o filtro de ar e o indicador.',
            'Verifique a tensão da correia: 10-15 mm de deflexão.',
            'Verifique o sistema de exaustão: sem fuligem preta, sem corrosão na conexão flexível.',
            'Teste o ATS: simule falha de rede e confirme partida, transferência e desligamento.',
            'Limpe o radiador e as aletas com ar de baixa pressão.',
            'Registre as horas de funcionamento e os dados de carga.',
            'Inspecione a canopy e o ambiente: remova folhas, ninhos e água parada.'
        ],
        'quarterly': 'A cada 3 meses: filtros de combustível, densidade da bateria, aperto das conexões. A cada 12 meses: troca completa de óleo, folga das válvulas, injetores, teste de carga.',
        'bottom': 'Um gerador reserva é um seguro. Você só descobre se funciona quando precisa dele. Dez minutos por mês mantêm esse seguro válido.',
        'cta': 'Se você está comprando um novo gerador e quer um plano de manutenção incluso, [contate nossa equipe de engenharia](/contact).'
    },
    'ar': {
        'title': 'قائمة صيانة المولد: 12 مهمة شهرية',
        'excerpt': 'المولد الاحتياطي يعمل فقط إذا قمت بصيانته. إليك قائمة الفحص الشهرية العملية التي يتبعها فريق الخدمة لدينا.',
        'intro': 'مولد الديزل هو آلة تبقى خاملة 99% من الوقت. الـ 1% الأخرى — عند انقطاع الشبكة — يجب أن يعمل ويستقبل الحمل ويستمر دون انقطاع. هذا يحدث فقط مع الصيانة المناسبة.',
        'why': 'المولد الذي لا يعمل أبداً يتدهور أيضاً. الوقود يفسد، البطاريات تفقد شحنها، الخراطيم المطاطية تتشقق. فحص شهري لمدة 10 دقائق يمنع 90% من أعطال الطوارئ.',
        'items': [
            'قم بتشغيل واختبار المولد بحمل 30% على الأقل لمدة 30 دقيقة.',
            'افحص البطارية: جهد الشحن ~27V لنظام 24V. البطارية الميتة هي السبب الأول لفشل التشغيل.',
            'افحص مستوى وجودة الزيت. إذا بدا حليبياً أو رائحته وقود، جدولة تغيير الزيت.',
            'افحص مستوى سائل التبريد وتركيز مانع التجمد قبل الشتاء.',
            'افحص القاعدة والفلاتر والأنابيب بحثاً عن بقع رطبة.',
            'افحص فلتر الهواء والمؤشر.',
            'افحص شد الحزام: انحراف 10-15 ملم.',
            'افحص نظام العادم: لا يوجد سخام أسود، لا تآكل في الوصلة المرنة.',
            'اختبر ATS: حاكي انقطاع الكهرباء وأكد التشغيل والتحويل والإيقاف.',
            'نظف المبرد والزعانف بهواء منخفض الضغط.',
            'سجل ساعات التشغيل وبيانات الحمل.',
            'افحص الكابينة والبيئة: أزل الأوراق والأعشاش والمياه الراكدة.'
        ],
        'quarterly': 'كل 3 أشهر: فلاتر الوقود، كثافة البطارية، شد التوصيلات. كل 12 شهراً: تغيير الزيت الكامل، ضبط الصمامات، فحص الحاقنات، اختبار الحمل.',
        'bottom': 'المولد الاحتياطي هو تأمين. لا تعرف أنه يعمل إلا عندما تحتاجه. عشر دقائق شهرياً تحافظ على هذا التأمين سارياً.',
        'cta': 'إذا كنت تشتري مولداً جديداً وتريد خطة صيانة متضمنة، [اتصل بفريق الهندسة لدينا](/contact).'
    },
    'tr': {
        'title': 'Jeneratör Bakım Kontrol Listesi: Aylık 12 Görev',
        'excerpt': 'Yedek jeneratör sadece bakım yaparsanız çalışır. İşte servis ekibimizin uyguladığı pratik aylık kontrol listesi.',
        'intro': 'Dizel jeneratör zamanın %99unda boşta duran bir makinedir. Diğer %1de, şebeke kesildiğinde, çalışmalı, yükü almalı ve sorunsuz çalışmaya devam etmelidir. Bu sadece doğru bakımla olur.',
        'why': 'Hiç çalışmayan bir jeneratör de bozulur. Yakıt bayatlar, piller şarj kaybeder, lastik hortumlar çatlar. Aylık 10 dakikalık yürüyüş, acil durum çağrılarının %90nı önler.',
        'items': [
            'Jeneratörü en az %30 yük altında 30 dakika çalıştırın.',
            'Pili kontrol edin: şarj gerilimi 24V sistem için ~27V. Bitik pil, çalıştırma başarısızlığının 1numaralı nedenidir.',
            'Yağ seviyesini ve kalitesini kontrol edin. Süt beyazı görünüyorsa veya yakıt kokuyorsa yağ değişimi planlayın.',
            'Soğutucu seviyesini ve antifriz konsantrasyonunu kış öncesi kontrol edin.',
            'Şasi, filtreler ve yakıt hatlarında nemli lekeler olup olmadığına bakın.',
            'Hava filtresini ve göstergeyi kontrol edin.',
            'Kemer gerginliğini kontrol edin: 10-15 mm sapma olmalı.',
            'Egzoz sistemini kontrol edin: siyah kurum olmamalı, esnek bağlantıda korozyon olmamalı.',
            'ATSyi test edin: şebeke kesintisini simüle edin ve çalıştırma, transfer ve kapatmayı doğrulayın.',
            'Radyatörü ve petekleri düşük basınçlı havayla temizleyin.',
            'Çalışma saatlerini ve yük verilerini kaydedin.',
            'Kabin ve çevreyi kontrol edin: yaprak, yuva ve durgun suyu temizleyin.'
        ],
        'quarterly': 'Her 3 ayda: yakıt filtreleri, pil özgül ağırlığı, elektrik bağlantıları. Her 12 ayda: tam yağ değişimi, valf ayarı, enjektör kontrolü, yük bankası testi.',
        'bottom': 'Yedek jeneratör bir sigortadır. İhtiyacınız olduğunda çalışıp çalışmadığını anlarsınız. Aylık 10 dakika bu sigortayı geçerli tutar.',
        'cta': 'Yeni bir jeneratör satın alıyorsanız ve bakım planı dahil istiyorsanız, [mühendislik ekibimizle iletişime geçin](/contact).'
    },
    'th': {
        'title': 'รายการตรวจสอบบำรุงรักษาเครื่องกำเนิดไฟฟ้า: 12 งานประจำเดือน',
        'excerpt': 'เครื่องกำเนิดไฟฟ้าสำรองจะทำงานได้ก็ต่อเมื่อคุณบำรุงรักษา นี่คือรายการตรวจสอบประจำเดือนที่ทีมบริการของเราปฏิบัติ',
        'intro': 'เครื่องกำเนิดไฟฟ้าดีเซลเป็นเครื่องจักรที่อยู่เฉยๆ 99% ของเวลา อีก 1% เมื่อไฟดับ มันต้องสตาร์ท รับภาระ และทำงานต่อไปโดยไม่มีปัญหา สิ่งนี้เกิดขึ้นได้ด้วยการบำรุงรักษาที่เหมาะสมเท่านั้น',
        'why': 'เครื่องกำเนิดที่ไม่เคยทำงานก็เสื่อมสภาพได้ น้ำมันเชื้อเพลิงเก่า แบตเตอรี่หมดสภาพ ท่อยางแตกร้าว การตรวจสอบ 10 นาทีต่อเดือนป้องกันการเรียกด่วน 90%',
        'items': [
            'สตาร์ทและทดสอบเครื่องกำเนิดที่ภาระอย่างน้อย 30% เป็นเวลา 30 นาที',
            'ตรวจสอบแบตเตอรี่: แรงดันประจุ ~27V สำหรับระบบ 24V แบตเตอรี่เสียเป็นสาเหตุอันดับ 1 ของการสตาร์ทไม่ติด',
            'ตรวจสอบระดับและคุณภาพของน้ำมันเครื่อง ถ้าดูขาวข้นหรือมีกลิ่นน้ำมันเชื้อเพลิง ให้เปลี่ยน',
            'ตรวจสอบระดับน้ำหล่อเย็นและความเข้มข้นของสารป้องกันแข็งตัวก่อนฤดูหนาว',
            'ตรวจสอบฐาน เครื่องกรอง และท่อน้ำมันเพื่อหาจุดเปียก',
            'ตรวจสอบไส้กรองอากาศและตัวบ่งชี้',
            'ตรวจสอบความตึงของสายพาน: ควรหย่อน 10-15 มม.',
            'ตรวจสอบระบบไอเสีย: ไม่ควรมีเขม่าสีดำ ไม่ควรมีสนิมที่ข้อต่อยาง',
            'ทดสอบ ATS: จำลองไฟดับและยืนยันการสตาร์ท การถ่ายโอน และการหยุด',
            'ทำความสะอาดหม้อน้ำและครีบระบายความร้อนด้วยลมแรงดันต่ำ',
            'บันทึกชั่วโมงทำงานและข้อมูลภาระ',
            'ตรวจสอบตู้กันเสียงและสภาพแวดล้อม: เอาใบไม้ รัง และน้ำขังออก'
        ],
        'quarterly': 'ทุก 3 เดือน: เปลี่ยนไส้กรองน้ำมันเชื้อเพลิง ตรวจสอบความถ่วงจำเพาะของแบตเตอรี่ ขันข้อต่อไฟฟ้า ทุก 12 เดือน: เปลี่ยนถ่ายน้ำมันเครื่องตรวจสอบวาล์ว หัวฉีด และทดสอบภาระ',
        'bottom': 'เครื่องกำเนิดสำรองคือประกัน คุณจะรู้ว่ามันทำงานได้เมื่อคุณต้องการมัน 10 นาทีต่อเดือนช่วยให้ประกันนี้ใช้ได้',
        'cta': 'หากคุณกำลังซื้อเครื่องกำเนิดใหม่และต้องการแผนบำรุงรักษา [ติดต่อทีมวิศวกรรมของเรา](/contact).'
    },
    'vi': {
        'title': 'Danh Sách Kiểm Tra Bảo Trì Máy Phát Điện: 12 Công Việc Hàng Tháng',
        'excerpt': 'Máy phát điện dự phòng chỉ hoạt động nếu bạn bảo trì nó. Đây là danh sách kiểm tra hàng tháng thực tế mà đội ngũ kỹ thuật của chúng tôi thực hiện.',
        'intro': 'Máy phát điện diesel là máy móc nằm im 99% thời gian. 1% còn lại — khi lưới điện mất — nó phải khởi động, nhận tải và chạy liên tục không sự cố. Điều này chỉ xảy ra khi bảo trì đúng cách.',
        'why': 'Máy phát không bao giờ chạy vẫn xuống cấp. Nhiên liệu hết hạn, ắc quy mất điện, ống cao su nứt vỡ. Kiểm tra 10 phút hàng tháng ngăn 90% sự cố khẩn cấp.',
        'items': [
            'Khởi động và thử máy phát với tải ít nhất 30% trong 30 phút.',
            'Kiểm tra ắc quy: điện áp sạc ~27V cho hệ thống 24V. Ắc quy hết điện là nguyên nhân số 1 khiến máy không khởi động.',
            'Kiểm tra mức và chất lượng nhớt. Nếu thấy màu sữa hoặc có mùi nhiên liệu, lên lịch thay nhớt.',
            'Kiểm tra mức nước làm mát và nồng độ antifreeze trước mùa đông.',
            'Kiểm tra khung, lọc và đường ống nhiên liệu tìm vết ẩm.',
            'Kiểm tra lọc gió và chỉ báo.',
            'Kiểm tra độ căng dây curoa: võng 10-15 mm.',
            'Kiểm tra hệ thống xả: không có muội đen, không ăn mòn khớp mềm.',
            'Kiểm tra ATS: mô phỏng mất điện và xác nhận khởi động, chuyển tải và tắt máy.',
            'Làm sạch bộ tản nhiệt và cánh tản nhiệt bằng khí áp suất thấp.',
            'Ghi lại giờ hoạt động và dữ liệu tải.',
            'Kiểm tra vỏ và môi trường: dọn lá, tổ chim, nước đọng.'
        ],
        'quarterly': 'Mỗi 3 tháng: lọc nhiên liệu, trọng lượng riêng ắc quy, siết kết nối điện. Mỗi 12 tháng: thay nhớt toàn bộ, khe van, kim phun, kiểm tra tải.',
        'bottom': 'Máy phát dự phòng là bảo hiểm. Bạn chỉ biết nó hoạt động khi cần nó. Mười phút mỗi tháng giữ bảo hiểm đó có hiệu lực.',
        'cta': 'Nếu bạn mua máy phát mới và muốn có kế hoạch bảo trì, [liên hệ đội ngũ kỹ thuật của chúng tôi](/contact).'
    },
    'id': {
        'title': 'Checklist Perawatan Genset: 12 Tugas Bulanan',
        'excerpt': 'Genset cadangan hanya bekerja jika Anda merawatnya. Berikut adalah checklist bulanan praktis yang diikuti tim servis kami.',
        'intro': 'Genset diesel adalah mesin yang menganggur 99% dari waktu. 1% sisanya — saat listrik padam — ia harus start, menerima beban, dan terus berjalan tanpa kendala. Itu hanya terjadi dengan perawatan yang tepat.',
        'why': 'Genset yang tidak pernah jalan tetap menurun. Bahan bakar basi, aki kehilangan daya, selang karet retak. Pemeriksaan 10 menit bulanan mencegah 90% panggilan darurat.',
        'items': [
            'Start dan uji genset dengan beban minimal 30% selama 30 menit.',
            'Periksa aki: tegangan pengisian ~27V untuk sistem 24V. Aki mati adalah penyebab #1 genset gagal start.',
            'Periksa level dan kualitas oli. Jika tampak keruh atau berbau bahan bakar, jadwalkan ganti oli.',
            'Periksa level coolant dan konsentrasi antifreeze sebelum musim dingin.',
            'Periksa rangka, filter, dan selang bahan bakar cari titik lembap.',
            'Periksa filter udara dan indikator.',
            'Periksa tegangan fan belt: defleksi 10-15 mm.',
            'Periksa sistem knalpot: tidak ada jelaga hitam, tidak korosi pada sambungan fleksibel.',
            'Uji ATS: simulasi pemadaman listrik dan konfirmasi start, transfer, dan shutdown.',
            'Bersihkan radiator dan sirip dengan udara tekanan rendah.',
            'Catat jam operasi dan data beban.',
            'Periksa kanopi dan lingkungan: buang daun, sarang, air menggenang.'
        ],
        'quarterly': 'Setiap 3 bulan: filter bahan bakar, specific gravity aki, kencangkan koneksi listrik. Setiap 12 bulan: ganti oli penuh, klep, injektor, uji beban.',
        'bottom': 'Genset cadangan adalah asuransi. Anda hanya tahu ia bekerja saat membutuhkannya. Sepuluh menit sebulan menjaga asuransi itu tetap berlaku.',
        'cta': 'Jika Anda membeli genset baru dan ingin paket perawatan, [hubungi tim teknik kami](/contact).'
    }
}

for loc, t in data.items():
    lines = [
        '---',
        f'title: "{t["title"]}"',
        'date: "2026-10-21"',
        f'excerpt: "{t["excerpt"]}"',
        '---',
        '',
        '![Generator maintenance](/images/blog/generator-maintenance-checklist.jpg)',
        '',
        t['intro'],
        '',
        '## Why monthly maintenance matters',
        '',
        t['why'],
        '',
        '## The 12-point monthly checklist',
        '',
    ]
    for i, item in enumerate(t['items'], 1):
        lines.append(f'### {i}. Task {i}')
        lines.append('')
        lines.append(item)
        lines.append('')
    lines.extend([
        '## Quarterly and annual',
        '',
        t['quarterly'],
        '',
        '## Bottom line',
        '',
        t['bottom'],
        '',
        t['cta'],
        '',
    ])
    path = f'content/blog/{loc}/generator-maintenance-checklist.md'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'Written {loc}')
