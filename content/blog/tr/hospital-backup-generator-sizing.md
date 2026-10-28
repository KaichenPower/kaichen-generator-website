---
title: "Hastaneler için yedek güç dizel jeneratörü: güç seçimi rehberi"
date: "2026-10-28"
excerpt: "Hastane yedek gücü için dizel jeneratör nasıl boyutlandırılır: yük listesi, kVA hesabı, motor yol alma, yakıt otonomisi, yedeklilik ve yük bankası testi."
image: "/images/blog/hospital-generator-sizing.jpg"
---

![Yangzhou fabrikamızda hastane yedek gücü için sessiz dizel jeneratör grubu](/images/blog/hospital-generator-sizing.jpg)

# Hastaneler için yedek güç dizel jeneratörü: güç seçimi rehberi

Hastanede şebeke kesintisi bir rahatsızlık değildir. Kesintiden saniyeler sonra ameliyathanenin ışığı söner, yoğun bakımdaki ventilatörler saatler değil dakikalar dayanan akülere düşer, kan bankası dolapları 6 °C'yi aşmaya başlar, asansörler hastalarla kat arasında kalır ve hemşire çağrı sistemi kararır.

Bu yüzden **hastane yedek gücü için dizel jeneratör**, fabrika veya şantiye jeneratöründen farklı şekilde belirlenir. Bütçeye sığan en büyük grup değil, gücü, yol alma davranışı, yakıt otonomisi, akustiği ve test kayıtları bir akreditasyon denetçisine karşı savunulabilir olması gereken bir yaşam güvenliği makinesidir.

Bu rehber, hastane projelerinde uyguladığımız gerçek hesap sırasını izler: yük listesini kurmak, gerekli düzeltmelerle kVA'ya çevirmek, motor yol almasını kontrol etmek, ardından yakıt, yedeklilik, gürültü ve test kapsamını belirlemek. Sayılar KC serisi teknik föylerimizden, iki gerçek hastane sınıfı ünite dahil.

## 1. Jeneratör hastanede gerçekte neyi besler

Hastanenin elektrik tesisatı genellikle normal besleme ile bir veya birkaç esas baraya ayrılır. Jeneratöre yalnızca esas baralar bağlanır. Bu sınırı doğru çizmek işin yarısıdır.

| Yük grubu | Tipik içerik | Boyutlandırma açısından anlamı |
|---|---|---|
| Yaşam güvenliği | Ameliyathane ve yoğun bakım aydınlatması, yangın alarmı, duman tahliyesi, kaçış aydınlatması, medikal gaz alarmları | Yaklaşık 10 saniyede devreye girme, asla atılamaz |
| Kritik | Yoğun bakım ve yenidoğan cihazları, diyaliz, kan bankası soğutması, eczane soğuk zinciri, laboratuvar inkübatörleri, bilişim ve hemşire çağrı | Gerilim kararlılığı brüt güçten daha önemli |
| Ekipman | Asansörler, su pompaları, yangın pompası, havalandırma, sterilizasyon, kısmen mutfak ve çamaşırhane | Belirleyici olan çalışma gücü değil motor yol alması |
| Opsiyonel | Servis prizleri, standart klima, mutfağın bir bölümü | Genelde bağlanmaz veya aşırı yükte atılır |

Buradan iki pratik kural çıkar. Birincisi: bütçe ve yakıt deposu taşımıyorsa tüm hastaneyi jeneratöre bağlamayın; projelerin çoğu bağlı yükün %40–60'ını esas barada tutar. İkincisi: motor yüklerini çalışma değil yol alma sorunu olarak ele alın; 15 kW'lık bir asansör motoru bir iki saniye boyunca nominal akımının beş ila yedi katını çekebilir.

Mevzuat ülkeye göre değişir — ABD'de NFPA 99 ve NFPA 110, Birleşik Krallık'ta HTM 06-01, Avrupa ve pek çok ihracat pazarında tıbbi mahaller için IEC 60364-7-710. Ayrıntıda ayrılırlar, özde birleşirler: tanımlı esas bara, tanımlı transfer süresi, tanımlı yakıt süresi ve belgelenmiş periyodik testler. kVA'yı sabitlemeden önce yerel sürümü doğrulayın.

## 2. Önce yük listesi, sonra kVA

Hastane jeneratör gücü üzerine her tartışma aslında yük listesi tartışmasıdır. Tabloda, devre devre yapın.

Her kalem için dört veri kaydedin: plaka kW, güç faktörü, talep faktörü (aynı anda ne kadarı çalışıyor) ve yol alma yöntemi (doğrudan, yıldız-üçgen, yumuşak yol verici, frekans invertörü).

Esas barada soğutma grupları, mutfak ve çamaşırhanenin de bulunduğu 200 yataklı bir genel hastane örneği. Bunlar planlama değerleridir, projenin tek hat şemasının yerini tutmaz:

| Yük | Bağlı kW | Talep faktörü | Çalışma kW |
|---|---|---|---|
| Ameliyathane, yoğun bakım, acil aydınlatma, yangın sistemleri | 120 | 1,0 | 120 |
| Yoğun bakım cihazları, kan bankası, eczane, bilişim | 90 | 1,0 | 90 |
| Asansörler (4 × 15 kW) | 60 | 0,6 | 36 |
| Soğutma grubu (esas barada bir adet) | 90 | 1,0 | 90 |
| Pompalar, su arıtma, yangın pompası | 55 | 1,0 | 55 |
| Mutfak ve çamaşırhane, kısmi | 60 | 1,0 | 60 |
| **Toplam çalışma** | | | **451** |

0,9 çeşitlilik faktörü yaklaşık **406 kW** verir. Büyüme payı eklenir — hastane görüntüleme, yatak, klima ekler — bu yüzden %20 gerçekçi bir paydır: **487 kW**. En yakın standart ünite **500 kW / 625 kVA**'dır.

Sonra yol alma durumuna dönün. Soğutma grubu, ameliyathane zaten yüklüyken altı kat akımla doğrudan kalkarsa, grup bu basamağı gerilim düşümü tıbbi cihazları düşürmeyecek şekilde karşılamalıdır. Kontrol geçmezse yanıt otomatik olarak daha büyük jeneratör değildir: soğutma grubuna yumuşak yol verici veya invertör takmaktır ve bu genelde 200 kW fazla alternatörden ucuzdur.

## 3. Formül ve dört düzeltme

Temel çevrim basittir:

**kVA = kW ÷ güç faktörü**

50 Hz gruplarımızın standart 0,8 endüktif faktörüyle 400 kW çalışma yükü, düzeltme öncesi 500 kVA alternatör ister. Ardından dört düzeltme uygulanır.

**Büyüme payı.** Yeni hastane için %15–25; kimse bugünkü yatak sayısına göre boyutlandırmaz.

**Motor yol alma ve kademeli yük.** Geçici gerilim düşümü tıbbi cihazların tolere ettiği sınırda kalmalıdır. KC serisi föylerimizde belirtilen değerler: geçici gerilim sapması ≤ %15, kararlı durum gerilim regülasyonu ≤ %0,5, geçici frekans sapması ≤ %0,5, gerilim ve frekans geri dönüşü ≤ 3 saniye. Yoğun bakım monitörünün transfer sırasında yaşadığı tam olarak budur.

**Saha düzeltmesi (derating).** 40 °C için nominal olan grup 45 °C'de güç kaybeder, yükseklikte daha çok kaybeder. Radyatör bir köşeye üflüyor ve makine dairesi sıcaksa, ya güç düşürülür ya hava yolu düzeltilir.

**Çalışma rejimi.** Yedek nominal (sınırlı saat, aşırı yük yok) ile ana nominal (sürekli, bir saat %10 aşırı yük). Şebeke onarımı sırasında sekiz saat çalışan hastane yedek rejimdedir; her gün kesinti yaşayan hastane ana rejimdedir ve öyle belirtilmelidir.

## 4. İki gerçek referans

Soyut yönlendirme yazması kolay, uygulaması zordur. Bunlar hastane hizmeti için ürettiğimiz iki grup; veriler doğrudan KC teknik föylerinden.

| Parametre | KC-YC200 | KC-YC1600 |
|---|---|---|
| Nominal / yedek güç | 200 kW / 220 kW | 1.600 kW / 1.760 kW |
| Gerilim / akım | 380/220 V, 360 A | 380/220 V, 2.880 A |
| Frekans, güç faktörü | 50 Hz, 0,8 endüktif | 50 Hz, 0,8 endüktif |
| Motor | Yuchai YC6MK350L-D20, 235 / 258,5 kW | Yuchai YC16VTD2700-D30, 1.805 / 1.985 kW |
| Silindir / hacim | Sıralı 6, 10,34 L, 123 × 145 mm | V16, 52,26 L, 152 × 180 mm |
| Aşırı besleme / regülatör | Turbo ara soğutmalı, elektronik | Turbo ara soğutmalı, elektronik |
| Yakıt tüketimi | 200 g/kWh | 200 g/kWh |
| Alternatör | KCI-200, fırçasız, AVR, IP23, H sınıfı, bakır | KCI-1600, fırçasız, AVR, IP23, H sınıfı, bakır |
| Boyutlar (U × G × Y) | 3.000 × 1.100 × 1.750 mm | 5.500 × 2.200 × 2.700 mm |
| Ağırlık | 2.800 kg | 15.800 kg (referans) |
| Gürültü (LP7M) | 102 dB(A) | 102 dB(A) |

**200 kW sınıfı ne zaman uygun.** Esas barası ameliyathane aydınlatması, yoğun bakım cihazları, yangın sistemleri, bilişim ve iki asansörle sınırlı, soğutma grubu normal beslemede kalan klinikler, günübirlik cerrahi merkezleri, küçük hastaneler ve görüntüleme ek binaları. 2.800 kg ve 3 m uzunlukla, 1,2 m kapı genişliği olan bir tadilatta önemli olan şekilde, bodrum makine dairesine transpalet ile girer.

**1.600 kW sınıfı ne zaman uygun.** Esas barası gerçekten merkezi soğutma gruplarını, mutfağı, çamaşırhaneyi, görüntülemeyi ve 10–20 asansörü kapsayan bölge ve eğitim hastaneleri. 15.800 kg ve 5,5 m ile gerçek bir makine dairesi, beton plak veya zemin seviyesinde saha, vinç planı ve genelde tek ünite yerine paralel iki ünite gerekir.

İki boyut arasında ara kademeler vardır; önemli olan föyün, tasarım mühendisinin sayıları doğrudan elektrik modeline aktarabileceği kadar eksiksiz olmasıdır.

## 5. Yakıt otonomisi: 72 saat sorusu

Yakıt, hastane şartnamelerinin en sık denetimde düştüğü yerdir; çünkü tüketim kWh başına verilir ve çevrim unutulur.

200 g/kWh ve yaklaşık 0,84 kg/L dizel ile:

**Saatte litre = nominal kW × 0,2 ÷ 0,84**

| Yük (KC-YC200) | Saatte yakıt | 24 saatte | 72 saatte |
|---|---|---|---|
| %100 (200 kW) | 47,6 L/sa | 1.143 L | 3.429 L |
| %50 ortalama (100 kW) | 23,8 L/sa | 571 L | 1.714 L |
| %25 ortalama (50 kW) | 11,9 L/sa | 286 L | 857 L |

Yani 200 kW'lık bir grup, gerçekçi yarım yük ortalamasında 72 saat için yaklaşık **1.700 L** ister. 2.000 L ana depo belirtin; pay ve kullanılamayan hacim kalır. 1.600 kW grup yarım yükte 24 saatte yaklaşık **4.570 L** ister; bu yüzden büyük hastaneler şasi deposu yerine gömülü veya sızdırmaz havuzlu büyük depo ve yakıt temizleme sözleşmesi kurar.

Denetçilerin baktığı üç ayrıntı: 8 saatlik çalışma için **günlük tank** (ana depodaki sorun grubu hemen durdurmasın diye), hacmin **%110 sızdırmaz havuzu** ve bina otomasyonuna bağlı **yüksek/düşük seviye alarmları**. Yakıt hattında depo çıkışında yangına dayanıklı kesme valfi olsun ve hat asla merdiven boşluğundan geçmesin.

## 6. Yedeklilik, paralel çalışma ve transfer

Tek jeneratör tek arıza noktasıdır. Hastaneler yeni yapıda bunu nadiren kabul eder.

| Şema | Anlamı | Tipik kullanım |
|---|---|---|
| N | Esas yük için boyutlandırılmış tek ünite | Klinikler, küçük hastaneler |
| N+1 | Herhangi biri arızalandığında yükü alabilen ek ünite | Genel hastaneler, 1.000 kW yük için 3 × 500 kW |
| 2N | Ayrı odalarda iki tam bağımsız besleme | Eğitim hastaneleri, büyük yerleşkeler |

Paralel çalışma yedeklilikten fazlasını verir: %100'de bir ünite yerine %60'ta iki ünite yakıt ve gece gürültüsünü azaltır, biri yükü taşırken diğeri bakıma alınabilir. Kontrolörlerimiz yük paylaşımı, izokron yük paylaşımı ve otomatik senkronizasyonu destekler; tek üniteyi ayırmak için bara bağlantı kesicisi vardır.

Transferde anahtar sayı, devreye girme süresidir. Yaşam güvenliği devrelerinde genellikle yaklaşık 10 saniye içinde enerji beklenir; ameliyathane ve yoğun bakım bu boşluğu UPS veya statik transfer anahtarıyla kapatır, jeneratörden anında hazır olmasını beklemez. Tüm diziyi — şebeke kaybı, ATS sinyali, marş, gerilim oluşumu, kesici kapanması, yük alımı — kesintinin gecesinde değil, tezgahta test edin.

## 7. Gürültü, yerleşim ve komşular

Tablodaki iki ünite açık şasi olup LP7M referans noktasında 7 metrede 102 dB(A)'dır. Bu yüksek bir seviyedir, yaklaşık zincirli testere düzeyi. İyi yalıtılmış makine dairesinde veya uzak sahada kabul edilebilir, servis penceresinden 30 metre uzakta kabul edilemez.

Maliyet sırasına göre seçenekler:

- **Sessiz kabin** — genelde üniteyi 7 m'de 70–75 dB(A) aralığına indirir.
- **Oda akustiği** — akustik kaplama, sızdırmaz kapılar, yüzer zemin, doğru hesaplanmış giriş ve çıkış hava susturucuları. Büyük gruplarda sıkı bir sınır değerine ulaşmanın genelde daha ucuz yolu odadır.
- **Yerleşim** — radyatör çıkışını ve baca ağzını servis cephesinden uzaklaştırın, baca yüksekliğini en yakın açılabilir pencereye göre kontrol edin.

Seçim yapmadan önce yerel sınır değerleri kontrol edin, çok değişir; birçok ülkede gece en yakın hassas alıcıda 45–55 dB(A) mertebesinde sınır uygulanır. 1,6 MW'lık bir makinede tek başına kabinin yeteceğini varsaymayın; yetmez.

## 8. Sonucu belirleyen montaj ayrıntıları

Doğru bir föyü çalışan bir tesise çeviren kalemler bunlardır:

- **Soğutma havası.** Radyatörün serbest girişi ve dış havaya kanallı çıkışı olmalı. Posta kutusu büyüklüğünde panjurlu bir oda grubu düşürür ve alternatörü pişirir.
- **Egzoz karşı basıncı.** Uzun hatlar, keskin dirsekler ve küçük susturucular karşı basıncı yükseltir ve güç kaybettirir. Hattı tedarikçinin izin verilen maksimum karşı basıncı elinizdeyken çizin.
- **Titreşim izolasyonu.** Şasi altında yaylı veya kauçuk takozlar, esnek egzoz kompansatörleri ve esnek yakıt bağlantısı. Bunlar olmadan gürültü döşemeden üst katlardaki servislere gider.
- **Kablo kesiti.** Nominal akıma ve gerçek ortam sıcaklığına göre hesaplayın; güç ve kumanda kablolarını ayrı tavlarda tutun.
- **Topraklama ve nötr.** Sistem topraklama düzenini hastanenin elektrik mühendisiyle doğrulayın: jeneratörün nötr işlemi tesisata uymalı, tersi değil.
- **Yangın kompartımanı.** Jeneratör odası kendi algılama ve genelde kendi söndürme sistemi olan bir yangın kompartımanıdır.
- **Erişim.** Alternatör ucunu ve motorun iki yanını erişilebilir bırakın; bakımı yapılamayan grup erken arızalanır.

## 9. Test: çoğu tedarikçinin atladığı bölüm

Hastane jeneratörü, ihtiyaç duyulduğu gece değerlendirilir. Bu yüzden Yangzhou fabrikamızdan çıkan her ünite sevkten önce sabit bir sırayla dijital yük bankasına girer:

| Adım | Süre | Neyin doğrulandığı |
|---|---|---|
| Yüksüz | — | Isınma, yağ basıncı, şarj gerilimi |
| %25 yük | 30 dk | Gerilim ve frekans kararlılığı, egzoz sıcaklığı |
| %50 yük | 30 dk | Regülatör tepkisi, tüketim, gürültü |
| %75 yük | 60 dk | Soğutma sistemi, soğutma sıvısı sıcaklığı, kayış gerginliği |
| %100 yük | 60 dk | Tam nominal çıkış, gerilim regülasyonu ±%1,5 içinde |
| %110 aşırı yük | 1 dk | Koruma açması ve alarm doğrulaması |

Test sonrası termal döngüden sonra izolasyon direnci ve toprak sürekliliğini kontrol eder, tüm koruma fonksiyonlarını (aşırı hız, yüksek su sıcaklığı, düşük yağ basıncı, aşırı akım, acil stop) doğrular ve ATS dizisini baştan sona tezgahta test ederiz. Test raporu üniteyle birlikte gider.

Proje tanıklı test, üçüncü taraf muayene raporu (BV, SGS veya TUV) veya sahaya özgü FAT protokolü istiyorsa bu, sevkten bir hafta önce değil, ünite üretime girmeden önce planlanmalıdır.

## 10. Hastaneler neden Kaichen ile çalışıyor

Çin'in Yangzhou kentinde 20 kVA'dan 3.000 kVA'ya jeneratör grupları üretiyoruz ve hastane segmenti işimizin önemli bir parçası. Bu segmentte diğerlerinden daha çok öne çıkan üç şey var.

**Alternatörlerimizi kendimiz üretiyoruz.** KCI serisi bakır sargılı, H sınıfı izolasyonlu, IP23 korumalı, AVR kontrollü ve montajla aynı tesiste üretilir. Bir hastane belirli bir geçici tepki istediğinde dışarıdan alternatör aramak yerine onu değiştiririz.

**Tam yükte, kendi tesisimizde test ediyoruz.** 2 MW dijital yük bankası, 1.600 kW'lık bir ünitenin sevkten önce %110'da kanıtlanmasını sağlar; sadece avluda boşta çalıştırmakla değil.

**Müşterinin dilinde dokümante ediyoruz.** Teknik föyler, işletme ve bakım kılavuzları, kontrol mantığı açıklamaları ve etiketler yayınladığımız dillerde verilebilir; bu, saha ekibi İngilizce konuşmadığında devreye almayı kısaltır.

Hastane referanslarımız belediye hastanesi için 200 kW'lık bir üniteden bölge hastanesi yerleşkeleri için 1.600–1.800 kW sınıfı kurulumlara uzanır; planlı yük bankası testleriyle yıllardır yedek hizmette olan makineler dahil. Her sevkiyatta CE ve ISO 9001 dokümantasyonu, ilk bakım aralığı için yedek parça seti ve devreye alma sırasında 24/7 teknik destek bulunur.

## Sık sorulan sorular

**Bir hastane hangi güçte jeneratöre ihtiyaç duyar?**
Yatak sayısına değil esas baraya bağlıdır. Ameliyathane aydınlatması, yoğun bakım cihazları ve iki asansörü olan bir klinik genelde 150–250 kW ister. Soğutma grupları esas barada olan 200 yataklı genel hastane çoğunlukla 400–600 kW aralığına düşer. Mutfak, çamaşırhane, görüntüleme ve 15+ asansörü olan bölge yerleşkesi genelde 1.200–2.000 kW, çoğunlukla paralel iki veya daha fazla ünite ister.

**Yakıt kaç saat yetmeli?**
Yaygın şartnameler tanımlı yükte 72 saat, kritik tesislerde bazen 96 saat ister. Depoyu beklenen ortalama yükteki gerçek g/kWh değerinden boyutlandırın: 200 kW ünite yarım yükte 72 saat için yaklaşık 1.700 L ister.

**Dizel jeneratör ameliyathaneleri besleyebilir mi?**
Evet, ama doğrudan değil. Ameliyathane genelde jeneratör yükü alana kadar geçen 10–30 saniyeyi kapatan UPS veya statik transfer anahtarı üzerinden beslenir; jeneratörün işi bundan sonra gerilim ve frekansı tıbbi cihazların tolere ettiği sınırlarda tutmaktır.

**Hastane için sessiz kabin mi açık grup mu?**
Hastalardan, personelden veya sınır çizgisinden duyulan her şey için sessiz kabin. Açık grup yalnızca iyi yalıtılmış makine dairesinde veya uzak sahada pratiktir.

**Hastane jeneratörü ne sıklıkla test edilmeli?**
Aylık yüksüz veya düşük yüklü çalıştırma artı yıllık tam yük testi yaygın bir temeldir; birçok akreditasyon şeması belgelenmiş aylık test ve nominal güçte yıllık yük testi ister. ATS'yi ayrı değil aynı anda test edin.

## Sonraki adım

Bir hastane ünitesi belirliyorsanız esas bara yük listesini ve saha koşullarını gönderin — yükseklik, ortam sıcaklığı, sınır gürültü değeri, istenen yakıt süresi — ve boyutlandırmayı pratik kurala göre değil gerçek yol alma durumuna göre yapalım. Ürettiğimiz makine sınıfını [Cummins 200 kW sessiz jeneratör](/tr/products/cummins-200kw-silent-diesel-generator/), [Yuchai 300 kW sessiz jeneratör](/tr/products/yuchai-300kw-silent-diesel-generator/) ve [Mitsubishi 1000 kW açık jeneratör](/tr/products/mitsubishi-1000kw-open-diesel-generator/) sayfalarında görebilir, ya da tek hat şemanızla [bize ulaşabilirsiniz](/tr/contact/).
