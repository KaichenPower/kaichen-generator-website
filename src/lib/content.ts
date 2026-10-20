import fs from 'fs';
import path from 'path';
import { load } from 'js-yaml';
import { locales } from './site';

export type ProductData = {
  slug: string;
  /** URL 友好 slug，由英文产品全名生成（全语种一致） */
  urlSlug: string;
  name: string;
  brand: string;
  powerKVA: number;
  type: string;
  description?: string;
  image?: string;
  features?: string[];
  specs?: Record<string, string>;
  [key: string]: unknown;
};

/** 把文本转为 URL 友好的小写连字符 slug */
export function slugify(text: string): string {
  return (text || '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

/** 解决方案（行业）slug 列表 —— 对应 content/i18n 中 solutions 分组下的键 */
export const solutionSlugs = [
  'commercial-community',
  'data-center',
  'medical',
  'factory',
  'mining-oil',
  'transportation',
  'agriculture',
  'construction-site',
  'home-backup-power',
] as const;

// 读取全部产品
export function getAllProducts(): ProductData[] {
  const dir = path.join(process.cwd(), 'content', 'products');
  if (!fs.existsSync(dir)) return [];
  const files = fs.readdirSync(dir).filter((f) => f.endsWith('.yaml'));
  return files
    .map((file) => {
      const slug = file.replace('.yaml', '');
      const raw = fs.readFileSync(path.join(dir, file), 'utf8');
      const data = load(raw) as Record<string, unknown>;
      const name = (data.name as string) || slug;
      return { slug, urlSlug: slugify(name), ...data, name } as ProductData;
    })
    .sort((a, b) => (Number(a.powerKVA) || 0) - (Number(b.powerKVA) || 0));
}

// 读取单个产品详情
export function getProductBySlug(slug: string): ProductData | null {
  const filePath = path.join(process.cwd(), 'content', 'products', `${slug}.yaml`);
  if (!fs.existsSync(filePath)) return null;
  const raw = fs.readFileSync(filePath, 'utf8');
  const data = load(raw) as Record<string, unknown>;
  return { slug, urlSlug: slugify((data.name as string) || slug), ...data } as ProductData;
}

// 按 URL slug（英文产品全名）查找产品
export function getProductByUrlSlug(urlSlug: string): ProductData | null {
  return getAllProducts().find((p) => p.urlSlug === urlSlug) || null;
}

// 生成静态语种参数，用于 Next.js 静态页面生成
export function generateLocaleParams() {
  return locales.map((locale) => ({ locale }));
}
