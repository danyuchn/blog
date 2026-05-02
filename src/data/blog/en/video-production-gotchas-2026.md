---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-01T04:00:00Z
title: "Nine video production bugs I hit in April 2026"
slug: en/video-production-gotchas-2026
featured: false
draft: false
tags:
  - ffmpeg
  - remotion
  - automation
  - gotchas
  - youtube
description: "Running a fully automated video pipeline with Remotion, ffmpeg, yt-dlp, SiliconFlow ASR, and the YouTube API — here are nine specific bugs from April, in the order I hit them."
---

Our channel's production pipeline runs almost entirely on code: Remotion for animation, ffmpeg for post-production compositing, SiliconFlow ASR for subtitles, yt-dlp for downloading source material, YouTube Data API for automated uploads. When it works, a video goes from script to published with no manual steps. When it breaks, you get this post.

Nine bugs from April, in order.

---

### 1. YouTube Analytics API dimension names don't match the Studio UI

The `insightTrafficSourceType` values the API returns don't line up with what you see in Studio. "Subscribers" in the UI becomes `SUBSCRIBER` in the API; "Channel page" might come back as `YT_CHANNEL_PAGE`. Easy to get confused when you're trying to match numbers.

On top of that, Analytics API has a **48–72 hour delay**. If you run a script right after upload and see low numbers, it's not a bug — the data just hasn't arrived yet.

Quick check to see actual dimension values:

```bash
curl "https://youtubeanalytics.googleapis.com/v2/reports?ids=channel==MINE&metrics=views&dimensions=insightTrafficSourceType&startDate=2026-04-01&endDate=2026-04-30&key=$YT_KEY"
```

---

### 2. ffmpeg drawbox without timestamps causes overlapping boxes

I wanted static annotation boxes that appear during specific segments. Used drawbox filter, but put multiple boxes into a single `filter_complex` without separate `enable='between(t,start,end)'` params. Result: boxes showed up at wrong times and overlapped in strange ways.

Fix: give each box its own drawbox with its own time range.

```bash
ffmpeg -i input.mp4 \
  -vf "drawbox=x=10:y=10:w=200:h=50:color=red@0.5:enable='between(t,2,5)', \
       drawbox=x=10:y=80:w=200:h=50:color=blue@0.5:enable='between(t,8,12)'" \
  output.mp4
```

---

### 3. Remotion outputs yuvj420p — YouTube reads it wrong

Remotion's default pixel format is `yuvj420p` (full-range). YouTube's pipeline treats it as `yuv420p` (limited-range), which makes colors look washed out and too bright.

Add a transcode step after render:

```bash
ffmpeg -i remotion_output.mp4 -c:v libx264 -pix_fmt yuv420p -c:a copy final.mp4
```

While you're at it, run LUFS normalization in this step too (-13 LUFS is YouTube's target).

---

### 4. ffmpeg aselect with 200+ between() expressions OOMs

Wanted to cut 218 segments out of an audio file in one go:

```bash
ffmpeg -i input.mp3 -af "aselect='between(t,0.5,1.2)+between(t,3.1,3.8)+...'" output.mp3
```

218 `between()` calls crashes ffmpeg during filter graph initialization — OOM, no output. 

Fix: write cut points to a segment list file and use the ffmpeg segment muxer, or run it in Python batches of 20 segments at a time.

---

### 5. SiliconFlow ASR returns empty word-level timestamps

Called SiliconFlow's speech recognition API with word-level timestamp enabled. Got back a response with empty `segments` and `words` lists — only top-level `text` had content.

Not a code bug. Some models (especially the fast variants) only support utterance-level output, not word-level. Check the model's capability docs or switch to a full Whisper large-v3 equivalent.

---

### 6. set -e + Remotion render causes premature script exit

Batch script starts with `set -e`, then:

```bash
npx remotion render MyComp output.mp4
ffmpeg -i output.mp4 ...
```

Remotion writes an incomplete mp4 while rendering. The next `ffmpeg` line reads it, gets a non-zero exit code, and `set -e` kills the whole script.

Fix option 1: chain with `&&` instead of newlines. Fix option 2: wrap the render line with `set +e` and `set -e` to handle its exit code separately.

---

### 7. pgrep -lf deadlocks on itself

Waiting for a render to finish with:

```bash
while pgrep -lf "remotion render"; do sleep 10; done
```

This loop never exits. The shell process running the while loop has `"remotion render"` in its own argv, so `pgrep -lf` always matches itself.

Three actual fixes:

```bash
# 1. Anchor to the real process
pgrep -f '^node.*remotion'

# 2. Track the PID directly
npx remotion render & PID=$!; wait $PID

# 3. Monitor the output file size until it stabilizes
```

---

### 8. yt-dlp subtitle language codes are inconsistent

Tried downloading with `--sub-lang zh-Hant`. But YouTube's actual language tags can be `zh-Hant`, `zh-TW`, or auto-generated ones like `zh-Hant-RsSZZSfhlqk` (with a random hash appended). Hardcoding the code doesn't work.

Check first, then download:

```bash
yt-dlp --list-subs "https://www.youtube.com/watch?v=VIDEO_ID"
# Use whatever code actually shows up
yt-dlp --sub-lang zh-Hant-RsSZZSfhlqk --write-sub --no-download ...
```

---

### 9. YouTube Data API caption quota is only 10,000 units per day

The standard quota for the YouTube Data API is 10,000 units per day. Caption operations (captions.list, captions.download) each cost quota. Run a batch script without checking your remaining quota first and you'll burn through it mid-run.

Quota resets at midnight PDT — which is 2pm the next day in Taiwan. Plan accordingly, or you'll wake up to a stalled pipeline wondering why nothing is uploading.

---

Every automated pipeline hits bugs. The only way to save time in the long run is to write them down when they happen. This list will keep growing.
