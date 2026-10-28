---
title: "Dieselgenerator für die Notstromversorgung von Krankenhäusern: Auslegungsleitfaden"
date: "2026-10-28"
excerpt: "So dimensionieren Sie einen Dieselgenerator für Krankenhaus-Notstrom: Lastliste, kVA-Berechnung, Motoranlauf, Kraftstoffautonomie, Redundanz und Lastbankprüfung."
image: "/images/blog/hospital-generator-sizing.jpg"
---

![Schallgedämpfter Dieselgenerator für Krankenhaus-Notstrom in unserem Werk in Yangzhou](/images/blog/hospital-generator-sizing.jpg)

Ein Netzausfall im Krankenhaus ist keine Unannehmlichkeit. Innerhalb von Sekunden verliert der OP sein Licht, die Beatmungsgeräte auf der Intensivstation fallen auf Akkus zurück, die Minuten statt Stunden halten, die Kühlschränke der Blutbank beginnen über 6 °C zu steigen, die Aufzüge bleiben mit Patienten zwischen den Etagen stehen, und die Rufanlage wird dunkel.

Deshalb wird ein **Dieselgenerator für Krankenhaus-Notstrom** anders ausgelegt als ein Generator für eine Fabrik oder eine Baustelle. Er ist nicht „das größte Aggregat, das ins Budget passt“, sondern eine sicherheitsrelevante Maschine, deren Leistung, Anlaufverhalten, Kraftstoffautonomie, Akustik und Prüfprotokolle gegenüber einem Akkreditierungsprüfer belegbar sein müssen.

Dieser Leitfaden folgt der tatsächlichen Auslegungsreihenfolge, die wir bei Krankenhausprojekten anwenden: Lastliste erstellen, mit den nötigen Korrekturen in kVA umrechnen, Motoranlauf prüfen, dann Kraftstoff, Redundanz, Schall und Prüfumfang festlegen. Die Zahlen stammen aus unseren Datenblättern der KC-Serie, einschließlich zweier realer Aggregate in Krankenhausklasse.

## 1. Was der Generator im Krankenhaus tatsächlich versorgt

Die Elektroinstallation eines Krankenhauses ist in der Regel in eine Normalversorgung und einen oder mehrere Sicherheitsstromkreise (Essential Bus) aufgeteilt. Nur die Sicherheitsstromkreise laufen über den Generator. Diese Grenze richtig zu ziehen, ist die halbe Arbeit.

| Lastgruppe | Typischer Inhalt | Bedeutung für die Auslegung |
|---|---|---|
| Personensicherheit | OP- und Intensivbeleuchtung, Brandmeldeanlage, Entrauchung, Sicherheitsbeleuchtung, Medizalgas-Alarme | Umschaltung in etwa 10 Sekunden, nie abwerfbar |
| Kritisch | Intensiv- und Neonatologiegeräte, Dialyse, Kühlung der Blutbank, Kühlkette der Apotheke, Laborinkubatoren, IT und Rufanlage | Spannungsstabilität wichtiger als Rohleistung |
| Einrichtung | Aufzüge, Wasserpumpen, Feuerlöschpumpe, Lüftung, Sterilisation, teils Küche und Wäscherei | Der Motoranlauf bestimmt, nicht die Dauerleistung |
| Optional | Steckdosen der Stationen, Standardklimatisierung, Teile der Küche | Meist nicht aufgeschaltet oder bei Überlast abgeworfen |

Daraus folgen zwei praktische Regeln. Erstens: nicht das ganze Krankenhaus auf den Generator legen, wenn Budget und Kraftstoffspeicher das nicht tragen — die meisten Projekte führen 40–60 % der Anschlusslast über den Sicherheitsstromkreis. Zweitens: Motorlasten als Anlaufproblem behandeln, nicht als Dauerleistungsproblem; ein 15-kW-Aufzugsmotor kann ein bis zwei Sekunden lang das Fünf- bis Siebenfache seines Nennstroms ziehen.

Das Regelwerk unterscheidet sich nach Land — NFPA 99 und NFPA 110 in den USA, HTM 06-01 in Großbritannien, IEC 60364-7-710 für Medizinbereiche in Europa und vielen Exportmärkten. In Details weichen sie ab, im Kern stimmen sie überein: definierter Sicherheitsstromkreis, definierte Umschaltzeit, definierte Kraftstoffdauer und dokumentierte wiederkehrende Prüfungen. Klären Sie die lokale Fassung, bevor Sie die kVA festschreiben.

## 2. Erst die Lastliste, dann die kVA

Jede Diskussion über die Generatorleistung im Krankenhaus ist in Wahrheit eine Diskussion über die Lastliste. Erstellen Sie sie in einer Tabelle, Stromkreis für Stromkreis.

Erfassen Sie je Position vier Angaben: kW auf dem Typenschild, Leistungsfaktor, Gleichzeitigkeitsfaktor und Anlaufart (direkt, Stern-Dreieck, Sanftanlasser, Frequenzumrichter).

Beispiel für ein Allgemeinkrankenhaus mit 200 Betten, bei dem Kältemaschinen, Küche und Wäscherei am Sicherheitsstromkreis hängen. Es sind Planungswerte, kein Ersatz für den eigenen Übersichtsplan:

| Last | Angeschlossen kW | Gleichzeitigkeitsfaktor | Dauerleistung kW |
|---|---|---|---|
| OP, Intensiv, Sicherheitsbeleuchtung, Brandschutzsysteme | 120 | 1,0 | 120 |
| Intensivgeräte, Blutbank, Apotheke, IT | 90 | 1,0 | 90 |
| Aufzüge (4 × 15 kW) | 60 | 0,6 | 36 |
| Kältemaschine (eine am Sicherheitsstromkreis) | 90 | 1,0 | 90 |
| Pumpen, Wasseraufbereitung, Feuerlöschpumpe | 55 | 1,0 | 55 |
| Küche und Wäscherei, teilweise | 60 | 1,0 | 60 |
| **Summe Dauerleistung** | | | **451** |

Ein Diversitätsfaktor von 0,9 ergibt rund **406 kW**. Dazu kommt Reserve für Erweiterung — ein Krankenhaus ergänzt Bildgebung, Betten, Klimatisierung —, weshalb 20 % realistisch sind: **487 kW**. Das nächstliegende Standardaggregat ist eine Einheit mit **500 kW / 625 kVA**.

Danach prüfen Sie den Anlauf. Startet die Kältemaschine direkt mit sechsfachem Strom, während der OP bereits Last hat, muss das Aggregat diese Stufe aufnehmen, ohne dass der Spannungseinbruch Medizingeräte abschaltet. Fällt die Prüfung durch, ist die Antwort nicht automatisch ein größerer Generator, sondern ein Sanftanlasser oder Umrichter an der Kältemaschine — meist billiger als 200 kW mehr Alternator.

## 3. Die Formel und die vier Korrekturen

Die Grundumrechnung ist einfach:

**kVA = kW ÷ Leistungsfaktor**

Mit dem Standardwert 0,8 induktiv unserer 50-Hz-Aggregate benötigen 400 kW Dauerlast 500 kVA Alternatorleistung — vor jeder Korrektur. Danach greifen vier Korrekturen.

**Erweiterungsreserve.** 15–25 % für ein neues Krankenhaus, denn niemand legt für die heutige Bettenzahl aus.

**Motoranlauf und Laststufen.** Der transiente Spannungseinbruch muss innerhalb dessen bleiben, was die Medizintechnik verträgt. Unsere KC-Datenblätter geben vor: transienter Spannungsabweichung ≤ 15 %, Spannungsregelung im Beharrungszustand ≤ 0,5 %, transiente Frequenzabweichung ≤ 0,5 %, Wiederkehr von Spannung und Frequenz ≤ 3 Sekunden. Genau das erlebt ein Intensivmonitor während der Umschaltung.

**Derating am Standort.** Ein bei 40 °C ausgelegtes Aggregat verliert bei 45 °C Leistung und im Höhenlagenbetrieb mehr. Ist der Maschinenraum heiß, weil der Kühler in eine Ecke bläst, wird entweder derating angewandt oder der Luftweg korrigiert.

**Betriebsart.** Standby-Nennung (begrenzte Stunden, keine Überlastfähigkeit) gegenüber Prime-Nennung (Dauerbetrieb, 10 % Überlast für eine Stunde). Ein Krankenhaus, das während einer Netzreparatur acht Stunden auf dem Aggregat fährt, ist Standby; ein Krankenhaus mit täglichen Ausfällen ist Prime und muss so spezifiziert werden.

## 4. Zwei reale Referenzpunkte

Abstrakte Hinweise sind leicht zu schreiben und schwer anzuwenden. Hier zwei Aggregate, die wir für Krankenhausprojekte bauen, mit Werten direkt aus den KC-Datenblättern.

| Parameter | KC-YC200 | KC-YC1600 |
|---|---|---|
| Nenn- / Reserveleistung | 200 kW / 220 kW | 1.600 kW / 1.760 kW |
| Spannung / Strom | 380/220 V, 360 A | 380/220 V, 2.880 A |
| Frequenz, Leistungsfaktor | 50 Hz, 0,8 induktiv | 50 Hz, 0,8 induktiv |
| Motor | Yuchai YC6MK350L-D20, 235 / 258,5 kW | Yuchai YC16VTD2700-D30, 1.805 / 1.985 kW |
| Zylinder / Hubraum | Reihe 6, 10,34 L, 123 × 145 mm | V16, 52,26 L, 152 × 180 mm |
| Aufladung / Regelung | Turbolader mit Ladeluftkühler, elektronisch | Turbolader mit Ladeluftkühler, elektronisch |
| Kraftstoffverbrauch | 200 g/kWh | 200 g/kWh |
| Alternator | KCI-200, bürstenlos, AVR, IP23, Klasse H, Kupfer | KCI-1600, bürstenlos, AVR, IP23, Klasse H, Kupfer |
| Abmessungen (L × B × H) | 3.000 × 1.100 × 1.750 mm | 5.500 × 2.200 × 2.700 mm |
| Gewicht | 2.800 kg | 15.800 kg (Richtwert) |
| Schall (LP7M) | 102 dB(A) | 102 dB(A) |

**Wann die 200-kW-Klasse passt.** Praxen, ambulante Operationszentren, kleine Krankenhäuser und Bildgebungsanbauten, deren Sicherheitsstromkreis auf OP-Beleuchtung, Intensivgeräte, Brandschutzsysteme, IT und zwei Aufzüge begrenzt ist und deren Kältemaschine an der Normalversorgung bleibt. Mit 2.800 kg und 3 m Länge lässt sich das Aggregat auf einem Hubwagen in einen Keller-Maschinenraum bringen — entscheidend bei einer Sanierung mit 1,2 m Türbreite.

**Wann die 1.600-kW-Klasse passt.** Regional- und Lehrkrankenhäuser, deren Sicherheitsstromkreis tatsächlich zentrale Kältemaschinen, Küche, Wäscherei, Bildgebung und 10–20 Aufzüge umfasst. Bei 15.800 kg und 5,5 m braucht es einen echten Maschinenraum, eine Betonplatte oder ein Fundament auf Erdgleiche, einen Kranplan und in der Regel zwei Aggregate in Parallelbetrieb statt eines.

Zwischen beiden Größen liegen Zwischenstufen; entscheidend ist, dass das Datenblatt so vollständig ist, dass der Planer die Werte direkt in sein Elektromodell übernehmen kann.

## 5. Kraftstoffautonomie: die 72-Stunden-Frage

Kraftstoff ist der Punkt, an dem Krankenhaus-Spezifikationen am häufigsten durch eine Prüfung fallen, weil der Verbrauch pro kWh angegeben wird und die Umrechnung vergessen wird.

Mit 200 g/kWh und Diesel bei etwa 0,84 kg/L:

**Liter pro Stunde = Nennleistung kW × 0,2 ÷ 0,84**

| Last (KC-YC200) | Kraftstoff pro Stunde | Pro 24 h | Pro 72 h |
|---|---|---|---|
| 100 % (200 kW) | 47,6 L/h | 1.143 L | 3.429 L |
| 50 % Mittel (100 kW) | 23,8 L/h | 571 L | 1.714 L |
| 25 % Mittel (50 kW) | 11,9 L/h | 286 L | 857 L |

Ein 200-kW-Aggregat mit realistischer mittlerer Halblast braucht also rund **1.700 L für 72 Stunden**. Legen Sie einen Haupttank von 2.000 L aus, bleibt Reserve plus nicht nutzbares Volumen. Beim 1.600-kW-Aggregat bei Halblast sind es etwa **4.570 L pro 24 Stunden**; deshalb erhalten große Krankenhäuser einen erdverlegten oder in einer Auffangwanne stehenden Großtank samt Brennstoffpflege-Vertrag statt eines Rahmentanks.

Drei Details, die Prüfer ansehen: ein **Tagesbehälter** für 8 Betriebsstunden (damit ein Problem am Haupttank das Aggregat nicht sofort stoppt), **Auffangvolumen von 110 %** und **Hoch-/Tiefstandsmeldungen** auf die Gebäudeleittechnik. In der Kraftstoffleitung ein feuerwiderstandsfähiges Absperrventil am Tankausgang, und niemals eine Führung durch das Treppenhaus.

## 6. Redundanz, Parallelbetrieb und Umschaltung

Ein einzelner Generator ist ein einzelner Ausfallpunkt. Krankenhäuser akzeptieren das im Neubau selten.

| Schema | Bedeutung | Typischer Einsatz |
|---|---|---|
| N | Ein Aggregat für die Sicherheitslast | Praxen, kleine Krankenhäuser |
| N+1 | Ein zusätzliches Aggregat, das die Last bei Ausfall übernehmen kann | Allgemeinkrankenhäuser, 3 × 500 kW für 1.000 kW |
| 2N | Zwei vollständig unabhängige Versorgungen mit getrennten Räumen | Lehrkrankenhäuser, große Standorte |

Parallelbetrieb bringt mehr als Redundanz: zwei Aggregate bei 60 % statt eines bei 100 % senken Verbrauch und Nachtgeräusch, und eines lässt sich warten, während das andere die Last trägt. Unsere Steuerungen unterstützen Lastverteilung, isochrone Lastverteilung und automatische Synchronisierung, mit Sammelschienentrenner zur Freischaltung eines Aggregats.

Bei der Umschaltung legen Sie die Umschaltzeit früh fest. Für Personensicherheitskreise werden meist etwa 10 Sekunden erwartet; OP und Intensiv überbrücken diese Lücke mit USV oder statischem Umschalter, statt vom Generator sofortige Bereitschaft zu verlangen. Prüfen Sie die gesamte Sequenz — Netzausfall, ATS-Signal, Anlassen, Spannungsaufbau, Schließen des Leistungsschalters, Lastübernahme — auf dem Prüfstand, nicht in der Nacht des Ausfalls.

## 7. Schall, Standort und Nachbarschaft

Beide Aggregate der Tabelle sind offene Rahmenausführungen mit 102 dB(A) in 7 Metern am Referenzpunkt LP7M. Das ist laut, etwa in der Größenordnung einer Kettensäge. Akzeptabel in einem gut gedämmten Maschinenraum oder auf einem abgelegenen Gelände, inakzeptabel 30 Meter vor einem Stationsfenster.

Optionen nach Kosten:

- **Schallschutzhaube** — bringt ein Aggregat typisch in den Bereich 70–75 dB(A) in 7 m.
- **Raumdämmung** — akustische Auskleidung, dichte Türen, schwimmender Estrich und korrekt dimensionierte Zu- und Abluftschalldämpfer. Bei großen Aggregaten ist der Raum meist der günstigere Weg zu einem strengen Grenzwert.
- **Standort** — Kühlerausblas und Abgasleitung von der Stationsfassade wegführen und die Schornsteinhöhe gegen das nächste zu öffnende Fenster prüfen.

Klären Sie die örtlichen Grenzwerte vor der Wahl, sie unterscheiden sich stark; in vielen Rechtsordnungen gelten nachts etwa 45–55 dB(A) am nächsten maßgeblichen Immissionsort. Verlassen Sie sich bei einem 1,6-MW-Aggregat nicht auf eine Haube allein — das reicht nicht.

## 8. Montagedetails, die über den Erfolg entscheiden

Sie machen aus einem korrekten Datenblatt eine funktionierende Anlage:

- **Kühlluft.** Der Kühler braucht freien Zutritt und einen kanalgeführten Austritt ins Freie. Ein Maschinenraum mit Lüftungsgitter in Briefkastengröße führt zum Derating und zur Überhitzung des Alternators.
- **Abgasgegendruck.** Lange Wege, enge Bögen und zu kleine Schalldämpfer erhöhen den Gegendruck und kosten Leistung. Planen Sie mit dem maximal zulässigen Gegendruck des Herstellers.
- **Schwingungsisolierung.** Feder- oder Gummilager unter dem Rahmen, flexible Abgaskompensatoren und eine flexible Kraftstoffanbindung. Ohne sie wandert der Schall über die Decke in die Stationen darüber.
- **Kabelbemessung.** Nach Nennstrom bei tatsächlicher Umgebungstemperatur, Leistungs- und Steuerkabel in getrennten Trassen.
- **Erdung und Neutralleiter.** Die Netzform mit dem Elektroplaner des Krankenhauses abstimmen: die Neutralleiterbehandlung des Generators muss zur Anlage passen, nicht umgekehrt.
- **Brandabschnitt.** Der Generatorraum ist ein Brandabschnitt mit eigener Detektion und meist eigener Löschanlage.
- **Zugänglichkeit.** Alternatorende und beide Motorseiten freihalten: ein Aggregat, das nicht gewartet werden kann, fällt früh aus.

## 9. Prüfung: der Teil, den die meisten Anbieter auslassen

Ein Krankenhausgenerator wird in der Nacht beurteilt, in der er gebraucht wird. Deshalb kommt jedes Aggregat unseres Werks in Yangzhou vor dem Versand nach einer festen Sequenz auf eine digitale Lastbank:

| Stufe | Haltezeit | Geprüft wird |
|---|---|---|
| Ohne Last | — | Aufwärmen, Öldruck, Ladespannung |
| 25 % Last | 30 min | Spannungs- und Frequenzstabilität, Abgastemperatur |
| 50 % Last | 30 min | Reglerverhalten, Verbrauch, Geräusch |
| 75 % Last | 60 min | Kühlsystem, Kühlmitteltemperatur, Riemenspannung |
| 100 % Last | 60 min | Volle Nennleistung, Spannungsregelung innerhalb ±1,5 % |
| 110 % Überlast | 1 min | Schutzauslösung und Alarmprüfung |

Nach dem Lauf prüfen wir Isolationswiderstand und Erddurchgang nach thermischer Wechselbeanspruchung, verifizieren alle Schutzfunktionen (Überdrehzahl, Wassertemperatur hoch, Öldruck niedrig, Überstrom, Not-Aus) und testen die ATS-Sequenz von Anfang bis Ende auf dem Prüfstand. Ein Prüfbericht reist mit dem Aggregat.

Braucht das Projekt einen Prüfungstermin mit Beisein, einen Fremdprüfbericht (BV, SGS oder TUV) oder ein standortspezifisches FAT-Protokoll, muss das vor Produktionsbeginn gebucht werden — nicht in der Woche vor dem Versand.

## 10. Warum Krankenhäuser mit Kaichen arbeiten

Wir bauen Generatoraggregate in Yangzhou, China, von 20 kVA bis 3.000 kVA, und Krankenhausprojekte sind ein wesentlicher Teil unserer Arbeit. Drei Punkte wiegen in diesem Segment mehr als anderswo.

**Wir fertigen unsere Alternatoren selbst.** Die KCI-Serie ist mit Kupfer gewickelt, Klasse-H-isoliert, IP23 geschützt, AVR-geregelt und entsteht am selben Standort wie die Montage. Braucht ein Krankenhaus ein bestimmtes Transientverhalten, ändern wir den Alternator, statt einen einzukaufen.

**Wir prüfen unter Volllast, im Haus.** Eine digitale Lastbank mit 2 MW erlaubt es, ein 1.600-kW-Aggregat vor dem Versand bei 110 % zu prüfen und nicht nur im Leerlauf auf dem Hof.

**Wir dokumentieren in der Sprache des Kunden.** Datenblätter, Betriebs- und Wartungshandbücher, Steuerlogik-Beschreibungen und Typenschilder können in den Sprachen geliefert werden, in denen wir publizieren — das verkürzt die Inbetriebnahme, wenn das Baustellenteam kein Englisch spricht.

Unsere Krankenhausreferenzen reichen von einem 200-kW-Aggregat für ein kommunales Krankenhaus bis zu Anlagen der 1.600–1.800-kW-Klasse für regionale Klinikstandorte, darunter Maschinen, die seit Jahren im Notstrombetrieb mit planmäßigen Lastbankprüfungen laufen. Jede Lieferung enthält CE- und ISO-9001-Dokumentation, ein Ersatzteilpaket für das erste Wartungsintervall und 24/7-Techniksupport während der Inbetriebnahme.

## Häufige Fragen

**Welche Generatorleistung braucht ein Krankenhaus?**
Das hängt vom Sicherheitsstromkreis ab, nicht von der Bettenzahl. Eine Praxis mit OP-Beleuchtung, Intensivgeräten und zwei Aufzügen braucht meist 150–250 kW. Ein Allgemeinkrankenhaus mit 200 Betten und Kältemaschinen am Sicherheitsstromkreis liegt üblicherweise bei 400–600 kW. Ein regionaler Klinikstandort mit Küche, Wäscherei, Bildgebung und über 15 Aufzügen braucht oft 1.200–2.000 kW, meist zwei oder mehr Aggregate im Parallelbetrieb.

**Wie lange muss der Kraftstoff reichen?**
Übliche Spezifikationen fordern 72 Stunden bei definierter Last, bei kritischen Einrichtungen teils 96 Stunden. Bemessen Sie den Tank aus dem tatsächlichen Verbrauch in g/kWh bei erwarteter mittlerer Last: für ein 200-kW-Aggregat bei Halblast decken etwa 1.700 L die 72 Stunden.

**Kann ein Dieselgenerator Operationssäle versorgen?**
Ja, aber nicht direkt. Der OP wird üblicherweise über USV oder statischen Umschalter versorgt, der die 10–30 Sekunden bis zur Lastübernahme überbrückt; danach muss der Generator Spannung und Frequenz in den Grenzen halten, die die Medizintechnik verträgt.

**Schallhaube oder offenes Aggregat?**
Schallhaube für alles, was von Patienten, Personal oder der Grundstücksgrenze hörbar ist. Offen ist nur in einem gut gedämmten Maschinenraum oder auf abgelegenem Gelände praktikabel.

**Wie oft soll ein Krankenhausgenerator geprüft werden?**
Monatliche Leerlauf- oder Schwachlastläufe plus eine jährliche Volllastprüfung auf der Lastbank sind eine übliche Basis; viele Akkreditierungssysteme verlangen dokumentierte Monatsprüfungen und jährliche Lastprüfungen bei Nennleistung. Prüfen Sie die ATS dabei mit, nicht separat.

## Nächster Schritt

Wenn Sie ein Krankenhausaggregat auslegen, senden Sie uns die Lastliste des Sicherheitsstromkreises und die Standortbedingungen — Höhenlage, Umgebungstemperatur, Grenzwert für Schall an der Grundstücksgrenze, geforderte Kraftstoffdauer — und wir dimensionieren auf den tatsächlichen Anlauf statt nach Faustregel. Die Maschinenklasse, die wir bauen, sehen Sie auf den Seiten [Cummins 200 kW schallgedämpft](/de/products/cummins-200kw-silent-diesel-generator/), [Yuchai 300 kW schallgedämpft](/de/products/yuchai-300kw-silent-diesel-generator/) und [Mitsubishi 1000 kW offen](/de/products/mitsubishi-1000kw-open-diesel-generator/), oder [kontaktieren Sie uns](/de/contact/) mit Ihrem Übersichtsplan.
