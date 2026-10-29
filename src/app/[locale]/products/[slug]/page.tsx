import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { getTranslations } from 'next-intl/server';
import { Link } from '@i18n/navigation';
import { getProductByUrlSlug, getAllProducts } from '../../../../lib/content';
import EnquiryForm from '../../../../components/EnquiryForm';
import ProductCard from '../../../../components/ProductCard';
import Breadcrumbs from '../../../../components/Breadcrumbs';
import JsonLd from '../../../../components/JsonLd';
import { getAlternates, siteConfig } from '@/lib/site';

type Props = { params: Promise<{ locale: string; slug: string }> };

// 把 YAML 中的规格标签键映射到 i18n specLabels 分组
const LABEL_KEYS: Record<string, string> = {
  'Prime power': 'primePower',
  'Standby power': 'standbyPower',
  Engine: 'engine',
  Alternator: 'alternator',
  Voltage: 'voltage',
  Control: 'control',
  Starting: 'starting',
  Cooling: 'cooling',
  'Noise level': 'noiseLevel',
  'Fuel tank': 'fuelTank',
  Container: 'container',
  'Fuel system': 'fuelSystem',
  Trailer: 'trailer',
  Frame: 'frame',
  'Fuel consumption': 'fuelConsumption',
  Mobility: 'mobility',
  Dimensions: 'dimensions',
  Weight: 'weight',
};

// English spec value -> i18n key in specValues namespace
const VALUE_MAP: Record<string, string> = {
  'Brushless self-excited': 'brushlessSelfExcited',
  'Brushless, self-excited': 'brushlessSelfExcited',
  'Digital control panel': 'digitalControlPanel',
  'Digital controller': 'digitalController',
  'Digital controller with auto start': 'digitalControllerAuto',
  'Digital controller with parallel capability': 'digitalControllerParallel',
  'Digital controller with remote monitoring': 'digitalControllerRemote',
  'Digital AMF controller': 'digitalAmfController',
  'Automatic ATS-ready controller': 'atsController',
  'Advanced parallel-capable controller': 'advancedParallel',
  'Advanced paralleling controller': 'advancedParallel',
  'Electric start, 24V': 'electricStart24',
  'Electric start, 12/24V': 'electricStart1224',
  'Water-cooled radiator': 'waterCooled',
  'Water-cooled, container optimized': 'waterCooledContainer',
  'Radiator, container optimized': 'radiatorContainer',
  'Heavy-duty skid with anti-vibration mounts': 'skidAntiVib',
  'Heavy-duty skid with forklift slots': 'skidForklift',
  'Single-axle trailer, road-ready': 'singleAxleTrailer',
  'Two-axle highway trailer': 'twoAxleTrailer',
  '20ft ISO container': 'iso20ft',
  '40ft ISO container': 'iso40ft',
  '40ft high-cube module': 'hc40ft',
  '180L built-in': 'tank180',
  '300L built-in': 'tank300',
  '600L built-in': 'tank600',
  '900L built-in': 'tank900',
  '75L built-in': 'tank75',
  '68–72 dB(A) at 7m': 'noise6872',
  '69–75 dB(A) at 7m': 'noise6975',
  '70–75 dB(A) at 7m': 'noise7075',
  '70–76 dB(A) at 7m': 'noise7076',
  '72–78 dB(A) at 7m': 'noise7278',
  '≤ 78 dB(A) @ 7m': 'noiseLe78',
  '≤70 dB(A) @ 7m': 'noiseLe70',
  '≤72 dB(A) @ 7m': 'noiseLe72',
  '≤75 dB(A) @ 7m': 'noiseLe75',
  'approx. 640 L/h at 100% load': 'fuel640',
  'approx. 91 L/h at 100% load': 'fuel91',
  'Day tank + external connection': 'dayTank',
  '400/230V, 50Hz (custom voltages available)': 'voltageCustom',
  'Stamford / Leroy-Somer brushless': 'stamfordLeroyBrushless',
  'Deepsea or ComAp AMF controller': 'deepseaComApAmf',
  '400/230V, 50Hz, 3-phase': 'voltage3phase',
  '120L built-in': 'tank120',
  '≤68 dB(A) @ 7m': 'noiseLe68',
  'Cummins 4BT3.9-G2': 'engine4bt',
  'approx. 197 g/kWh at 100% load': 'fuel197g',
  '102 dB(A) at 7m': 'noise102',
  '4900 × 2050 × 2600 mm': 'dimsMhi',
  '10,500 kg': 'weightMhi',
  'approx. 200 g/kWh at 100% load': 'fuel200g',
  '4450 × 1800 × 2350 mm': 'dimsC800',
  '8,000 kg': 'weightC800',
};

export function generateStaticParams() {
  const products = getAllProducts();
  return products.map((p) => ({ slug: p.urlSlug }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale, slug } = await params;
  const product = getProductByUrlSlug(slug);
  if (!product) return {};
  const pt = await getTranslations({ locale, namespace: 'products' });
  const has = (key: string): boolean => {
    try { return pt.has(key); } catch { return false; }
  };
  const safeRaw = (key: string): any => {
    try { return has(key) ? pt.raw(key) : undefined; } catch { return undefined; }
  };
  const name = (safeRaw(`${product.slug}.name`) as string) || product.name;
  const description =
    (safeRaw(`${product.slug}.description`) as string) || product.description || '';
  const alternates = getAlternates(`/products/${product.urlSlug}`);
  return {
    title: name,
    description,
    alternates: { canonical: alternates[locale], languages: alternates },
  };
}

export default async function ProductDetailPage({ params }: Props) {
  const { locale, slug } = await params;
  const pp = await getTranslations({ locale, namespace: 'productsPage' });
  const pt = await getTranslations({ locale, namespace: 'products' });
  const sl = await getTranslations({ locale, namespace: 'specLabels' });
  const nav = await getTranslations({ locale, namespace: 'nav' });
  const common = await getTranslations({ locale, namespace: 'common' });
  const pe = await getTranslations({ locale, namespace: 'aboutExtended' });
  const sv = await getTranslations({ locale, namespace: 'specValues' });
  const pu = await getTranslations({ locale, namespace: 'powerUnits' });

  const product = getProductByUrlSlug(slug);
  if (!product) notFound();

  const ptype = await getTranslations({ locale, namespace: 'productType' });

  // i18n 按内部 slug 取本地化名称/描述/特性等；缺失时安全回退到 yaml 英文
  // 注意：next-intl 的 pt.raw() 对缺失键不抛错，而是返回键名字符串本身，
  // 因此必须先用 pt.has() 判断键是否真实存在。
  const has = (key: string): boolean => {
    try { return pt.has(key); } catch { return false; }
  };
  const safeRaw = (key: string): any => {
    try { return has(key) ? pt.raw(key) : undefined; } catch { return undefined; }
  };
  const arr = (v: unknown): string[] => (Array.isArray(v) ? v : []);
  // Translate product type words (Silent/Open/Container/Mobile Trailer) while keeping brand + power in original.
  const localizeName = (raw: string): string => {
    let n = raw;
    n = n.replace(/Silent Diesel Generator/g, `${ptype('silent')} ${ptype('dieselGenerator')}`);
    n = n.replace(/Open Diesel Generator/g, `${ptype('open')} ${ptype('dieselGenerator')}`);
    n = n.replace(/Mobile Trailer Diesel Generator/g, `${ptype('mobileTrailer')} ${ptype('dieselGenerator')}`);
    n = n.replace(/Containerized Diesel Generator/g, `${ptype('container')} ${ptype('dieselGenerator')}`);
    n = n.replace(/Containerized Power Plant/g, `${ptype('powerPlant')}`);
    n = n.replace(/Mobile Trailer Power Station/g, `${ptype('mobileTrailer')} ${ptype('powerPlant')}`);
    // Localize power units in product names
    n = n.replace(/(\d+)kVA/g, `$1${pu('kva')}`);
    n = n.replace(/(\d+)kW/g, `$1${pu('kw')}`);
    return n;
  };
  const rawName = (safeRaw(`${product.slug}.name`) as string) || product.name;
  const name = localizeName(rawName);
  const rawDesc = (safeRaw(`${product.slug}.description`) as string) || product.description || '';
  const description = rawDesc.replace(/(\d+)kVA/g, `$1${pu('kva')}`).replace(/(\d+)kW/g, `$1${pu('kw')}`);
  const localizedFeatures = arr(safeRaw(`${product.slug}.features`));
  const features: string[] =
    localizedFeatures.length > 0 ? localizedFeatures : arr(product.features);
  const applications = arr(safeRaw(`${product.slug}.applications`));
  const problems = arr(safeRaw(`${product.slug}.problems`));

  const specs = Object.entries(product.specs || {});
  const label = (key: string) => {
    const mapped = LABEL_KEYS[key];
    return mapped ? (sl(mapped) as string) : key;
  };
  const value = (v: string) => {
    const mapped = VALUE_MAP[v];
    let result = mapped ? (sv(mapped) as string) : v;
    // Localize power units in values like "27 kW / 34 kVA"
    result = result.replace(/(\d+)\s*kW/g, `$1 ${pu('kw')}`);
    result = result.replace(/(\d+)\s*kVA/g, `$1 ${pu('kva')}`);
    // Translate trailing " series" (e.g. "Yuchai YC6B series" -> "Yuchai YC6B سلسلة")
    const seriesWord: Record<string, string> = {
      en: 'series', ru: 'серия', es: 'serie', fr: 'série', de: 'Baureihe',
      pt: 'série', ar: 'سلسلة', tr: 'seri', th: 'ซีรีส์', vi: 'dòng', id: 'seri',
    };
    const w = seriesWord[locale] || 'series';
    if (result.endsWith(' series')) return result.slice(0, -' series'.length) + ' ' + w;
    // Translate trailing "controller" (e.g. "Deep Sea / KCP controller" -> "جهاز تحكم")
    const ctrlWord: Record<string, string> = {
      en: 'controller', ru: 'контроллер', es: 'controlador', fr: 'contrôleur', de: 'Steuergerät',
      pt: 'controlador', ar: 'جهاز تحكم', tr: 'kontrol cihazı', th: 'เครื่องควบคุม', vi: 'bộ điều khiển', id: 'pengontrol',
    };
    const cw = ctrlWord[locale] || 'controller';
    result = result.replace(/\s*controller$/i, ' ' + cw);
    return result;
  };

  // 相关产品：同品牌优先，不足按功率就近补齐（按 urlSlug 排除当前产品）
  const all = getAllProducts();
  const sameBrand = all.filter((p) => p.urlSlug !== slug && p.brand === product.brand);
  const others = all.filter((p) => p.urlSlug !== slug && p.brand !== product.brand);
  const related = [...sameBrand, ...others].slice(0, 4);

  const abs = (p: string) => `${siteConfig.domain}/${locale}${p}`;
  const crumbs = [
    { label: nav('home'), href: '/', url: abs('/') },
    { label: nav('products'), href: '/products', url: abs('/products') },
    { label: name, url: abs(`/products/${slug}`) },
  ];

  return (
    <>
      <JsonLd
        data={{
          '@context': 'https://schema.org',
          '@type': 'Product',
          name,
          description,
          sku: product.slug,
          brand: { '@type': 'Brand', name: product.brand },
          image: product.image ? `${siteConfig.domain}${product.image}` : undefined,
          category: product.type,
          additionalProperty: (specs || []).map(([k, v]) => ({
            '@type': 'PropertyValue',
            name: label(k),
            value: String(v),
          })),
        }}
      />

      <div className="page-hero page-hero--detail">
        <div className="container">
          <p className="page-hero-tag">{pp('detailTag')}</p>
        </div>
      </div>

      <Breadcrumbs items={crumbs} />

      <div className="product-detail-top">
        <div>
          {product.image ? (
            <div className="product-detail-thumb">
              <img src={product.image as string} alt={name} loading="lazy" />
            </div>
          ) : (
            <div className="product-detail-thumb">{product.powerKVA} {pu('kva')}</div>
          )}
        </div>

        <div className="product-detail-intro">
          <h1>{name}</h1>
          <p className="product-detail-desc">{description}</p>
          <div className="product-card-meta" style={{ marginTop: '1rem', justifyContent: 'flex-start' }}>
            <span>
              <strong>{pp('brandLabel')}:</strong> {product.brand}
            </span>
            <span>
              <strong>{pp('typeLabel')}:</strong> {
                product.type === 'silent' ? ptype('silent') :
                product.type === 'open' ? ptype('open') :
                product.type === 'container' ? ptype('container') :
                product.type === 'mobile' ? ptype('mobileTrailer') :
                product.type
              }
            </span>
          </div>
          <p style={{ marginTop: '1.5rem' }}>
            <a href="#enquiry" className="btn btn-accent">
              {nav('getQuote')}
            </a>
          </p>
        </div>
      </div>

      <div className="product-detail-sections">
        <section className="product-detail-section">
          <h2 style={{ color: 'var(--color-primary)', marginTop: 0 }}>{pp('specsTitle')}</h2>
          <table className="spec-table">
            <tbody>
              {specs.map(([k, v]) => (
                <tr key={k}>
                  <td>{label(k)}</td>
                  <td>{value(String(v))}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>

        {features.length > 0 && (
          <section className="product-detail-section">
            <h2 style={{ color: 'var(--color-primary)' }}>{pp('featuresTitle')}</h2>
            <ul className="feature-list">
              {features.map((f, i) => (
                <li key={i}>{f}</li>
              ))}
            </ul>
          </section>
        )}

        {applications.length > 0 && (
          <section className="product-detail-section">
            <h2 style={{ color: 'var(--color-primary)' }}>{pp('applicationsTitle')}</h2>
            <ul className="feature-list">
              {applications.map((a, i) => (
                <li key={i}>{a}</li>
              ))}
            </ul>
          </section>
        )}

        {problems.length > 0 && (
          <section className="product-detail-section">
            <h2 style={{ color: 'var(--color-primary)' }}>{pp('problemsTitle')}</h2>
            <ul className="feature-list">
              {problems.map((p, i) => (
                <li key={i}>{p}</li>
              ))}
            </ul>
          </section>
        )}

        <section className="product-detail-section">
          <h2 style={{ color: 'var(--color-primary)' }}>{pe('manufacturingTitle')}</h2>
          <p>{pe('mfgIntro')}</p>

          <h3 style={{ marginTop: '1.2rem' }}>{pe('mfgBuiltTitle')}</h3>
          <ul className="feature-list">
            <li><strong>{pe('mfgBuilt1Title')}</strong> {pe('mfgBuilt1Text')}</li>
            <li><strong>{pe('mfgBuilt2Title')}</strong> {pe('mfgBuilt2Text')}</li>
            <li><strong>{pe('mfgBuilt3Title')}</strong> {pe('mfgBuilt3Text')}</li>
            <li><strong>{pe('mfgBuilt4Title')}</strong> {pe('mfgBuilt4Text')}</li>
          </ul>

          <h3 style={{ marginTop: '1.2rem' }}>{pe('mfgLoadTestTitle')}</h3>
          <p>{pe('mfgLoadTestIntro')}</p>
          <table className="spec-table">
            <tbody>
              <tr><td>{pe('mfgRow1Title')}</td><td>{pe('mfgRow1Desc')}</td></tr>
              <tr><td>{pe('mfgRow2Title')}</td><td>{pe('mfgRow2Desc')}</td></tr>
              <tr><td>{pe('mfgRow3Title')}</td><td>{pe('mfgRow3Desc')}</td></tr>
              <tr><td>{pe('mfgRow4Title')}</td><td>{pe('mfgRow4Desc')}</td></tr>
              <tr><td>{pe('mfgRow5Title')}</td><td>{pe('mfgRow5Desc')}</td></tr>
              <tr><td>{pe('mfgRow6Title')}</td><td>{pe('mfgRow6Desc')}</td></tr>
            </tbody>
          </table>

          <h3 style={{ marginTop: '1.2rem' }}>{pe('mfgFinalTitle')}</h3>
          <ul className="feature-list">
            <li>{pe('mfgFinal1')}</li>
            <li>{pe('mfgFinal2')}</li>
            <li>{pe('mfgFinal3')}</li>
            <li>{pe('mfgFinal4')}</li>
          </ul>
          <p style={{ marginTop: '0.8rem' }}>{pe('mfgClosing')}</p>
        </section>
      </div>

      {related.length > 0 && (
        <section className="section section-alt">
          <div className="container">
            <div className="section-head">
              <h2>{common('relatedProducts')}</h2>
            </div>
            <div className="product-grid">
              {related.map((p) => (
                <ProductCard key={p.slug} product={p} />
              ))}
            </div>
            <div style={{ textAlign: 'center', marginTop: '2rem' }}>
              <Link href="/products" className="btn btn-accent">
                {common('allProducts')}
              </Link>
            </div>
          </div>
        </section>
      )}

      <section id="enquiry" className="section section-enquiry">
        <div className="container">
          <EnquiryForm
            subject={`${name} – ${product.powerKVA}${pu('kva')}`}
            productName={name}
            productUrl={`${siteConfig.domain}/${locale}/products/${slug}`}
          />
        </div>
      </section>
    </>
  );
}
