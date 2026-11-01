import type { Metadata } from 'next';
import { getTranslations } from 'next-intl/server';
import { Link } from '@i18n/navigation';
import Breadcrumbs from '../../../../../components/Breadcrumbs';
import JsonLd from '../../../../../components/JsonLd';
import ProductCard from '../../../../../components/ProductCard';
import { getAllProducts } from '@/lib/content';
import { getAlternates, siteConfig } from '@/lib/site';

export const dynamic = 'force-static';

const categorySlugs = [
  'cummins',
  'sdec',
  'weichai',
  'volvo',
  'yuchai',
  'kaichen',
  'silent-canopy',
  'rainproof-canopy',
  'containerized-silent',
  'mobile-silent',
  'mobile-trailer',
  'other-oem',
] as const;

type Props = { params: Promise<{ locale: string; category: string }> };

export function generateStaticParams() {
  return categorySlugs.map((category) => ({ category }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale, category } = await params;
  const t = await getTranslations({ locale, namespace: 'productCategories' });
  const alternates = getAlternates(`/products/categories/${category}`);
  return {
    title: t(`${category}.title`),
    description: t(`${category}.description`),
    alternates: { canonical: alternates[locale], languages: alternates },
  };
}

export default async function ProductCategoryPage({ params }: Props) {
  const { locale, category } = await params;
  const t = await getTranslations({ locale, namespace: 'productCategories' });
  const nav = await getTranslations({ locale, namespace: 'nav' });
  const pp = await getTranslations({ locale, namespace: 'productsPage' });
  const title = t(`${category}.title`);
  const description = t(`${category}.description`);
  const products = getAllProducts().filter((p) => (p.category as string) === category);
  const image = `/images/product-categories/${category}.jpg`;

  return (
    <div className="container" style={{ paddingTop: 32, paddingBottom: 48 }}>
      <Breadcrumbs items={[{ label: nav('home'), href: '/' }, { label: pp('title'), href: '/products' }, { label: title }]} />
      <div style={{ display: 'grid', gridTemplateColumns: 'minmax(280px, 420px) 1fr', gap: 32, alignItems: 'center', marginBottom: 28 }}>
        <img src={image} alt={title} style={{ width: '100%', borderRadius: 12, background: '#f3f4f6' }} />
        <div>
          <h1 style={{ marginBottom: 12 }}>{title}</h1>
          <p>{description}</p>
        </div>
      </div>

      {products.length > 0 ? (
        <div className="product-grid">
          {products.map((product) => <ProductCard key={product.slug} product={product} />)}
        </div>
      ) : (
        <div className="empty-state">
          {description} — <Link href="/contact">{pp('contactCta')}</Link>
        </div>
      )}

      <JsonLd
        data={{
          '@context': 'https://schema.org',
          '@type': 'CollectionPage',
          name: title,
          description,
          inLanguage: locale,
          isPartOf: { '@type': 'WebSite', name: siteConfig.brandName, url: siteConfig.domain },
        }}
      />
    </div>
  );
}
