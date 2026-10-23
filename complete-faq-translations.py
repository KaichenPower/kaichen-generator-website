import json
import os

base_dir = "D:/projects/kaichen-generator-website/content/i18n"

# 读取英语版本的 FAQ 作为源
with open(os.path.join(base_dir, "en.json"), 'r', encoding='utf-8') as f:
    en_data = json.load(f)

en_faqs = en_data['faqPage']['faqs']

# 8个语言的 FAQ 翻译
translations = {
    "fr": {
        "nav": {"faq": "FAQ"},
        "faqPage": {
            "title": "Questions Fréquemment Posées",
            "subtitle": "Réponses directes sur la garantie, le dimensionnement, les délais, type silencieux vs ouvert, puissance de secours vs principale, support export et après-vente.",
            "askQuestion": "Posez-nous une question",
            "faqs": [
                {
                    "q": "Quelle garantie offrez-vous sur un groupe électrogène neuf ?",
                    "a": "Un groupe neuf standard bénéficie d'une garantie de 1 an ou 1 000 heures (selon la première éventualité), mesurée à partir de la mise en service ou de la date de facture. Le moteur, l'alternateur et le panneau de contrôle peuvent être étendus à 2 ans sous notre option de garantie étendue."
                },
                {
                    "q": "Quel est le délai de livraison ?",
                    "a": "Les plages de puissance standard (20–500 kVA) sont généralement en stock et expédiées sous 7–15 jours. Les configurations personnalisées, les systèmes parallèles haute tension ou les carports spéciaux prennent généralement 25–45 jours."
                },
                {
                    "q": "Comment choisir la bonne taille de générateur pour mon site ?",
                    "a": "Additionnez les kW en fonctionnement de chaque charge que le groupe doit supporter en même temps, puis ajoutez 20–30 % de marge pour le courant de démarrage du moteur et l'expansion future. En règle générale, un petit bureau ou magasin nécessite 20–50 kVA, un étage d'usine ou un hôtel de taille moyenne nécessite 100–300 kVA, et un centre de données ou un hôpital passe à 500 kVA et plus."
                },
                {
                    "q": "Type silencieux ou ouvert – lequel dois-je choisir ?",
                    "a": "Choisissez un groupe à capot silencieux si l'unité se trouve près des personnes (bureau, hôpital, zone résidentielle, toit) et que vous devez maintenir le bruit autour de 65–75 dB(A) à 7 mètres. Choisissez un groupe de type ouvert si l'unité va dans une salle des machines dédiée qui dispose déjà d'un traitement acoustique."
                },
                {
                    "q": "Quelle est la différence entre puissance de secours et puissance principale ?",
                    "a": "L'énergie de secours est destinée à un usage d'urgence occasionnel lors des coupures de réseau, généralement jusqu'à 200 heures par an à 70 % de charge moyenne, sans surcharge autorisée. L'énergie principale (continue) fonctionne comme source d'alimentation principale du site, 24 heures sur 24, avec une surcharge de 10 % autorisée pendant une heure sur douze."
                },
                {
                    "q": "Prendiez-vous en charge la tension, la fréquence et les environnements spéciaux personnalisés ?",
                    "a": "Oui. Nous construisons des groupes 50 Hz / 60 Hz, de 220V monophasé jusqu'à 11kV triphasé, et adaptons le groupe pour haute altitude (déclassement), climats froids (chauffage de chemise d'eau, liquide de refroidissement arctique), sites côtiers (traitement anticorrosion) et environnements poussiéreux (préfiltres)."
                },
                {
                    "q": "Pouvez-vous exporter à l'étranger et gérer la documentation ?",
                    "a": "Nous avons un département export au Centre d'Innovation de Yangzhou et avons expédié vers l'Asie du Sud-Est, le Moyen-Orient, l'Afrique, l'Amérique du Sud et l'Europe de l'Est. Nous fournissons la facture commerciale, la liste de colisage, le connaissement, les certificats CE/ISO, le rapport d'essai et (sur demande) un rapport d'inspection tiers de SGS, BV ou TUV."
                },
                {
                    "q": "À quoi ressemble la réponse après-vente ?",
                    "a": "Nous maintenons plus de 2 000 points de service agréés dans toute la Chine. Le même jour, les ingénieurs arrivent sur site en 2–4 heures dans les villes, 4–8 heures dans la province et dans les 24 heures dans les autres provinces. Les acheteurs étrangers bénéficient d'une assistance vidéo à distance, d'un kit de pièces de rechange et des contacts des partenaires locaux."
                },
                {
                    "q": "L'installation et la formation des opérateurs sont-elles incluses ?",
                    "a": "Les groupes standard sont livrés avec un guide vidéo gratuit. L'installation sur site, la mise en service et la formation pratique des opérateurs (démarrage/arrêt, reconnaissance des alarmes, entretien de routine) sont disponibles en tant que service payant."
                },
                {
                    "q": "Testez-vous chaque groupe avant expédition ?",
                    "a": "Oui. Chaque groupe fonctionne sur notre banc de charge numérique de 2 MW selon une séquence en quatre étapes – 20 %, 50 %, 75 % et 100 % de charge nominale – pendant au moins 2 heures au total. Tout le test est enregistré en vidéo et partagé avec vous avant que le groupe ne quitte l'usine."
                }
            ]
        }
    },
    "de": {
        "nav": {"faq": "FAQ"},
        "faqPage": {
            "title": "Häufig Gestellte Fragen",
            "subtitle": "Klare Antworten zu Garantie, Dimensionierung, Lieferzeit, schallisoliert vs offen, Notstrom vs Dauerleistung, Exportunterstützung und After-Sales.",
            "askQuestion": "Stellen Sie uns eine Frage",
            "faqs": [
                {
                    "q": "Welche Garantie bieten Sie für einen neuen Generator an?",
                    "a": "Ein neuer Standardgenerator hat 1 Jahr oder 1.000 Betriebsstunden Garantie (je nachdem, was zuerst eintritt), gemessen ab Inbetriebnahme oder Rechnungsdatum. Motor, Generator und Schaltschrank können auf 2 Jahre erweitert werden durch unsere verlängerte Garantieoption."
                },
                {
                    "q": "Wie lange ist die Lieferzeit?",
                    "a": "Standardleistungen (20–500 kVA) sind normalerweise auf Lager und werden innerhalb von 7–15 Tagen versendet. Individuelle Konfigurationen, Hochspannungs-Parallelsysteme oder spezielle Schallschutzgehäuse benötigen normalerweise 25–45 Tage."
                },
                {
                    "q": "Wie wähle ich die richtige Generatorgröße für meinen Standort?",
                    "a": "Addieren Sie die laufende kW jeder Last, die das Aggregat gleichzeitig tragen muss, und addieren Sie dann 20–30 % Marge für Motoranlaufstrom und zukünftige Erweiterung. Als Faustregel gilt: Ein kleines Büro oder Geschäft benötigt 20–50 kVA, eine Fabrikhalle oder ein mittelgroßes Hotel benötigt 100–300 kVA, und ein Rechenzentrum oder Krankenhaus geht auf 500 kVA und darüber."
                },
                {
                    "q": "Schallisoliert oder offen – welchen soll ich wählen?",
                    "a": "Wählen Sie ein schallisoliertes Aggregat, wenn die Einheit in der Nähe von Menschen steht (Büro, Krankenhaus, Wohngebiet, Dach) und Sie den Lärm auf etwa 65–75 dB(A) in 7 Metern Entfernung halten müssen. Wählen Sie ein offenes Aggregat, wenn die Einheit in einen eigenen Maschinenraum geht, der bereits schallgedämmt ist."
                },
                {
                    "q": "Was ist der Unterschied zwischen Notstrom und Dauerleistung?",
                    "a": "Notstrom ist für gelegentlichen Notfalleinsatz bei Netzausfällen gedacht, typischerweise bis zu 200 Stunden pro Jahr bei 70 % durchschnittlicher Last, ohne Überlastung. Dauerleistung (Kontinuitätsbetrieb) versorgt den Standort als Hauptstromquelle, 24 Stunden am Tag, mit 10 % Überlastung für eine Stunde von zwölf."
                },
                {
                    "q": "Unterstützen Sie kundenspezifische Spannung, Frequenz und Sonderumgebungen?",
                    "a": "Ja. Wir bauen 50 Hz / 60 Hz Aggregate von 220V einphasig bis 11kV dreiphasig und passen das Aggregat für Höhenlagen (Leistungsreduzierung), kalte Klimate (Wasserbadheizung, Arktis-Kühlmittel), Küstenstandorte (Korrosionsschutz) und staubige Umgebungen (Vorfilter) an."
                },
                {
                    "q": "Können Sie ins Ausland exportieren und die Dokumentation übernehmen?",
                    "a": "Wir haben eine Exportabteilung im Yangzhou Innovation Center und haben nach Südostasien, Naher Osten, Afrika, Südamerika und Osteuropa geliefert. Wir stellen Handelsrechnung, Packliste, Seefrachtbrief, CE/ISO-Zertifikate, Prüfbericht und (auf Wunsch) einen Inspektionsbericht eines Dritten von SGS, BV oder TUV zur Verfügung."
                },
                {
                    "q": "Wie sieht der After-Sales-Service aus?",
                    "a": "Wir unterhalten mehr als 2.000 autorisierte Servicestellen in ganz China. Am selben Tag erreichen Ingenieure den Standort in 2–4 Stunden in Städten, 4–8 Stunden innerhalb der Provinz und innerhalb von 24 Stunden in anderen Provinzen. Ausländische Käufer erhalten Fern-Videounterstützung, ein Ersatzteilset und Kontakte zu lokalen Partnern."
                },
                {
                    "q": "Sind Installation und Bedienerschulung enthalten?",
                    "a": "Standardaggregate werden mit kostenloser Videoanleitung geliefert. Installation vor Ort, Inbetriebnahme und praktische Bedienerschulung (Start/Stopp, Alarmerkennung, routinemäßige Wartung) sind als kostenpflichtige Dienstleistung verfügbar."
                },
                {
                    "q": "Testen Sie jedes Aggregat vor dem Versand?",
                    "a": "Ja. Jedes Aggregat läuft auf unserer 2 MW digitalen Lastbank durch eine vierstufige Sequenz – 20 %, 50 %, 75 % und 100 % Nennlast – für insgesamt mindestens 2 Stunden. Der gesamte Test wird auf Video aufgezeichnet und vor dem Verlassen des Werks mit Ihnen geteilt."
                }
            ]
        }
    },
    "pt": {
        "nav": {"faq": "Perguntas Frequentes"},
        "faqPage": {
            "title": "Perguntas Frequentes",
            "subtitle": "Respostas diretas sobre garantia, dimensionamento, prazo de entrega, tipo silencioso vs aberto, potência reserva vs principal, suporte de exportação e pós-venda.",
            "askQuestion": "Faça-nos uma pergunta",
            "faqs": [
                {
                    "q": "Qual garantia vocês oferecem em um gerador novo?",
                    "a": "Um gerador novo padrão tem garantia de 1 ano ou 1.000 horas (o que ocorrer primeiro), medida a partir da comissionamento ou data da fatura. Motor, alternador e painel de controle podem ser estendidos para 2 anos sob nossa opção de garantia estendida."
                },
                {
                    "q": "Qual é o prazo de entrega?",
                    "a": "Faixas de potência padrão (20–500 kVA) geralmente estão em estoque e são enviadas em 7–15 dias. Configurações personalizadas, sistemas paralelos de alta tensão ou capotas especiais geralmente levam 25–45 dias."
                },
                {
                    "q": "Como escolher o tamanho certo de gerador para o meu local?",
                    "a": "Some os kW em funcionamento de cada carga que o gerador deve suportar ao mesmo tempo, depois adicione 20–30 % de margem para corrente de partida do motor e expansão futura. Como regra geral, um pequeno escritório ou loja precisa de 20–50 kVA, um piso de fábrica ou um hotel de médio porte precisa de 100–300 kVA, e um data center ou hospital vai para 500 kVA e acima."
                },
                {
                    "q": "Tipo silencioso ou aberto – qual devo escolher?",
                    "a": "Escolha um gerador com capota silenciosa se a unidade estiver perto de pessoas (escritório, hospital, área residencial, telhado) e você precisar manter o ruído em torno de 65–75 dB(A) a 7 metros. Escolha um gerador aberto se a unidade for para uma sala de máquinas dedicada que já tem tratamento acústico."
                },
                {
                    "q": "Qual é a diferença entre potência reserva e potência principal?",
                    "a": "Energia reserva é para uso emergencial ocasional durante quedas de energia, geralmente até 200 horas por ano a 70 % de carga média, sem sobrecarga permitida. Energia principal (contínua) funciona como fonte de energia principal do local, 24 horas por dia, com 10 % de sobrecarga permitida por uma hora em doze."
                },
                {
                    "q": "Vocês suportam tensão, frequência e ambientes especiais personalizados?",
                    "a": "Sim. Construímos geradores 50 Hz / 60 Hz, de 220V monofásico até 11kV trifásico, e adaptamos o gerador para alta altitude (redução de potência), climas frios (aquecedor de camisa de água, refrigerante ártico), locais costeiros (tratamento anticorrosão) e ambientes empoeirados (pré-filtros)."
                },
                {
                    "q": "Vocês podem exportar para o exterior e lidar com a documentação?",
                    "a": "Temos um departamento de exportação no Centro de Inovação de Yangzhou e enviamos para Sudeste Asiático, Oriente Médio, África, América do Sul e Europa Oriental. Fornecemos fatura comercial, lista de embalagem, conhecimento de embarque, certificados CE/ISO, relatório de teste e (sob consulta) um relatório de inspeção de terceiros da SGS, BV ou TUV."
                },
                {
                    "q": "Como é o atendimento pós-venda?",
                    "a": "Mantemos mais de 2.000 pontos de serviço autorizados em toda a China. No mesmo dia, engenheiros chegam ao local em 2–4 horas nas cidades, 4–8 horas dentro da província e em 24 horas em outras províncias. Compradores estrangeiros recebem suporte remoto por vídeo, um kit de peças sobressalentes e contatos de parceiros locais."
                },
                {
                    "q": "A instalação e o treinamento do operador estão incluídos?",
                    "a": "Geradores padrão são enviados com guia de vídeo gratuita. Instalação no local, comissionamento e treinamento prático do operador (partida/parada, reconhecimento de alarmes, manutenção de rotina) estão disponíveis como serviço pago."
                },
                {
                    "q": "Vocês testam cada gerador antes do envio?",
                    "a": "Sim. Cada gerador funciona em nossa banco de carga digital de 2 MW através de uma sequência de quatro passos – 20 %, 50 %, 75 % e 100 % de carga nominal – por pelo menos 2 horas no total. Todo o teste é gravado em vídeo e compartilhado com você antes que o gerador saia da fábrica."
                }
            ]
        }
    },
    "ar": {
        "nav": {"faq": "الأسئلة الشائعة"},
        "faqPage": {
            "title": "الأسئلة الشائعة",
            "subtitle": "إجابات مباشرة حول الضمان، تحديد الحجم، مهلة التسليم، النوع الكاتم للصوت مقابل المفتوح، طاقة الاحتياط مقابل الطاقة الرئيسية، دعم التصدير وخدمة ما بعد البيع.",
            "askQuestion": "اسألنا سؤالاً",
            "faqs": [
                {
                    "q": "ما هو الضمان الذي تقدمونه على مولد جديد؟",
                    "a": "يأتي المولد القياسي الجديد بضمان لمدة سنة واحدة أو 1000 ساعة عمل (أيهما يأتي أولاً)، مقاساً من تاريخ التشغيل أو تاريخ الفاتورة. يمكن تمديد الضمان على المحرك والمولد ولوحة التحكم إلى سنتين ضمن خيار الضمان الممتد لدينا."
                },
                {
                    "q": "ما هي مدة التسليم؟",
                    "a": "عادةً ما تكون نطاقات الطاقة القياسية (20–500 كيلو فولت أمبير) متوفرة في المخزون وتُشحن خلال 7–15 يوماً. عادةً ما تستغرق التكوينات المخصصة أو الأنظمة المتوازية عالية الجهد أو المظلات الخاصة 25–45 يوماً."
                },
                {
                    "q": "كيف أختار حجم المولد المناسب لموقعي؟",
                    "a": "اجمع الكيلوواط التشغيلي لكل حمل يجب أن يحمله المولد في نفس الوقت، ثم أضف 20–30 % هامش لتيار بدء تشغيل المحرك والتوسع المستقبلي. كقاعدة عامة، يحتاج مكتب صغير أو متجر إلى 20–50 كيلو فولت أمبير، وطابق مصنع أو فندق متوسط الحجم يحتاج إلى 100–300 كيلو فولت أمبير، ومركز بيانات أو مستشفى يصل إلى 500 كيلو فولت أمبير وما فوق."
                },
                {
                    "q": "النوع الكاتم للصوت أم المفتوح – أيهما يجب أن أختار؟",
                    "a": "اختر مجموعة مظلة كاتمة للصوت إذا كانت الوحدة تقع بالقرب من الأشخاص (مكتب، مستشفى، منطقة سكنية، سطح) وتحتاج إلى الحفاظ على الضوضاء حوالي 65–75 ديسيبل (A) على بعد 7 أمتار. اختر مجموعة من النوع المفتوح إذا كانت الوحدة تذهب إلى غرفة آلات مخصصة لديها بالفعل معالجة صوتية."
                },
                {
                    "q": "ما هو الفرق بين طاقة الاحتياط والطاقة الرئيسية؟",
                    "a": "طاقة الاحتياط مخصصة للاستخدام الطارئ العرضي أثناء انقطاع الشبكة، عادةً حتى 200 ساعة في السنة عند 70 % متوسط الحمل، دون السماح بالحمل الزائد. الطاقة الرئيسية (المستمرة) تشغل الموقع كمصدر الطاقة الرئيسي، 24 ساعة في اليوم، مع السماح بحمل زائد 10 % لمدة ساعة واحدة من كل اثني عشر."
                },
                {
                    "q": "هل تدعمون الجهد والتردد والبيئات الخاصة المخصصة؟",
                    "a": "نعم. نحن نبني مجموعات 50 هرتز / 60 هرتز، من 220 فولت أحادي الطور حتى 11 كيلوفولت ثلاثي الطور، ونصمم المجموعة خصيصاً للمرتفعات العالية (تخفيض القدرة)، والمناخات الباردة (سخان سترة الماء، سائل التبريد القطبي)، والمواقع الساحلية (معالجة مقاومة للتآكل) والبيئات المتربة (مرشحات مسبقة)."
                },
                {
                    "q": "هل يمكنكم التصدير إلى الخارج والتعامل مع الوثائق؟",
                    "a": "لدينا قسم تصدير في مركز الابتكار بيانغتشو وقمنا بالشحن إلى جنوب شرق آسيا والشرق الأوسط وأفريقيا وأمريكا الجنوبية وأوروبا الشرقية. نحن نقدم الفاتورة التجارية وقائمة التعبئة وبوليصة الشحن وشهادات CE/ISO وتقرير الاختبار و (عند الطلب) تقرير فحص طرف ثالث من SGS أو BV أو TUV."
                },
                {
                    "q": "كيف تبدو استجابة خدمة ما بعد البيع؟",
                    "a": "نحن نحافظ على أكثر من 2000 نقطة خدمة معتمدة في جميع أنحاء الصين. في نفس اليوم، يصل المهندسون إلى الموقع خلال 2–4 ساعات في المدن، و4–8 ساعات داخل المقاطعة، وخلال 24 ساعة في المقاطعات الأخرى. يحصل المشترون الأجانب على دعم فيديو عن بعد، وطقم قطع غيار، وجهات اتصال للشركاء المحليين."
                },
                {
                    "q": "هل يتم تضمين التثبيت وتدريب المشغل؟",
                    "a": "يتم شحن المجموعات القياسية مع دليل فيديو مجاني. التثبيت في الموقع والتشغيل التجريبي والتدريب العملي للمشغل (بدء/إيقاف، التعرف على الإنذارات، الصيانة الدورية) متاحة كخدمة مدفوعة."
                },
                {
                    "q": "هل تختبرون كل مجموعة قبل الشحن؟",
                    "a": "نعم. تعمل كل مجموعة على بنك الحمل الرقمي الخاص بنا بقدرة 2 ميجاوات من خلال تسلسل من أربع خطوات – 20 %، 50 %، 75 % و 100 % من الحمل المقنن – لمدة لا تقل عن ساعتين إجمالاً. يتم تسجيل الاختبار بأكمله على فيديو ومشاركته معك قبل أن تغادر المجموعة المصنع."
                }
            ]
        }
    },
    "tr": {
        "nav": {"faq": "SSS"},
        "faqPage": {
            "title": "Sıkça Sorulan Sorular",
            "subtitle": "Garanti, boyutlandırma, teslim süresi, sessiz tip vs açık tip, yedek güç vs ana güç, ihracat desteği ve satış sonrası hizmet hakkında doğrudan cevaplar.",
            "askQuestion": "Bize bir sorun sorun",
            "faqs": [
                {
                    "q": "Yeni bir jeneratörde hangi garantiyi sunuyorsunuz?",
                    "a": "Standart bir yeni set, devreye alma veya fatura tarihinden itibaren ölçülen, 1 yıl veya 1.000 saat garantiye sahiptir (hangisi önce gelirse). Motor, alternatör ve kontrol paneli, genişletilmiş garanti seçeneğimiz kapsamında 2 yıla kadar uzatılabilir."
                },
                {
                    "q": "Teslim süresi ne kadar?",
                    "a": "Standart güç aralıkları (20–500 kVA) genellikle stokta bulunur ve 7–15 gün içinde gönderilir. Özel konfigürasyonlar, yüksek voltajlı paralel sistemler veya özel kaportalar genellikle 25–45 gün sürer."
                },
                {
                    "q": "Sitem için doğru jeneratör boyutunu nasıl seçerim?",
                    "a": "Setin aynı anda taşıması gereken her yükün çalışma kW'sını toplayın, ardından motor başlangıç akımı ve gelecekteki genişleme için %20–30 pay ekleyin. Genel bir kural olarak, küçük bir ofis veya dükkan 20–50 kVA, bir fabrika katı veya orta boy bir otel 100–300 kVA, bir veri merkezi veya hastane 500 kVA ve üzerine çıkar."
                },
                {
                    "q": "Sessiz tip mi açık tip mi – hangisini seçmeliyim?",
                    "a": "Ünite insanların yakınında bulunuyorsa (ofis katı, hastane, yerleşim alanı, çatı) ve gürültüyü 7 metrede 65–75 dB(A) civarında tutmanız gerekiyorsa sessiz kaplamalı set seçin. Ünite, akustik işlemesi zaten yapılmış özel bir makine odasına gidecekse açık tip set seçin."
                },
                {
                    "q": "Yedek güç ve ana güç arasındaki fark nedir?",
                    "a": "Yedek güç, şebeke kesintileri sırasında ara sıra acil kullanım içindir, tipik olarak yılda 200 saate kadar %70 ortalama yükte, aşırı yük olmadan. Ana (sürekli) güç, sitenin ana güç kaynağı olarak 7/24 çalışır, on iki saatte bir saat boyunca %10 aşırı yüke izin verilir."
                },
                {
                    "q": "Özel voltaj, frekans ve özel ortamları destekliyor musunuz?",
                    "a": "Evet. 50 Hz / 60 Hz setleri, 220V tek fazlıdan 11kV üç fazlıya kadar üretiyoruz ve seti yüksek irtifa (güç düşürme), soğuk iklimler (gömlek suyu ısıtıcısı, arktik soğutucu), sahil bölgeleri (korozyon önleme) ve tozlu ortamlar (ön filtreler) için özelleştiriyoruz."
                },
                {
                    "q": "Yurt dışına ihracat yapabilir ve belgeleri halledebilir misiniz?",
                    "a": "Yangzhou İnovasyon Merkezi'nde bir ihracat departmanımız var ve Güneydoğu Asya, Orta Doğu, Afrika, Güney Amerika ve Doğu Avrupa'ya sevk ettik. Ticari fatura, paketleme listesi, konşimento, CE/ISO sertifikaları, test raporu ve (talep üzerine) SGS, BV veya TUV'dan üçüncü taraf inceleme raporu sağlıyoruz."
                },
                {
                    "q": "Satış sonrası destek nasıl?",
                    "a": "Çin genelinde 2.000'den fazla yetkili servis noktası bulunduruyoruz. Aynı gün, mühendisler şehirlerde 2–4 saat, il içinde 4–8 saat ve diğer illerde 24 saat içinde sahaya ulaşır. Yurt dışı alıcılar uzaktan video desteği, yedek parça kiti ve yerel ortak iletişim bilgileri alır."
                },
                {
                    "q": "Kurulum ve operatör eğitimi dahil mi?",
                    "a": "Standart setler ücretsiz video rehberi ile gönderilir. Sahada kurulum, devreye alma ve uygulamalı operatör eğitimi (başlat/durdurma, alarm tanıma, rutin bakım) ücretli bir hizmet olarak mevcuttur."
                },
                {
                    "q": "Her seti sevkıyattan önce test ediyor musunuz?",
                    "a": "Evet. Her set, 2 MW dijital yük bankamızda dört aşamalı bir sekansla – %20, %50, %75 ve %100 anma yükü – toplam en az 2 saat boyunca çalışır. Tüm test video kaydedilir ve set fabrikadan ayrılmadan önce sizinle paylaşılır."
                }
            ]
        }
    },
    "th": {
        "nav": {"faq": "คำถามที่พบบ่อย"},
        "faqPage": {
            "title": "คำถามที่พบบ่อย",
            "subtitle": "คำตอบตรงไปตรงมาเกี่ยวกับการรับประกัน ขนาดที่เหมาะสม ระยะเวลาจัดส่ง แบบเก็บเสียง vs แบบเปิด พลังงานสำรอง vs พลังงานหลัก การสนับสนุนการส่งออก และบริการหลังการขาย",
            "askQuestion": "ถามคำถามกับเรา",
            "faqs": [
                {
                    "q": "คุณให้การรับประกันเครื่องกำเนิดไฟฟ้าใหม่เป็นระยะเวลาเท่าใด?",
                    "a": "ชุดเครื่องมาตรฐานใหม่มีการรับประกัน 1 ปี หรือ 1,000 ชั่วโมง (อย่างใดอย่างหนึ่งจะถึงก่อน) นับจากวันที่เริ่มใช้งานหรือวันที่ออกใบแจ้งหนี้ เครื่องยนต์ เครื่องกำเนิดไฟฟ้า และแผงควบคุมสามารถขยายเวลาเป็น 2 ปีได้ภายใต้ตัวเลือกการรับประกันแบบขยายของเรา"
                },
                {
                    "q": "ระยะเวลาจัดส่งนานแค่ไหน?",
                    "a": "ช่วงกำลังไฟมาตรฐาน (20–500 kVA) มักมีในสต็อกและจัดส่งภายใน 7–15 วัน การกำหนดค่าแบบกำหนดเอง ระบบขนานแรงดันสูง หรือหลังคาพิเศษ โดยทั่วไปจะใช้เวลา 25–45 วัน"
                },
                {
                    "q": "ฉันจะเลือกขนาดเครื่องกำเนิดไฟฟ้าที่เหมาะสมสำหรับสถานที่ของฉันได้อย่างไร?",
                    "a": "รวม kW การทำงานของทุกภาระที่ชุดต้องรับพร้อมกัน จากนั้นเพิ่มระยะเผื่อ 20–30 % สำหรับกระแสสตาร์ทมอเตอร์และการขยายในอนาคต โดยทั่วไปแล้ว สำนักงานขนาดเล็กหรือร้านค้าต้องการ 20–50 kVA, โรงงานหรือโรงแรมขนาดกลางต้องการ 100–300 kVA และศูนย์ข้อมูลหรือโรงพยาบาลต้องการ 500 kVA ขึ้นไป"
                },
                {
                    "q": "แบบเก็บเสียงหรือแบบเปิด – ฉันควรเลือกแบบไหน?",
                    "a": "เลือกชุดแบบมีหลังคาเก็บเสียงหากหน่วยอยู่ใกล้ผู้คน (ชั้นสำนักงาน โรงพยาบาล ย่านที่อยู่อาศัย หลังคา) และคุณต้องการรักษาระดับเสียงรบกวนประมาณ 65–75 เดซิเบล (A) ที่ระยะ 7 เมตร เลือกชุดแบบเปิดหากหน่วยจะไปในห้องเครื่องเฉพาะที่มีการจัดการเสียงอยู่แล้ว"
                },
                {
                    "q": "พลังงานสำรองและพลังงานหลักต่างกันอย่างไร?",
                    "a": "พลังงานสำรองมีไว้สำหรับใช้งานฉุกเฉินเป็นครั้งคราวระหว่างไฟฟ้าดับ โดยทั่วไปสูงสุด 200 ชั่วโมงต่อปีที่ภาระเฉลี่ย 70 % โดยไม่อนุญาตให้มีการโอเวอร์โหลด พลังงานหลัก (ต่อเนื่อง) ทำงานเป็นแหล่งจ่ายไฟหลักของสถานที่ ตลอด 24 ชั่วโมง โดยอนุญาตให้มีโอเวอร์โหลด 10 % เป็นเวลาหนึ่งชั่วโมจากสิบสองชั่วโมง"
                },
                {
                    "q": "คุณรองรับแรงดันไฟฟ้า ความถี่ และสภาพแวดล้อมพิเศษแบบกำหนดเองหรือไม่?",
                    "a": "ใช่ เราผลิตชุด 50 Hz / 60 Hz ตั้งแต่ 220V เฟสเดียวไปจนถึง 11kV สามเฟส และปรับแต่งชุดสำหรับที่สูง (ลดกำลัง), สภาพอากาศหนาวเย็น (เครื่องทำน้ำอุ่น, น้ำหล่อเย็นอาร์กติก), สถานที่ชายฝั่ง (การป้องกันการกัดกร่อน) และสภาพแวดล้อมที่มีฝุ่น (ตัวกรองก่อน)"
                },
                {
                    "q": "คุณสามารถส่งออกไปต่างประเทศและจัดการเอกสารได้หรือไม่?",
                    "a": "เรามีแผนกส่งออกที่ศูนย์นวัตกรรมหยางโจว และได้จัดส่งไปยังเอเชียตะวันออกเฉียงใต้ ตะวันออกกลาง แอฟริกา อเมริกาใต้ และยุโรปตะวันออก เราจัดทำใบแจ้งหนี้การค้า รายการบรรจุภัณฑ์ ใบตราส่งสินค้า ใบรับรอง CE/ISO รายงานการทดสอบ และ (ตามคำขอ) รายงานการตรวจสอบจากบุคคลที่สามจาก SGS, BV หรือ TUV"
                },
                {
                    "q": "บริการหลังการขายเป็นอย่างไร?",
                    "a": "เรามีจุดบริการที่ได้รับอนุญาตมากกว่า 2,000 แห่งทั่วประเทศจีน ในวันเดียวกัน วิศวกรจะมาถึงสถานที่ภายใน 2–4 ชั่วโมงในเขตเมือง 4–8 ชั่วโมงภายในจังหวัด และภายใน 24 ชั่วโมงในจังหวัดอื่นๆ ผู้ซื้อต่างประเทศจะได้รับการสนับสนุนทางวิดีโอระยะไกล ชุดอะไหล่ และข้อมูลติดต่อพันธมิตรในท้องถิ่น"
                },
                {
                    "q": "รวมการติดตั้งและการฝึกอบรมผู้ปฏิบัติงานหรือไม่?",
                    "a": "ชุดมาตรฐานจัดส่งพร้อมคู่มือวิดีโอฟรี การติดตั้งในสถานที่ การเริ่มการทำงาน และการฝึกอบรมผู้ปฏิบัติงานภาคปฏิบัติ (สตาร์ท/หยุด การรู้จำสัญญาณเตือน การบำรุงรักษาตามปกติ) มีให้บริการเป็นค่าบริการ"
                },
                {
                    "q": "คุณทดสอบทุกชุดก่อนจัดส่งหรือไม่?",
                    "a": "ใช่ ทุกชุดทำงานบนธนาคารโหลดดิจิทัล 2 MW ของเราผ่านลำดับสี่ขั้นตอน – 20 %, 50 %, 75 % และ 100 % ของภาระพิกัด – เป็นเวลาอย่างน้อย 2 ชั่วโมงโดยรวม การทดสอบทั้งหมดถูกบันทึกเป็นวิดีโอและแชร์กับคุณก่อนที่ชุดจะออกจากโรงงาน"
                }
            ]
        }
    },
    "vi": {
        "nav": {"faq": "Câu hỏi thường gặp"},
        "faqPage": {
            "title": "Câu Hỏi Thường Gặp",
            "subtitle": "Câu trả lời thẳng thắn về bảo hành, kích thước, thời gian giao hàng, kiểu cách âm vs kiểu mở, điện dự phòng vs điện chính, hỗ trợ xuất khẩu và dịch vụ sau bán hàng.",
            "askQuestion": "Hãy đặt câu hỏi với chúng tôi",
            "faqs": [
                {
                    "q": "Bạn cung cấp bảo hành gì cho một máy phát điện mới?",
                    "a": "Máy tiêu chuẩn mới có bảo hành 1 năm hoặc 1.000 giờ (tùy điều kiện nào đến trước), tính từ ngày vận hành hoặc ngày hóa đơn. Động cơ, máy phát điện và bảng điều khiển có thể được gia hạn lên 2 năm theo tùy chọn bảo hành mở rộng của chúng tôi."
                },
                {
                    "q": "Thời gian giao hàng là bao lâu?",
                    "a": "Các dải công suất tiêu chuẩn (20–500 kVA) thường có sẵn trong kho và giao hàng trong 7–15 ngày. Cấu hình tùy chỉnh, hệ thống song song điện áp cao hoặc mái che đặc biệt thường mất 25–45 ngày."
                },
                {
                    "q": "Làm thế nào để chọn kích thước máy phát điện phù hợp cho địa điểm của tôi?",
                    "a": "Cộng kW hoạt động của mọi tải mà bộ máy phải chịu cùng lúc, sau đó thêm 20–30 % biên độ cho dòng khởi động động cơ và mở rộng trong tương lai. Theo quy tắc thông thường, một văn phòng nhỏ hoặc cửa hàng cần 20–50 kVA, một nhà xưởng hoặc khách sạn cỡ trung bình cần 100–300 kVA, và một trung tâm dữ liệu hoặc bệnh viện cần 500 kVA trở lên."
                },
                {
                    "q": "Kiểu cách âm hay kiểu mở – tôi nên chọn kiểu nào?",
                    "a": "Chọn bộ máy có mái che cách âm nếu máy đặt gần người (tầng văn phòng, bệnh viện, khu dân cư, mái nhà) và bạn cần giữ ồn khoảng 65–75 dB(A) ở khoảng cách 7 mét. Chọn bộ kiểu mở nếu máy đi vào phòng máy chuyên dụng đã có xử lý âm thanh."
                },
                {
                    "q": "Sự khác biệt giữa điện dự phòng và điện chính là gì?",
                    "a": "Điện dự phòng dùng cho mục đích khẩn cấp không thường xuyên khi mất lưới điện, thường tối đa 200 giờ mỗi năm ở tải trung bình 70 %, không cho phép quá tải. Điện chính (liên tục) chạy địa điểm như nguồn điện chính, 24 giờ một ngày, cho phép quá tải 10 % trong một giờ trong mười hai giờ."
                },
                {
                    "q": "Bạn có hỗ trợ điện áp, tần số và môi trường đặc biệt tùy chỉnh không?",
                    "a": "Có. Chúng tôi chế tạo bộ máy 50 Hz / 60 Hz, từ 220V pha đơn đến 11kV ba pha, và tùy chỉnh bộ máy cho độ cao (giảm công suất), khí hậu lạnh (bộ làm nóng nước áo, chất làm mát Bắc Cực), địa điểm ven biển (xử lý chống ăn mòn) và môi trường bụi bặm (bộ lọc trước)."
                },
                {
                    "q": "Bạn có thể xuất khẩu ra nước ngoài và xử lý tài liệu không?",
                    "a": "Chúng tôi có bộ phận xuất khẩu tại Trung tâm Đổi mới Dương Châu và đã giao hàng đến Đông Nam Á, Trung Đông, Châu Phi, Nam Mỹ và Đông Âu. Chúng tôi cung cấp hóa đơn thương mại, danh sách đóng gói, vận đơn, chứng chỉ CE/ISO, báo cáo thử nghiệm và (theo yêu cầu) báo cáo kiểm tra bên thứ ba từ SGS, BV hoặc TUV."
                },
                {
                    "q": "Dịch vụ sau bán hàng như thế nào?",
                    "a": "Chúng tôi duy trì hơn 2.000 điểm dịch vụ được ủy quyền trên toàn Trung Quốc. Trong cùng ngày, kỹ sư đến nơi trong 2–4 giờ ở thành phố, 4–8 giờ trong tỉnh và trong vòng 24 giờ ở các tỉnh khác. Người mua ở nước ngoài nhận được hỗ trợ video từ xa, bộ phụ tùng liên hệ và địa điểm đối tác địa phương."
                },
                {
                    "q": "Bao gồm lắp đặt và đào tạo người vận hành chứ?",
                    "a": "Bộ tiêu chuẩn được giao kèm hướng dẫn video miễn phí. Lắp đặt tại chỗ, vận hành thử và đào tạo thực hành người vận hành (khởi động/dừng, nhận biết báo động, bảo dưỡng định kỳ) có sẵn dưới dạng dịch vụ trả phí."
                },
                {
                    "q": "Bạn có kiểm tra từng bộ trước khi giao hàng không?",
                    "a": "Có. Mỗi bộ chạy trên ngân hàng tải điện tử 2 MW của chúng tôi qua chu trình bốn bước – 20 %, 50 %, 75 % và 100 % tải định mức – tổng cộng ít nhất 2 giờ. Toàn bộ bài kiểm tra được ghi video và chia sẻ với bạn trước khi bộ rời khỏi nhà máy."
                }
            ]
        }
    },
    "id": {
        "nav": {"faq": "FAQ"},
        "faqPage": {
            "title": "Pertanyaan yang Sering Diajukan",
            "subtitle": "Jawaban langsung tentang garansi, ukuran, waktu tunggu, tipe sunyi vs terbuka, daya cadangan vs daya utama, dukungan ekspor dan purna jual.",
            "askQuestion": "Ajukan Pertanyaan kepada Kami",
            "faqs": [
                {
                    "q": "Garansi apa yang Anda tawarkan pada genset baru?",
                    "a": "Genset standar baru memiliki garansi 1 tahun atau 1.000 jam (mana yang lebih dulu), dihitung sejak commissioning atau tanggal faktur. Mesin, alternator dan panel kontrol dapat diperpanjang hingga 2 tahun di bawah opsi garansi diperpanjang kami."
                },
                {
                    "q": "Berapa lama waktu tunggu?",
                    "a": "Rentang daya standar (20–500 kVA) biasanya ada dalam stok dan dikirim dalam 7–15 hari. Konfigurasi kustom, sistem paralel tegangan tinggi atau kanopi khusus biasanya memakan waktu 25–45 hari."
                },
                {
                    "q": "Bagaimana cara memilih ukuran genset yang tepat untuk lokasi saya?",
                    "a": "Jumlahkan kW operasi dari setiap beban yang harus ditahan genset secara bersamaan, kemudian tambahkan 20–30 % margin untuk arus start motor dan ekspansi di masa depan. Sebagai aturan praktis, kantor kecil atau toko membutuhkan 20–50 kVA, lantai pabrik atau hotel menengah membutuhkan 100–300 kVA, dan pusat data atau rumah sakit membutuhkan 500 kVA ke atas."
                },
                {
                    "q": "Tipe sunyi atau tipe terbuka – mana yang harus saya pilih?",
                    "a": "Pilih genset kanopi sunyi jika unit berada dekat dengan orang (lantai kantor, rumah sakit, area perumahan, atap) dan Anda perlu menjaga kebisingan sekitar 65–75 dB(A) pada jarak 7 meter. Pilih genset tipe terbuka jika unit masuk ke ruang mesin khusus yang sudah memiliki perlakuan akustik."
                },
                {
                    "q": "Apa perbedaan antara daya cadangan dan daya utama?",
                    "a": "Daya cadangan untuk penggunaan darurat sesekali saat pemadaman jaringan, biasanya hingga 200 jam per tahun pada beban rata-rata 70 %, tanpa overload yang diizinkan. Daya utama (berkelanjutan) menjalankan lokasi sebagai sumber daya utama, 24 jam sehari, dengan 10 % overload diizinkan selama satu jam dalam dua belas jam."
                },
                {
                    "q": "Apakah Anda mendukung tegangan, frekuensi, dan lingkungan khusus kustom?",
                    "a": "Ya. Kami membuat genset 50 Hz / 60 Hz, dari 220V satu fasa hingga 11kV tiga fasa, dan menyesuaikan genset untuk dataran tinggi (penurunan daya), iklim dingin (pemanas jaket air, cairan pendingin Arktik), lokasi pesisir (perlakuan anti-korosi) dan lingkungan berdebu (filter awal)."
                },
                {
                    "q": "Bisakah Anda mengekspor ke luar negeri dan menangani dokumentasi?",
                    "a": "Kami memiliki departemen ekspor di Pusat Inovasi Yangzhou dan telah mengirim ke Asia Tenggara, Timur Tengah, Afrika, Amerika Selatan dan Eropa Timur. Kami menyediakan faktur komersial, daftar pengepakan, bill of lading, sertifikat CE/ISO, laporan uji dan (atas permintaan) laporan inspeksi pihak ketiga dari SGS, BV atau TUV."
                },
                {
                    "q": "Bagaimana tanggapan layanan purna jual?",
                    "a": "Kami memelihara lebih dari 2.000 titik layanan resmi di seluruh Tiongkok. Pada hari yang sama, insinyur tiba di lokasi dalam 2–4 jam di kota-kota, 4–8 jam dalam provinsi dan dalam 24 jam di provinsi lain. Pembeli luar negeri mendapatkan dukungan video jarak jauh, kit suku cadang dan kontak mitra lokal."
                },
                {
                    "q": "Apakah instalasi dan pelatihan operator sudah termasuk?",
                    "a": "Genset standar dikirim dengan panduan video gratis. Instalasi di lokasi, commissioning dan pelatihan operator praktis (start/stop, pengenalan alarm, perawatan rutin) tersedia sebagai layanan berbayar."
                },
                {
                    "q": "Apakah Anda menguji setiap genset sebelum pengiriman?",
                    "a": "Ya. Setiap genset berjalan di bank beban digital 2 MW kami melalui urutan empat langkah – 20 %, 50 %, 75 % dan 100 % beban terukur – selama minimal 2 jam total. Seluruh tes direkam dalam video dan dibagikan kepada Anda sebelum genset meninggalkan pabrik."
                }
            ]
        }
    }
}

for lang, data in translations.items():
    filepath = os.path.join(base_dir, f"{lang}.json")
    with open(filepath, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    
    # Update nav.faq
    json_data['nav']['faq'] = data['nav']['faq']
    
    # Update faqPage
    json_data['faqPage'] = data['faqPage']
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    
    print(f"Updated {lang}")
