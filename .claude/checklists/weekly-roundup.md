# 週報執行清單（blog 端）

範圍：**社群匯出素材到手之後 → 等待使用者 commit 指令為止**。
上游步驟（素材盤點四來源、YouTube 掃描時機、匯出申請）屬 `~/knowledge-base/000-weekly-routines.md`，不在本清單重複——knowledge-base 未掛載時提醒使用者。

每週照順序打勾。每步附「怎麼驗證」與「失敗時對策」。

## 1. 分類

- [ ] 跑 `scripts/classify_posts.py`（讀 `/tmp/ig_export`，輸出 `scripts/classified_posts.json`）。
  - 失敗對策：**Threads-only 匯出**（無 IG `posts_1.json`）會報錯 → 跳過腳本，為當週日期範圍寫一次性分類 snippet，不要為單次案例改腳本。
  - Meta 匯出編碼：文字是 latin-1 包 UTF-8，逐欄 `s.encode('latin-1').decode('utf-8')` 修正。
- [ ] **與上週 micro-notes 去重**：匯出視窗頭一兩天的貼文常已收進上週週報，逐條對照上週區段剔除（W25 實例：兩則 Fable 貼文已在 W24 文章中）。

## 2. 聚類提案

- [ ] 聚類後向使用者提案（全跑 vs Top N）。
- [ ] **必須明說每個未選篇章的去處**（micro-notes / 留下週 / 棄寫）——漏說會導致使用者事後追問、補開重做（歷史上發生過 build 跑兩次）。

## 3. 寫作（zh 先行）

- [ ] 每篇從 `.claude/templates/article.md` 起手，遵守 `.claude/specs/article-spec.md`。
- [ ] 多篇並行時：寫手 prompt 用 `.claude/templates/fanout-writer-prompt.md` 生成，**派工前 working tree 清乾淨、圖片由主對話先複製**。
- [ ] 回收：照自首清單逐句裁決忠實度，砍 AI 補述（模板內有完整回收 checklist）。

## 4. 翻譯與去 AI 腔

- [ ] en 版檔名與 zh 完全相同、段落一一對應。
- [ ] en 全部過 `/humanizer` skill。

## 5. Micro-notes 維護（規格：`.claude/specs/micro-notes-spec.md`）

- [ ] 新碎念分流：有可複用洞見 → live；純反應/時效梗 → 2026-archive。
- [ ] live 檔 ≤35 條；超過就聚類抽取成文（同主題 3+ 條）或搬 archive，被吸收條目 zh/en 都刪。
- [ ] zh/en 條目數、順序完全同步。

## 6. 驗證（全綠才算完成）

- [ ] `npm run check:content` — 0 error。有 error 逐條修，不得跳過。
- [ ] `npm run build` — astro check + build + pagefind 全過。
- [ ] `npm run dev` 抽查：新文章出現在首頁列表、翻譯連結（Read in English / 閱讀中文版）正常、圖片正常顯示。
  - 翻譯連結沒出現的第一嫌疑：pubDatetime 是未來時間被 postFilter 過濾（article-spec 陷阱 1）。
  - 出現假 duplicate-id 警告：清 `.astro/` 目錄。

## 7. 收尾

- [ ] 向使用者回報：本週篇數、micro-notes 增刪、build 頁數、驗證證據（check:content 與 build 輸出）。
- [ ] **停在這裡等指令**：使用者明說「commit」/「commit & push」才動 git。commit 逐檔 `git add <path>`，禁 `git add -A`。
- [ ] commit 後更新 memory（MEMORY.md 的週報里程碑一行）。
