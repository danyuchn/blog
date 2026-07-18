---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-10T04:00:00Z
title: 不要用 AI 的摘要驗收 AI
slug: zh/dont-grade-ai-by-its-summary
featured: false
draft: false
tags:
  - ai-workflow
  - case-study
  - lessons-learned
description: "這週反覆踩到同一類錯誤：agent 說沒改檔卻留下檔案、commit message 與 diff 不符、逐字稿說話人中途漂移。驗收必須回到原始狀態。"
---

派出的「掃逐字稿找遺漏」agent，prompt 明講唯讀禁編輯，卻意外寫入一個 xlsx 練習檔，而且在回報中說「沒有修改任何檔案」。靠 `git diff --stat` 抓到非預期變更，再用 mtime 對上該 agent 的執行時間，才確認是它做的。

教訓：唯讀約束要用工具層級保證，不能只靠 prompt 文字；agent 自報「沒有做 X」也要驗證，不能因為是負向陳述就假設可信。

## Commit message 與實際 diff

今早 commit 的訊息寫「reorder the opening flow」，但實際 diff 顯示只重排了 HTML deck 與 cue card。繁中 prep 稿只改了一行 prompt 文字，順序完全沒動，直到晚上重新核對才發現脫鉤。

教訓：commit message 的變更聲明要對照實際 diff 驗證，不能只信文字描述；多份平行文件各自獨立維護時，任何一次「重排」都要逐檔核對是否同步。

## 同一個說話人編號中途換人

Tencent 智能紀要的說話人標記在通話中途會漂移。Sam 說完要離開會議後，同一個「說話人 3」被系統重新分配給晚點才深度發言的 Sho，導致我最初把 Sam 的發言誤植給 Sho。

教訓：同一編號中途換人，肉眼掃過去不會發現。不能只憑逐字稿標記做人物歸屬，需搭配內容邏輯或請當事人確認。

## 獨立覆核的結論也要覆核

獨立 agent 覆核 A-2 教案時抓到一處實質錯誤，也另外主張整場含真實資料段落都有錄影、牴觸既定資料界線。Dustin 事後確認後一項主張錯誤：全程在 Ray 個人電腦操作，未錄影，不涉及合規界線問題。

教訓：獨立 agent 的「抓到錯誤」本身也可能是錯的。尤其涉及合規、錄影這類高風險斷言，推論不能直接當作 ground truth 寫入 SSOT，仍需當事人確認才能定案。

同一個主題後來也拍成影片：<https://youtu.be/d5Ipmp6RSJ0>

<!--
新增非原文句子清單（忠實度自首）：
無。只從 daily note 原文刪減、拼接與調整指稱。
-->
