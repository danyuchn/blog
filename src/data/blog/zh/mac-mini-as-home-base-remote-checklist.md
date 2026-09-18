---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-13T04:00:00Z
title: 出國前的遠端連線檢查表：把 Mac Mini 留在家當本體
slug: zh/mac-mini-as-home-base-remote-checklist
featured: false
draft: false
tags:
  - claude-code
  - codex
  - remote-work
description: '出國前一次寫下的八條遠端配置檢查表：Tailscale、Herdr、咖啡因防休眠、自動重開機、遠端存取，把留在家中的 Mac Mini 當成 Claude/Codex 的 harness 本體。'
---

明天是買了 Mac Mini 後第一次出遠門出國旅行。以下記錄一下出門前的遠端配置檢查表：

1. Tailscale確定內網都有連接且握手成功，Mosh/SSH協定都打通
2. Mac Mini使用咖啡因指令保持常駐不休眠
3. 設置意外關機自動重開機模式
4. Herdr常駐，且配置好machine模式，可以在其他內網裝置連進同一個herdr server
5. 在筆電的Finder、手機的檔案App中設置好可以存取內網中Mac Mini資料夾
6. 提前刷新Claude/Codex 的登入 token
7. 隨身帶的筆電、手機有裝可以連回家裡的遠端桌面救急
8. 想辦法教會還在家的女友怎麼幫忙reboot電腦跟路由器（？？

隔天實測：目前 tailscale + herdr 遠端連回家中的 codex，一切正常。真是有趣的體驗。

會這樣折騰，是因為出遠門旅行，但是筆電容量不足，harness跟排程也都在家中的mac mini。跟之前寫的[旅館出門吃飯前的五步備援 SOP](/blog/posts/zh/ipad-workflow-robustness)不一樣，那篇是人還在台灣、出門吃頓飯的短暫備援；這次是整個人離開這座城市，Mac Mini 要撐好幾天當本體。

<!--
新增非原文句子清單（忠實度自首）：
1. 「跟之前寫的[出門吃飯前，讓 Claude Code 在旅館背景偷跑的五步 SOP]不一樣，那篇是人還在台灣、出門吃頓飯的短暫備援；這次是整個人離開這座城市，Mac Mini 要撐好幾天當本體。」 — 類型：框架句（依派工指示新增的唯一允許框架句，點出與既有文章的差異並附連結）
-->
