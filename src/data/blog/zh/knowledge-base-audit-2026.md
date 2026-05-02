---
title: "知識庫大掃除：用 AI 幫你找到埋了幾個月的爛帳"
slug: "zh/knowledge-base-audit-2026"
pubDatetime: 2026-05-01T04:00:00Z
description: "Rules 從 13,020 降到 7,590 tokens、92 個 wikilink 斷連、待辦系統五大根因——記錄一次花了四天的知識庫健檢，以及整理出來的季度 SOP。"
tags: [知識管理, Obsidian, Claude Code, 系統健檢, 自動化]
featured: false
draft: false
---

知識庫壞掉通常不是因為某一天突然出錯，而是慢慢爛掉的。

某天你發現一個 wikilink 點了沒反應，某天你打開待辦清單發現同一件事被追蹤了兩個地方，某天你要找三週前存過的書籤，找了十分鐘找不到。每一件事單獨看都不嚴重，合在一起就是「這個系統我已經不太信任了」。

四月底我花了四天做了一次完整的健檢。記錄幾個發現和後來整理出來的 SOP，給同樣在用 Obsidian + Claude Code 組合的人參考。

---

## Rules 系統：悄悄胖起來的 42%

我用 Claude Code 的方式是把大量的個人規則和偏好寫在 rules 資料夾裡，讓 Claude 每次啟動都讀進來。問題是這些規則一條條加，沒有人在管總量。

這次 audit 發現每次對話的起始 context 已經吃掉 13,020 tokens，等於還沒做任何事，額度就先跑掉一大塊。

解法是把「不是每次都用到」的規則改成 skill lazy-load：只有呼叫特定 skill 的時候才載入，而不是常駐在每次對話。重構完之後降到 7,590 tokens，減少 42%。

實際感受是同樣的 Claude Max 方案，同樣的時間，能做的事情明顯變多了。

---

## Vault Wikilink：92 個斷連，分三層處理

Obsidian 的 wikilink 系統很好用，但相對應的，只要一個檔案被改名、移動，或者當初打錯，連結就靜靜地斷在那裡，不會有任何提示。

這次用 Claude Code 跑了一次全 vault 掃描，找出 92 個有問題的 wikilink。沒有直接全部修掉，而是分三層：

**高優先**：核心 projects 主檔、daily notes 的主連結斷了 — 立刻補，當天解決。

**中優先**：daily notes 裡的交叉引用、book notes 的來源連結 — 批次修，用 Claude 一次過。

**低優先**：歸檔的舊 notes 裡的漏連 — 先標記，留著觀察，不急著動。

重點是分層之後可以決定什麼時候花多少力氣。如果全部當緊急事項處理，那本來就不緊急的問題反而會讓你不想做。

---

## 待辦系統的五個根本原因

這次健檢裡最有收穫的部分，是終於把「待辦清單為什麼總是亂」這件事想清楚了。

找到五個根本原因：

1. **雙主檔職責模糊**：同一件事同時被兩個地方追蹤，但誰是 source of truth 沒講清楚，兩邊都可能過期。
2. **角色漂移**：某個 agent 或 rule 原本只負責 A，慢慢開始做 B，但沒有更新職責說明，導致其他地方也以為自己要管 B。
3. **無歸檔**：完成的事情沒有正式 close 掉，繼續混在待辦清單裡，清單越來越長、越來越難信任。
4. **邊界未定**：這個 task 是誰的問題？哪個 agent 管？哪個 project 下面？邊界不清就容易被擱置。
5. **狀態欄位沒有統一 schema**：有些地方用 `- [ ]`，有些地方用 `status: pending`，有些地方用圖示，搜尋時完全抓不齊。

五個問題裡，雙主檔和無歸檔是最常見的。解法都不複雜，但你得先知道問題在哪裡。

---

## 書籤：定出四軸之後才能搜尋

書籤系統崩潰的方式很固定：一開始隨手記，後來越存越多，最後「我知道我存過，但找不到」。

這次把書籤全部重新整理，定出四個控制詞彙軸：

- `kind`：是什麼東西（tool / article / video / reference / thread）
- `topic`：屬於哪個主題（claude-code / youtube / teaching / finance...）
- `applies`：適用於哪個專案（claude-course / blog / gmat-skills / general）
- `status`：目前狀態（active / stale / archived）

加了這四軸之後，搜尋準確率明顯提升。最重要的改變是現在會定期清理 `status: stale` 的書籤，而不是讓它們無限累積。

---

## 工具補充：neat-freak

健檢做到一半，在 GitHub 上發現一個社群 skill 叫 [neat-freak](https://github.com/KKKKhazix/khazix-skills)，它的介紹很像在戳痛點：「代碼都迭代了七八輪，文檔還是最初那一版；記憶裡寫著 SQLite，其實你早換 PostgreSQL 了。」

每次任務結束後執行 `/neat`，它會自動對齊 `CLAUDE.md` / `AGENTS.md`、`docs/`、以及 agent 的記憶系統，輸出一份變更摘要。概念跟我做的手動健檢差不多，但包成一個 skill 就變成可以每次跑的習慣，而不是每季才臨時想起來。

自動化不是替代思考，是讓思考可以更頻繁發生。

---

## 季度健檢 SOP

最後整理成一個 checklist，大概每季做一次：

- [ ] `claude cost` 或 `/context` 確認每次對話的起始 token count 是否超過 8,000，超過就做 lazy-load 重構
- [ ] 跑 wikilink broken link scan，找出斷連清單，依三層優先序處理
- [ ] 待辦來源審計：每個 todo 必須明確知道它在哪一個唯一地點存在
- [ ] 書籤 review：清理 `status: stale` 的，重新標記沒分類的
- [ ] Skill 清單 review：是否有重複功能的 skill、或者已經沒在用的 skill 還掛著

這五件事一次花兩到三小時。不做的話，問題不是不存在，是不知道在哪裡。
