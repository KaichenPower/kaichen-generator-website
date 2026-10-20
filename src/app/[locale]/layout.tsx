import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { NextIntlClientProvider } from 'next-intl';
import { getMessages, getTranslations, setRequestLocale } from 'next-intl/server';
import { routing } from '@i18n/routing';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import MobileNav from '@/components/MobileNav';
import BackToTop from '@/components/BackToTop';
import CookieConsent from '@/components/CookieConsent';
import JsonLd from '@/components/JsonLd';
import { getAlternates, siteConfig } from '@/lib/site';
import '../globals.css';

type Props = { params: Promise<{ locale: string }> };

export function generateStaticParams() {
  return routing.locales.map((locale) => ({ locale }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params;
  if (!routing.locales.includes(locale as (typeof routing.locales)[number])) return {};
  setRequestLocale(locale);
  const t = await getTranslations({ locale, namespace: 'meta' });
  const alternates = getAlternates('/');
  return {
    title: {
      default: t('title'),
      template: `%s | ${t('title')}`,
    },
    description: t('description'),
    alternates: {
      canonical: alternates[locale] || alternates.en,
      languages: alternates,
    },
    openGraph: {
      title: t('title'),
      description: t('description'),
      type: 'website',
      locale,
      siteName: 'Kaichen Power',
    },
    robots: { index: true, follow: true },
  };
}

export default async function RootLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: Props['params'];
}) {
  const { locale } = await params;
  if (!routing.locales.includes(locale as (typeof routing.locales)[number])) {
    notFound();
  }
  setRequestLocale(locale);
  const messages = await getMessages({ locale });

  return (
    <html lang={locale} dir="ltr">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
          rel="stylesheet"
        />
      </head>
      <body>
        <JsonLd
          data={{
            '@context': 'https://schema.org',
            '@type': 'Organization',
            name: siteConfig.brandName,
            legalName: siteConfig.legalName,
            url: siteConfig.domain,
            logo: `${siteConfig.domain}/logo.png`,
            email: siteConfig.email,
            telephone: siteConfig.phone,
            address: {
              '@type': 'PostalAddress',
              streetAddress: siteConfig.address,
              addressCountry: 'CN',
            },
            sameAs: [
              siteConfig.social.facebook,
              siteConfig.social.youtube,
              siteConfig.social.vk,
            ].filter(Boolean),
          }}
        />
        <JsonLd
          data={{
            '@context': 'https://schema.org',
            '@type': 'WebSite',
            name: siteConfig.brandName,
            url: siteConfig.domain,
            inLanguage: locale,
            publisher: { '@type': 'Organization', name: siteConfig.brandName },
          }}
        />
        <NextIntlClientProvider locale={locale} messages={messages}>
          <div className="site-shell">
            <Header />
            <main className="site-main">{children}</main>
            <Footer />
          </div>
          <MobileNav />
          <BackToTop />
          <CookieConsent />
        </NextIntlClientProvider>
      </body>
    </html>
  );
}
