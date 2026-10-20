import type { Metadata } from 'next';
import { getTranslations } from 'next-intl/server';
import { Link } from '@i18n/navigation';
import { getAllPosts } from '../../../lib/blog';
import BlogList from '../../../components/BlogList';
import Breadcrumbs from '../../../components/Breadcrumbs';
import JsonLd from '../../../components/JsonLd';
import { getAlternates, siteConfig } from '@/lib/site';

type Props = { params: Promise<{ locale: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'blogPage' });
  const alternates = getAlternates('/blog');
  return {
    title: t('title'),
    description: t('subtitle'),
    alternates: { canonical: alternates[locale], languages: alternates },
  };
}

export default async function BlogPage({ params }: Props) {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'blogPage' });
  const nav = await getTranslations({ locale, namespace: 'nav' });
  const common = await getTranslations({ locale, namespace: 'common' });
  const posts = getAllPosts(locale);

  const abs = (p: string) => `${siteConfig.domain}/${locale}${p}`;
  const crumbs = [
    { label: nav('home'), href: '/', url: abs('/') },
    { label: nav('blog'), url: abs('/blog') },
  ];

  return (
    <>
      <JsonLd
        data={{
          '@context': 'https://schema.org',
          '@type': 'ItemList',
          name: t('title'),
          itemListElement: posts.map((p, i) => ({
            '@type': 'ListItem',
            position: i + 1,
            name: p.title,
            url: abs(`/blog/${p.slug}`),
          })),
        }}
      />

      <section className="page-hero">
        <div className="container">
          <h1>{t('title')}</h1>
          <p>{t('subtitle')}</p>
        </div>
      </section>

      <Breadcrumbs items={crumbs} />

      <section className="content-block">
        <BlogList posts={posts} />
        <div style={{ textAlign: 'center', marginTop: '2.5rem' }}>
          <Link href="/products" className="btn btn-accent">
            {common('allProducts')}
          </Link>
        </div>
      </section>
    </>
  );
}
