---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-03T04:00:00Z
modDatetime: 2026-09-04T04:00:00Z
title: 我在 Claude 和 Codex 之間搬了三次家
slug: zh/three-moves-between-claude-and-codex
featured: false
draft: false
tags:
  - codex
  - claude-code
  - token-optimization
description: '五月把整套 harness 搬到 Codex、七月換掉主力、蜜月期額度怎麼花都花不完、七月補貼大戰打出 57.5x 的帳面價值，到八月額度被偷縮 50% 與 77%。一條照時間排的編年紀錄。'
---

我在 Claude Code 和 Codex 之間來回搬了三次家。以下照時間順序排：五月把整套 harness 搬過去、七月換掉主力、蜜月期、充滿 reset 的七月，最後蜜月期結束。

## 五月：先做一個 Skill 把 harness 搬過去

這個週末成功做的事情就是把 Claude Code 的個人環境遷移到 Codex 身上。

說真的，現在越來越習慣用 Codex，除了額度重置大方之外，還因為 GPT-5.5 講話已經沒有那種油膩味，工作溝通起來很踏實，反而是 Opus 4.7 我時不時想要給他巴蕊。

但是要把整套 harness 遷移過去，挺困難的。

### 痛點

- harness 遷移涉及多項設定與檔案，流程繁瑣
- MCP、hooks 等關鍵設定需要手動處理，試錯成本高
- 未來環境更新後，兩邊容易不同步
- 遷移整套個人工作流，往往耗時又耗力

### SKILL 做了什麼

我把這些流程包成一個 Skill：

- 協助在半小時內完成 Claude Code → Codex 的遷移計畫
- 自動處理 `claude.md` / `agents.md`、SKILL 等基礎設定遷移
- 協助整理 MCP、hooks 等較複雜的遷移項目
- 提供「維護模式」，自動比對變更並同步到 Codex
- 降低人工操作與試錯風險，提升遷移效率

Repo 在這：<https://github.com/danyuchn/claude-codex-harness-sync>

![Claude Code → Codex 遷移 SKILL](/blog/assets/posts/three-moves-between-claude-and-codex/codex-migration-skill--codex-migration.jpg)

### 額外收穫：Codex CLI 還有改進空間

用 Codex 一段時間後最不能忍的是 CLI——光是 `/rewind` 沒得用就很不能讓人理解。Claude Code 那邊 `/rewind` 已經是日常救命招式，遷過去之後一試錯就回不去了，要靠 git stash 或重跑整段對話，效率明顯掉。

希望 OpenAI 那邊更新快一點。

### 順便講一個生圖的意外發現

在一開始創造圖片時，在 Codex 內部直接手動下指令，會比 Claude Code 轉交 Codex 還要好。因為 Claude 常常會下出過度約束的 prompt，而 GPT-image-2 反而是越少約束越能展現其創意跟美感。

中介層越多，原始意圖越容易被「修飾」掉——這個觀察應該不只適用生圖，所有跨 agent 的任務轉交都該想想這件事。

## 七月十日：主力真的換過去了

我一直是個容易嘗試新事物，但是很難轉移習慣事物的人。過去的 4o 出走潮、Antigravity 棄用潮，我都是走在偏後面的一波，但是後續的趨勢都證明了我的決策沒有什麼錯。如果不是原本的主力太讓我失望，且未來看不到可預見的改善跡象，我是不會輕易換的。

現在我終於決定讓主力從 Claude Code 轉到 Codex 了。

### 七輪五小時窗口

Claude 5x（100 美元）方案的五小時額度，從頭到尾都用 Fable 5，大約等於 16% Fable 專屬額度。

要在 7 月 7 日前把重新 reset 的 100% 用滿，大約需要 100 ÷ 16 = 6.25，也就是至少七輪五小時窗口。我已經用掉一輪，所以還有六輪、30 小時窗口。

我排好了六輪時程。屆時週配額應該只剩下 30–40%，但是離下次 reset 還有五天，我將轉往 Codex。據說 OpenAI 就是要趁 Fable 退場時推出能力相當的 GPT-5.6 Sol Ultra 搶人，加上之前一直 reset 送我的 banked reset quota，應該可以撐到週日 Claude reset。

我真是算盤的聲音打到月球都聽得到。

### 默默飄走

我覺得 Anthropic 一定沒有想過，Fable 推出來但額度沒有提升的情況下，100 美元的訂閱一小時內就會撞到窗口。

在剩下四小時的冷卻時間中，人們會想的是再加 100 美元呢？還是會想說加個 20 美元用用 GPT-5.6 Sol？

加了、用了，發現這裡的 20 美元比那裡的 100 美元還持久，而且 5.6 Sol 的效果跟 Fable 也打得不分上下，那……

至少我就是這樣默默飄走的。

## 七月中：額度蜜月期

這週我整個人陷入 Codex 的蜜月期。

先從額度說起。以前不管是 Claude Code 還是 Codex，額度用一用就 reset，每次 reset 都覺得心痛。上禮拜我索性請 AI 幫我搭了一個自動排程：每 5 小時自動用最低階模型打一則訊息觸發五小時窗口，晚上十一點後如果週額度比原定進度落後 10% 以上，就自動掃過未來所有待辦裡可以自動完成的項目，通通做掉，標記「待裁決」或開 PR 等我早上起床審核。這樣一來，週額度可以用好用滿，也不會擋到白天工作需要的額度。

結果換到 Codex 之後，這套排程幾乎沒派上用場——因為額度怎麼樣都花不完。

最誇張的一次是幫一位教授朋友寫 ML 論文。他有三套完整的開題 prompt、寫作規範、一大串約束，我拿一個剛被 reset 週額度的 Codex 20 鎂小號開 GPT-5.6 Sol Ultra 上去做。1.5 小時後額度就耗盡了，但因為開了 /goal，Sol 像瘋狗一樣死咬不放，最終在 2.5 小時後完工，連配圖都用原生 gpt-image-2 一氣呵成。寫稿、改期刊格式、寫 code、跑實驗全都一手包辦。傳給教授朋友後，他說這跟我之前用 Fable 花 100 鎂方案幹光額度幫他跑出來的論文，品質差不多好，但這次只要 20 塊（其實應該算 5 塊，因為只是一個 weekly cycle），而且 Claude 還不能直接生圖。就算是在學術前沿的任務上，Fable 還是太貴了。

隔天我又開 Sol Ultra 幫他寫了四篇論文，才好不容易把週額度幹光，結果一醒來又 reset 了，隔天貌似還要再 reset 一次。這幾天 OpenAI 那邊也確實在動作：Tibo 在 X 上說暫時取消了 Plus/Business/Pro 方案的 5 小時額度限制，還讓 GPT-5.6 Sol 全面變得更省額度，甚至幫 ChatGPT Work 和 Codex 的 50 萬用戶加開了 banked reset。

從 Claude Code 換到 Codex 的整體感覺，很像我第一次到泰國——處處是驚喜。開了 /goal 額度燒完了還在緊咬不放，這是什麼認真精神；額度怎樣都花不完，訂閱費 CP 值高得嚇人；開了 /fast 1.5 倍消耗的快射模式，還是花不完。最重要的是 tool call 中間模型終於開始說人話了，跟 Claude 講話我都不知道是我中文不好還是英文不好。

工具鏈也跟著換血。以前我做教學影片動畫是用 Claude Code + Remotion，常常會有文字 overflow、動畫對不上口白這些問題。現在同樣的事情用 Codex + Hyperframe，一次過，而且額度竟然更省。這不是業配，我找工具的時候還刻意避開業配、避開要收費的。

還在蜜月期，之後會不會降智我不知道，但目前這幾天真的是花不完的爽感。

## 八月初：充滿 reset 的七月，補貼大戰復盤

AI 輕量用戶來復盤一下這個「充滿 reset 的七月」的狀況。

Claude、Codex 各訂 100，一有 reset 就用好用滿，如圖所示，發揮了 57.5x 的價值（計算價格已經排除掉裡面的本地模型 qwen 系列）。

![七月整月的 ccusage 用量表格截圖，全部合計 2.33 億 input tokens 與 6119 萬 output tokens，等值 11501.51 美元；其中 Claude 一列 7415.12 美元、Codex 一列 4086.39 美元](/blog/assets/posts/three-moves-between-claude-and-codex/july-of-resets-subsidy-war--1-july-usage.jpg)

我蠻期待 OpenAI 或 Anthropic 任何一家上市，因為市場才有機會看到真實的 token 成本。

補貼大戰不知道會持續多久，GPT 昨天又宣布降價，Kimi／Deepseek 也在持續讓 benchmark 貼近、把價格打下來，局勢看得不是很明白，但看明白我們市井小民也不能改變啥。

七月上旬那一波尤其明顯：又是主動 reset，又是主動還過期的 credit。沒有任何理由，我能想到的唯一理由就是看到 GPT-5.6 發布，急了。

我個人已經在積極做的，是把 harness 持續瘦身、把部分很單純的單發任務路由到本地模型夜間做或走量大管飽的 Gemini 訂閱方案，這條線另外寫在 [第二次 harness 減肥：全域 skills 58 砍到 40](/blog/posts/zh/skills-58-to-40-second-diet)。

### Deepseek 那張圖可能要作廢了

之前盛傳「Deepseek CP 值斬殺線」的那張圖，可能很快就要作廢了。Deepseek 宣布即將大幅調漲 API 價格。

![X 上 Jukan 帳號的貼文截圖，內容為 DeepSeek 計畫近期全面調漲 API 價格且幅度顯著，下方附 DeepSeek 平台用量頁面的公告橫幅，以及餘額 19.75 美元、累計花費 0.24 美元的欄位](/blog/assets/posts/three-moves-between-claude-and-codex/july-of-resets-subsidy-war--2-deepseek-price.jpg)

想像得到 Luna／Terra 在偷笑。

### 關於 reset 本身

經過我的（不專業）研究，OpenAI 給的重置沒有想像中大方：重置後七天窗口重新計算，Anthropic 則是七天窗口固定，後者其實是讓你在重置後用較短的窗口享有 100% 額度。而且觀察過去的重置宣布時間，都卡在之前發的 banked reset 快過期的時候。

所以我在此立帖為證，8/12-14 一定重置，到時候大家可以回來看。為什麼呢？因為 Tibo 很賊，都會選重置卡到期日故意重置，最後一張重置卡到期日是 8/13。

拿到期日做文章的不只重置。A：「Fable 只能用到 7/12 哦」（隔壁出新模型，大家覺得不錯想改訂閱）「誒誒，別走，幫你延到 7/19 啦」。

另外一個體感：Codex 100 USD 的週額度，好像比 Claude 100 USD 少。還沒有統計 token usage，所以這只是體感，有人跟我有一樣的感受嗎？不知道是因為 Opus 5 太耐用，還是因為 Codex 我用了太多瀏覽器跟電腦控制任務。

還有一件事順帶記一下：Anthropic 最新文章只並列 Fable、Opus、Sonnet，完全沒提 Haiku。Sonnet 看起來正在接手原本 Haiku 的位置，這也是一種不明說的漲價；Haiku 很可能停在 4.5。

月底這幾天更妙，一邊瘋狂 reset，另一邊瘋狂封鎖帳號，簡直是我見過最荒謬的場景。

Anthropic 摳死～

沒了額度就去 x 留言給 tibo 祈願，reset 了就 `/model sol max`，徹底沒了就掏出信用卡哭著刷 200。

## 八月二十日：蜜月期結束

一個多月後，蜜月期結束了。

兩週前我在碎念裡留過一個預測：

> 風向變來變去。以 Tibo 現在吊胃口又假大方丟 reset 在一個本來就會 reset 的時間、codex 版本代碼被挖出未來要賣 reset 券、現在額度耗費又頗高的趨勢下，我預計最短 2 個月、最長 4 個月，OpenAI 會再度跌落神壇。反正他們在行銷公關上就是輪流犯錯，靠對手的犯錯取得優勢。

Codex 額度偷縮被網友質疑了。

Plus 額度實測被偷縮 50%，Pro 5x 實測被偷縮 77%。

![網友實測 Codex 額度被偷縮的數據截圖，列出 Plus 與 Pro 5x 兩種方案的縮水幅度](/blog/assets/posts/three-moves-between-claude-and-codex/codex-quota-nerf-off-the-pedestal--1-codex-quota-nerf.jpg)

沒想到我之前的估計「兩個月跌下神壇」還是太樂觀了。現在 Reddit、X 上都有不少網友叫 Tibo 粗來打球！

Codex 是時候走下神壇了吧。Claude 家最近低調很多，四平八穩沒犯什麼錯，反而是 Codex 偷縮額度，感覺風向已經在變了。

就在這之前幾天，Codex 在沒有頻繁 reset 後，我必須面臨自己真實的任務體感：

承認 Opus 5 真的很划算，額度消耗很少，反而是 Sol 消耗比較快，只是之前被 reset 掩蓋了。當然 Sol 說話我還是比較能看得懂的，但是 Opus 5 的外星話可以靠自己開發的 Skill 解決，也是可以接受。

我現在比較不能忍受的反而是 Codex 要 reset 不 reset，讓我難以掌控自己的用量節奏。

接下來就看 Claude 這一週結束後是否會拔掉 50% 的用量優惠。如果繼續延長的話，那我又會回到 Claude 主力、Codex 附屬的配置。

我果然是數位遊牧啊，逐 token 如逐水草而居的遊牧民族。

## 九月初：塵埃落定，Claude 主力、Codex 副手

過去幾個月我 10 篇文章有 9 篇都在臭 Anthropic，但也必須誠實面對自己的選擇：兩個月兩邊各 100 美元雙開之後，我最終選擇把 Codex 降級到 20 美元，維持 Claude 的 100。

主因是 Fable，次因是 OpenAI 的額度政策。我的工作上創造性任務比維護性任務多，目前所有模型裡，能像上師一樣高度洞悉我的意圖、優雅簡潔地點出我的 unknown unknowns 的，只有 Fable。不是說 GPT 不好，Sol 也是頂級聰明且非常細心，但在我眼裡就是一個聽話的工具人；Luna 成本效益極高，電腦控制表現也好。

<!--
新增非原文句子清單（忠實度自首）：
1.「我在 Claude Code 和 Codex 之間來回搬了三次家。以下照時間順序排：五月把整套 harness 搬過去、七月換掉主力、蜜月期、充滿 reset 的七月，最後蜜月期結束。」— 框架句（合併文開頭，內容全部指向下文既有段落）
2. 五個 H2 段標題「五月：先做一個 Skill 把 harness 搬過去」「七月十日：主力真的換過去了」「七月中：額度蜜月期」「八月初：充滿 reset 的七月，補貼大戰復盤」「八月二十日：蜜月期結束」— 小標（合併用；語意取自原五篇標題與其發文日期）
3.「一個多月後，蜜月期結束了。」— 銜接（取代原文的「一個多月前我寫過[…額度蜜月期](…)。現在蜜月期結束了。」外部連結；合併後蜜月期已在同一篇上文，改為時間銜接）
4.「我個人已經在積極做的，是把 harness 持續瘦身、把部分很單純的單發任務路由到本地模型夜間做或走量大管飽的 Gemini 訂閱方案，這條線另外寫在 [第二次 harness 減肥：全域 skills 58 砍到 40](/blog/posts/zh/skills-58-to-40-second-diet)。」— 改寫（原 july-of-resets 的「## 個人已經在積極做的」整節屬 harness 減肥系列、非本篇主線，壓縮成一句並外連；原節內「這週減了 40% 常駐注入的 token」數字與「未來打算做的進一步分流：非敏感資訊，或者透過本地……」截斷句於此捨棄）
5. 原五篇各自的 H2 小標降為 H3（痛點／SKILL 做了什麼／額外收穫／順便講一個生圖的意外發現／七輪五小時窗口／默默飄走／Deepseek 那張圖可能要作廢了／關於 reset 本身），文字未改 — 改寫（標題層級調整）
其餘所有段落、數據、引用區塊、連結與圖片 alt 均逐字取自五篇原文（codex-migration-skill、why-i-switched-from-claude-code-to-codex、codex-quota-honeymoon、july-of-resets-subsidy-war、codex-quota-nerf-off-the-pedestal），僅做標題層級調整與圖片路徑改指合併目錄，未新增原文沒有的事實、判準或結論，未替作者調和前後立場，也未新增總收尾。

2026-09-04 週例行補記：新增「九月初：塵埃落定，Claude 主力、Codex 副手」一節，素材取自 08-31 Threads 貼文，逐句改寫。新增句：小標（框架句）。其餘句子逐句對應原文，未新增原文沒有的判斷。原貼文結尾一句因文意未完（「Luna 成本效益極高、電腦控制表現」後截斷）已省略未收錄。
-->
