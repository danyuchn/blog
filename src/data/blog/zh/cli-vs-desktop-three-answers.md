---
author: Dustin Yuchen Teng
pubDatetime: 2026-03-24T04:00:00Z
modDatetime: 2026-08-28T04:00:00Z
title: "一年下來，我對「該用終端機還是桌面版」的答案變了三次"
slug: zh/cli-vs-desktop-three-answers
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - developer-experience
description: '從三月的 Cowork 燒 token、四月的「答案還是終端機」、五月的「初學者直接從桌面版開始就好」，到八月的「CLI 是親生的」。同一個問題，我在五篇文章裡給過三種不同的答案，這裡照時間順序排出來。'
---

這個問題我被問過很多次：Claude Code 到底該用終端機還是桌面版？過去一年我寫過五次，答案變了三次——三月和四月是「終端機，沒得商量」，五月變成「初學者直接從桌面版開始就好」，八月又變回「CLI 是親生的，其他都是後媽養的」。以下照時間順序排，每一節標明時間點。前後打架的地方我不打算圓，那就是我當時的答案。

## 2026 年 3 月：先從 Cowork 為什麼幾小時就頂到限額講起

有 Max 方案的人常問這個問題：用 Claude Code 在終端機跑整天開發，用量從不超過一半；但切換到 Cowork 做幾小時的小專案，就頂到限額。

同樣是 Max，同樣是 Claude，怎麼差這麼多？

### 結論先說

Cowork 消耗 token 的速度遠高於 Claude Code CLI。一個 Cowork session 做複雜的檔案操作，消耗的 quota 相當於幾十條普通聊天訊息。Max 5x 的「225+ 條訊息」換算成 Cowork，大概只能做 10 到 20 個實質操作。

原因有三層，分別來自 Cowork 的架構設計。

### 第一層：Cowork 的隱藏 token 開銷

Cowork 跑在 sandboxed VM 裡。每次操作背後看不見的東西：

- **截圖 + 圖片處理**：Vision token 非常貴，遠比純文字貴
- **多次 AI 推理呼叫**：一個「任務」可能觸發 5 到 10 次 API call
- **整檔讀入 context**：不像 CLI 可以精準控制只載入需要的部分
- **完整歷史疊加**：每一步都帶著前面所有步驟的歷史，context 只增不減

你以為在做一件事，背後其實跑了十幾個 API 呼叫。

### 第二層：Claude Code CLI 天生省 token

CLI 有幾個 Cowork 沒有的優勢：

**Prompt caching。** System prompt、CLAUDE.md、工具定義這些重複出現的內容會被快取，不重複計費。每次新的 session，這些不用重新算錢。

**精準 context control。** 你可以控制只讀哪些檔案、只載入哪些 skill。好的 CLAUDE.md 架構用 on-demand loading，比一次全塞進去省很多。

**沒有視覺處理。** 純文字互動，不需要截圖或圖片辨識，直接省掉 vision token 這整塊開銷。

### 第三層：速度問題造成惡性循環

Cowork 極慢。Claude Code 5 分鐘能完成的任務，Cowork 可能要跑 40 分鐘。

慢不只是慢而已——慢等於更多 context 累積，等於更多 token 消耗。任務拖越長，每一步帶的歷史越多，計費越高。這是惡性循環。

### 社群怎麼說

這不是個人感受，有 GitHub issues 記錄：

- [#16856](https://github.com/anthropics/claude-code/issues/16856)：用戶回報 token 消耗速度比以前快 4 倍以上
- [#23318](https://github.com/anthropics/claude-code/issues/23318)：多人確認用量異常，懷疑計算方式改變
- [#33120](https://github.com/anthropics/claude-code/issues/33120)：Cowork 專屬的 rate limit 問題

Zvi Mowshowitz 寫過一篇專文比較兩者差異，結論跟這裡一致：差距主要來自 context control。Threads 上也有開發者說「Burns limits way faster than Claude Code」、「5min task in CC → 40min in Cowork」。

### 額外觀察：為什麼 Opus 在 CLI 裡「感覺更聰明」

這是我自己的體感，但有合理解釋。

CLI 的 context 更乾淨、更聚焦，模型能把算力花在真正的問題上，而不是處理 sandbox 環境的雜訊。同樣的模型，input 品質不同，output 自然不一樣。

另外，Cowork 的沙盒體驗，個人覺得還是不夠成熟。隔壁棚的 ChatGPT Work 就好很多。

### 什麼時候用哪個

**Claude Code CLI 適合：** 開發工作、長時間 session、需要精準控制的任務。Token 效率最高，適合每天大量使用。

**Cowork 適合：** 需要圖形操作、瀏覽器互動、或者不熟悉終端機的情境。代價是 quota 消耗快很多。

有 Max 方案的人，如果主要工作是寫程式，大部分時間都不需要碰 Cowork。

## 2026 年 4 月：桌面版改版了，答案還是終端機

Anthropic 這週更新了 Claude 的桌面應用程式，設計改版了，更漂亮，介面也更友善。終端機本來就會嚇跑不少人，有個漂亮的 GUI 入口確實降低了門檻。

![Redesigning Claude Code on desktop for parallel agents](/blog/images/claude-desktop-redesign.jpg)

但如果你問我日常用哪個，答案還是終端機。

### 更新節奏的差距

Claude Code CLI 現在幾乎每天有 1 到 2 個版本更新。桌面版 App 的更新週期大概是 2 到 4 週。

這個差距不只是版本號的問題。幾乎所有的新功能、性能修復、行為改善，都會先在 CLI 上線，桌面版往往要等好幾個禮拜才跟上。

上週的 2.1.100，修掉了大型檔案 JSON 跳脫導致 token 虛耗的問題，還修掉了長 session 記憶體暴增的 bug。這兩個問題我在 CLI 這邊當天就拿到修復，桌面版用戶還得再等一段時間。

如果你認真用 Claude Code 做工作，這個落差是切實的代價。

### 資源效率的差距

我的主力機是 M2 MacBook Air。開著 Claude Desktop App 做其他事會明顯感到卡頓，整台機器的反應明顯遲鈍。

終端機的 Claude Code CLI 幾乎沒有這個問題。我現在平常開著 3 個 Ghostty 視窗，每個視窗裡有 3 到 4 個 pane，跑 5 到 6 個 Claude session 同時工作，系統沒什麼負擔。

純 terminal 應用本來就住在電腦底層，對 GUI 那層的開銷是零。

### 一個很多人不知道的問題

桌面版 App 跟 CLI 讀的是**完全不同的設定檔**，而且兩邊不互相繼承。

| 環境 | 設定檔位置 |
|------|-----------|
| Claude Code CLI | `~/.claude.json` |
| Claude Desktop App | `~/Library/Application Support/Claude/claude_desktop_config.json` |

這代表你在 CLI 裝的 MCP server、設定的環境變數、配置的 PATH，桌面版 App 一概不知道。

桌面版 App 有一個額外的限制：它不繼承 shell 的 PATH 環境變數。所以如果你在設定檔裡填 `uvx` 這種命令，桌面版找不到，要填完整路徑（例如 `/Users/danyuchn/.local/bin/uvx`）。

每次裝新 MCP 都要記得兩邊都設定一遍。這件事本身沒有什麼大不了，但如果你不知道這個差異，在桌面版裡找不到某個 MCP，很可能會繞很久才發現根本原因只是設定檔不同。

### 建議

Desktop App 對入門者來說是一個很好的起點。它降低了「我還沒習慣終端機」這個心理門檻，設計確實也比黑底白字的終端機友善多了。

但如果你已經用 Claude Code 做正式工作，長期來說搬到 CLI 是對的。更新節奏快、資源效率好、設定靈活度高——這些加起來每天都有感。

## 同一天稍晚：為什麼終端機裡的 Claude 才是完全體

我對 Claude Code 的純 CLI 命令行介面有一種莫名的好感。後來想通了——我是 PTT 世代的老人，黑底白字的介面有一種奇特的熟悉感。

但好感只是個人喜好，選 CLI 的真正理由比情懷硬很多。

### 速度和資源效率

終端機的執行速度跟 GUI 工具完全不在同一個量級。這不是感覺，是可以測量的現實：純 terminal 應用對系統資源的負載接近零，VSCode 這類的 IDE 吃的資源是它的好幾倍。

### IDE 只是把 Claude 的手腳綁起來

任何 IDE 都加了一層包裝。這層包裝有它的價值——語法高亮、檔案樹、debug 面板——但它同時也限制了 Claude 能做的事。

在 CLI 裡，Claude 直接對話的是作業系統本身。沒有 IDE 的 wrapper，沒有 GUI 的 overhead，沒有介面邏輯決定哪些工具能用、哪些功能被隱藏。

這就是為什麼我說 CLI 裡的 Claude 才是「完全體」——不是誇張，是字面意思。

### 多視窗工作流

等待 AI 回應的時間是可以利用的。我的工作習慣是：

- session A 跑長任務（抓資料、build、大批量操作）
- session B 處理中期任務（改程式、寫文章、整理資料）
- session C 快速來回問答（查資料、確認細節）

三條線同時跑，不存在「等待」這件事。一個 session 在處理的時候，另外兩個不是在工作就是在等我給新指令。

這個工作模式在 GUI 環境裡很難做到，因為多視窗的管理成本高。在終端機裡，一個 `tmux` 或 Ghostty 的多分頁就搞定。

### Ghostty：Anthropic 團隊的推薦

Boris（Claude Code 的主要維護者）說過：「雖然我自己在用 iTerm2，但整個 Anthropic 團隊推薦 Ghostty。」

我從 iTerm2 跳過來之後完全不後悔。Ghostty 的特點：

- GPU 渲染，捲動和響應速度跟 iTerm2 不是一個等級
- 字體設定特別靈活，中英文字體可以分開指定，各自優化
- 設定檔乾淨，純文字，版本控管友善

![Ghostty 終端機截圖](/blog/images/micro-notes/ghostty.jpg)

**字體是很值得花時間設定的一件事。** 在終端機裡一天看幾個小時的文字，字體舒不舒服對工作狀態有真實影響。可以跟 Claude Code 說你想改 Ghostty 的字體，請它推薦適合的中英文字體組合，改完再說不舒服再換，反正它幫你改。

### 語音輸入也能跑得動

補充一個跟 CLI 組合的工作流：語音輸入。

在終端機裡打字錯了不需要回頭修，Claude 大部分情況下都能看懂語境。我開始頻繁用語音輸入之後，發現就算格式慘不忍睹、成篇錯字、嗯嗯啊啊口頭禪，Claude 都看得懂。

用語音指令給任務、用文字確認結果——這個組合在終端機環境裡比 GUI 更流暢，因為焦點完全在 Claude 的輸出上，不需要分心去點選介面元素。

## 2026 年 5 月：答案變了，初學者直接從桌面版開始就好

我自己一直都用終端機。系統資源佔用少、更新快、功能完整，這三件事在過去一年的多數時間都是終端機的優勢。

但是現在的桌面版我也覺得不錯了。

大概兩到三個禮拜前，Anthropic 把桌面 App 大翻新。現在 90% 以上的功能都跟終端機同步，剩下的 10% 是進階開發者才會用到的功能（譬如 hook、subagent 的某些行為、進階 MCP 設定）。桌面版的更新速度也跟著拉起來，跟以前那種一兩週才更新一次的節奏完全不一樣了。

最新的功能還是會在終端機先出來。但老實說，**最新的功能爛尾機率很大**。Anthropic 永遠都是退出新功能比後續維護來得快。一般使用者沒有必要去追那些還在 research preview 階段、會被各種 bug 困擾的東西。等那些功能需求穩定後再搬到 App，反而是更舒服的選擇。

所以如果你是初學者，對終端機有恐懼，從桌面版開始**完全沒問題的**。等你慢慢摸熟流程、知道自己會需要哪些進階功能、覺得 GUI 限制住你了，再切換到終端機也來得及。順序顛倒過來的學習成本反而比較高。

至於我為什麼還是繼續用終端機？因為我已經習慣了 hook、各種自訂 skill、跟 git/ffmpeg/yt-dlp 的混合工作流。這些都是 CLI 比較順手的場景。如果你的場景是「主要在跟 Claude Code 對話、寫文件、整理資料」，桌面版完全夠用。

換句話說：工具的選擇沒有對錯，只有適不適合你當下的需求。先用桌面版上手，過半年後如果你發現自己想要做更多自動化、想接 hook、想串本地腳本，那時候再花一個下午學終端機就好。沒必要在第一天就被一堆 flag 跟設定檔擋住。

## 2026 年 8 月：CLI 是親生的，其他都是後媽養的

因為新的功能或者剛修的 bug 都會優先在 CLI，所以 CLI 是原生第一環境。remote control 要更新要等猴年馬月。

呃，我舉個例子。早期的 remote control 環境中，打斜線不會有提示 SKILL 選單，所以除非記得 SKILL 全名，不然叫不出來。這還是 remote control 推出三個月後才修復的。

他們全都是 Anthropic 原生，但親生的孩子也是有偏心。CLI 一天一更最頻繁（因為員工自己就在用），Desktop 以前很慢、後來大改版更新變勤了，其他的就都慢吞吞。看 CHANGELOG 打 remote control，你就可以看到跟他相關的修復頻率了。

那如果平常在家電腦都用慣 CLI 的情況下，直接讓 CLI 鏡像到移動設備不是最方便的嗎？

![手機上透過 mosh 連回 Mac mini 跑 CLI，畫面是 agent 正在把一批 gog CLI 的工具陷阱寫進文件的 diff](/blog/assets/posts/cli-vs-desktop-three-answers/1-remote-control.jpg)

為什麼不用官方 Claude / Codex 的雲端控制手機 App？

因為他們不知道何時才會出 split pane⋯

![手機畫面上下同時開著兩個 pane，各自是一個獨立的 CLI session](/blog/assets/posts/cli-vs-desktop-three-answers/2-no-split-pane.jpg)

還有一個非常奇怪的事情：以前一天一更的 Claude Code CLI，竟然已經 8 天沒有更新了。經過機器人強力去重後的 Issues 仍然穩定在五千上下，所以不代表沒 bug 可修。

![anthropics/claude-code repo 的 GitHub 頁面，Issues 顯示 5k+，最新 commit 標著 v2.1.220、committed last week](/blog/assets/posts/cli-vs-desktop-three-answers/3-cli-no-update.jpg)

是不是在蹲一波什麼大的，還是內部發生了什麼劇烈的調整，目前未知。

跟他們之前大力宣傳的 AI 自我修復工作流，差別很大吧。只能說這家公司，說的跟做的要分兩套來看。

## 四月那段哲學收尾，現在讀起來

四月那篇的最後，我寫的是一段比較哲學的東西：選擇 CLI 不只是技術偏好，也是一種對 AI 工作方式的態度宣示。你決定要認真用這個工具，而不是讓它待在一個方便但受限的沙盒裡。你要的是完整的能力，哪怕入門成本稍高一點。這個選擇，長期下來有複利。

那是四月寫的。五月我叫初學者從桌面版開始，八月我在抱怨 CLI 以外都是後媽養的。三個答案就擺在這裡。

<!--
新增非原文句子清單（忠實度自首）：
1.「這個問題我被問過很多次：Claude Code 到底該用終端機還是桌面版？過去一年我寫過五次，答案變了三次——三月和四月是「終端機，沒得商量」，五月變成「初學者直接從桌面版開始就好」，八月又變回「CLI 是親生的，其他都是後媽養的」。以下照時間順序排，每一節標明時間點。前後打架的地方我不打算圓，那就是我當時的答案。」— 框架句（合併文開頭；三個答案的措辭皆取自下文既有原文）
2. 六個 H2 段標題「2026 年 3 月：先從 Cowork 為什麼幾小時就頂到限額講起」「2026 年 4 月：桌面版改版了，答案還是終端機」「同一天稍晚：為什麼終端機裡的 Claude 才是完全體」「2026 年 5 月：答案變了，初學者直接從桌面版開始就好」「2026 年 8 月：CLI 是親生的，其他都是後媽養的」「四月那段哲學收尾，現在讀起來」— 小標（合併用；語意取自原五篇標題與其首句）
3.「還有一個非常奇怪的事情：」中的「還有」— 銜接（沿用 cli-is-the-firstborn 原文既有的銜接詞）
4.「另外，」（Cowork 沙盒不夠成熟前）— 銜接（沿用 cowork-vs-claude-code 原文既有的碎念併入銜接詞）
5. 末節「四月那篇的最後，我寫的是一段比較哲學的東西：」與「那是四月寫的。五月我叫初學者從桌面版開始，八月我在抱怨 CLI 以外都是後媽養的。三個答案就擺在這裡。」— 改寫（原 cli-terminal-philosophy 的「## 不只是工具，是一種態度」一節是為那篇的結構寫的收尾，此處改寫成合併文的結語：哲學段本身的四句文字逐字保留，僅前加時間標記、後加兩句指回三個答案並列的事實，未替作者調和成統一結論、未替作者解釋立場為何改變）
6. 原五篇的 H2 小節（更新節奏的差距／資源效率的差距／IDE 只是把 Claude 的手腳綁起來 等）降為 H3，標題文字未改 — 改寫（合併後的標題層級調整）
7. cli-is-the-firstborn 三張圖片路徑改為 `/blog/assets/posts/cli-vs-desktop-three-answers/`，alt 文字沿用原文 — 改寫（合併後資產目錄變更）
其餘所有段落、表格、清單、數據、GitHub issue 編號、引用連結與判準均逐字取自五篇原文（cowork-vs-claude-code、claude-desktop-vs-cli、cli-terminal-philosophy、claude-code-desktop-vs-cli-w20、cli-is-the-firstborn），未新增原文沒有的論點或結論，五篇各自的立場原樣並陳、未做調和。
8. cli-terminal-philosophy「## 速度和資源效率」一節的第二段（M2 MacBook Air、3 視窗 3-4 pane、5-6 session、Desktop App 卡頓）未重複搬移 — 改寫（該段與同日稍早 claude-desktop-vs-cli「資源效率的差距」一節為同一組事實的重述，逐字保留在該節內；本節只留其獨有的第一段「VSCode 這類的 IDE 吃的資源是它的好幾倍」，無事實遺失）
-->
