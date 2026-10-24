# 每日自动发布规范（Blog & Product Publishing Standard）

> 本规范是每日定时发布任务的唯一执行标准。每次发布前必须先读取本文件，严格按照规范执行。

---

## 一、通用规则

### 1.1 内容质量红线
- ❌ **禁止**：模板化、凑字数、空洞内容
- ❌ **禁止**：不提国内客户名、地点（可以提 our Yangzhou factory）
- ✅ **必须**：每个产品/博客都要有具体技术参数、数值、单位
- ✅ **必须**：从用户痛点/选型问题切入，不是从产品参数切入
- ✅ **必须**：东康/重康统一归为 Cummins 品牌
- ✅ **必须**：图片不重复、产品不重复、文章不重复

### 1.2 多语言翻译标准
- **11 个语种**：en / ru / es / fr / de / pt / ar / tr / th / vi / id
- **英语**：完整深度文章（2000+ 字）
- **俄语、西班牙语**：完整翻译（1800+ 字）
- **其他 8 个语种**：至少完整翻译标题、关键参数表、核心结论（800+ 字）
- ❌ **禁止**：硬编码英文残留，所有可见文本必须翻译
- ❌ **禁止**：日期字段不加引号（必须写成 `date: "2026-10-24"`，否则 YAML 解析成 Date 对象导致 build 失败）

### 1.3 图片规范
- 正文开头**必须**有 Markdown 图片引用：`![alt text](/images/blog/xxx.jpg)`
- 图片从 `D:/projects/知识库/blog产品图片/` 或产品图片库选择
- 图片命名：用博客 slug 命名，不要重复使用已用过的图片
- 图片必须复制到 `public/images/blog/` 目录

### 1.4 SEO 标准
- **Title 长度**：控制在 50–60 字符，避免被 SERP 截断
- **Meta Description**：150–160 字符，包含核心关键词
- **H2/H3 层级**：清晰结构，包含关键词变体
- **内部链接**：每篇博客至少 2 个内链（指向产品页或其他博客）
- **URL slug**：自动生成，不需要手动指定

---

## 二、博客发布规范（Blog Day）

### 2.1 选题方向
从知识库问答库 / 售后问题 / 客户痛点中选主题：
- 选型类："How to choose a xxx kW generator"
- 故障类："Why your generator won't start / overheats / uses too much fuel"
- 对比类："Standby vs Prime power"、"Silent vs Open type"
- 场景类："Generator for hospitals / data centers / factories / farms"
- 维护类："Maintenance checklist"、"Oil change interval"

### 2.2 文章结构（必须包含）
1. **开头配图**：Markdown 图片引用
2. **引言**：从用户痛点切入，说明为什么这个问题重要
3. **工厂背书**：提一下 our Yangzhou factory、2 MW load bank test、warranty 等
4. **7–10 个分点**：每个分点包含：
   - 问题描述（为什么会发生）
   - 具体参数/数值/单位（如电压、压力、温度、电流、RPM）
   - 检查方法（怎么测、测哪里）
   - 解决方案（怎么修、换什么、多久换）
5. **参数表格**：至少 1–2 个对照表（如电池电压对照表、维护周期表、故障代码表）
6. **维护建议**：周/月/季度/年度保养清单
7. **CTA**：联系我们、查看产品、24/7 技术支持

### 2.3 字数要求
- 英语：2000–3000 字
- 俄语/西班牙语：1800–2500 字
- 其他 8 语种：800–1200 字（完整翻译核心内容）

---

## 三、产品发布规范（Product Day）

### 3.1 产品来源
- 从 `D:/projects/知识库/产品参数库/` 读取真实产品参数
- 产品图片从产品图片库选择，不要重复
- 东康/重康统一归为 Cummins

### 3.2 YAML 规范
- 文件位置：`content/products/xxx.yaml`
- 必须包含：slug、title、brand、power_kva、power_kw、engine_model、alternator_model、dimensions、weight、description、specs
- 所有规格标签和值必须翻译到 11 个语种（i18n 文件）

### 3.3 产品描述要求
- 从用户选型痛点切入，不是罗列参数
- 说明适用场景（医院、工厂、数据中心、矿山等）
- 包含具体技术参数（功率、电压、频率、噪音、尺寸、重量）
- 包含工厂背书和质保信息

---

## 四、Build & Push 流程

### 4.1 执行步骤
1. 先读取本规范文件
2. 确认今天是产品日还是博客日
3. 检查已发布列表，避免重复
4. 写内容 / 创建 YAML
5. 翻译到 10 个非英语语种
6. 复制配图到 public 目录
7. **检查日期格式**：所有 date 字段必须加引号
8. Build：`node node_modules/next/dist/bin/next build`
9. Push：`git add -A; git commit -m "message"; git push origin main`
10. 清理临时脚本文件

### 4.2 常见错误预防
- ❌ Date 字段不加引号 → build 失败（YAML 解析成 Date 对象）
- ❌ 正文没引用图片 → 页面没图
- ❌ 硬编码英文残留 → 其他语言页面有英文
- ❌ 图片文件名重复 → 图片不显示

---

## 五、发布记录

每次发布后更新 `_published-products.json` 或博客列表，记录已发布内容，避免重复。

---

**最后更新：2026-10-24**
