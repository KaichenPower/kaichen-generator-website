---
title: "Generador diésel para respaldo eléctrico de hospitales: guía de dimensionamiento"
date: "2026-10-28"
excerpt: "Cómo dimensionar un generador diésel para respaldo de hospital: lista de cargas, cálculo de kVA, arranque de motores, autonomía de combustible, redundancia y pruebas con banco de carga."
image: "/images/blog/hospital-generator-sizing.jpg"
---

![Generador diésel insonorizado para respaldo hospitalario en nuestra fábrica de Yangzhou](/images/blog/hospital-generator-sizing.jpg)

# Generador diésel para respaldo eléctrico de hospitales: guía de dimensionamiento

Un corte de red en un hospital no es una molestia. En segundos, el quirófano pierde la iluminación, los ventiladores de la UCI pasan a baterías que duran minutos y no horas, las neveras del banco de sangre empiezan a superar los 6 °C, los ascensores se detienen entre plantas con pacientes dentro y el sistema de llamada de enfermería se apaga.

Por eso un **generador diésel para respaldo de hospital** se especifica de forma distinta a un generador para una fábrica o una obra. No es «el equipo más grande que entra en el presupuesto», sino una máquina de seguridad de vida cuya potencia, comportamiento de arranque, autonomía de combustible, acústica y registro de pruebas deben poder defenderse ante un auditor de acreditación.

Esta guía recorre la secuencia real de cálculo que usamos en proyectos hospitalarios: elaborar la lista de cargas, convertir a kVA con las correcciones necesarias, comprobar el arranque de motores y después fijar combustible, redundancia, ruido y pruebas. Las cifras provienen de nuestras hojas técnicas de la serie KC, incluidas dos unidades reales de clase hospitalaria.

## 1. Qué alimenta realmente el generador en un hospital

La instalación eléctrica de un hospital suele dividirse en un suministro normal y uno o varias barras esenciales. Solo las barras esenciales pasan al generador. Definir bien ese límite es la mitad del trabajo.

| Grupo de carga | Contenido típico | Qué implica para el cálculo |
|---|---|---|
| Seguridad de vida | Iluminación de quirófano y UCI, alarma de incendio, extracción de humos, alumbrado de evacuación, alarmas de gases medicinales | Transferencia en unos 10 segundos; nunca se puede deslastrar |
| Crítico | Equipos de UCI y neonatología, diálisis, refrigeración del banco de sangre, cadena de frío de farmacia, incubadoras de laboratorio, TI y llamada de enfermería | Importa más la estabilidad de tensión que la potencia bruta |
| Equipos | Ascensores, bombas de agua, bomba contra incendios, climatización, esterilización, parte de cocina y lavandería | Manda el arranque de motores, no la potencia en régimen |
| Opcional | Tomas de habitaciones, climatización estándar, parte de cocina | Normalmente no pasa al generador o se deslastra en sobrecarga |

De aquí salen dos reglas prácticas. Primera: no ponga todo el hospital en el generador si el presupuesto y el depósito de combustible no lo soportan; la mayoría de proyectos dejan en la barra esencial el 40–60 % de la carga conectada. Segunda: trate las cargas de motor como un problema de arranque, no de régimen; un motor de ascensor de 15 kW puede pedir de cinco a siete veces su corriente nominal durante uno o dos segundos.

El marco normativo varía por país — NFPA 99 y NFPA 110 en Estados Unidos, HTM 06-01 en Reino Unido, IEC 60364-7-710 para locales médicos en Europa y muchos mercados de exportación. Difieren en detalles, pero coinciden en lo esencial: barra esencial definida, tiempo de transferencia definido, duración de combustible definida y pruebas periódicas documentadas. Confirme la edición local antes de cerrar los kVA.

## 2. Primero la lista de cargas, después los kVA

Toda discusión sobre potencia hospitalaria es en realidad una discusión sobre la lista de cargas. Hágalo en una hoja de cálculo, circuito por circuito.

Para cada ítem registre cuatro datos: kW de placa, factor de potencia, factor de demanda (cuánto funciona a la vez) y método de arranque (directo, estrella-triángulo, arrancador suave, variador).

Ejemplo para un hospital general de 200 camas con enfriadoras, cocina y lavandería en la barra esencial. Son cifras de planificación; no sustituyen el diagrama unifilar del proyecto:

| Carga | kW conectados | Factor de demanda | kW en régimen |
|---|---|---|---|
| Quirófanos, UCI, alumbrado de emergencia, sistemas contra incendios | 120 | 1,0 | 120 |
| Equipos de UCI, banco de sangre, farmacia, TI | 90 | 1,0 | 90 |
| Ascensores (4 × 15 kW) | 60 | 0,6 | 36 |
| Enfriadora (una en barra esencial) | 90 | 1,0 | 90 |
| Bombas, tratamiento de agua, bomba contra incendios | 55 | 1,0 | 55 |
| Cocina y lavandería, parcial | 60 | 1,0 | 60 |
| **Total en régimen** | | | **451** |

Un factor de simultaneidad de 0,9 da unos **406 kW**. Añadimos crecimiento —un hospital suma imagen, suma camas, suma climatización—, por lo que un 20 % es una reserva realista: **487 kW**. El equipo estándar más cercano es una unidad de **500 kW / 625 kVA**.

Después revise el arranque. Si la enfriadora arranca en directo con seis veces su corriente mientras el quirófano ya está cargado, el equipo debe absorber ese escalón sin que la caída de tensión desconecte equipos médicos. Si no pasa, la respuesta no es por defecto un generador mayor: es un arrancador suave o un variador en la enfriadora, normalmente más barato que 200 kW extra de alternador.

## 3. La fórmula y las cuatro correcciones

La conversión base es simple:

**kVA = kW ÷ factor de potencia**

Con el factor estándar 0,8 inductivo de nuestros equipos de 50 Hz, 400 kW de carga en régimen piden 500 kVA de alternador antes de corregir. Luego aplican cuatro correcciones.

**Reserva de crecimiento.** 15–25 % para un hospital nuevo: nadie dimensiona para el número de camas de hoy.

**Arranque de motores y carga escalonada.** La caída transitoria de tensión debe quedar dentro de lo que tolera el equipamiento médico. Nuestras hojas de la serie KC especifican: desviación transitoria de tensión ≤ 15 %, regulación de tensión en régimen ≤ 0,5 %, desviación transitoria de frecuencia ≤ 0,5 % y recuperación de tensión y frecuencia ≤ 3 segundos. Eso es lo que realmente ve un monitor de UCI durante la transferencia.

**Desclasificación por sitio.** Un equipo nominal a 40 °C pierde capacidad a 45 °C y pierde más en altitud. Si la sala está caliente porque el radiador descarga contra una esquina, se desclasifica o se corrige el caudal de aire.

**Régimen.** Potencia de respaldo (horas limitadas, sin sobrecarga) frente a potencia principal (continua, 10 % de sobrecarga durante una hora). Un hospital que usa el grupo ocho horas durante una reparación de red está en respaldo; uno con cortes diarios está en régimen principal y debe especificarse así.

## 4. Dos referencias reales

La orientación abstracta es fácil de escribir y difícil de aplicar. Estas son dos unidades que fabricamos para servicio hospitalario, con datos tomados directamente de las hojas técnicas KC.

| Parámetro | KC-YC200 | KC-YC1600 |
|---|---|---|
| Potencia nominal / respaldo | 200 kW / 220 kW | 1.600 kW / 1.760 kW |
| Tensión / corriente | 380/220 V, 360 A | 380/220 V, 2.880 A |
| Frecuencia, factor de potencia | 50 Hz, 0,8 inductivo | 50 Hz, 0,8 inductivo |
| Motor | Yuchai YC6MK350L-D20, 235 / 258,5 kW | Yuchai YC16VTD2700-D30, 1.805 / 1.985 kW |
| Cilindros / cilindrada | En línea 6, 10,34 L, 123 × 145 mm | V16, 52,26 L, 152 × 180 mm |
| Sobrealimentación / regulador | Turbointercooler, electrónico | Turbointercooler, electrónico |
| Consumo de combustible | 200 g/kWh | 200 g/kWh |
| Alternador | KCI-200, sin escobillas, AVR, IP23, clase H, cobre | KCI-1600, sin escobillas, AVR, IP23, clase H, cobre |
| Dimensiones (L × An × Al) | 3.000 × 1.100 × 1.750 mm | 5.500 × 2.200 × 2.700 mm |
| Peso | 2.800 kg | 15.800 kg (referencia) |
| Ruido (LP7M) | 102 dB(A) | 102 dB(A) |

**Cuándo encaja la clase de 200 kW.** Clínicas, centros de cirugía ambulatoria, hospitales pequeños y anexos de imagen donde la barra esencial se limita a iluminación de quirófano, equipos de UCI, sistemas contra incendios, TI y un par de ascensores, y la enfriadora queda en el suministro normal. Con 2.800 kg y 3 m de largo entra en una sala de máquinas en sótano sobre transpaleta, algo decisivo en una reforma con una puerta de 1,2 m.

**Cuándo encaja la clase de 1.600 kW.** Hospitales regionales y universitarios donde la barra esencial incluye de verdad enfriadoras centrales, cocina, lavandería, imagen y 10–20 ascensores. Con 15.800 kg y 5,5 m necesita una sala real, losa o recinto a nivel de suelo, plan de izado y, normalmente, dos unidades en paralelo en lugar de una.

Entre ambos tamaños hay escalones intermedios; lo importante es que la hoja técnica sea lo bastante completa para que el ingeniero la copie directamente al modelo eléctrico.

## 5. Autonomía: la pregunta de las 72 horas

El combustible es donde más fallan las especificaciones hospitalarias, porque el consumo se cita por kWh y todos olvidan convertirlo.

Con 200 g/kWh y densidad del diésel de unos 0,84 kg/L:

**Litros por hora = kW nominales × 0,2 ÷ 0,84**

| Carga (KC-YC200) | Combustible por hora | Por 24 h | Por 72 h |
|---|---|---|---|
| 100 % (200 kW) | 47,6 L/h | 1.143 L | 3.429 L |
| 50 % media (100 kW) | 23,8 L/h | 571 L | 1.714 L |
| 25 % media (50 kW) | 11,9 L/h | 286 L | 857 L |

Así, una unidad de 200 kW con una media realista de media carga necesita unos **1.700 L para 72 horas**. Especifique un tanque principal de 2.000 L y tendrá margen más volumen no utilizable. Para la unidad de 1.600 kW a media carga son unos **4.570 L al día**, por lo que los hospitales grandes instalan un depósito enterrado o con cubeto y un contrato de pulido de combustible, en lugar de un tanque en la bancada.

Tres detalles que revisan los inspectores: **tanque diario** para 8 horas de funcionamiento (para que un problema en el principal no pare el grupo), **cubeto del 110 %** del volumen y **alarmas de nivel alto y bajo** cableadas al sistema de gestión del edificio. En la línea de combustible, válvula de corte resistente al fuego a la salida del tanque y nunca por el hueco de escalera.

## 6. Redundancia, paralelo y transferencia

Un solo generador es un punto único de fallo. Los hospitales rara vez lo aceptan en obra nueva.

| Esquema | Qué significa | Uso habitual |
|---|---|---|
| N | Una unidad dimensionada para la carga esencial | Clínicas, hospitales pequeños |
| N+1 | Una unidad extra capaz de asumir la carga si falla cualquiera | Hospitales generales, 3 × 500 kW para 1.000 kW |
| 2N | Dos suministros completos e independientes con salas separadas | Hospitales universitarios, grandes campus |

El paralelo da más que redundancia: dos unidades al 60 % en lugar de una al 100 % reducen consumo y ruido nocturno, y permite mantener una mientras la otra sostiene la carga. Nuestros controladores soportan reparto de carga, reparto isócrono y sincronización automática, con barra de unión para aislar una unidad.

En la transferencia, fije pronto el tiempo de conmutación. Los circuitos de seguridad de vida suelen esperar energía en unos 10 segundos; quirófanos y UCI cubren ese hueco con SAI o conmutador estático en lugar de esperar un generador instantáneo. Pruebe toda la secuencia —fallo de red, señal del ATS, arranque, excitación, cierre del interruptor, toma de carga— en banco, no la noche del corte.

## 7. Ruido, ubicación y vecinos

Las dos unidades de la tabla son de bancada abierta a 102 dB(A) medidos a 7 metros en el punto de referencia LP7M. Es ruidoso, del orden de una motosierra. Aceptable en una sala bien atenuada o en un emplazamiento remoto, e inaceptable a 30 metros de la ventana de una habitación.

Opciones por orden de coste:

- **Carenado insonorizado**: normalmente baja la unidad al rango de 70–75 dB(A) a 7 m.
- **Atenuación de sala**: revestimiento acústico, puertas selladas, suelo flotante y atenuadores de entrada y salida de aire bien calculados. En equipos grandes suele ser la vía más económica para cumplir un límite estricto en el perímetro.
- **Ubicación**: aleje la descarga del radiador y la chimenea de la fachada de habitaciones y compruebe la altura respecto a la ventana practicable más cercana.

Consulte los límites de perímetro antes de elegir, porque varían mucho; muchas jurisdicciones aplican del orden de 45–55 dB(A) en el receptor sensible más cercano durante la noche. No asuma que un carenado insonorizado basta en una máquina de 1,6 MW: no basta.

## 8. Detalles de instalación que deciden si funciona

Estos convierten una hoja técnica correcta en una instalación que funciona:

- **Aire de refrigeración.** El radiador necesita entrada libre y salida canalizada al exterior. Una sala con una rejilla del tamaño de un buzón desclasifica el grupo y cocina el alternador.
- **Contrapresión de escape.** Tramos largos, curvas cerradas y silenciadores pequeños elevan la contrapresión y restan potencia. Trace con la contrapresión máxima admisible del proveedor en mano.
- **Aislamiento de vibraciones.** Soportes de resorte o caucho bajo la bancada, fuelles flexibles en escape y conexión flexible de combustible. Sin ellos el ruido viaja por la losa a las plantas superiores.
- **Sección de cables.** Calcule por la corriente nominal a la temperatura real y mantenga cables de potencia y control en bandejas separadas.
- **Puesta a tierra y neutro.** Confirme el esquema de puesta a tierra con el ingeniero eléctrico del hospital: el tratamiento del neutro del generador debe coincidir con la instalación, no al revés.
- **Sectorización contra incendios.** La sala del generador es un sector con detección propia y, normalmente, extinción propia.
- **Acceso.** Deje accesible el extremo del alternador y ambos lados del motor: un equipo que no se puede mantener falla pronto.

## 9. Pruebas: lo que más se omite

Un generador de hospital se juzga la noche en que se necesita. Por eso cada unidad que sale de nuestra fábrica de Yangzhou pasa por un banco de carga digital antes del envío, con una secuencia fija:

| Etapa | Duración | Qué se verifica |
|---|---|---|
| Sin carga | — | Calentamiento, presión de aceite, tensión de carga |
| 25 % de carga | 30 min | Estabilidad de tensión y frecuencia, temperatura de escape |
| 50 % de carga | 30 min | Respuesta del regulador, consumo, ruido |
| 75 % de carga | 60 min | Sistema de refrigeración, temperatura del refrigerante, tensión de correa |
| 100 % de carga | 60 min | Potencia nominal plena, regulación de tensión dentro de ±1,5 % |
| Sobrecarga 110 % | 1 min | Disparo de protecciones y verificación de alarmas |

Tras la prueba comprobamos resistencia de aislamiento y continuidad de tierra después de ciclos térmicos, verificamos todas las protecciones (sobrevelocidad, alta temperatura de agua, baja presión de aceite, sobrecorriente, paro de emergencia) y probamos la secuencia del ATS de principio a fin en banco. El informe de prueba viaja con la unidad.

Si el proyecto requiere prueba con testigo, informe de inspección de terceros (BV, SGS o TUV) o un protocolo FAT específico, debe reservarse antes de que la unidad entre en producción, no la semana previa al envío.

## 10. Por qué los hospitales trabajan con Kaichen

Fabricamos grupos electrógenos en Yangzhou, China, de 20 kVA a 3.000 kVA, y el segmento hospitalario es una parte importante de nuestro trabajo. Tres cosas pesan más aquí que en cualquier otro sector.

**Fabricamos nuestros propios alternadores.** La serie KCI se bobina en cobre, aislamiento clase H, protección IP23, regulación AVR y se produce en la misma planta que el montaje. Cuando un hospital necesita una respuesta transitoria concreta, cambiamos el alternador en lugar de buscarlo fuera.

**Probamos a plena carga, en casa.** Un banco de carga digital de 2 MW permite probar una unidad de 1.600 kW al 110 % antes de enviarla, no solo en vacío en el patio.

**Documentamos en el idioma del cliente.** Hojas técnicas, manuales de operación y mantenimiento, descripciones de lógica de control y placas pueden suministrarse en los idiomas en que publicamos, lo que acorta la puesta en marcha cuando el equipo de obra no habla inglés.

Nuestras referencias hospitalarias van de una unidad de 200 kW para un hospital municipal a instalaciones de clase 1.600–1.800 kW para campus de hospitales regionales, incluidas máquinas que llevan años en servicio de respaldo con pruebas de carga programadas. Cada envío incluye documentación CE e ISO 9001, un kit de repuestos para el primer intervalo de servicio y soporte técnico 24/7 durante la puesta en marcha.

## Preguntas frecuentes

**¿Qué tamaño de generador necesita un hospital?**
Depende de la barra esencial, no del número de camas. Una clínica con iluminación de quirófano, equipos de UCI y dos ascensores suele necesitar 150–250 kW. Un hospital general de 200 camas con enfriadoras en la barra esencial suele quedar entre 400 y 600 kW. Un campus regional con cocina, lavandería, imagen y más de 15 ascensores suele necesitar 1.200–2.000 kW, normalmente dos o más unidades en paralelo.

**¿Cuánto debe durar el combustible?**
Las especificaciones habituales piden 72 horas a una carga definida y a veces 96 horas en instalaciones críticas. Dimensione el tanque con el consumo real en g/kWh a la carga media prevista: para una unidad de 200 kW a media carga, unos 1.700 L cubren 72 horas.

**¿Puede un generador diésel alimentar quirófanos?**
Sí, pero no directamente. El quirófano se alimenta normalmente a través de un SAI o conmutador estático que cubre los 10–30 segundos hasta que el generador toma carga; la tarea del generador es mantener tensión y frecuencia dentro de los límites que tolera el equipamiento una vez conectado.

**¿Carenado insonorizado o bancada abierta?**
Insonorizado para todo lo que esté al alcance del oído de pacientes, personal o del perímetro. La bancada abierta solo es práctica en una sala bien atenuada o en un recinto remoto.

**¿Cada cuánto se prueba un generador de hospital?**
Funcionamiento mensual en vacío o baja carga más una prueba anual a plena carga en banco es una base común; muchos esquemas de acreditación exigen pruebas mensuales documentadas y anuales a potencia nominal. Pruebe el ATS al mismo tiempo, no por separado.

## Siguiente paso

Si está especificando un equipo hospitalario, envíenos la lista de cargas de la barra esencial y las condiciones del sitio —altitud, temperatura ambiente, límite de ruido en el perímetro, autonomía exigida— y dimensionaremos sobre el arranque real y no sobre una regla de pulgar. Puede ver la clase de máquina que fabricamos en las páginas del [generador Cummins 200 kW insonorizado](/es/products/cummins-200kw-silent-diesel-generator/), el [generador Yuchai 300 kW insonorizado](/es/products/yuchai-300kw-silent-diesel-generator/) y el [generador Mitsubishi 1000 kW abierto](/es/products/mitsubishi-1000kw-open-diesel-generator/), o [contactar con nosotros](/es/contact/) con su diagrama unifilar.
