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
- **标题核心词**：必须以谷歌核心关键词排名为基础，标题前半部分必须包含目标搜索关键词
- **标题含义**：标题要符合用户搜索意图（informational / commercial），不能自嗨
- **Meta Description**：150–160 字符，包含核心关键词
- **H2/H3 层级**：清晰结构，包含关键词变体
- **内部链接**：每篇博客至少 2 个内链（指向产品页或其他博客）
- **URL slug**：自动生成，不需要手动指定

---

## 二、博客发布规范（Blog Day）

### 2.1 选题方向与内容来源
**内容必须紧紧围绕飞书知识库创作，禁止脱离知识库凭空编造。**
- 主题来源：从知识库问答库 / 售后问题 / 客户案例中选主题
- 必须提到凯晨电力的优势、经验、技术能力等有利于用户选择的内容
- 可以提：Yangzhou factory、2 MW load bank test、10+ years experience、24/7 technical support、1-year warranty、OEM/ODM partner 等
- 禁止：编造没有依据的数据、案例、客户名

可选主题方向：
- 选型类："How to choose a xxx kW generator"
- 故障类："Why your generator won't start / overheats / uses too much fuel"
- 对比类："Standby vs Prime power"、"Silent vs Open type"
- 场景类："Generator for hospitals / data centers / factories / farms"
- 维护类："Maintenance checklist"、"Oil change interval"

### 2.2 文章结构（必须包含）
1. **开头配图**：Markdown 图片引用
2. **标题**：必须包含核心搜索关键词，前半部分是关键词，后半部分是修饰（如 "Diesel Generator Won't Start: 7 Common Causes and Fixes"）
3. **引言**：从用户痛点切入，说明为什么这个问题重要
4. **工厂背书**：提一下 our Yangzhou factory、2 MW load bank test、warranty 等
5. **7–10 个分点**：每个分点包含：
   - 问题描述（为什么会发生）
   - 具体参数/数值/单位（如电压、压力、温度、电流、RPM）
   - 检查方法（怎么测、测哪里）
   - 解决方案（怎么修、换什么、多久换）
6. **参数表格**：至少 1–2 个对照表（如电池电压对照表、维护周期表、故障代码表）
7. **维护建议**：周/月/季度/年度保养清单
8. **CTA**：联系我们、查看产品、24/7 技术支持

### 2.3 字数要求
- 英语：2000–3000 字
- 俄语/西班牙语：1800–2500 字
- 其他 8 语种：800–1200 字（完整翻译核心内容）

---

## 三、产品发布规范（Product Day）

### 3.1 产品来源与内容原则
**内容必须紧紧围绕产品图片与产品中心、产品参数知识库，禁止乱编乱造。**
- 产品参数：从 `D:/projects/知识库/产品参数库/` 读取真实参数，一个数字都不能编
- 产品图片：从产品图片库选择，必须与产品名称匹配（silent 配 silent 图，open 配 open 图）
- 东康/重康统一归为 Cummins 品牌
- 产品描述只需要把参数描述清楚，加上以下内容：
  - **负载测试**：出厂前 2 MW digital load bank test、0–110% load test
  - **交付**：warranty 1 year / 1000 hours、OEM/ODM、packaging、delivery time
  - **行业解决方案**：适用行业（医院、工厂、数据中心、矿山、农业等）
- 禁止：编造没有依据的参数、功率、尺寸、重量

### 3.2 YAML 规范
- 文件位置：`content/products/xxx.yaml`
- 必须包含：slug、title、brand、power_kva、power_kw、engine_model、alternator_model、dimensions、weight、description、specs
- 所有规格标签和值必须翻译到 11 个语种（i18n 文件）

### 3.3 产品描述要求
- 从用户选型痛点切入，不是罗列参数
- 说明适用场景（医院、工厂、数据中心、矿山等）
- 包含具体技术参数（功率、电压、频率、噪音、尺寸、重量）——**必须与知识库一致，不能编**
- 包含负载测试信息：出厂前 2 MW load bank test
- 包含交付信息：warranty 1 year / 1000 hours、OEM/ODM
- 包含行业解决方案：该功率段适合哪些行业、典型应用

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
