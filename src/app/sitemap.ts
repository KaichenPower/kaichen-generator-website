import type { MetadataRoute } from 'next';
import { siteConfig, locales } from '@/lib/site';
import { getAllProducts, solutionSlugs } from '@/lib/content';
import { getAllPosts } from '@/lib/blog';

export const dynamic = 'force-static';

// 自动生成 /sitemap.xml：覆盖 10 语种 × 全站页面
export default function sitemap(): MetadataRoute.Sitemap {
  const domain = siteConfig.domain;
  const urls: MetadataRoute.Sitemap = [];

  for (const locale of locales) {
    // 首页
    urls.push({ url: `${domain}/${locale}`, changeFrequency: 'weekly', priority: 1 });

    // 静态栏目
    for (const p of ['/about', '/solutions', '/contact', '/privacy', '/terms']) {
      urls.push({ url: `${domain}/${locale}${p}`, changeFrequency: 'monthly', priority: 0.7 });
    }

    // 产品列表 + 详情（用英文全名 urlSlug）
    urls.push({ url: `${domain}/${locale}/products`, changeFrequency: 'weekly', priority: 0.9 });
    for (const prod of getAllProducts()) {
      urls.push({
        url: `${domain}/${locale}/products/${prod.urlSlug}`,
        changeFrequency: 'weekly',
        priority: 0.8,
      });
    }

    // 行业方案
    for (const s of solutionSlugs) {
      urls.push({ url: `${domain}/${locale}/solutions#${s}`, changeFrequency: 'monthly', priority: 0.6 });
    }

    // 博客列表 + 详情（用标题 urlSlug）
    urls.push({ url: `${domain}/${locale}/blog`, changeFrequency: 'weekly', priority: 0.7 });
    for (const post of getAllPosts(locale)) {
      urls.push({
        url: `${domain}/${locale}/blog/${post.slug}`,
        lastModified: post.date ? new Date(post.date) : undefined,
        changeFrequency: 'weekly',
        priority: 0.6,
      });
    }
  }

  return urls;
}
