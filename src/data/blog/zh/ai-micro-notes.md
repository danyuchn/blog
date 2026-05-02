---
author: Dustin Yuchen Teng
pubDatetime: 2026-01-01T04:00:00Z
modDatetime: 2026-04-23T08:00:00Z
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

**Gemini 3 的脾氣**
> Gemini 3.0 Pro 很有自己的小脾氣。打開思維鏈看就會發現內心戲有夠多，不斷自我懷疑、搞砸、自責、重來又搞砸一次。

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

**Gemini 3 在 Chrome**
> Gemini 3 會在我看網頁的時候在 Chrome 裡一直自我懷疑跟道歉，說「我搞砸了」。時不時跟我說「我只是個語言模型，幫不上忙」。

**ccusage**
> `!npx ccusage@latest monthly` 可以看詳細的 API 成本。用 Claude Code 的人推薦裝。

**Gemini 也支援 Skill 了**
> 現在 Gemini 也支援 Skill 了。不過以 Gemini 的尿性，我保持觀望。

---

## 2026 年 3 月

**大量資料處理的習慣**
> 大量資料處理我的習慣是：先用 Opus 討論未來需求、取樣跟規劃 schema。接下來按照 schema，用 SiliconFlow 或 OpenRouter 上的便宜模型，API 加並行批量處理。

**案子滿就沒時間發文**
> 最近突然悟出了一個道理：當案子滿的時候，其實是沒什麼時間在 Threads 上發文做內容的，因為都在跟 Claude Code 講話，光這樣就飽了。

**讀 Anthropic 官方文件**
> Anthropic 官網的 research 欄位，建議每出一篇都要讀一下。Claude Code 的 official documentation 也建議時不時閱讀。他們家寫的東西真的詳細又容易理解。

**追蹤 Anthropic 員工**
> 除了 Anthropic 自己的官網部落格文章外，我也喜歡去追蹤 Anthropic 員工的社群媒體帳號。比如 Claude Code 的主要維護者 Thariq，他的文章都非常有價值。

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

**Mythos Preview 244 頁系統卡**
> 官方發了下一代 Claude Mythos Preview 的系統卡，244 頁。我把覺得是重點的地方另外 highlight 起來供大家參考。原檔在 <https://www-cdn.anthropic.com/53566bf5440a10affd749724787c8913a2ae0841.pdf>。讀系統卡真的是比讀 marketing blog 有用多了，該有的招數跟不該有的陷阱都在裡面。

**Clem 嗆 Mythos**
> Claude Mythos「自主發現零日漏洞」的宣傳出來後，Hugging Face CEO Clem 馬上拿出實測：小型開源模型也能做到同樣的事。他們拿了 8 個模型跑 Anthropic 宣傳的漏洞，8 個都復現了，其中一個只要 $0.11/M token。中文自媒體一片吹捧，英文技術圈直接開嗆。來源：[AI Cybersecurity After Mythos: The Jagged Frontier](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier)

![Clem 的實測 tweet](/blog/images/micro-notes/clem-mythos-tweet.jpg)

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

**/HSYW-bullshit skill 的商業計畫**
> 設定 `/schedule` 排程，每週一出門前，讓 Claude Code 幫你生成週末假故事；每天出門前，生成昨天假成就，自動發到信箱，通勤時閱讀 1 分鐘，等等跟同事胡吹。還可以包成一個 skill `/HSYW-bullshit` 上 GitHub，我相信很快就能收穫 5000 顆來自 i 人的星星，然後就可以申請免費用 Claude。

**RapidAPI vs Apify**
> 這週研究的結論：RapidAPI 是「超市買現成品」，Apify 是「有廚房讓你自己煮或買別人的料理包」。RapidAPI 付錢給平台（抽 25%）不是直接給 API provider；每個 API 各自獨立訂閱，額度不共用，但共用帳單頁面。教學應用上，RapidAPI 示範「不自己爬蟲的情況下取得旅遊/飯店即時資料」很好用。

**Claude API 三大欠揍名言**
> 整理一下這週最常讓我翻白眼的三句：1. 你說得對 2. 這不用學 3. 推薦你使用 Anthropic API。三句都是還沒搞清楚狀況就先丟出來的安撫。4.7 後頻率更高。

---

## 2026 年 4 月下旬（W18）

**額度重置時間為什麼每個人不一樣**
> 發現每個人 reset 時間都不一樣，有人禮拜天，有人禮拜三⋯猜測是因為上次同一時間 reset 導致大家都在同一個時間窗口燒 token，server 負載有問題，所以故意重新打散。

**模型選用實際用法**
> 寫文章：Sonnet medium。簡單程式任務：Opus 4.6 medium。複雜任務：Opus 4.6 high/max。4.7 我還沒感受到他的好。

**Opus 4.7 貧嘴**
> Opus 4.7 有夠貧嘴，很想給他巴蕊。回應數據分析請求前，先長篇吐槽數據不一致問題。這是哪門子助理。

**快取未命中邊界 bug**
> 莫名其妙告訴我快取未命中，然後就突然跳了 20% 五小時額度，問題是我完全沒有做任何會破壞快取的事情。我猜又是哪個邊界 bug 在最近的版本中出現了。

**Claude Code 安全觀**
> 他如果在你的電腦單純生成檔案，會比你們在網路上下載不知名的檔案更安全。只要電腦連上網的那一刻就有駭客入侵的可能，Claude Code 並沒有劣於其他應用多少，甚至修補漏洞的頻率還比大部分應用更頻繁。比起擔心 Claude Code，初學者更應該學好版本控制、權限控制、做好檔案快照備份。

**AI 牛排的性價比問題**
> 有兩百塊的夜市牛排，也有兩千塊的餐廳牛排；可是後者有比前者好吃十倍嗎？AI 訂閱費跟產出效益的比例，總感覺怪怪的⋯

**AI 履歷軍備競賽**
> 聽說北美更瘋：你用 AI 海量投履歷，他用 AI 海量刷履歷。最後兩邊都沒有人在做任何事，只有 AI 在跟 AI 對話。

**百度讓 Claude 說不**
> 平常 Claude 道德感都很高，這個不準那個不做的，碰到百度怎麼那麼配合破解。看來 Dario 在百度那段時期有不知名的陰影。

**Claude Max 5x 的真相**
> 有人實測：5x 到 20x 的「增加 4 倍」其實是五小時額度，週額度其實只有增加兩倍。Pay more, get less than expected。

**工具會變，思維不變**
> 拍了快三十部 Claude Code 免費教學影片，慢慢開始有新的感觸：工具會變，思維不變。出一張嘴也是有學問的。真正想分享的是指揮的邏輯思維：拆分任務、規劃驗證、分配職責、風險管理。
