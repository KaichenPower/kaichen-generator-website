import { getRequestConfig } from 'next-intl/server';
import { routing } from './routing';

import en from '../content/i18n/en.json';
import ru from '../content/i18n/ru.json';
import es from '../content/i18n/es.json';
import fr from '../content/i18n/fr.json';
import de from '../content/i18n/de.json';
import pt from '../content/i18n/pt.json';
import ar from '../content/i18n/ar.json';
import tr from '../content/i18n/tr.json';
import th from '../content/i18n/th.json';
import vi from '../content/i18n/vi.json';
import id from '../content/i18n/id.json';

const messages: Record<string, any> = { en, ru, es, fr, de, pt, ar, tr, th, vi, id };

export default getRequestConfig(async ({ requestLocale }) => {
  let locale = (await requestLocale) ?? routing.defaultLocale;
  if (!routing.locales.includes(locale as (typeof routing.locales)[number])) {
    locale = routing.defaultLocale;
  }

  return {
    locale,
    messages: messages[locale],
  };
});
