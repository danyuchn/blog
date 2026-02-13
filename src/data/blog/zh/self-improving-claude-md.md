---
author: Dustin Yuchen Teng
pubDatetime: 2026-02-13T12:00:00Z
title: "我掃了 500 個 Claude Code 對話紀錄，然後 AI 就不再犯同樣的錯了"
slug: zh/self-improving-claude-md
featured: true
draft: false
tags:
  - claude-code
  - ai-coding
  - productivity
description: "用 claude-log 工具掃描歷史對話，從你罵 AI 的紀錄中提煉規則寫進 claude.md，讓 Claude Code 真正學會不再踩同一個坑。"
---

## 前情提要

如果你有在用 Claude Code，你一定知道 `CLAUDE.md` 這個東西——就是一份放在專案根目錄的指示檔，告訴 AI「你在這個專案裡該遵守什麼規則」。

問題是：這份檔案通常是你自己手寫的。你覺得 AI 應該注意什麼，就寫什麼。但你不可能記得每一次 AI 犯過的錯，也不可能每次被氣到都冷靜地去更新文件。

結果就是，`CLAUDE.md` 永遠停留在「你以為 AI 需要知道的事」。至於 AI 實際上一直在搞砸什麼？你早就忘了。

## 偶然看到的一篇文章

前幾天我在逛 Hacker News 的時候看到倫敦工程師 Martin Alderson 寫的一篇文章：[Self-improving CLAUDE.md files](https://martinalderson.com/posts/self-improving-claude-md-files/)。

他的想法很簡單：Claude Code 的每一次對話都會存成 JSONL 檔案在你電腦裡（`~/.claude/projects/` 目錄下）。與其靠自己回憶 AI 犯過什麼錯，不如直接讓 AI 去掃這些歷史對話，找出你罵它的地方，然後自動把教訓寫進 `CLAUDE.md`。

他還做了一個叫 [claude-log](https://github.com/martinalderson/claude-log-cli) 的 CLI 工具來幫助解析這些紀錄。用 C# AOT 編譯的原生 binary，3MB，啟動 2 毫秒，裝好直接用。

## 我的實驗

我手上有 6 個專案在用 Claude Code，加起來超過 500 個 session。我想：既然工具都有了，不如一口氣全掃一遍。

### 安裝

```bash
# macOS Apple Silicon
curl -sL https://github.com/martinalderson/claude-log-cli/releases/latest/download/claude-log-osx-arm64 -o /tmp/claude-log
chmod +x /tmp/claude-log
cp /tmp/claude-log /usr/local/bin/claude-log
```

### 核心指令

```bash
# 列出所有專案
claude-log projects list

# 搜尋特定關鍵字（關鍵！）
claude-log sessions search "不對" --path ~/my-project
claude-log sessions search "改回來" --path ~/my-project
claude-log sessions search "不可接受" --path ~/my-project
```

重點就是搜那些**你罵 AI 的關鍵字**。中文的話我搜了：「不對」「不要」「錯了」「改回來」「不可接受」「先不要」「你沒有」「重做」「太複雜」。

英文使用者可能會搜：「wrong」「revert」「undo」「don't」「stop」「that's not what I asked」之類的。

## 挖出來的東西

### GMAT Simulator（198 個 session）

這是我最大的專案，挖出來的東西最多：

搜「改回來」的時候翻到一筆：AI 改 TPA 題型的分屏顯示，根本沒先看練習模式怎麼實作就動手，結果整個改錯，我叫它 revert。這就變成了新規則——修改功能前，先讀既有實作。

搜「不可接受」更精彩。AI 遇到 Firestore 權限問題，不去找根本原因，用 fallback 繞過去。我的原話是「不可接受。這種 fallback 是錯誤的處理方法。我要你回滾並且徹底解決權限問題。」於是加了規則：遇到問題修根因，禁止用 workaround 繞過。

搜「不對」翻到：資料庫有新舊兩種格式並存，AI 居然把新代碼改成去適配舊格式，方向完全反了。我當時說「不對，你應該是修改資料庫來支援新格式」。

還有一個意外收穫：CLAUDE.md 裡寫 Elo 解鎖門檻是 30 次，但程式碼寫的是 20 次。文件跟代碼 drift 了，不掃根本不會發現。

### GMAT Skills（211 個 session）

這個專案最慘，「不要」出現了 **146 次**。

最多的問題是參數和路徑打錯（IP 打錯、模型名稱寫錯、permalink 用 ID 還是 slug 搞混）。另外 AI 常常逐一處理個案而不去找通用規則，我多次說「不要個別處理，辨認樣式並設計規則」。

### Video Translate（46 個 session）

最大的發現是 AI 常常直接 Read 大型 log 檔，結果 context 直接爆掉，整個 session 要重來。光是「不要直接讀 log」的警告就出現了 14 次。

### Personal Finance（33 個 session）

找到一個很有趣的 pattern：AI 用訓練資料中的舊數據（比如「美股平均波動率 10%」），而不去上網查最新數據。我的原話是「你有上網找嗎？不要靠自己的猜想」。

### Crawler（12 個 session）

這個專案幾乎沒有糾正紀錄，搜尋「不對」「錯了」「改回來」全部零結果。代表 AI 在這個專案的表現一直不錯——可能是因為任務比較單純（爬蟲 + 資料整理）。

## 全自動化流程

手動一個一個搜太慢了，所以我讓 Claude Code 自己跑：我把 6 個專案丟給 6 個平行 agent，每個 agent 負責一個專案的分析和 CLAUDE.md 更新。另外再開一個 agent 專門處理使用者層級的 `~/.claude/CLAUDE.md`（跨專案的共通規則）。

7 個 agent 同時跑，全部跑完大概 5 分鐘。

## 效果

更新完 CLAUDE.md 之後，我的體感是：AI 確實更聽話了。

以前那種「我明明跟你說過不要這樣做」的 déjà vu 感少了很多。不是說 AI 變得完美了，而是那些「反覆踩同一個坑」的低級錯誤明顯減少了。

比如之前 AI 常常不讀既有代碼就開始改，現在會先 Read 相關檔案再動手。以前遇到問題就用 try-catch 吞掉，現在會先找根本原因。

## 幾個小提醒

搜尋關鍵字的選擇很重要。中文跟英文使用者罵 AI 的用語不一樣，你得用自己的語言去搜。session 少的專案可能什麼都搜不到，正常，不是每個專案都會有料。

另外 `sessions tools` 可以看工具使用統計，有時候能發現一些有趣的事，比如某個工具被用了幾千次但另一個幾乎沒被碰過。

我打算每個月跑一次，當作 AI 的績效考核。而且不要自己手動去看 JSONL，讓 Claude Code 自己用 claude-log 搜尋、分析、更新，整套自動化跑完就好。

說到底，你的 `CLAUDE.md` 應該是從實戰中打過來的教訓，不是你坐在那邊想像 AI 可能需要什麼。這個工具就是讓你把那些散落在幾百個 session 裡的教訓撈出來，5 分鐘的事。

---

**工具連結：**
- 文章：[Self-improving CLAUDE.md files](https://martinalderson.com/posts/self-improving-claude-md-files/)
- GitHub：[martinalderson/claude-log-cli](https://github.com/martinalderson/claude-log-cli)
