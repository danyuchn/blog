# 出處與授權

本 skill（`scripts/parse_threads_export.py` 的匯出解析邏輯、`references/analysis-dimensions.md` 的 15 維度分析架構、`references/file-template.md` 的輸出模板與重跑保留規則）改作自：

> [akseolabs-seo/AK-Threads-booster](https://github.com/akseolabs-seo/AK-Threads-booster) — `skills/voice/` 模組與 `scripts/parse_export.py`
> Copyright (c) 2026 AK SEO Labs

原專案採 MIT License，全文如下（依授權條款隨改作版本一併附上）：

```
MIT License

Copyright (c) 2026 AK SEO Labs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 與原版的差異

原專案是完整的 Threads 成長駭客系統（演算法訊號、互動預測、發文排程看板等）。本 skill 只保留「從歷史貼文萃取寫作語氣」這一段，並做了以下簡化：

- 拿掉 `algorithm_signals` / `psychology_signals` / `metrics` / `performance_windows` 等成長分析用的欄位 scaffold，語料只留 `id` / `text` / `created_at` / `permalink` / `word_count` / `paragraph_count`
- 拿掉 engagement-weighted（按讚數/瀏覽數加權）的證據分級，因為 Meta 官方帳號資料匯出本身不含互動數據；改為單純「近期 vs 歷史」的時間分級
- 保留了 `build_voice_distillation.py` 的兩階段（腳本統計 + AI 判讀）架構精神，改作成 `scripts/build_voice_fingerprint.py`：拿掉 engagement 相關欄位，把「高互動樣本」改成「近期 + 最長 + 隨機」分層抽樣的 `qualitative_sample.json`，讓 Fable 不用讀整包語料就能做質化分析（見 SKILL.md「額度控管」原則）
- 拿掉整套 `FAILSAFE.md` 五檔案復原機制，只保留「覆寫 `brand_voice.md` 前備份一份」的最小版本
