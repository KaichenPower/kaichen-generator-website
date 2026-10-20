import json

# Spanish
es = {
    "lastUpdated": "Última actualización: Octubre 2026",
    "sections": {
        "1": {"heading": "1. Introducción", "paragraphs": [
            "Bienvenido a www.cnkcpower.com (en adelante, \"nosotros\", \"nos\", \"nuestro\" o el \"Sitio\"). Estamos comprometidos a proteger su privacidad y garantizar una experiencia positiva al navegar por nuestro Sitio.",
            "Esta Política de Privacidad de Cookies explica qué son las cookies, cómo las usamos, los tipos de cookies que utilizamos y cómo puede controlarlas o eliminarlas. Esta Política forma parte de nuestra Política de Privacidad más amplia.",
            "Al utilizar nuestro Sitio, usted consiente el uso de cookies de acuerdo con esta Política. Si no está de acuerdo con nuestro uso de cookies, ajuste la configuración de su navegador o deje de utilizar el Sitio."
        ]},
        "2": {"heading": "2. ¿Qué son las Cookies?", "paragraphs": [
            "Las cookies son pequeños archivos de texto que se colocan en su dispositivo cuando visita un sitio web. Se utilizan ampliamente para que los sitios web funcionen de manera más eficiente y mejoren la experiencia del usuario.",
            "Las cookies pueden ser de sesión (temporales), persistentes (por un período determinado), propias (del sitio que visita) o de terceros (anunciantes o servicios de análisis)."
        ]},
        "3": {"heading": "3. Cómo usamos las Cookies", "paragraphs": [
            "Cookies estrictamente necesarias: Esenciales para el funcionamiento del Sitio (seguridad, idioma). No almacenan información personal y no se pueden desactivar.",
            "Cookies de análisis: Nos ayudan a entender cómo los visitantes usan el Sitio mediante información anónima. Solo se cargan con su consentimiento.",
            "Cookies de funcionalidad: Permiten que el Sitio recuerde sus preferencias (idioma, región) para una experiencia más personalizada.",
            "Cookies publicitarias: Se usan para mostrar anuncios relevantes a sus intereses y medir la eficacia de las campañas."
        ]},
        "4": {"heading": "4. Cookies de Terceros", "paragraphs": [
            "Trabajamos con proveedores terceros que pueden colocar cookies en su dispositivo, como servicios de análisis, redes publicitarias y plataformas sociales.",
            "Estos terceros tienen sus propias políticas de privacidad. No controlamos la colocación de estas cookies."
        ]},
        "5": {"heading": "5. Sus Derechos", "paragraphs": [
            "Según el RGPD (EEA y Reino Unido), puede dar o retirar su consentimiento en cualquier momento, solicitar acceso o eliminación de sus datos personales.",
            "Según la CCPA/CPRA (California), tiene derecho a saber qué datos se recopilan y solicitar su eliminación. No vendemos sus datos.",
            "Puede controlar las cookies desde la configuración de su navegador."
        ]},
        "6": {"heading": "6. Cambios a esta Política", "paragraphs": [
            "Podemos actualizar esta política ocasionalmente. Los cambios se publicarán en esta página con la fecha de actualización."
        ]},
        "7": {"heading": "7. Contáctenos", "paragraphs": [
            "Jiangsu Kaichen Power Equipment Co., Ltd.",
            "Dirección: Dinghuo Industrial Park, Jiangdu District, Yangzhou City, Jiangsu, China.",
            "Email: cnkcpower@gmail.com | Tel: +86-18012341322"
        ]}
    }
}

# French
fr = {
    "lastUpdated": "Dernière mise à jour : Octobre 2026",
    "sections": {
        "1": {"heading": "1. Introduction", "paragraphs": [
            "Bienvenue sur www.cnkcpower.com (ci-après « nous » ou le « Site »). Nous nous engageons à protéger votre vie privée et à vous offrir une expérience positive.",
            "Cette Politique de cookies explique ce que sont les cookies, comment nous les utilisons et comment vous pouvez les contrôler. Cette Politique fait partie de notre Politique de confidentialité.",
            "En utilisant notre Site, vous consentez à l'utilisation des cookies. Si vous n'acceptez pas, veuillez ajuster les paramètres de votre navigateur."
        ]},
        "2": {"heading": "2. Que sont les Cookies ?", "paragraphs": [
            "Les cookies sont de petits fichiers texte placés sur votre appareil lorsque vous visitez un site web. Ils rendent les sites plus efficaces et améliorent l'expérience utilisateur.",
            "Les cookies peuvent être de session (temporaires), persistants (durée déterminée), internes (du site visité) ou tiers (annonceurs, analyse)."
        ]},
        "3": {"heading": "3. Comment utilisons-nous les Cookies", "paragraphs": [
            "Cookies strictement nécessaires : Essentiels au fonctionnement du Site (sécurité, langue). Aucune donnée personnelle, impossible à désactiver.",
            "Cookies d'analyse : Ils nous aident à comprendre l'utilisation du Site via des informations anonymes. Chargés uniquement après consentement.",
            "Cookies de fonctionnalité : Ils mémorisent vos préférences (langue, région) pour une expérience personnalisée.",
            "Cookies publicitaires : Ils diffusent des publicités adaptées à vos centres d'intérêt."
        ]},
        "4": {"heading": "4. Cookies de Tiers", "paragraphs": [
            "Nous travaillons avec des prestataires tiers (analyse, publicité, réseaux sociaux) qui peuvent déposer des cookies sur votre appareil.",
            "Ces tiers ont leurs propres politiques de confidentialité. Nous ne contrôlons pas ces cookies."
        ]},
        "5": {"heading": "5. Vos Droits", "paragraphs": [
            "Selon le RGPD (EEE et Royaume-Uni), vous pouvez donner ou retirer votre consentement à tout moment, accéder ou supprimer vos données.",
            "Selon le CCPA/CPRA (Californie), vous avez le droit de savoir quelles données sont collectées et de demander leur suppression. Nous ne vendons pas vos données.",
            "Vous pouvez gérer les cookies via les paramètres de votre navigateur."
        ]},
        "6": {"heading": "6. Modifications", "paragraphs": [
            "Nous pouvons mettre à jour cette politique. Les modifications seront publiées sur cette page."
        ]},
        "7": {"heading": "7. Nous Contacter", "paragraphs": [
            "Jiangsu Kaichen Power Equipment Co., Ltd.",
            "Adresse : Dinghuo Industrial Park, Jiangdu District, Yangzhou City, Jiangsu, Chine.",
            "Email : cnkcpower@gmail.com | Tél : +86-18012341322"
        ]}
    }
}

for loc, data in [('es', es), ('fr', fr)]:
    with open(f'content/i18n/{loc}.json','r',encoding='utf-8') as f:
        full = json.load(f)
    full['privacy'] = data
    with open(f'content/i18n/{loc}.json','w',encoding='utf-8') as f:
        json.dump(full, f, ensure_ascii=False, indent=2)
    print(f"Updated {loc}")
