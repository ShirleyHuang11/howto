---
name: zoom-a-web-page
domain: digital
locale: [generic]
interface: web
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Make a web page larger or smaller without changing the whole computer display.

## Preconditions

- A web page is open in a desktop browser.
- The browser window is active.

## Steps

1. **Zoom in.** Press `Ctrl++` on Windows/Linux or `Command++` on Mac. → *Expect:* page text and content become larger.
2. **Zoom out if needed.** Press `Ctrl+-` on Windows/Linux or `Command+-` on Mac. → *Expect:* page content becomes smaller.
3. **Return to normal size.** Press `Ctrl+0` on Windows/Linux or `Command+0` on Mac. → *Expect:* the page returns to 100 percent zoom.
4. **Check layout.** Scroll and inspect buttons, menus, and text. → *Expect:* important controls remain visible and usable.

## Decision points

- Only text needs to be larger → check browser accessibility settings for text scaling.
- The whole screen is too small → use operating system display scaling instead.
- A site layout breaks at high zoom → lower zoom until controls fit.

## Failure modes & recovery

- **F1 Shortcut affects browser UI:** detect the toolbar changes but page content does not → click inside the page and try again.
- **F2 Content overlaps:** detect buttons or text covering each other → reduce zoom or rotate a mobile device.
- **F3 Zoom persists unexpectedly:** detect future visits still zoomed → reset with `Ctrl+0` or `Command+0`.

## Verification

The page is readable at the chosen zoom level, and the browser zoom indicator shows the expected percentage.

## Variations

- Chrome: the three-dot menu includes `Zoom` controls and a reset option.
- Firefox: the application menu includes `Zoom` controls and can zoom text only.
- Safari: use `View` > `Zoom In`, `Zoom Out`, or `Actual Size`.

## Safety & privacy

Zooming can make sensitive page content easier for others nearby to read. Reset zoom before sharing a screen if needed.
