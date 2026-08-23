---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-15T09:00:00Z
title: "YouTube API 大檔上傳卡死實測——216 MB 過 / 257 MB 不過，門檻約在 220-250 MB"
slug: zh/youtube-large-upload-216-257mb
featured: false
draft: false
tags:
  - youtube
  - video-production
  - api-debugging
description: 5/13 兩支影片用 YouTube Data API 上傳實測：216 MB 的法律 MCP 示範片成功、257 MB 的 AI 求職示範片卡死。同樣的 googleapiclient resumable upload，差別在檔案大小跟解析度。門檻約在 220-250 MB 之間。
canonicalURL: https://www.agentcrew.cc/blog/posts/zh/automated-video-pipeline-gotchas
---

這篇已經併入 [自動發片管道正在悄悄漏成品：Remotion、ffmpeg、YouTube API、HyperFrames 的踩坑總表](/blog/posts/zh/automated-video-pipeline-gotchas)，原本的內容完整保留在那一篇裡，之後也只會在那裡更新。
