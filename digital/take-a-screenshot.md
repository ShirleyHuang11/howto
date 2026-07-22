---
name: take-a-screenshot
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

You capture the correct part of the screen, find the saved image, and optionally annotate it without exposing unnecessary private information.

## Preconditions

- The screen content you want to capture is visible.
- You know whether the recipient needs the whole screen, one window, or a selected region.

## Steps

1. **Choose the capture area.** [BRANCH: full screen | window | region] use full screen for context, window for one app, or region when only a small detail matters. → *Expect:* you know what will be included and what should be excluded.
2. **Use the platform shortcut.** Windows: `Win+Shift+S` for Snipping Tool or `PrtScn`; macOS: `Shift+Command+5` or `Shift+Command+4`; Chromebook: `Ctrl+Show windows`; iPhone: side button plus volume up; Android: power plus volume down on most phones. → *Expect:* a capture overlay, flash, or thumbnail appears.
3. **Select the region or window if prompted.** Drag around the exact area, or click the target window. Include enough surrounding context for the recipient to understand it. → *Expect:* the selected area is captured.
4. **Find where it saved.** Windows Snipping Tool often copies to clipboard and may save under Pictures or Screenshots; macOS saves to Desktop unless changed; phones save to Photos or Gallery; Chromebooks save to Downloads. → *Expect:* the screenshot is visible in the expected location or clipboard.
5. **Annotate only what helps.** Use Markup, Snipping Tool, Preview, Photos, or a trusted editor to draw arrows, boxes, or blur sensitive details. → *Expect:* the important area is obvious and private details are hidden if needed.
6. **Check image clarity.** Open the screenshot before sending and zoom in on the important text. → *Expect:* text and controls are readable at normal viewing size.
7. **Share the right file.** Attach the image file, paste from clipboard, or drag it into the message or support form. → *Expect:* the recipient or form shows the screenshot preview.

## Decision points

- Need to show a bug → capture enough context, including the error, app name, and nearby controls.
- Need to hide private information → use region capture or redact before sharing.
- Screenshot shortcut does nothing → check keyboard layout, function-lock state, or device-specific button timing.
- Content blocks screenshots → respect the app restriction; banking, streaming, and secure work apps may prevent capture.

## Failure modes & recovery

- **F1 Screenshot is not saved:** detect: no file appears where expected, recover: paste into an image editor or use the capture tool's Save button.
- **F2 Wrong screen captured:** detect: image shows the other monitor or too much desktop, recover: use region or window capture.
- **F3 Text is unreadable:** detect: zooming in shows blur or tiny text, recover: capture a smaller region or increase display zoom before capturing.
- **F4 Private data included:** detect: passwords, account numbers, addresses, chats, or tabs are visible, recover: retake as a region or redact before sending.
- **F5 Phone shortcut opens a power menu:** detect: buttons were held too long, recover: press both buttons briefly and release together.

## Verification

The screenshot file or clipboard image shows exactly the intended content, is readable, and contains no avoidable private information.

## Variations

- `windows`: `Win+Shift+S` captures to clipboard first; open the notification to save or annotate.
- `macos`: `Shift+Command+5` lets you choose save location, timer, window, region, or full screen.
- `ios`: After capture, tap the thumbnail for Markup and crop before saving or sharing.
- `android`: Some phones add a scrolling screenshot option for long pages.

## Safety & privacy

Screenshots often expose browser tabs, notifications, account names, location, documents, and messages. Review before sharing, especially when sending to public forums, support chats, or coworkers.
