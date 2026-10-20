import urllib.request, re

# Check power units on product listing pages
print("=== Power units on product listing ===")
for loc in ['ar', 'th', 'ru', 'es', 'de', 'fr']:
    url = f'http://localhost:3000/{loc}/products'
    r = urllib.request.urlopen(url, timeout=10)
    html = r.read().decode('utf-8')
    # Find power unit displays
    kw_matches = re.findall(r'(\d+)\s*(kW|kVA|كيلوواط|كيلو فولت|кВт|кВА|กิโลวัตต์|กิโลโวลต์)', html)
    print(f'{loc:4s}: {kw_matches[:6]}')

# Check a blog detail page
print("\n=== Blog detail page content (Arabic) ===")
url = 'http://localhost:3000/ar/blog/why-data-centers-and-hospitals-move-up-to-a-500kw-backup-set'
r = urllib.request.urlopen(url, timeout=10)
html = r.read().decode('utf-8')
# Check if blog body has English power units
eng_kw = re.findall(r'\d+\s*kW\b', html)
print(f'English kW in Arabic blog: {eng_kw[:10]}')
# Check Arabic power units present
ar_kw = re.findall(r'كيلوواط|كيلو فولت', html)
print(f'Arabic power units found: {len(ar_kw)} occurrences')

# Check related posts section
print("\n=== Related posts on blog detail ===")
related = re.findall(r'related-post.*?<h[23][^>]*>(.*?)</h[23]>', html, re.DOTALL)
print(f'Related posts found: {len(related)}')
