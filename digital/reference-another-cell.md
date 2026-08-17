---
name: reference-another-cell
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

Use the value from another cell in a spreadsheet formula.

## Preconditions

- A spreadsheet is open.
- The source cell contains the value you want to reuse.

## Steps

1. **Select the destination cell.** Click the cell where the referenced value or calculation should appear. → *Expect:* the destination cell is active.
2. **Start a reference formula.** Type `=` and click the source cell, or type its address such as `=A2`. → *Expect:* the formula shows the source cell reference.
3. **Add calculation if needed.** Extend the formula, such as `=A2*1.08` or `=A2+B2`. → *Expect:* the complete formula appears in the cell or formula bar.
4. **Confirm the formula.** Press `Enter` or `Return`. → *Expect:* the destination cell displays the referenced value or calculated result.

## Decision points

- Reference should not move when copied → use an absolute reference such as `=$A$2`.
- Only the column should stay fixed → use `$A2`.
- Only the row should stay fixed → use `A$2`.

## Failure modes & recovery

- **F1 Wrong source cell:** detect the result matches the wrong value → edit the formula reference.
- **F2 Reference changes after copying:** detect copied formulas point to shifted cells → add `$` to make the needed part absolute.
- **F3 Circular reference:** detect a circular reference warning → move the formula to a cell outside its own dependency path.

## Verification

Changing the source cell changes the destination result, and the formula bar shows the intended cell reference.

## Variations

- `excel`: Press `F4` while editing a reference to cycle through absolute and relative forms.
- `google-sheets`: Press `F4` or `Fn+F4` on some keyboards to cycle reference locking.

## Safety & privacy

Low risk. Referenced cells may pull sensitive values into visible summary areas, so check destination visibility before sharing.
