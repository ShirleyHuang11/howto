---
name: filter-a-spreadsheet
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

Show only spreadsheet rows that match a chosen condition without deleting the other rows.

## Preconditions

- A spreadsheet table has column headers.
- You know which column and value should be used for filtering.

## Steps

1. **Select the table.** Click inside the data range. → *Expect:* a cell in the table is active.
2. **Turn on filters.** [BRANCH: Excel | Google Sheets] Excel: choose `Data > Filter`; Google Sheets: choose `Data > Create a filter`. → *Expect:* filter arrows or funnel icons appear in the header row.
3. **Open the target column filter.** Click the filter icon in the column header. → *Expect:* a menu with sort and filter options opens.
4. **Choose the condition.** Select values to show, or use a condition such as `Text contains` or `Greater than`. → *Expect:* the menu shows the intended filter rule.
5. **Apply the filter.** Click `OK` or confirm the menu. → *Expect:* nonmatching rows are hidden and row numbers may skip.

## Decision points

- Need multiple conditions → apply filters to additional columns.
- Need a private view in a shared Google Sheet → use `Data > Filter views > Create new filter view`.
- Need to remove the filter → choose `Data > Filter` again in Excel or `Data > Remove filter` in Google Sheets.

## Failure modes & recovery

- **F1 Missing headers:** detect filter icons on the wrong row → undo, add or select the header row, then enable filters again.
- **F2 Data seems deleted:** detect skipped row numbers or hidden rows → clear the filter from the column menu.
- **F3 Expected value absent:** detect a value missing from the filter checklist → check for extra spaces, spelling, or a different data type.

## Verification

Filter icons are visible, at least one row remains visible, hidden rows are not deleted, and every visible row matches the selected condition.

## Variations

- `excel`: Clear one column with `Data > Clear` while a filtered table is active.
- `google-sheets`: Filter views preserve other collaborators' current view.

## Safety & privacy

Low risk. Filters can hide relevant records during review, so clear filters before final audits or exports.
