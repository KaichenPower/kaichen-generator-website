# -*- coding: utf-8 -*-
import yaml as y
slug = 'yuchai-200kw-silent-generator'
bodies = {
'ru': '''![Дизельная генераторная установка 200 кВт в кожухе](/images/blog/yuchai-200kw-silent.jpg)

У вас небольшая фабрика, мастерская или ферма. Вы знаете, что нужно резервное питание. Но единственное число, которое никто не скажет вам прямо: **какого размера он на самом деле должен быть?**

Купите слишком большой — переплатите. Купите слишком маленький — он выключится в момент, когда включится двигатель. Давайте保持简单.

## Два числа, которые нужно вычислить

Забудьте о сложных расчётах. Начните с двух вещей:

1. **Что должно продолжать работать**, когда отключится свет? (Не всё — только самое необходимое.)
2. **Какие из этих вещей — двигатели или насосы**, которые потребруют большой пусковой ток при запуске?

Перечислите их, и у вас есть суть проблемы подбора размера.

## Почему «сложить всё вместе» недостаточно

Сложить рабочую мощность — это близко, но пусковой ток двигателя — это ловушка. Когда компрессор или насос запускается, он на мгновение потребляет в несколько раз больше обычной мощности. Генератор, подобранный только по сумме рабочей мощности, будет давиться при этом первом запуске — именно тогда, когда он вам нужен больше всего.

Поэтому опытные покупатели либо немного завышают размер для пуска двигателей, либо просят нас посмотреть на список нагрузки.

## Правило большого пальца для небольших объектов

После нескольких проектов люди останавливаются на простых ориентирах:

- Работайте на генераторе на уровне **70–80% от его номинальной мощности** при обычном использовании.
- Небольшая мастерская, ферма или магазинный кластер часто попадает в район **100–250 кВА** — что примерно равно установке **80–200 кВт**.
- Если вы близки к верхней границе этого диапазона, **200 кВт (250 кВА)** установка в кожухе — разумный, экономичный выбор.

## Ваши вопросы по подбору размера, ответы

| Ваш вопрос | Практический ответ |
|---|---|
| Как начать? | Перечислите essentials + двигатели, запускающиеся с пусковым рывком |
| Больше — безопаснее? | Нет — переразмер жжёт топливо и изнашивает странным образом |
| Что если я вырасту позже? | Выберите установку чуть выше вашей текущей нагрузки |
| Примерно где небольшой объект? | Часто 80–200 кВт резерв |

## Честная оговорка

Если ваш бизнес быстро растёт, или вы будете работать на установке много часов в день, планируйте заранее — увеличьте размер и обратите внимание на эффективность. Для обычной резервной задачи на небольшом рабочем объекте крепкая, экономичная установка 200 кВт в кожухе — взвешенная, низкорисковая покупка.

## Расскажите нам, что вы питаете

Отправьте нам список необходимого и двигателей. Мы подберём размер генератора под вашу реальную нагрузку — не под круглое число — и дадим вам цену, которую вы сможете заложить в бюджет.
''',
'es': '''![Grupo electrógeno diesel de 200kW dentro de un canopy](/images/blog/yuchai-200kw-silent.jpg)

Tienes una fábrica pequeña, un taller o una granja. Sabes que necesitas energía de respaldo. Pero el único número que nadie te dará directamente es: **¿qué tamaño necesita realmente?**

Compra demasiado grande y gastas de más. Compra demasiado pequeño y se apaga en el momento en que un motor se enciende. Mantengámoslo simple.

## Los dos números a calcular

Olvídate de los cálculos complicados. Empieza con dos cosas:

1. **¿Qué tiene que seguir funcionando** cuando se va la luz? (No todo — solo lo esencial.)
2. **¿Cuáles de esas cosas son motores o bombas** que atraen una gran subida de arranque cuando arrancan?

Enuméralos, y tienes el corazón del problema del dimensionamiento.

## Por qué "sumarlo todo" no es suficiente

Sumar la potencia de funcionamiento te acerca, pero la subida del motor es la trampa. Cuando un compresor o una bomba arranca, tira varias veces su potencia normal por un momento. Un generador dimensionado solo por el total en funcionamiento, se atragantará en ese primer arranque — justo cuando más lo necesitas.

Por qué los compradores experimentados o bien sobre-dimensionan ligeramente para arranques del motor, o nos hacen mirar la lista de carga.

## La regla del pulgar para sitios pequeños

Después de unos proyectos, la gente se asienta en guías simples:

- Haz funcionar el generador alrededor del **70–80% de su potencia nominal** en uso normal.
- Un taller pequeño, granja o grupo de tiendas a menudo cae alrededor de **100–250 kVA** — que es aproximadamente un grupo de **80–200 kW**.
- Si estás cerca de la parte alta de ese rango, un grupo silencioso de **200 kW (250 kVA)** es una opción sensata y económica.

## Tus preguntas de dimensionamiento, respondidas

| Tu pregunta | Respuesta práctica |
|---|---|
| ¿Cómo empiezo? | Lista esenciales + motores que arrancan con subida |
| ¿Más grande es más seguro? | No — sobredimensionado desperdicia combustible y desgasta raro |
| ¿Y si crezco luego? | Elige un grupo un poco por encima de tu carga actual |
| ¿Dónde cae un sitio pequeño? | A menudo 80–200 kW standby |

## La advertencia honesta

Si tu negocio está creciendo rápido, o vas a correr el grupo muchas horas al día, planifica con anticipación — dimensiona más y mira la eficiencia. Para el servicio de respaldo ordinario en un sitio de trabajo pequeño, un grupo robusto y económico de 200 kW silencioso es una compra medida y de bajo riesgo.

## Dinos qué alimentas

Envíanos la lista de esenciales y motores. Dimensionaremos el generador a tu carga real — no un número redondo — y te daremos un precio para tu presupuesto.
''',
'fr': '''![Groupe électrogène diesel de 200 kW dans un capot](/images/blog/yuchai-200kw-silent.jpg)

Vous dirigez une petite usine, un atelier ou une ferme. Vous savez que vous avez besoin d'une alimentation de secours. Mais le seul chiffre que personne ne vous donnera franchement : **de quelle taille en faut-il vraiment ?**

Achetez trop gros et vous surpayez. Achetez trop petit et il s'éteint dès qu'un moteur se met en marche. Restons simples.

## Les deux chiffres à calculer

Oubliez les calculs compliqués. Commencez par deux choses :

1. **Qu'est-ce qui doit continuer à fonctionner** quand le courant saute ? (Pas tout — juste l'essentiel.)
2. **Lequel de ces éléments sont des moteurs ou des pompes** qui tirent une grosse pointe au démarrage ?

Listez-les, et vous avez le cœur du problème de dimensionnement.

## Pourquoi « tout additionner » ne suffit pas

Additionner la puissance de fonctionnement vous rapproche, mais la pointe du moteur est le piège. Quand un compresseur ou une pompe démarre, il tire plusieurs fois sa puissance normale l'espace d'un instant. Un générateur dimensionné sur le seul total de fonctionnement va s'étouffer à ce premier démarrage — justement quand vous en avez le plus besoin.

C'est pourquoi les acheteurs expérimentés surdimensionnent légèrement pour les démarres moteur, ou nous font regarder la liste de charge.

## La règle empirique pour les petits sites

Après quelques projets, les gens s'arrêtent sur des repères simples :

- Faites tourner le générateur à environ **70–80 % de sa puissance nominale** en usage normal.
- Un petit atelier, une ferme ou un regroupement de commerces tombe souvent autour de **100–250 kVA** — ce qui correspond à peu près à un groupe de **80–200 kW**.
- Si vous êtes près du haut de cette plage, un groupe silencieux de **200 kW (250 kVA)** est un choix sensé et économique.

## Vos questions de dimensionnement, réponses

| Votre question | Réponse pratique |
|---|---|
| Par où commencer ? | Listez l'essentiel + moteurs démarrant en pointe |
| Plus gros, plus sûr ? | Non — surdimensionné gaspille le carburant et use bizarrement |
| Si je grandis plus tard ? | Choisissez un groupe un peu au-dessus de votre charge actuelle |
| Vers où tombe un petit site ? | Souvent 80–200 kW de secours |

## La mise en garde honnête

Si votre entreprise croît vite, ou que vous ferez tourner le groupe plusieurs heures par jour, planifiez à l'avance — dimensionnez plus haut et regardez l'efficacité. Pour le secours ordinaire sur un petit site de travail, un groupe silencieux robuste et économique de 200 kW est un achat mesuré et à faible risque.

## Dites-nous ce que vous alimentez

Envoyez-nous la liste de l'essentiel et des moteurs. Nous dimensionnerons le générateur selon votre vraie charge — pas un chiffre rond — et vous donnerons un prix à budgéter.
''',
'de': '''![200 kW schallgeschütztes Dieselaggregat in Kabine](/images/blog/yuchai-200kw-silent.jpg)

Sie betreiben eine kleine Fabrik, eine Werkstatt oder einen Hof. Sie wissen, dass Sie Notstrom brauchen. Aber die eine Zahl, die Ihnen niemand geradeheraus nennt: **Wie groß muss es wirklich sein?**

Zu groß gekauft — Sie überbezahlen. Zu klein gekauft — er schaltet sich ab, sobald ein Motor anspringt. Bleiben wir einfach.

## Die zwei Zahlen, die Sie herausfinden müssen

Vergessen Sie komplizierte Berechnungen. Beginnen Sie mit zwei Dingen:

1. **Was muss weiterlaufen**, wenn der Strom ausfällt? (Nicht alles — nur das Wesentliche.)
2. **Welche davon sind Motoren oder Pumpen**, die beim Start einen großen Anzug ziehen?

Listen Sie diese auf, und Sie haben den Kern des Dimensionierungsproblems.

## Warum „alles zusammenzählen" nicht reicht

Die Laufleistung zusammenzählen bringt Sie nah heran, aber der Motor-Anzug ist die Falle. Wenn ein Kompressor oder eine Pumpe startet, zieht er kurzzeitig ein Mehrfaches seiner Normalleistung. Ein Aggregat, das allein nach der Laufleistung dimensioniert ist, wird bei diesem ersten Start stottern — genau wenn Sie es am nötigsten brauchen.

Deshalb überdimensionieren erfahrene Käufer leicht für Motorstarts, oder lassen uns die Lastliste anschauen.

## Die Faustregel für kleine Standorte

Nach ein paar Projekten bleiben die Leute bei einfachen Leitplanken:

- Fahren Sie den Generator im Normalbetrieb bei etwa **70–80 % seiner Nennleistung**.
- Eine kleine Werkstatt, ein Hof oder ein Ladencluster landet oft bei **100–250 kVA** — was grob einem **80–200 kW**-Aggregat entspricht.
- Wenn Sie nahe am oberen Ende dieses Bereichs sind, ist ein schallgeschütztes **200 kW (250 kVA)**-Aggregat eine vernünftige, wirtschaftliche Wahl.

## Ihre Dimensionierungsfragen, beantwortet

| Ihre Frage | Praktische Antwort |
|---|---| | Wie fange ich an? | Liste Wesentliches + Motoren, die im Anzug starten |
| Größer sicherer? | Nein — überdimensioniert verschwendet Kraftstoff und nutzt seltsam ab |
| Was, wenn ich später wachse? | Wählen Sie ein Aggregat etwas über Ihrer aktuellen Last |
| Wo landet ein kleiner Standort? | Oft 80–200 kW Notbetrieb |

## Der ehrliche Vorbehalt

Wenn Ihr Unternehmen schnell wächst, oder Sie das Aggregat viele Stunden am Tag laufen lassen, planen Sie voraus — dimensionieren Sie höher und achten Sie auf Effizienz. Für den gewöhnlichen Notbetrieb an einem kleinen Arbeitsstandort ist ein robustes, wirtschaftliches 200 kW-Schallaggregat ein abgemessener, risikoarmer Einkauf.

## Sagen Sie uns, was Sie versorgen

Schicken Sie uns die Liste des Wesentlichen und der Motoren. Wir dimensionieren den Generator nach Ihrer echten Last — nicht nach einer runden Zahl — und nennen Ihnen einen Preis, den Sie budgetieren können.
''',
'pt': '''![Grupo gerador diesel de 200kW dentro de um canopy](/images/blog/yuchai-200kw-silent.jpg)

Você dirige uma fábrica pequena, uma oficina ou uma fazenda. Você sabe que precisa de energia reserva. Mas o único número que ninguém te dá direto é: **de que tamanho ele realmente precisa ser?**

Compre grande demais e você gasta à toa. Compre pequeno demais e ele desliga no momento em que um motor liga. Vamos manter simples.

## Os dois números para descobrir

Esqueça cálculos complicados. Comece com duas coisas:

1. **O que precisa continuar rodando** quando a luz acabar? (Nem tudo — só o essencial.)
2. **Quais dessas coisas são motores ou bombas** que puxam uma grande sobrecarga na partida?

Liste essas, e você tem o coração do problema de dimensionamento.

## Por que "somar tudo" não é suficiente

Somar a potência de funcionamento te aproxima, mas a sobrecarga do motor é a armadilha. Quando um compressor ou bomba liga, ele puxa várias vezes sua potência normal por um instante. Um gerador dimensionado só pelo total de funcionamento vai engasgar naquela primeira partida — exatamente quando você mais precisa.

É por isso que compradores experientes ou superdimensionam levemente para partidas de motor, ou nos deixam olhar a lista de carga para eles.

## A regra prática para pequenos locais

Depois de alguns projetos, as pessoas chegam a guias simples:

- Opere o gerador em cerca de **70–80% de sua potência nominal** no uso normal.
- Uma pequena oficina, fazenda ou aglomerado de lojas costuma ficar em torno de **100–250 kVA** — que é mais ou menos um grupo de **80–200 kW**.
- Se você está perto do topo dessa faixa, um grupo silencioso de **200 kW (250 kVA)** é uma escolha sensata e econômica.

## Suas perguntas de dimensionamento, respondidas

| Sua pergunta | Resposta prática |
|---|---|
| Como eu começo? | Liste essenciais + motores que partem na sobrecarga |
| Maior é mais seguro? | Não — superdimensionado desperdiça combustível e desgasta estranho |
| E se eu crescer depois? | Escolha um grupo um pouco acima da sua carga atual |
| Onde um local pequeno costuma ficar? | Frequentemente 80–200 kW standby |

## A ressalva honesta

Se seu negócio está crescendo rápido, ou você vai rodar o grupo muitas horas por dia, planeje com antecedência — aumente o tamanho e olhe a eficiência. Para o serviço de reserva comum em um pequeno local de trabalho, um grupo silencioso robusto e econômico de 200 kW é uma compra medida e de baixo risco.

## Diga-nos o que você alimenta

Nos envie a lista do essencial e dos motores. Dimensionaremos o gerador pela sua carga real — não por um número redondo — e te daremos um preço que você pode orçar.
''',
'ar': '''![مجموعة مولد ديزل 200kW داخل هيكل](/images/blog/yuchai-200kw-silent.jpg)

تدير مصنعاً صغيراً، أو ورشة، أو مزرعة. أنت تعلم أنك بحاجة إلى طاقة احتياطية. ولكن الرقم الوحيد الذي لن يعطيه لك أحد مباشرة: **ما الحجم الذي يحتاجه فعلاً؟**

اشترِ أكبر من اللازم وستبالغ في الإنفاق. اشترِ أصغر من اللازم وسيتوقف في اللحظة التي يُشغَّل فيها محرك. لنبقِ الأمر بسيطاً.

## الرقمان اللذان يجب حسابهما

انسَ الحسابات المعقدة. ابدأ بشيئين:

1. **ما الذي يجب أن يستمر في العمل** عندما ينقطع التيار؟ (ليس كل شيء — فقط الأساسيات.)
2. **أي من هذه الأشياء هي محركات أو مضخات** تسحب اندفاعاً كبيراً عند التشغيل؟

اذكر تلك، ولديك جوهر مشكلة تحديد الحجم.

## لماذا «جمعها كلها» ليس كافياً

جمع الطاقة التشغيلية يقربك، لكن اندفاع المحرك هو الفخ. عندما يشتغل ضاغط أو مضخة، يسحب عدة أضعاف طاقته العادية للحظة. المولد المحدد بحسب الإجمالي التشغيلي وحده سيتعثر عند ذلك التشغيل الأول — بالضبط عندما تحتاجه أكثر من أي وقت.

لهذا السبب يقوم المشترون ذوو الخبرة إما بزيادة الحجم قليلاً لعمليات تشغيل المحركات، أو يجعلوننا نلقي نظرة على قائمة الحمل.

## القاعدة التجريبية للمواقع الصغيرة

بعد بضعة مشاريع، يستقر الناس على أدلة بسيطة:

- شغّل المولد عند حوالي **70–80% من قدرته المقدرة** في الاستخدام العادي.
- ورشة صغيرة أو مزرعة أو مجموعة متاجر تقع غالباً حول **100–250 kVA** — وهو ما يعادل تقريباً مجموعة **80–200 kW**.
- إذا كنت قرب الطرف الأعلى من هذا النطاق، فإن مجموعة كاتمة **200 kW (250 kVA)** هي خيار معقود واقتصادي.

## أسئلتك حول تحديد الحجم، أجابت

| سؤالك | الجواب العملي |
|---|---|
| كيف أبدأ؟ | اذكر الأساسيات + المحركات التي تشتغل بالاندفاع |
| أكبر أكثر أماناً؟ | لا — الحجم الزائد يهدر الوقود ويتآكل بشكل غريب |
| ماذا إذا نموت لاحقاً؟ | اختر مجموعة أعلى قليلاً من حملك الحالي |
| أين يقع الموقع الصغير عادة؟ | غالباً 80–200 kW احتياط |

## التنبيه الصادق

إذا كان نشاطك التجاري ينمو بسرعة، أو ستشغّل المجموعة ساعات طويلة يومياً، خطط للمستقبل مسبقاً — زد الحجم وانظر إلى الكفاءة. للمهام الاحتياطية العادية في موقع عمل صغير، فإن المجموعة الكاتمة المتينة والاقتصادية بقدرة 200 kW هي عملية شراء محسوبة ومنخفضة المخاطر.

## أخبرنا بما تغذيه

أرسل لنا قائمة الأساسيات والمحركات. سنحدد حجم المولد وفقاً لحملك الحقيقي — ليس رقماً مستديراً — ونعطيك سعراً يمكنك وضعه في الميزانية.
''',
'tr': '''![Kanopi içinde 200kW sessiz dizel jeneratör seti](/images/blog/yuchai-200kw-silent.jpg)

Küçük bir fabrika, atölye veya çiftlik işletiyorsunuz. Yedek güce ihtiyacınız olduğunu biliyorsunuz. Ama kimsenin size dümdüz vermeyeceği tek rakam: **gerçekten ne kadar büyük olmalı?**

Çok büyük alırsanız, fazla harcarsınız. Çok küçük alırsanız, bir motor açıldığı an kapanır. Sade tutalım.

## Hesaplanması gereken iki rakam

Karmaşık hesapları unutun. İki şeyle başlayın:

1. **Güç kesildiğinde neyin çalışması gerekir?** (Her şey değil — sadece zorunlu olanlar.)
2. **Bunlardan hangileri motora ya da pompa, başladığında büyük bir başlangıç akımı çeker?**

Bunları listeleyin, boyutlandırma sorununun özüne sahipsiniz.

## Neden "hepsini topla" yeterli değil

Çalışma gücünü toplamak sizi yaklaştırır, ama motor başlangıç akımı tuzaktır. Bir kompresör veya pompa başladığında, bir an için normal gücünün birkaç katını çeker. Sadece çalışma toplamına göre boyutlandırılmış bir jeneratör, o ilk çalışmada kekeler — tam da en çok ihtiyacınız olduğunda.

Bu yüzden tecrübeli alıcılar ya motor başlangıçları için hafifçe büyültürler ya da yük listesine biz bakarız.

## Küçük sahalar için kaba kural

Birkaç projeden sonra insanlar basit kılavuzlara oturur:

- Normal kullanımda jeneratörü **nominal gücünün %70–80'i** civarında çalıştırın.
- Küçük bir atölye, çiftlik veya dükkan kümesi genellikle **100–250 kVA** civarına düşer — bu yaklaşık **80–200 kW** bir settir.
- Bu aralığın üst ucuna yakınsanız, **200 kW (250 kVA)** sessiz bir set mantıklı, ekonomik bir seçimdir.

## Boyutlandırma sorularınız, cevaplandı

| Sorunuz | Pratik cevap |
|---|---|
| Nasıl başlarım? | Zorunlu olanları + başlangıç akımı çeken motorları listeleyin |
| Büyük olan daha mı güvenli? | Hayır — aşırı boyut yakıt israf eder ve tuhaf aşındırır |
| Sonra büyürsem? | Mevcut yükünüzün biraz üstünde bir set seçin |
| Küçük saha nerede kalır? | Genelde 80–200 kW yedek |

## Dürüst uyarı

İşletmeniz hızla büyüyorsa veya grubu günde birçok saat çalıştıracaksanız, önceden planlayın — büyültün ve verime bakın. Küçük bir iş sahasında sıradan yedek servis için, sağlam ve ekonomik 200 kW sessiz set ölçülü, düşük riskli bir satın almadır.

## Neye güç verdiğinizi söyleyin

Bize zorunlu olanları ve motorların listesini gönderin. Jeneratörü gerçek yükünüze göre boyutlandıracağız — yuvarlak bir rakama göre değil — ve size bütçeleyebileceğiniz bir fiyat vereceğiz.
''',
'th': '''![ชุดเครื่องกำเนิดดีเซลคงทนเสียง 200kW ในเปลือก](/images/blog/yuchai-200kw-silent.jpg)

คุณดำเนินการโรงงานเล็ก เวิร์กชอป หรือฟาร์ม คุณรู้ว่าต้องการไฟสำรอง แต่ตัวเลขเดียวที่ไม่มีใครจะให้คุณตรงๆ: **มันต้องใหญ่แค่ไหนกันแน่?**

ซื้อใหญ่เกินไป คุณจ่ายเกิน ซื้อเล็กเกินไป มันดับทันทีที่มอเตอร์ตัวหนึ่งสตาร์ท มาเก็บให้ง่ายๆ กัน

## สองตัวเลขที่ต้องคำนวณ

ลืมการคำนวณซับซ้อนๆ ไป เริ่มจากสองสิ่ง:

1. **อะไรที่ต้องทำงานต่อ**เมื่อไฟดับ? (ไม่ใช่ทุกอย่าง — แค่ของจำเป็น)
2. **อะไรในนั้นเป็นมอเตอร์หรือปั๊ม**ที่ดึงกระแสสตาร์ทขนาดใหญ่ตอนเริ่ม?

รายการพวกนั้น และคุณมีใจกลางของปัญหาการกำหนดขนาด

## เหตุใด "บวกมันทั้งหมด" จึงไม่พอ

บวกกำลังวิ่งเข้าใกล้แล้ว แต่กระแสสตาร์ทของมอเตอร์คือกับดัก เมื่อคอมเพรสเซอร์หรือปั๊มสตาร์ท มันดึงกำลังปกติหลายเท่าในพริบตา เครื่องกำเนิดที่กำหนดขนาดจากยอดวิ่งอย่างเดียวจะกระตุกตอนสตาร์ทครั้งแรก — ตรงเวลาที่คุณต้องการมันมากที่สุด

นี่คือเหตุผลที่ผู้ซื้อที่มีประสบการณ์จะขยายขนาดเล็กน้อยสำหรับการสตาร์ทมอเตอร์ หรือให้เราดูรายการโหลดให้

## กฎลูกทุ่งสำหรับไซต์ขนาดเล็ก

หลังจากโปรเจกต์สองสามงาน คนก็ตั้งหลักที่คู่มือง่ายๆ:

- รันเครื่องกำเนิดที่ประมาณ **70–80% ของกำลังเรตติ้ง** ในการใช้งานปกติ
- เวิร์กชอปเล็ก ฟาร์ม หรือกลุ่มร้านค้า มักลงที่ประมาณ **100–250 kVA** — ซึ่งก็คือชุด **80–200 kW** โดยประมาณ
- ถ้าคุณอยู่ใกล้ขอบบนของช่วงนั้น ชุดคงทนเสียง **200 kW (250 kVA)** เป็นตัวเลือกที่ชาญฉลาดและประหยัด

## คำถามเรื่องขนาดของคุณ ตอบแล้ว

| คำถามของคุณ | คำตอบที่ใช้ได้จริง |
|---|---|
| ผมเริ่มยังไง? | รายการของจำเป็น + มอเตอร์ที่สตาร์ทด้วยกระแสสูง |
| ใหญ่กว่าปลอดภัยกว่าไหม? | ไม่ — ขนาดใหญ่เกินไปเผาผลาญน้ำมันและสึกหรอแปลกๆ |
| แล้วถ้าฉันโตขึ้นทีหลัง? | เลือกชุดที่สูงกว่าโหลดปัจจุบันเล็กน้อย |
| ไซต์เล็กลงที่ไหนคร่าวๆ? | มัก 80–200 kW สำรอง |

## ข้อควรระวังที่ซื่อสัตย์

ถ้าธุรกิจของคุณเติบโตเร็ว หรือคุณจะรันชุดหลายชั่วโมงต่อวัน วางแผนล่วงหน้า — ขยายขนาดและดูประสิทธิภาพ สำหรับงานสำรองธรรมดาที่ไซต์งานขนาดเล็ก ชุดคงทนเสียงที่แข็งแรงและประหยัด 200 kW คือการซื้อที่วัดผลได้และมีความเสี่ยงต่ำ

## บอกเราว่าคุณจ่ายไฟอะไร

ส่งรายการของจำเป็นและมอเตอร์มาให้เรา เราจะกำหนดขนาดเครื่องกำเนิดตามโหลดจริงของคุณ — ไม่ใช่ตัวเลขกลม — และให้ราคาที่คุณสามารถวางงบประมาณได้
''',
'vi': '''![Bộ máy phát diesel chống ồn 200kW trong canopy](/images/blog/yuchai-200kw-silent.jpg)

Bạn điều hành một nhà máy nhỏ, một xưởng hoặc một trang trại. Bạn biết mình cần điện dự phòng. Nhưng con số duy nhất không ai nói thẳng với bạn: **nó thực sự cần cỡ nào?**

Mua quá lớn thì bạn tiêu thừa. Mua quá nhỏ thì nó tắt ngay khi một động cơ bật lên. Hãy giữ cho đơn giản.

## Hai con số cần tính

Quên các phép tính phức tạp đi. Bắt đầu với hai thứ:

1. **Cái gì phải tiếp tục chạy** khi mất điện? (Không phải tất cả — chỉ cái thiết yếu.)
2. **Cái nào trong số đó là động cơ hoặc bơm** sẽ hút một dòng khởi động lớn khi chúng khởi động?

Liệt kê những thứ đó, và bạn đã có cốt lõi của bài toán kích thước.

## Tại sao "cộng tất cả" là không đủ

Cộng công suất chạy được gần, nhưng dòng khởi động của động cơ mới là cái bẫy. Khi một máy nén hoặc bơm khởi động, nó kéo công suất gấp nhiều lần bình thường trong khoảnh khắc. Một máy phát được kích thước chỉ trên tổng chạy sẽ nghẹn ở lần khởi động đầu tiên — đúng lúc bạn cần nó nhất.

Đây là lý do người mua kinh nghiệm hoặc hơi tăng kích thước cho khởi động động cơ, hoặc để chúng tôi xem danh sách tải cho họ.

## Quy tắc kinh nghiệm cho địa điểm nhỏ

Sau vài dự án, mọi người dừng ở các hướng dẫn đơn giản:

- Chạy máy phát ở khoảng **70–80% công suất định mức** trong sử dụng bình thường.
- Một xưởng nhỏ, trang trại hoặc cụm cửa hàng thường rơi vào khoảng **100–250 kVA** — tức là khoảng bộ **80–200 kW**.
- Nếu bạn ở gần đầu trên của dải đó, một bộ yên tĩnh **200 kW (250 kVA)** là lựa chọn hợp lý và tiết kiệm.

## Câu hỏi kích thước của bạn, đã trả lời

| Câu hỏi của bạn | Câu trả lời thực tế |
|---|---|
| Tôi bắt đầu thế nào? | Liệt kê thiết yếu + động cơ khởi động bằng dòng lớn |
| Lớn hơn có an toàn hơn? | Không — quá khổ lãng phí nhiên liệu và mòn bất thường |
| Nếu sau này tôi mở rộng? | Chọn bộ cao hơn tải hiện tại một chút |
| Địa điểm nhỏ thường ở đâu? | Thường 80–200 kW dự phòng |

## Lưu ý thành thật

Nếu doanh nghiệp bạn đang phát triển nhanh, hoặc bạn sẽ chạy bộ nhiều giờ mỗi ngày, hãy lên kế hoạch trước — tăng kích thước và xem hiệu quả. Với nhiệm vụ dự phòng thông thường tại một địa điểm làm việc nhỏ, một bộ yên tĩnh 200 kW chắc chắn và kinh tế là một lựa chọn đã cân nhắc, rủi ro thấp.

## Cho chúng tôi biết bạn cấp điện gì

Gửi chúng tôi danh sách thiết yếu và động cơ. Chúng tôi sẽ kích thước máy phát theo tải thực của bạn — không phải một con số tròn — và cho bạn một mức giá để lập ngân sách.
''',
'id': '''![Grup genset diesel silent 200kW di dalam kanopi](/images/blog/yuchai-200kw-silent.jpg)

Anda menjalankan pabrik kecil, bengkel, atau peternakan. Anda tahu butuh daya cadangan. Tapi satu angka yang tidak ada yang memberitahu Anda secara langsung: **sebenarnya perlu sebesar apa?**

Beli terlalu besar, dan Anda overspend. Beli terlalu kecil, dan mati saat sebuah motor dinyalakan. Mari kita sederhanakan.

## Dua angka yang harus dihitung

Lupakan perhitungan rumit. Mulai dengan dua hal:

1. **Apa yang harus tetap jalan** saat listrik padam? (Bukan semuanya — hanya yang penting.)
2. **Yang mana dari hal-hal itu motor atau pompa** yang menarik lonjakan besar saat dinyalakan?

Daftarkan itu, dan Anda punya inti masalah ukuran.

## Mengapa "jumlahkan semuanya" tidak cukup

Menjumlahkan daya jalan membuat Anda dekat, tapi lonjakan motor adalah jebakan. Saat kompresor atau pompa menyala, ia menarik beberapa kali daya normalnya untuk sesaat. Genset yang diukur hanya berdasarkan total jalan akan tersendat pada start pertama itu — justru saat Anda paling membutuhkannya.

Inilah mengapa pembeli berpengalaman sedikit oversize untuk start motor, atau membiarkan kami melihat daftar beban untuk mereka.

## Aturan praktis untuk lokasi kecil

Setelah beberapa proyek, orang menetap pada panduan sederhana:

- Jalankan genset di sekitar **70–80% daya nominalnya** dalam penggunaan normal.
- Bengkel kecil, peternakan, atau gugusan toko sering jatuh di sekitar **100–250 kVA** — kira-kira setara grup **80–200 kW**.
- Jika Anda dekat ujung atas rentang itu, grup silent **200 kW (250 kVA)** adalah pilihan yang masuk akal dan ekonomis.

## Pertanyaan ukuran Anda, terjawab

| Pertanyaan Anda | Jawaban praktis |
|---|---|
| Saya mulai dari mana? | Daftar yang penting + motor yang start dengan lonjakan |
| Lebih besar lebih aman? | Tidak — oversize buang bahan bakar dan aus aneh |
| Bagaimana jika nanti berkembang? | Pilih grup sedikit di atas beban saat ini |
| Kira-kira lokasi kecil jatuh di mana? | Sering 80–200 kW standby |

## Catatan jujur

Jika bisnis Anda berkembang pesat, atau Anda akan menjalankan grup banyak jam sehari, rencanakan dari awal — naik ukuran dan lihat efisiensi. Untuk tugas cadangan biasa di lokasi kerja kecil, grup silent 200 kW yang kokoh dan ekonomis adalah pembelian terukur dan berisiko rendah.

## Beri tahu kami apa yang Anda aliri

Kirimkan daftar yang penting dan motor. Kami akan mengukur genset sesuai beban nyata Anda — bukan angka bulat — dan memberi Anda harga yang bisa dianggarkan.
''',
}
eng = open(f'content/blog/{slug}.md', encoding='utf-8').read()
parts = eng.split('---', 2)
fm = y.safe_load(parts[1])
date = fm.get('date', '2026-10-12')
for loc, body in bodies.items():
    d = f'content/blog/{loc}'
    outpath = f'{d}/{slug}.md'
    existing = open(outpath, encoding='utf-8').read()
    e_parts = existing.split('---', 2)
    e_fm = y.safe_load(e_parts[1])
    title = e_fm.get('title', '')
    excerpt = e_fm.get('excerpt', '')
    fm_str = y.dump({'title': title, 'date': str(date), 'excerpt': excerpt},
                    allow_unicode=True, default_flow_style=False, width=9999)
    content = f'---\n{fm_str}---\n\n{body}\n'
    open(outpath, 'w', encoding='utf-8').write(content)
    print(f'Wrote {loc}/{slug}.md')
print('Done!')
