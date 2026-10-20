import { Link } from '@i18n/navigation';
import JsonLd from './JsonLd';

type Crumb = { label: string; href?: string; url?: string };

/**
 * 页面包包屑导航（含 BreadcrumbList 结构化数据）。
 * - href：站内语言路径，用于点击跳转（如 /products）
 * - url：绝对地址，用于 JSON-LD 的 item
 */
export default function Breadcrumbs({ items }: { items: Crumb[] }) {
  return (
    <>
      <nav aria-label="Breadcrumb" className="breadcrumbs container">
        <ol>
          {items.map((it, i) => {
            const last = i === items.length - 1;
            return (
              <li key={i}>
                {it.href && !last ? (
                  <Link href={it.href}>{it.label}</Link>
                ) : (
                  <span aria-current="page">{it.label}</span>
                )}
              </li>
            );
          })}
        </ol>
      </nav>
      <JsonLd
        data={{
          '@context': 'https://schema.org',
          '@type': 'BreadcrumbList',
          itemListElement: items.map((it, i) => ({
            '@type': 'ListItem',
            position: i + 1,
            name: it.label,
            ...(it.url ? { item: it.url } : {}),
          })),
        }}
      />
    </>
  );
}
