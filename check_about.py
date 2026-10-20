import urllib.request, re

r = urllib.request.urlopen('http://localhost:3000/ar/about', timeout=15)
html = r.read().decode('utf-8')

# Find certificate names in visible content
certs = re.findall(r'>(ISO\s*\d+|CE|GB/T\s*\d+)<', html)
print('Cert names in visible HTML:', set(certs))

# Find all text near "certificate" or "شهادة"
for m in re.finditer(r'>([^<]*(?:ISO|CE|GB/T|شهادة|certif)[^<]*)<', html, re.IGNORECASE):
    text = m.group(1).strip()
    if text and len(text) > 2:
        print(f'  Text: {text[:100]}')

# Check nav active
print('\n--- Nav links ---')
for m in re.finditer(r'<a[^>]*href="[^"]*about[^"]*"[^>]*>(.*?)</a>', html, re.DOTALL):
    print(f'  About link: {m.group(0)[:200]}')
