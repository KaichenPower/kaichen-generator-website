---
name: blog-seo-from-product-images
description: 从知识库产品图片中按品牌挑选未发布的图片，自动生成有深度、易被 Google 收录、对用户有用的英文博客文章，图片插入正文，标题含品牌+功率+机型关键词，并记录已发布图片避免重复。适用于"按品牌选产品图写文章/批量发布 SEO 博客"类需求。
---

# 从知识库产品图片批量生成 SEO 博客文章

## 用途

当用户要求"从知识库产品图片中选图写文章 / 按品牌发布博客 / 用产品图做 SEO 文章"时使用。目标是持续产出真实、有深度、关键词覆盖的英文博客，且**绝不重复使用已发布过的图片**。

## 关键路径

- 知识库产品图：`D:\projects\知识库\产品图片\<品牌> <功率>kW <机型>.jpg`
  - 品牌：Cummins, DOOSAN, Mitsubishi, Perkins, Scania, Shangchai, Volvo, Weichai, Yuchai
  - 机型：standard（开架）/ silent（静音）/ mobile trailer（拖车）/ power car
- 站点博客（英文根目录）：`D:\projects\kaichen-generator-website\content\blog\*.md`
- 图片输出目录：`D:\projects\kaichen-generator-website\public\images\blog\`
- 已发布记录（防重复清单）：`D:\projects\kaichen-generator-website\content\blog\_published-images.json`

## 执行流程

1. **读取防重复清单**：先读 `content/blog/_published-images.json` 的 `published[].source`（知识库源文件名）。
2. **挑选未发布图片**：列出 `D:\projects\知识库\产品图片\` 全部文件，排除已发布的 source。可按"每品牌一张、不同功率段/机型"选，保证内容差异化。
3. **复制图片**：把选定图片复制到 `public/images/blog/`，用 URL 友好文件名，如 `cummins-300kw-silent.jpg`。
4. **写文章**：每篇一篇英文 `.md` 放在 `content/blog/` 根目录，文件名用语义化英文 slug。frontmatter 固定格式：
   ```
   ---
   title: "<Brand> <Power>kW <Type> Diesel Generator: <Benefit> Guide"
   date: "YYYY-MM-DD"
   excerpt: "一句话概括，含品牌+功率关键词，120 词以内。"
   ---
   ```
   - 正文第一张图用 `![alt 含关键词](/images/blog/<file>.jpg)` 插入。
   - 结构：What Is / Key Specifications(表格) / What It Does / Key Advantages(列表) / What Problems It Solves(列表) / Typical Applications / CTA。
   - 必须覆盖关键词：品牌、功率(kW/kVA≈kW×1.25)、机型(open/silent/container/mobile)。
   - 参数写"Typical"典型值，注明按电压/频率/环境调整；不编造认证编号、型号、联系方式等事实。
   - 600–900 词，H2 分层，结尾 CTA 引导询盘。
5. **更新清单**：把本次使用的每张图追加到 `_published-images.json`（source、copied_to、post、published_on、brand）。
6. **重建验证**：杀 3000 端口 next 进程 → `next build` → `next start -p 3000` → `Invoke-WebRequest` 验证博客列表与新文章页 200、图片 200。

## 规则

- 每篇只对应一个品牌的一张真实产品图，标题必须含品牌+功率+机型关键词。
- 文章为英文（面向 Google 收录的 B2B 站）。
- 严禁重复使用 `_published-images.json` 里已记录的 source 图片。
- 图片必须真实来自知识库，不要 AI 生成产品图。
- 博客对外 URL slug 由文章 title 自动 slugify，无需手动指定。
