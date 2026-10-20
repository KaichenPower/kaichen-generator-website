import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { getTranslations } from 'next-intl/server';
import { Link } from '@i18n/navigation';
import { getAllPosts, getPostBySlug, renderMarkdownToHtml } from '../../../../lib/blog';
import Breadcrumbs from '../../../../components/Breadcrumbs';
import JsonLd from '../../../../components/JsonLd';
import { getAlternates, siteConfig } from '@/lib/site';

type Props = { params: Promise<{ locale: string; slug: string }> };

export function generateStaticParams() {
  return getAllPosts().map((p) => ({ slug: p.slug }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale, slug } = await params;
  const post = getPostBySlug(slug, locale);
  if (!post) return {};
  const alternates = getAlternates(`/blog/${slug}`);
  return {
    title: post.title,
    description: post.excerpt,
    alternates: { canonical: alternates[locale], languages: alternates },
  };
}

export default async function BlogPostPage({ params }: Props) {
  const { locale, slug } = await params;
  const t = await getTranslations({ locale, namespace: 'blogPage' });
  const nav = await getTranslations({ locale, namespace: 'nav' });
  const common = await getTranslations({ locale, namespace: 'common' });
  const post = getPostBySlug(slug, locale);
  if (!post) notFound();

  const bodyHtml = renderMarkdownToHtml(post.content);

  // 估算阅读时长：约 200 词/分钟
  const wordCount = post.content.trim().split(/\s+/).length;
  const readMin = Math.max(1, Math.round(wordCount / 200));

  // 相关文章：排除当前篇，按日期取 3 篇
  const related = getAllPosts(locale).filter((p) => p.slug !== slug).slice(0, 3);

  const abs = (p: string) => `${siteConfig.domain}/${locale}${p}`;
  const crumbs = [
    { label: nav('home'), href: '/', url: abs('/') },
    { label: nav('blog'), href: '/blog', url: abs('/blog') },
    { label: post.title, url: abs(`/blog/${slug}`) },
  ];

  return (
    <>
      <JsonLd
        data={{
          '@context': 'https://schema.org',
          '@type': 'BlogPosting',
          headline: post.title,
          description: post.excerpt,
          datePublished: post.date,
          dateModified: post.date,
          inLanguage: locale,
          image: post.image ? `${siteConfig.domain}${post.image}` : `${siteConfig.domain}/logo.png`,
          author: { '@type': 'Organization', name: siteConfig.brandName },
          publisher: { '@type': 'Organization', name: siteConfig.brandName },
          mainEntityOfPage: abs(`/blog/${slug}`),
        }}
      />

      <div className="page-hero page-hero--blog">
        <div className="container">
          <h1>{post.title}</h1>
        </div>
      </div>

      <Breadcrumbs items={crumbs} />

      <article className="blog-article">
        <div className="blog-meta">
          <span className="blog-meta-date">
            <svg className="blog-date-icon" viewBox="0 0 24 24" width="14" height="14" fill="currentColor" aria-hidden="true">
              <path d="M7 2h2v2h6V2h2v2h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2V2Zm-1 6v11h12V8H6Zm2 3h2v2H8v-2Zm4 0h2v2h-2v-2Zm-4 4h2v2H8v-2Zm4 0h2v2h-2v-2Z"/>
            </svg>
            <strong>{t('posted')}</strong> {post.date}
          </span>
          <span aria-hidden="true">·</span>
          <span>
            {readMin} {t('readTime')}
          </span>
          <span aria-hidden="true">·</span>
          <span>{siteConfig.brandName}</span>
        </div>
        <div
          className="blog-body"
          dangerouslySetInnerHTML={{ __html: bodyHtml }}
        />
        <p style={{ marginTop: '2rem' }}>
          <Link href="/blog" className="btn btn-accent">
            ← {t('backToBlog')}
          </Link>
        </p>
      </article>

      {related.length > 0 && (
        <section className="section section-alt">
          <div className="container">
            <div className="section-head">
              <h2>{common('relatedPosts')}</h2>
            </div>
            <div className="blog-list">
              {related.map((r) => (
                <Link key={r.slug} href={`/blog/${r.slug}`} className="blog-card">
                  <span className="blog-date">
                    <svg className="blog-date-icon" viewBox="0 0 24 24" width="14" height="14" fill="currentColor" aria-hidden="true">
                      <path d="M7 2h2v2h6V2h2v2h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2V2Zm-1 6v11h12V8H6Zm2 3h2v2H8v-2Zm4 0h2v2h-2v-2Zm-4 4h2v2H8v-2Zm4 0h2v2h-2v-2Z"/>
                    </svg>
                    {r.date}
                  </span>
                  <h3>{r.title}</h3>
                  <p>{r.excerpt}</p>
                  <span className="btn-link">{common('learnMore')}</span>
                </Link>
              ))}
            </div>
          </div>
        </section>
      )}
    </>
  );
}
