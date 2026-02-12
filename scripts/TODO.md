# IG/Threads → Blog 匯入待辦清單

## 批次規劃

### Batch 1：核心個人觀點（最容易產出、最有個人特色）✅ 完成
- [x] 1-1. Claude vs Gemini vs GPT 模型使用實錄 → `zh/claude-vs-gemini-vs-gpt.md`
- [x] 1-2. AI 時代的焦慮與適應 → `zh/ai-anxiety-and-adaptation.md`
- [x] 1-3. AI 碎念日記：短貼文集 → `zh/ai-micro-notes.md`

### Batch 2：技術實戰經驗 ✅ 完成
- [x] 2-1. Claude Code 實戰心得：達克曲線 → `zh/claude-code-dunning-kruger.md`
- [x] 2-2. Vibe Coding 的真與假（含初學知識清單，合併 2-3）→ `zh/vibe-coding-truth.md`
- [x] ~~2-3. AI 輔助寫程式的初學知識清單~~ → 已併入 2-2

### Batch 3：產品與應用 ✅ 完成
- [x] 3-1. 從零打造 AI 產品的踩坑日記 → `zh/ai-product-building.md`
- [x] 3-2. 用 Claude Skill 做 FIRE 理財規劃 → `zh/fire-planning-with-claude.md`
- [x] 3-3. 我的 AI 工作流：收斂與發散 → `zh/ai-workflow-convergence-divergence.md`

### Batch 4：教育與轉型 ✅ 完成
- [x] 4-1. 教學者如何擁抱 AI 而不被取代 → `zh/teachers-embrace-ai.md`

### 混合內容審核 ✅ 完成
- [x] 審核 103 則 AI+GMAT 混合內容 → 已提取 D 類觀點寫成 `zh/ai-era-critical-thinking.md`
- [x] 其餘 A/B/C 類（已吸收、純推廣、GMAT 專屬細節）全部捨棄
- [x] 去重已在各 Batch 改寫過程中完成

---

## 每篇文章的產出流程

1. 從 `scripts/categories/*.md` 中選出對應貼文
2. 去重、排序、標註可用段落
3. 用 AI 聚合改寫成完整 blog 文章（保留原始觀點，消除社群口吻）
4. 生成 Astro frontmatter（title, pubDatetime, description, slug, tags）
5. 存入 `src/data/blog/zh/`
6. `npm run build` 驗證

## 注意事項

- `/tmp/ig_export/` 重開機會消失，如需重建：
  ```bash
  mkdir -p /tmp/ig_export
  unzip -o ~/Downloads/instagram-dustin_gmat-2026-02-12-7rsM9Jkr.zip \
    "your_instagram_activity/threads/threads_and_replies.json" \
    "your_instagram_activity/media/posts_1.json" \
    -d /tmp/ig_export
  ```
- 分類結果 `scripts/classified_posts.json` 不用重跑（除非要重新分類）
- 各分類的完整內容 `scripts/categories/*.md` 也不用重跑
