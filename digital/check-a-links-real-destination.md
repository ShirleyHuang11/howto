---
name: check-a-links-real-destination
domain: digital
locale: [generic]
interface: web
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Check where a link really goes before opening it or entering information.

## Preconditions

- A link is visible in a browser, email, document, or message.
- You can see or copy the link without clicking it.

## Steps

1. **Hover without clicking.** Move the pointer over the link and keep the mouse button untouched. → *Expect:* the browser or app shows a destination preview.
2. **Read the domain.** Look for the main domain immediately before the first single slash after `https://`. → *Expect:* the domain matches the organization you expect.
3. **Check for lookalikes.** Compare spelling, extra words, hyphens, and unusual endings such as `.zip` or unfamiliar country codes. → *Expect:* the domain does not rely on a confusing imitation.
4. **Copy if you need a closer look.** Right-click and choose `Copy Link Address`, then paste into a plain text note. → *Expect:* the full URL is visible as text.
5. **Open only if it matches.** Use a new tab or type the known official site manually if uncertain. → *Expect:* you either reach the expected site or avoid opening the suspicious link.

## Decision points

- The visible text and destination differ → trust the destination preview, not the visible text.
- The link is shortened → expand it with a trusted link checker or ask the sender.
- The link asks for sign-in or payment → navigate to the official site manually.

## Failure modes & recovery

- **F1 Preview hidden:** detect no destination appears on hover → copy the link address and inspect it in plain text.
- **F2 Misread domain:** detect a subdomain or lookalike fooled you → identify the registered domain before clicking.
- **F3 Opened suspicious link:** detect an unexpected page, download, or login form → close it, do not enter data, and scan downloads.

## Verification

The link's real destination domain is identified, and it matches the expected organization before any sensitive action.

## Variations

- Chrome: the destination preview appears in the lower-left corner of the window.
- Firefox: the destination preview appears near the bottom of the window.
- Safari: enable `View` > `Show Status Bar` if link previews are not visible.

## Safety & privacy

Do not enter passwords, payment details, or recovery codes after following an uncertain link. Manual navigation to the known official domain is safer.
