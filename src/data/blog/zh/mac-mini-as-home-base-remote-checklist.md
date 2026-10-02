---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-13T04:00:00Z
modDatetime: 2026-10-02T01:00:00Z
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

## 補記：出門後的實測與踩坑

從台灣隨便一個飯店的 wifi 到泰國曼谷主機的 tailscale 直連實測數據，實際使用上沒有明顯的延遲。經過河內、台北兩地驗證，確定 Mac mini 主機放曼谷家裡，遠端走 mosh/ssh＋tailscale 內網連回去是穩定且正確的選擇。補充數據：台北某路易莎，一開始走香港中繼，過 1-2 分鐘後成功直連，往返延遲 87～92 ms，平均約 89 ms。

出門前的遠端演練也踩到幾個坑，後來都寫進了手冊：

- Mac mini 開了 FileVault：停電、自動更新或 `sudo reboot` 會停在硬碟解鎖畫面，Tailscale、SSH、AnyDesk 全都連不上。遠端唯一安全的重開方式是 `sudo fdesetup authrestart`，重開後停在登入畫面，要靠 AnyDesk 登入，而且 AnyDesk 要等一到兩分鐘才連得上。
- 重開機後從 SSH 讀不到登入鑰匙圈（`User interaction is not allowed`），git push 要求帳號、gh token 無效，Claude Code 也要重新 /login。用手機執行 `security unlock-keychain` 後三者都恢復，列為每次重開機後的必做步驟。
- 在筆電上遠端打字卡頓，量到 mini 的 Wi-Fi 每秒有約 0.4 秒的延遲尖峰。在 mini 上關掉 AirDrop 與接力後，立刻從平均 130ms 降到 3.6ms。
- SSH 連進來讀不到桌面、文件、下載，要打開「遠端登入 → 允許遠端使用者擁有完整磁碟取用權限」。

<!--
2026-10-02 W41 補記：新增一節，第一段為 09-30 21:33 與 10-01 12:29 兩則 Threads 貼文逐字合併；條列為作者 09-28 工作日誌「踩坑」段刪減改寫（去掉內網位址等細節）。新增非原文句子：小標（框架句）、「出門前的遠端演練也踩到幾個坑，後來都寫進了手冊：」（銜接）。
-->

<!--
新增非原文句子清單（忠實度自首）：
1. 「跟之前寫的[出門吃飯前，讓 Claude Code 在旅館背景偷跑的五步 SOP]不一樣，那篇是人還在台灣、出門吃頓飯的短暫備援；這次是整個人離開這座城市，Mac Mini 要撐好幾天當本體。」 — 類型：框架句（依派工指示新增的唯一允許框架句，點出與既有文章的差異並附連結）
-->
