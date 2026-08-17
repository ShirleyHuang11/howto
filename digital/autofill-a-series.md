---
name: autofill-a-series
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

Fill a spreadsheet range with a continuing number, date, or text series.

## Preconditions

- A spreadsheet is open.
- You know the starting pattern, such as `1, 2` or `Jan, Feb`.

## Steps

1. **Enter the starting values.** Type the first two values of the series in adjacent cells, such as `1` and `2`. → *Expect:* the pattern cells contain the seed values.
2. **Select the seed cells.** Highlight both starting cells. → *Expect:* a border surrounds the selected pattern.
3. **Drag the fill handle.** Drag the small square at the selection corner across or down the target range. → *Expect:* a preview or outline extends over the cells to fill.
4. **Release to fill.** Let go at the last target cell. → *Expect:* the cells fill with the continued series.
5. **Check the pattern.** Review the last few filled values. → *Expect:* the sequence follows the intended increment or calendar pattern.

## Decision points

- Need repeated copies instead of a series → enter one value, drag, then choose copy cells from the autofill options if available.
- Need weekdays only → use fill options in Excel or create a formula-based series.
- Need formulas copied → verify relative and absolute references before filling.

## Failure modes & recovery

- **F1 Values copied instead of incremented:** detect repeated values → undo, select at least two seed values, and drag again.
- **F2 Wrong increment:** detect the sequence jumps incorrectly → seed with the exact first two values that define the pattern.
- **F3 Formula references drift:** detect copied formulas point to wrong cells → use `$` absolute references where needed.

## Verification

The filled range contains a continuous series that matches the seed pattern through the final cell.

## Variations

- `excel`: Use `Home > Fill > Series` for precise step values and stop values.
- `google-sheets`: Autofill recognizes common date, month, and number patterns.

## Safety & privacy

Low risk. Autofill can overwrite existing cells if dragged too far, so confirm the destination range is empty or replaceable.
