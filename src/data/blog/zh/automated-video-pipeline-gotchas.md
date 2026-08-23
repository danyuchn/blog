---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-22T04:00:00Z
title: "自動發片管道正在悄悄漏成品：Remotion、ffmpeg、YouTube API、HyperFrames 的踩坑總表"
slug: zh/automated-video-pipeline-gotchas
featured: false
draft: false
tags:
  - video-production
  - gotchas
  - automation
description: '從 Remotion 到 HyperFrames，四個月的影片自動化踩坑合輯：exit 0 的殘檔、靜默截斷的縮圖標題、回 0 行的轉錄合併、卡死的大檔上傳。共同點是全都不報錯。'
---

這條管道最危險的地方不是它會壞掉，是它會安靜地少做一半事情然後回報成功。exit 0 的下載其實是殘檔、`compactTitle()` 把標題砍成半句掛了三十六支、13 段轉錄有 5 段回 0 行合併起來看起來還很完整——這些沒有一個會丟 error 給你。以下按時間順序，從 Remotion 那套一路記到 HyperFrames。

## Remotion 時代：四月的九個坑

我們頻道的影片製作管道幾乎全部用 code 跑：Remotion 做動畫、ffmpeg 後製合版、SiliconFlow ASR 轉字幕、yt-dlp 下載素材、YouTube Data API 自動上傳。好的時候一部影片從腳本到上傳不用人工介入，壞的時候就是這篇文章的內容。

以下是四月份遇到的九個坑，照踩到的時間順序排。

### 1. YouTube Analytics API 維度命名和 UI 不一樣

API 回傳的 `insightTrafficSourceType` 值和 Studio UI 上看到的名稱對不起來。比如 Studio 顯示「訂閱者」，API 裡是 `SUBSCRIBER`；Studio 顯示「頻道頁」，API 卻可能是 `YT_CHANNEL_PAGE`。

加上 Analytics API 本身有 **48–72 小時的延遲**，剛跑腳本看到數字很低，以為是 bug，其實是資料還沒進來。

查的時候先跑這個確認 dimension 的實際值：

```bash
curl "https://youtubeanalytics.googleapis.com/v2/reports?ids=channel==MINE&metrics=views&dimensions=insightTrafficSourceType&startDate=2026-04-01&endDate=2026-04-30&key=$YT_KEY"
```

### 2. ffmpeg drawbox 靜態框要分時間戳

想在影片特定段落加靜態注解框，用 drawbox filter。問題是如果你把多個 drawbox 串在一個 filter_complex 裡、沒有分別加 `enable='between(t,start,end)'`，渲染結果會出現框疊錯位或在不應該出現的時間點閃出來。

正確做法：每個框獨立一個 drawbox，各自指定時間範圍：

```bash
ffmpeg -i input.mp4 \
  -vf "drawbox=x=10:y=10:w=200:h=50:color=red@0.5:enable='between(t,2,5)', \
       drawbox=x=10:y=80:w=200:h=50:color=blue@0.5:enable='between(t,8,12)'" \
  output.mp4
```

### 3. Remotion render 輸出是 yuvj420p，上傳 YouTube 顏色偏

Remotion 預設 render 出來的 pixel format 是 `yuvj420p`（full-range），YouTube 的 pipeline 會把它當 `yuv420p`（limited-range）處理，結果顏色偏亮偏淡。

在 render 完後加一步轉碼：

```bash
ffmpeg -i remotion_output.mp4 -c:v libx264 -pix_fmt yuv420p -c:a copy final.mp4
```

這步也可以順便做 LUFS 標準化（`-13 LUFS` 是 YouTube 建議值），一起處理。

### 4. ffmpeg aselect 超過百個 between() 直接 OOM

想從一段音檔裡切出 218 個片段，想說用 aselect 一次搞定：

```bash
ffmpeg -i input.mp3 -af "aselect='between(t,0.5,1.2)+between(t,3.1,3.8)+...'" output.mp3
```

218 個 `between()` 讓 ffmpeg 在 filter graph 初始化階段就 OOM 崩掉。

解法是把切點寫成 segment list 檔，用 ffmpeg segment muxer 或用 Python 分批跑，每批不超過 20 個 segment。

### 5. SiliconFlow ASR word-level timestamp 欄位全空

呼叫 SiliconFlow 語音識別 API，設定回傳 word-level timestamp，拿到的 response 裡 `segments` 和 `words` 是空 list，只有頂層 `text` 有內容。

不是你的 code 寫錯，是部分 model（尤其是快速版）不支援 word-level，只支援 utterance-level。看文件確認 model 的 capability，或切換到 Whisper large-v3 類的完整版本。

### 6. set -e 配 Remotion render 會誤觸提前中止

Batch 腳本開頭 `set -e`，然後：

```bash
npx remotion render MyComp output.mp4
ffmpeg -i output.mp4 ...
```

問題在 Remotion render 過程中會把未完成的 mp4 先寫出來，下一行 ffmpeg 讀到不完整的檔案，exit code 非零，set -e 直接把整個腳本殺掉。

解法一：Remotion render 完成後再接 ffmpeg（用 `&&` 而非換行分隔）。解法二：render 那行改成 `set +e; npx remotion render ...; set -e`，讓 render 結果自己判斷。

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

### 8. yt-dlp 繁體中文字幕的 language code 不固定

用 `--sub-lang zh-Hant` 下載字幕，但實際 YouTube 上的字幕 language tag 可能是 `zh-Hant`、`zh-TW`，或是自動生成的 `zh-Hant-RsSZZSfhlqk`（後面帶一串隨機 hash）。

無法硬編碼，要先用 `--list-subs` 看清楚再下：

```bash
yt-dlp --list-subs "https://www.youtube.com/watch?v=VIDEO_ID"
# 然後用實際的 code
yt-dlp --sub-lang zh-Hant-RsSZZSfhlqk --write-sub --no-download ...
```

### 9. YouTube Data API caption quota 每天只有 10,000 units

一般 YouTube Data API 的每日 quota 是 10,000 units，caption 相關操作（captions.list、captions.download）每次都算 quota。

跑 batch 腳本前先確認剩餘額度，不然半夜跑完 quota，隔天早上整個 pipeline 都卡住，而且 quota 在 PDT 午夜（台灣隔日下午兩點）才 reset。

## 五月：YouTube API 大檔上傳，216 MB 過、257 MB 不過

5/13 後製兩支影片要上 YouTube：

- 5/10 講座剪出的「AI 求職示範」片段：8m27s，**257 MB**，2010×1080
- 法律 MCP 示範片：7m05s，**216 MB**，1658×1080

兩支都跑同一條 pipeline：ffmpeg 兩段式 loudnorm 到 -13 LUFS / TP -1（已是 yuv420p + bt709 免色域轉）→ opencc s2twp 簡轉繁 → Remotion 縮圖 → `googleapiclient` resumable upload。

結果一個成、一個不成。

### 失敗案例：AI 求職示範片（257 MB）

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

### 成功案例：法律 MCP 示範片（216 MB）

同樣 `googleapiclient` resumable upload（8 MB chunks），這次 `processingStatus=succeeded`。

差異：

- 檔案大小小了 41 MB
- 解析度 1658×1080（仍是非標準寬度，但比 2010 小）

### 當時的結論：門檻約在 220-250 MB 之間

兩支影片的對比讓我把 CLAUDE.md 裡的 SOP 從「> 200 MB 都失敗」修正為「**257 MB 確認失敗，216 MB 確認成功，門檻約在 220-250 MB**」。

實務上的處理方式：

- **< 200 MB**：直接 `googleapiclient` resumable upload，安全
- **200-220 MB**：嘗試 API，失敗就回退到 Studio 手動
- **> 250 MB**：直接走 Studio 手動，不浪費時間在 API

（這條門檻後來被推翻了，見最後一節第 10 點。）

### 順便記的兩個踩坑

最早寫 `tools/yt_upload_law.py` 用純 urllib chunked upload，跑到 16 MB 就 SSL EOF。改用 `googleapiclient.MediaFileUpload`，內建 retry 機制，穩定跑完。結論：YouTube 上傳用 `googleapiclient`，不用裸 urllib 或 curl。

5/13 嘗試用 [yutu](https://github.com/eat-pray-ai/yutu) 0.10.7 上傳，發現 credential parser 在 `yutu video insert` 階段就崩。報錯：

```
failed to parse client secret: illegal base64 data at input byte 6
```

即使有效 token、不傳 `-c` flag 也一樣崩。整個 yutu 客戶端 init 階段就掛掉。Fallback 是完全棄用 yutu，用 curl 打 YouTube Data API resumable upload 三個 endpoint：`POST /upload/youtube/v3/videos?uploadType=resumable` 拿 Location header 再 PUT bytes、`POST /upload/youtube/v3/thumbnails/set` 上傳縮圖、`POST /upload/youtube/v3/captions` resumable 上傳字幕。三個都直連。沒有 wrapper，但每一步都可控。

我自己這兩週為了搞清楚 257 MB 為何卡死，跑了至少四個版本的 upload script，刪了兩個失敗的影片 ID。最終的結論是：**API 不是萬能的**。當 API 在某個邊界附近表現不穩，最快的做法是接受邊界、退回手動，不要硬鑽。

技術人最容易掉進「我要把它全自動化」的坑。但是商業生產線的價值不在於「100% 自動」，是在於「90% 自動、10% 手動的容錯設計」。

## 六月：Remotion 動畫與 ffmpeg 後製

這一週做了兩部教學影片：一部是上線的 Ep27，另一部是另一支還在排程的。製作流程都是先錄口白，轉 SRT，再用 Remotion 把動畫鎖到字幕 timing 上，最後用 ffmpeg 接合與正規化。這一節只記製作技術層面反覆被糾正的坑。

### 字幕不是逐句鋪上去

第一個反覆被糾正的點：這不是字幕動畫。口白每句都鋪一張字幕，違反克制原則。正確做法是「只放重點」——一個標題加上最多兩個支撐元素。一旦改成這個密度，畫面才不會跟著旁白一句一句被字塞滿。

### 字級要比照投影片 spec

第二個點是字級。Remotion 預設大概 28-32，這個尺寸在手機上看太小。我改成比照投影片的 spec：body 是 2.4rem，約等於 38，影片實際用到 40。

### 砍內容之後一定要重核 timing 錨點

第三個點最容易被忽略：精簡之後務必重核 timing 錨點。問題出在我把內容砍掉，卻留著舊的 fadeIn 錨點，動畫就會早於口白出現。Ep27 有一處 S10e 的 chips 還掛在已經被砍掉的寄信段落上，整整早了 14 秒進場。

抓這種錯，最有效的方法是派多個 subagent 分段稽核，逐一核對「每個進場的 global = sceneStart + X，到底對到哪一句 SRT」。Ep27 一共修了三處動畫早於口白（S1、S10e、S11a）。

### Remotion 超過 10 分鐘含 Video 元件會 render crash

Remotion 在影片超過 10 分鐘、而且 composition 裡含 Video 元件時，render 會 crash，報 ffmpeg 254。

我的繞法是把整片拆開：最終片用一個 `demo` prop 把錄屏排除掉，Remotion 只 render intro 動畫段（`--frames=0-10601`），錄屏那段走 ffmpeg concat 另外接合進來。這樣 Remotion 就不需要在一個 render 裡同時處理超長片加 Video 元件。

### 安靜旁白的正規化：三個坑

另一支影片的 intro 旁白錄得極安靜，量出來 integrated 是 −39 LUFS，峰值只有 −19 dBFS。要拉到 −13，等於要 +26dB，這個增益幅度本身就埋了三個坑。

第一坑：`loudnorm linear=true` 只做線性增益，不會啟動 true-peak limiter，峰值直接衝到 +1.2 dBTP。

第二坑：`loudnorm` 一次硬推 26dB 會破。這不是它設計的範圍，連 dynamic 模式都會 +2 dBTP。

第三坑：`alimiter` 預設 `level=true`，會自動把音量回拉到滿幅，等於把你做的限制抵銷掉，必須改成 `level=false`。

最終解是不走 loudnorm，改用 `volume=29dB,alimiter=level=false:limit=0.63`。

### opencc s2twp 的過度在地化

口白簡轉繁我用 opencc s2twp，它會過度在地化。「荧幕」會被轉成「熒幕」，正確應該是「螢幕」；「权限」會被轉成「許可權」，正確應該是「權限」。轉完字幕一定要 grep 這兩個詞。

Ep27 的成片在這裡：[https://youtu.be/9nQe9OYYhP4](https://youtu.be/9nQe9OYYhP4)。

## 八月：整條流水線換成 HyperFrames 之後的十一個坑

[後來整條流水線換成 HyperFrames](/blog/posts/zh/ai-video-pipeline-codex-to-claude)，坑也整批換新。以下是八月這一週做一支混合片（動畫覆蓋加錄屏 pass-through）時踩到的，一個坑一節。

### 1. 轉場閃動＝切換點沒被遮罩蓋住

wipe 排在 `B-0.6～B`，紅幕在切換前 0.3 秒就滑走了，那一刀其實是裸切，畫面就閃一下。修法是把切點移進全遮窗：`B-0.35` 進場、`B±0.05` 停留、`B+0.35` 離場，停留 0.10 秒才能保證 30fps 下至少三幀全滿。更早那支片沿用的是同一套錯誤時序。

### 2.「純動畫必須單 worker」是 Remotion 的規則，不是 HyperFrames 的

在 Remotion 上訂的這條規則照套過來，render 慢五到八倍。實測 8 worker 下靜止動畫的相鄰幀比對差異像素是 0，並拿轉場的動態幀做反向對照，確認檢查器會動。5.9 萬幀約 22 分鐘跑完。

### 3. `.term` / `.codefile` 會靜默切掉最後一行

這兩個都是 flex child，會被 `scene-content` 壓縮，加上 `overflow: hidden` 就把最後一行吃掉，畫面上看起來只像「貼底」。修法是 `flex-shrink: 0`，加上之後真正過滿的那幾幕才會浮現。`hyperframes check` 只抽 9 幀不保證抓得到，要用 `hyperframes snapshot --zoom "<selector>"` 對元素本身放大驗。

### 4. preview 跑著的時候不要用 Edit 大改

`hyperframes preview` 跑著時會持續往 `index.html` 注入 `data-hf-id`，Edit 的 old_string 就對不上了。大改前先 `hyperframes preview --stop`。

### 5. 監看 render 的失敗過濾器不能只 grep `error`

HyperFrames 有一行 log 長這樣：`static-frame dedup: disabled (... this is the safe fallback, not an error)`，只 grep `error` 會把它誤報成失敗。過濾要排除含 `not an error` 的行。

### 6. 分段轉錄的輸出格式會在段與段之間漂移

13 段裡有 5 段是 `**[MM:SS] Name**：`、其餘是 `[MM:SS] **Name**：`。只認一種形狀的 regex 讓那 5 段靜默回 0 行，合併結果看起來完整，實際少 40%。要用寬鬆的 regex（容許前導 `**`），並逐段印行數核對——回 0 行是格式沒對上，不是那段沒東西。

### 7. 大檔下載 exit 0 不代表檔案是完整的

一支 938MB 的錄影抓到 971MB 時 read timeout，指令仍 exit 0，症狀要到 `ffprobe` 才現形（`moov atom not found`）。驗收條件是 ffprobe 讀得出 duration，不是 exit code 也不是檔案存在；重試迴圈要把 ffprobe 當成功判準。

### 8. 官方 slideshow 框架的 present 目前不能用

它的 `present` 是官方自己標註的 temporary workaround，要求 composition 暴露單一 `window.__timelines.root`。實測 25 幕 slide 全部解析失敗、player 卡在 loading。改成只借它的視覺語言與逐段揭示節奏，控制器自己寫 60 行，零框架相依。

### 9. 投影片版式要用實際放映尺寸驗，不是瀏覽器當下視窗

agent-browser 預設視窗高 577px，量出 10 頁溢出；改用 `style.height="720px"` 模擬 16:9 後剩 6 頁，字級下修再測才歸零。用預設視窗判斷會做出過度縮小的版面。`slides-tokens.css` 的字級是為 1080p 設計的，1280×720 放映要按比例覆寫。

### 10. Studio 顯示「Uploading 0%」不代表上傳卡住

判準是看 API 的 `uploadStatus` 與 `fileDetails.fileSize` 是否等於本地位元組數，不看 UI。這次 499MB 走 resumable 一次就成功，也推翻了舊紀錄裡「257MB 會失敗」的門檻——那是舊 chunked 路徑的限制。

### 11. 縮圖標題被靜默截斷

`compactTitle()` 自動砍標點、只留前 22 字、再從中點硬拆兩行，結果是「你必須知」「最常見的 5」「設定安」這種半截句掛在 YouTube 上好幾個月，36 支，沒人發現。改成手寫短標（缺條目就讓 build 直接失敗）、字級擬合改用各版型的真實容器寬、副標加 `word-break: keep-all`，並新增 `npm run lint:thumbnails` 當固定關卡。判準：任何會丟棄使用者內容的自動化，一律改成「放不下就縮小或報錯」，不准靜默丟字。

四個月、四套工具，同一個教訓：驗產物，不驗 exit code。

<!--
新增非原文句子清單（忠實度自首）：
1.「這條管道最危險的地方不是它會壞掉，是它會安靜地少做一半事情然後回報成功。exit 0 的下載其實是殘檔、`compactTitle()` 把標題砍成半句掛了三十六支、13 段轉錄有 5 段回 0 行合併起來看起來還很完整——這些沒有一個會丟 error 給你。以下按時間順序，從 Remotion 那套一路記到 HyperFrames。」— 框架句（合併文開頭；三個例子皆為下文原有事實的引用，未新增事實）
2. 四個 H2 段標題「Remotion 時代：四月的九個坑」「五月：YouTube API 大檔上傳，216 MB 過、257 MB 不過」「六月：Remotion 動畫與 ffmpeg 後製」「八月：整條流水線換成 HyperFrames 之後的十一個坑」— 小標（合併用；原四篇的標題語意保留）
3.「（這條門檻後來被推翻了，見最後一節第 10 點。）」— 銜接（指向本文第 10 點原有內容，不新增事實）
4.「這一節只記製作技術層面反覆被糾正的坑。」— 改寫（原句為「本篇只記製作技術層面反覆被糾正的坑，這些坑下次想第一次就做對。」，刪去指涉單篇的後半）
5.「四個月、四套工具，同一個教訓：驗產物，不驗 exit code。」— 框架句（收束；「驗收條件是 ffprobe 讀得出 duration，不是 exit code」為本文第 7 點原有判準的復述）
其餘所有段落、數據、指令、判準均逐字取自四篇原文（hyperframes-video-gotchas、remotion-ffmpeg-video-pitfalls、video-production-gotchas-2026、youtube-large-upload-216-257mb），僅做小標層級調整與少量順序重排，未新增原文沒有的根因或解法。原四篇的收尾句（「這週就這些。」「踩坑是自動化流程的必要成本……」「以上是這一週兩部影片……」「這個課我這週又上了一次。」）於合併時刪去，避免重複收尾。
-->
