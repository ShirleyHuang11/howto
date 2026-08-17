---
name: remove-duplicate-rows
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

Remove duplicate rows from a spreadsheet range based on selected columns.

## Preconditions

- A spreadsheet contains repeated rows or repeated key values.
- You know which columns define a duplicate.

## Steps

1. **Make a reversible copy.** Duplicate the sheet or copy the table to a new sheet. → *Expect:* an unchanged backup exists in the workbook.
2. **Select the data range.** Highlight the table including headers if present. → *Expect:* all rows to check are selected.
3. **Open duplicate removal.** [BRANCH: Excel | Google Sheets] Excel: choose `Data > Remove Duplicates`; Google Sheets: choose `Data > Data cleanup > Remove duplicates`. → *Expect:* a duplicate removal dialog opens.
4. **Choose comparison columns.** Check the columns that must match for a row to count as duplicate. → *Expect:* only the intended key columns are selected.
5. **Remove duplicates.** Confirm the dialog. → *Expect:* the app reports how many duplicate rows were removed and how many unique rows remain.

## Decision points

- Need to inspect duplicates first → use conditional formatting or a helper formula such as `=COUNTIF(A:A,A2)>1`.
- Duplicate means same entire row → select all columns.
- Duplicate means same ID only → select only the ID column.

## Failure modes & recovery

- **F1 Wrong rows removed:** detect expected records missing → restore from the copied sheet or undo immediately.
- **F2 Header treated as data:** detect header removed or counted → undo and enable `My data has headers` or `Data has header row`.
- **F3 Near-duplicates remain:** detect values differing only by spaces or case → clean with `TRIM` or standardize case, then repeat.

## Verification

The cleaned range has no repeated rows according to the selected comparison columns, and the backup sheet still contains the original data.

## Variations

- `excel`: `Data > Remove Duplicates` can compare any combination of columns.
- `google-sheets`: Use `Data cleanup > Cleanup suggestions` to inspect possible duplicates before removing them.

## Safety & privacy

Low risk, but duplicate removal deletes rows from the active range. Keep the backup until the result is verified.
