import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { slugify } from './content';

export type BlogPost = {
  /** URL slug，由英文标题全名生成（全语种一致） */
  slug: string;
  title: string;
  date: string;
  excerpt: string;
  image?: string;
  content: string;
};

const dir = path.join(process.cwd(), 'content', 'blog');

// 基础（英文）文件：内部文件名 slug -> 英文标题，用于生成统一的 URL slug
function baseMeta(): Record<string, string> {
  const map: Record<string, string> = {};
  if (!fs.existsSync(dir)) return map;
  const files = fs.readdirSync(dir).filter((f) => f.endsWith('.md'));
  for (const file of files) {
    const internal = file.replace('.md', '');
    try {
      const { data } = matter(fs.readFileSync(path.join(dir, file), 'utf8'));
      map[internal] = (data.title as string) || internal;
    } catch {
      map[internal] = internal;
    }
  }
  return map;
}

// 由 URL slug 反查内部文件名 slug
function internalByUrlSlug(urlSlug: string): string | null {
  const meta = baseMeta();
  for (const [internal, title] of Object.entries(meta)) {
    if (slugify(title) === urlSlug) return internal;
  }
  return null;
}

export function getAllPosts(locale: string = 'en'): BlogPost[] {
  const meta = baseMeta();
  const posts = Object.entries(meta)
    .map(([internal]) => {
      const urlSlug = slugify(meta[internal]);
      return getPostBySlug(urlSlug, locale);
    })
    .filter((p): p is BlogPost => p !== null)
    .sort((a, b) => (a.date < b.date ? 1 : -1));
  return posts;
}

export function getPostBySlug(slug: string, locale: string = 'en'): BlogPost | null {
  const internal = internalByUrlSlug(slug);
  if (!internal) return null;
  const localePath = path.join(dir, locale, `${internal}.md`);
  const basePath = path.join(dir, `${internal}.md`);
  const filePath = fs.existsSync(localePath) ? localePath : basePath;
  if (!fs.existsSync(filePath)) return null;
  const raw = fs.readFileSync(filePath, 'utf8');
  const { data, content } = matter(raw);
  // 自动从正文提取第一张图作为封面（frontmatter 未指定 image 时）
  let image = data.image as string | undefined;
  if (!image) {
    const m = content.match(/!\[[^\]]*\]\(([^)]+)\)/);
    if (m) image = m[1];
  }
  return {
    slug,
    title: (data.title as string) || slug,
    date: (data.date as string) || '',
    excerpt: (data.excerpt as string) || '',
    image,
    content,
  };
}

/**
 * Markdown 渲染器：把博客正文转为 HTML。
 * 支持 ## / ### 标题、- 无序列表、1. 有序列表、加粗 **text**、行内代码、
 * 图片 ![alt](src)、表格（| a | b | + 分隔行）、链接 [text](url) 与段落。
 * 内部链接自动加上 locale 前缀。
 */
export function renderMarkdownToHtml(md: string, locale: string = 'en'): string {
  const lines = md.split('\n');
  const html: string[] = [];
  let inUl = false;
  let inOl = false;

  const closeLists = () => {
    if (inUl) { html.push('</ul>'); inUl = false; }
    if (inOl) { html.push('</ol>'); inOl = false; }
  };

  const inline = (s: string) => {
    let out = s;
    // images inline: ![alt](src)
    out = out.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, '<img src="$2" alt="$1" loading="lazy" class="post-inline-img" />');
    // links: [text](url) - 内部链接自动加 locale 前缀
    out = out.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (match, text, url) => {
      // 外部链接（http/https）保持原样，加 target="_blank"
      if (url.startsWith('http://') || url.startsWith('https://') || url.startsWith('#')) {
        return `<a href="${url}" target="_blank" rel="noopener">${text}</a>`;
      }
      // 内部链接加上 locale 前缀
      const normalizedUrl = url.startsWith('/') ? url : `/${url}`;
      return `<a href="/${locale}${normalizedUrl}">${text}</a>`;
    });
    out = out.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    out = out.replace(/`(.+?)`/g, '<code>$1</code>');
    return out;
  };

  const isTableRow = (l: string) => /^\|.*\|\s*$/.test(l.trim());
  const isTableSep = (l: string) => /^\|[\s:|-]+\|\s*$/.test(l.trim()) && l.includes('-');
  const splitRow = (l: string) => l.trim().replace(/^\|/, '').replace(/\|$/, '').split('|').map((c) => c.trim());

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const t = line.trim();

    // table block: header row + separator
    if (isTableRow(line) && i + 1 < lines.length && isTableSep(lines[i + 1])) {
      closeLists();
      const header = splitRow(line);
      let r = i + 2;
      const rows: string[][] = [];
      while (r < lines.length && isTableRow(lines[r])) {
        rows.push(splitRow(lines[r]));
        r++;
      }
      let table = '<table><thead><tr>';
      header.forEach((c) => { table += `<th>${inline(c)}</th>`; });
      table += '</tr></thead><tbody>';
      rows.forEach((row) => {
        table += '<tr>';
        row.forEach((c) => { table += `<td>${inline(c)}</td>`; });
        table += '</tr>';
      });
      table += '</tbody></table>';
      html.push(table);
      i = r - 1;
      continue;
    }

    // standalone image paragraph
    const imgMatch = t.match(/^!\[([^\]]*)\]\(([^)]+)\)$/);
    if (imgMatch) {
      closeLists();
      html.push(`<figure class="post-figure"><img src="${imgMatch[2]}" alt="${imgMatch[1]}" loading="lazy" /></figure>`);
      continue;
    }

    if (t.startsWith('## ')) { closeLists(); html.push(`<h2>${inline(t.slice(3))}</h2>`); }
    else if (t.startsWith('### ')) { closeLists(); html.push(`<h3>${inline(t.slice(4))}</h3>`); }
    else if (/^- /.test(t)) {
      if (!inUl) { closeLists(); html.push('<ul>'); inUl = true; }
      html.push(`<li>${inline(t.slice(2))}</li>`);
    } else if (/^\d+\.\s/.test(t)) {
      if (!inOl) { closeLists(); html.push('<ol>'); inOl = true; }
      html.push(`<li>${inline(t.replace(/^\d+\.\s/, ''))}</li>`);
    } else if (t === '') { closeLists(); }
    else { closeLists(); html.push(`<p>${inline(t)}</p>`); }
  }
  closeLists();
  return html.join('\n');
}
