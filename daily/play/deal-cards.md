---
name: deal-cards
domain: daily
subdomain: play
locale: [generic]
interface: physical
difficulty: basic
est_time: 3min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Deal cards fairly so each player receives the right count in the right order for the game.

## Preconditions

- A shuffled deck suitable for the game.
- Players seated around a table.
- The card count for the chosen game is known.
- Agreement about who deals first.

## Steps

1. **Square the deck.** Tap all four edges and hold the deck face down. → *Expect:* the cards form one clean stack.
2. **Offer the cut.** Place the deck near the player to the dealer's right or according to local custom. → *Expect:* another player lifts part of the deck and completes the cut.
3. **Name the count.** Say how many cards each player gets for this game. → *Expect:* every player hears the target number before the deal starts.
4. **Start with the next player.** Deal one card face down to the player on your left, then continue clockwise. → *Expect:* the dealer receives a card last in each round.
5. **Deal one at a time.** Give one card per player per pass until the count is reached. → *Expect:* all hands grow evenly.
6. **Keep the packet low.** Slide or toss cards gently so faces stay hidden. → *Expect:* no card flips or exposes its value.
7. **Check the count.** Ask players to count their hands without showing faces. → *Expect:* each hand has the correct number.
8. **Apply the deal-again rule.** [BRANCH: clean deal | exposed or wrong count] keep playing if clean, or collect, reshuffle, cut, and redeal if fairness broke. → *Expect:* the table agrees the deal stands or restarts.

## Decision points

- A game deals counterclockwise → follow the rule announced before the first card.
- A card flips face up during the deal → use the game's exposed-card rule, or redeal if none was agreed.
- A player receives too many or too few cards → redeal unless the game has a specific correction.
- The deck runs out early → stop and verify the game uses enough cards for the player count.

## Failure modes & recovery

- **F1 Miscounted hand:** detect uneven hand sizes → collect every card, shuffle, cut, and deal again.
- **F2 Exposed card:** detect a face-up card during the deal → pause and follow the deal-again rule.
- **F3 Skipped player:** detect one player behind by a card → restart if any hidden order may be known.
- **F4 Unclear direction:** detect two players reaching at once → announce clockwise and restart the current deal.

## Verification

Every player has the required number of face-down cards, no exposed-card dispute remains, and the table agrees play can begin.

## Variations

- Poker often rotates the deal and uses blinds or antes before cards are dealt.
- Some trick-taking games deal in packets, but the count and direction still need to be explicit.
- Children's games may deal face up when learning, then switch to hidden hands.

## Safety & privacy

Keep hands private unless the game says otherwise, and do not peek while helping younger players count.
⚠️ *Irreversible:* Once play starts, a bad deal is harder to unwind, so check counts before the first move.
