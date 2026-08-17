---
name: find-text-on-a-page
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

Find a word or phrase on the currently open web page.

## Preconditions

- A web page is open in a browser.
- You know the word, phrase, or number to search for.

## Steps

1. **Open page find.** Press `Ctrl+F` on Windows/Linux or `Command+F` on Mac. → *Expect:* a small Find box appears in the browser.
2. **Type the target text.** Enter the word or phrase exactly enough to identify it. → *Expect:* matching text is highlighted on the page and the match count updates.
3. **Move between matches.** Press `Enter` for the next match or `Shift+Enter` for the previous match. → *Expect:* the highlight moves to another occurrence.
4. **Close find.** Press `Esc` or click the close button on the Find box. → *Expect:* the Find box closes and the page remains at the selected match.

## Decision points

- No matches appear → check spelling, use a shorter phrase, or search for a related word.
- The page loads more content while scrolling → scroll farther and repeat the search.
- Text is inside an image or video → page find will not detect it.

## Failure modes & recovery

- **F1 Wrong frame searched:** detect a match count of zero on a page with embedded content → click inside the frame or open it directly, then search again.
- **F2 Hidden match:** detect the match count changes but nothing visible highlights → expand collapsed sections or clear site overlays.
- **F3 Browser shortcut captured:** detect another app or site panel opening → use the browser menu item `Find` or `Find in Page`.

## Verification

The browser highlights at least one matching occurrence, or the Find box shows zero matches for the exact search text.

## Variations

- Chrome: use `Ctrl+F` or `Command+F`; match count appears in the Find box.
- Firefox: use `Ctrl+F` or `Command+F`; options such as case matching may appear in the Find bar.
- Safari: use `Command+F`; matches are highlighted on the page.

## Safety & privacy

Find text stays in the browser window briefly and may be visible to someone looking at your screen. Avoid searching sensitive terms on shared displays.
