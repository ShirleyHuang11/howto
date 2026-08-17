---
name: copy-a-link-address
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

Copy a link's destination URL without opening it.

## Preconditions

- A page with a link is open.
- You have somewhere safe to paste the copied address.

## Steps

1. **Point at the link.** Move the pointer over the link text, button, or image. → *Expect:* the cursor changes or the browser shows a destination preview.
2. **Open the link menu.** Right-click the link, or `Control`-click it on Mac. → *Expect:* a context menu with link actions appears.
3. **Copy the address.** Choose `Copy Link Address`, `Copy Link`, or `Copy Link Location`. → *Expect:* the URL is placed on the clipboard.
4. **Paste where needed.** Click the destination field or document and press `Ctrl+V` or `Command+V`. → *Expect:* the copied URL appears as text.

## Decision points

- The link is shortened → paste it into a note first and inspect it before sharing or opening.
- The link includes personal tokens → do not share it publicly.
- The page blocks right-click → use the browser status preview or open developer tools only if appropriate.

## Failure modes & recovery

- **F1 Page text copied instead:** detect pasted text is not a URL → right-click directly on the link, not nearby text.
- **F2 Temporary link copied:** detect long tracking or session parameters → copy a cleaner canonical link if the site provides one.
- **F3 Clipboard overwritten:** detect a different item pastes → copy the link again.

## Verification

Pasting from the clipboard produces the link destination URL you intended to copy.

## Variations

- Chrome: the menu item is usually `Copy link address`.
- Firefox: the menu item is usually `Copy Link`.
- Safari: the menu item is usually `Copy Link`.

## Safety & privacy

Copied URLs can include account, referral, tracking, reset, invite, or unsubscribe tokens. Inspect the link before sharing it.
