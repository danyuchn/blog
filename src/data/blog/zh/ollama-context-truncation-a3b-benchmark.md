---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-24T04:00:00Z
title: 本機 Ollama 跑 Claude Code 的兩個坑：context 被截斷、A3B 撐不住重驗證
slug: zh/ollama-context-truncation-a3b-benchmark
featured: false
draft: false
tags:
  - claude-code
  - harness
  - ai-tools
description: '記錄兩件事：cco（本機 Ollama 驅動 Claude Code）長期答非所問，根因不是模型不夠聰明，是完整 harness 的 system prompt 早就膨脹到 3-5 萬 token 被靜默截斷；順手把 Mac mini 換上 A3B 當夜間工人測了兩天。'
---

`cco` 是我拿本機 Ollama 驅動 Claude Code 的一個 shell alias。它一直有個毛病：在我完整的個人 harness 底下，回應常常答非所問，或者乾脆一片空白。我一直以為是模型不夠力，直到這天早上才把它挖出來。

## system prompt 早就爆了，只是它不吭聲

根因跟模型選型無關。我的 CLAUDE.md、加上 10 個全域 rules、40 個 skill 的說明、還有 15 個以上 MCP server 的工具定義，這些東西堆起來，讓 system prompt 常態膨脹到 3 到 5 萬 tokens，遠遠超過 Ollama 預設的 context window。超出的部分被靜默截斷了——它不會報錯，就是默默把 prompt 砍掉一截，模型讀到的是一份殘缺的指令，當然答非所問。

修法兩步。第一，改 launchd plist（`homebrew.mxcl.ollama.plist` 以及 Cellar 裡的模板），加上 `OLLAMA_CONTEXT_LENGTH=65536`，把 context window 拉大。第二，`cco` 一律掛上官方的 `--safe-mode` 旗標，把 system prompt 壓到大約 2 萬 tokens。

`qwen3-coder:30b` 加上這組修正之後，我跑了兩項真實測試：一項是精確覆誦指令，一項是寫一個 memoized 的 Fibonacci function。兩項都一次到位、單輪就完成。順手把三支 Ollama-based 的 custom subagent 也裝起來驗過了——`ollama`（泛用代理，跑 qwen3-coder:30b）、`ocr`（qwen3-vl:8b，中英混合圖片文字轉錄近乎完美）、`transcribe`（WhisperX medium 加 pyannote，做語音轉文字加講者分離，對真實 GMAT 諮詢錄音的轉錄品質很好）。WhisperX 加 pyannote 本來排到 8 月 4 號才要裝，提前搞定了。

## 換個新歡當夜間工人：A3B 兩天試運

context 的事解決後，我順手把 Mac mini 換上新歡試了兩天。機器是 Mac mini M4 高配、48GB 記憶體，模型是 Qwen3.6 的 35B-A3B。我用半開玩笑的文言體記了兩則實驗筆記。

第一天：「本地智模布設第一日，備蘋果微型主機 M4 高配款，運存四十八吉，布設通義三卷六版三十五參數 A3B 模體試運。此模難當繁復校驗套件之重載；啓安守簡式裸機馳行，運行方得平穩。」白話說，就是這顆 A3B 扛不住太複雜的驗證套件——也就是完整 harness 那份肥大的 system prompt——改用簡化的安全模式、裸機跑，才穩得下來。相較之下 `qwen3-coder:30b` 每秒的文書處理通量更高，處理程式碼刪改這類任務時，跟智輔協同施為之功尤佳，搭配得更順。

第二天心得就沒那麼樂觀了：「本地智模布設第二日，始知四十八吉運存，僅為初入茅廬之資。若令本地智模獨任長時事務，非但艱澀，速率亦遲。」48GB 記憶體只是入門規格，真要讓本機模型獨自扛長時間的任務，既吃力又慢。於是我把本機模型的職守重新定位：「僅司單次任務，創設智庫滌淨、聲語成文、文字辨識、文牘去秘諸般自製智輔，以供雲上閉源頂模調度驅遣。」翻成白話——只做單次任務，做知識庫清理、語音轉文字、OCR、文件去敏這幾支自製 subagent，供雲端閉源的頂級模型調度驅遣。

目前的結論是先把方案存起來，不建排程，也不動 `cco` 的預設。就這樣。

<!--
新增非原文句子清單（忠實度自首）：
1. 「我一直以為是模型不夠力，直到這天早上才把它挖出來。」— 類型：框架句（銜接素材 A「診斷並修復」與「根因非模型選型」）
2. 「超出的部分被靜默截斷了——它不會報錯，就是默默把 prompt 砍掉一截，模型讀到的是一份殘缺的指令，當然答非所問。」— 類型：改寫（把素材 A 的「prompt 被靜默截斷」展開為讀者能懂的因果，未新增技術主張）
3. 「context 的事解決後，我順手把 Mac mini 換上新歡試了兩天。」— 類型：銜接（兩節之間過場）
4. 「我用半開玩笑的文言體記了兩則實驗筆記。」— 類型：框架句（引出素材 B 文言體）
5. 「第二天心得就沒那麼樂觀了」— 類型：銜接（引出素材 B 第二則）
6. 「目前的結論是先把方案存起來，不建排程，也不動 cco 的預設。」— 類型：改寫（素材 C「先保存方案，不建排程，也不改 cco 預設」原意重述）
7. 「就這樣。」— 類型：框架句（短促收尾）
-->
