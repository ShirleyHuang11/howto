---
name: freeze-a-header-row
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

Keep the header row visible while scrolling through a spreadsheet.

## Preconditions

- A spreadsheet is open.
- The first row or another top row contains column labels.

## Steps

1. **Identify the header row.** Scroll to the top of the sheet and confirm which row contains labels. → *Expect:* the header row is visible.
2. **Freeze the header.** [BRANCH: Excel | Google Sheets] Excel: choose `View > Freeze Panes > Freeze Top Row`; Google Sheets: choose `View > Freeze > 1 row`. → *Expect:* a freeze line appears below the header row.
3. **Test the scroll.** Scroll down several rows. → *Expect:* the header row stays visible at the top of the grid.

## Decision points

- Header is not row 1 → select the row below the header, then use `View > Freeze Panes` in Excel or `View > Freeze > Up to row current row` in Google Sheets.
- Need frozen columns too → use the freeze menu for columns after freezing rows.
- Need to undo → choose `View > Freeze Panes > Unfreeze Panes` in Excel or `View > Freeze > No rows` in Google Sheets.

## Failure modes & recovery

- **F1 Wrong row frozen:** detect a blank or data row stays visible → unfreeze, select the correct row position, and freeze again.
- **F2 Freeze option disabled:** detect the menu item is unavailable → finish editing the current cell and try again.
- **F3 Printed output unchanged:** detect headers do not repeat on printed pages → set print titles separately in page setup.

## Verification

After scrolling down, the intended header row remains visible above the moving data rows.

## Variations

- `excel`: `Freeze Top Row` always freezes row 1.
- `google-sheets`: The gray freeze handle near row numbers can also be dragged below the header.

## Safety & privacy

Low risk. Freezing rows changes only the view, not the data.
