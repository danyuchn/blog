# Content Workflow（入口文檔）

本檔是內容產出的流程入口。**規格細節不在本檔**——寫作前先讀對應 spec，起手一律用 template，收尾一律跑 validator。
（本檔與 `.codex/content-workflow.md` 為刻意維護的雙份，必須逐字節相同；`npm run check:content` 會驗證。）

## 文件地圖

| 需求 | 讀哪裡 |
|---|---|
| 寫/改任何文章（frontmatter、檔名、圖片、embed、改寫七原則、voice） | `.claude/specs/article-spec.md` |
| 維護碎念三檔（上限、配對、抽取） | `.claude/specs/micro-notes-spec.md` |
| 選 tag / 新增 tag | `.claude/specs/tags.md`（白名單，CI 強制） |
| 新文章起手 | 複製 `.claude/templates/article.md` |
| 多篇並行寫作（fan-out） | `.claude/templates/fanout-writer-prompt.md`（含派工前/回收 checklist） |
| 每週週報全流程 | `.claude/checklists/weekly-roundup.md` |
| 機器驗證 | `npm run check:content`（CI blocking；錯誤訊息會指回對應 spec） |
| 品牌調性 / 讀者輪廓 | `.impeccable.md` |

## 社群匯入七步驟

1. **Extract & Classify**：`scripts/classify_posts.py`（Gemini 分類，30 則/批，輸出 gitignored 的 `scripts/classified_posts.json`）。
   - Meta 匯出是 latin-1 包 UTF-8，逐欄 `s.encode('latin-1').decode('utf-8')` 修正。
   - **Threads-only 匯出**（無 IG `posts_1.json`）會讓腳本報錯：跳過腳本、為當週日期範圍寫一次性分類 snippet，不要為單次案例改腳本。
   - **匯出視窗與上週重疊必去重**：匯出開頭一兩天的貼文常已收進上週週報，提案前對照上週 micro-notes 區段剔除。
2. **Aggregate**：聚類提案。**提案分批（全跑 vs Top N）時必說每個未選篇章的去處**（micro-notes / 留下週 / 棄寫），否則會補開重做。
3. **Write**：zh 先寫（照 article-spec + template）。
4. **Translate**：en 版，檔名與 zh 完全相同。
5. **Humanize**：en 全部過 `/humanizer` skill。
6. **Build & Verify**：`npm run check:content` → `npm run build` → `npm run dev` 抽查。
7. **Deploy**：停下等使用者明說「commit & push」。

## 圖卡（IG 輪播）匯入

圖片複製到 `public/assets/posts/<slug-basename>/` → Read 工具直接 OCR 圖片 → 以圖片內容為主要素材寫成完整文章 → 嵌入原圖（路徑與命名規則見 article-spec）。

## Fan-out 寫作協議

多篇全交 subagent 寫、主對話只驗證時，寫手 prompt 一律由 `.claude/templates/fanout-writer-prompt.md` 生成，不可自行簡化。三條鐵則（事故驅動，模板內有完整版）：

- **忠實度自首清單**：每個寫手必回報「新增非原文句子」逐句清單，主對話逐句裁決——比盲讀全篇快且不漏。
- **派工前 working tree 清乾淨、圖片主對話先複製**：W25 曾有寫手違規 `git add -A && commit && push`，把既有變更一併掃走。
- **收尾 commit 主對話自己做**：逐檔 `git add <path>`，禁 `git add -A`，等使用者指令。

## 語意去重工具

`scripts/semantic_dedup.py`：`gemini-embedding-2` 對全部文章（`--micro` 含碎念條目）做語意向量，列近重複對。
- 跑法：`export GEMINI_API_KEY=<key>` → `uv run scripts/semantic_dedup.py --micro --threshold 0.78 --json /tmp/blog_dedup.json`（key 在 `blog/.env`；失效再從 GMAT-skills / PDT-learning / crawler 借）。
- 判讀：**高相似 ≠ 該合併**。同主題不同角度、或時間軸上的觀點演進，保留比合併更有資訊量；published URL 無 redirect，真要合併才動。

## YouTube 來源澄清（自家上架 vs 訂閱）

週報「本週 YouTube 新增影片」預設指 **AgentCrew Academy 自家上架**（`playlistItems` API 抓 uploads playlist）。「訂閱頻道的新片」（`subscriptions` API，`scripts/youtube_weekly_scan.py`）是另一用途，需明確要求。上游盤點流程見 `~/knowledge-base/000-weekly-routines.md`。
