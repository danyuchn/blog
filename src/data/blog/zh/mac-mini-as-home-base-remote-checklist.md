---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-13T04:00:00Z
modDatetime: 2026-10-09T00:00:00Z
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

## 出門後的實測與踩坑

從台灣隨便一個飯店的 wifi 到泰國曼谷主機的 tailscale 直連實測數據，實際使用上沒有明顯的延遲。經過河內、台北兩地驗證，確定 Mac mini 主機放曼谷家裡，遠端走 mosh/ssh＋tailscale 內網連回去是穩定且正確的選擇。補充數據：台北某路易莎，一開始走香港中繼，過 1-2 分鐘後成功直連，往返延遲 87～92 ms，平均約 89 ms。

出門前的遠端演練也踩到幾個坑，後來都寫進了手冊：

- Mac mini 開了 FileVault：停電、自動更新或 `sudo reboot` 會停在硬碟解鎖畫面，Tailscale、SSH、AnyDesk 全都連不上。遠端唯一安全的重開方式是 `sudo fdesetup authrestart`，重開後停在登入畫面，要靠 AnyDesk 登入，而且 AnyDesk 要等一到兩分鐘才連得上。
- 重開機後從 SSH 讀不到登入鑰匙圈（`User interaction is not allowed`），git push 要求帳號、gh token 無效，Claude Code 也要重新 /login。用手機執行 `security unlock-keychain` 後三者都恢復，列為每次重開機後的必做步驟。
- 在筆電上遠端打字卡頓，量到 mini 的 Wi-Fi 每秒有約 0.4 秒的延遲尖峰。在 mini 上關掉 AirDrop 與接力後，立刻從平均 130ms 降到 3.6ms。
- SSH 連進來讀不到桌面、文件、下載，要打開「遠端登入 → 允許遠端使用者擁有完整磁碟取用權限」。

<!--
2026-10-02 W41 補記：新增一節，第一段為 09-30 21:33 與 10-01 12:29 兩則 Threads 貼文逐字合併；條列為作者 09-28 工作日誌「踩坑」段刪減改寫（去掉內網位址等細節）。新增非原文句子：小標（框架句）、「出門前的遠端演練也踩到幾個坑，後來都寫進了手冊：」（銜接）。
-->

## 弱網環境：換 mosh 與跨機傳圖

後來把遠端連回家中 Claude Code CLI 的通訊協定，從 SSH 改成 mosh 了，在飯店 Wifi 瘋狂掉封包的情境下，mosh 竟然超級順，太感動了。

不過經 mosh 連進 mini 時，Markdown 連結不變色也點不開（官方 mosh 不轉送 OSC 8）。

另一個問題是傳圖。我的方法是（mini 被操控機，Air 操控機）：

1. 把 Air 剪貼簿裡的圖存成 png（用 pngpaste）
2. 透過 Tailscale 用 scp 傳到 mini 的 /tmp/
3. 把 mini 上的檔案路徑放回 Air 的剪貼簿
4. 你在 Claude Code 裡直接貼上那個路徑，Claude 就讀得到圖

有一些要看東西的部分我還是會搭配 copyparty 這個套件，他是一個蠻好用的網頁式檔案總管，可以在 Tailscale 內網中打開且預覽各式各樣的檔案。

<!--
2026-10-09 W42 補記：第一段為 10-06 23:39 Threads 貼文逐字；第二段為作者 10-07 工作日誌踩坑改寫；條列與末段為 10-07 07:39 Threads 回覆逐字（去掉開頭「我昨天也是在處理圖的問題...不過是傳圖」）。新增非原文句子：小標（框架句）、「另一個問題是傳圖。」（銜接）。
-->

## 遠端點檔案連結與弱網備援

這兩個禮拜出遠門，常常用筆電跟手機遙控家裡的 mac mini 上的 claude code CLI 工作。每次點下去檔案連結發現沒有反應，才想到連結是本機路徑，點下去只會在家裡的 mini 開啟，然後又要匆忙補一句：幫我用 tailscale 在筆電／手機上打開。

後來靈機一動，用 Claude Mod 做了一個切換器：在筆電或手機上的時候就切模式，Mod 會自動把模型輸出的本機路徑攔截轉譯成內網路徑，並注入提示詞：用戶現在在 XX 遠端，如果用戶要求打開檔案，請操作 tailscale 在該遠端執行。

我真是冰雪聰明！

![remote-device Mod 的說明畫面：/at air、/at iphone、/at mini 三種模式，把回覆裡的 file:// 連結改成 copyparty 網址，並提示 Claude 要開檔就 ssh 到 Air 執行 open。](/blog/assets/posts/mac-mini-as-home-base-remote-checklist/1-remote-device-mod.jpg)

另外意外發現 tailscale 的妙用：不小心買到中國節點的旅遊 esim 導致 AI 全 G 時，還可以用 ssh 問 AI。

![手機用 mosh 連回家裡的 Mac mini，請 AI 查釜山的汗蒸幕，回覆照常出現。](/blog/assets/posts/mac-mini-as-home-base-remote-checklist/2-ssh-ask-ai-china-esim.jpg)

有人問要不要讓所有流量都走 exit node。沒有需要。如果是 claude，我擔心有什麼我不知道的裝置指紋，如果跟 vpn 出口地域特徵不一致，會被 flag、被封。所以還是完全讓裝置隱身在後方就好。

<!--
2026-10-16 W43 補記：第一～三段為 10-09 23:30 Threads 貼文逐字；第四段為 10-13 08:51 Threads 貼文逐字（去掉開頭「好好笑，」）；末段為 10-13 16:26 Threads 回覆逐字合併。新增非原文句子：小標（框架句）、「另外」（銜接）、「有人問要不要讓所有流量都走 exit node。」（銜接，原文為回覆他人時的開頭「沒有需要所有流量都走exit node⋯」拆寫）、兩張圖 alt 文字（改寫）。
-->

<!--
新增非原文句子清單（忠實度自首）：
1. 「跟之前寫的[出門吃飯前，讓 Claude Code 在旅館背景偷跑的五步 SOP]不一樣，那篇是人還在台灣、出門吃頓飯的短暫備援；這次是整個人離開這座城市，Mac Mini 要撐好幾天當本體。」 — 類型：框架句（依派工指示新增的唯一允許框架句，點出與既有文章的差異並附連結）

2026-10-26 拼接順稿：
將三個 H2 標題的「補記：」字樣移除改為自然主題標題，並將與前後文矛盾的時間副詞「剛剛」「剛才」調整為「後來」。
-->
