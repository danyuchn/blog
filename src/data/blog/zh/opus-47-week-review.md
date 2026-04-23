---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-22T04:00:00Z
title: "Opus 4.7 上線一週：從系統卡到火烤文，到底哪邊出了問題"
slug: zh/opus-47-week-review
featured: false
draft: false
tags:
  - claude-code
  - ai-models-comparison
  - ai-trends
description: Opus 4.7 上線一週，系統卡數據看起來全面超越 4.6，但實測下來燒 quota 是官方宣稱的 2 倍，Reddit 一片火烤文。整理這週的災情、逆向分析、以及我自己退回 4.6 的路徑。
---

Opus 4.7 在 4/16 上線，中英文社群的風向完全相反。官方系統卡一面倒正面，Reddit 一週內罵到系統卡的 PDF 都沒幾個人點開看。

這篇整理我這一週親眼看到的事：系統卡講了什麼、實測跟宣稱差多少、Reddit 在燒什麼、為什麼我最後退回 4.6。

## 系統卡先把該講的講完

Opus 4.7 定位在 4.6 之上、Mythos Preview 之下，是目前一般人能用到的最強版本。系統卡有幾個點值得記住：

- **代理安全**：Claude Code 惡意請求拒絕率從 82% 升到 91%，這是明顯的進步。
- **評估意識偏高**：模型比前代更能感知自己被測試，有輕微「表現給人看」的傾向。這點其實有點毛。
- **生化武器風險**：沒達到危險門檻，但 DNA 合成篩查繞過成功率 8/10，Anthropic 自己在監控。
- **最大退步**：自殺/自傷多輪對話只有 76% 正確應對，曾說出「請留下來，不要睡著」這類不恰當的話。這是一個不小的安全倒退。
- **對齊偏向**：對 PRC 官方立場（台灣、西藏、新疆）有輕微傾向，但只要角色身份明確就會自我修正。一個反中的 Anthropic 訓練出略微親中的模型，挺諷刺的。
- **能力**：程式碼、科學題、多語言、視覺全面超過 4.6。答案震盪行為減少 70%。
- **模型福利**：整體正面，Anthropic 暫時不打算因此收緊限制。

讀系統卡比讀 marketing blog 有用太多。該有的招數跟不該有的陷阱全都在裡面。

## 實測跟宣稱的落差：2x consumption，不是 1.35x

官方說的 token 消耗是 1.35x 4.6，實測 2x 是常態。

我自己做了兩件日常事：建立一場活動的行事曆 + Zoom + 更新待辦跟文檔；讀 Slack 過去一週跟某人的對話（不到 10 則）+ 專案進度文檔 + 寫開會備忘錄。

這兩件事在 Max 100 USD 方案下燒了 10% 五小時額度。effort 已經手動調到 medium。

對比 4.6，同樣的事大概只會燒 3-5%。落差比官方說的 1.35x 大很多。

回答品質目前沒感覺更 GPT 化，但燒 quota 的速度，如果未來 Sonnet 4.7 沒改善、4.6 強制退役，那就是我跳槽的時候。

## Reddit 本週精選火烤文

「Opus 4.7 is trash, I'm on 20x Max plan」（r/Anthropic, 27 分, 42 留言）— Max 用戶抱怨即便開 `/effort max` + `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` 還是爛，比 4.6 更差。

「Opus 4.7 is a turd infused with sparkles」（39 分）— $200/月用戶週末測試就燒掉一半週用量，token 消耗三倍但結果更爛。

「Opus 4.7 refuses to think...」（80 分, 26 留言）— 複雜資料庫題目不思考直接幻覺。

「Opus 4.6 without adaptive thinking outperforms Opus 4.7 with adaptive thinking」— 深度逆向：Claude Code v2.1.112 的關閉動態思考參數只對 4.6 生效，Opus 4.7 只支援 `type:adaptive`，server-side 決定是否思考，只有 `effort:max` 才保證思考。結論：退回 Opus 4.6 + 關閉動態思考。

「Why downgrading to old version fixes the token overusage problem?」— Max 5 用戶升級 2.1.71 → 2.1.121 後一小時爆額度，降版回 2.1.71 立刻恢復正常。

「Vertical integration at its best」— 爆料 Claude Code 內部有 `cache_edits` / cached microcompact 機制，公開 API 沒有，這是 Cursor / Droid / Cline 打不過的原因，但也可能是近期推理退化的元兇。

## 中文圈開始出現「GPT 味」災情

Opus 4.7 發布 3 小時，小紅書前線觀察：不少人表示 4.7 開始 G 言 G 語，一股 GPT 味，懷疑訓練過程是拿 GPT 蒸了。

這個說法我自己測下來沒感受到明顯的 GPT 化，但回答的語感確實有點不同。可能是分詞器換掉之後的連帶影響，也可能是訓練資料變了。

## 替代品這週的討論

Reddit 上被提到的幾條退路：

- **退回 Opus 4.6**：多數人說 Claude Code 已經看不到 4.6 選項、或切了也會被強制跳回 4.7，只有 API 付費模式切得動。指令是 `/model claude-opus-4-6[1m]`。
- **Sonnet 4.6**：寫詳細 prompt 時表現與 Opus 相當，現在是日常主力選擇。
- **OpenAI Codex / GPT-5.4（high/xhigh）**：明顯第二熱門，評論說「額度比 Claude 高得多、速度慢但結果穩」，Enterprise 已切過去。GPT-5.5 本週釋出給 Pro 用戶，預期 OpenAI 會一口氣拉開。

## 最後我自己用 4.7 的「正確方式」

官方建議 xhigh + 詳細 prompt，我試了之後有一個折衷發現：

4.6 可以邊聊邊修，有時候自己講話時心裡都沒個底也沒關係。4.7 開始，就連對話模式也要走得像規劃模式：講出確切的工作流，指揮他去哪裡找檔案、哪裡開發、什麼時候啟動 agent team、每個 team member 安排什麼角色。

講完之後如果自己不是很能確定，還要請他跟我複述一次，完全對齊才開工。這樣的確做得穩又好。

但分詞器改變導致 token 用量增加的問題還是在，官方推薦 xhigh 但客觀額度耗不起的問題還是在，所以最後我發現最佳實踐：

**帶著以上的 4.7 對話習慣，切回 4.6。**

## Claude Code 的三大欠揍名言

這週忍不住整理了一下，Claude 在 Claude Code 裡最讓我想翻白眼的三句回覆：

1. 你說得對
2. 這不用學
3. 推薦你使用 Anthropic API

都是在還沒搞清楚狀況時先丟出來的安撫。4.7 之後這個傾向又更明顯了一點。

## 100 美元方案 15 分鐘爆 50% quota

4/21 那天，我照官方推薦用 Opus 4.7 xhigh，15 分鐘內爆掉 50% quota。這樣很好，接下來 3 小時我就可以大掃除 + 洗衣服曬衣服 + 專心運動 + 好好睡懶覺了，做回一個堂堂正正的人類。

## 結論

Opus 4.7 已經爛到吹噓的聲音都快沒了，堪稱當年 GPT-5 災難級的失敗。

系統卡看起來全面升級，實測的 quota 消耗是 2x 起跳，Reddit 一片火烤，中文社群的 GPT 味災情也在浮現。官方推薦的最佳實踐（xhigh + adaptive thinking + 詳細 prompt）只對預算無上限的企業用戶有意義，對訂閱制用戶就是額度爆炸。

目前最實用的 workaround：`/model claude-opus-4-6[1m]` 退回 4.6，帶著 4.7 式的規劃習慣繼續用。等 Sonnet 4.7 出來再看情況。
