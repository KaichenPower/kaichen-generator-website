# -*- coding: utf-8 -*-
"""Translate blog body for 120kw-backup-set-on-tight-budget to 10 locales."""
import yaml as y, os

slug = '120kw-backup-set-on-tight-budget'

bodies = {
'ru': '''![Дизельная генераторная установка Shangchai 120 кВт в кожухе](/images/blog/blog-shangchai-120kw-silent.jpg)

У каждого покупателя есть бюджет. Честный вопрос не в том, «как потратить как можно меньше?», а в том, «где можно срезать, не купив проблему, за которую придётся платить позже?»

Установка 120 кВт (примерно 150 кВА) — это размер, где этот компромисс становится реальным. Это точка входа для небольшого завода, коммерческого здания или отеля, которые не могут позволить себе простой, но это также размер, где самое дешёвое предложение выглядит заманчиво.

## Для чего предназначена установка 120 кВт

Прежде чем говорить о бюджете, определитесь с назначением:

- Небольшое производственное подразделение с несколькими станками и офисной нагрузкой
- Отель на 30–50 номеров с освещением, лифтами и насосами
- Супермаркет среднего размера с холодильным и кассовым оборудованием
- Школа или учебный центр с освещением и IT-помещением
- Строительный городок с башенным краном, освещением и офисом на площадке

Рабочая нагрузка здесь обычно 80–100 кВт. Установка имеет запас для запуска двигателей, и она не настолько велика, чтобы работать с перегрузкой при частичной нагрузке.

## Где экономия безопасна

Если бюджет ограничен, есть места, где можно потратить меньше без сожалений:

- **Обработка кожуха.** Порошковая окраска стандартного цвета стоит меньше, чем покраска. Двигатель она защищает так же.
- **Марка генератора.** Местного уважаемого генератора достаточно для резервной работы. Известный импортный генератор нужен только если нагрузка высокочувствительна.
- **Функции контроллера.** Вам не нужна полная сенсорная система мониторинга с удалённым GSM, если установку проверяют еженедельно на месте.
- **Размер расходного бака.** Скромного бака на 8 часов достаточно для резервной работы; 24-часовой подземный бак нужен только для критических объектов.

Установка на базе Shangchai в этом классе часто попадает сюда, потому что сам двигатель хорошо проверен на внутреннем китайском рынке и широко поддерживается по всей Азии. Разница в цене по сравнению с импортным двигателем реальна, а машина всё равно выполняет свою работу.

## Где экономия опасна

Есть границы, которые не стоит пересекать, даже если продавец дружелюбен:

- **Экономия на автоматическом вводе резерва.** Ручной запуск приемлем на ферме, где кто-то есть на месте. В отеле или клинике установка должна запускаться сама за секунды.
- **Отказ от шумозащитного кожуха.** Открытая установка 120 кВт громкая. В итоге вы построите стену вокруг неё, что обойдётся дороже, чем кожух.
- **Занижение на один тир.** Установка 100 кВт для нагрузки 90 кВт будет всю жизнь работать на пределе. Двигатель перегревается, напряжение проседает, и гарантия аннулируется из-за злоупотребления.
- **Отсутствие местного сервиса.** Это то, что кусается. Дешёвая установка без местной мастерской — это не покупка, это ставка.

## Арифметика ограниченного бюджета

Предположим, бюджет даёт вам два варианта:

1. Установка 120 кВт с импортным двигателем, полностью укомплектованная, но без места для расходного бака.
2. Установка 120 кВт на базе Shangchai, с шумозащитным кожухом, АВР и 8-часовым баком.

Для большинства небольших коммерческих объектов второй вариант — более разумная покупка. Вы платите меньше не за меньшее — вы платите меньше за функции, которые реально используете, и пропускаете значки, которые вам не нужны.

## Финальный чек-лист перед принятием решения

- [ ] Список нагрузки разделён на рабочую и пусковую.
- [ ] Напряжение и фазность подтверждены.
- [ ] Выбран резервный или основной режим.
- [ ] Определена местная сервисная мастерская для марки двигателя.
- [ ] Запланирован бетонный фундамент и путь выхлопа.
- [ ] АВР включён, а не опционален.

Если ваш бюджет ограничен, скажите нам цифру. Мы построим установку, которая подходит ему, не сокращая важные детали.
''',

'es': '''![Grupo diesel silencioso Shangchai 120kW](/images/blog/blog-shangchai-120kw-silent.jpg)

Cada comprador tiene un presupuesto. La pregunta honesta no es «¿cómo gastar lo menos posible?» sino «¿dónde puedo recortar sin comprar un problema que pagaré después?»

Un grupo silencioso de 120 kW (unos 150 kVA) es el tamaño donde este compromiso se hace real. Es el punto de entrada para una fábrica pequeña, un edificio comercial o un hotel que no puede permitirse una avería, pero también es el tamaño donde la cotización más barata parece tentadora.

## Para qué sirve un grupo de 120 kW

Antes de hablar de presupuesto, sea claro en el ajuste:

- Una unidad de fabricación pequeña con algunas máquinas y carga de oficina
- Un hotel de 30 a 50 habitaciones con iluminación, ascensores y bombas de agua
- Un supermercado mediano con refrigeración y sistemas de cobro
- Una escuela o centro de formación con iluminación y sala de TI
- Un campamento de construcción con grúa torre, iluminación y oficina en sitio

La carga en marcha aquí suele ser de 80 a 100 kW. El grupo tiene margen para arranques de motor, y no es tan grande que trabaje con carga parcial.

## Dónde el ahorro es seguro

Si el presupuesto es ajustado, hay lugares donde puede gastar menos sin arrepentirse:

- **Acabado de la carcasa.** Una carcasa con pintura en polvo de color estándar cuesta menos que una pintada. Protege el motor igual.
- **Marca del alternador.** Un alternador local de buena reputación está bien para servicio de respaldo. Solo necesita un alternador de importación conocido si la carga es muy sensible.
- **Características del controlador.** No necesita un sistema completo de monitoreo táctil con GSM remoto si el grupo se revisa semanalmente en sitio.
- **Tamaño del tanque diurno.** Un tanque modesto de 8 horas está bien para servicio de respaldo; solo necesita un tanque de sótano de 24 horas para sitios de misión crítica.

Un grupo basado en Shangchai en esta clase suele aterrizar aquí, porque el motor en sí está bien probado en el mercado interno chino y ampliamente respaldado en toda Asia. El paso de precio frente a un motor importado es real, y la máquina todavía hace el trabajo.

## Dónde el ahorro es peligroso

Hay líneas que no debe cruzar, incluso cuando el vendedor es amable:

- **Cortar el interruptor de transferencia automática.** Un arranque manual está bien en una granja donde alguien está en sitio. En un hotel o clínica, el grupo debe arrancarse solo en segundos.
- **Saltar la carcasa acústica.** Un grupo abierto de 120 kW es ruidoso. Terminará construyendo un muro a su alrededor, que cuesta más que la carcasa habría costado.
- **Subdimensionar por un nivel.** Un grupo de 100 kW para una carga de 90 kW pasará su vida al límite. El motor se sobrecalienta, el voltaje cae, y la garantía se anula por abuso.
- **Sin servicio local.** Este es el que muerde. Un grupo barato sin taller local no es una compra, es una apuesta.

## La aritmética de un presupuesto ajustado

Suponga que su presupuesto le da dos opciones:

1. Un grupo de 120 kW con motor importado, totalmente equipado, pero sin espacio para un tanque diurno.
2. Un grupo de 120 kW basado en Shangchai, carcasa silenciosa, interruptor de transferencia automática, y un tanque de 8 horas.

Para la mayoría de los sitios comerciales pequeños, la segunda opción es la compra más inteligente. No está pagando menos por menos — está pagando menos por las características que realmente usa, y saltando los emblemas que no necesita.

## Una lista final antes de comprometerse

- [ ] Lista de carga dividida en funcionamiento y arranque de motor.
- [ ] Voltaje y fase confirmados.
- [ ] Servicio de respaldo vs continuo elegido.
- [ ] Taller de servicio local identificado para la marca del motor.
- [ ] Zócalo de concreto y ruta de escape planeados.
- [ ] Interruptor de transferencia automática incluido, no opcional.

Si su presupuesto es ajustado, díganos el número. Construiremos el grupo que se ajuste sin cortar las partes que importan.
''',

'fr': '''![Groupe diesel silencieux Shangchai 120kW](/images/blog/blog-shangchai-120kw-silent.jpg)

Chaque acheteur a un budget. La question honnête n'est pas « comment dépenser le moins possible ? » mais « où puis-je couper sans acheter un problème que je paierai plus tard ? »

Un groupe silencieux de 120 kW (environ 150 kVA) est la taille où ce compromis devient réel. C'est le point d'entrée pour une petite usine, un bâtiment commercial ou un hôtel qui ne peut pas se permettre une panne, mais c'est aussi la taille où le devis le moins cher semble tentant.

## À quoi sert un groupe de 120 kW

Avant de parler budget, soyez clair sur l'adéquation :

- Une petite unité de fabrication avec quelques machines et une charge de bureau
- Un hôtel de 30 à 50 chambres avec éclairage, ascenseurs et pompes à eau
- Un supermarché de taille moyenne avec réfrigération et systèmes de caisse
- Une école ou un centre de formation avec éclairage et salle informatique
- Un camp de chantier avec grue à tour, éclairage et bureau de site

La charge de fonctionnement ici est généralement de 80 à 100 kW. Le groupe a une marge pour les démarrages moteur, et il n'est pas si grand qu'il travaille à vide à charge partielle.

## Où les économies sont sûres

Si le budget est serré, il y a des endroits où vous pouvez dépenser moins sans regret :

- **Finition du capot.** Un capot peint en poudre de couleur standard coûte moins cher qu'un capot peint. Il protège le moteur de la même façon.
- **Marque de l'alternateur.** Un alternateur local réputé convient pour le service de secours. Vous n'avez besoin d'un alternateur d'importation connu que si la charge est très sensible.
- **Fonctions du contrôleur.** Vous n'avez pas besoin d'un système complet de surveillance à écran tactile avec GSM distant si le groupe est vérifié hebdomadairement sur place.
- **Taille du réservoir journalier.** Un réservoir modeste de 8 heures convient pour le service de secours ; vous n'avez besoin d'un réservoir de sous-sol de 24 heures que pour les sites critiques.

Un groupe basé sur Shangchai dans cette classe atterrit souvent ici, car le moteur lui-même est bien éprouvé sur le marché intérieur chinois et largement soutenu en Asie. L'écart de prix par rapport à un moteur importé est réel, et la machine fait toujours le travail.

## Où les économies sont dangereuses

Il y a des lignes que vous ne devriez pas franchir, même quand le vendeur est aimable :

- **Supprimer l'interrupteur de transfert automatique.** Un démarrage manuel convient dans une ferme où quelqu'un est sur place. Dans un hôtel ou une clinique, le groupe doit démarrer seul en quelques secondes.
- **Sauter le capot phonique.** Un groupe ouvert de 120 kW est bruyant. Vous finirez par construire un mur autour, ce qui coûte plus cher que le capot n'aurait coûté.
- **Sous-dimensionner d'un cran.** Un groupe de 100 kW pour une charge de 90 kW passera sa vie à la limite. Le moteur surchauffe, la tension chute, et la garantie s'annule d'elle-même par abus.
- **Pas de service local.** C'est celui qui mord. Un groupe bon marché sans atelier local n'est pas un achat, c'est un pari.

## L'arithmétique d'un budget serré

Supposons que votre budget vous donne deux options :

1. Un groupe de 120 kW à moteur importé, entièrement équipé, mais sans place pour un réservoir journalier.
2. Un groupe de 120 kW basé sur Shangchai, capot silencieux, interrupteur de transfert automatique, et un réservoir de 8 heures.

Pour la plupart des petits sites commerciaux, la deuxième option est l'achat le plus judicieux. Vous ne payez pas moins pour moins — vous payez moins pour les fonctions que vous utilisez réellement, et vous sautez les badges dont vous n'avez pas besoin.

## Une liste de contrôle finale avant de vous engager

- [ ] Liste des charges divisée en fonctionnement et démarrage moteur.
- [ ] Tension et phase confirmées.
- [ ] Service de secours vs continu choisi.
- [ ] Atelier de service local identifié pour la marque du moteur.
- [ ] Socle en béton et chemin d'échappement planifiés.
- [ ] Interrupteur de transfert automatique inclus, pas en option.

Si votre budget est serré, dites-nous le chiffre. Nous construirons le groupe qui lui convient sans couper les pièces qui comptent.
''',

'de': '''![Volvo 120kW Shangchai schallgeschütztes Dieselaggregat](/images/blog/blog-shangchai-120kw-silent.jpg)

Jeder Käufer hat ein Budget. Die ehrliche Frage ist nicht «wie gebe ich so wenig wie möglich aus?» sondern «wo kann ich kürzen, ohne ein Problem zu kaufen, für das ich später bezahle?»

Ein 120 kW (ca. 150 kVA) Schallschutzaggregat ist die Größe, bei der dieser Kompromiss real wird. Es ist der Einstiegspunkt für eine kleine Fabrik, ein Geschäftsgebäude oder ein Hotel, das sich einen Ausfall nicht leisten kann, aber es ist auch die Größe, bei die das günstigste Angebot verlockend aussieht.

## Wofür ein 120-kW-Aggregat ist

Bevor wir über Budget sprechen, seien Sie klar über die Eignung:

- Eine kleine Produktionseinheit mit einigen Maschinen und Bürolast
- Ein Hotel mit 30–50 Zimmern mit Beleuchtung, Aufzügen und Wasserpumpen
- Ein mittelgroßer Supermarkt mit Kühlung und Kassensystemen
- Eine Schule oder ein Trainingscenter mit Beleuchtung und IT-Raum
- Eine Baustelle mit Turmkran, Beleuchtung und Baustellenbüro

Die laufende Last hier beträgt normalerweise 80–100 kW. Das Aggregat hat Puffer für Motorstarts, und es ist nicht so groß, dass es bei Teillast schlecht läuft.

## Wo die Einsparung sicher ist

Wenn das Budget knapp ist, gibt es Stellen, an denen Sie weniger ausgeben können ohne es zu bereuen:

- **Kabinenfinish.** Eine pulverbeschichtete Kabine in Standardfarbe kostet weniger als eine lackierte. Sie schützt den Motor genauso.
- **Generator-Marke.** Ein lokal angesehener Generator reicht für Notbetrieb. Sie brauchen einen bekannten Import-Generator nur, wenn die Last hochempfindlich ist.
- **Controller-Funktionen.** Sie brauchen kein vollständiges Touchscreen-Monitoringsystem mit GSM-Fernüberwachung, wenn das Aggregat wöchentlich vor Ort geprüft wird.
- **Tagestankgröße.** Ein bescheidener 8-Stunden-Tank reicht für Notbetrieb; einen 24-Stunden-Kellertank brauchen Sie nur für kritische Standorte.

Ein Shangchai-basiertes Aggregat in dieser Klasse landet oft hier, weil der Motor selbst auf dem chinesischen Inlandsmarkt gut bewährt ist und in ganz Asien unterstützt wird. Der Preisunterschied zu einem Importmotor ist real, und die Maschine macht immer noch die Arbeit.

## Wo die Einsparung gefährlich ist

Es gibt Grenzen, die Sie nicht überschreiten sollten, auch wenn der Verkäufer freundlich ist:

- **Den Netzumschalter kürzen.** Ein manueller Start ist auf einem Bauernhof in Ordnung, wo jemand vor Ort ist. In einem Hotel oder einer Klinik muss das Aggregat innerhalb von Sekunden selbst starten.
- **Die Schallschutzkabine überspringen.** Ein offenes 120-kW-Aggregat ist laut. Sie werden am Ende eine Mauer darum bauen, was mehr kostet als die Kabine gekostet hätte.
- **Um eine Stufe unterdimensionieren.** Ein 100-kW-Aggregat für eine 90-kW-Last wird sein Leben am Limit verbringen. Der Motor überhitzt, Spannung bricht ein, und die Garantie erlischt durch Missbrauch.
- **Kein lokaler Service.** Das ist das, was beißt. Ein billiges Aggregat ohne lokale Werkstatt ist kein Kauf, es ist eine Wette.

## Die Arithmetik eines knappen Budgets

Angenommen, Ihr Budget gibt Ihnen zwei Optionen:

1. Ein 120-kW-Aggregat mit Importmotor, voll ausgestattet, aber kein Platz für einen Tagestank.
2. Ein 120-kW-Aggregat auf Shangchai-Basis, Schallschutzkabine, automatischer Netzumschalter und ein 8-Stunden-Tank.

Für die meisten kleinen Geschäftsstandorte ist die zweite Option der klügere Kauf. Sie zahlen nicht weniger für weniger — Sie zahlen weniger für die Funktionen, die Sie tatsächlich nutzen, und überspringen die Marken, die Sie nicht brauchen.

## Eine letzte Checkliste, bevor Sie sich festlegen

- [ ] Lastliste aufgeteilt in laufende und Motoranlasslast.
- [ ] Spannung und Phase bestätigt.
- [ ] Not- vs. Dauerbetrieb gewählt.
- [ ] Lokale Servicewerkstatt für die Motormarke identifiziert.
- [ ] Betonsockel und Abgasweg geplant.
- [ ] Automatischer Netzumschalter inklusive, nicht optional.

Wenn Ihr Budget knapp ist, nennen Sie uns die Zahl. Wir bauen das Aggregat, das passt, ohne die Teile zu kürzen, die wichtig sind.
''',

'pt': '''![Grupo diesel silencioso Shangchai 120kW](/images/blog/blog-shangchai-120kw-silent.jpg)

Cada comprador tem um orçamento. A pergunta honesta não é «como gastar o mínimo possível?» mas «onde posso cortar sem comprar um problema que pagarei depois?»

Um grupo silencioso de 120 kW (cerca de 150 kVA) é o tamanho onde essa troca se torna real. É o ponto de entrada para uma pequena fábrica, um prédio comercial ou um hotel que não pode permitir uma pane, mas também é o tamanho onde a cotação mais barata parece tentadora.

## Para que serve um grupo de 120 kW

Antes de falar de orçamento, seja claro no ajuste:

- Uma pequena unidade de fabricação com algumas máquinas e carga de escritório
- Um hotel de 30 a 50 quartos com iluminação, elevadores e bombas de água
- Um supermercado médio com refrigeração e sistemas de caixa
- Uma escola ou centro de treinamento com iluminação e sala de TI
- Um canteiro de obras com grua torre, iluminação e escritório de obra

A carga de funcionamento aqui geralmente é de 80 a 100 kW. O grupo tem margem para partidas de motor, e não é tão grande que trabalhe a seco em carga parcial.

## Onde a economia é segura

Se o orçamento está apertado, há lugares onde você pode gastar menos sem arrependimento:

- **Acabamento da canopy.** Uma canopy com pintura a pó de cor padrão custa menos que uma pintada. Protege o motor da mesma forma.
- **Marca do alternador.** Um alternador local de boa reputação serve para serviço de emergência. Você só precisa de um alternador importado conhecido se a carga for altamente sensível.
- **Recursos do controlador.** Você não precisa de um sistema completo de monitoramento touchscreen com GSM remoto se o grupo é checado semanalmente no local.
- **Tamanho do tanque diário.** Um tanque modesto de 8 horas serve para serviço de emergência; você só precisa de um tanque de porão de 24 horas para locais de missão crítica.

Um grupo baseado em Shangchai nesta classe geralmente cai aqui, porque o motor em si é bem comprovado no mercado doméstico chinês e amplamente suportado em toda a Ásia. O passo de preço em relação a um motor importado é real, e a máquina ainda faz o trabalho.

## Onde a economia é perigosa

Há linhas que você não deve cruzar, mesmo quando o vendedor é simpático:

- **Cortar o chave de transferência automática.** Uma partida manual serve em uma fazenda onde alguém está no local. Em um hotel ou clínica, o grupo deve iniciar sozinho em segundos.
- **Pular a canopy acústica.** Um grupo aberto de 120 kW é barulhento. Você acabará construindo um muro ao redor, o que custa mais do que a canopy custaria.
- **Subdimensionar por um nível.** Um grupo de 100 kW para uma carga de 90 kW passará a vida no limite. O motor superaquece, a tensão cai, e a garantia se anula por abuso.
- **Sem serviço local.** Este é o que morde. Um grupo barato sem oficina local não é uma compra, é uma aposta.

## A aritmética de um orçamento apertado

Suponha que seu orçamento lhe dá duas opções:

1. Um grupo de 120 kW com motor importado, totalmente equipado, mas sem espaço para um tanque diário.
2. Um grupo de 120 kW baseado em Shangchai, canopy silenciosa, chave de transferência automática, e um tanque de 8 horas.

Para a maioria dos pequenos locais comerciais, a segunda opção é a compra mais sábia. Você não está pagando menos por menos — está pagando menos pelos recursos que realmente usa, e pulando os emblemas de que não precisa.

## Uma lista final antes de se comprometer

- [ ] Lista de cargas dividida em funcionamento e partida de motor.
- [ ] Tensão e fase confirmadas.
- [ ] Serviço de emergência vs contínuo escolhido.
- [ ] Oficina de serviço local identificada para a marca do motor.
- [ ] Base de concreto e rota de exaustão planejadas.
- [ ] Chave de transferência automática incluída, não opcional.

Se seu orçamento está apertado, diga-nos o número. Construiremos o grupo que cabe nele sem cortar as partes que importam.
''',

'ar': '''![مجموعة ديزل كاتمة Shangchai 120 كيلوواط](/images/blog/blog-shangchai-120kw-silent.jpg)

كل مشتري لديه ميزانية. السؤال الصادق ليس «كيف أنفق أقل قدر ممكن؟» بل «أين يمكنني التقليل دون شراء مشكلة سأدفع ثمنها لاحقاً؟»

المجموعة الكاتمة 120 كيلوواط (حوالي 150 كيلو فولت أمبير) هي الحجم الذي تصبح فيه هذه المقايضة حقيقية. إنها نقطة الدخول لمصنع صغير، مبنى تجاري، أو فندق لا يستطيع تحمل التوقف، لكنها أيضاً الحجم حيث تبدو أرخص عرض مغرياً.

## لما تستخدم مجموعة 120 كيلوواط

قبل أن نتحدث عن الميزانية، كن واضحاً في الملاءمة:

- وحدة تصنيع صغيرة ببضع آلات وحمل مكتبي
- فندق 30-50 غرفة مع إضاءة ومصاعد ومضخات مياه
- سوبر ماركت متوسط الحجم مع تبريد وأنظمة دفع
- مدرسة أو مركز تدريب مع إضاءة وغرفة تكنولوجيا معلومات
- مجمع بناء مع رافعة برجية وإضاءة ومكتب موقع

الحمل التشغيلي هنا عادة 80-100 كيلوواط. المجموعة لديها هامش لبدء تشغيل المحركات، وليست كبيرة جداً لدرجة أن تحمل جزئياً.

## أين يكون الادخار آمناً

إذا كانت الميزانية ضيقة، هناك أماكن يمكنك إنفاق أقل فيها دون ندم:

- **تشطيب الهيكل.** الهيكل المطلي بالبودرة بلون قياسي يكلف أقل من المطلي. يحمي المحرك بنفس الطريقة.
- **علامة المولد.** مولد محلي ذو سمعة جيدة يكفي للخدمة الاحتياطية. تحتاج فقط إلى مولد مستورد معروف إذا كان الحمل حساساً للغاية.
- **ميزات المتحكم.** لا تحتاج إلى نظام مراقبة بشاشة لمس كاملة مع GSM بعيد إذا كانت المجموعة تفحص أسبوعياً في الموقع.
- **حجم خزان اليوم.** خزان متواضع لمدة 8 ساعات يكفي للخدمة الاحتياطية؛ تحتاج فقط إلى خزان قبو لمدة 24 ساعة لمواقع المهمة الحرجة.

المجموعة القائمة على Shangchai في هذه الفئة غالباً ما تهبط هنا، لأن المحرك نفسه مثبت جيداً في السوق المحلية الصينية ومدعوم على نطاق واسع في جميع أنحاء آسيا. فرق السعر مقابل محرك مستورد حقيقي، والآلة لا تزال تقوم بالعمل.

## أين يكون الادخار خطيراً

هناك خطوط لا يجب عبورها، حتى عندما يكون البائع ودياً:

- **قطع مفتاح التحويل التلقائي.** البدء اليدوي جيد في مزرعة حيث يوجد شخص في الموقع. في فندق أو عيادة، يجب أن تبدأ المجموعة بنفسها خلال ثوانٍ.
- **تخطي الهيكل الصوتي.** المجموعة المفتوحة 120 كيلوواط صاخبة. ستنتهي ببناء جدار حولها، مما يكلف أكثر مما كان سيكلفه الهيكل.
- **تقليل الحجم بمستوى واحد.** مجموعة 100 كيلوواط لحمل 90 كيلوواط ستقضي حياتها على الحافة. المحرك يسخن، والجهد ينخفض، والضمان يبطل نفسه بسبب الإساءة.
- **لا خدمة محلية.** هذا هو الذي يعض. المجموعة الرخيصة بدون ورشة محلية ليست عملية شراء، بل رهان.

## حساب الميزانية الضيقة

افترض أن ميزانيتك تعطيك خيارين:

1. مجموعة 120 كيلوواط بمحرك مستورد، كاملة المواصفات، ولكن لا توجد مساحة لخزان يومي.
2. مجموعة 120 كيلوواط قائمة على Shangchai، هيكل كاتم الصوت، مفتاح تحويل تلقائي، وخزان 8 ساعات.

بالنسبة لمعظم المواقع التجارية الصغيرة، الخيار الثاني هو الشراء الأكثر حكمة. أنت لا تدفع أقل مقابل أقل — أنت تدفع أقل مقابل الميزات التي تستخدمها فعلياً، وتتخطى الشعارات التي لا تحتاجها.

## قائمة تحقق نهائية قبل الالتزام

- [ ] قائمة الأحمال مقسمة إلى تشغيل وبدء محرك.
- [ ] الجهد والطور مؤكدان.
- [ ] تم اختيار الخدمة الاحتياطية مقابل الرئيسية.
- [ ] تم تحديد ورشة خدمة محلية لعلامة المحرك.
- [ ] تم التخطيط لقاعدة خرسانية ومسار العادم.
- [ ] مفتاح التحويل التلقائي مضمن، وليس اختيارياً.

إذا كانت ميزانيتك ضيقة، أخبرنا بالرقم. سنبني المجموعة التي تناسبها دون قطع الأجزاء المهمة.
''',

'tr': '''![Shangchai 120kW sessiz dizel jeneratör](/images/blog/blog-shangchai-120kw-silent.jpg)

Her alıcının bir bütçesi vardır. Dürüst soru «nasıl en az harcarım?» değil, «sonra için ödeyeceğim bir sorun satın almadan nereden kesebilirim?» sorusudur.

120 kW (yaklaşık 150 kVA) sessiz grup, bu değiş tokuşun gerçekleştiği boyuttur. Ufak fabrika, ticari bina veya arıza göze alamayan bir otel için giriş noktasıdır, ama aynı zamanda en ucuz teklifin cazip göründüğü boyuttur.

## 120 kW grup ne içindir

Bütçeden bahsetmeden önce, uyumu netleştirin:

- Birkaç makine ve ofis yüküyle küçük bir üretim birimi
- Aydınlatma, asansör ve su pompalarıyla 30-50 odalı otel
- Soğutma ve kasa sistemleriyle orta boy bir süpermarket
- Aydınlatma ve BT odasıyla okul veya eğitim merkezi
- Kule vinç, aydınlatma ve şantiye ofisiyle inşaat kampı

Buradaki çalışan yük genellikle 80-100 kW'dır. Grubun motor kalkışları için baş payı vardır ve kısmi yükte zorlanmayacak kadar büyük değildir.

## Tasarrufun güvenli olduğu yerler

Bütçe sıkıysa, pişman olmadan daha az harcayabileceğiniz yerler vardır:

- **Kabin kaplaması.** Standart renkte toz boya kaplama kabin, boyalı olandan daha ucuza gelir. Motoru aynı şekilde korur.
- **Alternatör markası.** Yerel olarak itibarlı bir alternatör, yedek görev için iyidir. Yalnızca yük yüksek derecede hassassa bilinen bir import alternatöre ihtiyacınız vardır.
- **Kontrol özellikleri.** Grup şantiyede haftalık kontrol ediliyorsa, uzaktan GSM'li tam dokunmatik izleme sistemine ihtiyacınız yoktur.
- **Günlük depo boyutu.** Mütevazı 8 saatlik depo, yedek görev için iyidir; yalnızca kritik görevli siteler için 24 saatlik bodrum deposuna ihtiyacınız vardır.

Bu sınıftaki Shangchai tabanlı bir grup genellikle buraya düşer, çünkü motorun kendisi Çin iç pazarında iyi kanıtlanmıştır ve Asya genelinde yaygın olarak desteklenir. Import motora karşı fiyat adımı gerçektir ve makine yine de işi yapar.

## Tasarrufun tehlikeli olduğu yerler

Satıcı dostu olsa bile geçmemeniz gereken çizgiler vardır:

- **Otomatik transfer anahtarını kesmek.** Şantiyede birinin bulunduğu çiftlikte manuel başlatma iyidir. Otelde veya klinikte, grubun saniyeler içinde kendiliğinden başlaması gerekir.
- **Ses kabinini atlamak.** Açık 120 kW grup gürültülüdür. Etrafında bir duvar inşa etmekle sonuçlanırsınız, bu da kabinin mâl olacağından daha pahalıya gelir.
- **Bir kademe küçültmek.** 90 kW yük için 100 kW grup, ömrünü sınırda geçirecektir. Motor aşırı ısınır, voltaj düşer ve garanti kötüye kullanımdan kendini iptal eder.
- **Yerel servis yok.** Isıran odur. Yerel atölyesi olmayan ucuz bir grup bir satın alma değildir, bir bahistir.

## Sıkı bütçenin matematiği

Diyelim ki bütçeniz size iki seçenek veriyor:

1. 120 kW import motorlu grup, tam özellikli, ama günlük depo için yer yok.
2. 120 kW Shangchai tabanlı grup, sessiz kabin, otomatik transfer anahtarı ve 8 saatlik depo.

Çoğu küçük ticari site için ikinci seçenek daha akıllı bir alımdır. Daha az için daha az ödüyorsunuz değil — gerçekten kullandığınız özellikler için daha az ödüyor ve ihtiyaç duymadığınız markaları atlıyorsunuz.

## Karar vermeden önce son kontrol listesi

- [ ] Yük listesi çalışan ve motor kalkış olarak ayrıldı.
- [ ] Voltaj ve faz teyit edildi.
- [ ] Yedek vs birincil görev seçildi.
- [ ] Motor markası için yerel servis atölyesi belirlendi.
- [ ] Beton kaide ve egzoz güzergahı planlandı.
- [ ] Otomatik transfer anahtarı dahil, isteğe bağlı değil.

Bütçeniz sıkıysa, bize rakamı söyleyin. Önemli parçaları kesmeden, ona uyan grubu inşa edeceğiz.
''',

'th': '''![ชุดดีเซลคงทนเสียง Shangchai 120 กิโลวัตต์](/images/blog/blog-shangchai-120kw-silent.jpg)

ผู้ซื้อทุกคนมีงบประมาณ คำถามที่ตรงไปตรงมาไม่ใช่ «จะใช้จ่ายให้น้อยที่สุดได้อย่างไร?» แต่คือ «ฉันจะตัดตรงไหนได้โดยไม่ซื้อปัญหาที่จะต้องจ่ายในภายหลัง?»

กลุ่มคงทนเสียง 120 กิโลวัตต์ (ประมาณ 150 kVA) คือขนาดที่การแลกเปลี่ยนนี้เป็นจริง จุดเริ่มต้นสำหรับโรงงานขนาดเล็ก อาคารพาณิชย์ หรือโรงแรมที่ไม่สามารถเสียหยุดได้ แต่ก็เป็นขนาดที่ใบเสนอราคาถูกที่สุดดูน่าดึงดูด

## ชุด 120 กิโลวัตต์ใช้ทำอะไร

ก่อนพูดถึงงบประมาณ ให้ชัดเจนเรื่องความเหมาะสม:

- หน่วยผลิตขนาดเล็กที่มีไม่กี่เครื่องและภาระสำนักงาน
- โรงแรม 30-50 ห้องพร้อมแสงไฟ ลิฟต์ และปั๊มน้ำ
- ซูเปอร์มาร์เก็ตขนาดกลางพร้อมระบบทำความเย็นและระบบชำระเงิน
- โรงเรียนหรือศูนย์ฝึกอบรมพร้อมแสงไฟและห้องไอที
- สถานที่ก่อสร้างพร้อมเครนหอคอย แสงไฟ และสำนักงานไซต์

ภาระการทำงานที่นี่ปกติ 80-100 กิโลวัตต์ กลุ่มมีพื้นที่สำหรับการสตาร์ทมอเตอร์ และไม่ใหญ่เกินไปจนทำงานที่ภาระบางส่วน

## ที่ประหยัดได้อย่างปลอดภัย

ถ้างบประมาณจำกัด มีสถานที่ที่คุณสามารถใช้จ่ายน้อยลงโดยไม่เสียใจ:

- **งานตกแต่งเปลือก.** เปลือกเคลือบผงสีมาตรฐานราคาถูกกว่าแบบพ่นสี ปกป้องเครื่องยนต์ได้เหมือนกัน
- **ยี่ห้อเครื่องกำเนิดไฟฟ้า.** เครื่องกำเนิดไฟฟ้าท้องถิ่นที่มีชื่อเสียงใช้ได้สำหรับงานสำรอง คุณต้องการเครื่องกำเนิดไฟฟ้านำเข้าที่รู้จักเฉพาะถ้าภาระมีความละเอียดอ่อนสูง
- **ฟีเจอร์ตัวควบคุม.** คุณไม่จำเป็นต้องใช้ระบบตรวจสอบหน้าจอสัมผัสเต็มรูปแบบพร้อม GSM ระยะไกล ถ้ากลุ่มถูกตรวจสอบสัปดาห์ละครั้งที่ไซต์
- **ขนาดถังประจำวัน.** ถัง 8 ชั่วโมงเรียบง่ายใช้ได้สำหรับงานสำรอง คุณต้องการถังใต้ดิน 24 ชั่วโมงเฉพาะสำหรับไซต์วิกฤติ

กลุ่มพื้นฐาน Shangchai ในคลาสนี้มักตกอยู่ที่นี่ เพราะตัวเครื่องยนต์ได้รับการพิสูจน์อย่างดีในตลาดภายในประเทศจีนและได้รับการสนับสนุนอย่างกว้างขวางทั่วเอเชีย ขั้นราคาที่เทียบกับเครื่องยนต์นำเข้าเป็นเรื่องจริง และเครื่องก็ยังทำงานได้

## ที่ประหยัดได้อย่างอันตราย

มีเส้นที่คุณไม่ควรข้าม แม้ว่าพนักงานขายจะเป็นมิตร:

- **ตัดสวิตช์ถ่ายโอนอัตโนมัติ.** การสตาร์ทแบบแมนนวลใช้ได้ในฟาร์มที่มีคนอยู่ที่ไซต์ ในโรงแรมหรือคลินิก กลุ่มต้องสตาร์ทเองภายในไม่กี่วินาที
- **ข้ามเปลือกกันเสียง.** กลุ่มเปิด 120 กิโลวัตต์มีเสียงดัง คุณจะต้องสร้างกำแพงล้อมรอบ ซึ่งมีค่าใช้จ่ายมากกว่าเปลือกจะมีราคา
- **ลดขนาดลงหนึ่งระดับ.** กลุ่ม 100 กิโลวัตต์สำหรับภาระ 90 กิโลวัตต์จะใช้ชีวิตของมันที่ขอบเขต เครื่องยนต์ร้อนเกินไป แรงดันตก และการรับประกันเป็นโมฆะเองจากการใช้งานผิดวิธี
- **ไม่มีบริการท้องถิ่น.** นี่คือสิ่งที่กัด กลุ่มราคาถูกที่ไม่มีเวิร์กชอปท้องถิ่นไม่ใช่การซื้อ แต่เป็นการพนัน

## คณิตศาสตร์ของงบประมาณที่จำกัด

สมมติว่างบประมาณของคุณให้สองตัวเลือก:

1. กลุ่ม 120 กิโลวัตต์พร้อมเครื่องยนต์นำเข้า ครบฟีเจอร์ แต่ไม่มีที่สำหรับถังประจำวัน
2. กลุ่ม 120 กิโลวัตต์พื้นฐาน Shangchai เปลือกกันเสียง สวิตช์ถ่ายโอนอัตโนมัติ และถัง 8 ชั่วโมง

สำหรับไซต์พาณิชย์ขนาดเล็กส่วนใหญ่ ตัวเลือกที่สองคือการซื้อที่ฉลาดกว่า คุณไม่ได้จ่ายน้อยลงเพราะของน้อยลง — คุณจ่ายน้อยลงสำหรับฟีเจอร์ที่คุณใช้จริง และข้ามโลโก้ที่คุณไม่ต้องการ

## รายการตรวจสอบสุดท้ายก่อนตัดสินใจ

- [ ] รายการภาระแบ่งเป็นทำงานและสตาร์ทมอเตอร์
- [ ] แรงดันและเฟสถูกยืนยัน
- [ ] เลือกงานสำรองเทียบหลักแล้ว
- [ ] ระบุเวิร์กชอปบริการท้องถิ่นสำหรับยี่ห้อเครื่องยนต์แล้ว
- [ ] วางแผนฐานคอนกรีตและเส้นทางไอเสียแล้ว
- [ ] สวิตช์ถ่ายโอนอัตโนมัติรวมอยู่ ไม่ใช่อุปกรณ์เสริม

ถ้างบประมาณของคุณจำกัด บอกเราเลขนั้น เราจะสร้างกลุ่มที่พอดีโดยไม่ตัดส่วนที่สำคัญ
''',

'vi': '''![Tổ máy diesel chống ồn Shangchai 120kW](/images/blog/blog-shangchai-120kw-silent.jpg)

Mỗi người mua đều có ngân sách. Câu hỏi thành thật không phải «làm sao để tiêu ít nhất có thể?» mà là «tôi có thể cắt ở đâu mà không mua phải một vấn đề mà tôi sẽ trả giá sau?»

Một tổ máy chống ồn 120 kW (khoảng 150 kVA) là kích thước mà sự đánh đổi này trở nên thực tế. Đó là điểm khởi đầu cho một nhà máy nhỏ, một tòa nhà thương mại, hoặc một khách sạn không thể cho phép sự cố, nhưng cũng là kích thước mà báo giá rẻ nhất trông hấp dẫn.

## Tổ máy 120 kW dùng để làm gì

Trước khi nói về ngân sách, hãy rõ về sự phù hợp:

- Một đơn vị sản xuất nhỏ với vài máy và tải văn phòng
- Một khách sạn 30–50 phòng với chiếu sáng, thang máy và bơm nước
- Một siêu thị cỡ trung với hệ thống lạnh và thanh toán
- Một trường học hoặc trung tâm đào tạo với chiếu sáng và phòng IT
- Một khu công trường với cẩu tháp, chiếu sáng và văn phòng công trường

Tải chạy ở đây thường là 80–100 kW. Tổ máy có dư địa cho khởi động động cơ, và không quá lớn đến mức chạy kém ở tải một phần.

## Tiết kiệm an toàn ở đâu

Nếu ngân sách eo hẹp, có những nơi bạn có thể chi ít hơn mà không hối tiếc:

- **Hoàn thiện canopy.** Canopy sơn tĩnh điện màu tiêu chuẩn rẻ hơn sơn. Nó bảo vệ động cơ như nhau.
- **Thương hiệu máy phát.** Máy phát uy tín địa phương là đủ cho nhiệm vụ dự phòng. Bạn chỉ cần máy phát nhập khẩu nổi tiếng nếu tải rất nhạy cảm.
- **Tính năng bộ điều khiển.** Bạn không cần hệ thống giám sát màn hình cảm ứng đầy đủ với GSM từ xa nếu tổ máy được kiểm tra hàng tuần tại chỗ.
- **Kích thước thùng ngày.** Thùng 8 giờ khiêm tốn là đủ cho nhiệm vụ dự phòng; bạn chỉ cần thùng tầng hầm 24 giờ cho các địa điểm quan trọng.

Một tổ máy dựa trên Shangchai trong hạng này thường rơi vào đây, vì bản thân động cơ đã được kiểm chứng tốt trên thị trường nội địa Trung Quốc và được hỗ trợ rộng rãi trên khắp châu Á. Chênh lệch giá so với động cơ nhập khẩu là thực tế, và máy vẫn làm được việc.

## Tiết kiệm nguy hiểm ở đâu

Có những giới hạn bạn không nên vượt qua, ngay cả khi nhân viên bán hàng thân thiện:

- **Cắt bỏ công tắc chuyển đổi tự động.** Khởi động thủ công ổn trên một nông trại có người tại chỗ. Ở khách sạn hoặc phòng khám, tổ máy phải tự khởi động trong vài giây.
- **Bỏ qua canopy cách âm.** Một tổ máy mở 120 kW ồn. Bạn sẽ kết thúc bằng cách xây một bức tường xung quanh, tốn hơn cả canopy.
- **Giảm kích thước một bậc.** Tổ máy 100 kW cho tải 90 kW sẽ dành cả đời ở giới hạn. Động cơ quá nhiệt, điện áp sụt, và bảo hành tự vô hiệu do lạm dụng.
- **Không có dịch vụ địa phương.** Đây là cái cắn. Một tổ máy rẻ không có xưởng địa phương không phải là mua, mà là cá cược.

## Phép tính của ngân sách eo hẹp

Giả sử ngân sách cho bạn hai lựa chọn:

1. Tổ máy 120 kW động cơ nhập khẩu, đầy đủ tính năng, nhưng không có chỗ cho thùng ngày.
2. Tổ máy 120 kW dựa trên Shangchai, canopy chống ồn, công tắc chuyển đổi tự động, và thùng 8 giờ.

Đối với hầu hết các địa điểm thương mại nhỏ, lựa chọn thứ hai là mua khôn ngoan hơn. Bạn không trả ít hơn vì ít hơn — bạn trả ít hơn cho các tính năng bạn thực sự dùng, và bỏ qua các logo bạn không cần.

## Danh sách kiểm tra cuối cùng trước khi cam kết

- [ ] Danh sách tải tách thành chạy và khởi động động cơ.
- [ ] Điện áp và pha đã xác nhận.
- [ ] Đã chọn nhiệm vụ dự phòng vs chính.
- [ ] Đã xác định xưởng dịch vụ địa phương cho thương hiệu động cơ.
- [ ] Đã lên kế hoạch móng bê tông và đường ống xả.
- [ ] Công tắc chuyển đổi tự động được bao gồm, không phải tùy chọn.

Nếu ngân sách của bạn eo hẹp, hãy cho chúng tôi biết con số. Chúng tôi sẽ xây tổ máy phù hợp mà không cắt các bộ phận quan trọng.
''',

'id': '''![Grup diesel silent Shangchai 120kW](/images/blog/blog-shangchai-120kw-silent.jpg)

Setiap pembeli punya anggaran. Pertanyaan jujur bukan «bagaimana cara menghabiskan sesedikit mungkin?» tapi «di mana saya bisa memotong tanpa membeli masalah yang akan saya bayar nanti?»

Grup silent 120 kW (sekitar 150 kVA) adalah ukuran di mana trade-off ini menjadi nyata. Ini adalah titik masuk untuk pabrik kecil, gedung komersial, atau hotel yang tidak mampu rusak, tapi juga ukuran di mana penawaran termurah terlihat menggoda.

## Untuk apa grup 120 kW

Sebelum kita bicara tentang anggaran, perjelas dulu kecocokannya:

- Unit manufaktur kecil dengan beberapa mesin dan beban kantor
- Hotel 30–50 kamar dengan pencahayaan, lift, dan pompa air
- Supermarket menengah dengan sistem pendingin dan kasir
- Sekolah atau pusat pelatihan dengan pencahayaan dan ruang IT
- Perkampungan konstruksi dengan derek menara, pencahayaan, dan kantor lapangan

Beban berjalan di sini biasanya 80–100 kW. Grup memiliki margin untuk start motor, dan tidak terlalu besar sehingga bekerja berat pada beban parsial.

## Di mana penghematan aman

Jika anggaran ketat, ada tempat di mana Anda bisa menghabiskan lebih sedikit tanpa penyesalan:

- **Finishing canopy.** Canopy powder-coat warna standar lebih murah daripada yang dicat. Melindungi mesin sama baiknya.
- **Merek alternator.** Alternator lokal bereputasi baik untuk tugas standby. Anda hanya butuh alternator impor terkenal jika beban sangat sensitif.
- **Fitur controller.** Anda tidak butuh sistem monitoring touchscreen penuh dengan GSM jarak jauh jika grup dicek mingguan di lokasi.
- **Ukuran tangki harian.** Tangki 8 jam sederhana cukup untuk tugas standby; Anda hanya butuh tangki basement 24 jam untuk lokasi mission-critical.

Grup berbasis Shangchai di kelas ini sering mendarat di sini, karena mesin itu sendiri terbukti baik di pasar domestik China dan didukung luas di seluruh Asia. Selisih harga dibandingkan mesin impor adalah nyata, dan mesin tetap menjalankan pekerjaannya.

## Di mana penghematan berbahaya

Ada garis yang tidak sebaiknya Anda lewati, bahkan ketika penjual ramah:

- **Memotong Automatic Transfer Switch.** Start manual baik di peternakan di mana ada orang di lokasi. Di hotel atau klinik, grup harus start sendiri dalam hitungan detik.
- **Melewatkan canopy suara.** Grup terbuka 120 kW berisik. Anda akan berakhir membangun dinding di sekelilingnya, yang lebih mahal daripada canopy.
- **Under-sizing satu tingkat.** Grup 100 kW untuk beban 90 kW akan menghabiskan hidupnya di tepi. Mesin overheat, voltase turun, dan garansi membatalkan diri karena penyalahgunaan.
- **Tidak ada servis lokal.** Ini yang menggigit. Grup murah tanpa bengkel lokal bukan pembelian, tapi taruhan.

## Aritmetika anggaran ketat

Misalkan anggaran Anda memberi dua pilihan:

1. Grup 120 kW mesin impor, penuh fitur, tapi tidak ada ruang untuk tangki harian.
2. Grup 120 kW berbasis Shangchai, canopy silent, automatic transfer switch, dan tangki 8 jam.

Untuk sebagian besar lokasi komersial kecil, pilihan kedua adalah pembelian yang lebih bijaksana. Anda tidak membayar lebih sedikit untuk lebih sedikit — Anda membayar lebih sedikit untuk fitur yang benar-benar Anda gunakan, dan melewatkan lencana yang tidak Anda butuhkan.

## Daftar periksa terakhir sebelum Anda komitmen

- [ ] Daftar beban dibagi menjadi berjalan dan start motor.
- [ ] Tegangan dan fase dikonfirmasi.
- [ ] Tugas standby vs prime dipilih.
- [ ] Bengkel servis lokal diidentifikasi untuk merek mesin.
- [ ] Pondasi beton dan rute knalpot direncanakan.
- [ ] Automatic transfer switch disertakan, bukan opsional.

Jika anggaran Anda ketat, beri tahu kami angkanya. Kami akan membangun grup yang sesuai tanpa memotong bagian yang penting.
''',
}

eng = open(f'content/blog/{slug}.md', encoding='utf-8').read()
parts = eng.split('---', 2)
fm = y.safe_load(parts[1])
date = fm.get('date', '2026-10-16')

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
