---
name: open-a-link-in-a-new-tab
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

Open a link in a separate tab while keeping the current page available.

## Preconditions

- A browser page with a visible link is open.
- Pop-up or new-tab blocking is not preventing normal user-clicked tabs.

## Steps

1. **Point at the link.** Move the pointer over the link and pause. → *Expect:* the browser status area shows the link destination or the cursor changes.
2. **Open the context menu.** Right-click the link, or press `Control` and click on Mac. → *Expect:* a menu appears with link actions.
3. **Choose new tab.** Select `Open Link in New Tab`. → *Expect:* a new tab appears for the link while the original page stays open.
4. **Switch when ready.** Click the new tab, or press `Ctrl+Tab` on Windows/Linux or `Control+Tab` on Mac. → *Expect:* the linked page is visible in the new tab.

## Decision points

- You want the new tab immediately → middle-click the link or hold `Ctrl`/`Command` while clicking.
- You do not trust the link → copy or inspect the address before opening it.
- A link triggers a download → confirm the file type and source before saving.

## Failure modes & recovery

- **F1 Menu lacks new-tab option:** detect no link actions in the menu → right-click directly on the link text or image.
- **F2 New tab blocked:** detect a browser warning or no tab opening → allow tabs for that site only if you trust it.
- **F3 Link opens in same tab:** detect the current page changes → press Back, then use the context menu method.

## Verification

The original page remains in one tab, and the linked destination is open in another tab.

## Variations

- Chrome: `Ctrl+click` on Windows/Linux or `Command+click` on Mac opens a background tab.
- Firefox: middle-click opens a background tab by default.
- Safari: `Command+click` opens a link in a new tab when tab browsing is enabled.

## Safety & privacy

New tabs can still load trackers, ads, or sign-in pages. Check the destination before entering passwords or private information.
