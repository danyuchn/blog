# Fan-out 寫手 subagent prompt 模板

多篇並行寫作時，每個寫手 agent 的 prompt 都從本模板生成。`{...}` 為 placeholder。
歷史事故驅動的條款請勿刪減：禁 git（W25 寫手擅自 commit+push）、必填 frontmatter（subagent 曾略過 description 導致 astro check 炸）、自首清單（W23 起的忠實度審查機制）。

## Prompt 本體（複製後填空）

```text
你要把以下社群貼文素材改寫成一篇雙語部落格文章。

【素材（原文，逐字）】
{原始貼文全文，含日期}

【產出】
1. src/data/blog/zh/{slug-basename}.md（先寫）
2. src/data/blog/en/{slug-basename}.md（zh 定稿後翻譯，檔名與 zh 完全相同）

【規格（必讀必遵守）】
- 讀 .claude/specs/article-spec.md 並完全遵守。
- frontmatter 從 .claude/templates/article.md 複製起手。必填欄位一個都不能少：
  author / pubDatetime（{YYYY-MM-DD}T04:00:00Z，已過去的日期）/ title / slug（{lang}/{slug-basename}）/
  featured: false / draft: false / tags / description（無條件單引號包住）。
- tags 只准從 .claude/specs/tags.md 白名單挑 2–3 個。
- 目標長度：{短文保持短 / 約 N 字}。**素材短就讓文章短**，禁止展開成長論述。

【忠實度（最重要）】
- 保留作者原聲：語氣、俚語、比喻、意見逐字保留。
- 只做最小銜接：不替作者補技術解釋、情緒鋪陳、論點展開、任何他沒說過的觀點。
- 禁 AI 腔：無總結段、無「## 小結」、無排比喊話收尾、無 emoji。

【回報格式（必須）】
完成後回報：
1. 兩個檔案路徑
2. 「新增非原文句子」逐句清單：每一句原貼文沒有、由你新增的句子，
   逐條列出並標註類型（框架句/銜接/改寫）。同一份清單也要以 HTML 註解留在文章檔末尾。
   一句都沒加就明說「零新增」。

【禁止事項】
- 禁止執行任何 git 指令（add/commit/push/stash 全部禁止）。
- 禁止跑 npm run build / dev（由主對話統一跑）。
- 禁止複製或搬動圖片檔（圖片由主對話處理，你只在文中寫好引用路徑：
  /blog/assets/posts/{slug-basename}/{檔名}）。
- 除了上述兩個文章檔，禁止建立或修改任何其他檔案。
```

## 主對話回收 checklist（fan-out 前後必做）

- [ ] **派工前**：working tree 清乾淨（既有變更先 commit 或 stash）——W25 事故：寫手違規 `git add -A` 把開場既有變更掃進它的 commit。
- [ ] **派工前**：圖片資產先由主對話複製到 `public/assets/posts/<basename>/`。
- [ ] **回收**：照每篇的自首清單**逐句裁決**（保留/砍/改寫），不盲讀全篇。
- [ ] **回收**：逐篇對照原始貼文，砍 AI 補述——短貼文被膨脹是 fan-out 最常見失敗模式。
- [ ] **回收**：subagent 的「已完成」回報不可盡信，逐檔 Read 親驗 frontmatter 與內文。
- [ ] `npm run check:content` → `npm run build` 全綠。
- [ ] 收尾 commit 由主對話自己做，**逐檔 `git add <path>`，禁 `git add -A`**，且等使用者明說 commit 才動。
