import os

translations = {
    'ru': {
        'title': 'Чек-лист обслуживания дизель-генератора: 12 задач ежемесячно',
        'excerpt': 'Резервный генератор работает только если вы его обслуживаете. Вот практический ежемесячный чек-лист, которому следует наша сервисная команда.',
        'intro_p1': 'Дизельный генератор — это техника, которая 99% времени простаивает. Остальный 1% — когда отключается сеть — он должен запуститься, принять нагрузку и работать без сбоев. Это возможно только при правильном обслуживании.',
        'intro_p2': 'Установив сотни генераторов на фабриках, в больницах, дата-центрах и коммерческих зданиях, наша сервисная команда следует одному ежемесячному чек-листу.',
        'why_h': 'Почему важно ежемесячное обслуживание',
        'why_p': 'Генератор, который никогда не работает, всё равно изнашивается. Топливо стареет, аккумуляторы теряют заряд, резиновые шланги трескаются, грызуны строят гнёзда в кожухе. 10-минутный ежемесячный осмотр предотвращает 90% аварийных вызовов.',
        'checklist_h': '12-пунктный ежемесячный чек-лист',
        'items': [
            ('Запустите и протестируйте генератор', 'Запустите генератор под нагрузкой не менее 30% в течение 30 минут. Холостого теста недостаточно — двигатель должен выйти на рабочую температуру, а генератор — принять реальную нагрузку.'),
            ('Проверьте аккумулятор', 'Измерьте напряжение зарядки (около 27В для системы 24В). Очистите клеммы и проверьте уровень электролита. Севший аккумулятор — причина №1 отказа запуска генератора.'),
            ('Проверьте уровень и качество масла', 'Выньте щуп. Масло должно быть между отметками min и max. Если оно выглядит молочным или пахнет топливом — запланируйте замену.'),
            ('Проверьте уровень охлаждающей жидкости', 'Посмотрите в расширительный бачок. Проверьте концентрацию антифриза перед зимой — большинство отказов происходит в первые холода.'),
            ('Осмотрите топливные утечки', 'Проверьте раму, топливные фильтры и шланги на влажные пятна. Дизель испаряется и оставляет след задолго до появления явной утечки.'),
            ('Проверьте воздушный фильтр', 'Выньте фильтр и посмотрите индикатор (если установлен). В пыльном месте фильтр нужно менять чаще, чем в чистом машинном зале.'),
            ('Проверьте натяжение ремня', 'Нажмите на ремень вентилятора — он должен прогибаться на 10–15 мм. Слабый ремень вызывает перегрев, треснувший — требует немедленной замены.'),
            ('Проверьте выхлопную систему', 'Осмотрите стыки выхлопа на наличие чёрной сажи, что означает утечку. Проверьте, не корродирует ли гибкое соединение.'),
            ('Протестируйте АВР', 'Симулируйте отключение сети и убедитесь, что генератор запускается, АВР переключает нагрузку, и генератор правильно останавливается при восстановлении сети.'),
            ('Очистите радиатор и рёбра', 'Пыль и насекомые блокируют воздушный поток. Очистите радиатор изнутри наружу воздухом низкого давления. Перегрев — вторая по частоте причина отказа.'),
            ('Запишите наработку и данные нагрузки', 'Зафиксируйте показания счётчика моточасов и среднюю нагрузку во время теста. Это покажет, когда нужно следующее ТО и не перегружен ли генератор.'),
            ('Осмотрите кожух и окружение', 'Удалите листья, гнёзда и стоячую воду. Убедитесь, что вентиляционные жалюзи чистые и агрегат не используется как склад.')
        ],
        'quarterly_h': 'Что делать ежеквартально и ежегодно',
        'quarterly_p': 'Каждые 3 месяца: замена топливных фильтров, проверка плотности электролита, протяжка электрических соединений. Каждые 12 месяцев: полная замена масла и фильтров, проверка зазоров клапанов, осмотр форсунок и нагрузочный тест.',
        'bottom_h': 'Итог',
        'bottom_p': 'Резервный генератор — это страховка. Вы узнаете, работает ли он, только когда он вам понадобится. 10 минут в месяц поддерживают эту страховку в силе.',
        'cta_p': 'Если вы покупаете новый генератор и хотите включить план обслуживания, [свяжитесь с нашей инженерной командой](/contact) — мы предоставим график обслуживания, адаптированный к вашему объекту.'
    },
    'es': {
        'title': 'Lista de Mantenimiento del Generador: 12 Tareas Mensuales',
        'excerpt': 'Un generador de reserva solo funciona si lo mantienes. Aquí está la lista práctica mensual que sigue nuestro equipo de servicio.',
        'intro_p1': 'Un generador diesel es una máquina que está inactiva el 99% del tiempo. El otro 1%, cuando falla la red, debe arrancar, tomar la carga y seguir funcionando sin problemas. Eso solo ocurre si lo mantienes correctamente.',
        'intro_p2': 'Después de instalar cientos de generadores en fábricas, hospitales, centros de datos y edificios comerciales, nuestro equipo de servicio sigue la misma lista mensual.',
        'why_h': 'Por qué importa el mantenimiento mensual',
        'why_p': 'Un generador que nunca funciona también se degrada. El combustible se echa a perder, las baterías se descargan, las mangueras de goma se agrietan y los roedores hacen nidos en el capó. Una revisión mensual de 10 minutos previene el 90% de las averías.',
        'checklist_h': 'La lista de 12 puntos mensuales',
        'items': [
            ('Arranque y prueba del generador', 'Ejecute el generador con al menos 30% de carga durante 30 minutos. Una prueba sin carga no es suficiente: el motor debe alcanzar la temperatura de trabajo.'),
            ('Revise la batería', 'Mida el voltaje de carga (unos 27V para un sistema de 24V). Limpie los terminales. Una batería muerta es la causa #1 de fallo de arranque.'),
            ('Inspeccione el nivel y calidad del aceite', 'Saque la varilla. El aceite debe estar entre las marcas mín y máx. Si parece lechoso o huele a combustible, programe un cambio.'),
            ('Revise el nivel del refrigerante', 'Mire el depósito de expansión. Pruebe la concentración del anticongelante antes del invierno: la mayoría de las averías ocurren en la primera ola de frío.'),
            ('Busque fugas de combustible', 'Revise el chasis, los filtros y las tuberías en busca de manchas húmedas.'),
            ('Inspeccione el filtro de aire', 'Saque el filtro y revise el indicador (si tiene). Un lugar polvoriento necesita cambios más frecuentes.'),
            ('Revise la tensión de la correa', 'Presione la correa del ventilador: debe deflectar 10–15 mm. Una correa floja causa sobrecalentamiento; una agrietada debe cambiarse ya.'),
            ('Verifique el sistema de escape', 'Busque hollín negro en las juntas del escape, lo que indica una fuga.'),
            ('Pruebe el ATS (interruptor de transferencia)', 'Simule un fallo de red y confirme que el generador arranca, el ATS transfiere la carga y el generador se detiene correctamente.'),
            ('Limpie el radiador y las aletas', 'El polvo y los insectos bloquean el flujo de aire. Limpie el radiador de adentro hacia afuera con aire a baja presión.'),
            ('Registre las horas de funcionamiento y datos de carga', 'Anoté el contador horario y la carga promedio durante la prueba. Esto le dice cuándo toca el próximo servicio.'),
            ('Inspeccione el capó y el entorno', 'Elimine hojas, nidos y agua estancada. Asegúrese de que las rejillas de ventilación estén despejadas.')
        ],
        'quarterly_h': 'Qué hacer trimestral y anualmente',
        'quarterly_p': 'Cada 3 meses: cambie filtros de combustible, revise la batería, apriete conexiones. Cada 12 meses: cambio completo de aceite y filtros, revisión de válvulas, inyectores y prueba de carga.',
        'bottom_h': 'Conclusión',
        'bottom_p': 'Un generador de reserva es un seguro. Solo descubre si funciona cuando lo necesitas. Diez minutos al mes mantienen ese seguro vigente.',
        'cta_p': 'Si está comprando un generador nuevo y quiere un plan de mantenimiento incluido, [contacte a nuestro equipo de ingeniería](/contact).'
    }
}

# Generate markdown for each locale
for loc, t in translations.items():
    lines = [
        '---',
        f'title: "{t["title"]}"',
        'date: "2026-10-21"',
        f'excerpt: "{t["excerpt"]}"',
        '---',
        '',
        '![Generator maintenance](/images/blog/generator-maintenance-checklist.jpg)',
        '',
        t['intro_p1'],
        '',
        t['intro_p2'],
        '',
        f'## {t["why_h"]}',
        '',
        t['why_p'],
        '',
        f'## {t["checklist_h"]}',
        '',
    ]
    for i, (h, p) in enumerate(t['items'], 1):
        lines.append(f'### {i}. {h}')
        lines.append('')
        lines.append(p)
        lines.append('')
    lines.extend([
        f'## {t["quarterly_h"]}',
        '',
        t['quarterly_p'],
        '',
        f'## {t["bottom_h"]}',
        '',
        t['bottom_p'],
        '',
        t['cta_p'],
        '',
    ])
    path = f'content/blog/{loc}/generator-maintenance-checklist.md'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'Written {loc}')
