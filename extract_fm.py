# -*- coding: utf-8 -*-
import yaml, glob, io
out = io.open('blog_frontmatter.txt','w',encoding='utf-8')
for f in sorted(glob.glob('content/blog/*.md')):
    raw = open(f,encoding='utf-8').read()
    parts = raw.split('---',2)
    fm = yaml.safe_load(parts[1])
    internal = f.replace('\\','/').split('/')[-1].replace('.md','')
    out.write(f'=== {internal} ===\n')
    out.write(f'title: {fm["title"]}\n')
    out.write(f'excerpt: {fm["excerpt"]}\n\n')
out.close()
print('done')
