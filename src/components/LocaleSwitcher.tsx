'use client';
import { useEffect, useRef, useState } from 'react';
import { usePathname } from 'next/navigation';
import { useLocale } from 'next-intl';

// 语言列表（与 i18n/routing.ts、content/i18n 保持一致）
const locales = [
  { code: 'en', label: 'English', flag: '/images/flags/en.png' },
  { code: 'ru', label: 'Русский', flag: '/images/flags/ru.png' },
  { code: 'es', label: 'Español', flag: '/images/flags/es.png' },
  { code: 'fr', label: 'Français', flag: '/images/flags/fr.png' },
  { code: 'de', label: 'Deutsch', flag: '/images/flags/de.png' },
  { code: 'pt', label: 'Português', flag: '/images/flags/pt.png' },
  { code: 'ar', label: 'العربية', flag: '/images/flags/ar.png' },
  { code: 'tr', label: 'Türkçe', flag: '/images/flags/tr.png' },
  { code: 'th', label: 'ไทย', flag: '/images/flags/th.png' },
  { code: 'vi', label: 'Tiếng Việt', flag: '/images/flags/vi.png' },
  { code: 'id', label: 'Indonesia', flag: '/images/flags/id.png' },
];

export default function LocaleSwitcher() {
  const locale = useLocale();
  const pathname = usePathname();
  const [open, setOpen] = useState(false);
  const rootRef = useRef<HTMLDivElement>(null);

  // 点击外部或按 Esc 关闭下拉
  useEffect(() => {
    if (!open) return;
    function onDoc(e: MouseEvent) {
      if (rootRef.current && !rootRef.current.contains(e.target as Node)) setOpen(false);
    }
    function onKey(e: KeyboardEvent) {
      if (e.key === 'Escape') setOpen(false);
    }
    document.addEventListener('mousedown', onDoc);
    document.addEventListener('keydown', onKey);
    return () => {
      document.removeEventListener('mousedown', onDoc);
      document.removeEventListener('keydown', onKey);
    };
  }, [open]);

  function go(code: string) {
    setOpen(false);
    if (code === locale) return;
    // 去掉当前语言前缀，替换为目标语言前缀
    const segments = pathname.split('/').filter(Boolean);
    const rest = segments.slice(1).join('/');
    const next = `/${code}${rest ? '/' + rest : ''}`;
    window.location.assign(next);
  }

  const current = locales.find((l) => l.code === locale) ?? locales[0];

  return (
    <div className="lang-switcher" ref={rootRef}>
      <button
        type="button"
        className="lang-btn"
        aria-label="Language"
        aria-haspopup="listbox"
        aria-expanded={open}
        onClick={() => setOpen((o) => !o)}
      >
        <img src={current.flag} alt="" className="lang-flag" width={20} height={14} />
        <span className="lang-btn-label">{current.label}</span>
        <span className="lang-caret" aria-hidden="true">
          ▾
        </span>
      </button>

      {open && (
        <ul className="lang-menu" role="listbox" aria-label="Language">
          {locales.map((item) => (
            <li key={item.code} role="option" aria-selected={item.code === locale}>
              <button
                type="button"
                className={`lang-menu-item${item.code === locale ? ' is-current' : ''}`}
                onClick={() => go(item.code)}
              >
                <img src={item.flag} alt="" className="lang-flag" width={20} height={14} />
                <span>{item.label}</span>
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
