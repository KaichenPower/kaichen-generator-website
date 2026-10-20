import { defineRouting } from 'next-intl/routing';

// 全站支持的 10 种语言（与 content/i18n 下的翻译文件一一对应）
export const routing = defineRouting({
  locales: ['en', 'ru', 'es', 'fr', 'de', 'pt', 'ar', 'tr', 'th', 'vi', 'id'],
  defaultLocale: 'en',
});
