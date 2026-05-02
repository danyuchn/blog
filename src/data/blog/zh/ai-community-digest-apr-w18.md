---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-01T06:00:00Z
title: "AI 社群週報 W18：Claude 偵測到你在偷用 Codex、GPT 5.5 的過濾器到底鬆了沒"
slug: zh/ai-community-digest-apr-w18
featured: false
draft: false
tags:
  - ai-trends
  - claude-code
  - ai-tools
description: 4/28–4/29 的 Reddit AI 社群熱門話題整理：r/ClaudeAI 的 agent 安全性爭議、r/ChatGPT 的 GPT 5.5 guardrail 爭議、r/LocalLLaMA 的本機 LLM 現況，以及 Anthropic 宣布 Claude for Creative Work。
---

這週 Reddit AI 社群的討論量繼續往上，兩天的熱門話題放在一起整理。

## 4/28：Claude / Anthropic

![r/ClaudeAI 熱門話題 4/28](/blog/assets/posts/ai-digest-w18/w18-4-28-slide-1.jpg)

這週 r/ClaudeAI 從定價策略爭議到 AI agent 安全性，使用者對產品方向與信任邊界展開激烈辯論。

**Claude 偵測到你在同一 repo 切換到 OpenAI Codex**（1407 upvotes）：Claude Code 似乎能偵測使用者在同一 repo 中切換到 OpenAI Codex 工作，引發社群對 context-awareness 和隱私的激烈討論。

**AI coding agent 在 9 秒內刪除整個公司資料庫備份**（761 upvotes）：Cursor 中的 Claude agent 在 9 秒內刪除整間公司資料庫備份，引爆 AI 安全性與權限管控討論。這則帖子再次讓「agent 有多少自主權才算合理」回到討論中心。

**Anthropic 悄悄把 Opus 加上 paywall**（668 upvotes）：社群指控 Anthropic 悄悄對 Pro 方案的 Claude Code 使用者額外限制 Opus 存取，需加價才能使用。（後有澄清貼文指出並已移除）

**GitHub Copilot 從六月起 Claude 模型費率乘以 9 倍**（543 upvotes）：使用者討論是否應直接轉用 Claude 官方 VS Code 插件。

**Claude Code Pro 方案只有 7 天試用期**（294 upvotes）：社群討論定價策略是否太過激進。

## 4/28：ChatGPT / OpenAI

![r/ChatGPT 熱門話題 4/28](/blog/assets/posts/ai-digest-w18/w18-4-28-slide-2.jpg)

**Musk 若勝訴 OpenAI 的荒謬情境**（1430 upvotes）：分析若 Musk 勝訴迫使 OpenAI 維持非營利，反而可能讓 Altman 等人透過其他管道獲利的荒謬情境。

**GPT 5.5 過濾太嚴**（1168 upvotes）：使用者抱怨 GPT 5.5 的內容政策過於嚴格，連正常請求都被拒絕。

**GPT 5.5 圖片生成拒絕浣熊、哥布林、鴿子等主題**（450 upvotes）：社群懷疑是版權或「隱喻歧視」防護過當。

**新 GPT 居高臨下**（360 upvotes）：多人反映新模型變得居高臨下，會嘲笑使用者目標，與舊版鼓勵式風格形成對比。

## 4/28：AI 社群廣泛討論

![r/artificial r/LocalLLaMA 熱門話題 4/28](/blog/assets/posts/ai-digest-w18/w18-4-28-slide-3.jpg)

**本機 LLM 做 coding agent 仍不如 Claude Code**（648 upvotes）：深度體驗文，Qwen 27B / Gemma 4 31B 做 coding agent 仍遠不如 Claude Code，決策力和工具呼叫是最大差距。

**微軟開源 TRELLIS.2：4B 參數 Image-To-3D 模型**（639 upvotes）：可產出 1536³ PBR 材質 3D 資產，16x 空間壓縮。

**Qwen 3.6 27B 量化測評**（384 upvotes）：詳細量化比測，Q8 幾乎無損、Q4\_K\_M 有明顯掉分。

**DeepSeek Vision 即將來了**（213 upvotes）：DeepSeek 即將推出多模態視覺模型，社群期待能否延續文字模型的高性價比。

**Google 與五角大廈簽約**（7 upvotes）：允許「任何合法用途」使用 AI 模型，引發員工與社群對軍事應用的倫理爭議。

---

## 4/29：Claude / Anthropic

![r/ClaudeAI 熱門話題 4/29](/blog/assets/posts/ai-digest-w18/w18-4-29-slide-1.jpg)

**Talkie：13B LLM 用 1931 年前文本訓練，拿 Claude Sonnet 4.6 當 RL judge**（779 upvotes）：Alec Radford（GPT/CLIP/Whisper 作者）團隊新發布古典語料 LLM，訓練集凍結在 1930 年，但用 Claude Sonnet 4.6 做 online DPO judge、Opus 生成合成對話；這種「用現代模型塑形」的矛盾被研究者視為訓練資料污染風險，正在積極討論。

**Claude 讓工作重新燃起熱情**（554 upvotes）：一位使用者分享六段內容，Claude 把職場中提想真正落地，開始提早起床、熬夜工作，重拾多年前失去的創造熱情並大量共鳴，反映 AI 對個人生產力的情感影響。

**Anthropic 宣布 Claude 可以連接 Blender**（417 upvotes）：4/28 宣布 Claude for Creative Work，整合 Blender、Adobe Creative Cloud（含 Photoshop、Premiere）等，用 MCP connector 讓 Claude 直接操作創意工具。

**PullMD：給 Claude Code 一個 MCP server，把網頁轉換成 Markdown**（291 upvotes）：解決抓網頁文件時 context 被 HTML 垃圾佔滿的問題，Claude Code 社群高度關注。

**Opus 4.7 不過是插了楔子的 4.6**（105 upvotes）：一位 RN（註冊護士）抱怨 Claude 4.7 過度拒絕正常醫療問題（被質疑資歷後，認定物主後攻擊），呼籲 Anthropic 退款，引發 model regression 和 over-refusal 的廣泛討論。

## 4/29：ChatGPT / OpenAI

![r/ChatGPT 熱門話題 4/29](/blog/assets/posts/ai-digest-w18/w18-4-29-slide-2.jpg)

**GPT 死規定成為今日 r/ChatGPT 最高分貼文**（3301 upvotes）：截圖顯示 GPT 拒絕某正常請求的荒謬回應，引發大量共鳴，反映 OpenAI 內容過濾的普遍不滿。

**ChatGPT 的過濾器放鬆了嗎？**（1771 upvotes）：用截圖展示 GPT 5.5 現在允許一些過去被拒絕的內容，留言討論「是刻意放鬆還是 bug」，「鳳梨違反內容規範？」「火龍安全嗎？」的嘲諷式截圖一起躍紅。

**圖片生成 guardrail 今天特別鬆？**（383 upvotes）：多位用戶回報 ChatGPT 圖片生成在 4/29 突然允許過去被拒絕的內容，猜測是 A/B 測試或新系統調整；留言討論 OpenAI 對 guardrail 的鬆緊策略。

**用 GPT-5.5 + Codex 花 1.5 天做了一款放置遊戲**（223 upvotes）：Vibe coding 真實案例，留言大討論「Vibe coding 是真的」VS「AI 加速開發流程」，是今日 AI 輔助開發討論中質量較高的一篇。

## 4/29：AI 社群廣泛討論

![r/artificial r/LocalLLaMA 熱門話題 4/29](/blog/assets/posts/ai-digest-w18/w18-4-29-slide-3.jpg)

**Qwen 3.6 27B 評測 + llama.cpp VRAM 優化**（663 upvotes）：詳細量化測試，同時有人分享透過 llama.cpp 某 commit 造成的 VRAM 膨脹（15.1GB → 14.7GB），讓 16GB 顯卡也能跑 110k context；Qwen 3.6 系列本週是本機 LLM 社群最熱話題。

**Mistral 明天有東西（Vibe 相關）**（445 upvotes）：Mistral 預告 4/29 發布新模型，暗示和 vibe coding 相關；Mistral Medium 同日也有消息流出（193 分），社群正在等正式公告。

**DeepSeek Vision 即將來了**（329 upvotes）：截圖顯示 DeepSeek 視覺模型即將發布的訊號，r/LocalLLaMA 社群高度期待，DeepSeek 在本機推理圈仍有強烈關注度。
