import type { Metadata } from 'next';
import { getTranslations } from 'next-intl/server';
import { Link } from '@i18n/navigation';
import Breadcrumbs from '../../../components/Breadcrumbs';
import JsonLd from '../../../components/JsonLd';
import CertGallery from '../../../components/CertGallery';
import { getAlternates, siteConfig } from '@/lib/site';

type Props = { params: Promise<{ locale: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'aboutPage' });
  const alternates = getAlternates('/about');
  return {
    title: t('title'),
    description: t('description'),
    alternates: { canonical: alternates[locale], languages: alternates },
  };
}

const factoryImages = [
  '/images/factory/factory1.jpg',
  '/images/factory/factory7.png',
  '/images/factory/mobile-workshop.png',
  '/images/factory/sheet-metal.png',
];

const customerImages = [
  '/images/customers/custom1.jpg',
  '/images/customers/custom2.jpg',
  '/images/customers/custom3.webp',
];

const certCategories = (cats: any, names: any) => [
  {
    id: 'system',
    label: cats('system'),
    certs: [
      { src: '/images/certs/cert-08.jpg', name: names('cert-08') },
      { src: '/images/certs/cert-06.jpg', name: names('cert-06') },
      { src: '/images/certs/cert-07.jpg', name: names('cert-07') },
      { src: '/images/certs/cert-02.jpg', name: names('cert-02') },
    ],
  },
  {
    id: 'oem',
    label: cats('oem'),
    certs: [
      { src: '/images/certs/cert-01.jpg', name: names('cert-01') },
      { src: '/images/certs/cert-03.jpg', name: names('cert-03') },
      { src: '/images/certs/cert-04.jpg', name: names('cert-04') },
      { src: '/images/certs/cert-09.jpg', name: names('cert-09') },
      { src: '/images/certs/cert-05.jpg', name: names('cert-05') },
      { src: '/images/certs/cert-11.jpg', name: names('cert-11') },
      { src: '/images/certs/cert-10.jpg', name: names('cert-10') },
      { src: '/images/certs/cert-12.jpg', name: names('cert-12') },
    ],
  },
  {
    id: 'patents',
    label: cats('patents'),
    certs: [
      { src: '/images/certs/cert-21.jpg', name: names('cert-21') },
      { src: '/images/certs/cert-23.jpg', name: names('cert-23') },
      { src: '/images/certs/cert-22.jpg', name: names('cert-22') },
      { src: '/images/certs/cert-13.jpg', name: names('cert-13') },
      { src: '/images/certs/cert-14.jpg', name: names('cert-14') },
      { src: '/images/certs/cert-15.jpg', name: names('cert-15') },
      { src: '/images/certs/cert-16.jpg', name: names('cert-16') },
      { src: '/images/certs/cert-17.jpg', name: names('cert-17') },
      { src: '/images/certs/cert-18.jpg', name: names('cert-18') },
      { src: '/images/certs/cert-19.jpg', name: names('cert-19') },
      { src: '/images/certs/cert-20.jpg', name: names('cert-20') },
    ],
  },
];

export default async function AboutPage({ params }: Props) {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'aboutPage' });
  const nav = await getTranslations({ locale, namespace: 'nav' });
  const common = await getTranslations({ locale, namespace: 'common' });
  const te = await getTranslations({ locale, namespace: 'aboutExtended' });
  const certCats = await getTranslations({ locale, namespace: 'aboutPage.certCats' });
  const certNames = await getTranslations({ locale, namespace: 'aboutPage.certNames' });

  const abs = (p: string) => `${siteConfig.domain}/${locale}${p}`;
  const crumbs = [
    { label: nav('home'), href: '/', url: abs('/') },
    { label: nav('about'), url: abs('/about') },
  ];

  const expertise = [
    { key: 'expertise1', icon: '🏗️' },
    { key: 'expertise2', icon: '🔇' },
    { key: 'expertise3', icon: '📦' },
    { key: 'expertise4', icon: '🚛' },
  ];

  return (
    <>
      <JsonLd
        data={{
          '@context': 'https://schema.org',
          '@type': 'AboutPage',
          name: t('title'),
          url: abs('/about'),
          description: t('lead'),
        }}
      />

      <section className="page-hero">
        <div className="container">
          <h1>{t('title')}</h1>
          <p>{t('lead')}</p>
        </div>
      </section>

      <Breadcrumbs items={crumbs} />

      <section className="content-block">
        <h2>{t('companyIntro')}</h2>
        <p>{t('body1')}</p>
        <p>{t('body2')}</p>

        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(160px, 1fr))',
          gap: '1.5rem',
          margin: '2.5rem 0',
          padding: '2rem',
          background: 'linear-gradient(135deg, #0b2a4a 0%, #14466f 100%)',
          borderRadius: '8px',
          color: '#fff',
        }}>
          {[
            { num: '2013', label: te('statsFounded') },
            { num: '8,000', label: te('statsCapacity') },
            { num: '20,000+', label: te('statsDelivered') },
            { num: '160+', label: te('statsStaff') },
            { num: '36,000 ㎡', label: te('statsArea') },
            { num: '2,000+', label: te('statsService') },
          ].map((s) => (
            <div key={s.label} style={{ textAlign: 'center' }}>
              <div style={{ fontSize: '1.8rem', fontWeight: 700, color: '#ffb347' }}>{s.num}</div>
              <div style={{ fontSize: '0.85rem', opacity: 0.9, marginTop: '0.3rem' }}>{s.label}</div>
            </div>
          ))}
        </div>

        <h2>{te('inhouseTitle')}</h2>
        <p>{te('inhouseText')}</p>
        <ul className="feature-list">
          <li><strong>{te('inhouse1Title')}</strong> {te('inhouse1Text')}</li>
          <li><strong>{te('inhouse2Title')}</strong> {te('inhouse2Text')}</li>
          <li><strong>{te('inhouse3Title')}</strong> {te('inhouse3Text')}</li>
        </ul>

        <h2>{te('loadbankTitle')}</h2>
        <p>{te('loadbankText')}</p>
        <table className="spec-table">
          <tbody>
            <tr><td>{te('lbRow1Title')}</td><td>{te('lbRow1Desc')}</td></tr>
            <tr><td>{te('lbRow2Title')}</td><td>{te('lbRow2Desc')}</td></tr>
            <tr><td>{te('lbRow3Title')}</td><td>{te('lbRow3Desc')}</td></tr>
            <tr><td>{te('lbRow4Title')}</td><td>{te('lbRow4Desc')}</td></tr>
          </tbody>
        </table>

        <h2>{te('benchmarkTitle')}</h2>
        <p>{te('benchmarkText')}</p>
        <ul className="feature-list">
          <li>{te('benchmark1')}</li>
          <li>{te('benchmark2')}</li>
          <li>{te('benchmark3')}</li>
          <li>{te('benchmark4')}</li>
          <li>{te('benchmark5')}</li>
        </ul>

        <h2>{t('missionTitle')}</h2>
        <p>{t('missionText')}</p>

        <h2>{t('qualityTitle')}</h2>
        <p>{t('qualityText')}</p>

        <h2>{t('expertiseTitle')}</h2>
        <div className="solution-grid">
          {expertise.map((item) => (
            <div key={item.key} className="solution-card">
              <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>
                {item.icon}
              </div>
              <h3>{t(item.key)}</h3>
            </div>
          ))}
        </div>
      </section>

      <section className="section section-alt">
        <div className="container">
          <div className="section-head">
            <h2>{t('factoryTitle')}</h2>
          </div>
          <div className="about-gallery">
            {factoryImages.map((src) => (
              <div key={src} className="about-gallery-item">
                <img src={src} alt={t('factoryTitle')} loading="lazy" />
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="section">
        <div className="container">
          <div className="section-head">
            <h2>{t('customersTitle')}</h2>
          </div>
          <div className="about-gallery">
            {customerImages.map((src) => (
              <div key={src} className="about-gallery-item">
                <img src={src} alt={t('customersTitle')} loading="lazy" />
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="section section-alt">
        <div className="container">
          <div className="section-head">
            <h2>{t('certTitle')}</h2>
            <p>{t('certSubtitle')}</p>
          </div>
          <CertGallery
            categories={certCategories(certCats, certNames)}
            allLabel={t('certAllLabel')}
            showMoreLabel={t('showMoreCerts')}
            showLessLabel={t('showLessCerts')}
          />
        </div>
      </section>

      <section className="section">
        <div className="container" style={{ textAlign: 'center' }}>
          <h2 style={{ color: 'var(--color-primary)' }}>{t('expertiseTitle')}</h2>
          <p>{t('qualityText')}</p>
          <div className="hero-actions" style={{ justifyContent: 'center' }}>
            <Link href="/products" className="btn btn-accent">
              {common('allProducts')}
            </Link>
            <Link href="/contact" className="btn btn-outline" style={{ borderColor: 'var(--color-primary)', color: 'var(--color-primary)' }}>
              {nav('contact')}
            </Link>
          </div>
        </div>
      </section>
    </>
  );
}
