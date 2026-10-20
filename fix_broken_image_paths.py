# -*- coding: utf-8 -*-
import os, re, glob

# Restore image paths that were broken by power unit replacement.
# Pattern in markdown: ![alt](/images/blog/blog-XXX-NNNkw-YYY.jpg)
# After bad replacement: ![alt](/images/blog/blog-XXX-NNN كيلوواط-YYY.jpg) or NNN กิโลวัตต์-...
# We need to fix only inside the (path) portion.

# All image slugs that exist in content/blog/*.md originals - we can derive from the alt text.
# Safer approach: in each file, find image markdown and restore the URL portion.

def fix_image_paths(filepath, locale):
    raw = open(filepath, encoding='utf-8').read()
    # Find all ![...](path) patterns and fix the path
    def fix_path(m):
        alt = m.group(1)
        path = m.group(2)
        # Restore: replace <num> كيلوواط -> <num>kw, <num> กิโลวัตต์ -> <num>kw
        # Also handle kVA variant if any in paths (unlikely)
        fixed = re.sub(r'(\d[\d,.]*)\s*كيلوواط', r'\1kw', path)
        fixed = re.sub(r'(\d[\d,.]*)\s*กิโลวัตต์', r'\1kw', fixed)
        fixed = re.sub(r'(\d[\d,.]*)\s*كيلو فولت أمبير', r'\1kVA', fixed)
        fixed = re.sub(r'(\d[\d,.]*)\s*กิโลโวลต์แอมแปร์', r'\1kVA', fixed)
        return f'![{alt}]({fixed})'
    new = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', fix_path, raw)
    if new != raw:
        open(filepath, 'w', encoding='utf-8').write(new)
        return True
    return False

count = 0
for loc in ['ar', 'th']:
    files = glob.glob(os.path.join('content/blog', loc, '*.md'))
    for fp in files:
        if fix_image_paths(fp, loc):
            count += 1
            print(f'Fixed image: {loc}/{os.path.basename(fp)}')
print(f'Done! {count} files fixed.')
