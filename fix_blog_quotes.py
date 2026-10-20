# -*- coding: utf-8 -*-
"""Re-write all translated blog files using yaml.dump for proper escaping."""
import yaml as y
import os, importlib.util

# Import the translation data from translate_blog.py
spec = importlib.util.spec_from_file_location("tb", "translate_blog.py")
tb = importlib.util.module_from_spec(spec)

# We can't just exec it because it writes files. Instead, re-define T here by reading the module.
# Simpler: just re-run the file writing part using yaml.dump
exec(open("translate_blog.py", encoding="utf-8").read().split("# Now write files")[0])

for slug, locales in T.items():
    for loc, (title, excerpt) in locales.items():
        d = f'content/blog/{loc}'
        outpath = f'{d}/{slug}.md'
        eng = open(f'content/blog/{slug}.md', encoding='utf-8').read()
        parts = eng.split('---', 2)
        body = parts[2].strip()
        fm = y.safe_load(parts[1])
        date = fm.get('date', '2026-10-16')
        # Use yaml.dump for proper quoting
        fm_str = y.dump({'title': title, 'date': str(date), 'excerpt': excerpt},
                        allow_unicode=True, default_flow_style=False, width=9999)
        content = f'---\n{fm_str}---\n\n{body}\n'
        open(outpath, 'w', encoding='utf-8').write(content)

print('All files re-written with yaml.dump')
