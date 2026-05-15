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
---

5/13 後製兩支影片要上 YouTube：

- 5/10 講座剪出的「AI 求職示範」片段：8m27s，**257 MB**，2010×1080
- 法律 MCP 示範片：7m05s，**216 MB**，1658×1080

兩支都跑同一條 pipeline：ffmpeg 兩段式 loudnorm 到 -13 LUFS / TP -1（已是 yuv420p + bt709 免色域轉）→ opencc s2twp 簡轉繁 → Remotion 縮圖 → `googleapiclient` resumable upload。

結果一個成、一個不成。

## 失敗案例：AI 求職示範片（257 MB）

試了兩種 API 上傳路徑：

1. **curl 單發 resumable PUT**
2. **Python `googleapiclient` chunked resumable PUT**（8 MB 一塊 + ACK）

兩次都 `uploadStatus=uploaded`，但 `processingStatus` 永遠卡 `processing` 超過 1 小時不動。Studio UI 顯示「Processing will begin shortly」配上傳箭頭 icon。

兩個失敗版本（`7UhRoAvWr-w` 跟 `FP4_8D4vfes`）都已 DELETE。

**暫行 SOP**：放棄 API 上傳，改用 YouTube Studio 手動拖檔。手動上傳幾分鐘內 processing 完成，video ID 變更為 `HcADayRCJMg`。

可能原因（未驗證）：

- ffmpeg `-c:v copy` 後 metadata fragment 不完整
- YT backend 對 2010×1080 非標準寬度處理慢
- 超過某個 MB 門檻會觸發 backend 不同的 processing pipeline

## 成功案例：法律 MCP 示範片（216 MB）

同樣 `googleapiclient` resumable upload（8 MB chunks），這次 `processingStatus=succeeded`。

差異：

- 檔案大小小了 41 MB
- 解析度 1658×1080（仍是非標準寬度，但比 2010 小）

## 結論：門檻約在 220-250 MB 之間

兩支影片的對比讓我把 CLAUDE.md 裡的 SOP 從「> 200 MB 都失敗」修正為「**257 MB 確認失敗，216 MB 確認成功，門檻約在 220-250 MB**」。

實務上的處理方式：

- **< 200 MB**：直接 `googleapiclient` resumable upload，安全
- **200-220 MB**：嘗試 API，失敗就回退到 Studio 手動
- **> 250 MB**：直接走 Studio 手動，不浪費時間在 API

## 順便記的兩個踩坑

### urllib SSL EOF 中途斷線

最早寫 `tools/yt_upload_law.py` 用純 urllib chunked upload，跑到 16 MB 就 SSL EOF。改用 `googleapiclient.MediaFileUpload`，內建 retry 機制，穩定跑完。

**結論**：YouTube 上傳用 `googleapiclient`，不用裸 urllib 或 curl。

### yutu credential parser bug

5/13 嘗試用 [yutu](https://github.com/eat-pray-ai/yutu) 0.10.7 上傳，發現 credential parser 在 `yutu video insert` 階段就崩。報錯：

```
failed to parse client secret: illegal base64 data at input byte 6
```

即使有效 token、不傳 `-c` flag 也一樣崩。整個 yutu 客戶端 init 階段就掛掉。

**Fallback**：完全棄用 yutu，用 curl 打 YouTube Data API resumable upload 三個 endpoint：

1. `POST /upload/youtube/v3/videos?uploadType=resumable` 拿 Location header → PUT bytes
2. `POST /upload/youtube/v3/thumbnails/set` 上傳縮圖
3. `POST /upload/youtube/v3/captions` resumable 上傳字幕

三個都直連。沒有 wrapper，但每一步都可控。

## 為什麼記下這些

如果你也在做影片上傳自動化，這些門檻跟 fallback 都會省你好幾個小時。

我自己這兩週為了搞清楚 257 MB 為何卡死，跑了至少四個版本的 upload script，刪了兩個失敗的影片 ID。最終的結論是：**API 不是萬能的**。當 API 在某個邊界附近表現不穩，最快的做法是接受邊界、退回手動，不要硬鑽。

技術人最容易掉進「我要把它全自動化」的坑。但是商業生產線的價值不在於「100% 自動」，是在於「90% 自動、10% 手動的容錯設計」。這個課我這週又上了一次。
