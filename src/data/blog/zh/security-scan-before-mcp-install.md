---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-15T10:00:00Z
title: "裝 MCP 之前先讓 Claude 幫你掃——找到 7 個漏洞，但說這個可以裝"
slug: zh/security-scan-before-mcp-install
featured: false
draft: false
tags:
  - mcp
  - security
  - claude-code
description: 講座當週我拍了一支影片，講「裝任何 MCP / npm / pip / clone 之前先跑 /security-scan」這件事。實測了一個三方 MCP，Claude 掃出 7 個漏洞，但綜合評估後說「可以裝」。這篇是影片的補充文字版。
---

本週 AgentCrew Academy 上架了一支影片：「裝 MCP 之前先讓 Claude 幫你掃——它找到了 7 個漏洞，但說這個可以裝」（[B0_lqDs4Sac](https://youtu.be/B0_lqDs4Sac)）。這篇是補充文字版。

## 為什麼這件事重要

MCP server 是 Claude Code 的「外掛市集」。任何人都可以發 MCP server 到 GitHub、npm、PyPI。你裝下去之後，那個 MCP server 在你電腦裡能做的事情，跟你授權給它的權限有關。

但是大多數人安裝 MCP 的流程是：

1. 在 Twitter 或 Reddit 看到別人推薦
2. 複製 `claude mcp add` 指令
3. 貼進終端機按 Enter

這個流程裡完全沒有「先看一下這個 MCP 在做什麼」的步驟。

## `/security-scan` 是什麼

我自己有一個全域 skill 叫 `/security-scan`。當我下這個指令、把目標 repo URL 或 npm 套件名給它，Claude Code 會：

1. **下載原始碼**（git clone 或 npm view tarball）
2. **掃 dependency tree**：列出所有 transitive dependencies，比對已知 CVE
3. **掃 manifest 檔**：`package.json` / `pyproject.toml` / `Cargo.toml` 看 maintainer 是誰、有沒有奇怪的 install script
4. **掃原始碼**：找潛在的 command injection、SSRF、unsafe deserialization、credential exfiltration patterns
5. **掃網路行為**：靜態分析裡有沒有打 `http://` 而不是 `https://`、有沒有寫死的外部 endpoint
6. **產出評估**：CRITICAL / HIGH / MEDIUM / LOW 分級 + 是否建議安裝

整個流程約 3-5 分鐘。

## 實測案例：找到 7 個漏洞但說可以裝

影片裡實測的是一個三方 MCP server。我先不講名字（避免誤導觀眾——這支影片的重點是 SOP，不是評價那個特定 MCP）。

掃出來的 7 個 finding：

1. **MEDIUM**：`requests` 套件版本過舊（有已知 CVE，但不是這個 MCP 直接觸發的路徑）
2. **MEDIUM**：URL 處理沒做 SSRF 防護（但這個 MCP 設計就是要打外部 API，無法完全消除）
3. **LOW**：`subprocess.run(shell=True)` 用法但是 input 來自固定字串，不是 user input
4. **LOW**：log 裡會印出 API key 的前 4 個字元（不會洩漏完整 key，但仍是不必要的揭露）
5. **LOW**：沒有 rate limiting（在 MCP 場景下不嚴重，因為 caller 是你自己）
6. **INFO**：README 沒寫安全考量
7. **INFO**：缺少 SECURITY.md

Claude Code 綜合評估後給的結論是「**可以裝**」。理由：

- **沒有 CRITICAL 或 HIGH**
- MEDIUM 的兩條都是「設計上的取捨」而不是「實作 bug」
- LOW 的三條都是 code hygiene 問題，不影響安全核心
- INFO 的兩條是 documentation 缺失，可以提 PR

如果你看到的是 CRITICAL 或 HIGH，特別是「unsafe deserialization」「shell injection with user input」「hardcoded credentials」這類，**STOP**。不要裝。

## 為什麼讓 AI 自己評估、而不是你自己看

兩個原因：

### 1. 速度

人工讀 7 個 finding 一個一個查 CVE 編號、確認 affected version 是哪些、判斷你的場景會不會觸發——這套流程一個 finding 至少 5-10 分鐘。7 個就是 35-70 分鐘。AI 5 分鐘做完。

### 2. 認知偏差

人類在「看到自己想裝的東西」的時候，會傾向找理由說服自己「這個 finding 應該沒關係吧」。AI 沒有這個偏差。

當然 AI 也有「過度警示」的偏差（看到任何 `subprocess` 就標 HIGH）。所以最後的判斷還是要你看 AI 的 reasoning，自己拍板。但是讓 AI 先做第一輪過濾，比你自己從零開始好得多。

## 跟全域 hook 配合

我把 `/security-scan` 還掛了一個 PreToolUse hook：當 Claude Code 嘗試執行 `claude mcp add`、`npm install`、`pip install`、`git clone` 之類的指令，hook 會跳出來提醒「**裝任何東西之前先跑 /security-scan**」。

這樣即使我自己一時忘記、想直接複製貼上某個推薦指令，hook 也會擋住。

CRITICAL / HIGH findings → STOP，不裝、回報、考慮 alternative。

## 給沒有 `/security-scan` skill 的人

如果你還沒寫這個 skill，最簡單的版本是直接跟 Claude Code 講：

> 請下載 <repo URL> 的原始碼，掃描其依賴、shell 用法、network 行為、credential handling 有沒有安全疑慮。給我 CRITICAL/HIGH/MEDIUM/LOW 分級評估，最後給我「建議安裝 / 不建議 / 條件式安裝」的結論。

這個 prompt 跑下來大概就是 80% 的 `/security-scan` 體驗。等你常常用之後，再考慮把它包成一個 skill。

## 為什麼要寫這篇

MCP server 的數量在過去幾個月暴增。Twinkle Hub、mcp-taiwan-legal-db、各種 Reddit 大神寫的小工具——每天都有人推薦新的可以裝。

如果你照單全收，你的 Claude Code 環境裡的 MCP server 會在三個月內累積到 20-30 個。其中可能有幾個是惡意的（譬如 typosquatting：`mcp-anthrop1c` 假裝是官方的 `mcp-anthropic`）；也有幾個是寫得太爛、會把你的 API key log 到外部服務的。

**裝 MCP 不是免費的**。它的成本是「你電腦的安全表面積」。每多裝一個就多一份信任債。

`/security-scan` 是還這份債的最低成本工具。
