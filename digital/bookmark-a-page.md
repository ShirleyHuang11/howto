---
name: bookmark-a-page
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

Save the current web page as a browser bookmark so it can be opened later.

## Preconditions

- The page you want to save is open.
- You are using the browser profile where you want the bookmark stored.

## Steps

1. **Confirm the page.** Check the title and address bar. → *Expect:* the page shown is the one you want to save.
2. **Open bookmark controls.** Press `Ctrl+D` on Windows/Linux or `Command+D` on Mac, or click the star in the address bar. → *Expect:* a bookmark dialog or popover opens.
3. **Choose a name and folder.** Edit the bookmark name if needed and select a folder such as Bookmarks Bar or Favorites. → *Expect:* the dialog shows the intended name and folder.
4. **Save the bookmark.** Click `Done`, `Save`, or the equivalent button. → *Expect:* the star or bookmark icon shows the page is saved.

## Decision points

- You need the bookmark visible often → save it to the bookmarks bar or favorites bar.
- The page is behind a login → bookmark the stable page address, not a temporary checkout or session URL.
- You are using a temporary profile → switch profiles before saving.

## Failure modes & recovery

- **F1 Bookmark saved in wrong folder:** detect it is missing from the expected bar or folder → open bookmark manager and move it.
- **F2 Duplicate bookmark:** detect the browser says the page is already saved → edit the existing bookmark instead of creating another.
- **F3 Temporary URL saved:** detect the bookmark later opens an error or expired page → navigate to the stable page and update the bookmark.

## Verification

The page appears in the selected bookmark folder and opens when clicked.

## Variations

- Chrome: use the star at the right side of the address bar or `Ctrl+D`/`Command+D`.
- Firefox: use the star in the address bar; clicking it again edits the bookmark.
- Safari: use `Bookmarks` > `Add Bookmark` or `Command+D`.

## Safety & privacy

Bookmarks can reveal private interests, accounts, or work projects to anyone using the same profile. Avoid saving sensitive pages in shared profiles.
