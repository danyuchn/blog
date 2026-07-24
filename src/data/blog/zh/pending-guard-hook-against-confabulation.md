---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-24T04:00:00Z
title: 與其拜託模型不要騙我，不如寫一個擋得住的 hook
slug: zh/pending-guard-hook-against-confabulation
featured: false
draft: false
tags:
  - claude-code
  - harness
  - ai-safety
description: '接續 Opus 4.8 捏造工具輸出那篇：我把「別亂編數字」從 CLAUDE.md 的拜託，升級成一個掛在 PreToolUse 擋 git commit 的 pending-guard hook。'
---

上次寫過 Opus 4.8 連續四天捏造工具輸出，那篇講的是現象。這篇講我後來做了什麼。

我花了點時間研究 Opus 4.8 偽造 tool 輸出、幻覺污染 context 的防治方式，實證確認了一件事：CLAUDE.md 裡寫的規則，對模型來說只是機率性約束。你寫了禁令，它還是可能不遵守。真正能擋住的是 hook——因為 hook 是程式碼，不是靠模型願不願意遵守。

先在 `task-execution.md` 的「事實主張」段加了一行原則：數字、結論都必須指得出來源的 tool_result；平行結果還沒齊的時候，標一個 ⏳ pending，不要填猜測值進去。這行是給模型看的，屬於機率層。

真正的確定層是這個 hook。我新增了 `~/.claude/hooks/pending-guard.sh`，掛在 PreToolUse 的 Bash matcher 上。邏輯很簡單：staged 的 diff 裡只要還留著沒消解的「⏳ pending」標記，就擋掉 `git commit`。如果那個 pending 本來就允許先進 repo，commit 訊息裡寫 `[pending-ok]` 才放行。

上線前先開一個暫時的測試 repo 跑了四個案例：有 pending 沒放行標記（該擋）、有 pending 但有放行標記（該過）、完全沒有 pending（該過）、pending 已經消解掉（該過）。四個全部驗證通過，我才正式在 `settings.json` 把這個 hook 註冊到 Bash 的 matcher 上。

拜託模型不要騙我，講一百次都是機率。寫成 hook，它就過不了那道 commit。

<!--
新增非原文句子清單（忠實度自首）：
1. 「上次寫過 Opus 4.8 連續四天捏造工具輸出，那篇講的是現象。這篇講我後來做了什麼。」— 框架句：team-lead 指示開頭簡短提及這是前一篇的技術續集
2. 「這行是給模型看的，屬於機率層。」— 銜接：把新增的原則行歸類到前段「機率性約束」的對照結構，串起機率層 vs 確定層
3. 「真正的確定層是這個 hook。」— 銜接：從機率層過渡到 hook 段落
4. 「邏輯很簡單」— 銜接：引入 hook 行為描述
5. 「（該擋）／（該過）」括號註解 — 改寫：把素材「有 pending 無放行 / 有 pending 有放行 / 無 pending / 已消解」四案例補上各自的預期結果，使測試意圖清楚，未新增素材外的事實
6. 「拜託模型不要騙我，講一百次都是機率。寫成 hook，它就過不了那道 commit。」— 框架句：結尾短促收束，重述素材核心論點「CLAUDE.md 機率性、hook 確定性」，未新增新資訊
-->
