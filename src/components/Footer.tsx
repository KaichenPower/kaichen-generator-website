import { useTranslations } from 'next-intl';
import { Link } from '@i18n/navigation';
import { siteConfig } from '../lib/site';

export default function Footer() {
  const t = useTranslations('footer');
  const nav = useTranslations('nav');
  const common = useTranslations('common');

  const quickLinks = [
    { key: 'home', href: '/' },
    { key: 'about', href: '/about' },
    { key: 'products', href: '/products' },
    { key: 'solutions', href: '/solutions' },
    { key: 'blog', href: '/blog' },
    { key: 'FAQ', href: '/faq', label: 'FAQ' },
    { key: 'contact', href: '/contact' },
  ] as const;

  return (
    <footer className="footer">
      <div className="footer-grid container">
        <div className="footer-col footer-about">
          <div className="footer-brand">
            <img src="/logo.png" alt="Kaichen Power" className="brand-logo" />
            <span className="brand-text">Kaichen<span>Power</span></span>
          </div>
          <p className="footer-about-text">{t('aboutText')}</p>
          <div className="footer-social">
            <a
              href={siteConfig.social.facebook}
              target="_blank"
              rel="noopener noreferrer"
              className="footer-social-link"
              aria-label="Kaichen Power on Facebook"
            >
              <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true">
                <path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.4v7A10 10 0 0 0 22 12Z"/>
              </svg>
            </a>
            <a
              href={siteConfig.social.youtube}
              target="_blank"
              rel="noopener noreferrer"
              className="footer-social-link"
              aria-label="Kaichen Power on YouTube"
            >
              <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true">
                <path d="M23 7.2a3 3 0 0 0-2.1-2.1C18.8 4.6 12 4.6 12 4.6s-6.8 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12 31 31 0 0 0 1 16.8a3 3 0 0 0 2.1 2.1c2.1.5 8.9.5 8.9.5s6.8 0 8.9-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 23.5 12 31 31 0 0 0 23 7.2ZM9.7 15.4V8.6l6.1 3.4Z"/>
              </svg>
            </a>
            <a
              href={siteConfig.social.vk}
              target="_blank"
              rel="noopener noreferrer"
              className="footer-social-link"
              aria-label="Kaichen Power on VK"
            >
              <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true">
                <path d="M13.2 18.4c-5.9 0-9.6-4.2-9.8-11.2h3c.1 5 2.3 7.1 4 7.5V7.2h2.8v4.3c1.7-.2 3.5-2.1 4.1-4.3h2.8c-.5 2.8-2.5 4.7-3.9 5.5 1.4.7 3.6 2.5 4.4 5.7h-3c-.6-2-1.9-3.6-3.7-4v4h-.7Z"/>
              </svg>
            </a>
            <a
              href={siteConfig.social.instagram}
              target="_blank"
              rel="noopener noreferrer"
              className="footer-social-link"
              aria-label="Kaichen Power on Instagram"
            >
              <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true">
                <path d="M12 2.2c3.2 0 3.6 0 4.8.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.2.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.2.1-1.6.1-4.8.1s-3.6 0-4.8-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.8c.1-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2Zm0 3.2a6.6 6.6 0 1 0 0 13.2 6.6 6.6 0 0 0 0-13.2Zm0 10.9a4.3 4.3 0 1 1 0-8.6 4.3 4.3 0 0 1 0 8.6Zm6.8-11.1a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3Z"/>
              </svg>
            </a>
            <a
              href={siteConfig.social.linkedin}
              target="_blank"
              rel="noopener noreferrer"
              className="footer-social-link"
              aria-label="Kaichen Power on LinkedIn"
            >
              <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true">
                <path d="M20.4 20.4h-3.5v-5.6c0-1.3 0-3-1.9-3s-2.1 1.4-2.1 2.9v5.7H9.4V9h3.4v1.6h.1c.5-.9 1.6-1.9 3.4-1.9 3.6 0 4.3 2.4 4.3 5.5v6.2ZM5.3 7.4a2 2 0 1 1 0-4.1 2 2 0 0 1 0 4.1ZM7.1 20.4H3.6V9h3.5v11.4Z"/>
              </svg>
            </a>
          </div>
        </div>

        <div className="footer-col">
          <h4>{t('quickLinks')}</h4>
          <ul className="footer-links">
            {quickLinks.map((link) => (
              <li key={link.key}>
                <Link href={link.href}>{'label' in link && link.label ? link.label : nav(link.key)}</Link>
              </li>
            ))}
          </ul>
        </div>

        <div className="footer-col">
          <h4>{t('productsTitle')}</h4>
          <ul className="footer-links">
            <li>
              <Link href="/products">{common('viewAll')}</Link>
            </li>
          </ul>
        </div>

        <div className="footer-col">
          <h4>{t('contactTitle')}</h4>
          <ul className="footer-contact">
            <li>
              <span className="footer-label">{t('email')}:</span>
              <a href={`mailto:${siteConfig.email}`} dir="ltr">{siteConfig.email}</a>
            </li>
            <li>
              <span className="footer-label">{t('whatsapp')}:</span>
              <a
                href={`https://wa.me/${siteConfig.phone.replace(/[^0-9]/g, '')}`}
                target="_blank"
                rel="noopener noreferrer"
                dir="ltr"
              >
                {siteConfig.phone}
              </a>
            </li>
            <li>
              <span className="footer-label">{t('address')}:</span>
              <span dir="ltr">{siteConfig.address}</span>
            </li>
          </ul>
        </div>
      </div>

      <div className="footer-bottom container">
        <p>
          © {new Date().getFullYear()} {siteConfig.legalName}. {t('rights')}
        </p>
        <div className="footer-legal">
          <Link href="/privacy">{t('privacy')}</Link>
        </div>
      </div>
    </footer>
  );
}
