---
name: use-conditional-formatting
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

Highlight spreadsheet cells automatically when they match a rule.

## Preconditions

- A spreadsheet contains values to evaluate.
- You know the condition to highlight, such as values greater than `100`.

## Steps

1. **Select the cells to format.** Drag across the range where the rule should apply. → *Expect:* the target range is highlighted.
2. **Open conditional formatting.** [BRANCH: Excel | Google Sheets] Excel: choose `Home > Conditional Formatting > Highlight Cells Rules`; Google Sheets: choose `Format > Conditional formatting`. → *Expect:* conditional formatting options appear.
3. **Choose the rule.** Select a condition such as `Greater Than` and enter `100`, or use a custom formula such as `=$B2="Late"`. → *Expect:* the rule shows the intended condition.
4. **Choose the style.** Pick a fill color or text style that will mark matching cells. → *Expect:* a preview or sample shows the selected style.
5. **Apply the rule.** Click `OK` in Excel or `Done` in Google Sheets. → *Expect:* cells matching the rule are highlighted.

## Decision points

- Need to highlight whole rows → use a custom formula with locked column references, such as `=$B2="Late"`.
- Need color scale instead of a yes/no rule → choose a color scale rule.
- Rule should ignore blanks → add a condition such as `=AND($B2<>"",$B2>100)`.

## Failure modes & recovery

- **F1 Rule applies to wrong range:** detect highlights outside the intended cells → edit the `Applies to` range.
- **F2 Relative reference shifts incorrectly:** detect only some rows highlight correctly → lock columns or rows with `$` in the custom formula.
- **F3 Conflicting rules:** detect unexpected colors → open rule management and reorder, edit, or remove overlapping rules.

## Verification

At least one cell that meets the condition is highlighted, a cell that does not meet it is unhighlighted, and the rule's applied range matches the selected cells.

## Variations

- `excel`: Manage existing rules with `Home > Conditional Formatting > Manage Rules`.
- `google-sheets`: Existing rules appear in the right-side Conditional format rules panel.

## Safety & privacy

Low risk. Highlighting can draw attention to sensitive records such as low scores, late payments, or health values in shared files.
