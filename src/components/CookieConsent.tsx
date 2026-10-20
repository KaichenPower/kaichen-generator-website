'use client';
import { useEffect, useState } from 'react';
import { Link } from '@i18n/navigation';
import { useTranslations, useLocale } from 'next-intl';

type Choice = 'accepted' | 'rejected' | null;

const STORAGE_KEY = 'kc_cookie_consent_v1';

export default function CookieConsent() {
  const [choice, setChoice] = useState<Choice>(null);
  const [open, setOpen] = useState(false);
  const locale = useLocale();
  const t = useTranslations('cookie');

  useEffect(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY) as Choice;
      if (saved === 'accepted' || saved === 'rejected') {
        setChoice(saved);
      } else {
        setOpen(true);
      }
    } catch {
      setOpen(true);
    }
  }, []);

  const save = (c: Choice) => {
    try { localStorage.setItem(STORAGE_KEY, c || ''); } catch {}
    setChoice(c);
    setOpen(false);
  };

  if (!open) return null;

  return (
    <div
      style={{
        position: 'fixed',
        left: 0,
        right: 0,
        bottom: 0,
        zIndex: 9999,
        background: '#1c2530',
        color: '#fff',
        padding: '1rem 1.25rem',
        boxShadow: '0 -4px 20px rgba(0,0,0,0.25)',
        fontSize: '0.88rem',
        lineHeight: 1.6,
      }}
    >
      <div
        style={{
          maxWidth: '1200px',
          margin: '0 auto',
          display: 'flex',
          flexWrap: 'wrap',
          gap: '1rem',
          alignItems: 'center',
          justifyContent: 'space-between',
        }}
      >
        <div style={{ flex: '1 1 400px', minWidth: 280 }}>
          <strong style={{ color: '#ffb347' }}>{t('title')}</strong>
          <p style={{ margin: '0.4rem 0 0' }}>
            {t('body')}{' '}
            <Link href="/privacy" style={{ color: '#ffb347', textDecoration: 'underline' }}>
              {t('privacyLink')}
            </Link>
            .
          </p>
        </div>
        <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
          <button
            type="button"
            onClick={() => save('rejected')}
            style={{
              padding: '0.5rem 1rem',
              background: 'transparent',
              color: '#fff',
              border: '1px solid #666',
              borderRadius: '4px',
              cursor: 'pointer',
              fontSize: '0.85rem',
            }}
          >
            {t('reject')}
          </button>
          <button
            type="button"
            onClick={() => save('accepted')}
            style={{
              padding: '0.5rem 1.25rem',
              background: 'linear-gradient(135deg, #d18f26, #b5741a)',
              color: '#1c2530',
              border: 'none',
              borderRadius: '4px',
              cursor: 'pointer',
              fontWeight: 600,
              fontSize: '0.85rem',
            }}
          >
            {t('accept')}
          </button>
        </div>
      </div>
    </div>
  );
}
