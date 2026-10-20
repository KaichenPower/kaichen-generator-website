import type { Metadata } from 'next';
import { getTranslations } from 'next-intl/server';
import { Link } from '@i18n/navigation';
import Breadcrumbs from '../../../components/Breadcrumbs';
import JsonLd from '../../../components/JsonLd';
import { getAlternates, siteConfig } from '@/lib/site';

type Props = { params: Promise<{ locale: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'legal' });
  const alternates = getAlternates('/privacy');
  return {
    title: t('privacyTitle'),
    alternates: { canonical: alternates[locale], languages: alternates },
  };
}

type Section = { heading: string; paragraphs: string[] };

export default async function PrivacyPage({ params }: Props) {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'legal' });
  const nav = await getTranslations({ locale, namespace: 'nav' });
  const privacy = await getTranslations({ locale, namespace: 'privacy' });
  const title = t('privacyTitle');

  // Read sections from i18n
  const sectionCount = 7;
  const sections: Section[] = [];
  for (let i = 1; i <= sectionCount; i++) {
    const heading = privacy(`sections.${i}.heading`);
    const rawParas = privacy.has(`sections.${i}.paragraphs.0`)
      ? privacy.raw(`sections.${i}.paragraphs`)
      : {};
    const paraKeys = Object.keys(rawParas);
    const paragraphs: string[] = [];
    paraKeys.forEach((key) => {
      paragraphs.push(privacy(`sections.${i}.paragraphs.${key}`));
    });
    sections.push({ heading, paragraphs });
  }

  const abs = (p: string) => `${siteConfig.domain}/${locale}${p}`;
  const crumbs = [
    { label: nav('home'), href: '/', url: abs('/') },
    { label: title, url: abs('/privacy') },
  ];

  return (
    <>
      <JsonLd
        data={{
          '@context': 'https://schema.org',
          '@type': 'WebPage',
          name: title,
          url: abs('/privacy'),
          description: title,
        }}
      />
      <section className="page-hero">
        <div className="container">
          <h1>{title}</h1>
          <p>{privacy('lastUpdated')}</p>
        </div>
      </section>
      <Breadcrumbs items={crumbs} />
      <section className="content-block">
        <div className="container" style={{ maxWidth: 820 }}>
          {sections.map((s, i) => (
            <div key={i} style={{ marginBottom: '1.5rem' }}>
              <h2 style={{ fontSize: '1.15rem', color: 'var(--color-primary)', marginTop: '1.5rem' }}>{s.heading}</h2>
              {s.paragraphs.map((p, j) => (
                <p key={j} style={{ lineHeight: 1.7, color: '#3a4656' }}>{p}</p>
              ))}
            </div>
          ))}
          <p>
            <Link href="/contact">{nav('contact')}</Link>
            {' · '}
            <Link href="/products">{nav('products')}</Link>
          </p>
        </div>
      </section>
    </>
  );
}
