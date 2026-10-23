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
  const alternates = getAlternates('/terms');
  return {
    title: t('termsTitle'),
    description: t('termsDescription'),
    alternates: { canonical: alternates[locale], languages: alternates },
  };
}

export default async function TermsPage({ params }: Props) {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'legal' });
  const nav = await getTranslations({ locale, namespace: 'nav' });
  const title = t('termsTitle');
  const body = t.raw('termsBody') as string[];
  const updated = t('updatedLabel');

  const abs = (p: string) => `${siteConfig.domain}/${locale}${p}`;
  const crumbs = [
    { label: nav('home'), href: '/', url: abs('/') },
    { label: title, url: abs('/terms') },
  ];

  return (
    <>
      <JsonLd
        data={{
          '@context': 'https://schema.org',
          '@type': 'WebPage',
          name: title,
          url: abs('/terms'),
        }}
      />
      <section className="page-hero">
        <div className="container">
          <h1>{title}</h1>
          <p className="legal-updated">{updated}</p>
          <div className="legal-body">
            {body.map((para, i) => (
              <p key={i}>{para}</p>
            ))}
            <p>
              <Link href="/privacy">{t('privacyTitle')}</Link>
              {' · '}
              <Link href="/contact">{nav('contact')}</Link>
            </p>
          </div>
        </div>
      </section>
      <Breadcrumbs items={crumbs} />
    </>
  );
}
