---
name: split-text-into-columns
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 4min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Split text from one spreadsheet column into separate columns using a delimiter.

## Preconditions

- A column contains combined text such as `First Last` or `City, State`.
- Empty columns exist to the right for the split results.

## Steps

1. **Back up nearby data.** Confirm the columns to the right are empty or insert new blank columns. → *Expect:* split output will not overwrite important data.
2. **Select the text column.** Click the column letter or select the cells to split. → *Expect:* the combined text cells are highlighted.
3. **Open split tools.** [BRANCH: Excel | Google Sheets] Excel: choose `Data > Text to Columns`; Google Sheets: choose `Data > Split text to columns`. → *Expect:* split options appear.
4. **Choose the delimiter.** Select comma, space, tab, semicolon, or custom delimiter. → *Expect:* the preview shows text separated into the expected columns.
5. **Apply the split.** Finish the wizard in Excel or accept the delimiter in Google Sheets. → *Expect:* each part appears in its own column.

## Decision points

- Delimiter appears inside values → use a more precise delimiter or clean the source text first.
- Need a formula instead → use `=SPLIT(A2,",")` in Google Sheets or `=TEXTSPLIT(A2,",")` in current Excel.
- Existing data sits to the right → insert blank columns before splitting.

## Failure modes & recovery

- **F1 Data overwritten:** detect replaced cells to the right → undo immediately, insert blank columns, and repeat.
- **F2 Wrong delimiter:** detect unsplit text or too many columns → undo and choose the correct delimiter.
- **F3 Extra spaces:** detect leading spaces in results → trim with `=TRIM(B2)` or find and replace double spaces.

## Verification

The original combined text is separated into adjacent columns, and no intended data to the right was overwritten.

## Variations

- `excel`: The Text to Columns wizard includes fixed-width splitting for aligned text.
- `google-sheets`: The separator dropdown can detect delimiters automatically.

## Safety & privacy

Low risk. Splitting names, addresses, or IDs can expose personal data in more columns, so review sharing permissions.
