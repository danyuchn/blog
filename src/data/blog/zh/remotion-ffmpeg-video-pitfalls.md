---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "用 Claude Code 做教學影片一週踩到的坑——Remotion 動畫與 ffmpeg 後製"
slug: zh/remotion-ffmpeg-video-pitfalls
featured: false
draft: false
tags:
  - ai-workflow
  - developer-experience
  - video-production
description: '這一週做兩部教學影片踩到的製作坑：字幕克制、字級、動畫錨點稽核、Remotion render crash 拆段、安靜旁白正規化、opencc 過度在地化。'
---

這一週做了兩部教學影片：一部是上線的 Ep27，另一部是另一支還在排程的。製作流程都是先錄口白，轉 SRT，再用 Remotion 把動畫鎖到字幕 timing 上，最後用 ffmpeg 接合與正規化。本篇只記製作技術層面反覆被糾正的坑，這些坑下次想第一次就做對。

## 字幕不是逐句鋪上去

第一個反覆被糾正的點：這不是字幕動畫。口白每句都鋪一張字幕，違反克制原則。正確做法是「只放重點」——一個標題加上最多兩個支撐元素。一旦改成這個密度，畫面才不會跟著旁白一句一句被字塞滿。

## 字級要比照投影片 spec

第二個點是字級。Remotion 預設大概 28-32，這個尺寸在手機上看太小。我改成比照投影片的 spec：body 是 2.4rem，約等於 38，影片實際用到 40。

## 砍內容之後一定要重核 timing 錨點

第三個點最容易被忽略：精簡之後務必重核 timing 錨點。問題出在我把內容砍掉，卻留著舊的 fadeIn 錨點，動畫就會早於口白出現。Ep27 有一處 S10e 的 chips 還掛在已經被砍掉的寄信段落上，整整早了 14 秒進場。

抓這種錯，最有效的方法是派多個 subagent 分段稽核，逐一核對「每個進場的 global = sceneStart + X，到底對到哪一句 SRT」。Ep27 一共修了三處動畫早於口白（S1、S10e、S11a）。

## Remotion 超過 10 分鐘含 Video 元件會 render crash

Remotion 在影片超過 10 分鐘、而且 composition 裡含 Video 元件時，render 會 crash，報 ffmpeg 254。

我的繞法是把整片拆開：最終片用一個 `demo` prop 把錄屏排除掉，Remotion 只 render intro 動畫段（`--frames=0-10601`），錄屏那段走 ffmpeg concat 另外接合進來。這樣 Remotion 就不需要在一個 render 裡同時處理超長片加 Video 元件。

## 安靜旁白的正規化：三個坑

另一支影片的 intro 旁白錄得極安靜，量出來 integrated 是 −39 LUFS，峰值只有 −19 dBFS。要拉到 −13，等於要 +26dB，這個增益幅度本身就埋了三個坑。

第一坑：`loudnorm linear=true` 只做線性增益，不會啟動 true-peak limiter，峰值直接衝到 +1.2 dBTP。

第二坑：`loudnorm` 一次硬推 26dB 會破。這不是它設計的範圍，連 dynamic 模式都會 +2 dBTP。

第三坑：`alimiter` 預設 `level=true`，會自動把音量回拉到滿幅，等於把你做的限制抵銷掉，必須改成 `level=false`。

最終解是不走 loudnorm，改用 `volume=29dB,alimiter=level=false:limit=0.63`。

## opencc s2twp 的過度在地化

口白簡轉繁我用 opencc s2twp，它會過度在地化。「荧幕」會被轉成「熒幕」，正確應該是「螢幕」；「权限」會被轉成「許可權」，正確應該是「權限」。轉完字幕一定要 grep 這兩個詞。

---

以上是這一週兩部影片在製作技術上反覆被糾正的點。Ep27 的成片在這裡：[https://youtu.be/9nQe9OYYhP4](https://youtu.be/9nQe9OYYhP4)。
