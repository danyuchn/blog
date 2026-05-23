---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-23T04:30:00Z
title: "iPad 跑 Claude Code 全攻略——tmux + Tailscale + Moshi"
slug: zh/ipad-claude-code-setup
featured: false
draft: false
tags:
  - claude-code
  - remote-work
  - ipad
description: '用 iPad 11 吋成功運行 Claude Code 的完整方案：tmux 保持 session、Tailscale 穿 NAT、Moshi 做 SSH 終端。目標是重建九成生產力，不只是修 bug。'
---

成功搞定，用 tmux + Tailscale + Moshi 在 iPad 11 吋上安穩運行 Claude Code。

![iPad 上運行 Claude Code 的實拍](/blog/assets/posts/ipad-claude-code-setup/ipad-claude-code-tmux.jpg)

## 為什麼不用遠端桌面？

試過 Jump Desktop、VNC、各種 remote control 方案。不怎麼舒服。遠端桌面的問題是延遲感明顯，操作不流暢，而且耗電比 SSH 多很多。

我的目標不是在 iPad 上「看到」Mac 的畫面來修個 bug，而是在 iPad 上重建九成的生產力。大多數使用場景是非編程的——寫文件、跑 agent、管理知識庫——不需要看 diff。

## 三件套組合

### Tailscale——穿 NAT 零設定

Tailscale 建立 WireGuard mesh network，不管 iPad 和 Mac Mini 在哪個網路環境下，都能直連。不用動路由器、不用開 port、不用搞 DDNS。裝好登入同一帳號就完事。

### Moshi——CJK 友善的 SSH 終端

iPad 上的 SSH app 試過好幾個。Termius 介面漂亮但 CJK rendering 有 bug，中文字顯示會跑掉。Blink Shell 也是選項，但 Moshi 在 CJK 支援上最穩定。

Moshi 的另一個優勢是它用 UDP 協定，在不穩定的網路環境下（咖啡店、機場）比傳統 SSH 更不容易斷線。

### tmux——session 不死

tmux 確保 SSH 斷線後 session 還活著。iPad 切到其他 app 再切回來，或者網路短暫中斷，重新連上就回到原本的工作狀態。搭配 Claude Code 的長時間 agent 任務，tmux 是必備的。

## 日常工作流

1. iPad 打開 Moshi，透過 Tailscale IP 連上 Mac Mini
2. `tmux attach` 接回 session
3. 在 tmux 裡開 Claude Code，正常工作
4. 需要多個 pane 就 tmux split，一邊跑 agent 一邊看 log

耗電量比遠端桌面少很多，iPad 可以撐一整個下午。

## 下一步

接下來要測試 Codex CLI 和 Cursor CLI 在這個環境下的支援程度。另外在等 Mac Mini M4 Pro 到貨，到時候本地算力會更充裕。

順帶一提，國外還有神人摸索出了在 Tesla 車機連 Claude Code 的用法。這個世界真的什麼人都有。
