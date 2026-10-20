'use client';
import { useTranslations } from 'next-intl';
import { Link } from '@i18n/navigation';

const items = [
  { key: 'home', href: '/' },
  { key: 'products', href: '/products' },
  { key: 'blog', href: '/blog' },
  { key: 'inquiry', href: '/contact' },
] as const;

export default function MobileNav() {
  const t = useTranslations('footerMobile');
  return (
    <nav className="mobile-nav" aria-label="Mobile navigation">
      {items.map((item) => (
        <Link key={item.key} href={item.href} className="mobile-nav-item">
          <span className="mobile-nav-label">{t(item.key)}</span>
        </Link>
      ))}
    </nav>
  );
}
