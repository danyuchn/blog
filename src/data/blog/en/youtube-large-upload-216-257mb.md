---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-15T09:00:00Z
title: "YouTube Data API large-file upload tested: 216 MB succeeds, 257 MB hangs—threshold around 220-250 MB"
slug: en/youtube-large-upload-216-257mb
featured: false
draft: false
tags:
  - youtube
  - video-production
  - api-debugging
description: 'Two 5/13 uploads via YouTube Data API: 216 MB legal MCP demo succeeded, 257 MB AI job-search clip hung indefinitely. Same googleapiclient resumable upload pipeline. The difference is file size and resolution. The practical threshold sits around 220-250 MB.'
---

On 5/13 I post-produced two videos for YouTube:

- AI job-search demo clip from the 5/10 lecture: 8m27s, **257 MB**, 2010×1080
- Legal MCP demo video: 7m05s, **216 MB**, 1658×1080

Both ran the same pipeline: ffmpeg two-pass loudnorm to -13 LUFS / TP -1 (already yuv420p + bt709, no color conversion) → opencc s2twp simplified-to-traditional → Remotion thumbnail → `googleapiclient` resumable upload.

One worked. One didn't.

## Failure: AI job-search clip (257 MB)

Tried two API upload paths:

1. **curl single resumable PUT**
2. **Python `googleapiclient` chunked resumable PUT** (8 MB chunks + ACK)

Both ended with `uploadStatus=uploaded`, but `processingStatus` stuck on `processing` for over an hour with zero movement. Studio UI showed "Processing will begin shortly" with the upload-arrow icon.

Both failed video IDs (`7UhRoAvWr-w` and `FP4_8D4vfes`) got DELETEd.

**Interim SOP**: abandon the API path, drag the file into YouTube Studio manually. Manual upload completed processing within a few minutes. Video ID changed to `HcADayRCJMg`.

Possible causes (unverified):

- Incomplete metadata fragment after ffmpeg `-c:v copy`
- YT backend processes non-standard 2010×1080 width slower
- Past some MB threshold a different backend processing pipeline kicks in

## Success: legal MCP demo (216 MB)

Same `googleapiclient` resumable upload (8 MB chunks). This time `processingStatus=succeeded`.

Differences:

- File size 41 MB smaller
- Resolution 1658×1080 (still non-standard width, but smaller than 2010)

## Conclusion: threshold around 220-250 MB

The contrast between the two videos let me correct my CLAUDE.md SOP from "> 200 MB always fails" to "**257 MB confirmed fails, 216 MB confirmed succeeds, threshold around 220-250 MB**."

Practical handling:

- **< 200 MB**: `googleapiclient` resumable upload, safe
- **200-220 MB**: try API, fall back to Studio manual if it stalls
- **> 250 MB**: go straight to Studio manual, don't waste time on API

## Two side gotchas worth recording

### urllib SSL EOF mid-upload

My earliest version, `tools/yt_upload_law.py`, used raw urllib for chunked upload. Hit SSL EOF at 16 MB. Switched to `googleapiclient.MediaFileUpload`, which has built-in retry. Stable through to completion.

**Conclusion**: use `googleapiclient` for YouTube upload, not raw urllib or curl.

### yutu credential parser bug

5/13 tried [yutu](https://github.com/eat-pray-ai/yutu) 0.10.7 for the upload. The credential parser broke even before `yutu video insert` did anything:

```
failed to parse client secret: illegal base64 data at input byte 6
```

Even with valid tokens and no `-c` flag, the entire yutu client init stage crashes.

**Fallback**: abandon yutu entirely. Use curl against the YouTube Data API resumable upload endpoints directly:

1. `POST /upload/youtube/v3/videos?uploadType=resumable` to get the Location header → PUT bytes
2. `POST /upload/youtube/v3/thumbnails/set` for thumbnail
3. `POST /upload/youtube/v3/captions` resumable for subtitles

All three direct. No wrapper, but every step is controllable.

## Why write this down

If you're doing video upload automation, these thresholds and fallbacks will save you hours.

To figure out why 257 MB was hanging, I burned through at least four versions of upload scripts and DELETEd two failed video IDs. The final lesson: **the API isn't omnipotent.** When the API behaves unstably near some boundary, the fastest move is to accept the boundary, fall back to manual, and stop drilling.

Technical folks fall easily into "I want it 100% automated." But the value of a production line isn't "100% automated." It's "90% automated, 10% manual fault-tolerant design." I re-took that lesson again this week.
