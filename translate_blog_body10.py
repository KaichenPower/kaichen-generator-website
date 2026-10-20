# -*- coding: utf-8 -*-
import yaml as y
slug = 'scania-400kw-silent-generator'
bodies = {
'ru': '''![Генераторная установка 400 кВт в акустическом кожухе](/images/blog/scania-400kw-silent.jpg)

Почти все выбирают генератор по цене покупки. Почти все забывают задать вопрос, который на самом деле определяет стоимость: **сколько топлива эта штука будет жечь, и как часто она будет работать?**

Давайте посчитаем вместе, потому что ответ меняет то, какой двигатель вам стоит купить.

## Начните с одного числа: сколько часов она будет работать?

Прежде чем сравнивать двигатели, будьте честны в этом:

- Установка, работающая **раз в год** во время шторма — топливо почти не важно. Покупайте самую дешёвую, которая соответствует.
- Установка, работающая **сотни часов в год** на слабой сети — топливо это ваш реальный бюджет, и эффективность имеет большое значение.

Та же мощность, совершенно другое решение о покупке.

## Сделайте грубый расчёт

Допустим, вам нужно 400 кВт, и установка жжёт около 80 литров в час при типичной нагрузке. За, скажем, 800 часов в год — это десятки тысяч литров. Несколько процентов лучшего расхода топлива — невидимые в брошюре — это серьёзная экономия каждый год, и она накапливается за десятилетие.

Именно поэтому эффективный двигатель с сильным крутящим моментом, такой как блок Scania, оправдывает себя: он сохраняет экономичность даже при частичной нагрузке, а именно там резервные установки проводят большую часть времени.

## Ловушки, в которые попадают покупатели

- **Переразмер** — покупка гораздо большего двигателя, чем вам нужно. Большой двигатель, работающий на холостом ходу под малой нагрузкой, жжёт топливо впустую и изнашивается странным образом.
- **Игнорирование частичной нагрузки** — эффективность при 100% мощности приятна, но вы редко работаете на 100%. Спросите об эффективности при половинной нагрузке.
- **Чтение только цены на ценнике** — дешёвый двигатель выглядит отлично до первого счёта за топливо.

## Ваши вопросы о стоимости, ответы

| Ваш вопрос | Практический ответ |
|---|---|
| Как оценить расход топлива? | Грубо литры/час × ваши годовые часы работы |
| Когда окупается эффективность? | Когда установка работает много часов в год |
| Что покрывает ~400 кВт? | Большие коммерческие здания, больницы, заводы |
| Больший двигатель всегда дороже в эксплуатации? | Часто да — подбирайте под вашу реальную нагрузку |

## Простое правило

Если ваш генератор много работает, покупайте эффективный двигатель. Если он почти не работает, не переплачивайте за эффективность, которую вы не будете использовать. В любом случае, подбирайте размер под вашу реальную нагрузку — не под круглое число.

## Отправьте нам ваши часы работы

Скажите нам, сколько часов в год установка, вероятно, будет работать, и вашу среднюю нагрузку. Мы оценим расход топлива для вас и покажем точку безубыточности, чтобы вы выбирали по цифрам, а не по догадкам.
''',
'es': '''![Grupo electrógeno diesel de 400kW en canopy acústico](/images/blog/scania-400kw-silent.jpg)

Casi todo el mundo compra un generador por el precio de compra. Casi todo el mundo olvida preguntar la pregunta que realmente decide el coste: **¿cuánto combustible va a quemar esta cosa, y con qué frecuencia va a funcionar?**

Vamos a calcularlo juntos, porque la respuesta cambia qué motor deberías comprar.

## Empieza con un número: ¿cuántas horas va a funcionar?

Antes de comparar motores, sé honesto con esto:

- Un grupo que funciona **una vez al año** durante una tormenta — el combustible apenas importa. Compra el más barato que cumpla.
- Un grupo que funciona **cientos de horas al año** en una red débil — el combustible es tu presupuesto real, y la eficiencia importa mucho.

Misma potencia, decisión de compra completamente diferente.

## Haz las matemáticas aproximadas

Digamos que necesitas 400 kW y el grupo quema unos 80 litros por hora a carga típica. En, digamos, 800 horas al año, eso son decenas de miles de litros. Unos pocos puntos porcentuales de mejor consumo — invisibles en el folleto — son un ahorro serio cada año, y se acumulan durante una década.

Por eso un motor eficiente y de par fuerte como el bloque Scania se gana su lugar: mantiene su economía de combustible incluso a carga parcial, que es donde los grupos standby pasan realmente la mayor parte del tiempo.

## Las trampas en las que caen los compradores

- **Sobredimensionar** — comprar un motor mucho más grande de lo que necesitas. Un motor grande en ralentí con poca carga quema combustible para nada y se desgasta de forma extraña.
- **Ignorar la carga parcial** — la eficiencia al 100% de potencia es agradable, pero rara vez corres al 100%. Pregunta por la eficiencia a media carga.
- **Solo leer el precio de etiqueta** — el motor barato se ve genial hasta la primera factura de combustible.

## Tus preguntas de coste, respondidas

| Tu pregunta | Respuesta práctica |
|---|---|
| ¿Cómo estimo el consumo? | Aproximadamente litros/hora × tus horas anuales |
| ¿Cuándo se amortiza la eficiencia? | Cuando el grupo corre muchas horas al año |
| ¿Qué cubre ~400 kW? | Grandes edificios comerciales, hospitales, plantas |
| ¿Un motor más grande siempre cuesta más en marcha? | A menudo sí — dimensiona según tu carga real |

## La regla simple

Si tu generador funciona mucho, compra el motor eficiente. Si apenas funciona, no pagues de más por una eficiencia que no usarás. De cualquier forma, dimensiona según tu carga real — no un número redondo.

## Envíanos tus horas de funcionamiento

Dinos cuántas horas al año es probable que funcione el grupo y tu carga media. Estimaremos el consumo de combustible y te mostraremos el punto de equilibrio, para que elijas con números en lugar de suposiciones.
''',
'fr': '''![Groupe électrogène diesel de 400 kW en capot acoustique](/images/blog/scania-400kw-silent.jpg)

Presque tout le monde achète un groupe électrogène au prix d'achat. Presque tout le monde oublie de poser la question qui décide réellement du coût : **combien de carburant cette chose va-t-elle brûler, et à quelle fréquence va-t-elle tourner ?**

Calculons-le ensemble, car la réponse change quel moteur vous devriez acheter.

## Commencez par un chiffre : combien d'heures va-t-il tourner ?

Avant de comparer les moteurs, soyez honnête là-dessus :

- Un groupe qui tourne **une fois par an** pendant une tempête — le carburant importe peu. Achetez le moins cher qui convienne.
- Un groupe qui tourne **des centaines d'heures par an** sur un réseau faible — le carburant est votre vrai budget, et l'efficacité compte beaucoup.

Même puissance, décision d'achat complètement différente.

## Faites le calcul approximatif

Disons que vous avez besoin de 400 kW et que le groupe brûle environ 80 litres par heure à charge typique. Sur, disons, 800 heures par an, cela fait des dizaines de milliers de litres. Quelques points de pourcentage de meilleure consommation — invisibles sur la brochure — sont une économie sérieuse chaque année, et cela se cumule sur une décennie.

C'est pourquoi un moteur efficace et coupleux comme un bloc Scania gagne sa place : il garde son économie de carburant même à charge partielle, c'est là que les groupes secours passent réellement la plupart de leur temps.

## Les pièges dans lesquels tombent les acheteurs

- **Surdimensionnement** — acheter un moteur bien plus gros que nécessaire. Un gros moteur qui tourne au ralenti sous charge légère brûle du carburant pour rien et s'use bizarrement.
- **Ignorer la charge partielle** — l'efficacité à 100 % de puissance est agréable, mais vous tournez rarement à 100 %. Demandez l'efficacité à mi-charge.
- **Lire seulement le prix affiché** — le moteur bon marché a l'air génial jusqu'à la première facture de carburant.

## Vos questions de coût, réponses

| Votre question | Réponse pratique |
|---|---|
| Comment estimer la consommation ? | Approximativement litres/heure × vos heures annuelles |
| Quand l'efficacité se rentabilise-t-elle ? | Quand le groupe tourne beaucoup d'heures par an |
| Que couvre ~400 kW ? | Grands bâtiments commerciaux, hôpitaux, usines |
| Un moteur plus gros coûte-t-il toujours plus cher à tourner ? | Souvent oui — dimensionnez selon votre vraie charge |

## La règle simple

Si votre générateur tourne beaucoup, achetez le moteur efficace. S'il tourne à peine, ne payez pas plus pour une efficacité que vous n'utiliserez pas. Dans les deux cas, dimensionnez selon votre charge réelle — pas un chiffre rond.

## Envoyez-nous vos heures de fonctionnement

Dites-nous combien d'heures par an le groupe est susceptible de tourner et votre charge moyenne. Nous estimerons la consommation de carburant et vous montrerons le point d'équilibre, pour que vous choisissiez avec des chiffres plutôt qu'à l'aveugle.
''',
'de': '''![400 kW schallgeschütztes Dieselaggregat in Akustikkabine](/images/blog/scania-400kw-silent.jpg)

Fast jeder kauft ein Aggregat nach dem Kaufpreis. Fast jeder vergisst, die Frage zu stellen, die tatsächlich über die Kosten entscheidet: **Wie viel Kraftstoff wird dieses Ding verbrauchen, und wie oft wird es laufen?**

Rechnen wir es gemeinsam durch, denn die Antwort ändert, welchen Motor Sie kaufen sollten.

## Beginnen Sie mit einer Zahl: wie viele Stunden wird es laufen?

Bevor Sie Motoren vergleichen, seien Sie damit ehrlich:

- Ein Aggregat, das **einmal pro Jahr** während eines Sturms läuft — Kraftstoff spielt kaum eine Rolle. Kaufen Sie das günstigste, das passt.
- Ein Aggregat, das **Hunderte Stunden pro Jahr** auf einem schwachen Netz läuft — Kraftstoff ist Ihr wahres Budget, und Effizienz zählt viel.

Gleiche Leistung, völlig andere Kaufentscheidung.

## Machen Sie die grobe Rechnung

Nehmen wir an, Sie brauchen 400 kW und das Aggregat verbraucht rund 80 Liter pro Stunde bei typischer Last. Über, sagen wir, 800 Stunden pro Jahr sind das Zehntausende Liter. Ein paar Prozentpunkte weniger Verbrauch — auf dem Prospekt unsichtbar — sind jedes Jahr eine ernsthafte Ersparnis, und sie summieren sich über ein Jahrzehnt.

Deshalb verdient sich ein effizientes, drehmomentstarker Motor wie ein Scania-Block seinen Platz: Er hält seinen Kraftstoffverbrauch auch bei Teillast, wo Notaggregate tatsächlich die meiste Zeit verbringen.

## Die Fallen, in die Käufer tappen

- **Überdimensionierung** — einen viel größeren Motor kaufen als nötig. Ein großer Motor, der leicht belastet im Leerlauf läuft, verbraucht Kraftstoff umsonst und verschleißt seltsam.
- **Teillast ignorieren** — Effizienz bei 100 % Leistung ist schön, aber Sie laufen selten bei 100 %. Fragen Sie nach der Effizienz bei Halblast.
- **Nur den Schildpreis lesen** — der billige Motor sieht großartig aus bis zur ersten Tankrechnung.

## Ihre Kostenfragen, beantwortet

| Ihre Frage | Praktische Antwort |
|---|---| | Wie schätze ich den Verbrauch? | Grob Liter/Stunde × Ihre Jahreslaufstunden |
| Wann zahlt sich Effizienz aus? | Wenn das Aggregat viele Stunden pro Jahr läuft |
| Was deckt ~400 kW ab? | Große Gewerbebauten, Krankenhäuser, Werke |
| Größerer Motor immer teurer im Betrieb? | Oft ja — dimensionieren Sie nach Ihrer echten Last |

## Die einfache Regel

Wenn Ihr Generator viel läuft, kaufen Sie den effizienten Motor. Wenn er kaum läuft, zahlen Sie nicht mehr für eine Effizienz, die Sie nicht nutzen werden. So oder so, dimensionieren Sie nach Ihrer tatsächlichen Last — nicht nach einer runden Zahl.

## Schicken Sie uns Ihre Laufstunden

Sagen Sie uns, wie viele Stunden pro Jahr das Aggregat voraussichtlich laufen wird und Ihre Durchschnittslast. Wir schätzen den Kraftstoffverbrauch für Sie und zeigen Ihnen den Break-even, damit Sie mit Zahlen statt mit Vermutungen wählen.
''',
'pt': '''![Grupo gerador diesel de 400kW em canopy acústico](/images/blog/scania-400kw-silent.jpg)

Quase todo mundo compra um gerador pelo preço de compra. Quase todo mundo esquece de fazer a pergunta que realmente decide o custo: **quanto combustível esse negócio vai queimar, e com que frequência vai rodar?**

Vamos calcular juntos, porque a resposta muda qual motor você deve comprar.

## Comece com um número: quantas horas vai rodar?

Antes de comparar motores, seja honesto sobre isso:

- Um grupo que roda **uma vez por ano** durante uma tempestade — combustível quase não importa. Compre o mais barato que sirva.
- Um grupo que roda **centenas de horas por ano** numa rede fraca — combustível é seu orçamento real, e eficiência importa muito.

Mesma potência, decisão de compra completamente diferente.

## Faça a conta aproximada

Digamos que você precisa de 400 kW e o grupo queima cerca de 80 litros por hora em carga típica. Ao longo de, digamos, 800 horas por ano, isso são dezenas de milhares de litros. Alguns pontos percentuais de melhor consumo — invisíveis na brochure — são uma economia séria a cada ano, e se acumulam ao longo de uma década.

É por isso que um motor eficiente e de torque forte como um bloco Scania se paga: ele mantém sua economia de combustível mesmo em carga parcial, que é onde grupos standby realmente passam a maior parte do tempo.

## As armadilhas em que os compradores caem

- **Sobredimensionar** — comprar um motor muito maior do que você precisa. Um motor grande em marcha lenta subcarregado queima combustível à toa e desgasta de forma estranha.
- **Ignorar carga parcial** — eficiência a 100% de potência é legal, mas você raramente roda a 100%. Pergunte sobre eficiência em meia carga.
- **Só ler o preço de etiqueta** — o motor barato parece ótimo até a primeira conta de combustível.

## Suas perguntas de custo, respondidas

| Sua pergunta | Resposta prática |
|---|---|
| Como estimo o consumo? | Aproximadamente litros/hora × suas horas anuais |
| Quando a eficiência se paga? | Quando o grupo roda muitas horas por ano |
| O que ~400 kW cobre? | Grandes prédios comerciais, hospitais, fábricas |
| Motor maior sempre custa mais pra rodar? | Frequentemente sim — dimensione pela sua carga real |

## A regra simples

Se seu gerador roda muito, compre o motor eficiente. Se mal roda, não pague mais por uma eficiência que você não vai usar. De qualquer forma, dimensione pela sua carga real — não por um número redondo.

## Envie-nos suas horas de funcionamento

Diga-nos quantas horas por ano o grupo provavelmente vai rodar e sua carga média. Estimaremos o consumo de combustível para você e mostraremos o ponto de equilíbrio, para você escolher com números em vez de suposições.
''',
'ar': '''![مجموعة مولد ديزل 400kW في هيكل عازل للصوت](/images/blog/scania-400kw-silent.jpg)

يتسوق الجميع تقريباً لشراء مولد حسب سعر الشراء. ينسى الجميع تقريباً طرح السؤال الذي يحدد التكلفة فعلياً: **كم من الوقود ستحرق هذه الآلة، وكم مرة ستعمل؟**

دعنا نحسبها معاً، لأن الإجابة تغير المحرك الذي يجب أن تشتريه.

## ابدأ برقم واحد: كم ساعة ستعمل؟

قبل أن تقارن المحركات، كن صادقاً بشأن هذا:

- مجموعة تعمل **مرة في السنة** أثناء العاصفة — الوقود لا يهم تقريباً. اشترِ الأرخص الذي يناسب.
- مجموعة تعمل **مئات الساعات في السنة** على شبكة ضعيفة — الوقود هو ميزانيتك الحقيقية، والكفاءة تهم كثيراً.

نفس الطاقة، قرار شراء مختلف تماماً.

## قم بالحساب التقريبي

لنفترض أنك تحتاج 400 kW والمجموعة تحرق حوالي 80 لتراً في الساعة بحمل نموذجي. على مدى، لنقل، 800 ساعة في السنة، هذا عشرات الآلاف من اللترات. بضع نقاط مئوية من تحسين استهلاك الوقود — غير مرئية في الكتيب — هي توفير جاد كل عام، وتتراكم على مدى عقد.

لهذا السبب فإن المحرك الفعال ذو العزم القوي مثل كتلة Scania يكسب قيمته: يحافظ على اقتصاد الوقود حتى عند الحمل الجزئي، وهو المكان الذي تقضي فيه مجموعات الاحتياط معظم وقتها فعلياً.

## الفخاخ التي يقع فيها المشترون

- **الحجم الزائد** — شراء محرك أكبر بكثير مما تحتاج. المحرك الكبير الذي يعمل على خمول بحمل خفيف يحرق الوقود بلا فائدة ويتآكل بشكل غريب.
- **تجاهل الحمل الجزئي** — الكفاءة عند 100% طاقة أمر لطيف، ولكنك نادراً ما تعمل عند 100%. اسأل عن الكفاءة عند نصف الحمل.
- **قراءة سعر اللافتة فقط** — المحرك الرخيص يبدو رائعاً حتى فاتورة الوقود الأولى.

## أسئلتك حول التكلفة، أجابت

| سؤالك | الجواب العملي |
|---|---|
| كيف أقدر استهلاك الوقود؟ | تقريباً لتر/ساعة × ساعات العمل السنوية |
| متى تؤتي الكفاءة ثمارها؟ | عندما تعمل المجموعة ساعات طويلة في السنة |
| ماذا يغطي ~400 kW؟ | المباني التجارية الكبيرة، المستشفيات، المصانع |
| المحرك الأكبر دائماً أغلى تشغيلاً؟ | غالباً نعم — حدد الحجم حسب حملك الحقيقي |

## القاعدة البسيطة

إذا كان مولدك يعمل كثيراً، اشترِ المحرك الفعال. إذا كان بالكاد يعمل، لا تدفع أكثر مقابل كفاءة لن تستخدمها. في كلتا الحالتين، حدد الحجم حسب حملك الفعلي — ليس رقماً مستديراً.

## أرسل لنا ساعات التشغيل

أخبرنا كم ساعة في السنة من المحتمل أن تعمل فيها المجموعة ومتوسط حملك. سنقدر استهلاك الوقود لك ونريك نقطة التعادل، لتختار بالأرقام بدلاً من التخمين.
''',
'tr': '''![Akustik kabinde 400kW sessiz dizel jeneratör seti](/images/blog/scania-400kw-silent.jpg)

Neredeyse herkes jeneratörü satın alma fiyatına göre alışveriş yapar. Neredeyse herkes asıl maliyeti belirleyen soruyu sormayı unutuyor: **Bu şey ne kadar yakıt yakacak ve ne sıklıkla çalışacak?**

Hadi birlikte hesaplayalım, çünkü cevap hangi motoru almanız gerektiğini değiştiriyor.

## Bir sayıyla başlayın: kaç saat çalışacak?

Motorları karşılaştırmadan önce, bu konuda dürüst olun:

- Yılda **bir kez** fırtına sırasında çalışan bir grup — yakıt neredeyse önemli değil. Ucuz olanı alın.
- Zayıf şebekede yılda **yüzlerce saat** çalışan bir grup — yakıt sizin gerçek bütçeniz ve verimlilik çok önemli.

Aynı güç, tamamen farklı satın alma kararı.

## Kaba hesabı yapın

Diyelim ki 400 kW'a ihtiyacınız var ve grup tipik yükte saatte yaklaşık 80 litre yakıyor. Yılda 800 saat üzerinde, bu on binlerce litre. Broşürde görünmeyen birkaç puan daha iyi yakıt tüketimi, her yıl ciddi bir tasarruftur ve on yıl boyunca birikir.

İşte bu yüzden Scania bloğu gibi verimli, yüksek torklu bir motor kendini hak ediyor: kısmi yükte bile yakıt ekonomisini korur, ki yedek gruplar gerçekte zamanlarının çoğunu orada geçirir.

## Alıcıların düştüğü tuzaklar

- **Aşırı boyutlandırma** — ihtiyacınız olandan çok daha büyük bir motor almak. Boştaki büyük motor boşa yakıt yakar ve tuhaf şekilde aşınır.
- **Kısmi yükü görmezden gelmek** — %100 güçte verimlilik güzel, ama nadiren %100'de çalışırsınız. Yarı yükte verimliliği sorun.
- **Sadece etiket fiyatını okumak** — ucuz motor, ilk yakıt faturasına kadar harika görünür.

## Maliyet sorularınız, cevaplandı

| Sorunuz | Pratik cevap |
|---|---|
| Yakıt kullanımını nasıl tahmin ederim? | Kabaca litre/saat × yıllık çalışma saatleriniz |
| Verimlilik ne zaman kendini amorti eder? | Grup yılda çok saat çalıştığında |
| ~400 kW neleri kapsar? | Büyük ticari binalar, hastaneler, tesisler |
| Daha büyük motor her zaman daha mı pahalı çalışır? | Genelde evet — gerçek yükünüze göre boyutlandırın |

## Basit kural

Jeneratörünüz çok çalışıyorsa, verimli motoru alın. Neredeyse hiç çalışmıyorsa, kullanmayacağınız verimlilik için fazla ödeme yapmayın. Her iki durumda da, gerçek yükünüze göre boyutlandırın — yuvarlak bir sayıya göre değil.

## Bize çalışma saatlerinizi gönderin

Grupta yılda kaç saat çalışması beklendiğini ve ortalama yükünüzü söyleyin. Yakıt kullanımını sizin için tahmin edeceğiz ve başa baş noktasını göstereceğiz, böylece tahminlerle değil sayılarla seçersiniz.
''',
'th': '''![ชุดเครื่องกำเนิดดีเซล 400kW ในเปลือกกันเสียง](/images/blog/scania-400kw-silent.jpg)

เกือบทุกคนเลือกซื้อเครื่องกำเนิดตามราคาซื้อ เกือบทุกคนลืมถามคำถามที่ตัดสินต้นทุนจริงๆ: **เครื่องนี้จะกินน้ำมันมากแค่ไหน และบ่อยแค่ไหนที่จะทำงาน?**

มาคำนวณด้วยกัน เพราะคำตอบเปลี่ยนว่าคุณควรซื้อเครื่องยนต์แบบไหน

## เริ่มที่ตัวเลขหนึ่ง: มันจะทำงานกี่ชั่วโมง

ก่อนเปรียบเทียบเครื่องยนต์ จริงใจเกี่ยวกับเรื่องนี้:

- ชุดที่ทำงาน**ปีละครั้ง**ระหว่างพายุ — น้ำมันแทบไม่สำคัญ ซื้อที่ถูกที่สุดที่ตรงสเปก
- ชุดที่ทำงาน**หลายร้อยชั่วโมงต่อปี**บนกริดอ่อน — น้ำมันคืองบประมาณจริงของคุณ และประสิทธิภาพสำคัญมาก

กำลังเท่ากัน การตัดสินใจซื้อต่างกันอย่างสิ้นเชิง

## คำนวณคร่าวๆ

สมมติว่าคุณต้องการ 400 kW และชุดกินน้ำมันประมาณ 80 ลิตรต่อชั่วโมงที่โหลดปกติ ตลอดสมมติว่า 800 ชั่วโมงต่อปี นั่นคือหลายหมื่นลิตร การใช้น้ำมันที่ดีขึ้นไม่กี่เปอร์เซ็นต์ — มองไม่เห็นในโบรชัวร์ — คือการประหยัดที่จริงจังทุกปี และสะสมเป็นทศวรรษ

นี่คือเหตุผลที่เครื่องยนต์ที่ประหยัดและแรงบิดสูงอย่างบล็อก Scania คุ้มค่ามัน: มันรักษาประหยัดน้ำมันได้แม้โหลดบางส่วน ซึ่งเป็นที่ที่ชุดสำรองใช้เวลาส่วนใหญ่จริงๆ

## กับดักที่ผู้ซื้อตก

- **ขนาดใหญ่เกินไป** — ซื้อเครื่องยนต์ที่ใหญ่กว่าที่คุณต้องการมาก เครื่องยนต์ใหญ่ที่เดินเบาใต้โหลดต่ำกินน้ำมันเปล่าๆ และสึกหรอแปลกๆ
- **ไม่สนใจโหลดบางส่วน** — ประสิทธิภาพที่กำลัง 100% เป็นเรื่องดี แต่คุณไม่ค่อยรันที่ 100% ถามเรื่องประสิทธิภาพที่ครึ่งโหลด
- **อ่านแค่ราคาป้าย** — เครื่องยนต์ราคาถูกดูดีมากจนถึงบิลน้ำมันใบแรก

## คำถามต้นทุนของคุณ ตอบแล้ว

| คำถามของคุณ | คำตอบที่ใช้ได้จริง |
|---|---|
| ผมประเมินการใช้น้ำมันอย่างไร? | คร่าวๆ ลิตร/ชั่วโมง × ชั่วโมงทำงานต่อปี |
| ประสิทธิภาพคุ้มทุนเมื่อไหร่? | เมื่อชุดทำงานหลายชั่วโมงต่อปี |
| ~400 kW ครอบคลุมอะไรบ้าง? | อาคารพาณิชย์ขนาดใหญ่ โรงพยาบาล โรงงาน |
| เครื่องยนต์ใหญ่กว่าวิ่งแพงกว่าเสมอไหม? | มักจะใช่ — ขนาดตามโหลดจริงของคุณ |

## กฎง่ายๆ

ถ้าเครื่องกำเนิดของคุณทำงานเยอะ ซื้อเครื่องยนต์ที่ประหยัด ถ้ามันแทบไม่ทำงาน อย่าจ่ายเพิ่มสำหรับประสิทธิภาพที่คุณจะไม่ใช่ ไม่ว่ายังไง ขนาดตามโหลดจริงของคุณ — ไม่ใช่ตัวเลขกลมๆ

## ส่งชั่วโมงทำงานของคุณมาให้เรา

บอกเราว่าชุดน่าจะทำงานกี่ชั่วโมงต่อปีและโหลดเฉลี่ยของคุณ เราจะประมาณการใช้น้ำมันให้คุณและจุดคุ้มทุน เพื่อให้คุณเลือกด้วยตัวเลขแทนที่จะเดา
''',
'vi': '''![Bộ máy phát diesel 400kW trong canopy âm học](/images/blog/scania-400kw-silent.jpg)

Hầu hết mọi người chọn máy phát theo giá mua. Hầu hết mọi người quên hỏi câu hỏi thực sự quyết định chi phí: **máy này sẽ đốt bao nhiêu nhiên liệu, và nó sẽ chạy bao thường xuyên?**

Hãy cùng tính, vì câu trả lời thay đổi việc bạn nên mua động cơ nào.

## Bắt đầu với một con số: nó sẽ chạy bao nhiêu giờ?

Trước khi so sánh động cơ, hãy thành thật về điều này:

- Bộ máy chạy **mỗi năm một lần** trong một cơn bão — nhiên liệu gần như không quan trọng. Cái rẻ nhất phù hợp thì mua.
- Bộ máy chạy **hàng trăm giờ mỗi năm** trên lưới yếu — nhiên liệu là ngân sách thực sự của bạn, và hiệu quả rất quan trọng.

Cùng công suất, quyết định mua hoàn toàn khác.

## Làm phép tính thô

Giả sử bạn cần 400 kW và bộ đốt khoảng 80 lít một giờ ở tải thông thường. Qua, chẳng hạn, 800 giờ một năm, đó là hàng chục nghìn lít. Vài điểm phần trăm tiết kiệm nhiên liệu tốt hơn — vô hình trên brochure — là khoản tiết kiệm nghiêm trọng mỗi năm, và nó tích lũy qua một thập kỷ.

Đây là lý do tại sao một động cơ hiệu quả, mô-men xoắn mạnh như khối Scania xứng đáng với đồng tiền: nó giữ được tiết kiệm nhiên liệu ngay cả ở tải một phần, nơi các bộ máy dự phòng thực sự dành phần lớn thời gian.

## Những cạm bẫy người mua rơi vào

- **Quá khổ** — mua động cơ lớn hơn nhiều so với nhu cầu. Một động cơ lớn chạy non tải đốt nhiên liệu vô ích và mòn bất thường.
- **Bỏ qua tải một phần** — hiệu quả ở 100% công suất thì hay, nhưng bạn hiếm khi chạy ở 100%. Hỏi về hiệu quả ở nửa tải.
- **Chỉ đọc giá niêm yết** — động cơ rẻ trông tuyệt vời cho đến hóa đơn nhiên liệu đầu tiên.

## Câu hỏi chi phí của bạn, đã trả lời

| Câu hỏi của bạn | Câu trả lời thực tế |
|---|---| | Tôi ước tính tiêu thụ nhiên liệu thế nào? | Khoảng lít/giờ × số giờ chạy hàng năm của bạn |
| Hiệu quả hoàn vốn khi nào? | Khi bộ chạy nhiều giờ mỗi năm |
| ~400 kW phủ gì? | Tòa nhà thương mại lớn, bệnh viện, nhà máy |
| Động cơ lớn hơn luôn chạy đắt hơn? | Thường có — kích thước theo tải thực của bạn |

## Quy tắc đơn giản

Nếu máy phát của bạn chạy nhiều, hãy mua động cơ hiệu quả. Nếu nó hầu như không chạy, đừng trả thêm cho hiệu quả mà bạn sẽ không dùng. Dù thế nào, kích thước theo tải thực của bạn — không phải một con số tròn.

## Gửi cho chúng tôi giờ chạy của bạn

Hãy cho chúng tôi biết bao nhiêu giờ một năm bộ này có khả năng chạy và tải trung bình của bạn. Chúng tôi sẽ ước tính tiêu thụ nhiên liệu và cho bạn xem điểm hòa vốn, để bạn chọn bằng con số thay vì đoán.
''',
'id': '''![Grup genset diesel 400kW dalam kanopi akustik](/images/blog/scania-400kw-silent.jpg)

Hampir semua orang belanja genset dari harga pembelian. Hampir semua orang lupa menanyakan pertanyaan yang sebenarnya menentukan biaya: **berapa banyak bahan bakar alat ini akan terbakar, dan seberapa sering ia akan berjalan?**

Mari kita hitung bersama, karena jawabannya mengubah mesin mana yang harus Anda beli.

## Mulai dengan satu angka: berapa jam ia akan berjalan?

Sebelum membandingkan mesin, jujurlah tentang ini:

- Grup yang berjalan **sekali setahun** saat badai — bahan bakar hampir tidak penting. Beli yang termurah yang memenuhi.
- Grup yang berjalan **ratusan jam setahun** di jaringan lemah — bahan bakar adalah anggaran nyata Anda, dan efisiensi sangat penting.

Daya sama, keputusan beli yang benar-benar berbeda.

## Lakukan perhitungan kasar

Misalkan Anda butuh 400 kW dan grup membakar sekitar 80 liter per jam pada beban tipikal. Atas, katakanlah, 800 jam setahun, itu puluhan ribu liter. Beberapa poin persentase konsumsi bahan bakar lebih baik — tak terlihat di brosur — adalah penghematan serius setiap tahun, dan bertambah selama satu dekade.

Inilah mengapa mesin yang efisien dan torsi kuat seperti blok Scania layak dipertahankan: ia mempertahankan hemat bahan bakar bahkan pada beban parsial, di mana grup standby benar-benar menghabiskan sebagian besar waktunya.

## Jebakan yang dihadapi pembeli

- **Ukuran berlebih** — membeli mesin jauh lebih besar dari yang Anda butuhkan. Mesin besar yang jalan idle di bawah beban ringan membakar bahan bakar sia-sia dan aus aneh.
- **Mengabaikan beban parsial** — efisiensi pada daya 100% bagus, tetapi Anda jarang berjalan di 100%. Tanyakan tentang efisiensi pada setengah beban.
- **Hanya membaca harga stiker** — mesin murah terlihat hebat sampai tagihan bahan bakar pertama.

## Pertanyaan biaya Anda, terjawab

| Pertanyaan Anda | Jawaban praktis |
|---|---| | Bagaimana saya memperkirakan penggunaan bahan bakar? | Kira-kira liter/jam × jam berjalan tahunan Anda |
| Kapan efisiensi terbayar? | Ketika grup berjalan banyak jam per tahun |
| Apa yang dicakup ~400 kW? | Bangunan komersial besar, rumah sakit, pabrik |
| Mesin lebih besar selalu lebih mahal dioperasikan? | Sering ya — ukur sesuai beban nyata Anda |

## Aturan sederhana

Jika genset Anda sering jalan, beli mesin yang efisien. Jika hampir tidak jalan, jangan bayar lebih untuk efisiensi yang tidak akan Anda gunakan. Bagaimanapun juga, ukur sesuai beban nyata Anda — bukan angka bulat.

## Kirim kami jam operasional Anda

Beri tahu kami berapa jam setahun grup mungkin akan berjalan dan beban rata-rata Anda. Kami akan memperkirakan penggunaan bahan bakar untuk Anda dan menunjukkan titik impas, sehingga Anda memilih dengan angka daripada tebakan.
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
