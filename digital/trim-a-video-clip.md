---
name: trim-a-video-clip
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Shorten a video by setting a new start and end point.

## Preconditions

- The video file is available on your device or in an editor.
- You know the portion of the clip you want to keep.

## Steps

1. **Open the video editor.** Open the clip in Photos, Gallery, QuickTime, Clipchamp, iMovie, or another editor. → *Expect:* the video timeline is visible.
2. **Choose trim.** Select `Edit`, `Trim`, scissors, or timeline handles. → *Expect:* trim handles or a highlighted timeline range appear.
3. **Set the start point.** Drag the left handle or playhead to the first frame you want to keep. → *Expect:* playback starts at the intended moment.
4. **Set the end point.** Drag the right handle to the last frame you want to keep. → *Expect:* playback ends at the intended moment.
5. **Preview the clip.** Play the trimmed range from start to finish. → *Expect:* only the desired section plays.
6. **Save a copy.** Choose `Save as copy`, `Export`, or equivalent when available. → *Expect:* a new trimmed video file is created.

## Decision points

- You need to preserve the original → save as a copy rather than overwriting.
- You need exact timing → type start and end times if the editor supports timecode.
- The clip is for upload → choose an export size accepted by the target site or app.

## Failure modes & recovery

- **F1 Trim handles hard to move:** detect imprecise start or end → zoom into the timeline or use keyboard/timecode controls.
- **F2 Original overwritten:** detect only the short version remains → check undo, version history, recently edited originals, or backups.
- **F3 Export fails:** detect an error or missing output file → free storage space and export again at a lower resolution.

## Verification

The saved video starts and ends at the intended moments and plays without including the removed sections.

## Variations

- `windows`: Photos and Clipchamp provide basic trimming.
- `mac`: QuickTime Player and Photos both support trim.
- `mobile-app`: iOS Photos and Android Gallery/Photos use drag handles around the timeline.

## Safety & privacy

Trimming may leave the original file on the device or in cloud history. Delete or secure the original if the removed section contains private information.
