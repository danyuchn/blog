---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-22T04:00:00Z
title: "Your Automated Video Pipeline Is Silently Dropping Work: Gotchas From Remotion, ffmpeg, the YouTube API, and HyperFrames"
slug: en/automated-video-pipeline-gotchas
featured: false
draft: false
tags:
  - video-production
  - gotchas
  - automation
description: 'Four months of video automation gotchas, from Remotion through HyperFrames: truncated downloads that exit 0, thumbnail titles cut mid-word, transcript chunks returning zero lines, large uploads that hang. None of them raise an error.'
---

The dangerous part of this pipeline isn't that it breaks. It's that it quietly does half the work and reports success. A download exits 0 but the file is truncated. `compactTitle()` chopped titles into half-sentences and left them on YouTube across thirty-six videos. Five of thirteen transcript chunks returned zero lines and the merged result still looked complete. Not one of those threw an error. Here they are in order, from the Remotion setup through to HyperFrames.

## The Remotion era: nine bugs from April

Our channel's production pipeline runs almost entirely on code: Remotion for animation, ffmpeg for post-production compositing, SiliconFlow ASR for subtitles, yt-dlp for downloading source material, YouTube Data API for automated uploads. When it works, a video goes from script to published with no manual steps. When it breaks, you get this post.

Nine bugs from April, in order.

### 1. YouTube Analytics API dimension names don't match the Studio UI

The `insightTrafficSourceType` values the API returns don't line up with what you see in Studio. "Subscribers" in the UI becomes `SUBSCRIBER` in the API; "Channel page" might come back as `YT_CHANNEL_PAGE`. Easy to get confused when you're trying to match numbers.

On top of that, Analytics API has a **48–72 hour delay**. If you run a script right after upload and see low numbers, it's not a bug — the data just hasn't arrived yet.

Quick check to see actual dimension values:

```bash
curl "https://youtubeanalytics.googleapis.com/v2/reports?ids=channel==MINE&metrics=views&dimensions=insightTrafficSourceType&startDate=2026-04-01&endDate=2026-04-30&key=$YT_KEY"
```

### 2. ffmpeg drawbox without timestamps causes overlapping boxes

I wanted static annotation boxes that appear during specific segments. Used drawbox filter, but put multiple boxes into a single `filter_complex` without separate `enable='between(t,start,end)'` params. Result: boxes showed up at wrong times and overlapped in strange ways.

Fix: give each box its own drawbox with its own time range.

```bash
ffmpeg -i input.mp4 \
  -vf "drawbox=x=10:y=10:w=200:h=50:color=red@0.5:enable='between(t,2,5)', \
       drawbox=x=10:y=80:w=200:h=50:color=blue@0.5:enable='between(t,8,12)'" \
  output.mp4
```

### 3. Remotion outputs yuvj420p — YouTube reads it wrong

Remotion's default pixel format is `yuvj420p` (full-range). YouTube's pipeline treats it as `yuv420p` (limited-range), which makes colors look washed out and too bright.

Add a transcode step after render:

```bash
ffmpeg -i remotion_output.mp4 -c:v libx264 -pix_fmt yuv420p -c:a copy final.mp4
```

While you're at it, run LUFS normalization in this step too (-13 LUFS is YouTube's target).

### 4. ffmpeg aselect with 200+ between() expressions OOMs

Wanted to cut 218 segments out of an audio file in one go:

```bash
ffmpeg -i input.mp3 -af "aselect='between(t,0.5,1.2)+between(t,3.1,3.8)+...'" output.mp3
```

218 `between()` calls crashes ffmpeg during filter graph initialization — OOM, no output.

Fix: write cut points to a segment list file and use the ffmpeg segment muxer, or run it in Python batches of 20 segments at a time.

### 5. SiliconFlow ASR returns empty word-level timestamps

Called SiliconFlow's speech recognition API with word-level timestamp enabled. Got back a response with empty `segments` and `words` lists — only top-level `text` had content.

Not a code bug. Some models (especially the fast variants) only support utterance-level output, not word-level. Check the model's capability docs or switch to a full Whisper large-v3 equivalent.

### 6. set -e + Remotion render causes premature script exit

Batch script starts with `set -e`, then:

```bash
npx remotion render MyComp output.mp4
ffmpeg -i output.mp4 ...
```

Remotion writes an incomplete mp4 while rendering. The next `ffmpeg` line reads it, gets a non-zero exit code, and `set -e` kills the whole script.

Fix option 1: chain with `&&` instead of newlines. Fix option 2: wrap the render line with `set +e` and `set -e` to handle its exit code separately.

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

### 8. yt-dlp subtitle language codes are inconsistent

Tried downloading with `--sub-lang zh-Hant`. But YouTube's actual language tags can be `zh-Hant`, `zh-TW`, or auto-generated ones like `zh-Hant-RsSZZSfhlqk` (with a random hash appended). Hardcoding the code doesn't work.

Check first, then download:

```bash
yt-dlp --list-subs "https://www.youtube.com/watch?v=VIDEO_ID"
# Use whatever code actually shows up
yt-dlp --sub-lang zh-Hant-RsSZZSfhlqk --write-sub --no-download ...
```

### 9. YouTube Data API caption quota is only 10,000 units per day

The standard quota for the YouTube Data API is 10,000 units per day. Caption operations (captions.list, captions.download) each cost quota. Run a batch script without checking your remaining quota first and you'll burn through it mid-run.

Quota resets at midnight PDT — which is 2pm the next day in Taiwan. Plan accordingly, or you'll wake up to a stalled pipeline wondering why nothing is uploading.

## May: large-file uploads, 216 MB succeeds and 257 MB hangs

On 5/13 I post-produced two videos for YouTube:

- AI job-search demo clip from the 5/10 lecture: 8m27s, **257 MB**, 2010×1080
- Legal MCP demo video: 7m05s, **216 MB**, 1658×1080

Both ran the same pipeline: ffmpeg two-pass loudnorm to -13 LUFS / TP -1 (already yuv420p + bt709, no color conversion) → opencc s2twp simplified-to-traditional → Remotion thumbnail → `googleapiclient` resumable upload.

One worked. One didn't.

### Failure: AI job-search clip (257 MB)

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

### Success: legal MCP demo (216 MB)

Same `googleapiclient` resumable upload (8 MB chunks). This time `processingStatus=succeeded`.

Differences:

- File size 41 MB smaller
- Resolution 1658×1080 (still non-standard width, but smaller than 2010)

### The conclusion at the time: threshold around 220-250 MB

The contrast between the two videos let me correct my CLAUDE.md SOP from "> 200 MB always fails" to "**257 MB confirmed fails, 216 MB confirmed succeeds, threshold around 220-250 MB**."

Practical handling:

- **< 200 MB**: `googleapiclient` resumable upload, safe
- **200-220 MB**: try API, fall back to Studio manual if it stalls
- **> 250 MB**: go straight to Studio manual, don't waste time on API

(That threshold got overturned later — see item 10 in the last section.)

### Two side gotchas worth recording

My earliest version, `tools/yt_upload_law.py`, used raw urllib for chunked upload. Hit SSL EOF at 16 MB. Switched to `googleapiclient.MediaFileUpload`, which has built-in retry. Stable through to completion. Conclusion: use `googleapiclient` for YouTube upload, not raw urllib or curl.

On 5/13 I also tried [yutu](https://github.com/eat-pray-ai/yutu) 0.10.7 for the upload. The credential parser broke even before `yutu video insert` did anything:

```
failed to parse client secret: illegal base64 data at input byte 6
```

Even with valid tokens and no `-c` flag, the entire yutu client init stage crashes. The fallback was to abandon yutu entirely and use curl against the YouTube Data API resumable upload endpoints directly: `POST /upload/youtube/v3/videos?uploadType=resumable` to get the Location header then PUT bytes, `POST /upload/youtube/v3/thumbnails/set` for the thumbnail, and `POST /upload/youtube/v3/captions` resumable for subtitles. All three direct. No wrapper, but every step is controllable.

To figure out why 257 MB was hanging, I burned through at least four versions of upload scripts and DELETEd two failed video IDs. The final lesson: **the API isn't omnipotent.** When the API behaves unstably near some boundary, the fastest move is to accept the boundary, fall back to manual, and stop drilling.

Technical folks fall easily into "I want it 100% automated." But the value of a production line isn't "100% automated." It's "90% automated, 10% manual fault-tolerant design."

## June: Remotion animation and ffmpeg post-production

I made two tutorial videos that week: one is Ep27, which is live, and another that was still scheduled. The pipeline is the same for both — record the narration, convert it to SRT, use Remotion to lock the animation to the subtitle timing, then stitch and normalize with ffmpeg. This section only covers the production-side stuff I kept getting corrected on.

### Subtitles aren't pasted in line by line

The first thing I kept getting corrected on: this is not subtitle animation. Putting one card on screen for every line of narration breaks the restraint principle. The right approach is to keep only the key point — one heading plus at most two supporting elements. Once you cut to that density, the screen stops getting packed with text one narration line at a time.

### Match the font size to the slide spec

The second one is font size. Remotion defaults to roughly 28-32, and that's too small to read on a phone. I switched to matching the slide spec: body is 2.4rem, about 38, and the video actually used 40.

### After you cut content, re-check the timing anchors

The third one is the easiest to miss: after trimming, you have to re-check the timing anchors. The bug came from cutting content but leaving the old fadeIn anchors behind, which makes the animation fire ahead of the narration. In Ep27 there was a spot where the S10e chips were still anchored to an email section I'd already cut, so they came in a full 14 seconds early.

The most effective way to catch this is to fan out several subagents to audit in segments, checking each entrance one by one: for every `global = sceneStart + X`, which SRT line does it actually land on? Ep27 ended up with three fixes where the animation ran ahead of the narration (S1, S10e, S11a).

### Remotion crashes on videos over 10 minutes with a Video component

When the video runs over 10 minutes and the composition contains a Video component, Remotion's render crashes with ffmpeg 254.

My workaround was to split the whole thing apart: the final cut uses a `demo` prop to exclude the screen recording, so Remotion only renders the intro animation segment (`--frames=0-10601`), and the screen recording gets stitched in separately with ffmpeg concat. That way Remotion never has to handle an over-long clip and a Video component in a single render.

### Normalizing quiet narration: three pitfalls

The intro narration on the other video was recorded extremely quiet — integrated came out at −39 LUFS, with peaks only at −19 dBFS. Pulling that up to −13 means +26dB, and that much gain alone buried three pitfalls.

Pitfall one: `loudnorm linear=true` only applies linear gain and won't engage the true-peak limiter, so peaks shot up to +1.2 dBTP.

Pitfall two: pushing the full 26dB through `loudnorm` in one pass clips. That's outside its design range, and even dynamic mode hit +2 dBTP.

Pitfall three: `alimiter` defaults to `level=true`, which automatically pulls the level back up to full scale, canceling out the limiting you just did. You have to set it to `level=false`.

The fix was to skip loudnorm entirely and use `volume=29dB,alimiter=level=false:limit=0.63`.

### opencc s2twp over-localization

For converting the narration from Simplified to Traditional Chinese I use opencc s2twp, and it over-localizes. It turns 荧幕 into 熒幕 when it should be 螢幕, and 权限 into 許可權 when it should be 權限. Always grep the subtitles for those two words after converting.

The finished Ep27 is here: [https://youtu.be/9nQe9OYYhP4](https://youtu.be/9nQe9OYYhP4).

## August: eleven gotchas after the pipeline moved to HyperFrames

[The whole pipeline later moved to HyperFrames](/blog/posts/en/ai-video-pipeline-codex-to-claude), and the gotchas got replaced along with it. Here are the ones I hit in one week of August while building a hybrid piece (animated overlays plus screen-recording pass-through), one per section.

### 1. Transition flicker means the cut point isn't covered by the mask

The wipe was scheduled at `B-0.6～B`, so the red curtain had already slid away 0.3 seconds before the cut. That cut was bare, and the frame flickered. The fix is to move the cut point inside the fully-masked window: enter at `B-0.35`, hold at `B±0.05`, exit at `B+0.35`. The 0.10-second hold is what guarantees at least three fully covered frames at 30fps. Looking back at an earlier episode, it inherited the same bad timing.

### 2. "Pure animation must use a single worker" is a Remotion rule, not a HyperFrames one

Carrying that rule over from Remotion makes renders five to eight times slower. I measured it: with 8 workers, adjacent-frame comparison on static animation gives a pixel difference of 0. To confirm the checker wasn't just broken, I ran it in reverse against moving transition frames, and it did catch differences. 59,000 frames finished in about 22 minutes.

### 3. `.term` / `.codefile` silently cut off the last line

Both are flex children, so `scene-content` squeezes them, and with `overflow: hidden` on top the last line just gets eaten. On screen it only looks like the text is sitting flush against the bottom. Setting `flex-shrink: 0` fixes it, and once that's in, the scenes that are genuinely overfull start showing up. Also, `hyperframes check` only samples 9 frames, so it isn't guaranteed to catch this. Use `hyperframes snapshot --zoom "<selector>"` to blow up the element itself and check.

### 4. Don't make big edits while preview is running

While `hyperframes preview` is running it keeps injecting `data-hf-id` attributes into `index.html`, and your Edit old_string stops matching. Run `hyperframes preview --stop` before any large edit.

### 5. A render failure filter can't just grep for `error`

HyperFrames prints a log line that reads `static-frame dedup: disabled (... this is the safe fallback, not an error)`. Grepping for `error` reports it as a failure. The filter has to exclude lines containing `not an error`.

### 6. Chunked transcription output drifts in format between chunks

Out of 13 chunks, 5 came out as `**[MM:SS] Name**：` and the rest as `[MM:SS] **Name**：`. A regex that only recognizes one of those shapes made those 5 chunks silently return 0 lines. The merged result looked complete but was missing 40% of the content. Use a looser regex when merging (allow the leading `**`), and print the line count per chunk to check. A chunk returning 0 lines means the format didn't match, not that the chunk was empty.

### 7. exit 0 on a large download doesn't mean the file is complete

A 938MB recording hit a read timeout at 971MB and the command still exited 0. The symptom only surfaced at `ffprobe`: `moov atom not found`. The acceptance condition for a large download is that ffprobe can read a duration, not the exit code and not the file existing. Retry loops should treat ffprobe as the success test.

### 8. The official slideshow framework's present mode isn't usable right now

Its `present` is flagged by the project itself as a temporary workaround, and it requires the composition to expose a single `window.__timelines.root`. In practice all 25 slides failed to parse and the player sat on loading. I ended up borrowing only its visual language and its progressive-reveal pacing, and wrote the controller myself in 60 lines with no framework dependency.

### 9. Verify slide layout at the real projection size, not your current browser window

agent-browser defaults to a 577px-tall window, which measured 10 pages as overflowing. Switching to `style.height="720px"` to simulate 16:9 left 6, and it only got to zero after I dialed the type size down and measured again. Judge by the default window and you end up shrinking the layout far more than you need to. The type scale in `slides-tokens.css` is designed for 1080p, so a 1280×720 projection needs a proportional override.

### 10. Studio showing "Uploading 0%" doesn't mean the upload is stuck

The thing to check is whether the API's `uploadStatus` and `fileDetails.fileSize` match the local byte count. Don't go by the UI. This time 499MB went through resumable upload on the first try, which also killed the old note about a "257MB fails" threshold. That was a limit of the old chunked path.

### 11. Thumbnail titles were being silently truncated

`compactTitle()` strips punctuation, keeps only the first 22 characters, and then hard-splits into two lines at the midpoint. The result was half-sentences sitting on YouTube for months. 36 of them. Nobody noticed. I replaced it with hand-written short titles (a missing entry now fails the build outright), switched the type fitting to each template's real container width, added `word-break: keep-all` on the subtitle, and added `npm run lint:thumbnails` as a permanent gate. The rule: any automation that discards user content has to be changed to shrink or error out when things don't fit. No silent dropping of characters.

Four months, four toolchains, one lesson: verify the artifact, not the exit code.

<!--
Sentences added by AI that are not in the source posts (fidelity disclosure):
1. "The dangerous part of this pipeline isn't that it breaks. It's that it quietly does half the work and reports success. ... Here they are in order, from the Remotion setup through to HyperFrames." — framing (merged-post opening; all three examples cited are facts already present below, no new facts introduced)
2. The four H2 section titles ("The Remotion era: nine bugs from April", "May: large-file uploads, 216 MB succeeds and 257 MB hangs", "June: Remotion animation and ffmpeg post-production", "August: eleven gotchas after the pipeline moved to HyperFrames") — section headings for the merge; semantics preserved from the four original titles
3. "(That threshold got overturned later — see item 10 in the last section.)" — transition (points at content already in this post, no new fact)
4. "This section only covers the production-side stuff I kept getting corrected on." — rewrite (original: "This post only covers the production-side stuff I kept getting corrected on, the kind of thing I want to get right the first time next round." — trailing clause referring to a single post removed)
5. "Four months, four toolchains, one lesson: verify the artifact, not the exit code." — framing (closing; restates the acceptance criterion already stated in item 7)
Everything else is taken verbatim from the four source posts (hyperframes-video-gotchas, remotion-ffmpeg-video-pitfalls, video-production-gotchas-2026, youtube-large-upload-216-257mb), with only heading-level adjustment and minor reordering. No new root causes or fixes were added. The four original closing lines were dropped to avoid four endings in one post.
-->
