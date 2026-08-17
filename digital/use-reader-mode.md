---
name: use-reader-mode
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

View an article-style page in a cleaner reading layout.

## Preconditions

- An article or text-heavy page is open.
- The browser supports reader view for that page.

## Steps

1. **Look for reader controls.** [BRANCH: Chrome | Firefox | Safari] check the address bar, toolbar, or side panel for a reader, page, or document icon. → *Expect:* a reader option appears if the page is eligible.
2. **Open reader mode.** Click the reader icon or choose the reader option from the browser menu. → *Expect:* the page changes to a simplified text layout.
3. **Adjust reading settings.** Change text size, font, color theme, or width if controls are available. → *Expect:* the article remains readable and fits the window.
4. **Leave reader mode.** Click the reader icon again, close the side panel, or use the Back button if needed. → *Expect:* the original web page view returns.

## Decision points

- Reader mode is unavailable → the page may not be article-like or the browser may not support reader mode there.
- Images or comments matter → use the normal page view instead.
- A paywall or login appears → reader mode is not a privacy or access bypass.

## Failure modes & recovery

- **F1 Reader icon missing:** detect no reader control in the address bar or menu → try Firefox or Safari, or use browser zoom instead.
- **F2 Important content disappears:** detect missing tables, figures, comments, or buttons → return to normal page view.
- **F3 Formatting looks wrong:** detect broken paragraphs or headings → refresh the page or use normal view.

## Verification

The page displays in a simplified reader layout with the main article text visible and adjustable.

## Variations

- Chrome: use Reading mode from the side panel when available.
- Firefox: click the reader-view icon in the address bar or press `F9` on supported pages.
- Safari: click the Reader icon in the Smart Search field or use `View` > `Show Reader`.

## Safety & privacy

Reader mode changes display only. The site can still know the page was loaded, and private article content may be visible on screen.
