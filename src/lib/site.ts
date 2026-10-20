import fs from 'fs';
import path from 'path';
import { load } from 'js-yaml';

const profilePath = path.join(process.cwd(), 'content', 'company', 'profile.yaml');
const profile = load(fs.readFileSync(profilePath, 'utf8')) as any;

// 全站 10 种语言定义（与 i18n/routing.ts、content/i18n 保持一致）
export const locales = ['en', 'ru', 'es', 'fr', 'de', 'pt', 'ar', 'tr', 'th', 'vi', 'id'] as const;
export type Locale = (typeof locales)[number];
export const defaultLocale: Locale = 'en';

export const siteConfig = {
  domain: profile.domain,
  brandName: profile.brandName,
  legalName: profile.legalName,
  email: profile.email,
  phone: profile.phone,
  address: profile.address,
  founded: profile.founded,
  registeredCapital: profile.registeredCapital,
  annualCapacityUnits: profile.annualCapacityUnits,
  annualSales: profile.annualSales,
  employees: profile.employees,
  plantAreaSqm: profile.plantAreaSqm,
  buildingAreaSqm: profile.buildingAreaSqm,
  certifications: profile.certifications || [],
  engineBrands: profile.engineBrands || [],
  unitTypes: profile.unitTypes || [],
  social: profile.social || {},
};

// 首页数据统计（真实公司数据，标签由各语种 home.stats 提供）
export const companyStats = [
  { value: String(profile.founded), labelKey: 'statsFounded' },
  { value: `${profile.annualCapacityUnits.toLocaleString('en-US')}`, labelKey: 'statsCapacity' },
  { value: `${profile.employees}+`, labelKey: 'statsEmployees' },
  { value: `${(profile.plantAreaSqm / 1000).toLocaleString('en-US')},000 m²`, labelKey: 'statsArea' },
];

// 生成多语言 hreflang 备用链接
export function getAlternates(path: string = '') {
  const alternates: Record<string, string> = {};
  locales.forEach((l) => {
    alternates[l] = `${siteConfig.domain}/${l}${path}`;
  });
  return alternates;
}
