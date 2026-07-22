---
name: solve-a-crossword
domain: daily
subdomain: play
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Solve a crossword by filling sure answers first, using crossing letters, spotting the theme, and recognizing wordplay.

## Preconditions

- A crossword grid and clue list.
- A pencil, erasable pen, or digital equivalent.
- Familiarity with across and down numbering.
- Permission to check answers only after trying.

## Steps

1. **Scan the easy clues.** Fill answers you know immediately, especially short common words and proper names. → *Expect:* several entries appear without guessing.
2. **Mark uncertain fills.** Write light letters or small notes for maybes. → *Expect:* doubtful answers look different from confirmed ones.
3. **Use crossings.** For each blank, check the across and down letters that intersect it. → *Expect:* a guessed word either strengthens or starts to fail.
4. **Look for the theme.** Read long clues and repeated clue patterns. → *Expect:* a trick or shared idea explains several answers.
5. **Watch wordplay tells.** Clues ending with question marks, odd grammar, or tiny words often signal puns or indirect meanings. → *Expect:* literal readings give way to playful answers.
6. **Fill by pattern.** Use known letters, word length, and clue tense or part of speech. → *Expect:* fewer words fit the available spaces.
7. **Work the stuck corner.** [BRANCH: many crossings | few crossings] solve from crossings if available, or move elsewhere to collect letters. → *Expect:* the hard area gains at least one anchor.
8. **Walk away briefly.** Stop for a few minutes when the same wrong idea repeats. → *Expect:* returning makes alternate meanings easier to see.
9. **Clean the grid.** Erase failed guesses and write final answers clearly. → *Expect:* every filled entry agrees with its crossings.

## Decision points

- A clue has an abbreviation → the answer may also be abbreviated.
- A clue uses past tense, plural, or comparison → the answer usually matches that grammar.
- A theme answer looks wrong literally → test whether it follows the puzzle's joke.
- The puzzle is from a hard source → expect more misdirection and less common vocabulary.

## Failure modes & recovery

- **F1 Confident wrong fill:** detect many crossings fighting one answer → erase it and re-solve from intersecting clues.
- **F2 Theme missed:** detect long answers that feel unrelated → compare them for repeated transformations.
- **F3 Spelling trap:** detect one square causing multiple conflicts → check names, foreign words, and variant spellings.
- **F4 Fatigue loop:** detect rereading clues without new letters → take a break and return later.

## Verification

Every square is filled, each across and down answer satisfies its clue, and no crossing letters contradict each other.

## Variations

- Cryptic crosswords require separate rules for definitions and wordplay.
- Mini crosswords reward fast first passes because the grid has fewer crossings.
- Themed weekday puzzles often get harder from Monday to Saturday.

## Safety & privacy

No personal data is needed; avoid writing private notes on a shared newspaper or public puzzle sheet.
⚠️ *Irreversible:* Ink can make wrong guesses hard to fix, so use pencil when learning.
