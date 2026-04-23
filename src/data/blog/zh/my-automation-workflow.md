---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-22T10:00:00Z
title: "我家的 Claude Code 自動化工作流：/loop、Monitor Tool、skill 體系、Obsidian 反思週報"
slug: zh/my-automation-workflow
featured: false
draft: false
tags:
  - claude-code
  - automation
  - ai-workflow
description: 從 /loop 指令幫我打 ERP 卡、Monitor Tool 做背景事件守門員、Google Map MCP 省瀏覽器操作、到 Obsidian 搭 Mirror 框架做反思週報——整理這半年我家 Claude Code 的自動化架構，順便釐清 commands 跟 skills 到底怎麼分。
---

半年下來，我的 Claude Code 工作流累積了一套自動化架構。

這篇不是要講「怎麼設定 X」的 how-to，而是想把幾個我實際每天用的自動化機制串起來，看整體是怎麼分工的。希望對正在摸索同類工作流的人有參考。

## 前提：commands 跟 skills 終於清楚了

先澄清一個常混淆的點。

今天讀官方文件才終於搞清楚：custom commands 是舊格式，已被合併進 skill 體系。兩者兼容，但 skill 多了目錄結構支援、frontmatter 控制、自動觸發。

以後統一叫 skill 就對了。

如果你還在 `.claude/commands/` 裡寫 `.md` 檔，官方建議遷移到 `~/.claude/skills/`。遷移不複雜，主要是加 frontmatter。

這個釐清對我整個工作流的分層架構影響很大——以前我把一些「指令式」的東西放在 commands、「知識式」的放在 skills，現在可以統一用 skill 結構管理。

## 第 1 層：`/loop` 排程指令

Claude Code 最新版本的 `/loop` 指令是我這半年覺得最實用的新功能之一。

實際使用案例：

**案例 A：自動打卡**

```
/loop 1d 幫我在 ERP 打卡
```

恭喜你，收穫全自動上下班。

**案例 B：Messenger 私訊中繼**

跟工作夥伴有部分還是在 Messenger 私人帳號上溝通，但是 Meta 沒辦法幫私人帳號接 API。所以我原本都是用截圖或複製訊息貼上。

現在有 `/loop` 可以自動循環執行任務了——定期開 Chrome MCP 去讀新訊息、彙整、放到我指定的資料夾。

`/loop` 的精髓在於「定期執行」是最簡單的自動化，但也是過去 Claude Code 最缺的一塊。有了之後很多小任務就不用手動觸發。

## 第 2 層：Monitor Tool 事件守門員

Claude Code 最近推出 Monitor Tool：讓 Claude 寫一段背景監看腳本（日誌、PR 狀態、API endpoint），只有偵測到重要事件才喚醒 agent，其他時間完全不消耗 token。

等於幫 agent 裝了一個守門員——別急著叫我，有事再說。

Monitor Tool 跟 `/loop` 是互補的：

- `/loop`：定期、無條件執行（我知道要做什麼、什麼時候做）
- Monitor Tool：不定期、條件觸發（我只在某件事發生時才要做）

前者是排程，後者是中斷。加起來能覆蓋大部分自動化需求。

我目前的 Monitor Tool 用例：

- 監看 GitHub Actions 失敗通知
- 監看 Vercel deploy 狀態
- 監看特定 API endpoint 的回應變化（外部 SaaS 狀態）

這些以前都是我開個 Terminal 視窗手動 `watch` 或 `tail -f`，現在 token 不消耗、事件來了才叫我。

## 第 3 層：MCP 工具層

MCP（Model Context Protocol）是讓 Claude 可以直接調用外部服務的標準協議。我常用的：

**Google Map MCP**（Anthropic 官方出的）

真好用。查地點、算距離、找路線，原本要開瀏覽器切來切去的流程，變成一條指令。對我這種在泰國常出門的人特別有感。

**agent-browser**（Vercel 出的 skill）

Chrome MCP 又耗 token 又容易斷線，只能說是最後的備案。如果不需要持久登入狀態的話，Vercel 出的 agent-browser skill 比它好用得多。

我的瀏覽器使用路由決策：

- 需要已登入 session（Google, Notion 等）→ Chrome MCP
- Bot detection 嚴格（Reddit, LinkedIn）→ Chrome MCP 或 JSON API
- 其他所有情境 → agent-browser

**crawl4ai**

搭配 agent-browser 用。`/agent-browser` 適合互動型，`/crawl4ai` 適合批量抓資料。

## 第 4 層：設計類 skill 的妙用

`/frontend-design` 醜死了怎麼辦？

直接叫他幫你重新設計，給你 20 個靜態 HTML 範例讓你選擇。

這是我最近發現的一個用法。以前我會直接調細節（改色碼、改 padding），結果改十次還是覺得不對。後來直接說「給我 20 個版本我挑一個」，反而比慢慢調效率高十倍。

這個心得背後的邏輯是：AI 擅長 generate、不擅長 iterate。你給它一次產多個候選，比叫它改一個候選好。

這個原則可以推廣到其他生成型 skill：寫 slogan、設計 logo、想命名、寫開場白。都是「給我 20 個我挑」比「給我 1 個我們慢慢改」有效率。

## 第 5 層：Obsidian + Mirror 框架反思週報

我的 Obsidian vault 裡面存放了：

- 日記
- 工作日誌
- 靈感
- 想法
- 各專案的連結
- 所有大大小小待辦事項

我常常問 Claude「今天我要做什麼」，然後每個禮拜還會用 Mirror 框架做反思週報：

1. 讀過去一週的 daily notes
2. 檢視自己的軌跡跟生涯目標是否符合
3. 找出最不願面對的教訓（比如拖延症）
4. 用原子習慣框架搭配給下週改善的建議

這是整個工作流的「覆盤層」。前面幾層都在執行，這一層在反省執行的方向對不對。

沒有這一層，自動化越強反而越容易快速地做錯事。有這一層，自動化才是放大器而不是放大錯誤的放大器。

## 整體架構

把這五層疊起來看：

```
【反思層】  Obsidian + Mirror 框架週報         ← 方向校準
【工具層】  MCP（Google Map / agent-browser）  ← 擴展能力
【中斷層】  Monitor Tool                        ← 事件觸發
【排程層】  /loop                               ← 定期觸發
【指令層】  skills（觸發即用）                  ← 主動呼叫
```

從下往上，每一層解決不同的問題。下面兩層（指令、排程）負責「做事」，中間層（中斷、工具）負責「效率」，上面一層（反思）負責「方向」。

## 我沒放進工作流的東西

同樣值得講。以下這些我有試過但最後沒留下：

- **AI 合成語音**：個人不喜歡，影片還是自己錄口白
- **複雜的 multi-agent 編排**：Claude Code 的 subagent 已經夠用，更複雜的框架（CrewAI、Autogen）對我的場景是 overkill
- **自動發布到社群平台**：我寧願自己排版檢查再發，自動發很容易出語氣不對的內容
- **大量資料處理直接餵 Opus**：改成先用 Opus 討論 schema，再用 SiliconFlow / OpenRouter 上的便宜模型批量處理

減法跟加法一樣重要。工作流不是越多工具越好，是該有的有、不該有的不要佔位置。

## 下一步

我目前還缺一塊是「長期記憶整合」——Obsidian、auto memory、CLAUDE.md、rules 這四個知識源頭現在是平行的，沒有統一的 indexing。

理想狀態是有一個 meta-skill 能跨這四個源頭檢索。這大概會是下個月的專案。
