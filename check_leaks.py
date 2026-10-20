import urllib.request, re

locales_to_check = ['ar', 'th', 'ru', 'es', 'fr', 'de', 'pt', 'tr', 'vi', 'id']
pages = ['', '/products', '/blog', '/contact', '/about']

# Common English UI strings that should NOT appear in non-English pages
checks = [
    'View Details', 'Get Quote', 'Read More', 'About Us',
    'Privacy Policy', 'Terms of', 'Back to',
    'Load More', 'Showing', 'Results',
]

for loc in locales_to_check:
    issues = []
    for page in pages:
        url = f'http://localhost:3000/{loc}{page}'
        try:
            r = urllib.request.urlopen(url, timeout=10)
            html = r.read().decode('utf-8')
            for eng in checks:
                if re.search(r'>\s*' + re.escape(eng) + r'\s*<', html):
                    issues.append(f'{page}: "{eng}"')
        except Exception as e:
            issues.append(f'{page}: ERROR {e}')
    if issues:
        print(f'=== {loc} ===')
        for i in issues:
            print(f'  {i}')
    else:
        print(f'{loc}: OK')
