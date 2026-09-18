---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-16T04:00:00Z
title: Anthropic 同一週：安全報告翻車，去識別化工具升級完全體
slug: zh/anthropic-two-opposite-moves-week
featured: false
draft: false
tags:
  - security
  - ai-tools
  - anthropic
description: 'Anthropic 同一週做了兩件相反的事：安全報告讓客戶對話隱私翻車，卻也讓我把去識別化工具升級成自動攔截的完全體。'
---

Anthropic 過去這個禮拜真的很好笑，他們同時做了兩件南轅北轍、背道而馳的事情。

第一，他們自以為地發佈了一份安全報告，結果被大家意識到：原來客戶對話你都隨便看啊？結果 Palantir、NVIDIA 都堵藍了。

第二，他們出了功能強大的 Claude Mod，讓我成功把[去識別化工具 pii-guard-tw](/blog/posts/zh/pii-guard-tw)升級成自動攔截的完全體。現在完全不需要手動操作，只要裝上更新後的外掛，從此之後在 A 的伺服器中，模型能看到的只剩下 `<PERSON_1>`、`<TW_MOBILE_1>`、`<TW_ID_1>`，但是送回你眼前的永遠是還原後的真實內容。

機制如圖：

![pii-guard 讓 AI 只看到安全代號、本機自動還原真實內容的三段式去識別化流程](/blog/assets/posts/anthropic-two-opposite-moves-week/pii-guard-flow.jpg)

整個流程分三段。第一段在你自己的電腦上：你的檔案（客戶：陳大文、手機：0912-345-678、身分證：A123456789）跟你輸入的文字，都先經過 pii-guard 在本機自動偵測，換成安全代號，才送到 AI 前。第二段是 Claude 實際看到的內容——它只看得到客戶：`<PERSON_1>`、手機：`<TW_MOBILE_1>`、身分證：`<TW_ID_1>` 這些代號，看不到真實個資，做完工作再把結果送回來。第三段又回到你的電腦：寫回檔案時自動還原成真實內容。你的真實個資，始終留在自己的電腦。

<!--
新增非原文句子清單（忠實度自首）：
1. 「第一，……」「第二，……」— 類型：改寫（把原文編號 1/2 的清單格式改成連貫段落，內容逐句保留，未新增觀點）
2. 「機制如圖：」後「整個流程分三段……你的真實個資，始終留在自己的電腦。」— 類型：改寫（把任務素材中作者自製圖卡的文字說明，改寫成連貫段落，內容全部來自使用者提供的圖卡文字，未新增未表達過的資訊）
3. 「[去識別化工具 pii-guard-tw](/blog/posts/zh/pii-guard-tw)」的超連結標記本身 — 類型：銜接（依編輯指示加入站內連結，指向既有文章 zh/pii-guard-tw）
-->
