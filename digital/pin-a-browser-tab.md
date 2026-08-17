---
name: pin-a-browser-tab
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

Pin an important browser tab so it stays compact and harder to close accidentally.

## Preconditions

- The page you want to keep open is loaded in a browser tab.
- You are using a browser that supports pinned tabs.

## Steps

1. **Select the tab.** Click the tab you want to pin. → *Expect:* the page is active and the tab is highlighted.
2. **Open the tab menu.** Right-click the tab, or `Control`-click it on Mac. → *Expect:* a tab context menu appears.
3. **Pin the tab.** Choose `Pin`, `Pin Tab`, or `Pin Tab to Start`. → *Expect:* the tab shrinks and moves to the left side of the tab bar.
4. **Test the pinned position.** Open another tab or switch tabs. → *Expect:* the pinned tab remains at the left and shows a small site icon.

## Decision points

- You need the page only once → leave it unpinned.
- The page plays audio or notifications → consider muting or closing it instead of pinning.
- The tab contains private information → do not pin it on a shared browser profile.

## Failure modes & recovery

- **F1 Pin option missing:** detect no pin action in the menu → update the browser or use bookmarks instead.
- **F2 Wrong tab pinned:** detect the wrong site icon at the left → right-click it and choose `Unpin`, then pin the correct tab.
- **F3 Pinned tab disappears after restart:** detect it is gone after reopening the browser → check startup settings or session restore.

## Verification

The chosen tab is pinned at the left side of the tab bar and remains open while other tabs are opened or closed.

## Variations

- Chrome: right-click a tab and choose `Pin`.
- Firefox: right-click a tab and choose `Pin Tab`.
- Safari: drag a tab to the left side of the tab bar or choose `Pin Tab` from the tab menu.

## Safety & privacy

Pinned tabs can reopen automatically and expose account pages or message previews. Use them only on trusted devices and profiles.
