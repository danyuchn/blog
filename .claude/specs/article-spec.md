# 文章規格（Article Spec）

規範性文件：新增或修改 `src/data/blog/{zh,en}/*.md` 的每一篇文章都必須符合本規格。
起手請複製 `.claude/templates/article.md`，不要從零手打 frontmatter。
機器可查的規則由 `npm run check:content` 強制（CI blocking）；其餘規則寫作時遵循。

## 檔名與 slug（validator 強制）

- 檔名：kebab-case、全小寫、英文（中文文章的檔名也用英文），如 `adhd-skill-agentic-search.md`。
- **zh 與 en 檔名必須完全相同**：`zh/foo.md` ↔ `en/foo.md`。翻譯配對（`src/utils/i18n.ts`）唯一依據是同檔名，檔名不同 = 翻譯連結斷掉。
- `slug` 必寫，固定等於 `<lang>/<檔名去 .md>`。
- 底線開頭檔名（`_draft.md`）會被 content loader 忽略，不要用。

## Frontmatter 欄位規則

欄位順序照模板。標「強制」者由 validator 擋 CI。

| 欄位 | 規則 | 強制 |
|---|---|---|
| `author` | 顯式寫 `Dustin Yuchen Teng`（不省略、不靠 schema default） | ✅ |
| `pubDatetime` | `YYYY-MM-DDT04:00:00Z`（UTC 04:00 = 曼谷 11:00）。**必須是已過去的時間** | ✅（未來時間擋）|
| `modDatetime` | 只有會持續更新的檔（micro-notes 等）才用 | |
| `title` | 含半形 `: ` 時整值用雙引號包；全形 `：` 不用 | |
| `slug` | 見上節 | ✅ |
| `featured` | 顯式寫 `false`（精選文章才 `true`，全站僅個位數） | ✅ |
| `draft` | 顯式寫 `false` | ✅ |
| `tags` | 2–3 個，YAML list 格式，**只准用 `.claude/specs/tags.md` 白名單內的 tag** | ✅（白名單）|
| `description` | **無條件用單引號包住**，內部 `'` escape 成 `''`。中文 35–90 字；英文可較長但求精簡 | |
| `ogImage` | 不使用（OG 圖由 `index.png.ts` 動態生成） | |

### 兩個高頻陷阱（historical incidents，違反必炸）

1. **pubDatetime 未來時間**：build 不會失敗，但文章被 `src/utils/postFilter.ts` 靜默過濾——首頁、RSS、翻譯連結全部消失，只有文章頁本身存在。W18 前後多次踩過。validator 現在會直接擋。
2. **description 含半形 `: ` 未加引號**：YAML 把它解析成新的 mapping key，`astro check` 報 `bad indentation of a mapping entry`。W20 一週連踩 3 次。所以規則是無條件單引號，不要自行判斷「這句沒冒號可以裸寫」。

## 內文結構

- **短敘事文**（截圖敘事、單一事件）：不用任何標題層級，純段落＋圖片。
- **長文／聚類文**：只用 H2（`##`）分節。不用 H1（title 會生成 H1）、幾乎不用 H3。
- 段落 2–5 句，第一人稱口語。作者 voice 見 `.impeccable.md`（曼谷 GMAT 老師轉 AI builder，個人・真實・有溫度）。
- **結尾短促收束**（如「就這樣。」），禁止 AI 式收尾：不寫 `## 小結`／`## 結語`、不排比喊話、不總結昇華。

## 改寫原則（社群貼文 → 文章時適用）

1. **保留原聲**：作者的語氣、俚語、比喻、意見逐字保留，絕不替作者添加他沒表達過的觀點。
2. **去平台碎片化**：把多則短貼文織成有邏輯流的段落。
3. **去重**：IG/Threads 同內容只留最完整版。
4. **濾雜訊**：裸連結、宣傳 CTA、報名表、無上下文 @mention 全刪。
5. **禁 AI 腔**：不加總結句、「讓我們一起探索」、emoji 點綴、湊數 bullet。
6. **最小銜接（忠實度）**：AI 只做最小銜接，不替作者補技術解釋、情緒鋪陳、論述展開。原貼文沒有的論點就不要加。**短素材保持短而緊湊**——歷史教訓：~150 字短貼文曾被 subagent 膨脹成長論述。
7. **文末自首註解**：改寫文結尾必留 HTML 註解，逐句列出 AI 新增的非原文句子並標註類型（框架句／銜接／改寫），格式見模板。這讓任何後續審查者能快速裁決忠實度。

## 圖片

- 目錄：`public/assets/posts/<slug-basename>/`。**目錄名不含語言前綴**（用 `foo` 不是 `zh/foo`），zh/en 共用同一目錄。
- 引用：`![完整描述句作 alt](/blog/assets/posts/<basename>/<name>.jpg)`——路徑必含 base path `/blog`。alt 是完整句子，zh/en 各自翻譯。
- 格式一律 `.jpg`。命名 pattern：截圖敘事 `1-start.jpg`、`2-xxx.jpg`；IG 圖卡 `card-1-主題.jpg`；官方公告截圖 `announcement.jpg`。
- validator 會驗證引用路徑對得到實體檔。
- 圖片複製由主對話執行，不交給寫手 subagent（見 fan-out 協議）。

## YouTube 嵌入（二選一）

1. **響應式播放器**（文章主體就是這支影片時）：

   ```html
   <div class="video-embed"><iframe src="https://www.youtube.com/embed/<ID>" title="影片標題" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
   ```

   `.video-embed` class 定義在 `src/styles/typography.css`（16:9 響應式）。

2. **內文參照連結**（週報型、順帶提及）：`<https://youtu.be/<ID>>` 或 `[說明](https://youtu.be/<ID>)`。

## 雙語流程

- 一律**先寫 zh，再翻 en**。en 內文段落與 zh 一一對應（同段數、同順序圖片）。
- en 翻譯完成後過 `/humanizer` skill 去 AI 腔。
- title/description/alt text 各自在地化，不逐字直譯。
