---
author: Dustin Yuchen Teng
pubDatetime: 2026-01-01T04:00:00Z
modDatetime: 2026-05-23T05:00:00Z
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

**Claude Extension 配 Claude Code**
> 我最常用的：Claude Extension 搭配 Claude Code，效率高到飛起來。

**Claude Code 寫文件**
> Claude Code 寫技術文件超好用，放到 Overleaf 一次過。

**Codex 的定位**
> 用 Codex。Codex 解複雜 bug 真的是神。（但很慢）

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

## 2026 年 2 月

**ccusage**
> `!npx ccusage@latest monthly` 可以看詳細的 API 成本。用 Claude Code 的人推薦裝。

**Gemini 也支援 Skill 了**
> 現在 Gemini 也支援 Skill 了。不過以 Gemini 的尿性，我保持觀望。

---

## 2026 年 3 月

**案子滿就沒時間發文**
> 最近突然悟出了一個道理：當案子滿的時候，其實是沒什麼時間在 Threads 上發文做內容的，因為都在跟 Claude Code 講話，光這樣就飽了。

**NeurIPS 被 AI 洗版**
> NeurIPS 都被 AI 洗到幾萬篇投稿了。博士用 AI 生成內容也不是很意外。

**小模型本地部署的價值**
> 如果是 3B 的話，最大的特色我猜是輕量加本地部署。畢竟很多 OCR 高敏感場景，資料是不能出去的。如果再搭配上聯邦學習架構就更好了。

**Claude 撼動華爾街**
> Claude 是那個唯一可以撼動華爾街各大軟體股股價的 AI。你說呢。

**OpenRouter 按量付費很划算**
> 只要用到大量文字的地方就會用到 OpenRouter，比如會議記錄整理。不過因為很 on-demand，而且都選量大便宜的模型，所以評估之後按量付費比較划算，儲值 10 USD 可以用好久。

**iQOS 藍牙逆向工程**
> 我真的是服了 Claude Code。前幾天在 Reddit 看到有人分享 Claude Code 是如何幫他解掉惡意勒索軟體、救回資料。今天我突發奇想，把 iQOS 接進電腦，問他能不能讀到資料。結果他真的自動幫我上網找資訊，找到有人逆向工程開發的開源專案，閱讀裡面的邏輯，然後自己寫一個腳本，硬是透過藍牙把 iQOS 的資料讀出來了。

---

## 2026 年 4 月

**Qwen 3.6 Plus**
> 在經歷核心人員出走的風波後，阿里巴巴在 OpenRouter 上發布了下一代模型 Qwen 3.6 Plus 的預覽版。官方表示強化了編程、Agentic、前端開發、複雜問題解決能力。不過目前的 preview 版會收集 prompt 跟 completion output，生產環境要謹慎。

**how-claude-code-works 這個站點**
> 最近減少看 Threads 的時間，開始認真讀這個網站：<https://windy3f3f3f3f.github.io/how-claude-code-works/>。系統性地吸收知識還是比碎片化好太多。

**Google OAuth 邪惡想法**
> 官方 Claude App Connector 的 OAuth 幾乎是全開，但 MCP 只用到一小部分。理論上可以借用它的 credential 自己架功能更完整的 MCP——Gmail 讀發刪、Drive 讀寫刪、Calendar 讀建刪，全通。但這違反服務條款，是未授權使用。所以說邪惡。正規做法還是自己去 Cloud Console 申請，或者用 [gog CLI](https://youtu.be/Ymzp6hF8ZBc)。

![Google 服務實測結果](/blog/images/micro-notes/google-oauth-connector-table.jpg)

**Haiku 4.5 做全端開發**
> 2026 最強炫智方式：用 Haiku 4.5 做完全端開發。不是逞強，是因為成本跟速度的組合現在只有 Haiku 撐得住「改一點、驗一點、再改一點」這種全端節奏。

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

**Claude Code 安全觀**
> 他如果在你的電腦單純生成檔案，會比你們在網路上下載不知名的檔案更安全。只要電腦連上網的那一刻就有駭客入侵的可能，Claude Code 並沒有劣於其他應用多少，甚至修補漏洞的頻率還比大部分應用更頻繁。比起擔心 Claude Code，初學者更應該學好版本控制、權限控制、做好檔案快照備份。

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

**claude-log-cli**
> 30 天內的對話都存在 jsonl 裡面。你可以裝 <https://github.com/martinalderson/claude-log-cli> 快速找歷史對話，改參數可以把預設保留的天數拉長。

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

**5/10 免費 AI 講座 350+ 報名**
> 一場免費講座，從 200 人累積到 350+ 報名。從業務、PM、行銷、研究員、設計、會計、工程師、補習班老闆——各行各業的人都來了。他們在問同一件事：「AI 已經改變職場了嗎？我準備好了嗎？」

---

## 2026 年 5 月中旬（W20）

**Stripe Atlas 四步路徑**
> 1. Stripe Atlas 誰都能做，500 USD 線上點一點就開好公司，我就是在清邁酒吧裡點手機申請的。2. 點完後再繼續點一點申請 Stripe，拿 API 去串 vibe coding 出來的網站。3. 教人怎麼點出以上 1、2，我也做過，不過是免費的。4. 這我就沒做了，因為太缺德。

**按需載入流量觀察**
> 我認為很重要的進階觀念「按需載入跟索引」反而流量較差。有可能是自己講得不夠淺顯，也有可能是大家雖然知道額度很重要，但是這部影片卻沒有很積極地把上下文管理跟額度連結在一起。其實上下文管理能省的不只是額度，還有提升模型的表現。

**L3 BD outreach 開信率**
> 用「交流型」第一封信（不提報價、不問需求、只提「想跟你約個時間，交流一下 AI 的實際應用」），開信率 67%。同一批 list 用「推銷型」（提課程、提 L3 顧問服務）開信率 17%。差距 4 倍。第一封信不要急著賣東西，這件事在 BD 漏斗的前期是真的成立。

**Resend `scheduled_at` 不可信**
> 設定 `scheduled_at` 排程後，回讀 `GET /emails/{id}` 才是真實狀態。如果欄位回讀 null，代表排程沒成功、已經立刻寄出。不要相信 batch 送出時的 response。

**AI 求職示範片**
> 5/10 講座的「AI 求職示範」段落剪出來放 YouTube：<https://youtu.be/HcADayRCJMg>。Claude Code 一次跑完 6 間公司客製履歷，比手動投省 5 個晚上。這段是講座當天最多人留言問的內容。

**Obsidian 影片的逆風**
> 在前陣子不少人跟風吹捧 HTML 揚棄 markdown 的時刻，我發了一部誠實分享自己 Obsidian 知識庫的影片，算不算是一種逆風呢？<https://youtu.be/EhMKfG1dvnI>

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

**DeepSeek 是性價比最高的平替**
> 等他們算力到位之後還會繼續降價。說真的，除了合規要求以外，DeepSeek 應該是目前性價比最高的平替了。

**廣泛焦慮症怎麼看風險報告**
> 教大家有廣泛焦慮症的我會怎麼看一份風險報告：一、8.6% 的風險太高了，不可以接受。二、萬一發生，70% 的狀況跟我想像的一樣、甚至更糟？不可接受。三、我們從不會只擔心 30 天後的事情，30 年還差不多。

**Gemini thinking budget 設無限會回空字串**
> Gemini 2.5 Flash 一直回 `{}` 空回應，根因是 `thinking.budget_tokens: -1`（無限）——thinking 把整個 token budget 吃完，`content` 就變成 null。3.x 改用 `reasoning_effort`，不要再在 model config 裡帶 `thinking`。
