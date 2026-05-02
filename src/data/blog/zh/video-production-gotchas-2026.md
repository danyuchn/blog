---
title: "自動化影片製作管道：2026 年四月踩過的九個坑"
slug: "zh/video-production-gotchas-2026"
pubDatetime: 2026-05-01T04:00:00Z
description: "用 Remotion、ffmpeg、yt-dlp、SiliconFlow ASR、YouTube API 自動化影片製作流程，四月份踩到的九個具體 bug 與解法。"
tags: [ffmpeg, Remotion, 自動化, 踩坑, YouTube]
featured: false
draft: false
---

我們頻道的影片製作管道幾乎全部用 code 跑：Remotion 做動畫、ffmpeg 後製合版、SiliconFlow ASR 轉字幕、yt-dlp 下載素材、YouTube Data API 自動上傳。好的時候一部影片從腳本到上傳不用人工介入，壞的時候就是這篇文章的內容。

以下是四月份遇到的九個坑，照踩到的時間順序排。

---

### 1. YouTube Analytics API 維度命名和 UI 不一樣

API 回傳的 `insightTrafficSourceType` 值和 Studio UI 上看到的名稱對不起來。比如 Studio 顯示「訂閱者」，API 裡是 `SUBSCRIBER`；Studio 顯示「頻道頁」，API 卻可能是 `YT_CHANNEL_PAGE`。

加上 Analytics API 本身有 **48–72 小時的延遲**，剛跑腳本看到數字很低，以為是 bug，其實是資料��沒進來。

查的時候先跑這個確認 dimension 的實際值：

```bash
curl "https://youtubeanalytics.googleapis.com/v2/reports?ids=channel==MINE&metrics=views&dimensions=insightTrafficSourceType&startDate=2026-04-01&endDate=2026-04-30&key=$YT_KEY"
```

---

### 2. ffmpeg drawbox 靜態框要分時間戳

想在影片特定段落加靜態注解框，用 drawbox filter。問題是如果你把多個 drawbox 串在一個 filter_complex 裡、沒有分別加 `enable='between(t,start,end)'`，渲染結果會出現框疊錯位或在不應該出現的時間點閃出來。

正確做法：每個框獨立一個 drawbox，各自指定時間範圍：

```bash
ffmpeg -i input.mp4 \
  -vf "drawbox=x=10:y=10:w=200:h=50:color=red@0.5:enable='between(t,2,5)', \
       drawbox=x=10:y=80:w=200:h=50:color=blue@0.5:enable='between(t,8,12)'" \
  output.mp4
```

---

### 3. Remotion render 輸出是 yuvj420p，上傳 YouTube 顏色偏

Remotion 預設 render 出來的 pixel format 是 `yuvj420p`（full-range），YouTube 的 pipeline 會把它當 `yuv420p`（limited-range）處理，結果顏色偏亮偏淡。

在 render 完後加一步轉碼：

```bash
ffmpeg -i remotion_output.mp4 -c:v libx264 -pix_fmt yuv420p -c:a copy final.mp4
```

這步也可以順便做 LUFS 標準化（`-13 LUFS` 是 YouTube 建議值），一起處理。

---

### 4. ffmpeg aselect 超過百個 between() 直接 OOM

想從一段音檔裡切出 218 個片段，想說用 aselect 一次搞定：

```bash
ffmpeg -i input.mp3 -af "aselect='between(t,0.5,1.2)+between(t,3.1,3.8)+...'" output.mp3
```

218 個 `between()` 讓 ffmpeg 在 filter graph 初始化階段就 OOM 崩掉。

解法是把切點寫成 segment list 檔，用 ffmpeg segment muxer 或用 Python 分批跑，每批不超過 20 個 segment。

---

### 5. SiliconFlow ASR word-level timestamp 欄位全空

呼叫 SiliconFlow 語音識別 API，設定回傳 word-level timestamp，拿到的 response 裡 `segments` 和 `words` 是空 list，只有頂層 `text` 有內容。

不是你的 code 寫錯，是部分 model（尤其是快速版）不支援 word-level，只支援 utterance-level。看文件確認 model 的 capability，或切換到 Whisper large-v3 類的完整版本。

---

### 6. set -e 配 Remotion render 會誤觸提前中止

Batch 腳本開頭 `set -e`，然後：

```bash
npx remotion render MyComp output.mp4
ffmpeg -i output.mp4 ...
```

問題在 Remotion render 過程中會把未完成的 mp4 先寫出來，下一行 ffmpeg 讀到不完整的檔案，exit code 非零，set -e 直接把整個腳本殺掉。

解法一：Remotion render 完成後再接 ffmpeg（用 `&&` 而非換行分隔）。解法二：render 那行改成 `set +e; npx remotion render ...; set -e`，讓 render 結果自己判斷。

---

### 7. pgrep 偵測 Remotion 時自我引用死鎖

等待 render 完成常見的寫法：

```bash
while pgrep -lf "remotion render"; do sleep 10; done
```

這個 while loop 的 shell process 本身 argv 就含有 `"remotion render"`（整行命令），`pgrep -lf` 會永遠匹配到這個 shell process 自己，死鎖不會結束。

正確做法有三種：

```bash
# 1. 錨定前綴，只匹配 node 程序
pgrep -f '^node.*remotion'

# 2. 記住 PID，等它消失
npx remotion render & PID=$!; wait $PID

# 3. 監控產出檔大小趨於穩定
```

---

### 8. yt-dlp 繁體中文字幕的 language code 不固定

用 `--sub-lang zh-Hant` 下載字幕，但實際 YouTube 上的字幕 language tag 可能是 `zh-Hant`、`zh-TW`，或是自動生成的 `zh-Hant-RsSZZSfhlqk`（後面帶一串隨機 hash）。

無法硬編碼，要先用 `--list-subs` 看清楚再下：

```bash
yt-dlp --list-subs "https://www.youtube.com/watch?v=VIDEO_ID"
# 然後用實際的 code
yt-dlp --sub-lang zh-Hant-RsSZZSfhlqk --write-sub --no-download ...
```

---

### 9. YouTube Data API caption quota 每天只有 10,000 units

一般 YouTube Data API 的每日 quota 是 10,000 units，caption 相關操作（captions.list、captions.download）每次都算 quota。

跑 batch 腳本前先確認剩餘額度，不然半夜跑完 quota，隔天早上整個 pipeline 都卡住，而且 quota 在 PDT 午夜（台灣隔日下午兩點）才 reset。

---

踩坑是自動化流程的必要成本，但只要每次遇到就記下來，第二次就省了很多時間。這份清單之後還會繼續長。
