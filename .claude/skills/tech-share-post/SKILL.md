---
name: tech-share-post
description: 把作者自己做的工具、外掛、流程寫成技術分享長文（痛點、實測、提示詞、附錄加圖與影片、中英雙語）。觸發語：寫一篇開發分享文、把這個工具寫成部落格、技術分享文、開發心得文、tech share post。
---

# tech-share-post

成品長相以 `.claude/specs/tech-share-post-spec.md` 為準，圖片規格以 `article-spec.md`「主動配圖」為準。本檔只管流程。
範本文章：`src/data/blog/zh/work-mode-ai-working-modes.md`（約 2 小時從 /goal 到上線）。

## 流程

1. **確認素材**：量化資料的分析檔（或先請 AI 用對話紀錄量一次）、作者原話出處（session id）、原始碼路徑。缺哪個先補，不自創數字。
2. **寫 brief**：複製 `references/brief-template.md`，把括號換成這篇的內容，存成 `.claude/tmp-brief-<名>.md`（不 commit，完成後刪）。多個寫手時一份 brief 一個任務。
3. **載入風格**：寫手先載入 `threads-voice`（正式語氣）與 `ui-visual-defaults`（圖與影片），再讀 `article-spec.md`、`tags.md`、`templates/article.md`。
4. **寫 zh 草稿**（`draft: true`，在 feature 分支，不 push）。原話逐字、數字只用素材。
5. **保守潤稿**：用 `references/agy-prompts.md` 的潤稿提示詞交給 agy；回來後用腳本比對數字集合、`>` 引言行、程式碼區塊、圖片與 video 行都沒變，再手改 agy 加的贅語。
6. **風格自檢**：`python3 ~/.claude/skills/threads-voice/scripts/check_draft.py check --acct 主帳 --mode 資訊 <稿>`，「必改」照改。
7. **英文版**：用 `references/agy-prompts.md` 的翻譯提示詞，寫手核對數字、引言、程式碼；不另跑 humanizer。
8. **圖與影片**：圖用 `.claude/figure-kit/`（720px、最小 15px、en 圖不得有中文）；影片見 `.claude/figure-kit/video/README.md`。每張成品自己 Read 一次確認沒破版。
9. **技術附錄**（可另派一個寫手）：brief 要求以原始碼為準、回報每個技術陳述的 檔案:行；圖至少時序、流程、狀態各一。
10. **驗收**：`npm run check:private`、`npm run check:content`、`npm run build`；本地開頁面截整頁圖看圖與影片載入。
11. **作者審稿**：以 `draft: true` 給作者看，依回饋改（作者常見回饋：拿掉對讀者沒用的歷史、要更多技術與圖、圖字太小、en 圖不得有中文）。
12. **發布**：作者明說後改 `draft: false`、pubDatetime 設已過去時間、push、等 CI、curl 驗證線上網址；查舊文是否主題重複；寫回 KB 主檔。

## 派寫手的注意

- 暫存檔、影格放 `mktemp -d`，不要 `rm` repo 內的東西。
- 圖片複製與最終 commit 由主對話做（見 content-workflow fan-out 協議）。
- 回報固定三段：產出清單、每個數字與引言的出處、沒把握的地方。
