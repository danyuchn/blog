# 文章起手模板

<!-- 使用方式：
1. 複製對應語言的 frontmatter 區塊到新檔 src/data/blog/{zh,en}/<slug-basename>.md
2. 把全大寫 placeholder 全部替換（搜 "◄" 確認沒漏）
3. 規則細節見 .claude/specs/article-spec.md；tag 只准用 .claude/specs/tags.md 白名單
4. 本模板檔在 content 目錄之外，不會被建置撈到；不要把本檔的說明文字複製進文章
-->

## zh 版（先寫）：`src/data/blog/zh/SLUG-BASENAME.md`

```yaml
---
author: Dustin Yuchen Teng
pubDatetime: YYYY-MM-DDT04:00:00Z # ◄ 必須是已過去的日期；時間固定 T04:00:00Z（曼谷 11:00）
title: 中文標題 # ◄ 含半形「: 」時整值用雙引號包
slug: zh/SLUG-BASENAME # ◄ 必須 = zh/ + 檔名去 .md
featured: false
draft: false
tags: # ◄ 2–3 個，只准用 tags.md 白名單
  - TAG-1
  - TAG-2
description: '一句話描述，35–90 字，無條件單引號包住，內部單引號寫成'' ' # ◄
---
```

## en 版（zh 完成後翻譯）：`src/data/blog/en/SLUG-BASENAME.md`（檔名必須與 zh 完全相同）

```yaml
---
author: Dustin Yuchen Teng
pubDatetime: YYYY-MM-DDT04:00:00Z # ◄ 與 zh 版相同
title: "English Title" # ◄ 含半形「: 」時雙引號包
slug: en/SLUG-BASENAME
featured: false
draft: false
tags: # ◄ 與 zh 版完全相同
  - TAG-1
  - TAG-2
description: 'One-line description, single-quoted unconditionally.' # ◄ 在地化翻譯，不逐字直譯
---
```

## 內文骨架

- 短敘事文：不用任何 `##` 標題，純段落＋圖片，段落 2–5 句第一人稱。
- 長文：只用 `##` 分節（不用 `#`、幾乎不用 `###`）。
- 圖片：`![完整描述句](/blog/assets/posts/SLUG-BASENAME/1-name.jpg)`（目錄名無語言前綴，zh/en 共用；一律 .jpg）。
- 結尾短促收束。禁 `## 小結`、禁排比喊話收尾。

## 文末自首註解（社群貼文改寫文必留；原創文可省略）

```html
<!--
新增非原文句子清單（忠實度自首）：
1. 「〔句子原文〕」 — 類型：框架句 / 銜接 / 改寫
2. …（每一句 AI 新增、原貼文沒有的句子都要列）
-->
```
