---
title: "Groupe électrogène diesel pour hôpital : guide de dimensionnement"
date: "2026-10-28"
excerpt: "Comment dimensionner un groupe électrogène diesel pour un hôpital : bilan de puissance, calcul en kVA, démarrage des moteurs, autonomie de carburant, redondance et essais en charge."
image: "/images/blog/hospital-generator-sizing.jpg"
---

![Groupe électrogène insonorisé pour secours hospitalier dans notre usine de Yangzhou](/images/blog/hospital-generator-sizing.jpg)

# Groupe électrogène diesel pour hôpital : guide de dimensionnement

Une coupure de réseau dans un hôpital n'est pas une gêne. En quelques secondes, le bloc opératoire perd son éclairage, les respirateurs de réanimation passent sur des batteries qui tiennent des minutes et non des heures, les enceintes de la banque du sang dépassent les 6 °C, les ascenseurs s'arrêtent entre deux étages avec des patients à bord et l'appel malade s'éteint.

C'est pourquoi un **groupe électrogène diesel pour hôpital** se spécifie autrement qu'un groupe pour une usine ou un chantier. Ce n'est pas « le plus gros groupe qui rentre dans le budget », mais une machine de sécurité des personnes dont la puissance, le comportement au démarrage, l'autonomie, l'acoustique et les procès-verbaux d'essai doivent tenir devant un auditeur d'accréditation.

Ce guide suit la séquence réelle que nous appliquons sur les projets hospitaliers : établir le bilan de puissance, convertir en kVA avec les corrections nécessaires, vérifier le démarrage des moteurs, puis fixer carburant, redondance, bruit et essais. Les chiffres proviennent de nos fiches techniques de la série KC, dont deux groupes réellement destinés à des hôpitaux.

## 1. Ce que le groupe alimente réellement dans un hôpital

L'installation électrique d'un hôpital est généralement divisée entre un départ normal et un ou plusieurs tableaux essentiels. Seuls les tableaux essentiels sont raccordés au groupe. Bien délimiter cette frontière, c'est la moitié du travail.

| Famille de charges | Contenu typique | Conséquence pour le dimensionnement |
|---|---|---|
| Sécurité des personnes | Éclairage des blocs et de réanimation, alarme incendie, désenfumage, éclairage d'évacuation, alarmes de gaz médicaux | Basculement en une dizaine de secondes, jamais délestable |
| Critique | Équipements de réanimation et néonatologie, dialyse, froid de la banque du sang, chaîne du froid pharmacie, incubateurs de laboratoire, informatique et appel malade | La stabilité de tension compte plus que la puissance brute |
| Équipement | Ascenseurs, pompes à eau, pompe incendie, traitement d'air, stérilisation, cuisine et blanchisserie partielles | Le démarrage des moteurs commande le dimensionnement, pas le régime établi |
| Optionnel | Prises des chambres, climatisation standard, partie de la cuisine | Généralement exclu ou délesté en surcharge |

Deux règles pratiques en découlent. D'abord, ne pas mettre tout l'hôpital sur le groupe si le budget et le stockage de carburant ne le permettent pas : la plupart des projets placent 40–60 % de la puissance installée sur le tableau essentiel. Ensuite, traiter les charges moteur comme un problème de démarrage et non de régime : un moteur d'ascenseur de 15 kW peut appeler cinq à sept fois son courant nominal pendant une à deux secondes.

Le cadre réglementaire varie selon les pays — NFPA 99 et NFPA 110 aux États-Unis, HTM 06-01 au Royaume-Uni, IEC 60364-7-710 pour les locaux médicaux en Europe et sur de nombreux marchés d'exportation. Les détails diffèrent, mais l'essentiel converge : un tableau essentiel défini, un temps de basculement défini, une autonomie définie et des essais périodiques documentés. Vérifiez la version locale avant de figer les kVA.

## 2. D'abord le bilan de puissance, ensuite les kVA

Toute discussion sur la puissance d'un groupe hospitalier est en réalité une discussion sur le bilan de puissance. Établissez-le sous tableur, circuit par circuit.

Pour chaque poste, notez quatre données : kW de plaque, facteur de puissance, facteur de simultanéité (ce qui fonctionne réellement ensemble) et mode de démarrage (direct, étoile-triangle, démarreur progressif, variateur).

Exemple pour un hôpital général de 200 lits dont les groupes froids, la cuisine et la blanchisserie sont sur le tableau essentiel. Ce sont des valeurs de pré-dimensionnement, qui ne remplacent pas le schéma unifilaire du projet :

| Charge | kW raccordés | Facteur de simultanéité | kW en régime |
|---|---|---|---|
| Blocs, réanimation, éclairage de sécurité, systèmes incendie | 120 | 1,0 | 120 |
| Équipements de réanimation, banque du sang, pharmacie, informatique | 90 | 1,0 | 90 |
| Ascenseurs (4 × 15 kW) | 60 | 0,6 | 36 |
| Groupe froid (un sur le tableau essentiel) | 90 | 1,0 | 90 |
| Pompes, traitement d'eau, pompe incendie | 55 | 1,0 | 55 |
| Cuisine et blanchisserie, partiel | 60 | 1,0 | 60 |
| **Total en régime** | | | **451** |

Un facteur de diversité de 0,9 donne environ **406 kW**. On ajoute une réserve d'évolution — un hôpital ajoute de l'imagerie, des lits, de la climatisation — d'où 20 %, soit **487 kW**. Le groupe standard le plus proche est une unité de **500 kW / 625 kVA**.

Vérifiez ensuite le démarrage. Si le groupe froid démarre en direct à six fois son courant alors que le bloc est déjà chargé, le groupe doit absorber ce palier sans que la chute de tension décroche les équipements médicaux. Si le contrôle échoue, la réponse n'est pas par défaut un groupe plus gros : c'est un démarreur progressif ou un variateur sur le groupe froid, généralement moins cher que 200 kW d'alternateur en plus.

## 3. La formule et les quatre corrections

La conversion de base est simple :

**kVA = kW ÷ facteur de puissance**

Avec le facteur standard 0,8 inductif de nos groupes 50 Hz, 400 kW de charge en régime demandent 500 kVA d'alternateur avant correction. Quatre corrections s'appliquent ensuite.

**Réserve d'évolution.** 15–25 % pour un hôpital neuf : personne ne dimensionne pour le nombre de lits du jour.

**Démarrage moteur et charge par paliers.** La chute transitoire de tension doit rester dans ce que tolèrent les équipements médicaux. Nos fiches de la série KC spécifient : écart transitoire de tension ≤ 15 %, régulation de tension en régime ≤ 0,5 %, écart transitoire de fréquence ≤ 0,5 %, retour à la tension et à la fréquence en ≤ 3 secondes. C'est ce que voit réellement un monitorage de réanimation pendant le basculement.

**Déclassement selon le site.** Un groupe donné pour 40 °C perd de la puissance à 45 °C, et davantage en altitude. Si la salle est chaude parce que le radiateur souffle dans un angle, on déclasse — ou on corrige la ventilation.

**Régime.** Puissance de secours (heures limitées, sans surcharge) contre puissance principale (continu, 10 % de surcharge pendant une heure). Un hôpital qui fait tourner le groupe huit heures pendant une réparation de réseau est en secours ; un hôpital coupé quotidiennement est en régime principal et doit être spécifié comme tel.

## 4. Deux repères réels

Les recommandations abstraites sont faciles à écrire et difficiles à utiliser. Voici deux groupes que nous construisons pour des projets hospitaliers, chiffres tirés directement des fiches KC.

| Paramètre | KC-YC200 | KC-YC1600 |
|---|---|---|
| Puissance nominale / secours | 200 kW / 220 kW | 1 600 kW / 1 760 kW |
| Tension / courant | 380/220 V, 360 A | 380/220 V, 2 880 A |
| Fréquence, facteur de puissance | 50 Hz, 0,8 inductif | 50 Hz, 0,8 inductif |
| Moteur | Yuchai YC6MK350L-D20, 235 / 258,5 kW | Yuchai YC16VTD2700-D30, 1 805 / 1 985 kW |
| Cylindres / cylindrée | En ligne 6, 10,34 L, 123 × 145 mm | V16, 52,26 L, 152 × 180 mm |
| Suralimentation / régulation | Turbocompresseur avec échangeur, électronique | Turbocompresseur avec échangeur, électronique |
| Consommation | 200 g/kWh | 200 g/kWh |
| Alternateur | KCI-200, sans balais, AVR, IP23, classe H, cuivre | KCI-1600, sans balais, AVR, IP23, classe H, cuivre |
| Dimensions (L × l × H) | 3 000 × 1 100 × 1 750 mm | 5 500 × 2 200 × 2 700 mm |
| Masse | 2 800 kg | 15 800 kg (indicatif) |
| Bruit (LP7M) | 102 dB(A) | 102 dB(A) |

**Quand la classe 200 kW convient.** Cliniques, centres de chirurgie ambulatoire, petits hôpitaux et annexes d'imagerie où le tableau essentiel se limite à l'éclairage des blocs, aux équipements de réanimation, aux systèmes incendie, à l'informatique et à deux ascenseurs, le groupe froid restant sur le départ normal. Avec 2 800 kg et 3 m de long, il entre dans une salle des machines en sous-sol sur un transpalette, ce qui compte en rénovation avec une porte de 1,2 m.

**Quand la classe 1 600 kW convient.** Hôpitaux régionaux et universitaires dont le tableau essentiel comprend réellement les groupes froids centraux, la cuisine, la blanchisserie, l'imagerie et 10 à 20 ascenseurs. À 15 800 kg et 5,5 m, il faut une vraie salle, un radier ou une plateforme au sol, un plan de levage et, en général, deux unités en parallèle plutôt qu'une.

Entre les deux existent des paliers intermédiaires ; l'essentiel est que la fiche technique soit assez complète pour que l'ingénieur la reporte directement dans son modèle électrique.

## 5. Autonomie : la question des 72 heures

Le carburant est le point où les spécifications hospitalières échouent le plus souvent, parce que la consommation est donnée en g/kWh et que la conversion est oubliée.

Avec 200 g/kWh et un gazole à environ 0,84 kg/L :

**Litres par heure = kW nominaux × 0,2 ÷ 0,84**

| Charge (KC-YC200) | Carburant par heure | Sur 24 h | Sur 72 h |
|---|---|---|---|
| 100 % (200 kW) | 47,6 L/h | 1 143 L | 3 429 L |
| 50 % moyen (100 kW) | 23,8 L/h | 571 L | 1 714 L |
| 25 % moyen (50 kW) | 11,9 L/h | 286 L | 857 L |

Un groupe de 200 kW à charge moyenne réaliste de moitié demande donc environ **1 700 L pour 72 heures**. Spécifiez une cuve principale de 2 000 L et vous gardez de la marge plus le volume non récupérable. Pour le 1 600 kW à mi-charge, comptez environ **4 570 L par 24 heures** : les grands hôpitaux installent donc une cuve enterrée ou sous rétention avec un contrat de polissage du carburant, et non une cuve sur châssis.

Trois points que vérifient les inspecteurs : un **réservoir journalier** de 8 heures de marche (pour qu'un incident sur la cuve principale n'arrête pas le groupe), une **rétention à 110 %** du volume et des **alarmes de niveau haut et bas** reportées en GTB. Sur la ligne, un robinet d'isolement coupe-feu en sortie de cuve, et jamais de passage par une cage d'escalier.

## 6. Redondance, mise en parallèle et basculement

Un groupe unique est un point de défaillance unique. Les hôpitaux l'acceptent rarement en construction neuve.

| Schéma | Signification | Usage typique |
|---|---|---|
| N | Un groupe dimensionné pour la charge essentielle | Cliniques, petits hôpitaux |
| N+1 | Un groupe supplémentaire capable de reprendre la charge en cas de défaillance | Hôpitaux généraux, 3 × 500 kW pour 1 000 kW |
| 2N | Deux alimentations complètes et indépendantes, salles séparées | Hôpitaux universitaires, grands campus |

La mise en parallèle apporte plus que la redondance : deux groupes à 60 % au lieu d'un à 100 % réduisent consommation et bruit nocturne, et permettent d'entretenir l'un pendant que l'autre tient la charge. Nos contrôleurs gèrent le partage de charge, le partage isochrone et la synchronisation automatique, avec un sectionneur de barres pour isoler une unité.

Sur le basculement, fixez tôt le temps de commutation. Les circuits de sécurité des personnes sont généralement attendus sous une dizaine de secondes ; blocs et réanimation couvrent cet intervalle par onduleur ou commutateur statique plutôt qu'en comptant sur un groupe instantané. Testez toute la séquence — perte réseau, signal ATS, lancement, montée en tension, fermeture du disjoncteur, prise de charge — sur banc, pas la nuit de la coupure.

## 7. Bruit, implantation et voisinage

Les deux groupes du tableau sont à châssis ouvert, 102 dB(A) à 7 mètres au point de référence LP7M. C'est fort, de l'ordre de la tronçonneuse. Acceptable dans une salle correctement traitée ou sur un site isolé, inacceptable à 30 mètres de la fenêtre d'une chambre.

Options par ordre de coût :

- **Capot insonorisé** : ramène généralement le groupe dans la plage 70–75 dB(A) à 7 m.
- **Traitement de la salle** : doublage acoustique, portes étanches, dalle flottante et silencieux d'entrée et de sortie d'air correctement dimensionnés. Pour un gros groupe, c'est souvent la voie la moins chère vers une limite de limite stricte.
- **Implantation** : éloigner le refoulement du radiateur et le conduit de fumée de la façade des chambres, et vérifier la hauteur du conduit par rapport à la fenêtre ouvrable la plus proche.

Vérifiez les limites de voisinage avant de choisir, elles varient beaucoup ; de nombreuses juridictions appliquent de l'ordre de 45–55 dB(A) au récepteur sensible le plus proche la nuit. Ne comptez pas sur un capot seul pour un groupe de 1,6 MW : ce ne sera pas suffisant.

## 8. Les détails d'installation qui décident du résultat

Ce sont eux qui transforment une fiche technique correcte en installation qui fonctionne :

- **Air de refroidissement.** Le radiateur exige une entrée libre et un refoulement canalisé vers l'extérieur. Une salle avec un claustra de la taille d'une boîte aux lettres déclassera le groupe et surchauffera l'alternateur.
- **Contre-pression d'échappement.** Tracés longs, coudes serrés et silencieux sous-dimensionnés augmentent la contre-pression et coûtent de la puissance. Tracez avec la contre-pression maximale admissible du fournisseur en main.
- **Isolation vibratoire.** Supports à ressort ou caoutchouc sous le châssis, compensateurs souples sur l'échappement et raccord de carburant souple. Sans eux, le bruit passe par la dalle vers les étages.
- **Section des câbles.** À calculer sur le courant nominal à la température réelle, en gardant câbles de puissance et de contrôle dans des chemins séparés.
- **Mise à la terre et neutre.** Validez le régime de neutre avec l'ingénieur électricien de l'hôpital : le traitement du neutre du groupe doit s'accorder à l'installation, pas l'inverse.
- **Compartimentage incendie.** La salle du groupe est un compartiment avec sa détection et, en général, son extinction.
- **Accessibilité.** Dégagez l'extrémité alternateur et les deux côtés du moteur : un groupe qu'on ne peut pas entretenir tombe en panne tôt.

## 9. Les essais : ce que la plupart des fournisseurs oublient

Un groupe d'hôpital se juge la nuit où on en a besoin. C'est pourquoi chaque unité quittant notre usine de Yangzhou passe sur un banc de charge numérique avant expédition, selon une séquence fixe :

| Palier | Maintien | Ce qui est vérifié |
|---|---|---|
| À vide | — | Montée en température, pression d'huile, tension de charge |
| 25 % de charge | 30 min | Stabilité tension et fréquence, température d'échappement |
| 50 % de charge | 30 min | Réponse du régulateur, consommation, bruit |
| 75 % de charge | 60 min | Circuit de refroidissement, température du liquide, tension de courroie |
| 100 % de charge | 60 min | Puissance nominale pleine, régulation de tension dans ±1,5 % |
| Surcharge 110 % | 1 min | Déclenchement des protections et vérification des alarmes |

Après l'essai, nous contrôlons la résistance d'isolement et la continuité de terre après cyclage thermique, vérifions toutes les protections (surrégime, température d'eau élevée, pression d'huile basse, surintensité, arrêt d'urgence) et testons la séquence ATS de bout en bout sur banc. Le procès-verbal accompagne le groupe.

Si le projet exige un essai avec témoin, un rapport d'inspection tierce (BV, SGS ou TUV) ou un protocole FAT spécifique, cela se réserve avant l'entrée en production, pas la semaine précédant l'expédition.

## 10. Pourquoi les hôpitaux travaillent avec Kaichen

Nous fabriquons des groupes électrogènes à Yangzhou, en Chine, de 20 kVA à 3 000 kVA, et le secteur hospitalier représente une part importante de notre activité. Trois choses comptent ici plus qu'ailleurs.

**Nous fabriquons nos propres alternateurs.** La série KCI est bobinée en cuivre, isolée classe H, protégée IP23, régulée par AVR et produite sur le même site que l'assemblage. Quand un hôpital exige une réponse transitoire précise, nous changeons l'alternateur au lieu d'en chercher un ailleurs.

**Nous essayons à pleine charge, chez nous.** Un banc de charge numérique de 2 MW permet d'éprouver un groupe de 1 600 kW à 110 % avant expédition, et pas seulement à vide dans la cour.

**Nous documentons dans la langue du client.** Fiches techniques, manuels d'exploitation et de maintenance, descriptions de logique de contrôle et plaques peuvent être fournis dans les langues que nous publions, ce qui raccourcit la mise en service quand l'équipe de site ne parle pas anglais.

Nos références hospitalières vont d'un groupe de 200 kW pour un hôpital municipal à des installations de classe 1 600–1 800 kW pour des campus hospitaliers régionaux, dont des machines en service de secours depuis des années avec essais de charge programmés. Chaque expédition comprend la documentation CE et ISO 9001, un kit de pièces pour le premier intervalle d'entretien et un support technique 24/7 pendant la mise en service.

## Questions fréquentes

**Quelle puissance de groupe faut-il pour un hôpital ?**
Cela dépend du tableau essentiel, pas du nombre de lits. Une clinique avec éclairage de bloc, équipements de réanimation et deux ascenseurs demande généralement 150–250 kW. Un hôpital général de 200 lits avec groupes froids sur le tableau essentiel se situe le plus souvent entre 400 et 600 kW. Un campus régional avec cuisine, blanchisserie, imagerie et plus de 15 ascenseurs demande souvent 1 200–2 000 kW, en général deux unités ou plus en parallèle.

**Quelle autonomie de carburant prévoir ?**
Les spécifications courantes demandent 72 heures à une charge définie, parfois 96 heures pour les installations critiques. Dimensionnez la cuve à partir de la consommation réelle en g/kWh à la charge moyenne attendue : pour un groupe de 200 kW à mi-charge, environ 1 700 L couvrent 72 heures.

**Un groupe diesel peut-il alimenter des blocs opératoires ?**
Oui, mais pas directement. Le bloc est normalement alimenté via un onduleur ou un commutateur statique qui couvre les 10–30 secondes jusqu'à la prise de charge par le groupe ; le rôle du groupe est ensuite de tenir tension et fréquence dans les limites tolérées par les équipements.

**Capot insonorisé ou châssis ouvert ?**
Insonorisé pour tout ce qui est audible depuis les chambres, le personnel ou la limite de propriété. Le châssis ouvert n'est réaliste que dans une salle bien traitée ou sur un site isolé.

**À quelle fréquence tester un groupe d'hôpital ?**
Des marches mensuelles à vide ou faible charge plus un essai annuel à pleine charge sur banc constituent une base courante ; de nombreux référentiels d'accréditation exigent des essais mensuels documentés et annuels à la puissance nominale. Testez l'ATS en même temps, pas séparément.

## Étape suivante

Si vous spécifiez un groupe hospitalier, envoyez-nous le bilan de puissance du tableau essentiel et les conditions du site — altitude, température ambiante, limite de bruit en limite de propriété, autonomie exigée — et nous dimensionnerons sur le démarrage réel plutôt que sur une règle empirique. Vous pouvez voir la classe de machine que nous construisons sur les pages du [groupe Cummins 200 kW insonorisé](/fr/products/cummins-200kw-silent-diesel-generator/), du [groupe Yuchai 300 kW insonorisé](/fr/products/yuchai-300kw-silent-diesel-generator/) et du [groupe Mitsubishi 1000 kW ouvert](/fr/products/mitsubishi-1000kw-open-diesel-generator/), ou [nous contacter](/fr/contact/) avec votre schéma unifilaire.
