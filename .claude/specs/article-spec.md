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
- **不寫防禦或免責語氣**（「老實說」「只代表…不代表…」「我這邊抓不到」「僅供參考」）。限制只在需要處用一兩句講一次，其餘直接講結論。
- **結尾短促收束**（如「就這樣。」），禁止 AI 式收尾：不寫 `## 小結`／`## 結語`、不排比喊話、不總結昇華。

### 站內連結不得指向合併 stub（validator 強制）

W36 文庫整併把數十篇舊文轉成 stub：`canonicalURL` ＋內文只有一句「已經併入…」。連過去讀者要再點一次才看到內容，所以連結一律指向 canonical 目標，不是原 slug。

**別憑記憶認 slug**——舊 slug 讀起來完全正常（`dont-scrape-login-sites`、`hotel-remote-cc-sop`、`silent-failures-verify-real-state` 都是 stub）。`npm run check:content` 會擋下並直接告訴你該連哪一篇；「檔案存在」不等於「內容在那裡」。

## 改寫原則（社群貼文 → 文章時適用）

1. **保留原聲**：作者的語氣、俚語、比喻、意見逐字保留，絕不替作者添加他沒表達過的觀點。
2. **去平台碎片化**：把多則短貼文織成有邏輯流的段落。
3. **去重**：IG/Threads 同內容只留最完整版。
4. **濾雜訊**：裸連結、宣傳 CTA、報名表、無上下文 @mention 全刪。
5. **禁 AI 腔**：不加總結句、「讓我們一起探索」、emoji 點綴、湊數 bullet。
6. **最小銜接（忠實度）**：AI 只做最小銜接，不替作者補技術解釋、情緒鋪陳、論述展開。原貼文沒有的論點就不要加。**短素材保持短而緊湊**——歷史教訓：~150 字短貼文曾被 subagent 膨脹成長論述。
7. **文末自首註解**：改寫文結尾必留 HTML 註解，逐句列出 AI 新增的非原文句子並標註類型（框架句／銜接／改寫），格式見模板。這讓任何後續審查者能快速裁決忠實度。
8. **私人姓名一律去識別化（凌駕第 1 條的逐字保留）**：客戶、學員、合作方、客戶同仁的真名（含英文名、公司名、課程或教案代號如 A-1／A-2）一律不出現，改成角色描述（「一位與會者」「客戶」「學員本人的電腦」）。素材是逐字的也一樣要改，**HTML 自首註解也算**（它會跟著頁面輸出）。公眾人物（如 Sam Altman）不受此限。本 repo 是公開的，發布前由 `npm run check:private` 機械攔截，名單在 repo 外（`~/knowledge-base/reference/data/blog-private-names.txt`），新客戶要補進名單。

## 併入既有文章（加節、碎念吸收、主題簇整併）

判準只有一條：**併完之後，讀起來要像一次寫成**。不是在文末再接一節。2026-10-26 全站審查 215 篇，80 篇讀起來像拼的，全部出自「文末加一節、標題寫『併入：』」的習慣。

1. **放進該在的位置**：新素材併進同主題的既有章節，或排在結論之前。全文只有一個收尾，而且放在最後。
2. **標題寫內容，不寫來歷**：不准出現「併入：」「補記：」「補充：」「附帶一條：」「Merged in:」「Postscript:」這類拼貼標記（`check:content` 會擋）。
3. **先去重再併**：新素材跟原文講同一件事時，只留最完整的一處；只出現一次的內容一律不准刪。
4. **時間詞對齊 pubDatetime**：「剛剛／今天／這週／明天」要跟文章的發布時間點與前後文一致，改成「後來」「那週」這類說法。
5. **過渡句只交代「為什麼接著講這個」**：一兩句、短、第一人稱。不准順手加原因、動機、事實或場景（例如「大概是負評太多才緊急推出」「這點我教學時超有感」都是越界）。
6. **description 跟著內容走**：併入後 description 跟內文對不上（例如坑數、範圍），就一起改。
7. **en 同步**：en 照新的 zh 結構做同樣的搬移與去重，只翻新增的過渡句，其他英文句子不動。
8. **自首註解**：在檔尾 HTML 註解加一段「<日期> 併入：」，逐句列出新增的過渡句，並用一句話寫出結構調整。

執行者是 agy，主對話只驗收：派工用 `.claude/templates/fanout-writer-prompt.md` Prompt B，併完跑 Prompt C 拼接審查，怪異度 ≥3 退回重做。

## 圖片

- 目錄：`public/assets/posts/<slug-basename>/`。**目錄名不含語言前綴**（用 `foo` 不是 `zh/foo`），zh/en 共用同一目錄。
- 引用：`![完整描述句作 alt](/blog/assets/posts/<basename>/<name>.jpg)`——路徑必含 base path `/blog`。alt 是完整句子，zh/en 各自翻譯。
- 格式一律 `.jpg`。命名 pattern：截圖敘事 `1-start.jpg`、`2-xxx.jpg`；IG 圖卡 `card-1-主題.jpg`；官方公告截圖 `announcement.jpg`。
- validator 會驗證引用路徑對得到實體檔。
- 圖片複製由主對話執行，不交給寫手 agy（見 fan-out 協議）。

### 主動配圖（選用，不強制）

素材沒附圖時，遇到下列情況可以自己畫 1–3 張示意圖；短敘事、心得、觀點文、社群貼文改寫照原樣不加。
- 值得畫：三步以上的流程或機制、前後對照、讀者看不到的畫面（終端機選單、設定頁）、會被拿來比較的數字。
- 不畫：一句話講得完的事、純裝飾、只為了版面好看。技術附錄給工程師看的圖可以多幾張，要畫出真實結構（時序、判斷分支、狀態），不只畫方塊箭頭。
- 做法：用 `.claude/figure-kit/`（`render.sh in.html out.jpg`；版面 720 CSS px、輸出 1440 寬、≤400KB；樣式照 `base.css`，即 ui-visual-defaults）。範例見 `example-gate-decision.html`。
- 規格：一般文字最小 15px、程式碼 14px，只有出處與小標可到 13px；放不下就改排版（側欄移下方、標籤分兩行），不縮字。
- 內容只能來自素材或可查的原始碼／數據；照紀錄重建的畫面在圖底註明「依實際紀錄重建」。en 版另畫一張，圖裡不得出現中文（範例也要翻）。
- 引用時包成可點開原圖：`[![alt](src)](src)`。

## YouTube 嵌入（二選一）

1. **響應式播放器**（文章主體就是這支影片時）：

   ```html
   <div class="video-embed"><iframe src="https://www.youtube.com/embed/<ID>" title="影片標題" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
   ```

   `.video-embed` class 定義在 `src/styles/typography.css`（16:9 響應式）。

2. **內文參照連結**（週報型、順帶提及）：`<https://youtu.be/<ID>>` 或 `[說明](https://youtu.be/<ID>)`。

## 雙語流程

- 一律**先寫 zh，再翻 en**。en 內文段落與 zh 一一對應（同段數、同順序圖片）。
- en 翻譯完成後由 agy 讀 `~/.claude/skills/humanizer/SKILL.md` 去 AI 腔（寫稿、翻譯、去 AI 腔都交 agy，主對話只驗收）。
- title/description/alt text 各自在地化，不逐字直譯。
