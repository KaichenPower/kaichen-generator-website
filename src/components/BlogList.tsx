'use client';
import { useState } from 'react';
import { useTranslations } from 'next-intl';
import { Link } from '@i18n/navigation';

type Post = {
  slug: string;
  title: string;
  date: string;
  excerpt: string;
  image?: string;
};

const PER_PAGE = 12;

export default function BlogList({ posts }: { posts: Post[] }) {
  const t = useTranslations('blogPage');
  const pp = useTranslations('productsPage');
  const [page, setPage] = useState(1);

  const pageCount = Math.max(1, Math.ceil(posts.length / PER_PAGE));
  const safePage = Math.min(page, pageCount);
  const start = (safePage - 1) * PER_PAGE;
  const shown = posts.slice(start, start + PER_PAGE);

  const goTo = (p: number) => {
    setPage(Math.min(Math.max(1, p), pageCount));
    if (typeof window !== 'undefined') window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <>
      {posts.length === 0 ? (
        <div className="empty-state">{t('empty')}</div>
      ) : (
        <>
          <div className="product-grid">
            {shown.map((post) => (
              <Link key={post.slug} href={`/blog/${post.slug}`} className="product-card">
                <div className="product-card-thumb">
                  {post.image ? (
                    <img
                      src={post.image}
                      alt={post.title}
                      loading="lazy"
                      style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                    />
                  ) : (
                    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100%', color: '#999' }}>
                      Kaichen Power
                    </div>
                  )}
                </div>
                <div className="product-card-body">
                  <div className="blog-date" style={{ marginBottom: '0.5rem' }}>
                    <svg className="blog-date-icon" viewBox="0 0 24 24" width="14" height="14" fill="currentColor" aria-hidden="true">
                      <path d="M7 2h2v2h6V2h2v2h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2V2Zm-1 6v11h12V8H6Zm2 3h2v2H8v-2Zm4 0h2v2h-2v-2Zm-4 4h2v2H8v-2Zm4 0h2v2h-2v-2Z" />
                    </svg>
                    {t('posted')} {post.date}
                  </div>
                  <h3 style={{ fontSize: '1.05rem', lineHeight: 1.4, minHeight: '2.8em' }}>{post.title}</h3>
                  <p style={{ fontSize: '0.88rem', color: '#555', margin: '0.5rem 0 0.75rem' }}>{post.excerpt}</p>
                  <span className="btn-link">{t('readMore')}</span>
                </div>
              </Link>
            ))}
          </div>

          {pageCount > 1 && (
            <nav className="pagination" aria-label="pagination">
              <button
                type="button"
                className="pagination-btn"
                disabled={safePage <= 1}
                onClick={() => goTo(safePage - 1)}
              >
                {pp('prev')}
              </button>
              {Array.from({ length: pageCount }, (_, i) => i + 1).map((n) => (
                <button
                  key={n}
                  type="button"
                  className={`pagination-btn${n === safePage ? ' is-active' : ''}`}
                  aria-current={n === safePage ? 'page' : undefined}
                  onClick={() => goTo(n)}
                >
                  {n}
                </button>
              ))}
              <button
                type="button"
                className="pagination-btn"
                disabled={safePage >= pageCount}
                onClick={() => goTo(safePage + 1)}
              >
                {pp('next')}
              </button>
              <span className="pagination-info">
                {pp('page')} {safePage} / {pageCount}
              </span>
            </nav>
          )}
        </>
      )}
    </>
  );
}
