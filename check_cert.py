import urllib.request, re

r = urllib.request.urlopen('http://localhost:3000/ar/about', timeout=15)
html = r.read().decode('utf-8')

# Check cert names are translated
for m in re.finditer(r'cert-card-name">(.*?)<', html):
    print('Cert:', m.group(1)[:80])

# Check nav active
active = re.findall(r'nav-link is-active[^>]*>(.*?)<', html)
print('Active nav:', active)

# Check cert tabs
tabs = re.findall(r'cert-tab[^>]*>(.*?)<', html)
print('Cert tabs:', [t.strip()[:50] for t in tabs])
