import type { Metadata } from 'next';
import { getTranslations } from 'next-intl/server';
import { Link } from '@i18n/navigation';
import { getAllProducts } from '../../../lib/content';
import ProductFilter from '../../../components/ProductFilter';
import Breadcrumbs from '../../../components/Breadcrumbs';
import JsonLd from '../../../components/JsonLd';
import { siteConfig, getAlternates } from '@/lib/site';

type Props = { params: Promise<{ locale: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'productsPage' });
  const alternates = getAlternates('/products');
  return {
    title: t('title'),
    description: t('subtitle'),
    alternates: {
      canonical: alternates[locale],
      languages: alternates,
    },
  };
}

export default async function ProductsPage({ params }: Props) {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'productsPage' });
  const pt = await getTranslations({ locale, namespace: 'products' });
  const nav = await getTranslations({ locale, namespace: 'nav' });
  const common = await getTranslations({ locale, namespace: 'common' });
  const products = getAllProducts();
  const ptype = await getTranslations({ locale, namespace: 'productType' });
  const pu = await getTranslations({ locale, namespace: 'powerUnits' });

  const localizeName = (raw: string): string => {
    let n = raw;
    n = n.replace(/Silent Diesel Generator/g, `${ptype('silent')} ${ptype('dieselGenerator')}`);
    n = n.replace(/Open Diesel Generator/g, `${ptype('open')} ${ptype('dieselGenerator')}`);
    n = n.replace(/Mobile Trailer Diesel Generator/g, `${ptype('mobileTrailer')} ${ptype('dieselGenerator')}`);
    n = n.replace(/Containerized Diesel Generator/g, `${ptype('container')} ${ptype('dieselGenerator')}`);
    n = n.replace(/Containerized Power Plant/g, `${ptype('powerPlant')}`);
    n = n.replace(/Mobile Trailer Power Station/g, `${ptype('mobileTrailer')} ${ptype('powerPlant')}`);
    n = n.replace(/(\d+)kVA/g, `$1${pu('kva')}`);
    n = n.replace(/(\d+)kW/g, `$1${pu('kw')}`);
    return n;
  };

  const abs = (p: string) => `${siteConfig.domain}/${locale}${p}`;
  const crumbs = [
    { label: nav('home'), href: '/', url: abs('/') },
    { label: nav('products'), url: abs('/products') },
  ];

  const items = products.map((p, i) => {
    const rawName = pt.has(`${p.slug}.name`) ? (pt.raw(`${p.slug}.name`) as string) : p.name;
    return {
      '@type': 'ListItem',
      position: i + 1,
      name: localizeName(rawName),
      url: abs(`/products/${p.urlSlug}`),
    };
  });

  return (
    <>
      <JsonLd
        data={{
          '@context': 'https://schema.org',
          '@type': 'ItemList',
          name: t('title'),
          itemListElement: items,
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
        <ProductFilter products={products} />
        <div style={{ textAlign: 'center', marginTop: '2.5rem' }}>
          <Link href="/contact" className="btn btn-accent">
            {nav('contact')}
          </Link>
        </div>
      </section>
    </>
  );
}
