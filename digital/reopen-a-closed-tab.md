---
name: reopen-a-closed-tab
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

Restore a browser tab that was closed by mistake.

## Preconditions

- The browser window is still open.
- The tab was closed recently enough to be in browser history.

## Steps

1. **Use the reopen shortcut.** Press `Ctrl+Shift+T` on Windows/Linux or `Command+Shift+T` on Mac. → *Expect:* the most recently closed tab reopens.
2. **Repeat if needed.** Press the shortcut again for earlier closed tabs. → *Expect:* tabs reopen in reverse order of closing.
3. **Check the restored page.** Look at the address bar and page content. → *Expect:* the page matches the tab you intended to restore.

## Decision points

- You closed a whole window → repeat the shortcut until the window or its tabs reopen.
- The reopened page requires sign-in → sign in only after confirming the domain is correct.
- The tab was private browsing → private tabs usually cannot be restored after closing.

## Failure modes & recovery

- **F1 Wrong tab restored:** detect an unrelated page opening → press the shortcut again or use History.
- **F2 Shortcut does nothing:** detect no tab change → open the browser History menu and select a recent page manually.
- **F3 Form data missing:** detect a restored form is blank → check drafts, autosave, or browser back-forward cache if available.

## Verification

The page from the accidentally closed tab is open again in a browser tab.

## Variations

- Chrome: the History menu also lists recently closed tabs and windows.
- Firefox: use `History` > `Recently Closed Tabs` if the shortcut is unavailable.
- Safari: use `History` > `Reopen Last Closed Tab` or `Command+Shift+T`.

## Safety & privacy

Reopening a tab can reveal pages that were intentionally closed. Be careful on shared screens or shared browser profiles.
