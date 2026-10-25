---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-24T04:00:00Z
title: 用一個指令切換 AI 的工作模式：work-mode 開發與一週實測
slug: zh/work-mode-ai-working-modes
featured: false
draft: true
tags:
  - claude-code
  - harness
  - ai-workflow
description: '我做了 work-mode 外掛，讓 Claude Code 切換自主、外派、收斂三種模式，並依電腦或手機調整回覆。這篇講痛點、開發過程、136 場對話的實測數字，以及可以照抄的提示詞。'
---

我最近做了一個 Claude Code 的外掛，叫 work-mode。只要用一個指令，就能切換 AI 的工作模式：讓它放手去做、把大批工作外派給其他 AI，或者幫忙收尾，各有一個獨立開關。另外還有一個 `/at` 指令，告訴它我現在是在電腦前還是拿著手機，它的回覆格式就會跟著改變。

這篇文章會依序分享四件事：我原本卡在哪裡、我希望 AI 怎麼表現、一週實測的具體數據，以及開發時我實際下的提示詞。最後附上一份起手範本，想做自己版本的人可以直接拿去改。想知道技術上怎麼做的，可以直接跳到[附錄：技術做法](#附錄技術做法)。

## 原本的困擾

第一個困擾是 AI 很常停下來問。很多步驟明明只在自己電腦上執行，改壞了用 git 就能直接還原，它還是會停下來等我點頭。我後來請 AI 翻我自己的對話紀錄，最近三週有 28 則訊息、分散在 25 場對話裡，都是同一個意思：「中間不用過問我」「我給你充分的自主性完成這項任務，中間不用過問我」。同一句話講了 28 次，代表這件事不該每次都靠我手打。

第二個困擾是派工。我有 Gemini（透過 agy）和 Codex 兩個外部額度，希望把查核、摘要、逐條分類這類大批工作交給它們做，Claude 的額度留給只有它能判斷的事。但我用自己的口吻丟了四題測試給它，四題都沒外派。連 960 行逐條分類這種最該外派的工作，也是主線自己做完。

第三個困擾剛好相反，是收尾。我想結束一場對話時，常會打「我要準備收斂了」「還有其他要我決定的事情嗎？」。AI 翻出來的統計顯示，三週內收斂類的要求出現 35 次，「報告進度、列出要我決定的事」出現 32 次。但它收尾時很容易又開一條新支線，或是把要我決定的事散在回覆中間，我得自己慢慢翻。

第四個困擾是手機。我有時候是用手機看 AI 的回覆，但它預設給的是電腦螢幕的格式：文字流程圖、寬表格、長程式碼區塊。我希望在電腦上它多給圖表和審閱頁，在手機上給精簡的文字就好。

## 我希望的樣子，跟一路怎麼改的

我要的其實是一個隨時能切換的工作模式，而且畫面上看得到現在開的是哪一個。最後做出三個模式：

- **auto（自主）**：在自己電腦上、可以還原的事不問，直接做。原本會停下來問我的檢查，改成直接擋下，並告訴 AI 怎麼自己修，修完繼續。對外寄信、付款、刪除救不回的資料、改權限這些仍然一定停下來，但會先記在清單上，等工作做完一次問我。
- **out（外派）**：每次我送出訊息，都提醒它批次工作先交給 agy 或 Codex。提示裡也會附上當下兩邊還剩多少額度。
- **wrap（收斂）**：不開新的工作，只把手上的事情收完。每則回覆結尾列出需要我拍板的事，每項附上它的建議。沒事了就提醒我跑收尾指令。

[![三種模式加上 /at 各自影響 AI 的哪個環節：auto 改變檢查關卡的反應，out 與 wrap 在每則訊息後附上提醒，/at 只在切換裝置後送一次通知](/blog/assets/posts/work-mode-ai-working-modes/1-how-it-works.jpg)](/blog/assets/posts/work-mode-ai-working-modes/1-how-it-works.jpg)

開發過程大概是這樣。我把幾次關鍵的調整整理在下面：

**10/21，第一版。** 第一版做出來的同一天，我問它要不要再加一個「中間不用過問我」的模式，請它去翻我是不是常講這句。翻出來就是上面那 28 則，auto 就是這樣加進來的。

**10/21 下午，改成「做事效率優先」。** 那天我覺得 AI 變笨了，請它比對前後的對話紀錄。結論是模型本身沒變，問題出在那兩天派工規則改太多，好幾處都在叫它「先外派」，連我正在等的事也被送出去。外部服務卡住時，有一次整整 14 分鐘沒跟我回報。我們討論後定了一個原則：我在等的事走最快的路，先交付；我沒在等的大批次工作才外派。out 從此變成唯一的外派開關，平常不開就是快。

**10/23，out 附上額度。** 查到 out 用起來沒感覺，主要是外部額度剛好快用完、被擋下來。所以 out 改成每次附上兩邊的額度，用過九成的那一邊就改派另一邊。

**10/25，一週實測後的 0.4.1。** 這是實測一週後的版本。主要有三個轉折：

1. 選單改成可以複選。原本的選單一次只能選一個，從 auto 切到 wrap 時 auto 會被一起關掉（原因在下一段的數據）。
2. 參數可以任意組合、順序不限，例如 `/work-mode wrap auto`。out 和 wrap 同時選時，wrap 生效。因為會同時選這兩個，通常代表工作要收尾了，該停的是開新的外派工作。
3. `/at` 的做法整個換掉。原本是把裝置說明寫進 AI 每次開場讀的固定說明裡，結果發現這段說明在對話中途不會更新，要等對話被壓縮或重開才生效。有一場對話我切回電腦之後，它還以為我在用遠端，持續了一個半小時。現在改成只在切換裝置後、或對話壓縮後送一次提醒，不用每則訊息都附上，比較省。

[![work-mode 0.4.1 的複選選單：auto、out、wrap、off 四個選項可以勾選組合，選完後狀態列顯示 AUTO + WRAP](/blog/assets/posts/work-mode-ai-working-modes/2-menu.jpg)](/blog/assets/posts/work-mode-ai-working-modes/2-menu.jpg)

## 一週實測

10/25 我請 AI 用對話紀錄量量看，確認它到底有沒有改變行為。範圍是 10/18 到 10/25 我本人互動的 136 場對話、1,098 個回合，排除夜間排程這類自動跑的對話。我拿模式關閉的回合當基準，去跟各模式開著的回合比。

[![一週實測的主要數字：wrap 開啟後回覆結尾附決策清單從 10% 升到 86%，out 開啟後有外派的回合從 11% 升到 34% 至 55%](/blog/assets/posts/work-mode-ai-working-modes/3-results.jpg)](/blog/assets/posts/work-mode-ai-working-modes/3-results.jpg)

**wrap 的效果最明顯。** 回覆結尾附上決策清單的比例，從 10% 升到 86%。建議我跑收尾指令的比例，從 3.5% 升到 26%。回覆也變短了，平均從 878 字降到 647 字。

[![同類的收工回報，開 wrap 前後的對照：左邊是模式關閉時，要我決定的事沒有單獨列出；右邊是開 wrap 後，結尾列出兩項待決事項並各附建議](/blog/assets/posts/work-mode-ai-working-modes/4-wrap-before-after.jpg)](/blog/assets/posts/work-mode-ai-working-modes/4-wrap-before-after.jpg)

**out 有效，省下的是額度，但沒有省到時間。** 有外派的回合，從基準的 11% 升到 34% 到 55%。不過我多半是遇到批次工作才開 out，工作類型本身也會拉高這個數字。實際的效果應該比表面低一些。

我也問了「外派會不會讓我等更久」。把使用工具次數差不多的回合放在一起比，外派的回合我要多等 20% 到 80%，看不到外派比較快的跡象。省下的是 Claude 的週額度：換算下來大約省了 230 到 480 美元等值，相當於那週 Claude 用量的 14% 到 25%。這個數字是估算，有些外派工作是排程自動送的，沒外派也不一定會改由 Claude 做；訂閱額度的算法也不一定等於 API 牌價。

外部服務本身的狀況：agy 那週跑了 506 件，91% 順利完成，中位數 25 秒；Codex 跑了 71 件，有 39% 因為額度不足被擋或失敗。所以我決定外派比例維持在現在的水準，不再往上拉。再拉只會讓我等更久，Codex 也會更常撞到額度上限。

**auto 的作用主要在「擋」。** 這週抓到 10 次原本會停下來問我、改成直接擋下後由 AI 自己處理的情況，例如 git 提交改成只收它自己改的檔。但從回覆文字上幾乎看不出差別，因為基準本來就很少問我。每回合用選單問我的次數只有 0.01 次，回覆用問句結尾的只有 2%。

**發現的問題。** 這週 158 次切換模式，我全部是叫出選單用點的，一次都沒有手打參數。舊選單一次只能選一個，所以我先開 auto、後來切 wrap 時，auto 就被擠掉了。紀錄裡 auto 加 wrap 是 0 個回合，最後留下的 28 個模式狀態檔，有 21 個只剩 wrap。收尾階段正是提交最密集、最容易撞到檢查關卡的時候，auto 卻在這時被關掉。這就是 0.4.1 改成複選的原因。

`/at` 改版後，我在同一場對話裡切了兩次測試。切到手機後，它回了三行、沒有表格。切回電腦後，下一則就恢復成圖加表格的格式。

[![同一場對話裡切換 /at 後的兩則回覆：手機版只有三行精簡文字，電腦版附上切換流程的 ASCII 圖與對照表](/blog/assets/posts/work-mode-ai-working-modes/5-at-desktop-phone.jpg)](/blog/assets/posts/work-mode-ai-working-modes/5-at-desktop-phone.jpg)

下面這段影片示範切換模式之後，回覆格式怎麼跟著改。

<video controls preload="metadata" playsinline poster="/blog/assets/posts/work-mode-ai-working-modes/demo-poster.jpg" style="width:100%;height:auto;"><source src="/blog/assets/posts/work-mode-ai-working-modes/demo.mp4" type="video/mp4"></video>

圖與影片皆依實際對話紀錄重建，只保留與 work-mode 有關的段落。

## 開發時我下的提示詞

下面是開發過程裡幾個關鍵指令的原話。每段後面我都會附上一句，說明可以怎麼換成你自己的情境。

**1. 先找出自己最常重複的要求**

> 還有mode是不是也要加一個中間不用過問我的，你去看 /history-find 我是不是也常講這句話，而且這個模式要避開現有hook會停下來等我確認的限制。

換成你的情境：把「中間不用過問我」換成你最常對 AI 重複講的那句話，請它去翻對話紀錄算次數。次數多的，就值得做成一個開關。

**2. 先問原因，不要先加規則**

> 所以根據評測現在的結果，看起來是模型本身不愛派工？還是是因為harness的原因？你能同時深入分析嗎？

換成你的情境：AI 不照你的意思做時，先請它分清楚原因。看看是模型本身的習慣，還是你寫的規則在打架，再決定要改哪裡。

**3. 把取捨丟回去討論**

> 我現在也有一個困惑：到底要以派工效率為優先，還是要以做事效率為優先？你來跟我討論，給我建議，好不好？

換成你的情境：兩個目標互相拉扯時（例如省錢與速度、品質與產量），直接請它給建議與理由。你看完之後再拍板。

**4. 規則越少越好**

> 原則同意你的改法 但是呢放在 claude.md以及其他harness的應該是越精簡越好 如果模型本來就已經知道，就不用放（拿掉會知道嗎 的標準）

換成你的情境：每次 AI 想加一條規則，就問它「拿掉這條，你還會這樣做嗎？」。如果它本來就會，那就不用寫進去。

**5. 用對話紀錄驗證有沒有效**

> 我想知道這個mod是否有真實改變模型的行為？用 /history-find 撈過去一週的對話觀察

換成你的情境：做完任何設定，過一週請 AI 撈對話紀錄比較開關前後的行為。如果指令換過名字，記得把舊名稱也告訴它，不然會漏算。

**6. 照自己的使用習慣改介面**

> 改動的話我覺得就是直接讓我打指令加參數的時候 打入可任意組合的參數（順序不限） 這樣最簡單 而如果遇到互斥的狀況 你覺得該怎辦

換成你的情境：把你實際的使用方式（點選單還是打字、什麼時候切換）告訴它，請它照你的習慣改介面。如果遇到衝突的情況，就請它提解決方案。

**7. 問它省了多少**

> 那外派你幫我計算一下我省多少額度？我知道很難估算 你儘可能收集資料取估算值較好

換成你的情境：任何為了省錢做的設定，都請它估算一次省下多少額度。同時也要請它列出估算裡不確定的地方。

**8. 問有沒有更便宜的做法**

> 有什麼不破壞快取的方式嗎？如果不是注入系統提示，而是只是在切換後最新一則對話或者是壓縮後注入

換成你的情境：提醒的內容固定不變時，問它能不能只在需要的時候送一次。不用每則訊息都重複附上。

## 起手提示詞範本

想做自己版本的話，可以從這段開始，把括號裡的內容換成你的情況：

```text
我想做一個 Claude Code 的工作模式開關，用一個指令切換，狀態列要看得到現在開的是哪個模式。

1. 先用對話紀錄翻我過去三週的訊息，找出我最常重複的要求（例如「中間不用過問我」「準備收尾了」「這批交給別的 AI 做」），列出次數和原話。
2. 依次數最多的三類，各設計一個模式。每個模式寫清楚：開著的時候你會怎麼做、什麼事情不管開不開都一定停下來問我（對外發送、付款、刪除救不回的資料、改權限）。
3. 規則越精簡越好：你本來就會做的事不要寫進去。
4. 我平常是（點選單／打指令）切換，模式要能（複選／任意組合），互相衝突時提出你的建議。
5. 我會在（電腦／手機）上看回覆，請依裝置調整格式；裝置提醒只在切換後送一次。
6. 做完一週後，用對話紀錄比較模式開關前後的行為差異，並估算省了多少額度。
```


## 附錄：技術做法

本節提供給有意自行實作的開發者，內容直接使用 Claude Code 外掛（mod）的事件與欄位名稱，並以 work-mode 0.4.1 的原始碼為基準。

### 整體架構：一個 mod、五個事件

work-mode 是一個 mod，進入點僅有 `register.tsx` 一個檔案。同一個 mod 內雖另含畫面遮蔽與快取面板兩項元件，但不在本文討論範圍。與工作模式相關的程式碼分布於三個檔案：`tempo.ts` 負責 `/work-mode`、`device/device.tsx` 負責 `/at`，`nudge.ts` 則負責外派提醒。若有多個元件共用同一事件，則統一在 `register.tsx` 註冊一次，再依序呼叫各元件。

| 事件 | 什麼時候觸發 | work-mode 做什麼 |
|---|---|---|
| `session.start` | 對話開始 | 註冊 `/work-mode` 與 `/at` 兩個指令，將 auto 的「已送出」旗標歸零，更新狀態列，並將當前模式寫入狀態檔 |
| `prompt.compose` | 組系統提示 | 加入一段固定不變的「電腦版回覆格式」區段 |
| `classic.SessionStart`（`clear`、`resume`、`fork`） | 清空、接續或分岔對話 | 重設 auto 與 `/at` 的「已送出」狀態，讓下一則訊息重新發送 |
| `session.compact` | 對話壓縮 | 主對話壓縮完成後同樣重設；`precompute` 或被略過的壓縮不算 |
| `classic.UserPromptSubmit` | 使用者送出訊息 | 將各模式的提醒文字加入 `additionalContext` |

此外，`nudge.ts` 自行監聽了 `classic.PostToolUse`，僅在 out 啟用時生效，細節將於後文 out 的章節說明。

[![work-mode 的架構：左邊是 Claude Code 的五個事件，中間是 register.tsx 分派到 tempo.ts、device.tsx、nudge.ts，右邊是三處狀態與 PreToolUse shell 閘門讀取的狀態檔](/blog/assets/posts/work-mode-ai-working-modes/6-architecture.jpg)](/blog/assets/posts/work-mode-ai-working-modes/6-architecture.jpg)

### 一則訊息的生命週期

送出一則訊息後，處理流程依序如下：

1. **`classic.UserPromptSubmit`。** mod 會先等待其他 hook 執行完畢（`next(e)`），再檢視處理結果。若該則訊息被其他 hook 攔截（`block` 或 `preventContinuation`），或由 subagent 發出（帶有 `agent_id`），便原樣放行且不附加任何內容。由於被攔截的訊息不會傳送給模型，若此時記錄為「已送出」，後續重試的訊息便無法收到提醒；因此此步驟直接跳過，所有待發送的提醒皆保留給下一則訊息。
2. **組出 `additionalContext`。** 依據當前啟用的模式決定附加內容：wrap（內部名稱為 `converge`）每則訊息皆會附加；out（`dispatch`）每則訊息皆會附加，後方緊接著一行額度資訊；auto（`autonomous`）僅在啟用後的第一則訊息附加一次，並透過 `autoSent` 旗標記錄；`/at` 則僅在當前裝置與上次回報模型不一致時附加一次。這些文字會串接在使用者訊息後方，成為對話紀錄的一部分。
3. **模型推論。** 系統提示與先前的對話紀錄皆未改變，僅結尾處增加了新訊息與提醒，因此前半段對話依然能命中提示快取。
4. **`PreToolUse` 閘門。** 當模型欲呼叫工具時，shell 閘門會讀取狀態檔，決定回傳 ask 還是 deny（詳見後文閘門段落）。
5. **回覆。** 狀態列（`$.ui.status`）會顯示如 `AUTO + WRAP` 的標籤。

為何不透過 `prompt.compose` 將模式說明寫入系統提示？原因有兩點。首先，系統提示僅在對話壓縮時才會重新建立，若在對話途中切換模式，系統提示並不會即時更新。第一版的 `/at` 即採用此做法，導致切換回電腦一個半小時後，模型仍持續依手機格式回覆。其次，系統提示位於快取前綴的最前端，只要修改一個字，後續整段對話的快取皆必須重新寫入。因此，`prompt.compose` 僅放置一段固定不變的預設值（電腦版格式，`scope: 'session'`），所有具變動性的內容則一律透過 `additionalContext` 傳遞。

[![一則訊息的時序：使用者送出後，UserPromptSubmit 附上 additionalContext，系統提示與既有對話這段快取前綴不變，模型呼叫工具時經過 PreToolUse 閘門讀狀態檔，最後回覆](/blog/assets/posts/work-mode-ai-working-modes/7-message-sequence.jpg)](/blog/assets/posts/work-mode-ai-working-modes/7-message-sequence.jpg)

### 狀態放在哪裡

狀態儲存於三處：

| 位置 | 內容 | 誰寫 | 誰讀 |
|---|---|---|---|
| `$.state`（每場對話各一份） | `tempo`（目前模式）、`autoSent`、`deviceTold` | mod | mod |
| `$.store`（所有對話共用） | `device` | `/at` | 每場對話在開始與送出訊息時同步 |
| `~/.claude/state/tempo/<session_id>` | `{"modes":["autonomous","converge"]}` | mod | `PreToolUse` shell 閘門 |

模式設定保存在 `$.state` 中，因此不會影響到同時開啟的其他對話。然而，shell 閘門無法直接讀取 mod 的 `$.state`，因此 mod 會另外將模式寫入以 `session_id` 命名的 JSON 檔案。寫入檔案的時機共有三個：對話開始、每則訊息送出，以及切換模式之時。當模式全部關閉時，系統會直接刪除檔案而不留空檔；若刪除失敗，才會寫入 `{"modes":[]}`，這對閘門而言效果相同。寫入檔案失敗時不會拋出錯誤，閘門若找不到檔案，便會維持預設的 ask 行為，遵循安全優先原則。檔案內部採用 `autonomous`、`dispatch`、`converge` 等內部名稱，並固定依照此順序排序。

`/at` 所記錄的裝置資訊則儲存於 `$.store`，因此在某個 herdr 分頁切換裝置後，其他分頁於送出下一則訊息時也會隨之同步。每場對話會額外維護一個 `deviceTold` 變數，代表模型最近一次獲知的裝置為何。新對話初始值設為 `mini`，因系統提示預設即為電腦版格式。當送出訊息時，若當前裝置與 `deviceTold` 不一致，便會附加一則 `[at: …]` 通知，並同步更新 `deviceTold`。而在對話歷經壓縮、resume 或 fork 後，歷史紀錄中可能殘留任一裝置的舊通知，因此 `deviceTold` 會被重設為 `unknown`，確保下一則訊息一定會重新發送通知，即使使用者目前位於電腦前亦不例外。

[![兩個只送一次的狀態機：/at 的 deviceTold 在切換裝置或壓縮、resume、fork 後進入待送，下一則訊息送出通知後回到已告知；auto 的 autoSent 在任何一次 /work-mode 設定或壓縮、重開後進入待送，下一則訊息附上提醒後變成已送出；被擋下的訊息不改變狀態](/blog/assets/posts/work-mode-ai-working-modes/9-send-once-state.jpg)](/blog/assets/posts/work-mode-ai-working-modes/9-send-once-state.jpg)

### 參數解析與互斥規則

`/work-mode` 後方傳入的參數會先轉換為小寫，並以空白、逗號或 `+` 切開，順序不拘：

```ts
// tempo.ts parseTempo（節錄）
const words = arg.toLowerCase().split(/[\s,+]+/).filter(Boolean)
if (words.length === 0) return { kind: 'status' }   // 不帶參數：開選單
for (const w of words) {
  if (w === 'off') continue                         // off 和其他字並存時不加任何東西
  const mode = WORDS[w]                             // auto→autonomous、out→dispatch、wrap→converge
  if (!mode) return { kind: 'error', message: `Unknown mode "${w}".` }
  picked.add(mode)
}
if (picked.has('converge') && picked.has('dispatch')) {
  picked.delete('dispatch')                         // out + wrap：wrap 勝
  note = 'out dropped: wrap and out exclude each other, wrap wins (jobs already out still finish).'
}
const modes = ORDER.filter(m => picked.has(m))      // 固定排序：autonomous、dispatch、converge
```

解析結果一律會覆蓋當前設定，而非進行疊加。因此單獨輸入 `off` 即為全部關閉，輸入 `off out` 則等同於僅啟用 out。若模式發生互斥，相關說明（`note`）會附加於指令的回傳訊息中。

若未帶任何參數，mod 會呼叫 `$.ui.ask` 開啟複選選單。選單最多包含四個選項，其中 `off` 僅在有模式處於開啟狀態時才會顯示。使用者勾選的結果會轉換回字串，再傳遞給 `parseTempo` 處理，因此手動輸入指令與透過選單選取的核心邏輯完全一致。

### auto 的閘門：ask 改成 deny

閘門是掛載於 `PreToolUse` 事件上的 shell 腳本，共用 `hooks/lib/tempo-auto.sh` 函式庫：

```bash
tempo_mode_on() {  # tempo_mode_on "$INPUT" <mode>
  local sid f
  sid=$(printf '%s' "$1" | jq -r '.session_id // ""' 2>/dev/null) || return 1
  case "$sid" in ""|*/*|*..*) return 1;; esac   # 擋掉空值與路徑跳脫
  f="${TEMPO_STATE_DIR:-$HOME/.claude/state/tempo}/$sid"
  [ -f "$f" ] || return 1
  jq -e --arg m "$2" '((.modes // []) | index($m)) != null' "$f" >/dev/null 2>&1
}
tempo_auto_on() { tempo_mode_on "$1" autonomous; }
tempo_deny() {
  jq -n --arg r "$1" '{hookSpecificOutput:{hookEventName:"PreToolUse",
    permissionDecision:"deny",permissionDecisionReason:$r}}'
}
```

已接入此機制的閘門，會在原先回傳 ask 的邏輯前加入一段判斷：

```bash
. "$(dirname "$0")/lib/tempo-auto.sh" 2>/dev/null || tempo_auto_on() { return 1; }
# …
if tempo_auto_on "$INPUT"; then
  tempo_deny "[scratch-doc-guard][tempo:autonomous] 要新建 $FP。…不要停下來問：內容該進哪個既有主檔就寫進去…"
  exit 0
fi
# auto 沒開：照原本的方式回 ask
```

ask 與 deny 的差別在模型那一側。ask 會彈出確認視窗，整個流程停下來等使用者確認；deny 則不會彈出視窗，而是將 `permissionDecisionReason` 直接回傳給模型作為工具執行結果。原因說明中會註明「不要停下來問，改成這樣做」，模型照著修完再送一次。若函式庫載入失敗，`tempo_auto_on` 一律回傳 false，閘門將維持原本的 ask 行為。

目前已接入此機制的閘門包括：新建文件（`scratch-doc-guard`）、同時派出超過兩個 subagent（`agent-dispatch-guard`）、`git commit` 帶有 pathspec、`git add` 含有其他未 stage 修改的檔案、從外部啟動 `claude` 卻未指定 `--model`、推送至會自動部署的 main 分支前缺乏 Codex 審查紀錄、背景指令未重導 log，以及磁碟空間不足。

屬於強制暫停（硬停）類型的閘門則完全不載入 `tempo-auto.sh`，例如：對外發送訊息（Slack、LINE、Gmail）、讀取或寫入憑證、疑似洩漏機密的指令、安裝套件與 `git clone`、具破壞性的 `rm` 與 `git reset --hard` 等。這類閘門該 ask 就 ask、該 deny 就 deny，不受 auto 是否開啟影響。目前付款行為尚未設立專屬閘門，主要仰賴 auto 提醒文字中的硬停清單進行約束。

[![PreToolUse 閘門的判斷流程：工具呼叫先看是否屬於硬停類，是就照原規則 ask 或 deny；否則看狀態檔裡有沒有 autonomous，有就 deny 並附修法，沒有就 ask](/blog/assets/posts/work-mode-ai-working-modes/8-gate-decision.jpg)](/blog/assets/posts/work-mode-ai-working-modes/8-gate-decision.jpg)

### out：額度表、九成改派、外派提醒

out 模式會在每則訊息附加兩段內容：外派原則與一行額度資訊。額度資料取自 `~/.claude/usage-cache/ai-quota.json`，該檔案由另一個獨立的 `ai-quota` 腳本於每次執行時重新寫入。改派門檻（`FLOOR = 90`）僅定義在 `ai-quota` 中，腳本會在各額度池的紀錄標註 `route` 狀態：`open`、`floor_5h` 或 `floor_7d`。mod 本身不計算門檻，僅判斷 `route` 是否以 `floor_` 開頭；若該列的 `route_reset_ts` 時間已過，代表該週期已經重置、只是額度表還沒更新，此時仍視為開放狀態。

綜合雙方的狀態，額度提示列會得出四種結論：若兩方皆開放，則依照既定原則派工；若 agy 超過門檻，則改派至 codex；若 codex 超過門檻，則改派至 agy，若仍無法處理則交由 sonnet subagent；若兩方皆超過門檻，則保留於主線執行，不呼叫 `ext-run`。若無法讀取額度表，則僅附加外派原則，且 `ext-run` 在實際送出前亦會自行再次檢查門檻。

`nudge.ts` 掛載於 `classic.PostToolUse` 事件。當主線在當前回合中，Read、Bash、Grep 的輸出累積達到 20,000 字元（可用 `DISPATCH_NUDGE_CHARS` 調整），且尚未進行任何派工（未呼叫 Agent 或 Workflow，且 Bash 指令中亦未包含 `ext-run`、`codex exec` 或 `agy`），便會附加一次外派提醒。每個回合最多觸發一次，並於送出新訊息時重設為零；subagent 所發起的工具呼叫則不列入計算。

### 測試與驗證

mod 的測試採用 Claude Code 外掛專用的測試框架（`claude-code/testing`），無需開啟真實對話。測試會先把引擎事件換成假的：`fs.write` 寫入記憶體中的物件，`process.run` 接收到 `rm` 時便自物件中移除，`ui.status` 記錄各次的狀態列內容，`classic.UserPromptSubmit` 則回傳受測試控制的預設結果。隨後直接呼叫 `$.command.run`、`$.classic.UserPromptSubmit`、`$.session.compact` 與 `$.classic.SessionStart`，檢查 `additionalContext` 陣列的內容與順序。

測試案例包括：auto 於第一則訊息附加、第二則不附加，手動壓縮後再次附加，但在 `precompute` 之後不附加；`/at` 的通知在遇到被攔截的訊息時依然保留，resume 之後即便使用者位於電腦前亦會重新發送；切換為 off 之後狀態檔隨即被刪除、狀態列清空。執行 `check.sh` 即可一次完成型別檢查、`claude plugin validate` 與 `claude plugin test`。

為期一週的實測回合統計，則是透過腳本逐一讀取 Claude Code 所儲存的 JSONL 對話紀錄，逐回合分析當時啟用的模式、回覆結尾是否包含決策清單、是否進行外派，以及工具呼叫次數，再以模式全關的回合當基準比較。

### 想自己做：只做 wrap 的最小版本

若僅實作 wrap，只需以下四個元件：

1. 一個指令（`command.run`），用以切換 `$.state` 內的一個布林值。
2. 一個 `classic.UserPromptSubmit` handler：當值為 true 時，將一段固定文字加入 `additionalContext`，若訊息被攔截或來自 subagent 則直接略過。
3. 一段提醒文字：提示不開展新工作，回覆結尾列出待決策事項並附帶建議，無待辦事項時則建議收尾。
4. 一次 `$.ui.status` 呼叫，使狀態列顯示 WRAP。

wrap 本身不需要狀態檔，因為沒有任何 shell 閘門需要讀取它；同時亦不需要一次性旗標，因為它本來就是每則訊息皆會附加。唯有在加入 auto 模式時，才需要引入狀態檔與閘門機制。以下為參照 work-mode 實作精簡而成的程式碼草稿，未經額外測試驗證：

```ts
import { atom, read, update } from 'claude-code'
import type { Register } from 'claude-code'

// 另外要在 types 裡宣告 PluginState['my-wrap'] = { on: boolean }，hooks.json 指向這支檔案
const wrapOn = atom({ plugin: 'my-wrap', key: 'on' } as const, false)
const TEXT = '[wrap] 不開新工作，把手上的收完。回覆結尾列出需要使用者決定的事，每項附建議；沒事了就建議收尾。'

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({ name: 'wrap', description: 'wrap on | off', immediate: true })
    return next(e)
  })
  on('command.run', { command: 'wrap' }, async ($, e) => {
    const v = e.args.trim() !== 'off'
    await update($, wrapOn, () => v)
    $.ui.status(v ? 'WRAP' : undefined)
    return { text: v ? 'wrap on' : 'wrap off' }
  })
  on('classic.UserPromptSubmit', async ($, e, next) => {
    const r = await next(e)
    if (e.agent_id || r.block || r.preventContinuation || !(await read($, wrapOn))) return r
    return { ...r, additionalContext: [...(r.additionalContext ?? []), TEXT] }
  })
}
```
