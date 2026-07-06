# Tag 受控詞彙表

規範性文件＋機器可讀 SSOT。文章的每個 tag 都必須出現在下方白名單，否則 `npm run check:content` 報 error、CI 擋部署。

**格式契約（勿破壞）**：validator 只解析 `tag-allowlist:start` 與 `tag-allowlist:end` 兩個 HTML 註解標記之間、行首為 `- \`tag-name\`` 的條目。標記外的反引號 tag（如下方棄用對照表）不會被當成白名單。

## 使用規則

- 每篇 2–3 個 tag，全 kebab-case、全小寫、英文（中文文章也用英文 tag）。
- **優先從「核心」區挑**。長尾區是歷史存量，非必要不擴散使用。
- **要用新 tag：先在本檔白名單加一行（含一句適用說明），再用於文章**。順序反了 CI 會擋。加新 tag 前先檢查白名單有無語意相近者——本詞彙表的存在就是為了阻止 `opinion/opinions` 這種近義重複再發生。

## 已棄用 tag（canonical 對照）

2026-07-05 正規化，以下舊 tag 已從全部文章移除，**永不再用**：

| 棄用 | 改用 |
|---|---|
| `opinions` | `opinion` |
| `ai-security` | `security` |
| `ai-coding-tools` | `ai-coding` |
| `ai-models-comparison` | `model-comparison` |

長尾區仍有近義組（`workflow`/`ai-workflow`、`enterprise`/`enterprise-ai`/`enterprise-training`、`consulting`/`ai-consulting`、`ai-models`/`model-comparison`、`teaching-design`/`course-design`/`ai-course`）——存量凍結不動，新文章一律用核心區對應 tag，未來清理時再合併。

## 白名單

<!-- tag-allowlist:start -->

### 核心（新文章優先選用）

- `claude-code` — Claude Code 工具本身：功能、用法、生態
- `ai-tools` — AI 工具泛稱：評測、心得、比較
- `ai-trends` — AI 產業動態、模型發布、趨勢觀察
- `ai-workflow` — AI 工作流設計與方法論
- `opinion` — 觀點文、評論、立場表達
- `developer-experience` — 開發者體驗、DX 觀察
- `teaching` — 教學現場、授課心得
- `ai-education` — AI 教育、培訓主題
- `productivity` — 生產力、效率方法
- `ai-coding` — AI 輔助寫程式（coding agent、vibe coding 實務）
- `case-study` — 具體案例拆解
- `claude` — Claude 模型本身（非 Claude Code 工具）
- `gemini` — Google Gemini 相關
- `codex` — OpenAI Codex 相關
- `model-comparison` — 跨模型比較、評測
- `security` — 資安：漏洞、防護、踩坑
- `skills` — Claude Code skill 開發與應用
- `micro-notes` — 碎念系列檔案專用
- `harness` — Claude Code harness（rules/hooks/memory）工程
- `mcp` — Model Context Protocol
- `token-optimization` — token 用量、成本優化
- `personal` — 個人生活、非技術敘事

### 長尾（歷史存量，非必要不擴散）

- `agentcrew` — AgentCrew 品牌相關
- `agentic-coding` — agent 自主寫程式
- `ai-consulting` — AI 顧問案
- `ai-course` — AI 課程
- `ai-daily-use` — AI 日常應用
- `ai-economics` — AI 經濟學、用量經濟
- `ai-ethics` — AI 倫理
- `ai-industry` — AI 產業結構
- `ai-models` — AI 模型泛稱
- `ai-product` — AI 產品觀察
- `ai-product-building` — 打造 AI 產品
- `ai-safety` — AI 安全（alignment 層面）
- `anthropic` — Anthropic 公司動態
- `api-debugging` — API 除錯
- `automation` — 自動化
- `book-review` — 書評
- `business` — 商業經營
- `career` — 職涯
- `channel-growth` — 頻道成長
- `claude-app` — Claude 桌面/行動 App
- `code-review` — 程式碼審查
- `competitive-analysis` — 競品分析
- `consulting` — 顧問工作
- `contract` — 合約
- `course-design` — 課程設計
- `creator` — 創作者
- `debugging` — 除錯
- `digital-nomad` — 數位遊牧
- `email-marketing` — Email 行銷
- `enterprise` — 企業場景
- `enterprise-ai` — 企業 AI 導入
- `enterprise-training` — 企業內訓
- `ffmpeg` — ffmpeg
- `firebase` — Firebase
- `frameworks` — 思考框架
- `freelancing` — 接案
- `gmail` — Gmail
- `gotchas` — 踩坑集
- `gpt` — OpenAI GPT 模型
- `gpt-image` — GPT 圖像生成
- `ipad` — iPad 工作流
- `knowledge-management` — 知識管理
- `leadership` — 領導
- `learning` — 學習方法
- `lessons-learned` — 事後檢討
- `meta` — 部落格自身、後設內容
- `mindset` — 心態
- `non-engineer` — 非工程師視角
- `obsidian` — Obsidian
- `open-source` — 開源
- `organization` — 組織
- `personal-finance` — 個人理財
- `prompting` — 提示工程
- `recommended-reading` — 推薦閱讀
- `reflection` — 反思
- `remote-work` — 遠端工作
- `remotion` — Remotion
- `resend` — Resend
- `resources` — 資源整理
- `seo` — SEO
- `speaking` — 演講
- `subscription` — 訂閱制
- `system-maintenance` — 系統維護
- `taiwan-data` — 台灣公開資料
- `teaching-design` — 教學設計
- `vibe-coding` — vibe coding 現象
- `video-production` — 影片製作
- `workflow` — 工作流泛稱
- `youtube` — YouTube
- `others` — schema 預設值，不主動使用

<!-- tag-allowlist:end -->
