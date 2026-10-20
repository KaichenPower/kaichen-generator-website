import type { Metadata } from 'next';
import { getTranslations } from 'next-intl/server';
import { Link } from '@i18n/navigation';
import { solutionSlugs } from '../../../lib/content';
import Breadcrumbs from '../../../components/Breadcrumbs';
import JsonLd from '../../../components/JsonLd';
import { getAlternates, siteConfig } from '@/lib/site';

type Props = { params: Promise<{ locale: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'solutions' });
  const alternates = getAlternates('/solutions');
  return {
    title: t('title'),
    description: t('subtitle'),
    alternates: { canonical: alternates[locale], languages: alternates },
  };
}

const icons: Record<string, string> = {
  'commercial-community': '🏢',
  'data-center': '🖥️',
  medical: '🏥',
  factory: '🏭',
  'mining-oil': '⛏️',
  transportation: '🚆',
  agriculture: '🌾',
  'construction-site': '🚧',
  'home-backup-power': '🏠',
};

export default async function SolutionsPage({ params }: Props) {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'solutions' });
  const nav = await getTranslations({ locale, namespace: 'nav' });
  const common = await getTranslations({ locale, namespace: 'common' });

  const abs = (p: string) => `${siteConfig.domain}/${locale}${p}`;
  const crumbs = [
    { label: nav('home'), href: '/', url: abs('/') },
    { label: nav('solutions'), url: abs('/solutions') },
  ];

  return (
    <>
      <JsonLd
        data={{
          '@context': 'https://schema.org',
          '@type': 'ItemList',
          name: t('title'),
          description: t('subtitle'),
          itemListElement: solutionSlugs.map((slug, i) => ({
            '@type': 'ListItem',
            position: i + 1,
            name: t(`${slug}.name`),
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
        <div className="solution-grid">
          {solutionSlugs.map((slug) => (
            <div key={slug} className="solution-card">
              <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>
                {icons[slug] || '⚡'}
              </div>
              <h3>{t(`${slug}.name`)}</h3>
              <p>{t(`${slug}.desc`)}</p>
            </div>
          ))}
        </div>
        <div style={{ textAlign: 'center', marginTop: '2.5rem' }}>
          <Link href="/products" className="btn btn-accent">
            {common('allProducts')}
          </Link>
          <Link href="/contact" className="btn btn-outline" style={{ borderColor: 'var(--color-primary)', color: 'var(--color-primary)', marginLeft: '0.5rem' }}>
            {nav('contact')}
          </Link>
        </div>
      </section>
    </>
  );
}
