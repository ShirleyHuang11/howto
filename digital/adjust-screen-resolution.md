---
name: adjust-screen-resolution
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 3min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Change the screen resolution so display content is clearer, larger, or better matched to the monitor.

## Preconditions

- You can access display settings on the device.
- The screen is connected and showing a usable image.

## Steps

1. **Open display settings.** [BRANCH: Windows | Mac] Windows: open Settings > System > Display; Mac: open System Settings > Displays. → *Expect:* display controls are visible.
2. **Select the display.** If multiple screens appear, choose the one you want to adjust. → *Expect:* the selected display is highlighted or named.
3. **Choose resolution or scaling.** Pick `Recommended`, `Default`, or another listed resolution or scaled option. → *Expect:* the screen preview or resolution value changes.
4. **Confirm the change.** Accept the confirmation prompt if the display looks usable. → *Expect:* the new setting remains active.
5. **Check readability.** Look at text, icons, and windows on the adjusted screen. → *Expect:* content is sharp and sized appropriately.

## Decision points

- Text is too small but sharp → adjust scaling rather than lowering resolution.
- Image is blurry → choose the monitor's recommended or native resolution.
- Screen goes blank → wait for the setting to revert automatically.

## Failure modes & recovery

- **F1 Display goes blank:** detect no image after applying → wait for automatic revert or press Escape.
- **F2 Everything looks blurry:** detect fuzzy text or icons → return to recommended resolution and change scaling.
- **F3 Wrong monitor changed:** detect the other screen changed → select the intended display and restore the first one.

## Verification

The intended display shows the selected resolution or scaling, and text appears readable without blur.

## Variations

- `windows`: Settings labels include Display resolution and Scale.
- `mac`: Displays may show thumbnails, `Default`, `More Space`, or `Larger Text`.
- `external-monitor`: some resolutions appear only after reconnecting the cable or updating drivers.

## Safety & privacy

Changing resolution is reversible, but very large scaling can expose less content during screen sharing. Check shared screens before presenting.
