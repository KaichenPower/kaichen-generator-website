'use client';
import { useState } from 'react';

export type CertItem = { src: string; name: string };
export type CertCategory = { id: string; label: string; certs: CertItem[] };

const INITIAL_COUNT = 8;

// 证书画廊：按类别页签展示，默认显示 8 张，点击展开全部/收起；点击弹大图，再点关闭
export default function CertGallery({
  categories,
  allLabel,
  showMoreLabel,
  showLessLabel,
}: {
  categories: CertCategory[];
  allLabel: string;
  showMoreLabel: string;
  showLessLabel: string;
}) {
  const [activeTab, setActiveTab] = useState<string>('all');
  const [limit, setLimit] = useState(INITIAL_COUNT);
  const [active, setActive] = useState<CertItem | null>(null);

  const allCerts = categories.flatMap((c) => c.certs);
  const shown =
    activeTab === 'all' ? allCerts : categories.find((c) => c.id === activeTab)?.certs ?? [];
  const expanded = shown.length <= limit;
  const displayed = shown.slice(0, limit);

  const switchTab = (id: string) => {
    setActiveTab(id);
    setLimit(INITIAL_COUNT);
  };

  return (
    <>
      <div className="cert-tabs" role="tablist" aria-label="Certificate categories">
        <button
          type="button"
          role="tab"
          aria-selected={activeTab === 'all'}
          className={`cert-tab${activeTab === 'all' ? ' is-active' : ''}`}
          onClick={() => switchTab('all')}
        >
          {allLabel} ({allCerts.length})
        </button>
        {categories.map((c) => (
          <button
            key={c.id}
            type="button"
            role="tab"
            aria-selected={activeTab === c.id}
            className={`cert-tab${activeTab === c.id ? ' is-active' : ''}`}
            onClick={() => switchTab(c.id)}
          >
            {c.label} ({c.certs.length})
          </button>
        ))}
      </div>

      <div className="cert-grid">
        {displayed.map((c) => (
          <button
            key={c.src}
            type="button"
            className="cert-card"
            onClick={() => setActive(c)}
            aria-label={`View certificate: ${c.name}`}
          >
            <span className="cert-card-thumb">
              <img src={c.src} alt={c.name} loading="lazy" />
            </span>
            <span className="cert-card-name">{c.name}</span>
          </button>
        ))}
      </div>

      {!expanded && (
        <div style={{ textAlign: 'center', marginTop: '1.5rem' }}>
          <button type="button" className="btn btn-accent" onClick={() => setLimit(shown.length)}>
            {showMoreLabel} ({shown.length})
          </button>
        </div>
      )}
      {expanded && shown.length > INITIAL_COUNT && (
        <div style={{ textAlign: 'center', marginTop: '1.5rem' }}>
          <button type="button" className="btn btn-accent" onClick={() => setLimit(INITIAL_COUNT)}>
            {showLessLabel}
          </button>
        </div>
      )}

      {active && (
        <div
          className="cert-lightbox"
          onClick={() => setActive(null)}
          role="dialog"
          aria-modal="true"
          aria-label={active.name}
        >
          <div className="cert-lightbox-inner">
            <button
              type="button"
              className="cert-lightbox-close"
              onClick={() => setActive(null)}
              aria-label="Close"
            >
              ✕
            </button>
            <img src={active.src} alt={active.name} />
            <p className="cert-lightbox-name">{active.name}</p>
          </div>
        </div>
      )}
    </>
  );
}
