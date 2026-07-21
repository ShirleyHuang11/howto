---
name: play-hangman
domain: daily
subdomain: play
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Players run a fair word-guessing game where one player chooses a secret word and the other guesses letters before the drawing is completed.

## Preconditions

- Paper, pencil, and at least two players are available.
- Players agree on the number of wrong guesses allowed.
- The word chooser can spell the chosen word correctly.

## Steps

1. **Choose a fair word.** Pick a word or short phrase the guesser could reasonably know. → *Expect:* chooser can define and spell it.
2. **Draw blanks.** Write one blank for each letter, leaving spaces or slashes between words. → *Expect:* guesser sees word length but not letters.
3. **Draw the gallows.** Sketch the base and post, or choose another countdown drawing. → *Expect:* there is a clear wrong-guess track.
4. **Guess one letter.** Guesser says a single unused letter. → *Expect:* both players know whether it has been guessed before.
5. **Reveal or mark.** Fill every matching blank, or add one body part for a miss. → *Expect:* the board changes after each valid guess.
6. **Track used letters.** Write incorrect and correct guessed letters off to the side. → *Expect:* repeats are easy to spot.
7. **Use strategy.** Guess common vowels and consonants, then infer word patterns. → *Expect:* guesses become more targeted.
8. **End the round.** [BRANCH: all blanks filled, guesser wins | drawing completed, chooser reveals word] → *Expect:* result is clear to both players.

## Decision points

- Word has repeated letters → reveal every occurrence at once.
- Guesser repeats a letter → do not penalize if used-letter tracking was unclear.
- Phrase includes punctuation → show punctuation before guessing starts.
- Players dislike the gallows image → use a flower, snowman, or countdown boxes.
- Skill levels differ → chooser picks a shorter or more familiar word.

## Failure modes & recovery

- **F1 Unfair word:** detect obscure names or misspellings; recover by choosing from an agreed category.
- **F2 Missed duplicate:** detect one guessed letter hidden in another spot; recover by filling all copies immediately.
- **F3 Argument over repeats:** detect disagreement about penalty; recover by using the written used-letter list.
- **F4 Too few guesses:** detect game ending before useful clues appear; recover by adding parts to the drawing.
- **F5 Revealed word early:** detect accidental spoken clue; recover by restarting with a new word.

## Verification

The final board either has every letter filled before the wrong-guess limit or shows the completed countdown with the secret word revealed.

## Variations

- Category hangman: announce a category such as animals, movies, or foods.
- Team play: teams alternate letter guesses and discuss quietly.
- Whiteboard play: use magnets or a board for repeat rounds.

## Safety & privacy

Low risk. Use neutral words and avoid secret phrases that reveal private information or target another player.
