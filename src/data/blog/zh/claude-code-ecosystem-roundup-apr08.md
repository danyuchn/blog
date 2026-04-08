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
description: 企業辦公工具、台灣本地服務、興趣領域、初學者入門——這四個角落本週都冒出了新的 Claude Code 資源。每一個都代表一類還沒被充分開發的使用場景。
---

本週我的 bookmarks 加了 4 個 Claude Code 相關資源。逐一看沒什麼，但放在一起你會發現一件事：**Claude Code 的生態系不是只有「寫程式」這一個軸**。它正在慢慢把企業辦公、本地服務、個人興趣、初學者入門各個角落都填起來。

這四個資源對我來說都有落地價值，順手整理一下分享給同樣在找應用場景的人。

## 1. Microsoft 365 CLI — 企業白領自動化的入口

企業課程學員最常問的一句話是：「我的工作系統有辦法接 Claude Code 嗎？」通常他們指的就是 Teams、Outlook、SharePoint、OneDrive 這一整組 Microsoft 365。

答案是有。而且有兩個工具：

- **`m365`**（PnP Community）：高階指令，懂業務情境。裝好就能 `m365 teams channel message list` 抓 Teams 頻道訊息，不用去查 Graph API。
- **`mgc`**（Microsoft 官方）：直接對應 Graph API 端點，100% 覆蓋但要查 API 文件。

給 Claude Code 裝的話，`m365` 是首選——NPM 一行 `npm install -g @pnp/cli-microsoft365` 就搞定，個人帳號直接登入，企業帳號看 IT 政策決定要不要給 Admin Consent。

實際可以玩的範例：抓 Teams 會議記錄 → Claude 整理摘要 → 自動貼回頻道；批次管理 SharePoint 文件庫權限；新人入職/離職的帳號自動化。這類「我每天在做但覺得不值得自己寫程式」的瑣事，cost 一瞬間就降到零。

GitHub：<https://github.com/pnp/cli-microsoft365>

## 2. job104-cli — 台灣人力平台的 POC

[@miblue119](https://www.threads.com/@miblue119/post/DWwL7YZGmK1) 做了一個 104 人力銀行的非官方 CLI / Skills POC，讓 AI agent 可以直接搜職缺、查履歷。純實驗性質、非營利，明確禁止 104 以外的廠商/個人拿去營利用。

為什麼值得看？因為這是台灣本地服務第一個有人願意做的 Claude Code 整合。官方沒做、也不知道什麼時候會做，但有個人直接上 POC 示範可行。

這個專案的架構（CLI + Skills 雙層）其實跟 AgentCrew 的教學框架一致——先有一個 CLI 處理實際 API call，上面包一層 Skill 給 Claude 讀。對於想把自己公司內部工具 Claude Code 化的人來說，這個 repo 是一個很好的 reference。

- 官網：<https://job104-cli.dev/>
- CLI：<https://github.com/MIBlue119/job104_cli>
- Skills：<https://github.com/MIBlue119/job104-cli-skills>
- 安裝：`brew install MIBlue119/tap/job104-cli` 或 `uv tool install job104-cli`

我希望接下來有人幫 1111、CakeResume、MetaHR 也做類似的 POC。台灣有太多好用的本地服務還停在 web UI 上。

## 3. 運動彩券 Skills — 興趣領域也能套邏輯

這類 skill 我會收藏是因為有朋友問到「Claude 能不能幫忙玩運彩」。查下去發現 mcpmarket 上已經有兩個現成的：

- **Market Mechanics & Betting**：做資金管理。Kelly Criterion 算最佳下注佔本金比例、Brier score 追蹤預測準確度、找出莊家賠率 vs 真實勝率的落差（value bet）。這是防止賭博變娛樂的一層門檻。
- **sports-betting-analyzer**：做情報分析。讓分盤、大小分、prop bets 的歷史對戰、近況、傷兵整合。

兩個都是針對美國運動盤（NBA/NFL），台灣運彩要自己餵賠率資料。而且裝之前記得 `/security-scan` 跑一下——mcpmarket 的 skill 品質差異很大。

對我有啟發的是：**任何領域只要你有穩定輸入（資料）+ 穩定邏輯（計算規則），就能做成 skill**。運彩是一個極端例子，但同樣的框架可以套到任何「資料 + 判斷」的工作——股市、基金、房地產分析都是。

## 4. Claude Code 安裝指南資源

第四個 bookmark 比較特別，是我為 AgentCrew Academy 網站安裝指南更新收集的資料，也一併分享。

Windows 學員最大的痛點不是 Claude Code 本身，是 **Git 沒裝 + `.local\bin` 不在 PATH**。我本來以為這只是少數狀況，結果教學發現這是通例——每班至少一半的 Windows 人卡在這裡。

最乾淨的 Windows 一行解法：

```powershell
winget install Git.Git --accept-package-agreements --accept-source-agreements --silent; irm https://claude.ai/install.ps1 | iex
```

`winget` 是 Windows 10/11 內建的，不用另外裝。這條指令會全自動裝 Git、裝 Claude Code、處理 PATH。學員唯一需要確認的是 UAC 視窗。裝完後要關掉 PowerShell 重開，Git 才會進 PATH。

Mac 就簡單很多：

```bash
brew install --cask claude-code
```

或者官方的 `curl -fsSL https://claude.ai/install.sh | bash`。

相關延伸閱讀：

- [Claude Code Quickstart（官方）](https://code.claude.com/docs/en/quickstart)
- [SmartScope — Windows Native Installation Guide](https://smartscope.blog/en/generative-ai/claude/claude-code-windows-native-installation/)

## 一個觀察

這四個資源擺在一起看，主線是：**Claude Code 的邊界從來不是「寫程式」，而是「任何有 CLI 或 API 的東西」**。

企業系統有 API（Microsoft Graph），就有 m365。台灣本地服務有非官方 CLI（job104-cli），就有人直接包成 skill。運彩有資料有公式，就有 Kelly Criterion 跟 Brier score。連安裝這件事本身，都變成「一條指令的工作流」。

你會不會用 Claude Code 完全取決於你有沒有把「這個東西有 CLI 嗎？」變成反射問題。如果有，就能接；如果沒有，就等別人做 POC 或自己做一個。

下週我大概會收更多。這類週盤點之後可能會變成例行——把碎片資源在被我忘記之前先整理出來，順便當作我的「有人在做什麼」雷達。
