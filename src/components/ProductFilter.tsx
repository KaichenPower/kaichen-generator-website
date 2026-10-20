'use client';
import { useState } from 'react';
import { useTranslations } from 'next-intl';
import ProductCard from './ProductCard';

export type Product = {
  slug: string;
  urlSlug?: string;
  name: string;
  brand: string;
  powerKVA: number;
  type: string;
  image?: string;
};

const powerRanges = [
  { id: 'p40', min: 20, max: 100, label: '20 – 100 {kva}' },
  { id: 'p200', min: 100, max: 300, label: '100 – 300 {kva}' },
  { id: 'p500', min: 300, max: 800, label: '300 – 800 {kva}' },
  { id: 'p1000', min: 800, max: 2000, label: '800 – 2000 {kva}' },
  { id: 'p4000', min: 2000, max: 5000, label: '2000+ {kva}' },
];

const PER_PAGE = 12;

export default function ProductFilter({ products }: { products: Product[] }) {
  const pp = useTranslations('productsPage');
  const pu = useTranslations('powerUnits');
  const ptype = useTranslations('productType');
  const [brand, setBrand] = useState('all');
  const [type, setType] = useState('all');
  const [range, setRange] = useState('all');
  const [page, setPage] = useState(1);

  const typeLabel = (t: string) => {
    if (t === 'silent') return ptype('silent');
    if (t === 'open') return ptype('open');
    if (t === 'container') return ptype('container');
    if (t === 'mobile') return ptype('mobileTrailer');
    return t;
  };

  const brands = Array.from(new Set(products.map((p) => p.brand))).sort();
  const types = Array.from(new Set(products.map((p) => p.type)));

  const filtered = products.filter((p) => {
    if (brand !== 'all' && p.brand !== brand) return false;
    if (type !== 'all' && p.type !== type) return false;
    if (range !== 'all') {
      const r = powerRanges.find((x) => x.id === range);
      if (r && (p.powerKVA < r.min || p.powerKVA >= r.max)) return false;
    }
    return true;
  });

  const pageCount = Math.max(1, Math.ceil(filtered.length / PER_PAGE));
  const safePage = Math.min(page, pageCount);
  const start = (safePage - 1) * PER_PAGE;
  const shown = filtered.slice(start, start + PER_PAGE);

  // 切换筛选条件时回到第 1 页
  const change = (setter: (v: string) => void) => (v: string) => {
    setter(v);
    setPage(1);
  };

  const goTo = (p: number) => {
    setPage(Math.min(Math.max(1, p), pageCount));
  };

  return (
    <>
      <div className="filter-bar">
        <div className="filter-group">
          <label>{pp('filterByBrand')}</label>
          <div className="filter-options">
            <button
              type="button"
              className={`filter-option${brand === 'all' ? ' is-active' : ''}`}
              onClick={() => change(setBrand)('all')}
            >
              {pp('all')}
            </button>
            {brands.map((b) => (
              <button
                key={b}
                type="button"
                className={`filter-option${brand === b ? ' is-active' : ''}`}
                onClick={() => change(setBrand)(b)}
              >
                {b}
              </button>
            ))}
          </div>
        </div>

        <div className="filter-group">
          <label>{pp('filterByType')}</label>
          <div className="filter-options">
            <button
              type="button"
              className={`filter-option${type === 'all' ? ' is-active' : ''}`}
              onClick={() => change(setType)('all')}
            >
              {pp('all')}
            </button>
            {types.map((t) => (
              <button
                key={t}
                type="button"
                className={`filter-option${type === t ? ' is-active' : ''}`}
                onClick={() => change(setType)(t)}
              >
                {typeLabel(t)}
              </button>
            ))}
          </div>
        </div>

        <div className="filter-group">
          <label>{pp('filterByPower')}</label>
          <div className="filter-options">
            <button
              type="button"
              className={`filter-option${range === 'all' ? ' is-active' : ''}`}
              onClick={() => change(setRange)('all')}
            >
              {pp('all')}
            </button>
            {powerRanges.map((r) => (
              <button
                key={r.id}
                type="button"
                className={`filter-option${range === r.id ? ' is-active' : ''}`}
                onClick={() => change(setRange)(r.id)}
              >
                {r.label.replace('{kva}', pu('kva'))}
              </button>
            ))}
          </div>
        </div>
      </div>

      {filtered.length === 0 ? (
        <div className="empty-state">{pp('noResults')}</div>
      ) : (
        <>
          <div className="product-grid">
            {shown.map((p) => (
              <ProductCard key={p.slug} product={p} />
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
