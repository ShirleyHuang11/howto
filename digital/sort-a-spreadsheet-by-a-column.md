---
name: sort-a-spreadsheet-by-a-column
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 3min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Sort rows in a spreadsheet by the values in one column while keeping each row's data together.

## Preconditions

- The sheet contains a rectangular data range.
- Each column has a clear header row, or you know whether headers are absent.

## Steps

1. **Select the data range.** Click any cell in the data table or drag across the full range. → *Expect:* the table or intended range is active.
2. **Open sort.** [BRANCH: Excel | Google Sheets] Excel: choose `Data > Sort`; Google Sheets: choose `Data > Sort range > Advanced range sorting options`. → *Expect:* a sort dialog opens.
3. **Set header handling.** Check `My data has headers` in Excel or `Data has header row` in Google Sheets if the first row is labels. → *Expect:* column names, not row values, appear as sort choices.
4. **Choose the sort column and order.** Select the column, then choose ascending `A to Z` or descending `Z to A`. → *Expect:* the dialog shows the intended column and direction.
5. **Apply the sort.** Click `OK` in Excel or `Sort` in Google Sheets. → *Expect:* rows reorder and values in the sort column follow the chosen order.

## Decision points

- Only one column is selected → cancel and select the full table so rows do not become mismatched.
- Need a secondary sort → add another sort level in the same dialog.
- Data is shared with others → consider creating a filter view in Google Sheets instead of changing everyone’s row order.

## Failure modes & recovery

- **F1 Rows misaligned:** detect names, dates, or amounts no longer match → immediately undo with `Ctrl+Z` or `Command+Z`.
- **F2 Header sorted into data:** detect header labels moved down → undo, then enable the header row option.
- **F3 Mixed number text order:** detect values sorting like `1, 10, 2` → convert text numbers to numeric values and sort again.

## Verification

The full rows remain intact, the selected column is in ascending or descending order, and the header row remains at the top if one exists.

## Variations

- `excel`: Use `Home > Sort & Filter > Custom Sort` for the same dialog.
- `google-sheets`: Use `Data > Create a filter` for temporary per-column sorting.

## Safety & privacy

Low risk. Sorting can change shared analysis; keep an untouched copy or use undo if row relationships look wrong.
