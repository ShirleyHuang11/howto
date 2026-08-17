---
name: add-a-dropdown-list-to-a-cell
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Add a dropdown list to one or more spreadsheet cells so users choose from allowed values.

## Preconditions

- A spreadsheet is open.
- You know the allowed values, such as `Open`, `In progress`, and `Done`.

## Steps

1. **Select the input cells.** Highlight the cells that should have the dropdown. → *Expect:* the target input cells are selected.
2. **Open data validation.** [BRANCH: Excel | Google Sheets] Excel: choose `Data > Data Validation`; Google Sheets: choose `Data > Data validation`. → *Expect:* validation settings appear.
3. **Choose list criteria.** [BRANCH: Excel | Google Sheets] Excel: choose `Allow: List`; Google Sheets: choose `Dropdown` or `Dropdown from a range`. → *Expect:* list settings are active.
4. **Enter allowed values.** Type values separated by commas, such as `Open,In progress,Done`, or select a source range. → *Expect:* the allowed values are listed in the validation settings.
5. **Save the validation.** Click `OK` in Excel or `Done` in Google Sheets. → *Expect:* a dropdown arrow or chip appears when a target cell is selected.
6. **Test the dropdown.** Click a target cell and choose one allowed value. → *Expect:* the cell fills with the selected value.

## Decision points

- List changes often → store options in a source range and point the dropdown to that range.
- Invalid entries should be blocked → set validation to reject invalid input rather than warn.
- Need colors in Google Sheets → assign dropdown option colors in the validation panel.

## Failure modes & recovery

- **F1 Dropdown missing:** detect no arrow or menu in the target cell → confirm the correct cells are selected and validation was saved.
- **F2 Values split incorrectly:** detect one option contains unwanted spaces or commas → edit the list or use a source range.
- **F3 Invalid entry accepted:** detect users can type anything → change validation behavior to reject invalid input.

## Verification

Each target cell offers only the intended dropdown choices, and selecting a choice writes that value into the cell.

## Variations

- `excel`: Source ranges for lists usually need to be on the same workbook and can use named ranges.
- `google-sheets`: Dropdown chips can display colors for status fields.

## Safety & privacy

Low risk. Dropdown options may reveal internal statuses or categories in shared sheets.
