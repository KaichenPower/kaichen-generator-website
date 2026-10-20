import json

de = {
    "lastUpdated": "Letzte Aktualisierung: Oktober 2026",
    "sections": {
        "1": {"heading": "1. Einführung", "paragraphs": [
            "Willkommen auf www.cnkcpower.com (nachfolgend 'wir' oder die 'Website'). Wir verpflichten uns, Ihre Privatsphaere zu schuetzen und Ihnen eine positive Erfahrung beim Besuch unserer Website zu bieten.",
            "Diese Cookie-Datenschutzrichtlinie erklärt, was Cookies sind, wie wir sie verwenden, welche Arten von Cookies wir einsetzen und wie Sie diese kontrollieren oder löschen können.",
            "Durch die Nutzung unserer Website stimmen Sie der Verwendung von Cookies gemäß dieser Richtlinie zu. Wenn Sie damit nicht einverstanden sind, passen Sie bitte Ihre Browsereinstellungen an."
        ]},
        "2": {"heading": "2. Was sind Cookies?", "paragraphs": [
            "Cookies sind kleine Textdateien, die auf Ihrem Gerät (Computer, Smartphone, Tablet) gespeichert werden, wenn Sie eine Website besuchen. Sie verbessern die Funktionsweise und Nutzererfahrung.",
            "Cookies können Sitzungscookies (temporär), dauerhafte Cookies (festgelegter Zeitraum), Erstanbieter-Cookies (von der besuchten Website) oder Drittanbieter-Cookies (Werbung, Analyse) sein."
        ]},
        "3": {"heading": "3. Wie wir Cookies verwenden", "paragraphs": [
            "Unbedingt erforderliche Cookies: Notwendig für die Funktion der Website (Sicherheit, Sprache). Speichern keine personenbezogenen Daten und können nicht deaktiviert werden.",
            "Leistungs- und Analyse-Cookies: Helfen uns zu verstehen, wie Besucher die Website nutzen (anonym). Nur nach Ihrer Einwilligung.",
            "Funktions-Cookies: Merken sich Ihre Auswahl (Sprache, Region) für eine personalisiertere Erfahrung.",
            "Targeting- und Werbe-Cookies: Zeigen relevante Werbung basierend auf Ihren Interessen."
        ]},
        "4": {"heading": "4. Drittanbieter-Cookies", "paragraphs": [
            "Wir arbeiten mit Drittanbietern zusammen (Analyse, Werbenetzwerke, soziale Medien), die Cookies auf Ihrem Gerät setzen können.",
            "Diese Drittanbieter haben eigene Datenschutzrichtlinien. Wir kontrollieren das Setzen dieser Cookies nicht."
        ]},
        "5": {"heading": "5. Ihre Rechte", "paragraphs": [
            "Gemäß DSGVO (EWR und UK) können Sie Ihre Einwilligung jederzeit widerrufen, Auskunft über Ihre Daten verlangen oder deren Löschung beantragen.",
            "Gemäß CCPA/CPRA (Kalifornien) haben Sie das Recht zu erfahren, welche personenbezogenen Daten erhoben werden, und deren Löschung zu verlangen. Wir verkaufen Ihre Daten nicht.",
            "Sie können Cookies über Ihre Browsereinstellungen verwalten und löschen."
        ]},
        "6": {"heading": "6. Änderungen dieser Richtlinie", "paragraphs": [
            "Wir können diese Richtlinie gelegentlich aktualisieren. Änderungen werden auf dieser Seite mit aktualisiertem Datum veröffentlicht."
        ]},
        "7": {"heading": "7. Kontakt", "paragraphs": [
            "Jiangsu Kaichen Power Equipment Co., Ltd.",
            "Adresse: Dinghuo Industrial Park, Jiangdu District, Yangzhou City, Jiangsu, China.",
            "Email: cnkcpower@gmail.com | Tel: +86-18012341322"
        ]}
    }
}

pt = {
    "lastUpdated": "Última atualização: Outubro 2026",
    "sections": {
        "1": {"heading": "1. Introdução", "paragraphs": [
            "Bem-vindo ao www.cnkcpower.com (doravante 'nos' ou o 'Site'). Estamos comprometidos em proteger sua privacidade e garantir uma experiencia positiva ao navegar em nosso Site.",
            "Esta Política de Privacidade de Cookies explica o que são cookies, como os usamos, os tipos de cookies que utilizamos e como você pode controlá-los ou excluí-los.",
            "Ao usar nosso Site, você consente com o uso de cookies de acordo com esta Política. Se você não concorda, ajuste as configurações do seu navegador."
        ]},
        "2": {"heading": "2. O que são Cookies?", "paragraphs": [
            "Cookies são pequenos arquivos de texto colocados no seu dispositivo (computador, smartphone, tablet) quando você visita um site. Eles melhoram o funcionamento e a experiência do usuário.",
            "Cookies podem ser de sessão (temporários), persistentes (período definido), próprios (do site visitado) ou de terceiros (anúncios, análise)."
        ]},
        "3": {"heading": "3. Como usamos Cookies", "paragraphs": [
            "Cookies estritamente necessários: Essenciais para o funcionamento do Site (segurança, idioma). Não armazenam dados pessoais e não podem ser desativados.",
            "Cookies de desempenho e análise: Ajudam a entender como os visitantes usam o Site (informações anônimas). Carregados apenas após consentimento.",
            "Cookies de funcionalidade: Lembram suas preferências (idioma, região) para uma experiência mais personalizada.",
            "Cookies de segmentação e publicidade: Exibem anúncios relevantes aos seus interesses."
        ]},
        "4": {"heading": "4. Cookies de Terceiros", "paragraphs": [
            "Trabalhamos com provedores terceirizados (análise, redes de publicidade, redes sociais) que podem definir cookies no seu dispositivo.",
            "Esses terceiros têm suas próprias políticas de privacidade. Não controlamos a definição desses cookies."
        ]},
        "5": {"heading": "5. Seus Direitos", "paragraphs": [
            "De acordo com o GDPR (EEE e Reino Unido), você pode dar ou retirar seu consentimento a qualquer momento, solicitar acesso ou exclusão dos seus dados pessoais.",
            "De acordo com a CCPA/CPRA (Califórnia), você tem o direito de saber quais dados são coletados e solicitar sua exclusão. Não vendemos seus dados.",
            "Você pode gerenciar e excluir cookies nas configurações do seu navegador."
        ]},
        "6": {"heading": "6. Alterações nesta Política", "paragraphs": [
            "Podemos atualizar esta política periodicamente. As alterações serão publicadas nesta página com a data atualizada."
        ]},
        "7": {"heading": "7. Contate-nos", "paragraphs": [
            "Jiangsu Kaichen Power Equipment Co., Ltd.",
            "Endereço: Dinghuo Industrial Park, Jiangdu District, Yangzhou City, Jiangsu, China.",
            "Email: cnkcpower@gmail.com | Tel: +86-18012341322"
        ]}
    }
}

for loc, data in [('de', de), ('pt', pt)]:
    with open(f'content/i18n/{loc}.json','r',encoding='utf-8') as f:
        full = json.load(f)
    full['privacy'] = data
    with open(f'content/i18n/{loc}.json','w',encoding='utf-8') as f:
        json.dump(full, f, ensure_ascii=False, indent=2)
    print(f"Updated {loc}")
