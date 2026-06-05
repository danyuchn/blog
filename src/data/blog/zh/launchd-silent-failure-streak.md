---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "靜默連敗 8 天：launchd 照常觸發，卻什麼都沒發生"
slug: zh/launchd-silent-failure-streak
featured: false
draft: false
tags:
  - ai-workflow
  - developer-experience
  - case-study
description: '一條每天 09:00 自動發片的本機 pipeline 連敗 8 天，launchd 照常觸發、零告警。記一次從搬檔到 exit 127 的脫鉤排查。'
---

我有一條本機的 `cc-update-pipeline`，每天早上 09:00 由 launchd 觸發，自動產出一支「CC 更新速覽」的 YouTube Short 並上傳。

它連續 8 天什麼都沒做，而我完全沒發現。

## 連敗

時間是 5/26 到 6/2。這段期間沒有任何告警，沒有任何錯誤通知。我以為片子一直在發，直到某天才意識到：這 8 天裡，一支都沒上。

最弔詭的地方是「觸發」和「執行」之間那條被我忽略的縫。launchd 確實有動作，但動作之後的腳本，根本沒跑起來。

## 診斷

我先去看 `launchctl list | grep <label>`，看那個 job 的退出碼。退出碼是 127。

127 是 bash 在找不到要執行的檔案時回的碼。也就是說，launchd 每天 09:00 準時去敲那個腳本，敲的卻是一個已經不存在於該路徑的檔案。它敲了空氣，安靜地記下一筆 exit 127，等明天再敲一次。

## 根因

根因要追回 5/26。那天我把 upload script 搬到了 `tools/` 底下，但 launchd plist 裡 `ProgramArguments` 的路徑還指向舊位置。腳本搬了，plist 沒跟著改——排程照常觸發，bash 找不到檔，靜默 exit 127。

而且不只是 plist 那一層脫鉤。搬完 upload script 之後，我也忘了同步改 `pipeline.sh` 裡引用的路徑，還有 upload script 自己的 `PROMO_DIR`——因為 `Path(__file__).parent` 隨著檔案搬家整個變了，原本相對它推算出來的目錄也跟著錯位。

另外，這段期間有幾天根本連 log entry 都沒有。最可能的解釋是電腦睡眠，導致 launchd 在那幾天連觸發都沒觸發。所以這 8 天的連敗，其實混著兩種沉默：有些天是敲了空氣 exit 127，有些天是電腦睡著、根本沒敲。

## 修復

修法直接：把 plist 裡的路徑改成新位置，reload。退出碼從 127 變回 0。同時補上 `pipeline.sh` 的路徑和 upload script 的 `PROMO_DIR`。

我沒有回補 5/26 到 6/2 那段期間的 v2.1.151 到 161——那些片就讓它過去。從當天 09:00 開始，pipeline 接著最新版繼續跑。

修完路徑、重新 render 的時候又撞上第二顆雷：Remotion 的 composition ID。pipeline 餵進去的是 `${TODAY}`（2026-06-04），但 Root.tsx 註冊的是 `${DATE_COMPACT}`（20260604）。兩個名字對不上，render 直接 crash。改成一致之後，v2.1.161 重新 render 並上傳到 YouTube，排程才算真的活回來。

## 寫在最後

這次連敗 8 天，沒有任何一行紅字救我。launchd 那邊看不出異狀，YouTube 後台沒有失敗任務，因為根本沒有任務送到那裡。整件事最便宜的偵測點，其實就是那句 `launchctl list | grep <label>` 看一眼退出碼——只是我 8 天都沒去看。
</content>
</invoke>
