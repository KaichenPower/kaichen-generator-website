# -*- coding: utf-8 -*-
"""Translate blog body for whole-factory-500kw-prime-power to 10 locales."""
import yaml as y, os

slug = 'whole-factory-500kw-prime-power'

bodies = {
'ru': '''![Дизельная генераторная установка Weichai 500 кВт в большом кожухе](/images/blog/blog-weichai-500kw-silent.jpg)

Во многих заводских проектах наступает момент, когда покупатель смотрит на счёт за подключение к сети и принимает решение: либо ждать шесть месяцев, пока энергетики проложат новый кабель и оплатить подключение, либо установить дизельную установку, которая станет основным источником питания завода.

Когда это происходит, генератор перестаёт быть резервным и становится инвестицией. Одна установка 500 кВт (около 625 кВА) на базе Weichai — распространённый выбор для такого решения. Однако планирование отличается от покупки резервного агрегата.

## Резерв — не основной

Первое, что нужно усвоить: установка 500 кВт, купленная как *основная мощность*, — это другая машина, чем та же коробка, купленная как резерв.

- Резервные установки простаивают 99% времени. Они работают несколько часов в год. Двигатель рассчитан на такой цикл.
- Основные установки работают 8–24 часа в день. Они являются основным источником питания. Двигатель должен быть рассчитан на непрерывную работу, с правильной топливной системой, охлаждением и смазкой.

Купите установку резервного режима как основную — и вы перестроите её задолго до ожидаемого срока. Купите установку основного режима как резервную — вы потратите чуть больше необходимого, но машина рассчитана на более долгий срок службы.

## Последовательность нагрузки — вся игра

Установка 500 кВт не начинает нести весь завод за одну секунду. Она распределяет нагрузку в заданной последовательности:

1. **Первые 0–30 секунд:** освещение, офис управления, системы безопасности. Установка прогревается до номинального напряжения.
2. **Следующая минута:** меньшие двигатели, конвейеры, водяные насосы, запускаемые в шахматном порядке контроллером.
3. **Через три минуты:** большие нагрузки — воздушный компрессор, чиллеры, основные производственные двигатели — запускаемые по одному.

Без последовательности первый запуск большого двигателя просадит напряжение, и установка отключится по перегрузке. С последовательностью завод запускается так же, как от сети.

Вот почему важен контроллер. Дешёвого трёхфункционального контроллера, который только запускает и останавливает, недостаточно для основной установки всего завода. Нужен PLC-контроллер, который управляет последовательностью запуска и сбрасывает второстепенные нагрузки, если установка перегревается.

## Вопрос топлива

Установка 500 кВт сжигает примерно 90–110 литров в час при средней нагрузке. Если она работает 12 часов в день, это более тысячи литров в день.

Планирование установки для всего завода означает планирование топлива:

- Дневной бак на установке, 8–12 часов.
- Основной бак во дворе, рассчитанный на неделю работы.
- Договор на поставку с местным поставщиком дизеля, который может прибыть на площадку по расписанию.

Пропустить основной бак — значит основной завод может оказаться в ожидании топливозаправки в производственный день.

## Вопрос резервирования

Одна установка 500 кВт — это одна точка отказа. Для небольшого завода это может быть приемлемо: когда установка на обслуживании, производство останавливается. Для завода с заказами на отгрузку покупатели часто планируют либо:

- Две установки 300 кВт параллельно, разделяющие нагрузку. Когда одна вышла из строя, другая несёт основную нагрузку.
- Одна установка 500 кВт плюс резервная 250 кВт, чтобы критическая линия продолжала работать во время обслуживания.

Какой вариант подходит, зависит от того, насколько дорог простой день для бизнеса. Мы рассчитываем оба варианта и позволяем математике решить.

## Weichai в этом размере

Двигатели Weichai в диапазоне 400–500 кВт распространены для основных установок, потому что блок простой, механический и хорошо поддерживается по всей Азии и Африке. Топливная толерантность хорошая для местного качества дизеля, а сеть запчастей плотная. Для завода на растущем рынке эта сервисопригодность и обеспечивает непрерывность производства.

## Поговорите с нами перед спецификацией

Если вы выбираете между подключением к сети и основной установкой, пришлите нам список нагрузок, часы работы в день и местную цену на топливо. Мы посчитаем и покажем, какой вариант реально выигрывает за пять лет.
''',

'es': '''![Grupo diesel silencioso Weichai 500kW en canopy grande](/images/blog/blog-weichai-500kw-silent.jpg)

Hay un momento en muchos proyectos de fábrica cuando el comprador mira la cotización de conexión a la red y toma una decisión: o esperar seis meses a que la utility tienda un cable nuevo y pague la tarifa de conexión, o instalar un grupo diesel que se convierte en la energía principal de la planta.

Cuando eso sucede, el generador deja de ser un respaldo y se convierte en una inversión. Un solo grupo silencioso Weichai de 500 kW (unos 625 kVA) es una forma común para esa decisión. La planificación, sin embargo, es diferente a comprar una unidad de standby.

## El standby no es el prime

Lo primero que hay que internalizar: un grupo de 500 kW comprado como *potencia primaria* es una máquina distinta de la misma caja comprada como standby.

- Los grupos de standby están parados el 99% del tiempo. Funcionan unas pocas horas al año. El motor está clasificado para ese ciclo de servicio.
- Los grupos prime funcionan de 8 a 24 horas al día. Son la fuente principal de energía. El motor debe estar clasificado para servicio continuo, con el sistema de combustible, refrigeración y lubricación adecuados.

Compre un grupo con clasificación standby como prime y lo reconstruirá mucho antes de lo esperado. Compre un grupo con clasificación prime como standby y habrá gastado un poco más de lo necesario, pero la máquina está construida para una vida más larga.

## La secuencia de carga es todo el juego

Un grupo de 500 kW no empieza a cargar toda la fábrica en un segundo. Carga la secuencia diseñada:

1. **Primeros 0–30 segundos:** iluminación, oficina de control, sistemas de seguridad. El grupo se calienta hasta el voltaje nominal.
2. **Siguiente minuto:** motores más pequeños, cintas transportadoras, bombas de agua, arrancados en orden escalonado por el controlador.
3. **Después de tres minutos:** cargas grandes — compresor de aire, enfriadoras, motores principales de producción — arrancadas una a una.

Sin secuencia, el primer arranque del motor grande arrastra el voltaje hacia abajo y el grupo dispara por sobrecarga. Con secuencia, la fábrica arranca como lo haría en la red.

Por eso el controlador importa. Un controlador barato de tres funciones que solo arranca y para no es suficiente para un grupo prime de fábrica completa. Necesita un controlador impulsado por PLC que gestione la secuencia de arranque y elimine cargas no esenciales si el grupo se calienta.

## La pregunta del combustible

Un grupo de 500 kW quema aproximadamente 90 a 110 litros por hora a carga promedio. Si funciona 12 horas al día, eso son más de mil litros al día.

Planificar una instalación de fábrica completa significa planificar el combustible:

- Tanque diario en el grupo, 8–12 horas.
- Tanque de almacenamiento en el patio, dimensionado para una semana de funcionamiento.
- Contrato de entrega con un proveedor local de diesel que pueda llegar al sitio a tiempo.

Saltarse el tanque de almacenamiento es cómo una fábrica de potencia primaria se encuentra esperando un camión de combustible en un día de producción.

## La pregunta de redundancia

Un solo grupo de 500 kW es un punto único de fallo. Para una fábrica pequeña eso puede ser aceptable: cuando el grupo está parado por mantenimiento, la producción se pausa. Para una fábrica con pedidos que enviar, los compradores suelen planificar:

- Dos grupos de 300 kW en paralelo, compartiendo la carga. Cuando uno está caído, el otro lleva la carga esencial.
- Un grupo de 500 kW más una unidad standby de 250 kW, para que la línea crítica siga arriba durante el mantenimiento.

Qué forma encaja depende de cuánto cuesta un día pausado para el negocio. Presupuestamos ambos y dejamos que las matemáticas decidan.

## Weichai en este tamaño

Los motores Weichai en el rango de 400–500 kW son comunes para instalaciones de potencia primaria porque el bloque es simple, mecánico y bien soportado en toda Asia y África. La tolerancia al combustible es buena para la calidad local del diesel, y la red de repuestos es densa. Para una fábrica en un mercado en crecimiento, esa reparabilidad es lo que mantiene la producción en marcha.

## Hable con nosotros antes de especificar

Si está decidiendo entre una conexión a la red y un grupo de potencia primaria, envíenos la lista de cargas, las horas de funcionamiento por día y el precio local del combustible. Haremos los números y le mostraremos qué opción gana realmente en cinco años.
''',

'fr': '''![Groupe diesel silencieux Weichai 500kW dans un grand capot](/images/blog/blog-weichai-500kw-silent.jpg)

Il y a un moment dans de nombreux projets d'usine où l'acheteur regarde le devis de raccordement au réseau et prend une décision : soit attendre six mois que le fournisseur pose un nouveau câble et payer la redevance de raccordement, soit installer un groupe diesel qui devient la source d'énergie principale de l'usine.

Quand cela arrive, le générateur cesse d'être une secours et devient un investissement. Un seul groupe silencieux Weichai de 500 kW (environ 625 kVA) est une forme courante pour cette décision. La planification, cependant, est différente de l'achat d'une unité de secours.

## Le secours n'est pas le principal

La première chose à intégrer : un groupe de 500 kW acheté en *puissance principale* est une machine différente de la même caisse achetée en secours.

- Les groupes de secours restent inactifs 99 % du temps. Ils fonctionnent quelques heures par an. Le moteur est dimensionné pour ce cycle de service.
- Les groupes principaux fonctionnent de 8 à 24 heures par jour. Ils sont la source d'énergie principale. Le moteur doit être dimensionné pour un service continu, avec le système de carburant, le refroidissement et la lubrification adéquats.

Achetez un groupe classé secours en principal et vous le reconstruirez bien plus tôt que prévu. Achetez un groupe classé principal en secours et vous aurez dépensé un peu plus que nécessaire, mais la machine est conçue pour une durée de vie plus longue.

## La séquence de charge est tout le jeu

Un groupe de 500 kW ne commence pas à porter toute l'usine en une seconde. Il porte la charge dans une séquence conçue :

1. **Premières 0–30 secondes :** éclairage, bureau de contrôle, systèmes de sécurité. Le groupe chauffe jusqu'à la tension nominale.
2. **Minute suivante :** moteurs plus petits, bandes transporteuses, pompes à eau, démarrés en ordre échelonné par le contrôleur.
3. **Après trois minutes :** grosses charges — compresseur d'air, refroidisseurs, moteurs principaux de production — démarrés un par un.

Sans séquence, le premier démarrage du gros moteur tire la tension vers le bas et le groupe disjonque par surcharge. Avec séquence, l'usine démarre comme elle le ferait sur le réseau.

C'est pourquoi le contrôleur compte. Un contrôleur bon marché à trois fonctions qui ne fait que démarrer et arrêter ne suffit pas pour un groupe principal d'usine entière. Vous avez besoin d'un contrôleur piloté par API qui gère la séquence de démarrage et déleste les charges non essentielles si le groupe chauffe.

## La question du carburant

Un groupe de 500 kW consomme environ 90 à 110 litres par heure à charge moyenne. S'il fonctionne 12 heures par jour, cela fait plus de mille litres par jour.

Planifier une installation d'usine entière signifie planifier le carburant :

- Réservoir journalier sur le groupe, 8–12 heures.
- Réservoir de stockage dans la cour, dimensionné pour une semaine de fonctionnement.
- Contrat de livraison avec un fournisseur local de gazole qui peut atteindre le site à l'heure.

Sauter le réservoir de stockage, c'est comment une usine en puissance principale se retrouve à attendre un camion-citerne un jour de production.

## La question de redondance

Un seul groupe de 500 kW est un point de défaillance unique. Pour une petite usine, cela peut être acceptable : quand le groupe est en maintenance, la production s'arrête. Pour une usine avec des commandes à expédier, les acheteurs planifient souvent soit :

- Deux groupes de 300 kW en parallèle, partageant la charge. Quand l'un est en panne, l'autre porte la charge essentielle.
- Un groupe de 500 kW plus une unité de secours de 250 kW, pour que la ligne critique reste en service pendant la maintenance.

Quelle forme convient dépend de combien coûte un jour d'arrêt pour l'entreprise. Nous chiffrons les deux et laissons les mathématiques décider.

## Weichai à cette taille

Les moteurs Weichai dans la gamme 400–500 kW sont courants pour les installations en puissance principale car le bloc est simple, mécanique et bien soutenu en Asie et en Afrique. La tolérance au carburant est bonne pour la qualité locale du gazole, et le réseau de pièces est dense. Pour une usine sur un marché en croissance, cette réparabilité est ce qui maintient la production en marche.

## Parlez-nous avant de spécifier

Si vous hésitez entre un raccordement au réseau et un groupe en puissance principale, envoyez-nous la liste des charges, les heures de fonctionnement par jour et le prix local du carburant. Nous ferons les calculs et vous montrerons quelle option gagne réellement sur cinq ans.
''',

'de': '''![Weichai 500kW schallgeschütztes Dieselaggregat in großer Kabine](/images/blog/blog-weichai-500kw-silent.jpg)

In vielen Fabrikprojekten kommt der Moment, wo der Käufer auf den Netzanschluss-Kostenvoranschlag blickt und eine Entscheidung trifft: entweder sechs Monate warten, bis der Versorger ein neues Kabel legt und die Anschlussgebühr zahlen, oder ein Dieselaggregat installieren, das die Hauptenergiequelle des Werks wird.

Wenn das passiert, hört der Generator auf, ein Backup zu sein, und wird zu einer Investition. Ein einzelnes Weichai-Schallschutzaggregat mit 500 kW (ca. 625 kVA) ist eine gängige Form für diese Entscheidung. Die Planung unterscheidet sich jedoch vom Kauf einer Notaggregate.

## Notbetrieb ist nicht Dauerbetrieb

Das Erste, was man verinnerlichen sollte: Ein 500-kW-Aggregat, das als *Dauerleistung* gekauft wird, ist eine andere Maschine als derselbe Kasten als Notaggregat.

- Notaggregate stehen 99% der Zeit still. Sie laufen ein paar Stunden im Jahr. Der Motor ist für diesen Zyklus ausgelegt.
- Daueraggregate laufen 8–24 Stunden am Tag. Sie sind die Hauptenergiequelle. Der Motor muss für Dauerbetrieb ausgelegt sein, mit dem richtigen Kraftstoffsystem, Kühlung und Schmierung.

Kaufen Sie ein Notaggregat als Daueraggregat, werden Sie es lange vor Erwartung überholen müssen. Kaufen Sie ein Daueraggregat als Notaggregat, haben Sie etwas mehr ausgegeben als nötig, aber die Maschine ist auf längere Lebensdauer gebaut.

## Lastfolge ist das ganze Spiel

Ein 500-kW-Aggregat übernimmt nicht in einer Sekunde die ganze Fabrik. Es übernimmt die Last in einer geplanten Reihenfolge:

1. **Erste 0–30 Sekunden:** Beleuchtung, Leitwarte, Sicherheitssysteme. Das Aggregat wärmt sich auf Nennspannung auf.
2. **Nächste Minute:** Kleinere Motoren, Förderbänder, Wasserpumpen, gestaffelt vom Controller gestartet.
3. **Nach drei Minuten:** Große Lasten — Luftkompressor, Kältemaschinen, Hauptproduktionsmotoren — nacheinander gestartet.

Ohne Reihenfolge zieht der erste große Motorstart die Spannung herunter und das Aggregat schaltet bei Überlast ab. Mit Reihenfolge fährt die Fabrik hoch wie am Netz.

Deshalb zählt der Controller. Ein billiger Dreifunktionscontroller, der nur startet und stoppt, reicht für ein Ganzfabrik-Daueraggregat nicht. Sie brauchen einen PLC-gesteuerten Controller, der die Startreihenfolge verwaltet und unwesentliche Lasten abwirft, wenn das Aggregat heiß läuft.

## Die Kraftstoff-Frage

Ein 500-kW-Aggregat verbrennt grob 90–110 Liter pro Stunde bei Durchschnittslast. Wenn es 12 Stunden am Tag läuft, sind das über tausend Liter am Tag.

Die Planung einer Ganzfabrik-Installation bedeutet die Planung des Kraftstoffs:

- Tagestank am Aggregat, 8–12 Stunden.
- Großtank im Hof, dimensioniert für eine Woche Laufzeit.
- Liefervertrag mit einem lokalen Diesel-Lieferanten, der den Standort pünktlich erreicht.

Den Großtank zu überspringen, ist, wie eine Dauerleistungsfabrik an einem Produktionstag wartend vor einem Tankwagen steht.

## Die Redundanz-Frage

Ein einzelnes 500-kW-Aggregat ist ein einzelner Ausfallpunkt. Für eine kleine Fabrik mag das akzeptabel sein: wenn das Aggregat zur Wartung ausfällt, pausiert die Produktion. Für eine Fabrik mit zu versendenden Aufträgen planen Käufer oft entweder:

- Zwei 300-kW-Aggregate parallel, die sich die Last teilen. Wenn eines ausfällt, trägt das andere die wesentliche Last.
- Ein 500-kW-Aggregat plus ein Notaggregat 250 kW, damit die kritische Linie während der Wartung läuft.

Welche Form passt, hängt davon ab, wie teuer ein Pausetag für das Geschäft ist. Wir kalkulieren beide und lassen die Mathematik entscheiden.

## Weichai in dieser Größe

Weichai-Motoren im Bereich 400–500 kW sind üblich für Dauerleistungsanlagen, weil der Block einfach, mechanisch und in ganz Asien und Afrika gut unterstützt ist. Die Kraftstofftoleranz ist gut für lokale Dieselqualität, und das Teilenetz ist dicht. Für eine Fabrik in einem Wachstumsmarkt ist diese Servicefreundlichkeit es, die die Produktion am Laufen hält.

## Sprechen Sie mit uns, bevor Sie spezifizieren

Wenn Sie sich zwischen einem Netzanschluss und einem Dauerleistungsaggregat entscheiden, senden Sie uns die Lastliste, die Laufstunden pro Tag und den lokalen Kraftstoffpreis. Wir rechnen nach und zeigen Ihnen, welche Option über fünf Jahre tatsächlich gewinnt.
''',

'pt': '''![Grupo diesel silencioso Weichai 500kW em canopy grande](/images/blog/blog-weichai-500kw-silent.jpg)

Há um momento em muitos projetos de fábrica quando o comprador olha para a cotação de conexão à rede e toma uma decisão: ou esperar seis meses pela concessionária estender um cabo novo e pagar a taxa de conexão, ou instalar um grupo a diesel que se torna a principal energia da planta.

Quando isso acontece, o gerador deixa de ser um backup e se torna um investimento. Um único grupo silencioso Weichai de 500 kW (cerca de 625 kVA) é uma forma comum para essa decisão. O planejamento, no entanto, é diferente de comprar uma unidade standby.

## Standby não é prime

A primeira coisa a internalizar: um grupo de 500 kW comprado como *potência primária* é uma máquina diferente da mesma caixa comprada como standby.

- Grupos standby ficam parados 99% do tempo. Rodam algumas horas por ano. O motor é dimensionado para esse ciclo de serviço.
- Grupos prime rodam de 8 a 24 horas por dia. São a principal fonte de energia. O motor deve ser dimensionado para serviço contínuo, com o sistema de combustível, refrigeração e lubrificação corretos.

Compre um grupo com classificação standby como prime e você o reconstruirá muito antes do esperado. Compre um grupo com classificação prime como standby e terá gasto um pouco mais que o necessário, mas a máquina é construída para vida mais longa.

## Sequenciamento de carga é todo o jogo

Um grupo de 500 kW não começa a carregar toda a fábrica em um segundo. Ele carrega em uma sequência projetada:

1. **Primeiros 0–30 segundos:** iluminação, escritório de controle, sistemas de segurança. O grupo esquenta até a tensão nominal.
2. **Próximo minuto:** motores menores, esteiras transportadoras, bombas d'água, ligados em ordem escalonada pelo controlador.
3. **Após três minutos:** grandes cargas — compressor de ar, chillers, motores principais de produção — ligados um a um.

Sem sequenciamento, a primeira partida do grande motor derruba a tensão e o grupo dispara em sobrecarga. Com sequenciamento, a fábrica sobe como subiria na rede.

É por isso que o controlador importa. Um controlador barato de três funções que só liga e desliga não é suficiente para um grupo prime de fábrica inteira. Você precisa de um controlador PLC que gerencie a sequência de partida e elimine cargas não essenciais se o grupo esquentar.

## A questão do combustível

Um grupo de 500 kW queima cerca de 90 a 110 litros por hora em carga média. Se rodar 12 horas por dia, são mais de mil litros por dia.

Planejar uma instalação de fábrica inteira significa planejar combustível:

- Tanque diário no grupo, 8–12 horas.
- Tanque bulk no pátio, dimensionado para uma semana de operação.
- Contrato de entrega com fornecedor local de diesel que consegue chegar ao local no prazo.

Pular o tanque bulk é como uma fábrica de potência primária se encontra esperando por um caminhão de combustível em um dia de produção.

## A questão da redundância

Um único grupo de 500 kW é um ponto único de falha. Para uma fábrica pequena, isso pode ser aceitável: quando o grupo está em manutenção, a produção pausa. Para uma fábrica com pedidos para embarcar, os compradores costumam planejar ou:

- Dois grupos de 300 kW em paralelo, dividindo a carga. Quando um está fora, o outro carrega a carga essencial.
- Um grupo de 500 kW mais uma unidade standby de 250 kW, para que a linha crítica fique no ar durante a manutenção.

Qual forma se encaixa depende de quão caro é um dia pausado para o negócio. Orçamos os dois e deixamos a matemática decidir.

## Weichai neste tamanho

Motores Weichai na faixa de 400–500 kW são comuns para instalações de potência primária porque o bloco é simples, mecânico e bem suportado em toda a Ásia e África. A tolerância ao combustível é boa para a qualidade local do diesel, e a rede de peças é densa. Para uma fábrica em um mercado em crescimento, essa reparabilidade é o que mantém a produção rodando.

## Fale conosco antes de especificar

Se você está decidindo entre uma conexão de rede e um grupo de potência primária, envie-nos a lista de cargas, as horas de operação por dia e o preço local do combustível. Faremos as contas e mostraremos qual opção realmente vence em cinco anos.
''',

'ar': '''![مجموعة ديزل كاتمة Weichai 500 كيلوواط في هيكل كبير](/images/blog/blog-weichai-500kw-silent.jpg)

هناك لحظة في العديد من مشاريع المصانع عندما ينظر المشتري إلى عرض سعر الربط الشبكي ويتخذ قراراً: إما الانتظار ستة أشهر حتى تمد شركة المرافق كابلاً جديداً ودفع رسوم الربط، أو تركيب مجموعة ديزل تصبح الطاقة الرئيسية للمصنع.

عندما يحدث ذلك، يتوقف المولد عن كونه احتياطياً ويصبح استثماراً. المجموعة الكاتمة الواحدة 500 كيلوواط (حوالي 625 كيلو فولت أمبير) القائمة على Weichai هي شكل شائع لهذا القرار. لكن التخطيط يختلف عن شراء وحدة احتياطية.

## الاحتياط ليس الرئيسي

أول شيء يجب استيعابه: مجموعة 500 كيلوواط تُشترى كـ *طاقة رئيسية* هي آلة مختلفة عن نفس الصندوق المُشترى كاحتياطي.

- المجموعات الاحتياطية تبقى خاملة 99% من الوقت. تعمل لبضع ساعات في السنة. المحرك مصنف لدورة الخدمة تلك.
- المجموعات الرئيسية تعمل 8 إلى 24 ساعة في اليوم. هي مصدر الطاقة الرئيسي. يجب أن يكون المحرك مصنفاً للخدمة المستمرة، مع نظام الوقود والتبريد والتشحيم المناسب.

اشترِ مجموعة مصنفة احتياطياً كرئيسية وستعيد بناءها قبل المتوقع بوقت طويل. اشترِ مجموعة مصنفة رئيسية كاحتياطية وستكون قد أنفقت أكثر قليلاً من اللازم، لكن الآلة مبنية لعمر أطول.

## تسلسل الأحمال هو اللعبة كلها

مجموعة 500 كيلوواط لا تبدأ بحمل المصنع كله في ثانية واحدة. تحمل الحمل بتسلسل مصمم:

1. **أول 0-30 ثانية:** الإضاءة، مكتب التحكم، أنظمة السلامة. تسخن المجموعة حتى الجهد المقدر.
2. **الدقيقة التالية:** محركات أصغر، سيور ناقلة، مضخات مياه، تُشغل بترتيب متداخل بواسطة المتحكم.
3. **بعد ثلاث دقائق:** أحمال كبيرة — ضاغط هواء، مبردات، محركات الإنتاج الرئيسية — تُشغل واحدة تلو الأخرى.

بدون تسلسل، أول بدء تشغيل محرك كبير يسحب الجهد للأسفل وتنطلق المجموعة على الحمل الزائد. مع التسلسل، يقلع المصنع كما يفعل على الشبكة.

لهذا يهم المتحكم. المتحكم الرخيص ثلاثي الوظائف الذي يشغل ويوقف فقط لا يكفي لمجموعة رئيسية لمصنع كامل. تحتاج إلى متحكم مدفوع بـ PLC يدير تسلسل البدء ويُلقي بالأحمال غير الضرورية إذا سخنت المجموعة.

## سؤال الوقود

مجموعة 500 كيلوواط تحرق تقريباً 90 إلى 110 لتر في الساعة عند الحمل المتوسط. إذا عملت 12 ساعة في اليوم، فهذا أكثر من ألف لتر في اليوم.

تخطيط منشأة مصنع كامل يعني تخطيط الوقود:

- خزان يومي على المجموعة، 8-12 ساعة.
- خزان رئيسي في الساحة، بحجم يكفي لأسبوع من التشغيل.
- عقد توريد مع مورد ديزل محلي يمكنه الوصول إلى الموقع في الموعد.

تخطي الخزان الرئيسي هو كيف تجد مصنع الطاقة الرئيسية نفسه ينتظر شاحنة وقود في يوم إنتاج.

## سؤال التكرار

مجموعة 500 كيلوواط واحدة هي نقطة فشل واحدة. بالنسبة لمصنع صغير قد يكون هذا مقبولاً: عندما تتوقف المجموعة للصيانة، يتوقف الإنتاج. بالنسبة لمصنع لديه طلبات للشحن، غالباً ما يخطط المشترون إما:

- مجموعتان 300 كيلوواط بالتوازي، تشاركان الحمل. عندما تتوقف واحدة، تحمل الأخرى الحمل الأساسي.
- مجموعة 500 كيلوواط بالإضافة إلى وحدة احتياطية 250 كيلوواط، لكي يبقى الخط الحرك قائماً أثناء الصيانة.

أي شكل يناسب يعتمد على مدى تكلفة اليوم المتوقف للعمل. نحن نسعّر كليهما ونترك الحساب يقرر.

## Weichai بهذا الحجم

محركات Weichai في نطاق 400-500 كيلوواط شائعة لمنشآت الطاقة الرئيسية لأن الكتلة بسيطة وميكانيكية ومدعومة جيداً في جميع أنحاء آسيا وأفريقيا. التسامح مع الوقود جيد لجودة الديزل المحلي، وشبكة قطع الغيار كثيفة. بالنسبة لمصنع في سوق نامٍ، فإن قابلية الخدمة هذه هي ما يبقي الإنتاج قائماً.

## تحدث معنا قبل أن تحدد المواصفات

إذا كنت تقرر بين الربط الشبكي ومجموعة طاقة رئيسية، أرسل لنا قائمة الأحمال، وساعات التشغيل يومياً، وسعر الوقود المحلي. سنجري الحسابات ونريك أي خيار يفوز فعلياً على مدى خمس سنوات.
''',

'tr': '''![Weichai 500kW büyük kabinli sessiz dizel jeneratör](/images/blog/blog-weichai-500kw-silent.jpg)

Birçok fabrika projesinde alıcının şebeke bağlantı teklifine baktığı ve karar verdiği bir an vardır: ya altı ay bekleyip kurumun yeni bir kablo çekmesini ve bağlantı ücretini ödemesini ya da tesisin ana gücü haline gelen bir dizel grup kurmasını.

Bu olduğunda, jeneratör yedek olmaktan çıkar ve bir yatırıma dönüşür. 500 kW'lık (yaklaşık 625 kVA) tek Weichai sessiz grup, bu kararın yaygın bir şeklidir. Ancak planlama, bir yedek ünite almaktan farklıdır.

## Yedek, prime değildir

Özümsenecek ilk şey: *prime güç* olarak alınan 500 kW'lık grup, yedek olarak alınan aynı kutudan farklı bir makinedir.

- Yedek gruplar zamanın %99'unu boşta geçirir. Yılda birkaç saat çalışır. Motor bu görev döngüsü için derecelendirilmiştir.
- Prime gruplar günde 8 ila 24 saat çalışır. Ana güç kaynağıdır. Motor, doğru yakıt sistemi, soğutma ve yağlama ile sürekli görev için derecelendirilmelidir.

Yedek dereceli bir grubu prime olarak satın alın ve beklenenden çok önce yeniden inşa edersiniz. Prime dereceli bir grubu yedek olarak satın alın ve gerektiğinden biraz fazla harcamış olursunuz, ama makine daha uzun ömür için inşa edilmiştir.

## Yük sıralaması tüm oyun

500 kW'lık bir grup bir saniyede tüm fabrikayı yüklenmez. Yükü tasarlanmış bir sırayla taşır:

1. **İlk 0–30 saniye:** aydınlatma, kontrol ofisi, güvenlik sistemleri. Grup nominal voltaja kadar ısınır.
2. **Sonraki dakika:** daha küçük motorlar, konveyör bantları, su pompaları, kontrolör tarafından kademeli sırada başlatılır.
3. **Üç dakika sonra:** büyük yükler — hava kompresörü, chillerlar, ana üretim motorları — birer birer başlatılır.

Sıralama olmadan, ilk büyük motor başlatması voltajı aşağı çeker ve grup aşırı yüklenmeden trip atar. Sıralama ile fabrika şebekede olacağı gibi ayağa kalkar.

Kontrolörün önemli olmasının nedeni budur. Sadece başlatıp duran ucuz üç fonksiyonlu kontrolör, tüm fabrika prime grubu için yeterli değildir. Başlatma sırasını yöneten ve grup ısınırsa gereksiz yükleri boşaltan PLC destekli bir kontrolöre ihtiyacınız vardır.

## Yakıt sorusu

500 kW'lık bir grup, ortalama yükte saatte kabaca 90 ila 110 litre yakar. Günde 12 saat çalışırsa, bu günde bin litreden fazla demektir.

Tüm fabrika kurulumunu planlamak, yakıtı planlamak anlamına gelir:

- Grup üzerinde günlük depo, 8–12 saat.
- Avluda haftalık çalışmaya boyutlandırılmış bulk depo.
- Sahaya zamanında ulaşabilen yerel bir dizel tedarikçisiyle teslimat sözleşmesi.

Bulk depoyu atlamak, bir prime güç fabrikasının bir üretim gününde yakıt kamyonu beklerken kalmasıdır.

## Yedeklilik sorusu

Tek 500 kW'lık grup tek bir arıza noktasıdır. Küçük bir fabrika için bu kabul edilebilir olabilir: grup bakımda olduğunda üretim duraklar. Gönderecek siparişleri olan bir fabrika için, alıcılar genellikle şunlardan birini planlar:

- Yükü paylaşan paralel iki 300 kW grup. Biri arızalandığında diğeri temel yükü taşır.
- Bir 500 kW grup artı 250 kW yedek ünite, bakım sırasında kritik hattın ayakta kalması için.

Hangi şeklin uyduğu, duraklayan bir günün iş için ne kadar pahalı olduğuna bağlıdır. İkisini de fiyatlandırırız ve matematiğe karar verdirtiriz.

## Bu boyutta Weichai

400–500 kW aralığındaki Weichai motorları, basit, mekanik blok ve Asya ile Afrika genelinde iyi desteklendiği için prime güç kurulumları için yaygındır. Yakıt toleransı yerel dizel kalitesi için iyidir ve parça ağı yoğundur. Büyüyen bir pazardaki bir fabrika için, üretimi ayakta tutan şey bu servis kolaylığıdır.

## Spec vermeden önce bizimle konuşun

Şebeke bağlantısı ile prime güç grubu arasında karar veriyorsanız, bize yük listesini, günlük çalışma saatlerini ve yerel yakıt fiyatını gönderin. Hesapları yapıp beş yıl içinde hangi seçeneğin gerçekten kazandığını göstereceğiz.
''',

'th': '''![ชุดดีเซลคงทนเสียง Weichai 500 กิโลวัตต์ในเปลือกขนาดใหญ่](/images/blog/blog-weichai-500kw-silent.jpg)

มีช่วงเวลาหนึ่งในโครงการโรงงานหลายแห่ง เมื่อผู้ซื้อมองไปที่ใบเสนอราคาการเชื่อมต่อไฟฟ้าและตัดสินใจ: รอหกเดือนให้การไฟฟ้าวางสายใหม่และจ่ายค่าเชื่อมต่อ หรือติดตั้งชุดดีเซลที่กลายเป็นพลังงานหลักของโรงงาน

เมื่อเกิดขึ้น เครื่องกำเนิดไฟฟ้าหยุดเป็นตัวสำรองและกลายเป็นการลงทุน ชุดคงทนเสียง Weichai 500 กิโลวัตต์เดียว (ประมาณ 625 kVA) เป็นรูปแบบทั่วไปสำหรับการตัดสินใจนั้น อย่างไรก็ตาม การวางแผนแตกต่างจากการซื้อหน่วยสำรอง

## สแตนด์บายไม่ใช่ไพรม์

สิ่งแรกที่ต้องซึมซับ: ชุด 500 กิโลวัตต์ที่ซื้อเป็น *พลังงานหลัก* เป็นเครื่องจักรอีกเครื่องหนึ่งจากกล่องเดียวกันที่ซื้อเป็นสแตนด์บาย

- ชุดสแตนด์บายว่าง 99% ของเวลา ทำงานไม่กี่ชั่วโมงต่อปี เครื่องยนต์ถูกจัดอันดับสำหรับรอบการทำงานนั้น
- ชุดไพร์มทำงาน 8 ถึง 24 ชั่วโมงต่อวัน เป็นแหล่งพลังงานหลัก เครื่องยนต์ต้องถูกจัดอันดับสำหรับการทำงานต่อเนื่อง ด้วยระบบเชื้อเพลิง ระบบระบายความร้อน และระบบหล่อลื่นที่ถูกต้อง

ซื้อชุดที่จัดอันดับสแตนด์บายเป็นไพร์ม และคุณจะต้องสร้างใหม่ก่อนที่คาดไว้นาน ซื้อชุดที่จัดอันดับไพร์มเป็นสแตนด์บาย และคุณใช้จ่ายมากกว่าที่จำเป็นเล็กน้อย แต่เครื่องถูกสร้างมาสำหรับอายุยืนกว่า

## การเรียงลำดับภาระคือทั้งเกม

ชุด 500 กิโลวัตต์ไม่ได้เริ่มรับภาระโรงงานทั้งหมดในหนึ่งวินาที มันรับภาระในลำดับที่ออกแบบ:

1. **0-30 วินาทีแรก:** แสงไฟ สำนักงานควบคุม ระบบความปลอดภัย ชุดอุ่นขึ้นจนถึงแรงดันไฟฟ้าที่กำหนด
2. **นาทีถัดไป:** มอเตอร์เล็กลง สายพานลำเลียง ปั๊มน้ำ สตาร์ทตามลำดับเว้นระยะโดยตัวควบคุม
3. **หลังสามนาที:** ภาระใหญ่ — คอมเพรสเซอร์อากาศ ชิลเลอร์ มอเตอร์ผลิตหลัก — สตาร์ททีละตัว

หากไม่มีการเรียงลำดับ การสตาร์ทมอเตอร์ใหญ่ครั้งแรกจะดึงแรงดันไฟฟ้าลงและชุดจะตัดโหลดเกิน หากมีการเรียงลำดับ โรงงานจะขึ้นมาอย่างที่จะขึ้นบนกริด

นี่คือเหตุผลที่ตัวควบคุมสำคัญ ตัวควบคุมราคาถูกสามฟังก์ชันที่แค่สตาร์ทและหยุดไม่เพียงพอสำหรับชุดไพร์มโรงงานทั้งหมด คุณต้องการตัวควบคุมที่ขับเคลื่อนด้วย PLC ซึ่งจัดการลำดับการสตาร์ทและปลดภาระที่ไม่จำเป็นหากชุดร้อนเกินไป

## คำถามเรื่องเชื้อเพลิง

ชุด 500 กิโลวัตต์เผาผลาญประมาณ 90 ถึง 110 ลิตรต่อชั่วโมงที่ภาระเฉลี่ย ถ้าทำงาน 12 ชั่วโมงต่อวัน นั่นคือมากกว่าหนึ่งพันลิตรต่อวัน

การวางแผนการติดตั้งโรงงานทั้งหมดหมายถึงการวางแผนเชื้อเพลิง:

- ถังประจำวันบนชุด 8-12 ชั่วโมง
- ถัง bulk ในลาน ขนาดสำหรับการทำงานหนึ่งสัปดาห์
- สัญญาจัดส่งกับผู้จัดจำหน่ายดีเซลท้องถิ่นที่สามารถมาถึงไซต์ได้ตรงเวลา

การข้ามถัง bulk คือวิธีที่โรงงานพลังงานหลักพบว่าตัวเองกำลังรอรถบรรทุกเชื้อเพลิงในวันที่ผลิต

## คำถามเรื่องความซ้ำซ้อน

ชุด 500 กิโลวัตต์เดียวคือจุดเดียวของความล้มเหลว สำหรับโรงงานขนาดเล็ก นี่อาจเป็นที่ยอมรับได้: เมื่อชุดหยุดเพื่อบำรุงรักษา การผลิตจะหยุดชั่วคราว สำหรับโรงงานที่มีคำสั่งซื้อเพื่อจัดส่ง ผู้ซื้อมักวางแผนอย่างใดอย่างหนึ่ง:

- ชุด 300 กิโลวัตต์สองตัวขนานกัน แบ่งภาระ เมื่อตัวหนึ่งเสีย อีกตัวหนึ่งรับภาระจำเป็น
- ชุด 500 กิโลวัตต์บวกหน่วยสำรอง 250 กิโลวัตต์ เพื่อให้สายสำคัญยังทำงานระหว่างการบำรุงรักษา

รูปแบบไหนเหมาะขึ้นอยู่กับว่าวันที่หยุดชั่วคราวมีราคาแพงแค่ไหนสำหรับธุรกิจ เราเสนอราคาทั้งสองและปล่อยให้คณิตศาสตร์ตัดสิน

## Weichai ที่ขนาดนี้

เครื่องยนต์ Weichai ในช่วง 400-500 กิโลวัตต์เป็นเรื่องปกติสำหรับการติดตั้งพลังงานหลัก เพราะบล็อกเรียบง่าย เป็นกล และได้รับการสนับสนุนอย่างดีทั่วเอเชียและแอฟริกา ความทนเชื้อเพลิงดีสำหรับคุณภาพดีเซลท้องถิ่น และเครือข่ายอะไหล่หนาแน่น สำหรับโรงงานในตลาดที่เติบโต ความสามารถในการซ่อมบำรุงนี้คือสิ่งที่ทำให้การผลิตดำเนินต่อ

## คุยกับเราก่อนที่คุณจะกำหนดสเปค

หากคุณกำลังตัดสินใจระหว่างการเชื่อมต่อกริดกับชุดพลังงานหลัก ส่งรายการภาระ ชั่วโมงทำงานต่อวัน และราคาเชื้อเพลิงท้องถิ่นมาให้เรา เราจะคำนวณและแสดงให้คุณเห็นว่าตัวเลือกไหนชนะจริงในห้าปี
''',

'vi': '''![Tổ máy diesel chống ồn Weichai 500kW trong canopy lớn](/images/blog/blog-weichai-500kw-silent.jpg)

Có một khoảnh khắc trong nhiều dự án nhà máy khi người mua nhìn vào báo giá kết nối lưới điện và đưa ra quyết định: hoặc chờ sáu tháng để tiện ích kéo cáp mới và trả phí kết nối, hoặc lắp đặt một tổ máy diesel trở thành nguồn điện chính của nhà máy.

Khi điều đó xảy ra, máy phát ngừng là dự phòng và trở thành một khoản đầu tư. Một tổ máy chống ồn Weichai 500 kW (khoảng 625 kVA) là hình thái phổ biến cho quyết định đó. Tuy nhiên, quy hoạch khác với mua một tổ máy dự phòng.

## Dự phòng không phải là chính

Điều đầu tiên cần thấm nhuần: một tổ máy 500 kW mua làm *công suất chính* là một máy khác với cùng một hộp mua làm dự phòng.

- Tổ máy dự phòng nằm không hoạt động 99% thời gian. Chúng chạy vài giờ mỗi năm. Động cơ được xếp hạng cho chu kỳ làm việc đó.
- Tổ máy chính chạy 8 đến 24 giờ mỗi ngày. Chúng là nguồn điện chính. Động cơ phải được xếp hạng cho nhiệm vụ liên tục, với hệ thống nhiên liệu, làm mát và bôi trơn phù hợp.

Mua tổ máy xếp hạng dự phòng làm chính và bạn sẽ xây dựng lại nó sớm hơn dự kiến. Mua tổ máy xếp hạng chính làm dự phòng và bạn đã chi nhiều hơn mức cần thiết một chút, nhưng máy được chế tạo cho tuổi thọ dài hơn.

## Tuần tự hóa tải là cả trò chơi

Một tổ máy 500 kW không bắt đầu chịu toàn bộ nhà máy trong một giây. Nó chịu tải theo một trình tự được thiết kế:

1. **0–30 giây đầu tiên:** chiếu sáng, văn phòng điều khiển, hệ thống an toàn. Tổ máy làm nóng lên đến điện áp định mức.
2. **Phút tiếp theo:** các động cơ nhỏ hơn, băng chuyền, bơm nước, khởi động theo thứ tự so le bởi bộ điều khiển.
3. **Sau ba phút:** các tải lớn — máy nén khí, chiller, động cơ sản xuất chính — khởi động từng cái một.

Nếu không có tuần tự, lần khởi động động cơ lớn đầu tiên kéo điện áp xuống và tổ máy ngắt do quá tải. Có tuần tự, nhà máy đi lên như khi trên lưới.

Đây là lý do bộ điều khiển quan trọng. Một bộ điều khiển rẻ tiền ba chức năng chỉ khởi động và dừng là không đủ cho một tổ máy chính cả nhà máy. Bạn cần một bộ điều khiển PLC quản lý trình tự khởi động và cắt bớt các tải không cần thiết nếu tổ máy chạy nóng.

## Câu hỏi về nhiên liệu

Một tổ máy 500 kW đốt khoảng 90 đến 110 lít mỗi giờ ở tải trung bình. Nếu chạy 12 giờ mỗi ngày, đó là hơn một nghìn lít mỗi ngày.

Quy hoạch một hệ thống cả nhà máy có nghĩa là quy hoạch nhiên liệu:

- Thùng ngày trên tổ máy, 8–12 giờ.
- Thùng kho ngoài sân, kích thước cho một tuần chạy.
- Hợp đồng giao hàng với nhà cung cấp diesel địa phương có thể đến công trường đúng hẹn.

Bỏ qua thùng kho là cách một nhà máy công suất chính thấy mình chờ xe bồn nhiên liệu vào một ngày sản xuất.

## Câu hỏi về dự phòng

Một tổ máy 500 kW là một điểm lỗi duy nhất. Đối với một nhà máy nhỏ, điều này có thể chấp nhận được: khi tổ máy dừng để bảo trì, sản xuất tạm dừng. Đối với một nhà máy có đơn hàng phải giao, người mua thường quy hoạch một trong hai:

- Hai tổ máy 300 kW song song, chia tải. Khi một cái dừng, cái kia chịu tải thiết yếu.
- Một tổ máy 500 kW cộng với một tổ máy dự phòng 250 kW, để dây chuyền quan trọng vẫn chạy trong khi bảo trì.

Hình thái nào phù hợp phụ thuộc vào việc một ngày tạm dừng đắt giá bao nhiêu đối với doanh nghiệp. Chúng tôi báo giá cả hai và để phép tính quyết định.

## Weichai ở kích thước này

Động cơ Weichai trong dải 400–500 kW phổ biến cho các hệ thống công suất chính vì khối đơn giản, cơ khí và được hỗ trợ tốt trên khắp châu Á và châu Phi. Dung sai nhiên liệu tốt cho chất lượng diesel địa phương, và mạng lưới phụ tùng dày đặc. Đối với một nhà máy ở thị trường đang tăng trưởng, khả năng bảo trì này là thứ giữ sản xuất chạy.

## Hãy nói chuyện với chúng tôi trước khi đặc tả

Nếu bạn đang quyết định giữa kết nối lưới điện và một tổ máy công suất chính, hãy gửi cho chúng tôi danh sách tải, số giờ chạy mỗi ngày và giá nhiên liệu địa phương. Chúng tôi sẽ tính toán và cho bạn thấy lựa chọn nào thực sự thắng trong năm năm.
''',

'id': '''![Grup diesel silent Weichai 500kW di kanopi besar](/images/blog/blog-weichai-500kw-silent.jpg)

Ada momen di banyak proyek pabrik ketika pembeli melihat penawaran penyambungan jaringan listrik dan mengambil keputusan: atau menunggu enam bulan sampai utilitas memasang kabel baru dan membayar biaya penyambungan, atau memasang grup diesel yang menjadi daya utama pabrik.

Ketika itu terjadi, generator berhenti menjadi cadangan dan menjadi investasi. Satu grup silent Weichai 500 kW (sekitar 625 kVA) adalah bentuk umum untuk keputusan itu. Namun perencanaannya berbeda dari membeli unit standby.

## Standby bukan prime

Hal pertama yang harus dipahami: grup 500 kW yang dibeli sebagai *daya primer* adalah mesin yang berbeda dari kotak yang sama yang dibeli sebagai standby.

- Grup standby berdiam diri 99% waktu. Mereka berjalan beberapa jam setahun. Mesin dinilai untuk siklus tugas itu.
- Grup prime berjalan 8 sampai 24 jam sehari. Mereka adalah sumber daya utama. Mesin harus dinilai untuk tugas kontinu, dengan sistem bahan bakar, pendinginan, dan pelumasan yang tepat.

Beli grup berperingkat standby sebagai prime dan Anda akan membangunnya kembali jauh sebelum yang diharapkan. Beli grup berperingkat prime sebagai standby dan Anda telah menghabiskan sedikit lebih dari yang diperlukan, tetapi mesin dibangun untuk umur lebih panjang.

## Urutan beban adalah seluruh permainan

Grup 500 kW tidak mulai memikul seluruh pabrik dalam satu detik. Ia memikul beban dalam urutan yang dirancang:

1. **0–30 detik pertama:** pencahayaan, kantor kontrol, sistem keselamatan. Grup menghangat hingga tegangan nominal.
2. **Menit berikutnya:** motor yang lebih kecil, sabuk konveyor, pompa air, dinyalakan dalam urutan bertahap oleh controller.
3. **Setelah tiga menit:** beban besar — kompresor udara, chiller, motor produksi utama — dinyalakan satu per satu.

Tanpa urutan, start motor besar pertama menarik tegangan turun dan grup trip pada kelebihan beban. Dengan urutan, pabrik naik seperti yang akan dilakukan di jaringan.

Inilah mengapa controller penting. Controller murah tiga fungsi yang hanya start dan stop tidak cukup untuk grup prime pabrik keseluruhan. Anda butuh controller yang digerakkan PLC yang mengelola urutan start dan melepas beban tidak penting jika grup berjalan panas.

## Pertanyaan bahan bakar

Grup 500 kW membakar sekitar 90 sampai 110 liter per jam pada beban rata-rata. Jika berjalan 12 jam sehari, itu lebih dari seribu liter sehari.

Merencanakan instalasi pabrik keseluruhan berarti merencanakan bahan bakar:

- Tangki harian pada grup, 8–12 jam.
- Tangki bulk di halaman, diukur untuk seminggu berjalan.
- Kontrak pengiriman dengan pemasok diesel lokal yang bisa mencapai lokasi tepat waktu.

Melewatkan tangki bulk adalah bagaimana pabrik daya primer menemukan dirinya menunggu truk bahan bakar di hari produksi.

## Pertanyaan redundansi

Satu grup 500 kW adalah satu titik kegagalan. Untuk pabrik kecil itu mungkin dapat diterima: ketika grup turun untuk perawatan, produksi berhenti. Untuk pabrik dengan pesanan untuk dikirim, pembeli sering merencanakan salah satu:

- Dua grup 300 kW paralel, berbagi beban. Ketika satu turun, yang lain memikul beban penting.
- Satu grup 500 kW ditambah unit standby 250 kW, agar jalur kritis tetap menyala selama perawatan.

Bentuk mana yang cocok tergantung pada seberapa mahal hari yang terhenti bagi bisnis. Kami memberikan harga keduanya dan membiarkan matematika memutuskan.

## Weichai pada ukuran ini

Mesin Weichai dalam rentang 400–500 kW umum untuk instalasi daya primer karena bloknya sederhana, mekanis, dan didukung baik di seluruh Asia dan Afrika. Toleransi bahan bakar baik untuk kualitas diesel lokal, dan jaringan suku cadang padat. Untuk pabrik di pasar yang tumbuh, keterlayanan inilah yang membuat produksi tetap berjalan.

## Bicaralah dengan kami sebelum Anda spesifikasi

Jika Anda memutuskan antara penyambungan jaringan dan grup daya primer, kirimkan daftar beban, jam operasi per hari, dan harga bahan bakar lokal. Kami akan menghitung dan menunjukkan pilihan mana yang benar-benar menang dalam lima tahun.
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
