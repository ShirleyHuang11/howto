---
name: calculate-an-average
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

Calculate the arithmetic average of a spreadsheet range.

## Preconditions

- A spreadsheet contains numeric values.
- There is an empty cell for the average result.

## Steps

1. **Select the result cell.** Click the empty cell where the average should appear. → *Expect:* the result cell is active.
2. **Enter the average formula.** Type `=AVERAGE(C2:C20)`, replacing `C2:C20` with the actual range. → *Expect:* the formula appears with the range highlighted.
3. **Confirm the formula.** Press `Enter` or `Return`. → *Expect:* the average appears in the result cell.
4. **Check the range.** Click the result cell and inspect the formula bar. → *Expect:* the formula includes only the intended numeric cells.

## Decision points

- Need to ignore zeros → use `=AVERAGEIF(C2:C20,"<>0")`.
- Need an average with conditions → use `=AVERAGEIF(B2:B20,"West",C2:C20)` or `=AVERAGEIFS(C2:C20,B2:B20,"West")`.
- Need weighted average → use `=SUMPRODUCT(C2:C20,D2:D20)/SUM(D2:D20)`.

## Failure modes & recovery

- **F1 Blank cells misunderstood:** detect the average differs from manual expectation → remember blanks are ignored, while zeros are included.
- **F2 Text numbers ignored:** detect numeric-looking cells not counted → convert the range to numbers and recalculate.
- **F3 Divide-by-zero error:** detect `#DIV/0!` → make sure the range contains at least one numeric value.

## Verification

The result cell contains an `AVERAGE`, `AVERAGEIF`, or weighted-average formula, and its range matches the intended values.

## Variations

- `excel`: Use `Home > AutoSum > Average` after selecting the result cell.
- `google-sheets`: Use `Insert > Function > AVERAGE` or type the formula directly.

## Safety & privacy

Low risk. Averages can hide outliers, so review the source range before reporting the result.
