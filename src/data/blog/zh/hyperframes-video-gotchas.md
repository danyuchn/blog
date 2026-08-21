---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-20T04:00:00Z
title: HyperFrames 影片產出的十一個坑
slug: zh/hyperframes-video-gotchas
featured: false
draft: false
tags:
  - video-production
  - gotchas
  - automation
description: '轉場閃動、worker 並行迷思、字幕格式漂移、投影片版式、縮圖靜默截斷——八月這一週在 HyperFrames 這條影片線上踩到的十一個坑，逐個記現象、根因、解法。'
---

四月那篇《[自動化影片製作管道：2026 年四月踩過的九個坑](/blog/posts/zh/video-production-gotchas-2026)》記的是 Remotion 那套；[後來整條流水線換成 HyperFrames](/blog/posts/zh/ai-video-pipeline-codex-to-claude)，坑也整批換新。以下是八月這一週做一支混合片（動畫覆蓋加錄屏 pass-through）時踩到的，一個坑一節。

## 1. 轉場閃動＝切換點沒被遮罩蓋住

wipe 排在 `B-0.6～B`，紅幕在切換前 0.3 秒就滑走了，那一刀其實是裸切，畫面就閃一下。修法是把切點移進全遮窗：`B-0.35` 進場、`B±0.05` 停留、`B+0.35` 離場，停留 0.10 秒才能保證 30fps 下至少三幀全滿。更早那支片沿用的是同一套錯誤時序。

## 2.「純動畫必須單 worker」是 Remotion 的規則，不是 HyperFrames 的

在 Remotion 上訂的這條規則照套過來，render 慢五到八倍。實測 8 worker 下靜止動畫的相鄰幀比對差異像素是 0，並拿轉場的動態幀做反向對照，確認檢查器會動。5.9 萬幀約 22 分鐘跑完。

## 3. `.term` / `.codefile` 會靜默切掉最後一行

這兩個都是 flex child，會被 `scene-content` 壓縮，加上 `overflow: hidden` 就把最後一行吃掉，畫面上看起來只像「貼底」。修法是 `flex-shrink: 0`，加上之後真正過滿的那幾幕才會浮現。`hyperframes check` 只抽 9 幀不保證抓得到，要用 `hyperframes snapshot --zoom "<selector>"` 對元素本身放大驗。

## 4. preview 跑著的時候不要用 Edit 大改

`hyperframes preview` 跑著時會持續往 `index.html` 注入 `data-hf-id`，Edit 的 old_string 就對不上了。大改前先 `hyperframes preview --stop`。

## 5. 監看 render 的失敗過濾器不能只 grep `error`

HyperFrames 有一行 log 長這樣：`static-frame dedup: disabled (... this is the safe fallback, not an error)`，只 grep `error` 會把它誤報成失敗。過濾要排除含 `not an error` 的行。

## 6. 分段轉錄的輸出格式會在段與段之間漂移

13 段裡有 5 段是 `**[MM:SS] Name**：`、其餘是 `[MM:SS] **Name**：`。只認一種形狀的 regex 讓那 5 段靜默回 0 行，合併結果看起來完整，實際少 40%。要用寬鬆的 regex（容許前導 `**`），並逐段印行數核對——回 0 行是格式沒對上，不是那段沒東西。

## 7. 大檔下載 exit 0 不代表檔案是完整的

一支 938MB 的錄影抓到 971MB 時 read timeout，指令仍 exit 0，症狀要到 `ffprobe` 才現形（`moov atom not found`）。驗收條件是 ffprobe 讀得出 duration，不是 exit code 也不是檔案存在；重試迴圈要把 ffprobe 當成功判準。

## 8. 官方 slideshow 框架的 present 目前不能用

它的 `present` 是官方自己標註的 temporary workaround，要求 composition 暴露單一 `window.__timelines.root`。實測 25 幕 slide 全部解析失敗、player 卡在 loading。改成只借它的視覺語言與逐段揭示節奏，控制器自己寫 60 行，零框架相依。

## 9. 投影片版式要用實際放映尺寸驗，不是瀏覽器當下視窗

agent-browser 預設視窗高 577px，量出 10 頁溢出；改用 `style.height="720px"` 模擬 16:9 後剩 6 頁，字級下修再測才歸零。用預設視窗判斷會做出過度縮小的版面。`slides-tokens.css` 的字級是為 1080p 設計的，1280×720 放映要按比例覆寫。

## 10. Studio 顯示「Uploading 0%」不代表上傳卡住

判準是看 API 的 `uploadStatus` 與 `fileDetails.fileSize` 是否等於本地位元組數，不看 UI。這次 499MB 走 resumable 一次就成功，也推翻了舊紀錄裡「257MB 會失敗」的門檻——那是舊 chunked 路徑的限制。

## 11. 縮圖標題被靜默截斷

`compactTitle()` 自動砍標點、只留前 22 字、再從中點硬拆兩行，結果是「你必須知」「最常見的 5」「設定安」這種半截句掛在 YouTube 上好幾個月，36 支，沒人發現。改成手寫短標（缺條目就讓 build 直接失敗）、字級擬合改用各版型的真實容器寬、副標加 `word-break: keep-all`，並新增 `npm run lint:thumbnails` 當固定關卡。判準：任何會丟棄使用者內容的自動化，一律改成「放不下就縮小或報錯」，不准靜默丟字。

這週就這些。

<!--
AI 新增的非原文句子（自首清單）：
1.「以下是八月這一週做一支混合片（動畫覆蓋加錄屏 pass-through）時踩到的，一個坑一節。」— 框架句（素材出處：08-18 日誌 Ep35 條目「六段全屏動畫覆蓋（27 幕）＋其餘錄屏 pass-through」）
2.「四月那篇……記的是 Remotion 那套；後來整條流水線換成 HyperFrames，坑也整批換新。」— 銜接句（回指既有兩篇文章，日誌無此句）
3.「畫面就閃一下。」— 銜接（把日誌標題「轉場閃動」還原成現象描述）
4.「並拿轉場的動態幀做反向對照，確認檢查器會動。」— 改寫（日誌原文：「並用轉場動態幀做反向對照證明檢查器會動」）
5.「這兩個都是 flex child」— 改寫（日誌原文為「`.term`／`.codefile` 是 flex child」）
6.「這週就這些。」— 框架句（收束，日誌無）
其餘各節的現象、根因、數據、判準均逐項對應 2026-08-18 與 2026-08-20 每日筆記的踩坑條目，未新增日誌沒有的根因或解法。
日誌中出現的客戶／人名一律未寫入本文。
-->
