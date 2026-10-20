"""Add cookie namespace translations to all locales."""
import json

cookie_en = {
  "title": "We value your privacy",
  "body": "We use cookies and similar technologies to operate this website, analyze traffic, and personalize content. Under the EU GDPR and UK GDPR, we need your consent before loading non-essential cookies. You can change your choice at any time in our",
  "privacyLink": "Privacy Policy",
  "reject": "Reject Non-Essential",
  "accept": "Accept All"
}

trans = {
  'ru': {"title":"Мы уважаем вашу конфиденциальность","body":"Мы используем файлы cookie и аналогичные технологии для работы сайта, анализа трафика и персонализации контента. В соответствии с GDPR ЕС и Великобритании нам необходимо ваше согласие перед загрузкой необязательных файлов cookie. Вы можете изменить свой выбор в нашей","privacyLink":"Политике конфиденциальности","reject":"Отклонить необязательные","accept":"Принять все"},
  'es': {"title":"Valoramos tu privacidad","body":"Utilizamos cookies y tecnologías similares para operar este sitio, analizar el tráfico y personalizar el contenido. Bajo el GDPR de la UE y del Reino Unido, necesitamos tu consentimiento antes de cargar cookies no esenciales. Puedes cambiar tu elección en cualquier momento en nuestra","privacyLink":"Política de Privacidad","reject":"Rechazar no esenciales","accept":"Aceptar todas"},
  'fr': {"title":"Nous respectons votre vie privée","body":"Nous utilisons des cookies et technologies similaires pour faire fonctionner ce site, analyser le trafic et personnaliser le contenu. Selon le RGPD de l'UE et du Royaume-Uni, nous avons besoin de votre consentement avant de charger des cookies non essentiels. Vous pouvez modifier votre choix à tout moment dans notre","privacyLink":"Politique de Confidentialité","reject":"Refuser non essentiels","accept":"Tout accepter"},
  'de': {"title":"Wir respektieren Ihre Privatsphäre","body":"Wir verwenden Cookies und ähnliche Technologien, um diese Website zu betreiben, Datenverkehr zu analysieren und Inhalte zu personalisieren. Gemäß der EU- und UK-DSGVO benötigen wir Ihre Einwilligung, bevor wir nicht notwendige Cookies laden. Sie können Ihre Auswahl jederzeit in unserer","privacyLink":"Datenschutzerklärung","reject":"Nicht notwendige ablehnen","accept":"Alle akzeptieren"},
  'pt': {"title":"Valorizamos a sua privacidade","body":"Utilizamos cookies e tecnologias semelhantes para operar este site, analisar o tráfego e personalizar o conteúdo. Sob o RGPD da UE e do Reino Unido, precisamos do seu consentimento antes de carregar cookies não essenciais. Pode alterar a sua escolha a qualquer momento na nossa","privacyLink":"Política de Privacidade","reject":"Rejeitar não essenciais","accept":"Aceitar todos"},
  'ar': {"title":"نحن نحترم خصوصيتك","body":"نستخدم ملفات تعريف الارتباط والتقنيات المماثلة لتشغيل هذا الموقع وتحليل حركة المرور وتخصيص المحتوى. بموجب اللائحة العامة لحماية البيانات للاتحاد الأوروبي والمملكة المتحدة، نحتاج إلى موافقتك قبل تحميل ملفات تعريف الارتباط غير الضرورية. يمكنك تغيير اختيارك في أي وقت في","privacyLink":"سياسة الخصوصية","reject":"رفض غير الضرورية","accept":"قبول الكل"},
  'tr': {"title":"Gizliliğinize değer veriyoruz","body":"Bu siteyi çalıştırmak, trafiği analiz etmek ve içeriği kişiselleştirmek için çerezler ve benzer teknolojiler kullanıyoruz. AB ve Birleşik Krallık GDPR kapsamında, zorunlu olmayan çerezleri yüklemeden önce izniniz gereklidir. Tercihinizi istediğiniz zaman şuradan değiştirebilirsiniz:","privacyLink":"Gizlilik Politikası","reject":"Zorunlu Olmayanı Reddet","accept":"Tümünü Kabul Et"},
  'th': {"title":"เราให้ความสำคัญกับความเป็นส่วนตัวของคุณ","body":"เราใช้คุกกี้และเทคโนโลยีที่คล้ายกันเพื่อใช้งานเว็บไซต์นี้ วิเคราะห์การเข้าชม และปรับแต่งเนื้อหา ภายใต้กฎหมาย GDPR ของสหภาพยุโรปและสหราชอาณาจักร เราต้องได้รับความยินยอมจากคุณก่อนโหลดคุกกี้ที่ไม่จำเป็น คุณสามารถเปลี่ยนแปลงตัวเลือกได้ที่","privacyLink":"นโยบายความเป็นส่วนตัว","reject":"ปฏิเสธคุกกี้ที่ไม่จำเป็น","accept":"ยอมรับทั้งหมด"},
  'vi': {"title":"Chúng tôi tôn trọng quyền riêng tư của bạn","body":"Chúng tôi sử dụng cookie và công nghệ tương tự để vận hành trang web, phân tích lưu lượng và cá nhân hóa nội dung. Theo GDPR của EU và Vương quốc Anh, chúng tôi cần sự đồng ý của bạn trước khi tải cookie không thiết yếu. Bạn có thể thay đổi lựa chọn bất cứ lúc nào tại","privacyLink":"Chính sách bảo mật","reject":"Từ chối không thiết yếu","accept":"Chấp nhận tất cả"},
  'id': {"title":"Kami menghargai privasi Anda","body":"Kami menggunakan cookie dan teknologi serupa untuk menjalankan situs ini, menganalisis lalu lintas, dan mempersonalisasi konten. Berdasarkan GDPR UE dan Inggris Raya, kami membutuhkan persetujuan Anda sebelum memuat cookie non-essensial. Anda dapat mengubah pilihan kapan saja di","privacyLink":"Kebijakan Privasi","reject":"Tolak Non-Essensial","accept":"Terima Semua"}
}

for loc, t in trans.items():
    p = f'content/i18n/{loc}.json'
    with open(p, encoding='utf-8') as f:
        data = json.load(f)
    data['cookie'] = t
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# en
with open('content/i18n/en.json', encoding='utf-8') as f:
    data = json.load(f)
data['cookie'] = cookie_en
with open('content/i18n/en.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Cookie translations added to all 11 locales')
