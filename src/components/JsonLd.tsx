/**
 * JSON-LD 结构化数据渲染组件。
 * 通过 dangerouslySetInnerHTML 注入，供搜索引擎 / AI 引用；
 * 对 < 做转义避免脚本注入。
 */
export default function JsonLd({ data }: { data: Record<string, unknown> }) {
  const json = JSON.stringify(data).replace(/</g, '\\u003c');
  return <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: json }} />;
}
