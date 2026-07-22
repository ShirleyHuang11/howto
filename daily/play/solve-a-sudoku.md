---
name: solve-a-sudoku
domain: daily
subdomain: play
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 20min-1h
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

You can solve an easy Sudoku grid using singles, pencil candidates, and box-line elimination without guessing.

## Preconditions

- A standard 9 by 9 Sudoku puzzle with enough clues for a logical easy solve.
- Pencil and eraser, or an app that supports candidate notes.
- Basic rule knowledge: each row, column, and 3 by 3 box contains digits 1 through 9 once.

## Steps

1. **Read the givens.** Scan the grid and notice rows, columns, or boxes that are already crowded with numbers. → *Expect:* several areas look close to finished.
2. **Scan for obvious singles.** For each empty cell in a crowded unit, ask what digits are missing and whether only one can fit. → *Expect:* at least one cell has a forced value on easy puzzles.
3. **Place only certain numbers.** Write a digit large only when row, column, and box all agree. → *Expect:* every placed digit can be defended by the rules.
4. **Pencil candidates.** In unresolved cells, write small possible digits after eliminating numbers already present in the same row, column, and box. → *Expect:* each empty cell has a short candidate list.
5. **Find hidden singles.** In each row, column, and box, look for a digit that appears as a candidate in only one place. → *Expect:* some placements become forced even when a cell has multiple candidates.
6. **Use box-line elimination.** If all candidates for a digit inside one box sit on the same row or column, remove that digit from the rest of that row or column outside the box. → *Expect:* candidate lists shrink without guessing.
7. **Loop the logic.** [BRANCH: new single appears | no progress] If a single appears, place it and rescan; if no progress, recheck candidates for a missed elimination. → *Expect:* each solved number unlocks more cells.
8. **Finish cleanly.** Fill the last cells only when they are forced, then inspect every row, column, and box. → *Expect:* no digit repeats in any unit.

## Decision points

- If two numbers seem possible, do not guess on an easy grid; look elsewhere for a forced move.
- If a contradiction appears, the most recent uncertain placement or candidate removal needs audit.
- If the puzzle requires chains or trial branches, it may not be an easy puzzle.

## Failure modes & recovery

- **F1 Duplicate digit:** a row, column, or box repeats a number → erase back to the last confident step and rescan that unit.
- **F2 Candidate overload:** every cell has too many marks → fill candidates one box at a time and erase eliminated digits immediately.
- **F3 Guess spiral:** one guess creates many dependent guesses → undo the branch and return to singles.
- **F4 Missed hidden single:** progress stalls → search each digit 1 through 9 within one box before scanning the whole grid.

## Verification

All 81 cells are filled, and each row, column, and 3 by 3 box contains the digits 1 through 9 exactly once.

## Variations

- Some printed puzzles use dots or corners for candidates; keep your notation consistent.
- Apps may highlight mistakes, but turn off auto-check if you want to practice reasoning.
- Harder puzzles add pairs, triples, X-wings, and other techniques after these basics.

## Safety & privacy

Low risk. The main hazard is frustration; take breaks before erasing wildly, and avoid uploading personal screenshots if a puzzle page includes account information.
