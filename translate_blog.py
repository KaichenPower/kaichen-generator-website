# -*- coding: utf-8 -*-
"""Translate blog frontmatter (title+excerpt) to 10 locales.
Reads English markdown files, writes translated frontmatter + English body (body translation follows).
"""
import yaml, glob, os, re

# slug -> { locale: (title, excerpt) }
T = {}

# 1. 120kW-backup-set-on-tight-budget
T['120kW-backup-set-on-tight-budget'] = {
  'ru': ('120 кВт резервная установка при ограниченном бюджете: на чём сэкономить, а на чём нельзя',
         '120 кВт бесшумная установка — где у бюджетных покупателей самый трудный выбор. На чём можно сэкономить, на чём нельзя, и как установка на базе Shangchai находит своё место в небольших мастерских и коммерческих зданиях.'),
  'es': ('Construir un grupo de respaldo de 120kW con presupuesto ajustado: qué negociar y qué no',
         'Un grupo silencioso de 120kW es donde los compradores con presupuesto toman sus decisiones más difíciles. Qué puede ahorrar, qué no, y cómo un grupo basado en Shangchai encuentra su lugar en talleres pequeños y edificios comerciales.'),
  'fr': ('Construire un groupe secours de 120kW avec un budget serré : quoi négocier et quoi garder',
         'Un groupe silencieux de 120kW est là où les acheteurs à budget serré font leurs choix les plus difficiles. Ce que vous pouvez économiser, ce que vous ne pouvez pas, et comment un groupe basé sur Shangchai trouve sa place dans les petits ateliers et bâtiments commerciaux.'),
  'de': ('120kW-Notstromaggregat mit kleinem Budget: Was man handeln kann und was nicht',
         'Ein 120kW-Schallschutzaggregat ist der Punkt, an dem Budgetkäufer ihre schwierigsten Entscheidungen treffen. Woran Sie sparen können, woran nicht und wie ein Shangchai-Aggregat in kleinen Werkstätten und Gewerbebauten seinen Platz findet.'),
  'pt': ('Montar um grupo de emergência de 120kW com orçamento apertado: o que negociar e o que não',
         'Um grupo silencioso de 120kW é onde os compradores com orçamento apertado fazem suas escolhas mais difíceis. O que você pode economizar, o que não pode, e como um grupo baseado em Shangchai encontra seu lugar em pequenas oficinas e edifícios comerciais.'),
  'ar': ('بناء وحدة احتياطية 120 كيلوواط بميزانية محدودة: ما يمكن المساومة فيه وما لا',
         'وحدة كاتم الصوت 120 كيلوواط حيث يتخذ المشترون ذوو الميزانية المحدودة أصعب قراراتهم. ما يمكنك التوفير فيه، وما لا يمكن، وكيف تجد وحدة أساسها Shangchai مكانها في الورش الصغيرة والمباني التجارية.'),
  'tr': ('Sıkı Bütçeyle 120kW Yedek Jeneratör Kurmak: Neyi Takas Edebilirsiniz, Neyi Edemezsiniz',
         '120kW sessiz jeneratör, bütçe dostu alıcıların en zor kararları verdiği noktadır. Nereden tasarruf edebileceğiniz, nereden edemeyeceğiniz ve Shangchai temelli bir jeneratörün küçük atölyelerde ve ticari binalarda nasıl yer bulduğu.'),
  'th': ('สร้างเครื่องสำรองไฟ 120 กิโลวัตต์ด้วยงบประมาณจำกัด: อะไรที่แลกเปลี่ยนได้และอะไรที่ไม่ได้',
         'เครื่องคงทนเสียง 120 กิโลวัตต์คือจุดที่ผู้ซื้องบจำกัดตัดสินใจยากที่สุด สิ่งที่ประหยัดได้ สิ่งที่ประหยัดไม่ได้ และเครื่องที่ใช้เครื่องยนต์ Shangchai เข้าที่ในโรงงานขนาดเล็กและอาคารพาณิชย์ได้อย่างไร'),
  'vi': ('Lắp đặt tổ máy dự phòng 120kW với ngân sách eo hẹp: Nên đánh đổi gì và không nên gì',
         'Tổ máy chống ồn 120kW là nơi người mua ngân sách eo hẹp đưa ra những lựa chọn khó khăn nhất. Những gì bạn có thể tiết kiệm, những gì không thể, và tổ máy dựa trên Shangchai tìm thấy vị trí của nó trong các xưởng nhỏ và tòa nhà thương mại như thế nào.'),
  'id': ('Membangun Grup Backup 120kW dengan Anggaran Terbatas: Apa yang Bisa Ditawar dan Tidak',
         'Grup silent 120kW adalah tempat pembeli beranggaran ketat membuat pilihan tersulit. Apa yang bisa dihemat, apa yang tidak bisa, dan bagaimana grup berbasis Shangchai menemukan tempatnya di bengkel kecil dan gedung komersial.'),
}

# 2. 50kw-generator-for-clinic-or-farm
T['50kw-generator-for-clinic-or-farm'] = {
  'ru': ('Генератор 50 кВт для клиники или фермы: правильный ли это размер?',
         'Бесшумная установка 50 кВт — частое решение для сельской клиники, семейной фермы или офисного склада. Руководство покупателя по честному подбору мощности — и нагрузкам, которые тихо её превышают.'),
  'es': ('Generador de 50kW para una clínica o granja: ¿Es este el tamaño correcto?',
         'Un grupo silencioso de 50kW suele ser la respuesta para una clínica rural, una granja familiar o un almacén de oficinas. Una guía del comprador para dimensionarlo honestamente — y las cargas que lo exceden silenciosamente.'),
  'fr': ('Générateur 50kW pour une clinique ou une ferme : Est-ce la bonne taille ?',
         'Un groupe silencieux de 50kW est souvent la solution pour une clinique rurale, une ferme familiale ou un entrepôt de bureaux. Un guide d\'achat pour dimensionner honnêtement — et les charges qui le dépassent silencieusement.'),
  'de': ('50kW-Generator für Klinik oder Bauernhof: Ist das die richtige Größe?',
         'Ein 50kW-Schallschutzaggregat ist oft die Lösung für eine Landklinik, einen Familienbauernhof oder ein Lagerbüro. Ein Kaufratgeber zur ehrlichen Dimensionierung — und Lasten, die es leise übersteigen.'),
  'pt': ('Gerador de 50kW para uma clínica ou fazenda: Este é o tamanho certo?',
         'Um grupo silencioso de 50kW costuma ser a resposta para uma clínica rural, uma fazenda familiar ou um escritório de armazém. Um guia do comprador para dimensioná-lo com honestidade — e as cargas que o excedem silenciosamente.'),
  'ar': ('مولد 50 كيلوواط لعيادة أو مزرعة: هل هذا الحجم مناسب؟',
         'وحدة كاتمة الصوت 50 كيلوواط غالباً ما تكون الحل للعيادة الريفية أو المزرعة العائلية أو مستودع المكاتب. دليل المشتري لتحديد الحجم بصدق — والأحمال التي تتجاوزه بهدوء.'),
  'tr': ('Klinik veya Çiftlik için 50kW Jeneratör: Doğru Boyut Bu mu?',
         '50kW sessiz jeneratör genellikle bir kırsal klinik, aile çiftliği veya depo ofisi için doğru cevaptır. Boyutlandırmayı dürüstçe yapan bir alıcı rehberi — ve sessizce aşan yükler.'),
  'th': ('เครื่องกำเนิดไฟฟ้า 50 กิโลวัตต์สำหรับคลินิกหรือฟาร์ม: ขนาดนี้ใช่ไหม?',
         'เครื่องคงทนเสียง 50 กิโลวัตต์มักเป็นคำตอบสำหรับคลินิกชนบท ฟาร์มครอบครัว หรือโกดังสำนักงาน คู่มือผู้ซื้อในการกำหนดขนาดอย่างตรงไปตรงมา — และภาระที่เกินขีดอย่างเงียบๆ'),
  'vi': ('Máy phát điện 50kW cho phòng khám hoặc trang trại: Có đúng kích thước?',
         'Tổ máy chống ồn 50kW thường là giải pháp cho phòng khám nông thôn, trang trại gia đình hoặc kho văn phòng. Hướng dẫn mua hàng để chọn công suất trung thực — và những tải âm thầm vượt quá nó.'),
  'id': ('Generator 50kW untuk Klinik atau Peternakan: Apakah Ukuran Ini Tepat?',
         'Grup silent 50kW sering menjadi jawaban untuk klinik pedesaan, peternakan keluarga, atau gudang kantor. Panduan pembeli untuk menentukan ukuran dengan jujur — dan beban yang diam-diam melebihinya.'),
}

# 3. cold-climate-320kw-volvo-generator
T['cold-climate-320kw-volvo-generator'] = {
  'ru': ('Резервное питание в холодном климате: почему установка Volvo 320 кВт лучше зимой',
         'Генераторы в холодном климате выходят из строя по предсказуемым причинам. Что меняется при температуре ниже нуля — и почему покупатели на северных объектах смотрят на установку Volvo 320 кВт.'),
  'es': ('Respaldo en clima frío: Por qué un grupo Volvo de 320kW aguanta mejor el invierno',
         'Los generadores en climas fríos fallan por razones predecibles. Qué cambia cuando la temperatura baja de cero — y por qué los compradores en sitios del norte miran un grupo Volvo de 320kW.'),
  'fr': ('Secours en climat froid : Pourquoi un groupe Volvo de 320kW gère mieux l\'hiver',
         'Les générateurs en climat froid tombent en panne pour des raisons prévisibles. Ce qui change quand la température descend sous zéro — et pourquoi les acheteurs sur des sites nordiques se tournent vers un groupe Volvo 320kW.'),
  'de': ('Notstrom in kaltem Klima: Warum ein 320kW-Volvo-Aggregat den Winter besser meistert',
         'Generatoren in kaltem Klima versagen aus vorhersehbaren Gründen. Was sich ändert, wenn die Temperatur unter null fällt — und warum Käufer in nördlichen Standorten auf ein Volvo-320kW-Aggregat setzen.'),
  'pt': ('Reserva em clima frio: Por que um grupo Volvo de 320kW lida melhor com o inverno',
         'Geradores em climas frios falham por razões previsíveis. O que muda quando a temperatura cai abaixo de zero — e por que compradores em locais do norte procuram um grupo Volvo de 320kW.'),
  'ar': ('الطاقة الاحتياطية في المناخ البارد: لماذا تتعامل وحدة Volvo 320 كيلوواط مع الشتاء بشكل أفضل',
         'تفشل المولدات في المناخات الباردة لأسباب يمكن التنبؤ بها. ما يتغير عندما تنخفض الحرارة تحت الصفر — ولماذا ينظر المشترون في المواقع الشمالية إلى وحدة Volvo 320 كيلوواط.'),
  'tr': ('Soğuk İklimde Yedekleme: 320kW Volvo Jeneratörü Kışla Neden Daha İyi Başa Çıkıyor',
         'Soğuk iklimlerde jeneratörler öngörülebilir nedenlerle arızalanır. Sıcaklık sıfırın altına düştüğünde neler değişir — ve kuzeydeki alıcılar neden 320kW Volvo temelli jeneratöre bakar.'),
  'th': ('ระบบสำรองไฟในสภาพอากาศหนาว: เหตุใดเครื่อง Volvo 320 กิโลวัตต์จึงจัดการฤดูหนาวได้ดีกว่า',
         'เครื่องกำเนิดไฟฟ้าในสภาพอากาศหนาวเย็นขัดข้องด้วยเหตุผลที่คาดเดาได้ สิ่งที่เปลี่ยนเมื่ออุณหภูมิต่ำกว่าศูนย์ — และเหตุใดผู้ซื้อในพื้นที่ภาคเหนือจึงมองหาเครื่อง Volvo 320 กิโลวัตต์'),
  'vi': ('Nguồn dự phòng khí hậu lạnh: Tại sao tổ máy Volvo 320kW xử lý mùa đông tốt hơn',
         'Máy phát điện ở khí hậu lạnh hỏng vì những lý do có thể đoán trước. Những gì thay đổi khi nhiệt độ xuống dưới 0 — và tại sao người mua ở các công trình phía bắc lại quan tâm đến tổ máy Volvo 320kW.'),
  'id': ('Backup Iklim Dingin: Mengapa Grup Volvo 320kW Menangani Musim Dingin dengan Lebih Baik',
         'Generator di iklim dingin gagal karena alasan yang dapat diprediksi. Apa yang berubah saat suhu turun di bawah nol — dan mengapa pembeli di lokasi utara melihat grup Volvo 320kW.'),
}

# 4. cummins-200kw-silent-generator
T['cummins-200kw-silent-generator'] = {
  'ru': ('Как выбрать правильный дизельный генератор 200 кВт в кожухе: что нужно знать покупателям',
         'Подбор мощности резервного генератора — где большинство покупателей ошибается. Руководство для покупателя по выбору бесшумной дизельной установки 200 кВт без переплат и недобора.'),
  'es': ('Cómo elegir el generador diesel silencioso de 200kW adecuado: Lo que los compradores deben saber',
         'Dimensionar un generador de respaldo es donde la mayoría de los compradores se equivocan. Una guía enfocada al comprador para elegir un grupo diesel silencioso de 200kW sin gastar de más ni quedarse cortos.'),
  'fr': ('Comment choisir le bon générateur diesel silencieux de 200kW : Ce que les acheteurs doivent savoir',
         'Dimensionner un générateur de secours est là où la plupart des acheteurs se trompent. Un guide axé acheteur pour choisir un groupe diesel silencieux de 200kW sans surcoût ni sous-dimensionnement.'),
  'de': ('So wählen Sie den richtigen 200kW-Schalldämm-Dieselgenerator: Was Käufer wissen müssen',
         'Die Dimensionierung des Notstromaggregats ist der Punkt, an dem die meisten Käufer Fehler machen. Ein käuferorientierter Leitfaden zur Auswahl eines 200kW-Schalldämm-Dieselaggregats ohne Über- oder Unterdimensionierung.'),
  'pt': ('Como escolher o gerador a diesel silencioso de 200kW certo: O que os compradores precisam saber',
         'Dimensionar um gerador de emergência é onde a maioria dos compradores erra. Um guia focado no comprador para escolher um grupo diesel silencioso de 200kW sem pagar mais nem ficar pequeno.'),
  'ar': ('كيف تختار مولد الديزل الكاتم 200 كيلوواط المناسب: ما يحتاج المشترون لمعرفته',
         'تحديد حجم المولد الاحتياطي حيث يخطئ معظم المشترين. دليل موجّه للمشتري لاختيار وحدة ديزل كاتمة 200 كيلوواط دون إفراط أو تقصير.'),
  'tr': ('Doğru 200kW Sessiz Dizel Jeneratör Nasıl Seçilir: Alıcıların Bilmesi Gerekenler',
         'Yedek jeneratör boyutlandırması çoğu alıcının hata yaptığı yerdir. 200kW sessiz dizel grubu fazla harcamadan veya yetersiz kalmadan seçmek için alıcı odaklı bir rehber.'),
  'th': ('วิธีเลือกเครื่องกำเนิดไฟฟ้าดีเซลคงทนเสียง 200 กิโลวัตต์ที่เหมาะสม: สิ่งที่ผู้ซื้อต้องรู้',
         'การกำหนดขนาดเครื่องกำเนิดไฟฟ้าสำรองคือจุดที่ผู้ซื้อส่วนใหญ่ผิดพลาด คู่มือสำหรับผู้ซื้อในการเลือกเครื่องดีเซลคงทนเสียง 200 กิโลวัตต์โดยไม่จ่ายเกินหรือได้น้อยเกินไป'),
  'vi': ('Cách chọn máy phát điện diesel chống ồn 200kW phù hợp: Điều người mua cần biết',
         'Xác định công suất máy phát điện dự phòng là nơi hầu hết người mua mắc sai lầm. Hướng dẫn tập trung vào người mua để chọn tổ máy diesel chống ồn 200kW mà không chi quá đắt hay quá nhỏ.'),
  'id': ('Cara Memilih Grup Diesel Silent 200kW yang Tepat: Yang Perlu Pembeli Tahu',
         'Menentukan ukuran generator backup adalah tempat kebanyakan pembeli salah. Panduan berfokus pembeli untuk memilih grup diesel silent 200kW tanpa overspend atau undersizing.'),
}

# 5. doosan-200kw-silent-generator
T['doosan-200kw-silent-generator'] = {
  'ru': ('Где можно разместить дизельный генератор в городе? Отвечаем на вопросы по размещению и шуму',
         'Самый трудный вопрос при покупке городского генератора — не мощность, а «куда его поставить и не будут ли жаловаться соседи?» Руководство покупателя по размещению бесшумной установки.'),
  'es': ('¿Dónde puede poner un generador diesel en una ciudad? Preguntas sobre ubicación y ruido respondidas',
         'La pregunta más difícil al comprar un generador urbano no es la potencia, sino «¿dónde va, y se quejarán los vecinos?» Una guía del comprador para ubicar un grupo silencioso.'),
  'fr': ('Où placer un générateur diesel en ville ? Questions d\'emplacement et de bruit répondues',
         'La question la plus difficile lors de l\'achat d\'un générateur urbain n\'est pas la puissance, mais « où le mettre, et les voisins vont-ils se plaindre ? » Un guide d\'achat pour l\'implantation d\'un groupe silencieux.'),
  'de': ('Wo kann man einen Dieselgenerator in einer Stadt aufstellen? Standort- und Lärmfragen beantwortet',
         'Die schwierigste Frage beim städtischen Generatorenkauf ist nicht die Leistung, sondern « wohin damit, und beschweren sich die Nachbarn? » Ein Kaufratgeber zur Aufstellung eines Schallschutzaggregats.'),
  'pt': ('Onde colocar um gerador a diesel em uma cidade? Perguntas sobre localização e ruído respondidas',
         'A pergunta mais difícil na compra de um gerador urbano não é a potência, mas « onde ele vai, e os vizinhos vão reclamar? » Um guia do comprador para instalar um grupo silencioso.'),
  'ar': ('أين يمكن وضع مولد ديزل في المدينة؟ إجابات على أسئلة الموقع والضوضاء',
         'أصعب سؤال عند شراء مولد حضري ليس الطاقة، بل «أين يوضع، وهل سيشتكي الجيران؟» دليل المشتري لتحديد موقع وحدة كاتمة.'),
  'tr': ('Şehirde Bir Dizel Jeneratörü Nereye Konur? Yerleşim ve Gürültü Soruları Yanıtlandı',
         'Kentsel jeneratör alımındaki en zor soru güç değil, « nereye konacak ve komşular şikayet eder mi? » Sessiz bir grubun yerleşimi için bir alıcı rehberi.'),
  'th': ('จะวางเครื่องกำเนิดไฟฟ้าดีเซลไว้ที่ไหนในเมือง? คำตอบเรื่องที่ตั้งและเสียงรบกวน',
         'คำถามยากที่สุดในการซื้อเครื่องกำเนิดไฟฟ้าในเมืองไม่ใช่กำลัง แต่「จะวางไว้ที่ไหน และเพื่อนบ้านจะร้องเรียนไหม」คู่มือผู้ซื้อในการตั้งเครื่องคงทนเสียง'),
  'vi': ('Đặt máy phát điện diesel ở đâu trong thành phố? Giải đáp thắc mắc về vị trí và tiếng ồn',
         'Câu hỏi khó nhất khi mua máy phát điện đô thị không phải công suất, mà là « đặt ở đâu, hàng xóm có phàn nàn không? » Hướng dẫn người mua về vị trí lắp đặt tổ máy chống ồn.'),
  'id': ('Di Mana Bisa Menempatkan Generator Diesel di Kota? Pertanyaan Lokasi dan Kebisingan Dijawab',
         'Pertanyaan tersulit saat membeli generator perkotaan bukan daya, tapi "di mana diletakkan, dan apakah tetangga akan komplain?" Panduan pembeli untuk menempatkan grup silent.'),
}

# 6. is-30kw-silent-generator-enough
T['is-30kw-silent-generator-enough'] = {
  'ru': ('Достаточно ли бесшумного генератора 30 кВт для небольшого магазина или офиса?',
         'Небольшому магазину, стоматологической клинике или загородному офису не нужна установка заводского размера. Как покупатели решают, достаточно ли 30 кВт — и когда тихо становится недостаточно.'),
  'es': ('¿Es suficiente un generador silencioso de 30kW para una pequeña tienda u oficina?',
         'Una tienda pequeña, una clínica dental o una oficina rural no necesitan un grupo de tamaño industrial. Cómo los compradores deciden si 30kW es suficiente — y cuando silenciosamente no lo es.'),
  'fr': ('Un générateur silencieux de 30kW est-il suffisant pour un petit magasin ou bureau ?',
         'Un petit magasin, une clinique dentaire ou un bureau rural n\'a pas besoin d\'un groupe de taille industrielle. Comment les acheteurs décident si 30kW suffit — et quand ça ne suffit pas silencieusement.'),
  'de': ('Reicht ein 30kW-Schalldämmgenerator für einen kleinen Laden oder ein Büro?',
         'Ein kleiner Laden, eine Zahnarztpraxis oder ein Landbüro braucht kein Aggregat in Industrieformat. Wie Käufer entscheiden, ob 30kW reicht — und wann es leise doch nicht reicht.'),
  'pt': ('Um gerador silencioso de 30kW é suficiente para uma pequena loja ou escritório?',
         'Uma loja pequena, uma clínica odontológica ou um escritório rural não precisa de um grupo de tamanho industrial. Como os compradores decidem se 30kW é suficiente — e quando silenciosamente não é.'),
  'ar': ('هل مولد كاتم 30 كيلوواط كافٍ لمتجر صغير أو مكتب؟',
         'المتجر الصغير أو عيادة الأسنان أو المكتب الريفي لا يحتاج إلى وحدة بحجم مصنع. كيف يقرر المشترون ما إذا كان 30 كيلوواط كافٍ — وعندما لا يكون كافياً بهدوء.'),
  'tr': ('Küçük Bir Dükkan veya Ofis İçin 30kW Sessiz Jeneratör Yeterli mi?',
         'Küçük bir dükkan, diş kliniği veya kırsal ofis fabrika boyutunda bir gruba ihtiyaç duymaz. Alıcıların 30kW\'ın yeterli olup olmadığına nasıl karar verdiği — ve sessizce yeterli olmadığı durumlar.'),
  'th': ('เครื่องกำเนิดไฟฟ้าคงทนเสียง 30 กิโลวัตต์ เพียงพอสำหรับร้านค้าเล็กหรือสำนักงานไหม?',
         'ร้านค้าเล็ก คลินิกทันตกรรม หรือสำนักงานชนบทไม่ต้องการเครื่องขนาดโรงงาน วิธีที่ผู้ซื้อตัดสินว่า 30 กิโลวัตต์ เพียงพอหรือไม่ — และเมื่อไม่เพียงพออย่างเงียบๆ'),
  'vi': ('Máy phát điện chống ồn 30kW có đủ cho cửa hàng nhỏ hoặc văn phòng?',
         'Cửa hàng nhỏ, phòng khám nha khoa hoặc văn phòng nông thôn không cần tổ máy cỡ nhà máy. Cách người mua quyết định 30kW có đủ không — và khi nào nó âm thầm không đủ.'),
  'id': ('Apakah Generator Silent 30kW Cukup untuk Toko Kecil atau Kantor?',
         'Toko kecil, klinik gigi, atau kantor pedesaan tidak perlu grup ukuran pabrik. Bagaimana pembeli memutuskan apakah 30kW cukup — dan ketika diam-diam tidak cukup.'),
}

# 7. mitsubishi-800kw-silent-generator
T['mitsubishi-800kw-silent-generator'] = {
  'ru': ('Когда нужен большой дизельный генератор или несколько работающих параллельно?',
         'Достаточно ли одного большого генератора для вашего объекта, или нужна параллельная резервированная схема? Руководство по принятию решения для дата-центров, больниц и крупных заводов.'),
  'es': ('¿Cuándo necesita un generador diesel grande, o varios funcionando en paralelo?',
         '¿Es un generador grande suficiente para sus instalaciones, o necesita redundancia paralela? Una guía de decisión para centros de datos, hospitales y grandes plantas.'),
  'fr': ('Quand faut-il un gros générateur diesel, ou plusieurs fonctionnant en parallèle ?',
         'Un gros générateur est-il suffisant pour votre site, ou faut-il une redondance parallèle ? Un guide de décision pour les centres de données, hôpitaux et grandes usines.'),
  'de': ('Wann brauchen Sie einen großen Dieselgenerator oder mehrere im Parallelbetrieb?',
         'Ist ein großer Generator für Ihre Einrichtung ausreichend, oder brauchen Sie parallele Redundanz? Ein Entscheidungshandbuch für Rechenzentren, Krankenhäuser und große Anlagen.'),
  'pt': ('Quando você precisa de um gerador a diesel grande, ou vários funcionando em paralelo?',
         'Um gerador grande é suficiente para sua instalação, ou você precisa de redundância paralela? Um guia de decisão para data centers, hospitais e grandes fábricas.'),
  'ar': ('متى تحتاج مولد ديزل كبيراً، أو عدة مولدات تعمل بالتوازي؟',
         'هل مولد واحد كبير يكفي لمنشأتك، أم تحتاج تكراراً متوازياً؟ دليل قرار لمراكز البيانات والمستشفيات والمصانع الكبيرة.'),
  'tr': ('Ne Zaman Büyük Bir Dizel Jeneratöre veya Paralel Çalışan Birkaç Jeneratöre İhtiyacınız Var?',
         'Tesisiniz için tek büyük jeneratör yeterli mi, yoksa paralel yedeklemeye mi ihtiyacınız var? Veri merkezleri, hastaneler ve büyük tesisler için bir karar rehberi.'),
  'th': ('เมื่อไหร่ที่คุณต้องการเครื่องกำเนิดไฟฟ้าดีเซลขนาดใหญ่ หรือหลายเครื่องทำงานขนานกัน?',
         'เครื่องกำเนิดไฟฟ้าขนาดใหญ่เพียงพอสำหรับสถานที่ของคุณหรือไม่ หรือคุณต้องการระบบขนานสำรอง? คู่มือการตัดสินใจสำหรับศูนย์ข้อมูล โรงพยาบาล และโรงงานขนาดใหญ่'),
  'vi': ('Khi nào bạn cần một máy phát điện diesel lớn, hoặc nhiều máy chạy song song?',
         'Một máy phát điện lớn có đủ cho cơ sở của bạn không, hay cần dự phòng song song? Hướng dẫn quyết định cho trung tâm dữ liệu, bệnh viện và nhà máy lớn.'),
  'id': ('Kapan Anda Perlu Generator Diesel Besar, atau Beberapa yang Berjalan Paralel?',
         'Satu generator besar cukup untuk fasilitas Anda, atau Anda butuh redundansi paralel? Panduan keputusan untuk pusat data, rumah sakit, dan pabrik besar.'),
}

# 8. mobile-power-car-vs-fixed-generator
T['mobile-power-car-vs-fixed-generator'] = {
  'ru': ('Нужна ли вам мобильная электростанция вместо стационарного генератора?',
         'Некоторым объектам не нужен генератор, прикрученный к бетонной площадке. Им нужен тот, что сам приезжает на объект. Когда мобильная электростанция 100 кВт лучше стационарной — и что проверить перед арендой или покупкой.'),
  'es': ('¿Necesita un carro de energía móvil en lugar de un generador fijo?',
         'Algunos sitios no necesitan un generador atornillado a una base de concreto. Necesitan uno que conduzca al trabajo. Una mirada a cuando un carro de energía móvil de 100kW supera a un grupo fijo — y qué verificar antes de alquilar o comprar.'),
  'fr': ('Avez-vous besoin d\'une centrale mobile plutôt qu\'un générateur fixe ?',
         'Certains sites n\'ont pas besoin d\'un générateur boulonné sur une dalle de béton. Ils en ont besoin d\'un qui se rend sur le chantier. Quand une centrale mobile de 100kW bat un groupe fixe — et quoi vérifier avant de louer ou acheter.'),
  'de': ('Brauchen Sie ein mobiles Stromaggregat statt eines festen Generators?',
         'Manche Standorte brauchen keinen Generator, der auf ein Betonfundament geschraubt ist. Sie brauchen einen, der zur Baustelle fährt. Wann ein 100kW-Mobilaggregat ein stationäres schlägt — und was Sie vor dem Mieten oder Kaufen prüfen sollten.'),
  'pt': ('Você precisa de uma unidade de energia móvel em vez de um gerador fixo?',
         'Alguns locais não precisam de um gerador parafusado em uma base de concreto. Eles precisam de um que dirija até o trabalho. Quando uma unidade móvel de 100kW supera um grupo fixo — e o que verificar antes de alugar ou comprar.'),
  'ar': ('هل تحتاج إلى عربة طاقة متنقلة بدلاً من مولد ثابت؟',
         'بعض المواقع لا تحتاج مولداً مثبتاً على قاعدة خرسانية. تحتاج مولداً يقود إلى موقع العمل. متى تتفوق عربة الطاقة المتنقلة 100 كيلوواط على الوحدة الثابتة — وما الذي يجب فحصه قبل الإيجار أو الشراء.'),
  'tr': ('Sabit Jeneratör Yerine Mobil Araç Güç Ünitesine mi İhtiyacınız Var?',
         'Bazı sahalara beton pad\'e cıvatalı bir jeneratör gerekmez. Şantiyeye giden bir tanesine ihtiyaç duyarlar. 100kW mobil güç aracının sabit bir grubu ne zaman yendiği — ve kiralama veya satın almadan önce neleri kontrol etmeniz gerektiği.'),
  'th': ('คุณต้องการรถไฟฟ้าเคลื่อนที่แทนเครื่องกำเนิดไฟฟ้าติดตั้งถาวรไหม?',
         'บางพื้นที่ไม่ต้องการเครื่องกำเนิดไฟฟ้าที่ยึดติดกับฐานคอนกรีต พวกเขาต้องการเครื่องที่ขับไปยังงานได้ เมื่อรถไฟฟ้าเคลื่อนที่ 100 กิโลวัตต์ดีกว่าเครื่องติดตั้งถาวร — และสิ่งที่ควรตรวจสอบก่อนเช่าหรือซื้อ'),
  'vi': ('Bạn có cần xe điện di động thay vì máy phát điện cố định?',
         'Một số địa điểm không cần máy phát điện bắt vít vào bệ bê tông. Họ cần máy chạy đến công trường. Khi nào xe điện di động 100kW hơn tổ máy cố định — và những gì cần kiểm tra trước khi thuê hoặc mua.'),
  'id': ('Apakah Anda Perlu Mobil Daya Bergerak, Bukan Generator Tetap?',
         'Beberapa lokasi tidak perlu generator yang dibaut ke bantalan beton. Mereka butuh yang dikendarai ke lokasi kerja. Kapan mobil daya bergerak 100kW mengalahkan grup tetap — dan apa yang harus diperiksa sebelum menyewa atau membeli.'),
}

# 9. perkins-200kw-silent-generator
T['perkins-200kw-silent-generator'] = {
  'ru': ('Какой двигатель генератора проще обслуживать и ремонтировать за границей?',
         'Генератор — это десятилетние отношения. Если ваш проект за рубежом, выбранный двигатель решает, как быстро его починят при поломке. Руководство покупателя.'),
  'es': ('¿Qué motor de generador es más fácil de mantener y reparar en el extranjero?',
         'Un generador es una relación de diez años. Si su proyecto está en el extranjero, el motor que elija decide qué tan rápido se repara cuando algo se rompe. Una guía del comprador.'),
  'fr': ('Quel moteur de générateur est le plus facile à entretenir et réparer à l\'étranger ?',
         'Un générateur est une relation de dix ans. Si votre projet est à l\'étranger, le moteur que vous choisissez décide de la rapidité de la réparation en cas de panne. Un guide d\'achat.'),
  'de': ('Welcher Generator-Motor ist im Ausland am einfachsten zu warten und zu reparieren?',
         'Ein Generator ist eine zehnjährige Beziehung. Wenn Ihr Projekt im Ausland ist, entscheidet der gewählte Motor, wie schnell er bei einem Defekt repariert wird. Ein Kaufratgeber.'),
  'pt': ('Qual motor de gerador é mais fácil de manter e reparar no exterior?',
         'Um gerador é um relacionamento de dez anos. Se seu projeto está no exterior, o motor que você escolhe decide a rapidez do conserto quando algo quebra. Um guia do comprador.'),
  'ar': ('ما هو محرك المولد الأسهل صيانةً وإصلاحاً في الخارج؟',
         'المولد علاقة تمتد لعشر سنوات. إذا كان مشروعك في الخارج، فإن المحرك الذي تختاره يحدد سرعة إصلاحه عند حدوث عطل. دليل المشتري.'),
  'tr': ('Yurt Dışında Hangi Jeneratör Motorunun Bakımı ve Onarımı En Kolay?',
         'Jeneratör on yıllık bir ilişkidir. Projeniz yurt dışındaysa, seçtiğiniz motor bir şey bozulduğunda ne kadar hızlı onarılacağını belirler. Bir alıcı rehberi.'),
  'th': ('เครื่องยนต์เครื่องกำเนิดไฟฟ้ายี่ห้อไหนดูแลและซ่อมในต่างประเทศง่ายที่สุด?',
         'เครื่องกำเนิดไฟฟ้าคือความสัมพันธ์สิบปี หากโครงการของคุณอยู่ต่างประเทศ เครื่องยนต์ที่คุณเลือกจะกำหนดความเร็วในการซ่อมเมื่อเกิดขัดข้อง คู่มือผู้ซื้อ'),
  'vi': ('Động cơ máy phát điện nào dễ bảo dưỡng và sửa chữa nhất ở nước ngoài?',
         'Máy phát điện là mối quan hệ mười năm. Nếu dự án của bạn ở nước ngoài, động cơ bạn chọn quyết định tốc độ sửa chữa khi có hỏng hóc. Hướng dẫn người mua.'),
  'id': ('Mesin Generator Mana yang Paling Mudah Dirawat dan Diperbaiki di Luar Negeri?',
         'Generator adalah hubungan sepuluh tahun. Jika proyek Anda di luar negeri, mesin yang Anda pilih menentukan seberapa cepat diperbaiki saat ada kerusakan. Panduan pembeli.'),
}

# 10. perkins-280kw-when-engine-brand-matters
T['perkins-280kw-when-engine-brand-matters'] = {
  'ru': ('Perkins 280 кВт против других двигателей: когда бренд внутри кожуха имеет значение',
         'Две бесшумные установки могут выглядеть одинаково снаружи и стоить одинаково. Разница в блоке двигателя. Когда выбор Perkins оправдывает себя — и когда более местный двигатель имеет больше смысла.'),
  'es': ('Perkins 280kW frente a otros motores: Cuando la marca dentro de la carcasa importa',
         'Dos grupos silenciosos pueden parecer idénticos por fuera y costar lo mismo. Lo que cambia es el bloque del motor. Una mirada del comprador a cuándo la elección Perkins se gana su lugar — y cuando un motor más local tiene más sentido.'),
  'fr': ('Perkins 280kW face aux autres moteurs : Quand la marque à l\'intérieur du capot compte',
         'Deux groupes silencieux peuvent sembler identiques de l\'extérieur et coûter le même prix. Ce qui change, c\'est le bloc moteur. Un regard d\'acheteur sur quand le choix Perkins vaut son prix — et quand un moteur plus local a plus de sens.'),
  'de': ('Perkins 280kW im Vergleich zu anderen Motoren: Wenn die Marke im Gehäuse zählt',
         'Zwei Schallschutzaggregate können außen identisch aussehen und gleich viel kosten. Was sich ändert, ist der Motorblock. Ein Käuferblick darauf, wann sich die Perkins-Wahl auszahlt — und wann ein lokaler Motor sinnvoller ist.'),
  'pt': ('Perkins 280kW vs outros motores: Quando a marca dentro da carcaça importa',
         'Dois grupos silenciosos podem parecer idênticos por fora e custar o mesmo. O que muda é o bloco do motor. Um olhar do comprador sobre quando a escolha Perkins se justifica — e quando um motor mais local faz mais sentido.'),
  'ar': ('Perkins 280 كيلوواط مقابل المحركات الأخرى: متى تهم العلامة التجارية داخل الهيكل',
         'وحدتان كاتمتان قد تبدوان متطابقتين من الخارج وتكلفان نفس السعر. ما يتغير هو كتلة المحرك. نظرة المشتري على متى يبرر اختيار Perkins قيمته — ومتى يكون المحرك المحلي أكثر منطقية.'),
  'tr': ('Perkins 280kW Diğer Motorlara Karşı: Kapak İçindeki Marka Ne Zaman Önemlidir',
         'İki sessiz grup dışarıdan aynı görünebilir ve aynı fiyata mal olabilir. Değişen motor bloğudur. Perkins seçiminin ne zaman kendini haklı çıkardığına ve ne zaman daha yerel bir motorun daha mantıklı olduğuna bir alıcı bakışı.'),
  'th': ('Perkins 280 กิโลวัตต์ เทียบกับเครื่องยนต์อื่น: เมื่อแบรนด์ภายในเปลือกสำคัญ',
         'เครื่องคงทนเสียงสองเครื่องอาจดูเหมือนกันจากภายนอกและราคาเท่ากัน สิ่งที่เปลี่ยนคือบล็อกเครื่องยนต์ มุมมองของผู้ซื้อว่าเมื่อใดการเลือก Perkins คุ้มค่า — และเมื่อใดเครื่องยนต์ท้องถิ่นมีความเหมาะสมกว่า'),
  'vi': ('Perkins 280kW so với các động cơ khác: Khi thương hiệu bên trong vỏ quan trọng',
         'Hai tổ máy chống ồn có thể trông giống hệt nhau từ bên ngoài và giá như nhau. Điều khác là khối động cơ. Cách người mua nhìn nhận khi nào lựa chọn Perkins đáng giá — và khi nào động cơ địa phương hơn hợp lý hơn.'),
  'id': ('Perkins 280kW vs Mesin Lain: Kapan Merek di Dalam Casing Berarti',
         'Dua grup silent bisa terlihat identik dari luar dan berharga sama. Yang berubah adalah blok mesin. Pandangan pembeli kapan pilihan Perkins membuahkan hasil — dan kapan mesin yang lebih lokal lebih masuk akal.'),
}

# 11. scania-400kw-silent-generator
T['scania-400kw-silent-generator'] = {
  'ru': ('Сколько топлива потребляет дизельный генератор? Стоимость эксплуатации для покупателей',
         'Счёт — наименьшая статья расходов генератора. Как рассчитать реальные расходы на топливо и эксплуатацию — и когда эффективный двигатель окупает себя.'),
  'es': ('¿Cuánto combustible consume un generador diesel? Costo de operación explicado para compradores',
         'La factura es el costo más pequeño que lleva un generador. Cómo calcular los costos reales de combustible y operación — y cuándo un motor eficiente se paga solo.'),
  'fr': ('Combien de carburant consomme un générateur diesel ? Coût de fonctionnement expliqué aux acheteurs',
         'La facture est le plus petit coût d\'un générateur. Comment calculer les vrais coûts de carburant et de fonctionnement — et quand un moteur efficace s\'amortit de lui-même.'),
  'de': ('Wie viel Kraftstoff verbraucht ein Dieselgenerator? Betriebskosten für Käufer erklärt',
         'Die Rechnung ist die kleinste Kostenposition eines Generators. Wie Sie echte Treibstoff- und Betriebskosten berechnen — und wann sich ein effizienter Motor von selbst amortisiert.'),
  'pt': ('Quanto de combustível um gerador a diesel consome? Custo de operação explicado para compradores',
         'A fatura é o menor custo que um gerador carrega. Como calcular os custos reais de combustível e operação — e quando um motor eficiente se paga por si.'),
  'ar': ('كم يستهلك مولد الديزل من الوقود؟ تكلفة التشغيل موضحة للمشترين',
         'الفاتورة هي أصغر تكلفة يحملها المولد. كيف تحسب تكاليف الوقود والتشغيل الحقيقية — ومتى يدفع المحرك الفعال ثمنه بنفسه.'),
  'tr': ('Bir Dizel Jeneratör Ne Kadar Yakıt Tüketir? Alıcılar İçin Çalışma Maliyeti Açıklandı',
         'Fatura, bir jeneratörün taşıdığı en küçük maliyettir. Gerçek yakıt ve çalışma maliyetleri nasıl hesaplanır — ve verimli bir motor ne zaman kendini amorti eder.'),
  'th': ('เครื่องกำเนิดไฟฟ้าดีเซลใช้เชื้อเพลิงเท่าไหร่? อธิบายค่าใช้จ่ายการทำงานสำหรับผู้ซื้อ',
         'ใบแจ้งหนี้คือต้นทุนที่น้อยที่สุดที่เครื่องกำเนิดไฟฟ้าแบกรับ วิธีคำนวณต้นทุนเชื้อเพลิงและการทำงานจริง — และเมื่อไหร่เครื่องยนต์ประสิทธิภาพสูงคืนทุนได้เอง'),
  'vi': ('Máy phát điện diesel tiêu thụ bao nhiêu nhiên liệu? Giải thích chi phí vận hành cho người mua',
         'Hóa đơn là chi phí nhỏ nhất mà máy phát điện mang theo. Cách tính chi phí nhiên liệu và vận hành thực tế — và khi nào động cơ hiệu quả tự hoàn vốn.'),
  'id': ('Berapa Bahan Bakar yang Dipakai Generator Diesel? Biaya Operasi Dijelaskan untuk Pembeli',
         'Faktur adalah biaya terkecil yang dibawa generator. Cara menghitung biaya bahan bakar dan operasi sebenarnya — dan kapan mesin efisien membayar sendiri.'),
}

# 12. shangchai-200kw-silent-generator
T['shangchai-200kw-silent-generator'] = {
  'ru': ('Как купить резервный генератор при ограниченном бюджете и не пожалеть об этом',
         'Низкий бюджет не означает плохой генератор. Где тратить, где экономить и как купить надёжное резервное питание без переплаты.'),
  'es': ('Cómo comprar un generador de respaldo con presupuesto ajustado sin arrepentimientos',
         'Un presupuesto bajo no significa un mal generador. Dónde gastar, dónde ahorrar y cómo comprar energía de respaldo confiable sin pagar de más.'),
  'fr': ('Comment acheter un générateur de secours avec un budget serré sans le regretter',
         'Un petit budget ne signifie pas un mauvais générateur. Où dépenser, où économiser et comment acheter une alimentation de secours fiable sans surpayer.'),
  'de': ('Wie Sie ein Notstromaggregat mit kleinem Budget kaufen, ohne es zu bereuen',
         'Ein niedriges Budget bedeutet keinen schlechten Generator. Wo man ausgibt, wo man spart und wie man zuverlässige Notstromversorgung ohne Überzahlung kauft.'),
  'pt': ('Como comprar um gerador de emergência com orçamento apertado sem se arrepender',
         'Um orçamento baixo não significa um gerador ruim. Onde gastar, onde economizar e como comprar energia de emergência confiável sem pagar mais.'),
  'ar': ('كيف تشتري مولداً احتياطياً بميزانية محدودة دون ندم',
         'الميزانية المنخفضة لا تعني مولداً سيئاً. أين تنفق، وأين توفر، وكيف تشتري طاقة احتياطية موثوقة دون دفع أكثر.'),
  'tr': ('Sıkı Bütçeyle Yedek Jeneratörü Nasıl Pişman Olmadan Satın Alınır',
         'Düşük bütçe kötü bir jeneratör anlamına gelmez. Nerede harcanır, nereden tasarruf edilir ve güvenilir yedek güç fazla ödenmeden nasıl alınır.'),
  'th': ('วิธีซื้อเครื่องกำเนิดไฟฟ้าสำรองด้วยงบจำกัดโดยไม่ต้องเสียใจภายหลัง',
         'งบประมาณต่ำไม่ได้หมายถึงเครื่องกำเนิดไฟฟ้าที่แย่ จะใช้จ่ายตรงไหน ประหยัดตรงไหน และซื้อระบบสำรองที่เชื่อถือได้โดยไม่จ่ายเกินราคาได้อย่างไร'),
  'vi': ('Cách mua máy phát điện dự phòng với ngân sách eo hẹp mà không hối tiếc',
         'Ngân sách thấp không có nghĩa là máy phát điện kém. Nên chi ở đâu, tiết kiệm ở đâu và cách mua nguồn điện dự phòng đáng tin cậy mà không trả quá đắt.'),
  'id': ('Cara Meli Generator Backup dengan Anggaran Terbatas Tanpa Menyesal',
         'Anggaran rendah bukan berarti generator buruk. Di mana harus belanja, di mana hemat, dan cara membeli daya backup andal tanpa membayar lebih.'),
}

# 13. standby-vs-prime-550kw-generator
T['standby-vs-prime-550kw-generator'] = {
  'ru': ('Резервный или первичный при 550 кВт: выбираем режим, который имеет значение',
         'Два коммерческих предложения на одну и ту же установку 550 кВт могут отличаться на треть, и разница — в режиме работы. Что на самом деле означают standby и prime — и как неправильный выбор сокращает срок жизни дорогой машины.'),
  'es': ('Respaldo vs Prime a 550kW: Elegir el servicio que importa',
         'Dos cotizaciones para el mismo grupo de 550kW pueden diferir en un tercio, y la diferencia es la clasificación de servicio. Qué significan realmente standby y prime — y cómo elegir mal acorta la vida de una máquina costosa.'),
  'fr': ('Secours vs Prime à 550kW : Choisir le service qui compte',
         ' Deux devis pour le même groupe de 550kW peuvent différer d\'un tiers, et la différence est le régime de service. Ce que signifient réellement secours et continu — et comment un mauvais choix raccourcit la vie d\'une machine chère.'),
  'de': ('Standby vs Prime bei 550kW: Den richtigen Betriebsart wählen',
         'Zwei Angebote für dasselbe 550kW-Aggregat können um ein Drittel differieren, und der Unterschied ist die Einsatzart. Was Standby und Prime wirklich bedeuten — und wie eine falsche Wahl das Leben einer teuren Maschine verkürzt.'),
  'pt': ('Emergência vs Prime em 550kW: Escolher o serviço que importa',
         'Dois orçamentos para o mesmo grupo de 550kW podem diferir em um terço, e a diferença é a classificação de serviço. O que standby e prime realmente significam — e como a escolha errada encurta a vida de uma máquina cara.'),
  'ar': ('الاحتياطي مقابل الأساسي عند 550 كيلوواط: اختيار التشغيل المهم',
         'عرضان لنفس الوحدة 550 كيلوواط قد يختلفان بمقدار الثلث، والفرق في تصنيف التشغيل. ما يعنيه الاحتياطي والأساسي فعلاً — وكيف أن الاختيار الخاطئ يقصّر عمر آلة باهظة.'),
  'tr': ('550kW\'da Yedek mi Birincil mi: Önemli Olan Çalışma Rejimi',
         'Aynı 550kW grup için iki teklif üçte bir oranında farklılık gösterebilir ve fark çalışma rejimindedir. Yedek ve birincil\'in gerçekte ne anlama geldiği — ve yanlış seçimin pahalı bir makinenin ömrünü nasıl kısalttığı.'),
  'th': ('สำรอง vs หลักที่ 550 กิโลวัตต์: เลือกโหมดการทำงานที่สำคัญ',
         'ใบเสนอราคาสองใบสำหรับเครื่อง 550 กิโลวัตต์เดียวกันอาจต่างกันหนึ่งในสาม และความแตกต่างคือระดับการทำงาน standby และ prime หมายถึงอะไรจริงๆ — และการเลือกผิดจะทำให้อายุเครื่องจักรราคาแพงสั้นลงอย่างไร'),
  'vi': ('Dự phòng vs liên tục tại 550kW: Chọn chế độ vận hành quan trọng',
         'Hai báo giá cho cùng một tổ máy 550kW có thể chênh nhau một phần ba, và sự khác biệt là cấp vận hành. Standby và prime thực sự có nghĩa là gì — và lựa chọn sai rút ngắn tuổi thọ máy đắt tiền như thế nào.'),
  'id': ('Standby vs Prime di 550kW: Memilih Duty yang Berarti',
         'Dua penawaran untuk grup 550kW yang sama bisa berbeda sepertiga, dan perbedaannya adalah rating tugas. Apa arti sebenarnya standby dan prime — dan bagaimana pilihan yang salah memperpendek umur mesin mahal.'),
}

# 14. volvo-300kw-silent-generator
T['volvo-300kw-silent-generator'] = {
  'ru': ('Как выбрать тихий компактный генератор для современного здания',
         'Крыши, дворы, офисы и больницы предъявляют три требования к шуму: небольшой, тихий, чистый. Как выбрать генератор, подходящий для современного здания.'),
  'es': ('Cómo elegir un generador silencioso y compacto para un edificio moderno',
         'Azoteas, patios, oficinas y hospitales tienen tres demandas de silencio: pequeño, silencioso, limpio. Cómo elegir un generador que encaje en un edificio moderno.'),
  'fr': ('Comment choisir un générateur silencieux et compact pour un bâtiment moderne',
         'Toits, cours, bureaux et hôpitaux ont trois exigences de silence : petit, silencieux, propre. Comment choisir un générateur adapté à un bâtiment moderne.'),
  'de': ('So wählen Sie einen leisen, platzsparenden Generator für ein modernes Gebäude',
         'Dächer, Höfe, Büros und Krankenhäuser haben drei Ruheansprüche: klein, leise, sauber. Wie Sie einen Generator wählen, der zu einem modernen Gebäude passt.'),
  'pt': ('Como escolher um gerador silencioso e compacto para um edifício moderno',
         'Coberturas, pátios, escritórios e hospitais têm três exigências de silêncio: pequeno, silencioso, limpo. Como escolher um gerador que se adapte a um edifício moderno.'),
  'ar': ('كيف تختار مولداً هادئاً موفراً للمساحة لمبنى حديث',
         'الأسطح والأفنية والمكاتب والمستشفيات لديها ثلاثة متطلبات للهدوء: صغير، هادئ، نظيف. كيف تختار مولداً يناسب مبنى حديثاً.'),
  'tr': ('Modern Bir Bina İçin Sessiz, Az Yer Kaplayan Jeneratör Nasıl Seçilir',
         'Çatılar, avlular, ofisler ve hastanelerin üç sessiz talebi vardır: küçük, sessiz, temiz. Modern bir binaya uyan bir jeneratör nasıl seçilir.'),
  'th': ('วิธีเลือกเครื่องกำเนิดไฟฟ้าเงียบประหยัดพื้นที่สำหรับอาคารสมัยใหม่',
         'ดาดฟ้า ลาน สำนักงาน และโรงพยาบาลมีข้อกำหนดด้านความเงียบสามประการ: เล็ก เงียบ สะอาด วิธีเลือกเครื่องกำเนิดไฟฟ้าที่เหมาะกับอาคารสมัยใหม่'),
  'vi': ('Cách chọn máy phát điện yên tĩnh, gọn nhẹ cho tòa nhà hiện đại',
         'Mái nhà, sân trong, văn phòng và bệnh viện có ba yêu cầu về độ yên tĩnh: nhỏ, yên, sạch. Cách chọn máy phát điện phù hợp với tòa nhà hiện đại.'),
  'id': ('Cara Memilih Generator Tenang dan Hemat Ruang untuk Gedung Modern',
         'Atap, halaman, kantor, dan rumah sakit punya tiga tuntutan ketenangan: kecil, tenang, bersih. Cara memilih generator yang cocok untuk gedung modern.'),
}

# 15. weichai-200kw-silent-generator
T['weichai-200kw-silent-generator'] = {
  'ru': ('Как быть уверенным, что резервный генератор действительно запустится при отключении?',
         'Генератор полезен только если запускается, когда он нужен. Что покупателям следует проверить на надёжность, самотестирование и местный сервис перед покупкой.'),
  'es': ('¿Cómo puede estar seguro de que su generador de respaldo realmente arrancará en un corte?',
         'Un generador solo es útil si arranca cuando lo necesita. Qué deben verificar los compradores sobre fiabilidad, auto-prueba y servicio local antes de comprometerse.'),
  'fr': ('Comment être sûr que votre générateur de secours démarrera vraiment en cas de coupure ?',
         'Un générateur n\'est utile que s\'il démarre quand vous en avez besoin. Ce que les acheteurs doivent vérifier sur la fiabilité, l\'auto-test et le service local avant de s\'engager.'),
  'de': ('Wie können Sie sicher sein, dass Ihr Notstromaggregat beim Ausfall wirklich startet?',
         'Ein Generator ist nur nützlich, wenn er startet, wenn Sie ihn brauchen. Was Käufer vor der Zusage über Zuverlässigkeit, Selbsttest und lokalen Service prüfen sollten.'),
  'pt': ('Como você pode ter certeza de que seu gerador de emergência realmente ligará na queda?',
         'Um gerador só é útil se ele liga quando você precisa. O que os compradores devem verificar sobre confiabilidade, autoteste e serviço local antes de fechar.'),
  'ar': ('كيف تتأكد من أن مولدك الاحتياطي سيبدأ فعلاً عند انقطاع الكهرباء؟',
         'المولد مفيد فقط إذا بدأ عندما تحتاجه. ما يجب على المشترين فحصه بشأن الموثوقية والاختبار الذاتي والخدمة المحلية قبل الالتزام.'),
  'tr': ('Yedek Jeneratörünüzün Kesintide Gerçekten Çalışacağından Nasıl Emin Olabilirsiniz?',
         'Bir jeneratör sadece ihtiyacınız olduğunda çalışırsa faydalıdır. Alıcıların karar vermeden önce güvenilirlik, öz test ve yerel servis için kontrol etmesi gerekenler.'),
  'th': ('จะมั่นใจได้อย่างไรว่าเครื่องกำเนิดไฟฟ้าสำรองจะสตาร์ทจริงเมื่อไฟดับ?',
         'เครื่องกำเนิดไฟฟ้ามีประโยชน์ก็ต่อเมื่อมันสตาร์ทเมื่อคุณต้องการ สิ่งที่ผู้ซื้อควรตรวจสอบเรื่องความน่าเชื่อถือ การทดสอบอัตโนมัติ และบริการในพื้นที่ก่อนตัดสินใจ'),
  'vi': ('Làm sao để chắc chắn máy phát điện dự phòng thực sự khởi động khi mất điện?',
         'Máy phát điện chỉ hữu ích nếu nó khởi động khi bạn cần. Những gì người mua nên kiểm tra về độ tin cậy, tự kiểm tra và dịch vụ địa phương trước khi quyết định.'),
  'id': ('Bagaimana Memastikan Generator Backup Anda Benar-Benar Menyala Saat Listrik Padam?',
         'Generator hanya berguna jika menyala saat Anda membutuhkannya. Apa yang harus pembeli periksa tentang keandalan, self-test, dan layanan lokal sebelum memutuskan.'),
}

# 16. what-300kw-generator-runs-in-factory
T['what-300kw-generator-runs-in-factory'] = {
  'ru': ('Что на самом деле приводит в движение резервный генератор 300 кВт на заводе?',
         'Бесшумная установка 300 кВт находится в busy среднем звене между небольшими офисами и промышленными заводами. Практический взгляд на то, какие фабрики, мастерские и здания она обслуживает — и где ей не хватает дыхания.'),
  'es': ('¿Qué hace funcionar un generador de respaldo de 300kW en una fábrica?',
         'Un grupo silencioso de 300kW se sitúa en el punto intermedio entre oficinas pequeñas y plantas industriales. Una mirada práctica a qué fábricas, talleres y edificios encaja — y donde se queda sin aliento.'),
  'fr': ('Qu\'est-ce qui fait réellement tourner un générateur de secours de 300kW dans une usine ?',
         'Un groupe silencieux de 300kW se situe dans le juste milieu entre petits bureaux et usines industrielles. Un regard pratique sur quelles usines, ateliers et bâtiments il convient — et où il s\'essouffle.'),
  'de': ('Was treibt ein 300kW-Notstromaggregat in einer Fabrik wirklich an?',
         'Ein 300kW-Schallschutzaggregat liegt in der belebten Mitte zwischen kleinen Büros und Industrieanlagen. Ein praktischer Blick darauf, welche Fabriken, Werkstätten und Gebäude es passt — und wo ihm die Puste ausgeht.'),
  'pt': ('O que um gerador de emergência de 300kW realmente move em uma fábrica?',
         'Um grupo silencioso de 300kW fica no meio do caminho entre escritórios pequenos e plantas industriais. Um olhar prático sobre quais fábricas, oficinas e edifícios ele serve — e onde fica sem fôlego.'),
  'ar': ('ما الذي يشغّله مولد احتياطي 300 كيلوواط فعلياً في مصنع؟',
         'وحدة كاتمة 300 كيلوواط تقع في المنطقة الوسطى المزدحمة بين المكاتب الصغيرة والمصانع الصناعية. نظرة عملية على المصانع والورش والمباني التي تناسبها — وحيث ينفد تنفسها.'),
  'tr': ('Bir Fabrikada 300kW Yedek Jeneratörü Gerçekten Neyi Çalıştırır?',
         '300kW sessiz grup, küçük ofisler ile endüstriyel tesisler arasındaki hareketli orta noktadadır. Hangi fabrikalara, atölyelere ve binalara uyduğuna ve nerede nefesinin kesildiğine pratik bir bakış.'),
  'th': ('เครื่องสำรองไฟ 300 กิโลวัตต์ ขับเคลื่อนอะไรจริงในโรงงาน?',
         'เครื่องคงทนเสียง 300 กิโลวัตต์อยู่ตรงกลางที่พลุกพล่านระหว่างสำนักงานขนาดเล็กและโรงงานอุตสาหกรรม มุมมองจริงจังว่าโรงงาน เวิร์กชอป และอาคารใดบ้างที่มันเหมาะ — และจุดที่มันหมดแรง'),
  'vi': ('Máy phát điện dự phòng 300kW thực sự chạy gì trong nhà máy?',
         'Tổ máy chống ồn 300kW nằm ở vị trí giữa bận rộn giữa văn phòng nhỏ và nhà máy công nghiệp. Cái nhìn thực tế về những nhà máy, xưởng và tòa nhà nó phù hợp — và khi nào nó hết hơi.'),
  'id': ('Apa yang Sebenarnya Dijalankan Generator Backup 300kW di Pabrik?',
         'Grup silent 300kW berada di tengah sibuk antara kantor kecil dan pabrik industri. Panduan praktis tentang pabrik, bengkel, dan gedung mana yang cocok — dan di mana ia kehabisan napas.'),
}

# 17. whole-factory-500kw-prime-power
T['whole-factory-500kw-prime-power'] = {
  'ru': ('Весь завод на одной установке 500 кВт: как покупатели это планируют',
         'Одна установка 500 кВт, обслуживающая весь завод — это другая задача планирования, чем резервный генератор. Последовательность нагрузок, топливо и резервирование решают, выдержит ли план соприкосновение с полом.'),
  'es': ('Toda la fábrica con un solo grupo de 500kW: Cómo los compradores lo planifican',
         'Un solo grupo de 500kW llevando toda una planta es un problema de planificación diferente al de un grupo de respaldo. La secuenciación de cargas, el combustible y la redundancia deciden si el plan sobrevive al contacto con el suelo.'),
  'fr': ('Faire tourner toute une usine sur un seul groupe de 500kW : Comment les acheteurs le planifient',
         'Un seul groupe de 500kW portant toute une usine est un problème de planification différent d\'un groupe de secours. Le séquençage des charges, le carburant et la redondance décident si le plan survit au contact du sol.'),
  'de': ('Eine ganze Fabrik auf einem 500kW-Aggregat betreiben: Wie Käufer es planen',
         'Ein einzelnes 500kW-Aggregat, das eine ganze Anlage trägt, ist ein anderes Planungsproblem als ein Notstromaggregat. Lastsequenzierung, Kraftstoff und Redundanz entscheiden, ob der Plan den Kontakt mit dem Boden übersteht.'),
  'pt': ('Operando uma fábrica inteira em um único grupo de 500kW: Como os compradores planejam',
         'Um único grupo de 500kW carregando toda a planta é um problema de planejamento diferente de um grupo de emergência. Sequenciamento de cargas, combustível e redundância decidem se o plano sobrevive ao contato com o chão.'),
  'ar': ('تشغيل مصنع كامل على وحدة 500 كيلوواط واحدة: كيف يخطط المشترون',
         'وحدة 500 كيلوواط واحدة تحمل مصنعاً بأكمله هي مشكلة تخطيط مختلفة عن المولد الاحتياطي. تسلسل الأحمال والوقود والتكرار تحدد ما إذا كانت الخطة ستنجو من التلامس مع أرضية المصنع.'),
  'tr': ('Tüm Fabrikayı Tek Bir 500kW Grupta Çalıştırmak: Alıcılar Nasıl Planlıyor',
         'Tüm tesisi taşıyan tek bir 500kW grubu, yedek bir gruptan farklı bir planlama sorunudur. Yük sıralaması, yakıt ve yedeklilik, planın zeminle temastan sağ çıkıp çıkmayacağına karar verir.'),
  'th': ('เดินโรงงานทั้งหมดด้วยเครื่อง 500 กิโลวัตต์เครื่องเดียว: ผู้ซื้อวางแผนอย่างไร',
         'เครื่อง 500 กิโลวัตต์เครื่องเดียวที่รับผิดชอบโรงงานทั้งหมดเป็นปัญหาการวางแผนต่างจากเครื่องสำรอง ลำดับภาระ เชื้อเพลิง และระบบสำรองตัดสินว่าแผนจะรอดจากการลงพื้นโรงงานหรือไม่'),
  'vi': ('Chạy toàn nhà máy trên một tổ máy 500kW: Người mua lập kế hoạch thế nào',
         'Một tổ máy 500kW duy nhất đảm nhận toàn nhà máy là bài toán quy hoạch khác với máy phát dự phòng. Tuần tự tải, nhiên liệu và dự phòng quyết định kế hoạch có trụ vững khi áp dụng thực tế không.'),
  'id': ('Menjalankan Seluruh Pabrik dengan Satu Grup 500kW: Bagaimana Pembeli Merencanakan',
         'Satu grup 500kW yang menopang seluruh pabrik adalah masalah perencanaan yang berbeda dari grup backup. Sekuens beban, bahan bakar, dan redundansi menentukan apakah rencana bertahan saat menyentuh lantai.'),
}

# 18. why-data-centers-choose-500kw
T['why-data-centers-choose-500kw'] = {
  'ru': ('Почему дата-центры и больницы переходят на резервную установку 500 кВт',
         'Между установкой 300 кВт и критически важным блоком 500 кВт существует качественный скачок. Взгляд на нагрузки, которые подталкивают покупателей за эту черту — и проектные различия, которые за этим следуют.'),
  'es': ('Por qué los centros de datos y hospitales pasan a un grupo de respaldo de 500kW',
         'Hay un salto cualitativo entre un grupo de planta de 300kW y una unidad crítica de 500kW. Una mirada a las cargas que empujan a los compradores sobre esa línea — y las diferencias de diseño que siguen.'),
  'fr': ('Pourquoi les centres de données et hôpitaux passent à un groupe secours de 500kW',
         'Il y a un changement d\'échelle entre un groupe de 300kW et une unité critique de 500kW. Un regard sur les charges qui poussent les acheteurs au-delà de cette limite — et les différences de conception qui suivent.'),
  'de': ('Warum Rechenzentren und Krankenhäuser auf ein 500kW-Notstromaggregat aufrüsten',
         'Zwischen einem 300kW-Anlagenaggregat und einer 500kW-Kritikeinheit liegt ein Quantensprung. Ein Blick auf die Lasten, die Käufer über diese Linie drängen — und die Konstruktionsunterschiede, die folgen.'),
  'pt': ('Por que data centers e hospitais migram para um grupo de emergência de 500kW',
         'Há um salto entre um grupo de planta de 300kW e uma unidade crítica de 500kW. Um olhar sobre as cargas que empurram os compradores para essa linha — e as diferenças de projeto que se seguem.'),
  'ar': ('لماذا ترتقي مراكز البيانات والمستشفيات إلى وحدة احتياطية 500 كيلوواط',
         'هناك نقلة نوعية بين وحدة 300 كيلوواط ووحدة حرجة 500 كيلوواط. نظرة على الأحمال التي تدفع المشترين عبر هذا الخط — والاختلافات التصميمية التي تتبع.'),
  'tr': ('Veri Merkezleri ve Hastaneler Neden 500kW Yedek Grubuna Geçiyor',
         '300kW tesis grubu ile 500kW görev kritik bir ünite arasında bir basamak atışı vardır. Alıcıları bu çizgiyi aşmaya iten yükler ve bunu takip eden tasarım farklarına bir bakış.'),
  'th': ('เหตุใดศูนย์ข้อมูลและโรงพยาบาลจึงยกระดับเป็นเครื่องสำรอง 500 กิโลวัตต์',
         'มีการก้าวกระโดดระหว่างเครื่อง 300 กิโลวัตต์กับหน่วยภาระวิกฤติ 500 กิโลวัตต์ มุมมองเกี่ยวกับภาระที่ผลักดันผู้ซื้อข้ามเส้นนั้น — และความแตกต่างด้านการออกแบบที่ตามมา'),
  'vi': ('Tại sao trung tâm dữ liệu và bệnh viện nâng cấp lên tổ máy dự phòng 500kW',
         'Có một bước nhảy giữa tổ máy 300kW và đơn vị trọng yếu 500kW. Cái nhìn về những tải đẩy người mua qua giới hạn đó — và những khác biệt thiết kế kéo theo.'),
  'id': ('Mengapa Pusat Data dan Rumah Sakit Beralih ke Grup Backup 500kW',
         'Ada lompatan besar antara grup pabrik 300kW dan unit mission-critical 500kW. Pandangan tentang beban yang mendorong pembeli melewati batas itu — dan perbedaan desain yang menyusul.'),
}

# 19. yuchai-200kw-silent-generator
T['yuchai-200kw-silent-generator'] = {
  'ru': ('Какой размер генератора нужен небольшой фабрике, мастерской или ферме? Простое руководство',
         'Слишком большой — тратите деньги; слишком маленький — сработает защита. Простое руководство по подбору дизельного генератора для малого бизнеса.'),
  'es': ('¿Qué tamaño de generador necesita una pequeña fábrica, taller o granja? Una guía simple',
         'Demasiado grande y desperdicia dinero; demasiado pequeño y se dispara. Una guía en lenguaje sencillo para dimensionar un generador diesel para una pequeña empresa.'),
  'fr': ('Quelle taille de générateur une petite usine, un atelier ou une ferme a besoin ? Un guide simple',
         'Trop gros et vous gaspillez de l\'argent ; trop petit et il disjoncte. Un guide en langage clair pour dimensionner un générateur diesel pour une petite entreprise.'),
  'de': ('Welche Generatorgröße braucht eine kleine Fabrik, Werkstatt oder ein Bauernhof? Ein einfacher Leitfaden',
         'Zu groß und Sie verschwenden Geld; zu klein und er springt ab. Ein einfacher Leitfaden zur Dimensionierung eines Dieselgenerators für ein kleines Unternehmen.'),
  'pt': ('Qual tamanho de gerador uma pequena fábrica, oficina ou fazenda precisa? Um guia simples',
         'Grande demais e você desperdiça dinheiro; pequeno demais e ele desarma. Um guia em linguagem simples para dimensionar um gerador a diesel para uma pequena empresa.'),
  'ar': ('ما حجم المولد الذي تحتاجه مصنع صغير أو ورشة أو مزرعة؟ دليل بسيط',
         'كبير جداً وتضيع المال؛ صغير جداً فيتعثر. دليل بلغة بسيطة لتحديد حجم مولد الديزل للأعمال الصغيرة.'),
  'tr': ('Küçük Fabrika, Atölye veya Çiftlik İçin Hangi Boyutta Jeneratör Gerekir? Basit Bir Kılavuz',
         'Çok büyükse para israfı; çok küçükse devre keser. Küçük bir işletme için dizel jeneratör boyutlandırması için sade bir rehber.'),
  'th': ('โรงงาน เวิร์กชอป หรือฟาร์มขนาดเล็กต้องการเครื่องกำเนิดไฟฟ้าขนาดไหน? คู่มือง่ายๆ',
         'ใหญ่เกินไปก็เสียเงิน เป็นเกินไปก็ตัดวงจร คู่มือภาษาธรรมดาในการกำหนดขนาดเครื่องกำเนิดไฟฟ้าดีเซลสำหรับธุรกิจขนาดเล็ก'),
  'vi': ('Nhà máy, xưởng hoặc trang trại nhỏ cần máy phát điện cỡ nào? Hướng dẫn đơn giản',
         'Quá lớn thì lãng phí tiền; quá nhỏ thì ngắt mạch. Hướng dẫn ngôn ngữ đơn giản để chọn công suất máy phát điện diesel cho doanh nghiệp nhỏ.'),
  'id': ('Ukuran Generator Apa yang Dibutuhkan Pabrik, Bengkel, atau Peternakan Kecil? Panduan Sederhana',
         'Terlalu besar boros uang; terlalu kecil langsung trip. Panduan bahasa sederhana untuk menentukan ukuran generator diesel untuk usaha kecil.'),
}

# Now write files
import os
for slug, locales in T.items():
    for loc, (title, excerpt) in locales.items():
        d = f'content/blog/{loc}'
        os.makedirs(d, exist_ok=True)
        outpath = f'{d}/{slug}.md'
        # Read English body
        eng = open(f'content/blog/{slug}.md', encoding='utf-8').read()
        parts = eng.split('---', 2)
        body = parts[2].strip()
        # Get date from English frontmatter
        import yaml as y
        fm = y.safe_load(parts[1])
        date = fm.get('date', '2026-10-16')
        content = f'---\ntitle: "{title}"\ndate: "{date}"\nexcerpt: "{excerpt}"\n---\n\n{body}\n'
        open(outpath, 'w', encoding='utf-8').write(content)
    print(f'Wrote {len(locales)} locale files for {slug}')

print('Done!')
