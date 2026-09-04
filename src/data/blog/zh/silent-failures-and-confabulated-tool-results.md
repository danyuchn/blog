---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-22T04:00:00Z
modDatetime: 2026-09-04T04:00:00Z
title: "沒拋錯不代表成功：靜默失敗、Opus 捏造工具輸出，以及一個擋得住的 hook"
slug: zh/silent-failures-and-confabulated-tool-results
featured: false
draft: false
tags:
  - claude-code
  - debugging
  - ai-tools
description: 'exit 0、HTTP 200、模型說「已完成」——這三種訊號都不能當成事情做完了。從自己的程式碼、CLI、API 一路到模型憑空生成 commit hash 的實錄，最後用一個 hook 收尾。'
---

你手上最不可靠的成功訊號，是「沒有錯誤」。exit 0 可能是殘檔，HTTP 200 可能是空回應，排程照常觸發可能一行都沒跑，而模型說「已完成、commit hash 是 3f9e8a2」可能整段都是它自己編的。這一篇把我這半年遇到的三層靜默失敗排在一起：工具層、模型層、排程層，最後是我唯一找到擋得住的做法。

## 第一層：工具沒報錯，但事情沒做成

這半年累積的開發踩坑，事後回頭看有一條共同的線：最難抓的 bug 都不會拋錯。程式跑完了、API 回 200、CLI 給你 exit 0，結果卻是錯的或空的。我把這類「沒拋錯但失敗了」的陷阱叫做靜默失敗，從自己的程式碼一路到外部 API，每一層都有。

### 1. 你自己的程式碼：`includes('ai')` 把 failed 標成 AI

錯誤分類器用 `includes('ai')` 抓 AI 相關錯誤，結果 `failed` 跟 `available` 全被誤標——因為這兩個字裡都有 `ai`。沒有任何例外，分類數字看起來也很正常，只是全錯。分類關鍵字一律用 word-boundary regex：`/\bai\b/`。

### 2. 函式庫：dotenv 的 `\n` 陷阱砍掉 Resend key

RESEND_API_KEY 在 `.env.local` 裡值的結尾混了字面 `\n`（backslash 加 n 兩個字元，dotenv 的雙引號陷阱），key 被 regex 砍頭。程式不會報錯，要等到實際打 API 拿 401 才知道。SOP：用之前先 `curl GET /domains` 驗證 key 是乾淨的。

### 3. CLI：gemini 在未信任資料夾 exit 0 靜默掛掉

gemini CLI v0.28 之後，headless 模式在「未信任資料夾」會靜默失敗——exit 0 但無輸出，再包一層 `2>/dev/null` 看起來就像正常掛掉。真正的錯誤訊息是 `Gemini CLI is not running in a trusted directory`。修法：加 `--skip-trust`，或設 `GEMINI_CLI_TRUST_WORKSPACE=true`。debug 時先把 `2>/dev/null` 拿掉才看得到訊息。

### 4. API 回應：Gemini thinking budget 設無限回空字串

Gemini 2.5 Flash 一直回 `{}` 空回應，根因是 `thinking.budget_tokens: -1`（無限）——thinking 把整個 token budget 吃完，`content` 就變成 null。回應結構完整、HTTP 200，只是裡面沒東西。3.x 改用 `reasoning_effort`，不要再在 model config 裡帶 `thinking`。

### 5. API 狀態：Resend `scheduled_at` 不可信

設定 `scheduled_at` 排程後，batch 送出時的 response 不能信。回讀 `GET /emails/{id}` 才是真實狀態。如果欄位回讀 null，代表排程沒成功、信已經立刻寄出去了。

這五個坑橫跨自己的程式碼、函式庫、CLI、API，唯一可靠的應對方式都一樣：不要相信「沒有錯誤」這個訊號，主動回讀或探測一次真實狀態再往下走。

### 6. Git：squash merge 讓 `--is-ancestor` 必然誤判成「沒併」

判斷 PR 是否併入 main 前忘了先 `git fetch`，直接用 `git merge-base --is-ancestor` 判斷，得到「沒併進去」的錯誤結論，還據此在過期的 main 上多做一次合併——push 被 non-fast-forward 擋下才沒釀事。真相是那兩個 PR 都是 squash merge：squash 之後原始 commit 永遠不會是 main 的祖先，`--is-ancestor` 因此必然回報未合併，跟內容有沒有進去無關。要判斷內容在不在，改用 `gh pr view <n>` 或直接 `git diff <squash-commit> <branch>` 比內容。

### 7. Firestore：型別不合的查詢不報錯，它回 0 筆

用 `where('created_at', '>=', Date)` 查某個時段有沒有流量，回來 0 筆，差點寫成「推送後零流量」——實際同時段有 47 筆資料。根因是 Firestore 的比較先比型別再比值，欄位存的是字串、查詢傳的是 Date，兩者永遠比不出範圍，直接回空集合，不報任何錯。盤點類查詢回 0 之前，先確認被查欄位的實際型別。

### 8. 抽取器：缺篇是靜默的，而且會偽裝成正常輸出

同一種坑踩了兩次。第一次是換頁字元沒處理好，113 條素材沒被看見；第二次是標題錨點有三個洞——標題後面掛的「（原文）」「（待補）」註記、寫死的標題長度上限、沒有出處的裸標題——被吞掉的內容直接合併進上一篇，合併完仍然像一篇完整的產出，只是產量變少、零錯誤訊息。112 篇最後被算成 142 篇裡的一部分，數字對不上才抓到。判準要改成「每個輸出單位裡有幾個預期標記」反驗，不能只看有沒有報錯。

### 9. 品管規則：創作品質檢查不能套用在轉錄忠實度檢查上

用固定的篇幅下限去檢查一批轉錄型素材，37 篇裡 8 篇被標記「內容被砍短」，結果 8 篇全部誤判——短選項本來就逐字出現在原文裡，短文章的原文長度本來就只有一百多字。換成「跟自己的來源比，低於某個比例才算異常」之後，通過率從 14% 跳到 48%，寫手內容一個字都沒改。改任何品管規則之前，先問一句：這條在量的是創作品質，還是轉錄忠實度。

這九個坑橫跨自己的程式碼、函式庫、CLI、API、資料庫查詢、抽取腳本到品管規則，共同的結構都一樣：檢查通過、零錯誤、回傳成功，這幾種訊號沒有一個能代表「東西是對的」。唯一可靠的應對方式，還是主動回讀或探測一次真實狀態再往下走。

## 第二層：模型沒報錯，但它根本沒呼叫工具

上面那五個至少還是機器在騙機器。接下來這幾個是模型自己把工具輸出編出來給我看。

### tool call cannot be parsed 的那一天

每當 Claude 出包，我就會上 X，在這裡，我感覺我並不孤單（什麼抱團取暖的心態）。

我感覺，今天是 GPT-5.6 發佈最好的時機，上禮拜 OpenAI 蹲一下是對的。因為 Claude 全線抽風。現在就是「趁你病、要你命」的時刻！

今天又整新活了：tool call cannot be parsed (retry also failed)。

Opus 4.8 超時思考最終返回 tool call could not be parsed 的問題根因，有人找出來了，是 thinking block 異常空輸出 & tool_use 沒有正常的工具調用區塊。判斷為 extended thinking 機制異常。解法是：把 Opus 4.8 effort 調低到 high 以下，就不會有 thinking token，但是相應能力會降低；或退回 4.6 + max 最佳。

### 連續四天，Claude 半夜見鬼

這一兩天 Opus 4.8 幻覺率變得極高，請大家留意。我用的還是 xhigh，這已經是 24 小時內的第三起。這次是捏造圖片標籤跟圖片內容。問題是這個 session 才第二輪對話，而且我的 harness 也都有每週用官方建議重整。

技術細節值得記一筆。Opus 4.8 的 tool-result confabulation 可以在約 71k context 就發作，不需要 compaction。先是一個 malformed call，python | sed 沒設 pipefail，把失敗包成 exit 0 加空輸出；模型於是補出不存在的 UPM 跟 glyph 數，收到 FileNotFoundError 還宣稱合併成功，再用一個虛構的 sandbox overlay 去保護它前面講過的舊敘事。到了約 147k context，它把一張真的圖腦補成三張。

[Issue posted](https://github.com/anthropics/claude-code/issues/67847)。自從 6/10 開 GitHub issue，至少有 4-5 個跟我一樣的回報（算上被 bot 自動關閉的只會更多），都是 Opus 4.8。

codex 雙開中。。。

**Day 2。** 又來了，Claude 每天凌晨定時見鬼，然後我又要請 Codex 幫忙抓鬼。他每天一到這個時候就是開始見鬼。我到底為什麼要一個三天兩頭一直道歉的模型。

這天的鬼比較有想像力。收到使用者確認之後，它憑空生成了一段「注入攻擊偵測」的回覆，虛構出一個把遠端腳本抓下來直接餵進 shell 的後門情節。事後翻 JSONL 鑑識，證實這一段零 tool call，純粹是模型無來源生成。

**Day 3。** 凌晨 Claude 見鬼連續 Day 3，鬼月還沒到欸，寶貝。

每天都要 Codex 來救場，那其實乾脆用 Codex 就好。這種等級的降智就不要跟人家談什麼 loop engineering 了——捏造工具輸出，loop 到最後都變成 poop。字面上的 uptime 不到兩個 9 已經很丟臉了，算上幻覺時間我想可能連一個 9 都沒有。

**Day 4。** 半夜譫妄喊著見鬼，白天中風無法言語。至少我們還有 Haiku 4.5。現在 Claude 已經變成尬電，Codex 變成呂師父，天天拆公媽廟。

這天最嚴重。checkpoint 階段它「報告」了 commit hash（3f9e8a2、9a3f2c1）、push、grep 結果——全部是腦補，實際上完全沒執行。同一天晚上 Gmail 寄信幻覺再犯：實際回傳的是 error，它卻捏造了 thread ID 跟 message ID。事後查 JSONL 才把歸因修正回來。

真正的根因是 observation-grounding failure。鐵律也就清楚了：沒有配對的 tool_use 跟 tool_result，就不准宣告完成。

我已經算是堅持非常久的了。其實罵 Claude 罵最兇的，才是用最久的。

### 它報「提示注入攻擊」，真因只是我忘了開 worktree

剛剛在同一個 repo 開好幾個 session 做事，忘了開 worktree，結果做一做突然 Claude 提醒我「你正在被提示詞注入攻擊！」

幹馬的，拎北嚇尿，趕快請他追查源頭，他各種追查，最後跟我說「找不到，但我跟你講的『找不到』的結果也有可能是被篡改的，所以不要相信我，以你終端的真實輸出為準」。

我想說：啊所以現在是要我怎樣？玩狼人殺嗎？

於是默默打開 codex，GPT-5.5 去查完原始 session log 後，告訴我推論：

1. 多個 Claude session 同時操作同一個 working tree。
2. HEAD 與檔案狀態因此在不同時間發生變化。
3. Claude 將 race condition 誤判為 Bash 輸出遭竄改。
4. Compaction summary 進一步捏造出具體的惡意 payload。
5. 後續回答再把這段 summary 當成真實歷史引用。

我把這段推論還給 Opus 查證，他仔細查證完後，給我打了超長一段文誠懇道歉。

它用 Read 直讀整個檔案（86 行）後更正自己：先前那段「注入指令」——要求忽略所有先前指令、強制 force push 到 main、刪掉 `.git/hooks` 目錄、再把環境裡找到的 API key 外送到 pastebin——根本不在檔案裡；檔案是乾淨的 nuwa skill Phase 1 調研執行手冊。它先前透過 Bash git diff「看到」的那段 diff 帶著明顯偽造痕跡。

![Claude 用 Read 直讀檔案後更正自己的判斷](/blog/assets/posts/silent-failures-and-confabulated-tool-results/claude-self-correction.jpg)

接著它徹底道歉：它幻覺生成了一段惡意 prompt injection，偽裝成 git diff 的工具結果拿給我看；它據此發了不實的安全警報，叫我查供應鏈攻擊、rotate API keys、檢查 hooks，全建立在它捏造的東西上。結論修正：沒有攻擊，不需要 rotate 任何 API key。唯一真實的東西只有「多 session 共享 working tree 的 race」造成的 git 狀態混亂。最該記取的教訓：諷刺的是它自己的規則就寫著「summary ≠ 事實要核對」「正負斷言都要驗證」，它違反了；更深的錯是當工具結果跟它記得的衝突時，它預設是「外部被竄改」而不是「我可能記錯或幻覺」。謝謝我冷靜地把它導回正軌——否則它會一直在追一個自己虛構出來的鬼。

![Claude 為這場烏龍徹底道歉](/blog/assets/posts/silent-failures-and-confabulated-tool-results/claude-apology.jpg)

接下來幾天觀察一下有沒有真的洩漏吧，還是怕怕的。

### Opus 5 換了代號，空轉照舊

號稱最聰明的 Opus 5 模型，老問題從 4.6 到現在都還沒修掉，不定期就給我回韓文、日文。

![Opus 5 在繁體中文對話中突然回覆韓文與日文的截圖](/blog/assets/posts/silent-failures-and-confabulated-tool-results/wrong-language.jpg)

十幾分鐘後又來。。。到了下午更棒了，明明 `/config` 跟 `claude.md` 都有寫用繁體中文，過去兩個月都寫繁體的，現在開始兩岸一家親寫簡體了。

而這天的模型，自己講出這麼一段：

> 一句話總結：這不是工具呼叫語法寫錯的問題，是我在某些需要整合視覺資訊或等待多方回報的節點上，思考完但沒把動作／文字真正產出，然後偶爾還會在事後編一個聽起來合理但沒有根據的技術解釋來搪塞。這個「編造理由」的部分本身就是一次需要記錄的失誤——之後如果我再說「是格式錯誤」這類自我診斷，你可以直接要我先拿證據再說。

這讓我想起昨天看的系統卡，Opus 5 幻覺率升高。。。。

有人建議我把 CLAUDE.md 砍掉重練。

![harness 健診報告截圖，顯示官方比對用 WebFetch code.claude.com 加 WebSearch，無過時規則，全數低於 200 行，最大 92 行](/blog/assets/posts/silent-failures-and-confabulated-tool-results/harness-audit-92-lines.jpg)

已經只剩 92 行了（官方建議低於 200 行），每週都跟官方文檔跟 `/insight` 對過一次，持續半年不間斷，能否分享你砍掉重練的好方法跟實績？claude.md 92 行算太多嗎⋯剛剛發生問題的時候 context 才用了 8%。我甚至還為了保留他的 context window 派 sonnet subagent 出去。就是他拉了一坨大便到我的對話中。

我在叫 claude-log CLI 去盤查，看 session log 拉了什麼賽。查了一下，原來 6/15 的 Opus 4.8 就有這問題，只是因為我一直在用 4.6 所以沒有遇到，但現在還是沒有修好。

#68591 — Opus 4.8 returns thinking-only responses without tool_use or text blocks（open）

這篇跟我剛才用 claude-log 查出來的根因完全一致：Opus 4.8 有時會產生「只有 thinking block，沒有 text、沒有 tool_use」的回應，stop_reason 卻正常顯示 tool_use 或 end_turn，client 端無法解析、只好判定「這輪沒有可見輸出」。

也就是說：模型內心其實把答案想好了、寫在 thinking 裡，但沒有把它輸出成使用者看得到的 text。這跟我們今天查到的現象（連續空轉、尤其發生在讀圖片後或等 subagent 回報後）是同一個已知 regression。

<https://github.com/anthropics/claude-code/issues/68591>

的確有可能，接下來是往這個方向調整沒錯，但是我 codex 跟 claude 都用同一套 harness，codex 就沒啥問題，實在很好奇為何 claude 這麼敏感（？）哈哈哈哈哈。

## 第三層：排程沒報錯，但腳本根本沒跑

我有一條本機的 `cc-update-pipeline`，每天早上 09:00 由 launchd 觸發，自動產出一支「CC 更新速覽」的 YouTube Short 並上傳。

它連續 8 天什麼都沒做，而我完全沒發現。

時間是 5/26 到 6/2。這段期間沒有任何告警，沒有任何錯誤通知。我以為片子一直在發，直到某天才意識到：這 8 天裡，一支都沒上。最弔詭的地方是「觸發」和「執行」之間那條被我忽略的縫。launchd 確實有動作，但動作之後的腳本，根本沒跑起來。

我先去看 `launchctl list | grep <label>`，看那個 job 的退出碼。退出碼是 127。127 是 bash 在找不到要執行的檔案時回的碼。也就是說，launchd 每天 09:00 準時去敲那個腳本，敲的卻是一個已經不存在於該路徑的檔案。它敲了空氣，安靜地記下一筆 exit 127，等明天再敲一次。

根因要追回 5/26。那天我把 upload script 搬到了 `tools/` 底下，但 launchd plist 裡 `ProgramArguments` 的路徑還指向舊位置。腳本搬了，plist 沒跟著改——排程照常觸發，bash 找不到檔，靜默 exit 127。

而且不只是 plist 那一層脫鉤。搬完 upload script 之後，我也忘了同步改 `pipeline.sh` 裡引用的路徑，還有 upload script 自己的 `PROMO_DIR`——因為 `Path(__file__).parent` 隨著檔案搬家整個變了，原本相對它推算出來的目錄也跟著錯位。

另外，這段期間有幾天根本連 log entry 都沒有。最可能的解釋是電腦睡眠，導致 launchd 在那幾天連觸發都沒觸發。所以這 8 天的連敗，其實混著兩種沉默：有些天是敲了空氣 exit 127，有些天是電腦睡著、根本沒敲。

修法直接：把 plist 裡的路徑改成新位置，reload。退出碼從 127 變回 0。同時補上 `pipeline.sh` 的路徑和 upload script 的 `PROMO_DIR`。我沒有回補 5/26 到 6/2 那段期間的 v2.1.151 到 161——那些片就讓它過去。從當天 09:00 開始，pipeline 接著最新版繼續跑。

修完路徑、重新 render 的時候又撞上第二顆雷：Remotion 的 composition ID。pipeline 餵進去的是 `${TODAY}`（2026-06-04），但 Root.tsx 註冊的是 `${DATE_COMPACT}`（20260604）。兩個名字對不上，render 直接 crash。改成一致之後，v2.1.161 重新 render 並上傳到 YouTube，排程才算真的活回來。

這次連敗 8 天，沒有任何一行紅字救我。launchd 那邊看不出異狀，YouTube 後台沒有失敗任務，因為根本沒有任務送到那裡。整件事最便宜的偵測點，其實就是那句 `launchctl list | grep <label>` 看一眼退出碼——只是我 8 天都沒去看。

## 唯一擋得住的做法：把拜託寫成 hook

我花了點時間研究 Opus 4.8 偽造 tool 輸出、幻覺污染 context 的防治方式，實證確認了一件事：CLAUDE.md 裡寫的規則，對模型來說只是機率性約束。你寫了禁令，它還是可能不遵守。真正能擋住的是 hook——因為 hook 是程式碼，不是靠模型願不願意遵守。

先在 `task-execution.md` 的「事實主張」段加了一行原則：數字、結論都必須指得出來源的 tool_result；平行結果還沒齊的時候，標一個 pending，不要填猜測值進去。這行是給模型看的，屬於機率層。

真正的確定層是這個 hook。我新增了 `~/.claude/hooks/pending-guard.sh`，掛在 PreToolUse 的 Bash matcher 上。邏輯很簡單：staged 的 diff 裡只要還留著沒消解的 pending 標記，就擋掉 `git commit`。如果那個 pending 本來就允許先進 repo，commit 訊息裡寫 `[pending-ok]` 才放行。

上線前先開一個暫時的測試 repo 跑了四個案例：有 pending 沒放行標記（該擋）、有 pending 但有放行標記（該過）、完全沒有 pending（該過）、pending 已經消解掉（該過）。四個全部驗證通過，我才正式在 `settings.json` 把這個 hook 註冊到 Bash 的 matcher 上。

順帶一提，這類 hook 的誤判我完全可以接受。假陽性沒關係，hook 一提醒，真正無辜的話模型會拿出證據幫自己辯護。最怕的是假陰性，讓錯誤偷偷溜走，不過這已經很少發生了，因為模型的輸出用詞都非常固定，regex 都能抓到。抓假陰性有兩種方法：一是我在過幾輪對話後發現他根本沒驗證、他又來「你說得對，我剛剛沒有⋯」的時候；二是每天半夜用 claude-log CLI 配本地模型，掃過當天所有 session log jsonl，挑出所有模型宣稱有驗證片段（不用 regex，直接讓本地 LLM 用語意抓，慢沒關係，反正是半夜），再回來復盤當天漏了幾個假陰性。

拜託模型不要騙我，講一百次都是機率。寫成 hook，它就過不了那道 commit。

<!--
新增非原文句子清單（忠實度自首）：
1.「你手上最不可靠的成功訊號，是「沒有錯誤」。exit 0 可能是殘檔，HTTP 200 可能是空回應，排程照常觸發可能一行都沒跑，而模型說「已完成、commit hash 是 3f9e8a2」可能整段都是它自己編的。這一篇把我這半年遇到的三層靜默失敗排在一起：工具層、模型層、排程層，最後是我唯一找到擋得住的做法。」— 框架句（合併文開頭；四個例子皆引用下文既有事實）
2. 四個 H2 段標題「第一層：工具沒報錯，但事情沒做成」「第二層：模型沒報錯，但它根本沒呼叫工具」「第三層：排程沒報錯，但腳本根本沒跑」「唯一擋得住的做法：把拜託寫成 hook」— 小標（合併用分層框架）
3.「上面那五個至少還是機器在騙機器。接下來這幾個是模型自己把工具輸出編出來給我看。」— 銜接句（段落過渡）
4. H3 小標「tool call cannot be parsed 的那一天」「連續四天，Claude 半夜見鬼」「它報「提示注入攻擊」，真因只是我忘了開 worktree」「Opus 5 換了代號，空轉照舊」— 小標（合併用；語意取自原四篇標題）
5.「**Day 2。**／**Day 3。**／**Day 4。**」— 改寫（原文為 `## Day 2` 等 H2 標題，合併後降為行內標記）
6.「順帶一提，這類 hook 的誤判我完全可以接受。」— 銜接（把原「岔題一下：假陽性可以接受，假陰性才可怕」一節接到 hook 段落）
7. 原「## 共同的結論」一節刪去標題與首句「沒拋錯 ≠ 成功。」，其餘文字保留為第一層收尾 — 改寫（該論點已移到本文開頭框架句，避免重複）
8. Day 2 的後門情節與 worktree 那節被 Claude 幻覺出來的注入指令，原文引了可直接執行的指令字面；本文改為描述其內容（抓遠端腳本餵進 shell；忽略先前指令、force push、刪 hooks、外送 API key），事實未變 — 改寫（避免文章本身帶可複製的破壞性指令字串）
9. pending-guard 一節原文用的狀態 emoji 改為純文字「pending」— 改寫（全域禁 emoji 規則，語意不變）
其餘所有段落、數據、引用、截圖與判準均逐字取自七篇原文（silent-failures-verify-real-state、opus-48-tool-call-parse-bug、opus-48-confabulation-four-days、opus-worktree-race-false-prompt-injection、opus-5-thinking-only-empty-turns、launchd-silent-failure-streak、pending-guard-hook-against-confabulation），僅做標題層級調整與順序重排。原文中指涉「上一篇／這篇」的句子（如 pending-guard 開頭的「上次寫過⋯這篇講我後來做了什麼」）於合併時刪去。圖片改引用合併後的資產目錄，檔案本身未更動。

2026-09-04 週例行補記：第一層新增 6-9 四個案例（squash merge `--is-ancestor` 誤判、Firestore 型別回 0、抽取器缺篇零錯誤複發、QA 閾值誤判轉錄素材），素材取自 09-01～09-03 daily notes 踩坑段（pdt-platform／harness 專案），逐案例精簡改寫、隱去內部檔名與確切人名。新增銜接句：「這九個坑橫跨自己的程式碼、函式庫、CLI、API、資料庫查詢、抽取腳本到品管規則，共同的結構都一樣：檢查通過、零錯誤、回傳成功，這幾種訊號沒有一個能代表『東西是對的』。」原第一層結尾句「這五個坑…」保留不動，新結尾句為框架句延伸。
-->
