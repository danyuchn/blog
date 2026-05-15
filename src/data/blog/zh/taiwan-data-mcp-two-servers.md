---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-15T05:30:00Z
title: "台灣公開資料兩個 MCP 評測——mcp-taiwan-legal-db 跟 Twinkle Hub 各適合什麼場景"
slug: zh/taiwan-data-mcp-two-servers
featured: false
draft: false
tags:
  - mcp
  - taiwan-data
  - ai-tools
  - claude-code
description: 兩個串接台灣公開資料的 MCP server——一個專精法律判決跟法規查詢、一個聚合 5.3 萬筆政府開放資料 + 37 個在地工具。實測下來各有強項，課程跟顧問場景的搭配方式不一樣。
---

最近兩週測了兩個串接台灣公開資料的 MCP server。背景是 L2 課程需要「官方資料來源」的 demo 素材，順便評估能不能直接給 L3 顧問客戶（法務、合規、政府機關）用。

## mcp-taiwan-legal-db

GitHub：[lawchat-oss/mcp-taiwan-legal-db](https://github.com/lawchat-oss/mcp-taiwan-legal-db)。101 stars，2026-05-12 仍活躍更新。

8 個 MCP 工具，串接三個官方來源：

- 司法院裁判書（`search_judgments` / `get_judgment`）
- 全國法規資料庫（`query_regulation` / `search_regulations`）
- 憲法法庭釋字／憲判字（`get_interpretation` / `search_interpretations`）
- 引用圖譜（`get_citations`）

技術細節幾個值得記的點：

- **混合請求策略**：一般走 httpx（約 0.25 秒）；觸發司法院 F5 WAF 時自動切 Playwright 刷 cookie
- **離線快取大法官解釋**：868 筆全部 bundle 進來，查的時候不用打網路
- **安裝方式**：`git clone` → `pip install -e .` → repo 根目錄有 `.mcp.json`，在該資料夾開 Claude Code 自動載入，零設定

實測上週 L2 課我把法律 MCP 接起來做「查專利侵權判決」的 demo，五分鐘內從關鍵字搜尋拉到全文，學員的反應比新聞 RSS demo 強很多。法務、顧問背景的學員特別吃這套。

**風險**：司法院 API 是爬蟲方式（非官方 API key），WAF 繞過機制理論上有被封風險。另外 Playwright 依賴需要 `playwright install chromium`，課堂環境多一步設定。

## Twinkle Hub

來自 [Twinkle AI](https://hub.twinkleai.tw)。定位是「把 data.gov.tw 全量 52,960 筆政府開放資料整理成單一 MCP endpoint」。Alpha 期間完全免費。

三層架構：

1. **OpenData**（5.3 萬筆政府資料，分 19 個 domain：不動產地政、交通運輸、醫療衛生、環境、農林漁牧、政府採購、教育、法律司法、財政統計、外交僑務、原住民族、社福勞工、文化觀光、產業科技、氣象、能源、公共安全、人口戶政、其他）
2. **TW Utility Tools**（37 個在地工具）
3. **BYO 連接器**（Notion / Sentry / n8n 等本機安裝）

第二層的 37 個 utility 工具實用度極高。我自己最常用的：

| 用途 | 工具名 |
|------|--------|
| 統編查公司登記 | `twtools-lookup_company_by_tax_id` |
| 統編 checksum | `twtools-validate_tax_id_number` |
| 身分證驗證 | `twtools-validate_taiwan_id_number` |
| 中文地址正規化 | `twtools-normalize_taiwan_address` |
| 中文地址英譯 | `twtools-address_zh_to_en` |
| 民國 ←→ 西元 | `twtools-roc_year_to_western` |
| 判定工作日／補假 | `twtools-is_taiwan_business_day` |
| 國定假日查詢 | `twtools-lookup_holidays` |
| 陽農曆互換 | `twtools-solar_to_lunar` / `lunar_to_solar` |
| 簡繁轉換 | `twtools-simplified_to_traditional` |

**安裝一行指令**（Alpha 期間免費，無需儲值）：

```bash
claude mcp add --transport http twinkle-hub https://api.twinkleai.tw/mcp/ \
  --header "Authorization: Bearer sk-..."
```

到 `https://hub.twinkleai.tw/login` 用 Google 或 GitHub 登入拿 API key 即可。

**踩坑**：我實測 4 個 dataset 的時候，金管會裁罰、勞動違規、統編查公司都很順，但 IPC 專利分類那一個會回亂碼，看起來是上游 data.gov.tw 編碼問題，跟 Twinkle Hub 自己無關。

## 兩個怎麼搭配

我自己現在的分工是：

- **mcp-taiwan-legal-db**：所有「需要看判決書、看法條原文」的場景。法律 demo、L3 顧問導入、給法務客戶用
- **Twinkle Hub**：所有「需要查政府其他資料」的場景。商業 demo、L2 課堂示範「政府開放資料 + MCP」整合、客戶背景調查（統編查公司）

兩個都裝著沒衝突。Claude Code 在判斷該叫哪個工具的時候，從工具名稱跟 description 就能分辨清楚。

如果你只裝一個，我會建議先裝 Twinkle Hub。因為 37 個 utility 工具的覆蓋面太廣，連「下個月 12 號是不是工作日」這種日常查詢都能直接問。法律 MCP 適合特定場景，但 Twinkle Hub 是每天都會用到的那種。
