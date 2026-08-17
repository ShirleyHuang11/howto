---
name: insert-a-hyperlink
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Selected text becomes a clickable hyperlink to the intended web page, email address, or document location.

## Preconditions

- A document or rich text editor is open.
- You have the exact URL, email address, or destination to link to.

## Steps

1. **Select the link text.** Highlight the word or phrase readers should click. → *Expect:* the intended display text is highlighted.
2. **Open the link dialog.** Press `Ctrl+K` on Windows/Linux or `Command+K` on Mac, or choose Insert > Link. → *Expect:* a link box or dialog appears.
3. **Enter the destination.** Paste the full URL, email address, or document target into the link field. → *Expect:* the destination appears in the link field.
4. **Apply the link.** Click Apply, OK, or press `Enter`. → *Expect:* the selected text changes to link styling, usually blue and underlined.
5. **Test the link.** Hold `Ctrl` or `Command` if required and click the linked text. → *Expect:* the intended page, email draft, or target opens.

## Decision points

- Link text is a raw URL → keep it only when the exact address matters; otherwise use descriptive text.
- Link points to a private file → confirm recipients have permission before sharing.

## Failure modes & recovery

- **F1 Link opens the wrong page:** detect: the tested destination is not intended → recover by editing the link and replacing the URL.
- **F2 Text did not become clickable:** detect: clicking only moves the cursor → recover by selecting the text and applying Insert > Link again.
- **F3 Recipient cannot open it:** detect: access denied or sign-in required → recover by changing sharing permissions or using a public destination.

## Verification

The selected text is clickable and opens the intended destination when tested.

## Variations

- `word`: Insert > Link can link to files, web pages, email addresses, and headings.
- `google-docs`: Insert > Link can suggest headings and bookmarks in the document.

## Safety & privacy

Links can expose private document locations or tracking URLs. Test the destination and avoid linking to sensitive files without permission checks.
