---
author: Dustin Yuchen Teng
pubDatetime: 2026-01-01T04:00:00Z
modDatetime: 2026-06-05T04:00:00Z
title: "AI 碎念日記 2026：那些太短但捨不得丟的觀點"
slug: zh/ai-micro-notes
featured: false
draft: false
tags:
  - ai-trends
  - ai-tools
  - micro-notes
description: 2026 年起在 Threads 和 IG 上累積的 AI 短碎念。模型吐槽、開發踩坑、行業觀察、工具心得，每則不超過三行。
---

這是 2026 年起在 Threads 上累積的 AI 短碎念。有些太短寫不成一篇完整的文章，但觀點或吐槽又捨不得丟。按時間排列，保留當下的原始想法。2025 年下半年的碎念請見[2025 歸檔版](/posts/zh/ai-micro-notes-2025)。

---

## 2026 年 1 月

**Claude Code 寫文件**
> Claude Code 寫技術文件超好用，放到 Overleaf 一次過。

**Knowledge Cutoff**
> Vibe Coding 的時候要注意 knowledge cutoff。你指定要用 Gemini 3 Pro，它會以為還沒有這個東西，給你擅自換成舊版。

**嘴砲界的 SOTA**
> 我一直以為台灣不會有 SOTA，沒想到今天一次讓我看見兩個——嘴砲界的 SOTA。

**Musk 與屎山代碼**
> Musk 什麼時候要去收購甲骨文？我想看他重構 2500 萬行的屎山代碼。

**Anthropic 在中國**
> 在小紅書上搜 Claude/Anthropic，會發現這是少數曾經明確「辱華」但最後安然無事的。現在看到的都是一片「太好用/怎麼翻牆用」。所以實力還是硬道理。

**rm -rf 的警告**
> 網路上已經有不少 `rm -rf` 的慘痛案例了。做這件事的時候永遠不要開 `dangerously skip permission`。

---

## 2026 年 3 月

**案子滿就沒時間發文**
> 最近突然悟出了一個道理：當案子滿的時候，其實是沒什麼時間在 Threads 上發文做內容的，因為都在跟 Claude Code 講話，光這樣就飽了。

**NeurIPS 被 AI 洗版**
> NeurIPS 都被 AI 洗到幾萬篇投稿了。博士用 AI 生成內容也不是很意外。

**Claude 撼動華爾街**
> Claude 是那個唯一可以撼動華爾街各大軟體股股價的 AI。你說呢。

**OpenRouter 按量付費很划算**
> 只要用到大量文字的地方就會用到 OpenRouter，比如會議記錄整理。不過因為很 on-demand，而且都選量大便宜的模型，所以評估之後按量付費比較划算，儲值 10 USD 可以用好久。

**iQOS 藍牙逆向工程**
> 我真的是服了 Claude Code。前幾天在 Reddit 看到有人分享 Claude Code 是如何幫他解掉惡意勒索軟體、救回資料。今天我突發奇想，把 iQOS 接進電腦，問他能不能讀到資料。結果他真的自動幫我上網找資訊，找到有人逆向工程開發的開源專案，閱讀裡面的邏輯，然後自己寫一個腳本，硬是透過藍牙把 iQOS 的資料讀出來了。

---

## 2026 年 4 月

**Claude Code 遊戲玩家天賦**
> 看到有留言區一半的網友連 Roblox 都拼錯字。不過會喜歡玩 Roblox 的其實很有天賦，給他換 Claude Code 吧，他在這裡面沈迷，未來肯定大有可為。操作滿兩年後出來做 AI agent 比很多工程師還有直覺。

**CC 就是 Claude Code**
> 糟糕，我現在看到 CC 都以為是 Claude Code，我生病了嗎⋯

**社交 agentic AI 俱樂部**
> 我需要一個社交 agentic AI 俱樂部：面對面不說話，用我手中的 Claude Code 跟對面的 Codex 吵架，互相審查代碼撕逼。門票要收。

**RapidAPI vs Apify**
> 這週研究的結論：RapidAPI 是「超市買現成品」，Apify 是「有廚房讓你自己煮或買別人的料理包」。RapidAPI 付錢給平台（抽 25%）不是直接給 API provider；每個 API 各自獨立訂閱，額度不共用，但共用帳單頁面。教學應用上，RapidAPI 示範「不自己爬蟲的情況下取得旅遊/飯店即時資料」很好用。

---

## 2026 年 4 月下旬（W18）

**AI 履歷軍備競賽**
> 聽說北美更瘋：你用 AI 海量投履歷，他用 AI 海量刷履歷。最後兩邊都沒有人在做任何事，只有 AI 在跟 AI 對話。

**百度讓 Claude 說不**
> 平常 Claude 道德感都很高，這個不準那個不做的，碰到百度怎麼那麼配合破解。看來 Dario 在百度那段時期有不知名的陰影。

---

## 2026 年 5 月上旬（W19）

**ICML 開獎焦慮**
> ICML 到底何時才要開獎...好緊張。

**GPT 笨拙塗鴉風 prompt 流行**
> 國外最流行的 GPT 生圖指令：「請用最笨拙、塗鴉、毫無價值的方式重繪附件圖片。使用白色背景，並讓它看起來像是用滑鼠在小畫家裡畫的。」Reddit 大作合集：<https://www.reddit.com/r/ChatGPT/comments/1t0pyb4/gpt_image_2_prompt_that_is_viral_right_now_redra/>

**MD 幻想**
> 我懂 md 幻想！剛開始用 Claude Code 的時候，每做一件事他就幫我創一個 md 文檔，報告他剛剛幹了什麼事。很快地，我的資料夾裡 md 檔就比代碼檔多出好幾倍。這樣算不算是一種 md 幻想？

**5 萬行腳本的 vibe**
> 想看一個腳本 5 萬行程式碼的 vibe。

**/effort xxhigh 的下一步**
> 下一步：我們推出 `/effort xxhigh`，建議使用以保持最佳效能。

**Mercury 銀行推出 CLI**
> 今早收到的信，當初辦美國公司接 Stripe 的時候合作的銀行 Mercury，推出 CLI 工具了，方便跟 AI agent 對接。台灣的銀行⋯⋯（望向金管會）

![Mercury CLI 公告畫面](/blog/assets/posts/mercury-cli-w19/mercury-cli.jpg)

**Claude FM Lo-Fi 直播**
> Claude 官方帳號又開始整活，弄了一個 Lo-Fi Music 直播。能在嚴肅的安全研究跟 Lo-Fi 之間自由切換，也算是這家公司的特色之一。

![Claude FM Lo-Fi 直播](/blog/assets/posts/claude-lofi-w19/lofi-stream.jpg)

---

## 2026 年 5 月中旬（W20）

**Stripe Atlas 四步路徑**
> 1. Stripe Atlas 誰都能做，500 USD 線上點一點就開好公司，我就是在清邁酒吧裡點手機申請的。2. 點完後再繼續點一點申請 Stripe，拿 API 去串 vibe coding 出來的網站。3. 教人怎麼點出以上 1、2，我也做過，不過是免費的。4. 這我就沒做了，因為太缺德。

**L3 BD outreach 開信率**
> 用「交流型」第一封信（不提報價、不問需求、只提「想跟你約個時間，交流一下 AI 的實際應用」），開信率 67%。同一批 list 用「推銷型」（提課程、提 L3 顧問服務）開信率 17%。差距 4 倍。第一封信不要急著賣東西，這件事在 BD 漏斗的前期是真的成立。

**Resend `scheduled_at` 不可信**
> 設定 `scheduled_at` 排程後，回讀 `GET /emails/{id}` 才是真實狀態。如果欄位回讀 null，代表排程沒成功、已經立刻寄出。不要相信 batch 送出時的 response。

## 2026 年 5 月下旬（W21）

**Karpathy 三姓家臣**
> Andrej Karpathy 宣布加入 Anthropic。OpenAI → Tesla → OpenAI（回鍋）→ 離開 → Anthropic。這應該是 AI 圈最強的三姓家臣了。不過換個角度看，頂尖人才往他認為最有潛力的地方跑，本身就是一種市場訊號。

**Claude.md 禁令自相矛盾**
> 我在 CLAUDE.md 寫了「被使用者糾正時禁止說『你說得對』」。結果 Claude 馬上無視，被我罵沒有遵守規則後，下一句回：「你說得對，我不應該違反語言禁令。」CLAUDE.md 寫的是建議不是強制，真要擋就得用 Hook。

**學得足夠慢就什麼都不用學**
> 在 AI 時代，只要你學得足夠慢，那你就可以什麼都不用學。因為等你學完，那個東西已經被自動化了。反過來說，學得夠快的人會發現自己能做的事越來越多。

**越南咖啡店網路品質**
> 到越南後一開始看到路邊那種門戶敞開、擺矮桌加露營椅的咖啡店，都會想避開，覺得網路不穩。後來才發現這種地方網路品質最好——因為一堆越南少年點一杯咖啡就在那邊玩手遊，萬一延遲高誰要來消費。


## 2026 年 5 月下旬（W22）

**沒開 ultracode 也被自動觸發 103 個 agent**
> 沒開 ultracode，它也給我自動觸發 dynamic workflow，一回神 103 個 agent 已經在路上了，氣死。看來我得研究有什麼參數可以把它強制關掉。不過老實說，我這個 request 只是在殺雞，所以也看不出來牛刀的優越性在哪。

**廣泛焦慮症怎麼看風險報告**
> 教大家有廣泛焦慮症的我會怎麼看一份風險報告：一、8.6% 的風險太高了，不可以接受。二、萬一發生，70% 的狀況跟我想像的一樣、甚至更糟？不可接受。三、我們從不會只擔心 30 天後的事情，30 年還差不多。

**Gemini thinking budget 設無限會回空字串**
> Gemini 2.5 Flash 一直回 `{}` 空回應，根因是 `thinking.budget_tokens: -1`（無限）——thinking 把整個 token budget 吃完，`content` 就變成 null。3.x 改用 `reasoning_effort`，不要再在 model config 裡帶 `thinking`。

## 2026 年 6 月上旬（W23）

**gemini CLI 在未信任資料夾會靜默掛掉**
> gemini CLI v0.28 之後，headless 模式在「未信任資料夾」會靜默失敗——exit 0 但無輸出，包了 `2>/dev/null` 看起來就像掛掉。真正的錯誤訊息是 `Gemini CLI is not running in a trusted directory`。修法：加 `--skip-trust`，或設 `GEMINI_CLI_TRUST_WORKSPACE=true`。

**dotenv 的 `\n` 陷阱殺掉 Resend key**
> RESEND_API_KEY 在 `.env.local` 裡值的結尾混了字面 `\n`（backslash 加 n 兩個字元，dotenv 雙引號陷阱），key 被 regex 砍頭。SOP：用之前先 `curl GET /domains` 驗證 key 是乾淨的。

**Codex 快照裡躺著明文 API key**
> 掃 `~/.codex/shell_snapshots/`，發現一份快照明文 export 了 16+ 組 API key，檔案權限還是 0644 world-readable。

**Vercel 臨時公開頁的兩個坑**
> 新 project 部署出來的 URL 預設開著 Deployment Protection（Vercel Authentication），外部訪客拿到 401。另一坑：`<proj>.vercel.app` 裸別名可能是別人佔走的空殼，自家自動更新的 prod 別名是 `<proj>-<team>.vercel.app`。發連結前先 curl 驗內容。

**額度重置時間為什麼刻意打亂**
> 因為如果重置同時重設時間，那所有人的重置時間會變得一樣，這樣子可能會導致大家有一樣的使用高峰：比如在週期快到的時候瘋狂用，可能會加重尖峰負載，導致伺服器不穩定，所以他們才刻意打亂，我猜是這樣。

**Claude Design 獨立額度消失**
> 早起一則冷新聞：Claude Design 的獨立額度已經消失，併入整體 Claude 的使用額度中。

**檔名叫「逐字稿」的不一定是逐字稿**
> 檔名寫「逐字稿」，打開來是已經整理過的摘要，真正的原始錄音另外存。另一個坑：SenseVoice STT 沒有說話人標記，多人同場時開場自介很容易張冠李戴。

**`includes('ai')` 把 failed 標成 AI**
> 錯誤分類器用 `includes('ai')` 抓 AI 相關錯誤，結果 failed 跟 available 全被誤標。分類關鍵字一律用 word-boundary regex：`/\bai\b/`。
