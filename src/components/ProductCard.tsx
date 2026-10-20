import { useTranslations } from 'next-intl';
import { Link } from '@i18n/navigation';

type Product = {
  slug: string;
  urlSlug?: string;
  name: string;
  brand: string;
  powerKVA: number;
  type: string;
  description?: string;
  image?: string;
};

export default function ProductCard({ product }: { product: Product }) {
  const common = useTranslations('common');
  const pp = useTranslations('productsPage');
  const pu = useTranslations('powerUnits');
  const pt = useTranslations('products');
  const ptype = useTranslations('productType');
  const rawName = pt.has(`${product.slug}.name`) ? pt(`${product.slug}.name`) : product.name;
  const localizeName = (raw: string): string => {
    let n = raw;
    n = n.replace(/Silent Diesel Generator/g, `${ptype('silent')} ${ptype('dieselGenerator')}`);
    n = n.replace(/Open Diesel Generator/g, `${ptype('open')} ${ptype('dieselGenerator')}`);
    n = n.replace(/Mobile Trailer Diesel Generator/g, `${ptype('mobileTrailer')} ${ptype('dieselGenerator')}`);
    n = n.replace(/Containerized Diesel Generator/g, `${ptype('container')} ${ptype('dieselGenerator')}`);
    n = n.replace(/Containerized Power Plant/g, `${ptype('powerPlant')}`);
    n = n.replace(/Mobile Trailer Power Station/g, `${ptype('mobileTrailer')} ${ptype('powerPlant')}`);
    // Localize power units in product names (e.g. "300kVA" -> "300кВА")
    n = n.replace(/(\d+)kVA/g, `$1${pu('kva')}`);
    n = n.replace(/(\d+)kW/g, `$1${pu('kw')}`);
    return n;
  };
  const name = localizeName(rawName);
  const href = product.urlSlug ? `/products/${product.urlSlug}` : `/products/${product.slug}`;

  return (
    <Link href={href} className="product-card">
      <div className="product-card-thumb">
        {product.image ? (
          <img
            src={product.image}
            alt={name}
            loading="lazy"
            style={{ width: '100%', height: '100%', objectFit: 'cover' }}
          />
        ) : (
          `${product.powerKVA} ${pu('kva')}`
        )}
      </div>
      <div className="product-card-body">
        <h3>{name}</h3>
        <div className="product-card-meta">
          <span>
            <strong>{pp('brandLabel')}:</strong> {product.brand}
          </span>
          <span>
            <strong>{pp('powerLabel')}:</strong> {product.powerKVA} {pu('kva')}
          </span>
        </div>
        <span className="btn-link">{common('learnMore')}</span>
      </div>
    </Link>
  );
}
