---
name: view-a-pages-source
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

Open the HTML source for the current web page.

## Preconditions

- A web page is open in a desktop browser.
- You only need to inspect source text, not change the live page.

## Steps

1. **Open page source.** [BRANCH: Chrome | Firefox | Safari] press `Ctrl+U` on Windows/Linux or `Command+Option+U` in Safari on Mac. → *Expect:* a new tab or window opens with page source.
2. **Search within source if needed.** Press `Ctrl+F` or `Command+F` and type a tag, word, or URL. → *Expect:* matching source text is highlighted.
3. **Return to the page.** Switch back to the original tab when finished. → *Expect:* the normal web page remains unchanged.

## Decision points

- You need live generated DOM → use Developer Tools Inspect instead of View Source.
- The source is minified → use browser developer tools formatting where available.
- The page requires sign-in → source may include account-specific data.

## Failure modes & recovery

- **F1 Shortcut opens developer tools:** detect an inspector panel instead of source text → use `view-source:` before the page URL or the browser menu item.
- **F2 Blank or sparse source:** detect little useful HTML → inspect the live page with Developer Tools.
- **F3 Source blocked by app behavior:** detect an error or login source → sign in if appropriate or use the page's normal developer tools.

## Verification

A source view opens showing HTML or source text for the page URL, and the original page is still available.

## Variations

- Chrome: use `Ctrl+U` or `Command+Option+U`, or type `view-source:` before the URL.
- Firefox: use `Ctrl+U` or `Command+U`, or `Tools` > `Browser Tools` > `Page Source`.
- Safari: enable the Develop menu if needed, then use `Develop` > `Show Page Source`.

## Safety & privacy

Page source can expose tokens, embedded identifiers, or private page data on authenticated sites. Do not share source from private account pages.
