---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-08T16:30:00Z
title: "本週 Claude Code 生態觀察：四個我收藏的新資源"
slug: zh/claude-code-ecosystem-roundup-apr08
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - ai-trends
description: '企業辦公工具、台灣本地服務、興趣領域、初學者入門——這四個角落本週都冒出了新的 Claude Code 資源。每一個都代表一類還沒被充分開發的使用場景。'
---

本週我的書籤收藏了四個看似各自獨立的新資源。逐一看或許只是個別工具，但把它們擺在一起，你會發現一件事：**Claude Code 的生態系不是只有「寫程式」這一個軸**。它正在慢慢把企業辦公、本地服務、個人興趣、初學者入門這四個角落逐一填補起來。

這四個資源都有明確的落地價值，整理分享給同樣在探索實際應用場景的人。

## Microsoft 365 CLI：企業白領自動化的入口

企業課程學員最常問的一句話是：「我的工作系統有辦法接 Claude Code 嗎？」大家日常通常指的就是 Teams、Outlook、SharePoint、OneDrive 這一整組微軟生態系。

答案是有，而且社群與官方各自提供了工具：

- **`m365`**（PnP Community）：封裝了業務情境的高階指令。安裝好後，直接下指令 `m365 teams channel message list` 就能抓取 Teams 頻道訊息，不需要手動查閱 Microsoft Graph API 的端點細節。
- **`mgc`**（Microsoft 官方）：直接一對一對應 Graph API 端點，雖然具備百分之百的覆蓋率，但得頻繁翻閱 API 文件。

如果要搭配 Claude Code 使用，`m365` 是首選。在終端機執行 `npm install -g @pnp/cli-microsoft365` 就能安裝完成。個人帳號可以直接登入使用；企業帳號則需依公司的 IT 資安政策，確認是否開放管理者同意（Admin Consent）。

實際可行的應用場景非常接地氣：抓取 Teams 會議記錄交給 Claude 提煉重點並自動貼回頻道；批次管理與調整 SharePoint 文件庫的權限；或是處理新人入職與離職的帳號自動化流程。這類「我每天在做但覺得不值得自己寫程式」的瑣事，cost 一瞬間就降到零。

GitHub：<https://github.com/pnp/cli-microsoft365>

## job104-cli：台灣在地服務的非官方 POC

[@miblue119](https://www.threads.com/@miblue119/post/DWwL7YZGmK1) 開發了一套 104 人力銀行的非官方 CLI 與 Skills 概念驗證（POC），讓 AI agent 可以直接搜尋職缺並調閱履歷。這項專案屬於個人實驗性質與非營利，並明確禁止 104 以外的廠商或個人拿去進行商業營利。

這件事值得關注的關鍵在於：這是台灣本地服務中，第一個有人願意替 Claude Code 生態系鋪路的概念驗證。官方尚未著手、也還不知道何時才會提供支援，但已有社群創作者直接端出 POC 示範可行性。

這個專案的架構（CLI + Skills 雙層）其實跟 AgentCrew 的教學框架一致：底層由 CLI 負責處理實際的網路請求與 API 呼叫，上層則包裝一層 Skill 提供給 Claude 理解與調用。對於想把自己公司內部現有系統或工具轉化為 Claude Code 接口的人來說，這個專案是非常好的架構參考範例。

- 官網：<https://job104-cli.dev/>
- CLI：<https://github.com/MIBlue119/job104_cli>
- Skills：<https://github.com/MIBlue119/job104-cli-skills>
- 安裝方式：`brew install MIBlue119/tap/job104-cli` 或 `uv tool install job104-cli`

台灣有許多實用且成熟的本地服務，至今依然停留在純網頁介面。期待未來能看見 1111、CakeResume、MetaHR 也出現類似的社群 POC，把更多本地資料接口釋放給終端 AI。

## 運動彩券 Skills：興趣領域也能套用資料與邏輯

這類技能會進入收藏清單，是因為有朋友問起「Claude 能不能幫忙玩運彩」。深入查詢後發現，mcpmarket 上已經有兩款現成工具：

- **Market Mechanics & Betting**：負責資金控管。利用凱利準則（Kelly Criterion）計算最佳下注佔本金比例，搭配布萊爾分數（Brier score）追蹤預測準確度，藉此找出莊家賠率與真實勝率之間的落差（value bet）。這是防止賭博變娛樂的一層門檻。
- **sports-betting-analyzer**：負責情報分析。針對讓分盤、大小分、球員特殊下注（prop bets），整合兩隊的歷史對戰數據、近期戰績與傷兵名單。

需要留意的是，這兩款工具目前都是針對美式運動盤（NBA 與 NFL）設計；如果想用在台灣運彩，必須自行提供與輸入賠率資料。此外，安裝之前記得先跑一下 `/security-scan`——mcpmarket 上的技能品質差異很大。

這項案例的核心啟發在於：**任何領域只要具備穩定輸入（資料）加上穩定邏輯（計算規則），就能打包成技能**。運彩看似是個偏鋒的興趣場景，但背後「數據輸入＋邏輯決策」的底層架構，完全可以套用到任何仰賴資料與判斷的工作，例如股市、基金或房地產分析。

## 避開環境設定痛點的一行安裝法

第四個資源是我在為教學網站整理安裝指南時收集的解法。

在教學現場觀察，初學者與 Windows 學員最大的痛點往往不是 Claude Code 本身的操作，而是最基礎的環境問題：**電腦裡沒裝 Git，而且 `.local\bin` 沒有被加入系統的 PATH 環境變數**。這不是少數個案，每班至少一半的 Windows 學員卡在這裡。

最乾淨、能避開手動除錯的 Windows 一行解法，是在 PowerShell 直接執行：

```powershell
winget install Git.Git --accept-package-agreements --accept-source-agreements --silent; irm https://claude.ai/install.ps1 | iex
```

`winget` 是 Windows 10 與 11 內建的套件管理工具，不用另外安裝。這條指令會全自動完成 Git 安裝、下載並安裝 Claude Code，並處理好 PATH。執行過程中唯一需要確認的只有系統彈出的使用者帳戶控制（UAC）視窗。安裝完畢後，請記得將 PowerShell 關掉重開，Git 才會正式載入環境變數中。

這裡補充一個環境細節：目前原生 Windows 環境在未安裝 Git for Windows 的情況下，Claude Code 會自動改用 PowerShell 運作；但是如果你後續需要執行 Bash 腳本或搭配終端監控（Monitor）工具，依然少不了 Git Bash 的支援。因此直接使用上面這條包含 Git 的一行指令，依然是相容性最佳、最省心的配置方式。

至於 Mac 系統，安裝相對單純許多，可透過 Homebrew 安裝：

```bash
brew install --cask claude-code
```

或者使用官方提供的腳本：`curl -fsSL https://claude.ai/install.sh | bash`。

延伸閱讀與官方參考資源：

- [Claude Code Quickstart（官方）](https://code.claude.com/docs/en/quickstart)
- [SmartScope — Windows Native Installation Guide](https://smartscope.blog/en/generative-ai/claude/claude-code-windows-native-installation/)

## 一個核心反射：邊界在於有沒有 CLI

把這四個資源放在一起看，貫穿其中的主線非常明確：**Claude Code 的邊界從來不是「寫程式」，而是「任何有 CLI 或 API 的東西」**。

企業系統有 API（Microsoft Graph），就有 `m365` 可以接手行政流程；台灣本地服務有非官方 CLI（`job104-cli`），社群就能直接包裝成技能；運動彩券只要有資料與計算公式，就能轉化為資金控管與情資分析模型；甚至連初學者的環境佈署，都能收斂成一條自動化腳本。

這意味著，決定能否將 Claude Code 派上用場的關鍵，在於是否建立了這項反射問題：**「這個工具或系統，有沒有 CLI 或 API？」**

只要有，就能直接串接；如果還沒有，可以等待社群提供概念驗證，或是嘗試自己動手做一個。持續把這些碎片資源在遺忘前整理出來，順便當作我的「有人在做什麼」雷達。

<!-- 2026-11-12 舊文盤點整篇重寫：將文末後記對 Windows 環境與 Git Bash 的補充完整整合進安裝章節，消除雙重收尾；調整小標結構並提煉核心判準，使陌生讀者能自然掌握 Claude Code 連接 CLI 與 API 的應用邏輯。 -->
