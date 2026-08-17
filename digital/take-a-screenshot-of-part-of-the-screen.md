---
name: take-a-screenshot-of-part-of-the-screen
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 1min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Capture a selected area of the screen as an image.

## Preconditions

- The content you want to capture is visible on screen.
- Private information outside the target area can be avoided or hidden.

## Steps

1. **Prepare the screen.** Arrange windows and hide private tabs, notifications, and account details. → *Expect:* only the intended content is visible near the capture area.
2. **Start area capture.** [BRANCH: Windows | Mac] Windows: press `Windows+Shift+S`; Mac: press `Command+Shift+4`. → *Expect:* the cursor changes to a crosshair or snipping tool.
3. **Select the region.** Drag around the exact area to capture, then release. → *Expect:* the selected area flashes, copies, or opens as a screenshot preview.
4. **Save or paste the screenshot.** Click the notification to save, or paste into the destination with `Ctrl+V` or `Command+V`. → *Expect:* the screenshot appears in the file location or target app.
5. **Inspect the image.** Open or zoom the screenshot before sharing. → *Expect:* no unintended private information is visible.

## Decision points

- Need the whole window → use the window capture option instead of dragging a region.
- Need a delayed menu capture → use the screenshot app's timer or delay feature.
- Sharing externally → redact private details before sending.

## Failure modes & recovery

- **F1 Shortcut does nothing:** detect no snipping overlay → open Snipping Tool on Windows or Screenshot on Mac manually.
- **F2 Wrong area captured:** detect missing or extra content → take the screenshot again with a tighter selection.
- **F3 Screenshot cannot be found:** detect no saved file → check clipboard by pasting, or check Desktop, Pictures, or Screenshots.

## Verification

The saved or pasted screenshot contains only the intended screen region and is readable.

## Variations

- `windows`: `Windows+Shift+S` copies the snip and may show a notification for saving.
- `mac`: `Command+Shift+4` saves to the default screenshot location unless settings changed.
- `mobile-app`: phones usually capture the full screen first; crop afterward for a partial screenshot.

## Safety & privacy

Screenshots often include names, emails, locations, tabs, notifications, tokens, or account numbers. Inspect and redact before sharing.
