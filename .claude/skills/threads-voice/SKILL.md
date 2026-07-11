---
name: threads-voice
description: "從使用者的 Threads 官方資料匯出檔萃取寫作語氣與風格特徵，輸出 brand_voice.md 供之後寫部落格文章時參考套用。觸發詞：threads 語氣、萃取風格、brand voice、我的寫作風格、分析我的貼文、學我的語氣。"
version: "1.0.0"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# threads-voice：從 Threads 貼文萃取寫作語氣

分析使用者的 Threads 歷史貼文，產出一份可在寫新文章時參考套用的 **brand_voice.md**。

改作自 [akseolabs-seo/AK-Threads-booster](https://github.com/akseolabs-seo/AK-Threads-booster) 的 `/voice` 模組（MIT License，出處與差異見 `../NOTICE.md`）。原專案是完整的 Threads 成長駭客系統，這裡只保留「萃取寫作語氣」這一段，拿掉演算法訊號、互動預測、發文排程等與部落格無關的部分。

## 原則

1. **描述性，不是規範性。** `brand_voice.md` 記錄「這個人怎麼寫」，不是「應該怎麼寫」。
2. **每個結論都要有原文佐證。** 不能靠感覺下結論；資料不夠就誠實說「資料不足，暫略」。
3. **近期優先於歷史。** 如果最近的貼文明顯偏離舊有模式，不要把舊模式當成硬規則。
4. **產出是第一版草稿，不是定案。** 旁觀者（模型）一定會漏掉使用者自己才知道的東西，必須明確告知使用者去讀、去改。
5. **使用者的手動修正永遠優先。** 重跑分析時絕不覆蓋 `## 使用者手動修正` 段落。
6. **腳本先算，Fable 後判斷。** 句長分布、口頭禪次數、開場/收尾模式、段落節奏這類可以純計數算出來的量化維度，一律交給腳本，不要讓 Fable 自己讀整包語料去數。語料量大（幾百篇以上）時尤其重要，不然一次分析就爆額度。
7. **Fable 不直接讀整包 `threads_corpus.json`。** Fable 只讀兩份小檔：`compiled/voice_fingerprint.md`（腳本算好的量化摘要）+ `compiled/qualitative_sample.json`（分層抽樣出的原文全文小樣本）。原始語料只在腳本解析/統計時被讀取，不進 Fable 的 context。

## 資料路徑

工作目錄固定在專案根目錄下的 `.claude/voice/`：

- `.claude/voice/threads_corpus.json` — 解析後的精簡語料（由 `scripts/parse_threads_export.py` 產生；**Fable 不直接讀這份，只有腳本會讀**）
- `.claude/voice/compiled/voice_fingerprint.md` — 腳本算好的量化統計摘要，Fable 分析前一定要讀
- `.claude/voice/compiled/voice_fingerprint.json` — 同一份統計的完整結構化版本，需要精確數字或 post id 時查這份
- `.claude/voice/compiled/qualitative_sample.json` — 分層抽樣出的原文全文小樣本（近期 + 最長 + 隨機各數十篇，去重），質化維度分析只讀這份
- `.claude/voice/brand_voice.md` — 最終輸出的風格檔

這個目錄預設被 `.gitignore` 排除（見下方「安裝時順手做的事」），因為原始貼文與認知層分析內容偏私人，這是公開的部落格 repo，不該被 commit 上去。

## 執行流程

### Step 1：確認/解析語料

1. 用 Glob 找 `.claude/voice/threads_corpus.json` 是否已存在且夠新。
2. 不存在的話，問使用者 Meta 官方資料匯出檔（zip 解壓後的資料夾或直接的 JSON/HTML 檔）放在哪，然後執行：
   ```bash
   python .claude/skills/threads-voice/scripts/parse_threads_export.py \
     --input <使用者匯出資料夾路徑> \
     --output .claude/voice/threads_corpus.json
   ```
3. 腳本若回報「找不到 Threads 資料」或「沒有解析到任何貼文」，把它印出的頂層 key 貼給使用者確認匯出格式，必要時手動調整 `scripts/parse_threads_export.py` 裡 `extract_post_from_json` 認得的 key 清單（Meta 匯出格式偶爾會變動，不同語言/地區帳號的欄位命名也可能不同）。
4. Bash 讀貼文總數（`python3 -c "import json;print(len(json.load(open('.claude/voice/threads_corpus.json'))['posts']))"`），不要用 Read 工具整包讀進 context。

### Step 2：蒸餾成量化摘要 + 質化樣本（額度控管的關鍵一步）

不管語料大小，一律先跑蒸餾腳本，不要跳過：

```bash
python .claude/skills/threads-voice/scripts/build_voice_fingerprint.py \
  --corpus .claude/voice/threads_corpus.json \
  --output-dir .claude/voice/compiled \
  --sample-size 15
```

貼文數很多（例如 300+）可以把 `--sample-size` 調小到 10；貼文數不到 60 篇時可以調到 20，讓質化樣本盡量涵蓋全部。

用貼文總數分級，如實告知使用者，分析深度跟著調整：

| 等級 | 貼文數 | 可以說的話 |
|------|--------|-----------|
| 資料太少 | < 5 | 「僅供參考，樣本太小，看不出穩定模式」 |
| 偏薄弱 | 5–9 | 「看得出一點傾向，但信心不高」 |
| 堪用 | 10–19 | 「基準堪用，但對離群值敏感」 |
| 穩定 | 20–49 | 「可信度不錯的工作基準」 |
| 深入 | 50+ | 「可以做細部交叉分析（如語氣 × 時段）」 |

< 5 篇時仍可產出 `brand_voice.md`，但每一段都要標「資料太少」，不要假裝有把握。這種資料量太小的情況，質化樣本基本上就是全部貼文，可以直接 Read `.claude/voice/threads_corpus.json` 省一次腳本呼叫。

### Step 3：15 維度分析（分兩軌，控制讀取量）

依 `references/analysis-dimensions.md` 逐一分析，但讀取順序固定：

1. **先 Read `.claude/voice/compiled/voice_fingerprint.md`。** 維度 1（句構）、10（段落節奏）、12（口頭禪清單）主要靠這份的統計直接寫結論，不用再去翻原文——腳本算出的次數本身就是證據。
2. **只在需要精確數字/特定 post id 時才 Read `voice_fingerprint.json`**（不要整份塞進分析，用 Grep 查特定欄位）。
3. **再 Read `.claude/voice/compiled/qualitative_sample.json`。** 維度 2–9、11、13–15（語氣切換、情緒表達、幽默、認知層信念等需要判斷力的部分）用這份樣本原文分析。**不要 Read `.claude/voice/threads_corpus.json` 全文**——樣本已經涵蓋近期、最長、隨機三個角度，如果分析到一半覺得樣本不夠，先跟使用者說明理由，再決定要不要擴大 `--sample-size` 重跑 Step 2，而不是直接讀整包語料。

每個維度：

- 至少找 2–3 個原文例子佐證重要結論（量化維度可以直接引用 fingerprint 裡的次數 + 範例）
- 標「近期穩定」或「僅見於早期」（fingerprint 的「時期分佈」段落已經算好）
- 資料不足就寫「此維度資料不足，暫略」，不要腦補

第 15 維（認知層：核心信念與判斷框架）是把「風格輪廓」推進到「這個人怎麼想」的關鍵，`voice_fingerprint.md` 的「認知層信念候選句」提供起點候選句，但實際歸納成信念/張力/判斷框架要靠 Fable 讀質化樣本後判斷，資料夠的話不要跳過。

### Step 4：輸出 brand_voice.md

依 `references/file-template.md` 的模板與重跑保留規則寫入 `.claude/voice/brand_voice.md`：

1. 檔案已存在 -> 先讀一遍，保留 `## 使用者手動修正` 整段與其他看起來是使用者手寫的內容，覆寫前給使用者看 diff 摘要並確認。
2. 覆寫前備份：把舊檔複製一份到 `.claude/voice/brand_voice.md.bak-<ISO 時間戳>`（格式 `20260711T063000Z`），備份失敗就中止寫入並告知使用者。
3. 寫入新內容。

### Step 5：完成回報

依 `references/file-template.md` 的「完成回報」段落回報，重點：

- 分析了幾篇貼文、資料量等級
- 挑 2–3 個最明顯的風格特徵，各附一段原文
- 明確說明這是**第一版草稿**，需要使用者讀過、修正
- 指出最需要使用者補充的段落（禁忌用語、「這不是我」的例子）
- 邀請使用者回饋修正

## 安裝時順手做的事（只需做一次）

如果 `.gitignore` 裡還沒有 `.claude/voice/`，主動加上去（比照現有的 `scripts/classified_posts.json` 個人資料排除慣例），並告知使用者已加入。

## 邊界提醒

- 這個 skill 只做萃取，不做套用。要拿 `brand_voice.md` 寫新文章時，使用者會手動貼上來或直接引用檔案路徑，不在這個 skill 的範圍內。
- 不做互動數據加權（讚數/瀏覽數），因為 Meta 官方帳號匯出不含這些欄位。
- 貼文若被判定為回覆（有 `parent`/`in_reply_to` 等欄位）會被 parser 過濾掉，只分析原創貼文。
