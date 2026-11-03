const fs = require('fs');
const path = require('path');
const outDir = path.join(process.cwd(), 'out');
let count = 0;
function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full);
    else if (entry.name === 'index.txt') {
      fs.unlinkSync(full);
      count++;
    }
  }
}
if (fs.existsSync(outDir)) walk(outDir);
console.log(`Removed ${count} RSC index.txt files`);
