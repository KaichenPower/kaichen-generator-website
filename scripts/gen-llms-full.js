const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const dir = path.join(process.cwd(), 'content', 'products');
const out = ['# Kaichen Power Full Site Context', '', 'This file lists the current exported product catalog and main page inventory for AI assistants.', ''];
const byCat = {};
for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.yaml'))) {
  const doc = yaml.load(fs.readFileSync(path.join(dir, f), 'utf8'));
  if (doc.source !== 'knowledge_base') continue;
  const cat = doc.category || 'other';
  (byCat[cat] ||= []).push(doc);
}
for (const [cat, items] of Object.entries(byCat).sort()) {
  out.push(`## ${cat}`, '');
  for (const p of items) {
    out.push(`- ${p.name} — ${p.powerKVA} kVA standby, image ${p.image}`);
  }
  out.push('');
}
out.push('## Main pages', '', '- /en/ home', '- /en/products/ catalog', '- /en/products/categories/ 11 brand and enclosure categories', '- /en/solutions/ industry applications', '- /en/blog/ buying guides and maintenance articles', '- /en/faq/ technical questions', '- /en/about/ factory profile', '- /en/contact/ enquiry form');
fs.writeFileSync(path.join(process.cwd(), 'public', 'llms-full.txt'), out.join('\n'), 'utf8');
console.log(out.length + ' lines, ' + fs.statSync(path.join(process.cwd(), 'public', 'llms-full.txt')).size + ' bytes');
