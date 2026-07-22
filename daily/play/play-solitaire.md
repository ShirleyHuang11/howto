---
name: play-solitaire
domain: daily
subdomain: play
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Play Klondike solitaire by building tableau stacks, moving aces to foundations, and recognizing when the game is stuck.

## Preconditions

- A shuffled standard 52-card deck.
- A table with room for seven columns, four foundations, and a stock pile.
- Basic knowledge of suits, ranks, and alternating colors.
- No jokers in the deck.

## Steps

1. **Lay the tableau.** Deal seven columns from left to right, with one card in the first column through seven in the last. → *Expect:* the columns form a staircase of card counts.
2. **Turn top cards face up.** Flip only the top card of each column. → *Expect:* seven visible cards are available for play.
3. **Place the stock.** Put the remaining deck face down above the tableau, leaving space for a waste pile and four foundations. → *Expect:* the layout has all working areas.
4. **Move aces up.** Send any exposed ace to an empty foundation spot. → *Expect:* each ace starts a suit pile.
5. **Build down in color.** Move face-up cards onto the next higher rank of the opposite color. → *Expect:* a red 7 can sit on a black 8, and similar moves are legal.
6. **Move stacks.** Move a face-up sequence together if it already alternates colors and descends by rank. → *Expect:* the whole legal run lands on a matching destination.
7. **Fill empty columns.** Move only a king, or a stack headed by a king, into an empty tableau column. → *Expect:* empty spaces become useful without breaking the rules.
8. **Turn the stock.** [BRANCH: draw one | draw three] reveal waste cards by the chosen rule and play the top available waste card. → *Expect:* new cards enter play without changing the tableau illegally.
9. **Stop when stuck.** If no tableau, waste, or foundation move exists, turn through the stock until a move appears or the cycle repeats. → *Expect:* you either find progress or identify a lost position.

## Decision points

- Draw-one is easier → use it while learning.
- Draw-three is traditional in many sets → only the top waste card is playable.
- A face-down tableau card can be uncovered → prefer moves that reveal it.
- A foundation move might trap a needed card → delay it if that rank is still useful in the tableau.

## Failure modes & recovery

- **F1 Illegal color build:** detect two same-color cards stacked together → undo the move and rebuild by alternating colors.
- **F2 Wrong foundation suit:** detect mixed suits in one foundation → return cards to the last legal state.
- **F3 Lost stock order:** detect waste cards shuffled by accident → restart because the draw order matters.
- **F4 False stuck claim:** detect an unplayed ace, king space, or legal stack move → make that move before ending.

## Verification

The game is successful if all 52 cards end on the four suit foundations from ace through king.

## Variations

- Vegas scoring counts passes through the stock and awards points for foundation cards.
- Relaxed solitaire allows unlimited stock passes.
- Turn-three solitaire is harder because fewer waste cards are immediately available.

## Safety & privacy

There is no meaningful privacy risk, but keep small cards away from toddlers and pets.
⚠️ *Irreversible:* Do not mix the waste or stock midgame unless you are choosing to restart.
