---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-15T06:30:00Z
title: "Resend 跟 Gmail 寄信工作流踩坑七連——HTML 模板、scheduled_at、Cloudflare、開信率對齊"
slug: zh/resend-gmail-email-pitfalls
featured: false
draft: false
tags:
  - email-marketing
  - resend
  - gmail
  - workflow
description: 這兩週密集用 Resend 批次寄信跟 Gmail draft 兩條路徑做課程通知、講座感謝信、BD outreach。整理七個踩坑：HTML inline style、scheduled_at 不生效、Cloudflare 1010、Click tracking、bad-recipients、Gmail thread 漏看、客製 vs 通用開信率對齊。
---

這兩週密集用 Resend 批次寄信跟 `gog gmail drafts create` 兩條路徑做課程通知、講座感謝信、BD outreach。一共寄出超過 1,400 封，學到的七件事整理在這裡。

## 1. Gmail 會把 `<style>` block 整段砍掉

`gog gmail drafts create --body-html` 本身完全可用，不需要打 Gmail API 原生 endpoint。但是如果 HTML 模板用了 `<style>` block 寫 class-based CSS，Gmail 會把 `<head>` 的 `<style>` 全部 strip 掉。

正解：**table layout + 全 inline style**。我自己的範本放在 `.claude/skills/course-email/references/email-html-template.md`，每次寄信前直接照抄結構。

誤判路徑（不要走）：看到 `gog gmail get` 輸出原始 HTML → 誤以為是 MIME type 錯誤 → 繞去 Python API 建 multipart/alternative → 其實完全多此一舉。

## 2. Resend `scheduled_at` 不見得會生效

我曾經把 Batch 2 設 `scheduled_at: "2026-05-18T09:00:00+07:00"`，結果 5/11 觸發後 Resend 沒有 honour 排程——所有 40 封都在 5/11 03:13 UTC 一起送出，`scheduled_at` 欄位回讀為 null。

收信人在「應該 5/18 才寄」的名單裡卻在 5/12 回信，才讓我發現。

檢查方法：**寄完後用 `GET /emails/{id}` 撈 `scheduled_at` 欄位**，不能信 batch 送出時的 response。如果回讀 null，代表排程沒成功，已經立刻寄出。要重新評估這件事是否會踩到收件人的時間預期。

## 3. Cloudflare 1010 會擋 urllib 預設 UA

5/10 寄 A2 講座感謝信，439 封 batch 全部回 Cloudflare 1010。改 User-Agent header：

```python
"User-Agent": "agentcrew-academy-mailer/1.0"
```

加上去之後 5 batch × 100 全部 Delivered 439/439。Resend 的 SDK 都有預設 UA，但是如果你直接用 `urllib.request.urlopen` 打他們的 API，會被 Cloudflare 認定為 bot。

## 4. Click tracking 預設可能是關的

5/10 寄出講座感謝信之後，我去 dashboard 看 click rate 全是 0%。一開始以為是收件人都不點，後來才發現 Resend 的 click tracking 預設沒開。

到 dashboard → Settings → Tracking → 找到 Click tracking toggle → 點開。**沒有 Save 按鈕**，auto-save 即生效。但這代表你開啟之前寄的所有信件 click 資料都拿不回來。新功能上線前先檢查 dashboard 設定，是這次的教訓。

## 5. Bad-recipients 要建立持久 list

寄了幾批之後，我整理出 11 人 bad list：5 個 typo（譬如 `xxx@hotail.com`、`xxx@gnail.com`）+ 6 個真實 bounce。這個 list 存成：

```
claude-course/official/events/a2-lecture-0510/bad-recipients.json
```

**每次寄信前先做 set 減法**，把 bad list 從目標 list 裡剔除。不然每次都重寄 → 每次都 bounce → 你的 sender reputation 會被慢慢拖垮。

## 6. Gmail sent box 用 `in:sent subject:"..."` 會漏看 reply

這個是 5/13 盤點 BD outreach 才發現的：我用 `in:sent subject:"..."` 搜尋，找到的是「我這側的寄出 + 我這側的回覆 thread」。但是有 4 個收件人是「對方先回信、原始 outreach 是 Resend 寄出（不在 Gmail）」——這種 thread 完全沒進 sent box。

完整盤點要**同時撈 Resend ID 清單 + Gmail `subject:"..." -in:sent` 兩邊比對**。如果你的 outreach 走 Resend 寄、收件人回信進 Gmail，這兩邊的資料完全分開存。

## 7. 客製分流 vs 通用版的開信率對比要等熟成

5/9 L1 課後信通用版（30 封）24hr 開信率 70.0%。5/10 L1 課後信客製分流版（14 封）24hr 開信率 64.3%。表面上看通用反高 5.7pp。

但是兩邊熟成時間不對等——通用累積約 30 小時，客製分流最早才寄出 5-9 小時。這個比較直接拿來下結論是有問題的。

正確做法：**取兩批都熟成滿 24 小時以後**的數據。再加上要排除週末效應（公司信箱在週末本來就低）、time of send 效應（早上 9 點寄 vs 晚上 9 點寄差很多）。客製 vs 通用的真實差異要等至少三批、五批才能看出來。

不要太早下結論。AI 寄信工作流的價值不是一個 metric 立刻拉高，是整個 funnel 的可控性提升。

---

這七件事如果你也在做寄信自動化，建議直接抄走當 checklist。
