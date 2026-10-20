import { getRequestConfig } from 'next-intl/server';
import { routing } from './routing';

export default getRequestConfig(async ({ requestLocale }) => {
  // 解析当前请求的 locale，非法或缺失时回退到默认英文
  let locale = (await requestLocale) ?? routing.defaultLocale;
  if (!routing.locales.includes(locale as (typeof routing.locales)[number])) {
    locale = routing.defaultLocale;
  }

  return {
    locale,
    messages: (await import(`../content/i18n/${locale}.json`)).default,
  };
});
