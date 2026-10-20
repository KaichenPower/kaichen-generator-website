import type { Metadata } from 'next';
import { getTranslations } from 'next-intl/server';
import { Link } from '@i18n/navigation';
import Breadcrumbs from '../../../components/Breadcrumbs';
import JsonLd from '../../../components/JsonLd';
import { getAlternates, siteConfig } from '@/lib/site';

type Props = { params: Promise<{ locale: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'blogPage' });
  const alternates = getAlternates('/faq');
  return {
    title: 'FAQ – Diesel Generator Sets | Kaichen Power',
    description:
      'Answers to common questions about diesel generator sets: warranty, lead time, sizing, silent vs open, standby vs prime, voltage and frequency, export support and after-sales response.',
    alternates: { canonical: alternates[locale], languages: alternates },
  };
}

const faqs = [
  {
    q: 'What warranty do you offer on a new generator set?',
    a: 'A standard new set carries a 1-year or 1,000-hour warranty (whichever comes first), measured from commissioning or invoice date. The engine, alternator and control panel can be extended to 2 years under our extended-warranty option. Wear items such as oil, filters, belts and batteries are excluded. The exact terms are written into the purchase contract.',
  },
  {
    q: 'How long is the lead time?',
    a: 'Standard power ranges (20–500 kVA) are usually in stock and ship within 7–15 days. Custom configurations, high-voltage parallel systems or special canopies typically take 25–45 days. We keep finished stock of common Weichai, Yuchai and SDEC sets to shorten lead time for urgent projects.',
  },
  {
    q: 'How do I choose the right generator size for my site?',
    a: 'Add the running kW of every load the set must carry at the same time, then add 20–30% margin for motor starting current and future expansion. As a rule of thumb, a small office or shop needs 20–50 kVA, a factory floor or a mid-size hotel needs 100–300 kVA, and a data center or hospital moves up to 500 kVA and above. Send us your load list and we will size the set for free.',
  },
  {
    q: 'Silent type or open type – which one should I pick?',
    a: 'Choose a silent canopy set if the unit sits near people (office floor, hospital, residential area, rooftop) and you need to keep noise around 65–75 dB(A) at 7 meters. Choose an open-type set if the unit goes into a dedicated machine room that already has acoustic treatment, because the canopy adds cost and reduces service access. Containerized and trailer-mounted options are available for outdoor or mobile duty.',
  },
  {
    q: 'What is the difference between standby power and prime power?',
    a: 'Standby power is for occasional emergency use during grid outages, typically up to 200 hours a year at 70% average load, with no overload allowed. Prime (continuous) power runs the site as the main power source, 24 hours a day, with 10% overload allowed for one hour in twelve. If you are buying for a site without a stable grid, always specify prime power – buying a standby set for continuous duty shortens its life and voids the warranty.',
  },
  {
    q: 'Do you support custom voltage, frequency and special environments?',
    a: 'Yes. We build 50 Hz / 60 Hz sets, from 220V single-phase up to 11kV three-phase, and tailor the set for high altitude (derating), cold climates (jacket water heater, arctic coolant), coastal sites (anti-corrosion treatment) and dusty environments (pre-filters). Remote monitoring via 4G and cloud, ATS auto-transfer and multi-machine paralleling are all available.',
  },
  {
    q: 'Can you export overseas and handle documentation?',
    a: 'We have an export department at the Yangzhou Innovation Center and have shipped to Southeast Asia, the Middle East, Africa, South America and Eastern Europe. We provide commercial invoice, packing list, bill of lading, CE/ISO certificates, test report and (on request) a third-party inspection report from SGS, BV or TUV. Export-standard anti-corrosion packaging is used by default.',
  },
  {
    q: 'What does the after-sales response look like?',
    a: 'We maintain more than 2,000 authorized service points across China. On the same day, engineers arrive on site within 2–4 hours in cities, 4–8 hours within the province and within 24 hours in other provinces. Overseas buyers get remote video support, a spare-parts kit and local partner contacts. The hotline runs 24/7/365. After the warranty expires, we keep supplying parts at cost plus labor for the life of the set.',
  },
  {
    q: 'Is installation and operator training included?',
    a: 'Standard sets ship with free video guidance. On-site installation, commissioning and hands-on operator training (start/stop, alarm recognition, routine maintenance) are available as a paid service. We test voltage, frequency and load on site and hand over a commissioning report before leaving. Civil works, cabling and exhaust piping are normally handled by your local contractor.',
  },
  {
    q: 'Do you test every set before shipment?',
    a: 'Yes. Every set runs on our 2 MW digital load bank through a four-step sequence – 20%, 50%, 75% and 100% rated load – for at least 2 hours total. The whole test is recorded on video and shared with you before the set leaves the factory, so you can verify the real output and protection trip settings before you receive the goods.',
  },
];

export default async function FaqPage({ params }: Props) {
  const { locale } = await params;
  const nav = await getTranslations({ locale, namespace: 'nav' });
  const common = await getTranslations({ locale, namespace: 'common' });

  const abs = (p: string) => `${siteConfig.domain}/${locale}${p}`;
  const crumbs = [
    { label: nav('home'), href: '/', url: abs('/') },
    { label: 'FAQ', url: abs('/faq') },
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
          <h1>Frequently Asked Questions</h1>
          <p>
            Straight answers on warranty, sizing, lead time, silent vs open, standby vs prime,
            export support and after-sales. If your question is not here, ask us directly.
          </p>
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
          {faqs.map((f) => (
            <div
              key={f.q}
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
            Ask Us a Question
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
