'use client';
import { useState } from 'react';
import { useTranslations } from 'next-intl';
import { Link, usePathname } from '@i18n/navigation';
import LocaleSwitcher from './LocaleSwitcher';

const navItems = [
  { key: 'home', href: '/' },
  { key: 'about', href: '/about' },
  { key: 'products', href: '/products' },
  { key: 'solutions', href: '/solutions' },
  { key: 'blog', href: '/blog' },
  { key: 'faq', href: '/faq' },
  { key: 'contact', href: '/contact' },
] as const;

export default function Header() {
  const t = useTranslations('nav');
  const [open, setOpen] = useState(false);
  const pathname = usePathname() || '/';

  const isActive = (href: string) => {
    if (href === '/') return pathname === '/';
    return pathname.startsWith(href);
  };

  return (
    <header className="header">
      <div className="header-inner container">
        <Link href="/" className="brand" onClick={() => setOpen(false)}>
          <img src="/logo.png" alt="Kaichen Power" className="brand-logo" />
          <span className="brand-text">Kaichen<span>Power</span></span>
        </Link>
        <nav className="nav" aria-label="Main navigation">
          {navItems.map((item) => (
            <Link key={item.key} href={item.href} className={`nav-link${isActive(item.href) ? ' is-active' : ''}`}>
              {t(item.key)}
            </Link>
          ))}
        </nav>
        <div className="header-right">
          <LocaleSwitcher />
          <button
            type="button"
            className={`nav-toggle${open ? ' is-open' : ''}`}
            aria-label="Toggle navigation"
            aria-expanded={open}
            aria-controls="nav-mobile"
            onClick={() => setOpen((o) => !o)}
          >
            <span className="nav-toggle-bar" />
            <span className="nav-toggle-bar" />
            <span className="nav-toggle-bar" />
          </button>
        </div>
      </div>

      <nav id="nav-mobile" className={`nav-mobile${open ? ' is-open' : ''}`} aria-label="Mobile menu">
        {navItems.map((item) => (
          <Link key={item.key} href={item.href} className={`nav-mobile-link${isActive(item.href) ? ' is-active' : ''}`} onClick={() => setOpen(false)}>
            {t(item.key)}
          </Link>
        ))}
      </nav>
    </header>
  );
}
