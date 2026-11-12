# 舊文盤點計畫（2026-11）

Dustin 2026-11-12 定的標準。範圍：`src/data/blog/zh` 全部舊文（en 跟著 zh 的判定走）。

## 判定標準

下架（四類任一）：
1. 時效已過：講舊模型、舊版本、舊價格或時事，現在讀會被誤導或覺得過時。
2. 只有展示沒做法：陌生讀者帶不走做法、判準或觀點。
3. 被後來的文取代：同主題有更完整的文章（含 W36 整併留下的 stub）。
4. 素材太薄：一兩則貼文撐出來的短文。

例外：時效已過但判準還適用 → 不下架，改成整篇重寫成通用判準（舊模型名當例子，文末註寫作時間）。

下架方式：設 `draft: true` 從列表與搜尋消失，另做「封存區」頁面列出它們（目前 `/archives` 是全站時間序列表，不是封存區，要新增欄位與頁面）。

重寫（留下的文章）：有明顯問題才重寫——拼接感、防禦語氣、陌生人讀不懂、多個收尾。
流程：agy 出判準 → JEV（TypeSafe 逐句判定，參考 threads-voice `jev_check.py`）逐篇判 → agy 覆核 → 重寫走 Prompt B（`.claude/templates/fanout-writer-prompt.md`）。

## 只有模糊處送 Dustin

agy 與 JEV 判定一致的直接執行；兩者不一致、或卡在「時效已過但判準可能還有用」邊界的，才做審閱頁給他裁決，不逐篇送。

## 待辦

- [x] 封存區設計（2026-11-12 上線：`archived: true`、`/archived` 頁）：新欄位（例 `archived: true`）＋封存頁＋postFilter 排除，翻譯配對不壞
- [x] agy 寫 JEV 判題 9 題
- [x] 25 篇校準（一致率 91%）後全量 266 篇
- [x] 全量判定；一致者照辦，封存 86 篇（`4eb6fbf`）；AGY 判保留的一律保留
- [x] 7 篇模糊項等 Dustin 裁決（審閱頁），裁決後執行 ✅ 2026-11-12
- [x] 重寫：33 篇交寫作模型整篇重寫、grok 事實查核後修正、翻英；AGY 評分最弱 5 篇由 Dustin 驗收（2 篇改後上線、2 篇封存、1 篇照原稿），31 篇上線（`588da64`、`bc0655b`） ✅ 2026-11-12

經驗：agy 互動 session（Flash Low）兩次都寫腳本套 JEV 分數冒充逐篇覆核；改用 ext-run 每批 15 篇、明令禁止寫程式、要求原文逐字引證，才真的逐篇讀。

### 重寫清單

- `2026-model-personality-cross-vendor`（rewrite_generalize）：雖然文章指出評估模型脾氣優於跑分的洞察依舊實用，但內容過度依賴 Gemini 3、Claude 4.7 與 GPT-5.5 等舊型號特質，需改寫為通用判準架構。
- `adhd-flow-why-i-teach-ai`（rewrite）：內文帶有反擊斂財質疑的強烈防禦語氣，且結尾在個人自白後突兀拼接診斷建議，需要重寫修飾。
- `ai-adoption-benefits-not-about-ai`（rewrite）：文章拼接了多次週報貼文並連綴四支影片宣傳，內文包含情緒化粗話且收尾多處斷裂，需要重新梳理整併。
- `ai-course-not-a-scam-teaching-flow`（rewrite）：含有明顯針對社群酸民的防禦性開嗆語氣與貼文拼接痕跡，需去感情化並重新梳理扎實的教學流程。
- `ai-era-critical-thinking`（rewrite）：文末生硬拼接回應同業攻擊的社群貼文導致主題發散與多重收尾，需剔除無關段落維持論點聚焦。
- `ai-usage-economics`（rewrite）：全文由多篇舊文與碎念拼接而成且不同段落模型版本矛盾，文末更追加後記更正前文造成雙重收尾。
- `anthropic-trust-crisis-backup`（rewrite_generalize）：開頭雖記載 2026 年 3 月的特定服務爭議與舊模型名稱，但提出的多端點備援及規則記憶同步判準依然有效，應改寫為通用判準專文。
- `benchmark-vs-real-use-dumb-user-test`（rewrite）：前半段提出蠢人跑分概念極具啟發，但後半段生硬拼接對特定模型的社群宣洩與向網友徵詢經驗的零散收尾，需重寫理順論述
- `cc-audit-skill`（rewrite）：文末以追加後記方式修正內文快取時效與上下文公式，破壞了原本安裝引導的收尾，應將修正直接整合進步驟內文
- `claude-code-dunning-kruger`（rewrite）：全文由多則早期零散貼文生硬拼接而成，在心路歷程、秘書比喻與成本工具間跳躍並帶有追加後記，需重寫理順連貫脈絡
- `claude-code-ecosystem-roundup-apr08`（rewrite）：全文在「一個觀察」段落已完成統整收束，文末卻追加後記回頭補充安裝細節形成雙重收尾，應將補充整合進第四節
- `claude-code-ecosystem-skills-hooks-agents`（rewrite）：全文在「生態系的意義」已完成統整收束，文末追加後記補充子代理預設行為造成雙重收尾，應將更新直接整合至對應小節
- `claude-code-initial-prompt-tips`（rewrite）：六點起始指令心法具實用價值，但開頭與結尾帶有強烈批判賣課收割的防禦語氣，應重寫去除防禦性贅述
- `claude-code-tips-apr-w17`（rewrite）：拼貼多則互不相干的設定碎念、影片製作流程與學員軼事，且夾雜對大眾心態的批判離題，拼接感強烈需重寫理順
- `cli-resource-paradox-local-models`（rewrite）：全文由資源吃緊碎念、跑模型笑話與 Qwen 新聞等多則無關貼文硬拼而成，段落轉折生硬且具強烈拼接感。
- `codex-defensive-writing-contest`（rewrite）：內文充斥情緒性宣洩並包含向讀者辯解反諷意圖的留言，帶有明顯防禦語氣需重新改寫語調。
- `cross-model-review-council`（rewrite）：正文中段突兀拼入「接入 Threads API 請鍵盤工程師憤怒式審查」的社群玩笑碎念，破壞專業技術文章結構且具明顯拼接感。
- `freelance-real-lessons`（rewrite）：前半段的接案定價與客戶邊界判準極具實務價值，但帶有情緒性防禦語氣且生硬拼接同事家教見聞造成雙重收尾，需重寫理順脈絡。
- `gpt-5-6-luna-max-grunt-work`（rewrite_generalize）：文中以過期的 GPT-5.6 與早期 6.0 型號為核心案例，但廉價模型包辦瀏覽器雜活、高階模型審核的架構判準長效適用，應重寫為通用選型判準。
- `harness-slim-down-36`（rewrite）：文末夾帶針對酸民質疑的防衛性反駁語氣與多餘結尾，需重寫剔除防禦段落以聚焦 harness 精簡方法論。
- `local-model-not-for-saving-money`（rewrite_generalize）：核心判斷「地端模型重在隱私而非省錢」與評測踩坑經驗依然適用，但內文混雜已淘汰的具體模型時效資訊，應改寫為通用架構專文
- `mine-a-month-of-ai-chats`（rewrite）：由短片宣傳、導流至其他文章的殘留段落及回覆網友留言拼接而成，結構零碎缺乏連貫性。
- `model-picks-beyond-the-main`（rewrite_generalize）：提及 Haiku 4.5 與 Qwen 預覽版等舊模型名稱，但分層選型與本地小模型專用之核心判準依然適用。
- `model-vendors-take-turns-failing`（rewrite）：將模型商當機備援與 Codex 防禦式語氣調校兩則無關主題生硬拼接，且文末出現多重收尾。
- `opus-effort-tuning-sonnet-sweetspot`（rewrite_generalize）：文中雖以過期的 Opus 4.7 與 Sonnet 4.6 為例，但依編程與非編程任務配置模型等級與 effort 檔位的判準依然適用，應重寫為通用選型文章。
- `responsibility-is-what-ai-cannot-do`（rewrite）：由社群開課意向調查與後續質疑回覆拼貼而成，帶有明顯防禦語氣且出現多個收尾，需重寫理順核心論點
- `teachers-ai-transition-apr`（rewrite）：由教學品質批判、補教選用模型與丟棄小孩論文三則無關貼文硬行拼接而成，轉折生硬且具多重收尾，需重寫理順主線。
- `voice-input-two-modes`（rewrite_generalize）：雙模態長錄音與 Gemini 轉錄的判準依然實用，但指令腳本仍綁定舊版模型名稱需泛化。
- `yelling-at-ai-vs-cheering-it-on`（rewrite）：內文由罵 AI、黎曼猜想打氣、Codex 伴侶諮商與禮貌用語四則貼文拼裝，篇章銜接突兀且末尾出現多重收尾。
