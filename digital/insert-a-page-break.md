---
name: insert-a-page-break
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Text after the cursor starts on a new page using a real page break.

## Preconditions

- A document is open in a word processor.
- You know where the new page should begin.

## Steps

1. **Place the cursor.** Click immediately before the content that should start on the next page. → *Expect:* the insertion cursor appears at the break point.
2. **Insert the page break.** Press `Ctrl+Enter` on Windows/Linux or `Command+Enter` on Mac, or choose Insert > Break > Page Break. → *Expect:* the following content moves to the top of the next page.
3. **Show breaks if needed.** Turn on paragraph marks or non-printing characters if the break is hard to see. → *Expect:* a page break marker is visible in the document.
4. **Review nearby pages.** Check the end of the previous page and the start of the next page. → *Expect:* no extra blank paragraphs or unwanted spacing appear.

## Decision points

- New formatting should begin after the break → use a section break instead of a simple page break.
- You only need more space before a heading → adjust paragraph spacing rather than pressing Enter many times.

## Failure modes & recovery

- **F1 Extra blank page appears:** detect: an empty page is inserted → recover by deleting extra paragraph marks around the break.
- **F2 Break is in the wrong place:** detect: the wrong content moves to the next page → recover by undoing and placing the cursor correctly.
- **F3 Manual blank lines were used:** detect: many empty paragraphs create the page change → recover by deleting them and inserting a real page break.

## Verification

The intended content starts at the top of the next page because of a page break, not repeated blank lines.

## Variations

- `word`: Layout > Breaks includes page, column, and section breaks.
- `google-docs`: Insert > Break > Page break inserts a printable page break.

## Safety & privacy

This is low risk. Check exported PDFs because page breaks affect final pagination.
