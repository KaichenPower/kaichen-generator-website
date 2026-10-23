import type { Metadata } from 'next';
import { getTranslations } from 'next-intl/server';
import { Link } from '@i18n/navigation';
import Breadcrumbs from '../../../components/Breadcrumbs';
import JsonLd from '../../../components/JsonLd';
import { getAlternates, siteConfig } from '@/lib/site';

type Props = { params: Promise<{ locale: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'faqPage' });
  const alternates = getAlternates('/faq');
  return {
    title: t('title'),
    description: t('subtitle'),
    alternates: { canonical: alternates[locale], languages: alternates },
  };
}

export default async function FaqPage({ params }: Props) {
  const { locale } = await params;
  const nav = await getTranslations({ locale, namespace: 'nav' });
  const common = await getTranslations({ locale, namespace: 'common' });
  const t = await getTranslations({ locale, namespace: 'faqPage' });

  // Read FAQs from i18n
  const faqs = t.raw('faqs') as { q: string; a: string }[];

  const abs = (p: string) => `${siteConfig.domain}/${locale}${p}`;
  const crumbs = [
    { label: nav('home'), href: '/', url: abs('/') },
    { label: t('title'), url: abs('/faq') },
  ];

  return (
    <>
      <JsonLd
        data={{
          '@context': 'https://schema.org',
          '@type': 'FAQPage',
          mainEntity: faqs.map((f) => ({
            '@type': 'Question',
            name: f.q,
            acceptedAnswer: { '@type': 'Answer', text: f.a },
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
        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(420px, 1fr))',
            gap: '1.5rem',
          }}
        >
          {faqs.map((f, i) => (
            <div
              key={i}
              style={{
                padding: '1.5rem',
                background: '#fff',
                border: '1px solid #e5e7eb',
                borderLeft: '4px solid var(--color-primary, #0b2a4a)',
                borderRadius: '6px',
              }}
            >
              <h3 style={{ marginTop: 0, fontSize: '1.05rem', color: 'var(--color-primary, #0b2a4a)' }}>
                {f.q}
              </h3>
              <p style={{ marginBottom: 0, fontSize: '0.92rem', lineHeight: 1.7, color: '#444' }}>
                {f.a}
              </p>
            </div>
          ))}
        </div>

        <div style={{ textAlign: 'center', marginTop: '2.5rem' }}>
          <Link href="/contact" className="btn btn-accent">
            {t('askQuestion')}
          </Link>
          <Link
            href="/products"
            className="btn btn-outline"
            style={{ marginLeft: '0.75rem', borderColor: 'var(--color-primary, #0b2a4a)', color: 'var(--color-primary, #0b2a4a)' }}
          >
            {common('allProducts')}
          </Link>
        </div>
      </section>
    </>
  );
}
