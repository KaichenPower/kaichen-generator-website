import type { Metadata } from 'next';
import { getTranslations } from 'next-intl/server';
import { Link } from '@i18n/navigation';
import { getAlternates, siteConfig } from '../../../lib/site';
import EnquiryForm from '../../../components/EnquiryForm';
import Breadcrumbs from '../../../components/Breadcrumbs';
import JsonLd from '../../../components/JsonLd';

type Props = { params: Promise<{ locale: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'contactPage' });
  const alternates = getAlternates('/contact');
  return {
    title: t('title'),
    description: t('subtitle'),
    alternates: { canonical: alternates[locale], languages: alternates },
  };
}

export default async function ContactPage({ params }: Props) {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'contactPage' });
  const nav = await getTranslations({ locale, namespace: 'nav' });
  const common = await getTranslations({ locale, namespace: 'common' });

  const abs = (p: string) => `${siteConfig.domain}/${locale}${p}`;
  const crumbs = [
    { label: nav('home'), href: '/', url: abs('/') },
    { label: nav('contact'), url: abs('/contact') },
  ];

  const contactItems = [
    { icon: '📧', title: t('email'), value: siteConfig.email, href: `mailto:${siteConfig.email}` },
    {
      icon: '💬',
      title: t('whatsapp'),
      value: siteConfig.phone,
      href: `https://wa.me/${siteConfig.phone.replace(/[^0-9]/g, '')}`,
    },
    { icon: '📍', title: t('address'), value: siteConfig.address, href: undefined },
  ];

  return (
    <>
      <JsonLd
        data={{
          '@context': 'https://schema.org',
          '@type': 'ContactPage',
          name: t('title'),
          url: abs('/contact'),
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
        <div className="contact-info-grid">
          {contactItems.map((item) => (
            <div key={item.title} className="contact-info-card">
              <div className="contact-icon">{item.icon}</div>
              <h3>{item.title}</h3>
              {item.href ? (
                <p>
                  <a href={item.href} target="_blank" rel="noopener noreferrer" dir="ltr" style={{direction:'ltr', unicodeBidi:'isolate'}}>
                    {item.value}
                  </a>
                </p>
              ) : (
                <p dir="ltr" style={{direction:'ltr', unicodeBidi:'isolate'}}>{item.value}</p>
              )}
            </div>
          ))}
        </div>

        <EnquiryForm />

        <div style={{ textAlign: 'center', marginTop: '2.5rem' }}>
          <Link href="/products" className="btn btn-accent">
            {common('allProducts')}
          </Link>
        </div>
      </section>
    </>
  );
}
