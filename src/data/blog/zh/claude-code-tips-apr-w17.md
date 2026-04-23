---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-22T05:00:00Z
title: "Claude Code 這週整理：分擔 CLAUDE.md 的進階設定、省 quota 技巧、Ghostty 點擊設定"
slug: zh/claude-code-tips-apr-w17
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - ai-workflow
description: 本週 Claude Code 累積的幾個實用設定與省錢技巧——Rules/Memory/Hooks 如何分擔 CLAUDE.md、Ghostty No Flicker 模式下連結點擊的修法、長文本用 Haiku 分派省 quota、4.7 後貼圖片跟改訊息對快取的差別。
---

這週 Claude Code 累積的幾個設定技巧，都不是很新的功能，但都是我自己撞到才知道的。按主題整理下來。

## 不要再把什麼都塞到 CLAUDE.md

大部分人只知道「默契檔」CLAUDE.md，但不知道 Rules、Memory、Hooks 都能分擔它的功能。我也曾經是 CLAUDE.md 寫到一千多行、然後大罵 Claude 怎麼那麼笨會忘東忘西的人。

後來我慢慢學會用幾個進階設定分擔默契檔的工作：

- **Rules**（`~/.claude/rules/`）：跨專案的技術規則、陷阱清單、工具路由表。用 `@path/to/rule.md` 從 CLAUDE.md 引入。
- **Memory**（auto memory）：會話級的用戶偏好、專案狀態、犯錯紀錄。會在新對話自動載入相關條目。
- **Hooks**（`settings.json`）：自動化行為（SessionStart 檢查、PreToolUse 攔截、PostToolUse 提醒）。模型不執行的，harness 會執行。

趁假日拍了一部影片解釋這幾個怎麼分工：<https://www.youtube.com/watch?v=kSFty4XwXS8>

## 解釋模式：給非工程背景的人

學員 onboarding 時常遇到的問題：Claude Code 講太多技術名詞，聽不懂。

解法兩步：

1. `/config` → `explanatory mode`，會開始變成解釋模式。
2. 如果還不夠清楚，在 CLAUDE.md 補一條規則，請他用非技術用語白話文解釋他在幹什麼。

兩條並用就能把 Claude 講的話壓到國中生也聽得懂的程度。

## Ghostty 點擊陷阱：No Flicker 模式下 cmd+click 失效

傳統的 Flicker 模式最近在 Ghostty 中的渲染一直出問題，會把同段歷史對話渲染好幾遍，回去翻的時候一直看到亂成一團的重複資訊。所以我改成 No Flicker 模式（文字列固定，滑鼠接管）。

改完之後原本的問題解決了，下個問題出現：原本 Ghostty 的 `cmd+click` 點擊連結跟路徑開啟檔案的功能，被 Claude Code 接管。有些路徑 Claude Code 認不得、點不開了。

我請 Claude Code 給我各種連結形式逐一測試，結論寫回 CLAUDE.md：

> 檔案位置一律用 `file://` 絕對路徑（如 `file:///Users/danyuchn/path/file.md`），必須加 `file://` 前綴才可點擊。例外：code block 內、指令範例、function 參數維持原格式。

題外話：有人可能會問為何不停用滑鼠接管？我只能說狀況更糟。停用滑鼠接管後，觸控板上滑下滑就完全無法控制歷史訊息了，會被鎖定在輸入框中。

## 省 quota：長文本用 Haiku 分派閱讀

這週學到的技巧：長文本閱讀時，不要讓主 agent 直接讀，因為高階模型碰到長文本 token 暴增。改成：

> 派幾個 Haiku agent 分段閱讀此文檔。你直接把檔案給他們，你自己不要提取文字（省 quota），然後彙整他們讀的摘要。

拆成數段避免注意力稀釋的問題，用 Haiku 也能省 cost。要特別指名「直接給檔案」避免較高階的主 agent 模型碰到長文本耗 token。

## 4.7 之後：貼圖片 vs 改訊息，快取的差別

今天學到的新教訓：Claude Code 官方文檔也會寫得不夠清楚。

**新訊息貼圖片是不會破壞快取的，修改舊訊息才會。**

我親自去撈快取欄位實測證明了這一點。所以如果你要附上參考圖，繼續貼新訊息，不要回去編輯舊的訊息加圖。

順帶一提，有錯就要認錯，不要硬拗。台灣愛硬拗的人太多，硬拗真的很難看，誠實道歉、負責任改進是每個人都要學習的課題。這條對人對模型都適用。

## 實務：bypass + 鉤子

有些人問我 permission mode 要怎麼設才不會一直跳框。實務上我還是 `bypass` + 鉤子比較方便——bypass 解決 false positive 的煩擾，鉤子在真正危險的點（刪檔、推遠端、對外通訊）攔截。

## Remotion 影片製作流程

在 Claude Code 做 Remotion 影片做得越來越上手了，大致上的工作流：

1. 調查主題內容，檢查官方文檔跟網友最佳實踐
2. 設計口白腳本、安插螢幕錄製位置（如有）
3. 錄口白，在剪映自動去贅字
4. 把字幕跟音檔丟回 Claude Code，請他開始設計動畫
5. 同時我去錄螢幕示範
6. 錄完後在剪映做簡單影片後製
7. 做完後動畫也差不多設計完了，影片丟回來請他嵌入
8. 同時檢查動畫是否合規、是否掉拍，有的話指揮修正並且請他截圖自我驗證
9. 完成後輸出影片跟封面
10. 等待的過程中請他修正字幕檔錯字，準備影片標題與描述
11. 做完後影片也輸出好了，直接用 YouTube API 上傳，設定定時發佈

整個流程 90% AI 深度參與，10% 是剪映的需求功能不支援 API/MCP，以及我個人不喜歡 AI 合成語音。

改天來開源這一套工作流的 Skill。範例影片：<https://youtu.be/J1WjxzzSzv8?si=w8jLGhBjh8_0HbYR>

## 還有一個意料外的實例：Xoogler 幫我長流量

前幾天教一個學員用 Claude Code 的時候，意外得知他之前在 Google 工作 8 年，負責 YouTube 相關業務。

我順便說「我們新創的頻道流量都漲不起來怎麼辦」，他也很熱心跟我分享幾個 YouTube 頻道要漲流量的內容心法（這樣是內線嗎？）

課後，我在請 Claude Code 整理課程實錄歸檔的時候，突然讀到有聊過這一段，我就隨口問 Claude Code：你能按他的建議做做看嗎？然後開給他我的頻道的 API 權限。

結果 24 小時之後，流量暴漲，一天訂閱者翻倍。

所以這次換我喊他一聲老師了。Xoogler 真的超級聰明，對話中就能感覺得到，雖然沒有編程背景，但不管是規劃邏輯或者指揮思路都是一點就通，跟 AI 協作進度超級快，一小時就趕超四小時進度。

## Rate limit 的現實

最後一個碎念：你懂那種早上九點的 5 小時用量剩 55%，15 分鐘後 hit limit 需要睡一覺重置的美好嗎？

```
You've hit your rate limit.
- Reset Friday 07:00 AM
```

這就是 Opus 4.7 之後的日常。如果你還沒看過我這週寫的 [Opus 4.7 一週回顧](/posts/zh/opus-47-week-review)，可以配著一起看。

官方 changelog 在這：<https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md>
