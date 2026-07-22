---
name: do-a-word-search
domain: daily
subdomain: play
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Find all listed words in a word search by scanning systematically in every allowed direction.

## Preconditions

- A word-search grid and word list.
- A pencil, highlighter, or erasable marker.
- Enough light to distinguish similar letters.
- Agreement about whether diagonal and backward words are allowed.

## Steps

1. **Read the rules.** Check whether words can run forward, backward, vertical, horizontal, or diagonal. → *Expect:* every allowed direction is known.
2. **Pick one word.** Start with a word that has an uncommon first letter or unusual letter pair. → *Expect:* the search target is specific.
3. **Scan first letters.** Move row by row looking only for the first letter of that word. → *Expect:* possible start points stand out.
4. **Check all directions.** From each start point, trace the next letters outward in every allowed direction. → *Expect:* most false starts fail within a few letters.
5. **Mark the find.** Circle or highlight the complete word without covering nearby letters. → *Expect:* the found word is visible and still readable.
6. **Cross off the list.** Mark the word on the word list immediately. → *Expect:* completed targets are not searched again.
7. **Sweep systematically.** [BRANCH: by word | by grid] either repeat word by word, or scan each row, column, and diagonal for any listed word. → *Expect:* the number of unmarked words shrinks steadily.
8. **Recheck leftovers.** For remaining words, search by last letter too because words may be backward. → *Expect:* missed reverse words become easier to spot.
9. **Finish the grid.** Inspect crowded intersections and edges one final time. → *Expect:* every listed word is found or clearly not present.

## Decision points

- A word has double letters → use the double letter pair as a search anchor.
- Many words start with the same letter → scan by rare second or third letters.
- The grid is large → use a ruler or blank paper to keep rows straight.
- A word seems absent → verify spelling before assuming a printing error.

## Failure modes & recovery

- **F1 Direction missed:** detect unfound words despite many first letters → include diagonals and backward paths.
- **F2 Overmarked grid:** detect highlighter covering letters → switch to light circles or underline marks.
- **F3 Skipped row:** detect uneven scanning progress → restart the sweep with a finger or ruler guide.
- **F4 Word-list mismatch:** detect a word with spelling different from the grid → search for both spellings, then note the mismatch.

## Verification

Every word in the list is crossed off and its full letter path is marked in the grid.

## Variations

- Timed word searches reward scanning by rare letters first.
- Classroom versions may hide vocabulary diagonally only after students know the terms.
- Digital grids may let you drag from first letter to last letter.

## Safety & privacy

Use washable markers with children, and avoid marking library books or borrowed puzzle pages.
⚠️ *Irreversible:* Permanent marker can bleed through paper, so test it off the puzzle first.
