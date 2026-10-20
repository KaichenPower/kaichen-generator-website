import { getTranslations } from 'next-intl/server';
import { Link } from '@i18n/navigation';
import fs from 'fs';
import path from 'path';
import { getAllProducts, solutionSlugs } from '@/lib/content';
import { getAllPosts } from '@/lib/blog';
import { companyStats } from '@/lib/site';
import ProductCard from '@/components/ProductCard';
import Slideshow from '@/components/Slideshow';

type Props = { params: Promise<{ locale: string }> };

// 合作品牌 LOGO（来自 public/images/coop）
function coopLogos(): string[] {
  const dir = path.join(process.cwd(), 'public', 'images', 'coop');
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir)
    .filter((f) => /\.(jpe?g|png|webp)$/i.test(f))
    .sort()
    .map((f) => `/images/coop/${f}`);
}

export default async function HomePage({ params }: Props) {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'home' });
  const common = await getTranslations({ locale, namespace: 'common' });
  const sol = await getTranslations({ locale, namespace: 'solutions' });
  const blog = await getTranslations({ locale, namespace: 'blogPage' });

  const features = (t.raw('features') as { title: string; text: string }[]) || [];
  const products = getAllProducts();
  const posts = getAllPosts(locale);

  return (
    <>
      {/* 首页轮播：知识库幻灯片图片 + 标题/副标题/CTA 叠加 */}
      <Slideshow />

      {/* 信任徽章条 */}
      <section className="trust-bar" aria-label={t('trustTitle')}>
        <div className="container trust-bar-inner">
          <span className="trust-bar-title">{t('trustTitle')}</span>
          {(t.raw('trustItems') as string[]).map((item) => (
            <span key={item} className="trust-badge">
              {item}
            </span>
          ))}
        </div>
      </section>

      {/* 工厂实拍专区 */}
      <section className="section">
        <div className="container">
          <div className="section-head">
            <h2>{t('factoryTitle')}</h2>
            <p>{t('factorySubtitle')}</p>
          </div>
          <div className="factory-gallery">
            {[
              { src: '/images/factory/factory1.jpg', caption: (t.raw('factoryCaptions') as string[])[0] },
              { src: '/images/factory/factory7.png', caption: (t.raw('factoryCaptions') as string[])[1] },
              { src: '/images/factory/mobile-workshop.png', caption: (t.raw('factoryCaptions') as string[])[2] },
              { src: '/images/factory/sheet-metal.png', caption: (t.raw('factoryCaptions') as string[])[3] },
            ].map((item) => (
              <figure key={item.src} className="factory-item">
                <img src={item.src} alt={item.caption} loading="lazy" />
                <figcaption>{item.caption}</figcaption>
              </figure>
            ))}
          </div>
        </div>
      </section>

      {/* 车间大图横幅 */}
      <section className="workshop-banner" aria-label={t('workshopTitle')}>
        <div className="container workshop-banner-inner">
          <h2>{t('workshopTitle')}</h2>
          <p>{t('workshopText')}</p>
          <div className="hero-actions">
            <Link href="/about" className="btn-link btn-link--light">
              {common('learnMore')}
            </Link>
            <Link href="/products" className="btn btn-accent">
              {t('viewAllProducts')}
            </Link>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="section">
        <div className="container">
          <div className="section-head">
            <h2>{t('featureTitle')}</h2>
          </div>
          <div className="feature-grid">
            {features.map((f, i) => (
              <div key={i} className="feature-card">
                <div className="feature-icon">{'⚡'}</div>
                <h3>{f.title}</h3>
                <p>{f.text}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="section section-alt">
        <div className="container">
          <div className="section-head">
            <h2>{t('statsTitle')}</h2>
          </div>
          <div className="stats-grid">
            {companyStats.map((s, i) => (
              <div key={i} className="stat">
                <div className="stat-value">{s.value}</div>
                <div className="stat-label">{t(s.labelKey)}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Products preview */}
      <section className="section">
        <div className="container">
          <div className="section-head">
            <h2>{t('productsTitle')}</h2>
            <p>{t('productsSubtitle')}</p>
          </div>
          <div className="product-grid">
            {products.slice(0, 6).map((p) => (
              <ProductCard key={p.slug} product={p} />
            ))}
          </div>
          <div style={{ textAlign: 'center', marginTop: '2rem' }}>
            <Link href="/products" className="btn btn-accent">
              {t('viewAllProducts')}
            </Link>
          </div>
        </div>
      </section>

      {/* Solutions preview */}
      <section className="section section-alt solutions-bg">
        <div className="container">
          <div className="section-head">
            <h2>{t('solutionsTitle')}</h2>
            <p>{t('solutionsSubtitle')}</p>
          </div>
          <div className="solution-grid">
            {solutionSlugs.slice(0, 6).map((slug) => (
              <div key={slug} className="solution-card">
                <h3>{sol(`${slug}.name`)}</h3>
                <p>{sol(`${slug}.desc`)}</p>
              </div>
            ))}
          </div>
          <div style={{ textAlign: 'center', marginTop: '2rem' }}>
            <Link href="/solutions" className="btn btn-accent">
              {common('viewAll')}
            </Link>
          </div>
        </div>
      </section>

      {/* About preview */}
      <section className="section">
        <div className="container">
          <div className="section-head">
            <h2>{t('aboutPreviewTitle')}</h2>
            <p>{t('aboutPreviewText')}</p>
          </div>
          <div style={{ textAlign: 'center' }}>
            <Link href="/about" className="btn btn-accent">
              {common('learnMore')}
            </Link>
          </div>
        </div>
      </section>

      {/* Blog preview */}
      {posts.length > 0 && (
        <section className="section section-alt">
          <div className="container">
            <div className="section-head">
              <h2>{t('blogTitle')}</h2>
            </div>
            <div className="blog-list">
              {posts.slice(0, 3).map((post) => (
                <Link key={post.slug} href={`/blog/${post.slug}`} className="blog-card">
                  <div className="blog-date">
                    <svg className="blog-date-icon" viewBox="0 0 24 24" width="14" height="14" fill="currentColor" aria-hidden="true">
                      <path d="M7 2h2v2h6V2h2v2h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2V2Zm-1 6v11h12V8H6Zm2 3h2v2H8v-2Zm4 0h2v2h-2v-2Zm-4 4h2v2H8v-2Zm4 0h2v2h-2v-2Z"/>
                    </svg>
                    {blog('posted')} {post.date}
                  </div>
                  <h3>{post.title}</h3>
                  <p>{post.excerpt}</p>
                  <span className="btn-link">{blog('readMore')}</span>
                </Link>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* Engine Brand Partners：置于页脚上方，以合作品牌 LOGO 展示 */}
      {coopLogos().length > 0 && (
        <section className="section">
          <div className="container">
            <div className="section-head">
              <h2>{t('brandsTitle')}</h2>
              <p>{t('brandsSubtitle')}</p>
            </div>
            <div className="coop-logos">
              {coopLogos().map((src) => (
                <img
                  key={src}
                  src={src}
                  alt="Engine brand partner logo"
                  loading="lazy"
                  className="coop-logo"
                />
              ))}
            </div>
          </div>
        </section>
      )}
    </>
  );
}
