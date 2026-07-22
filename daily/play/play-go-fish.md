---
name: play-go-fish
domain: daily
subdomain: play
locale: [generic]
interface: physical
difficulty: basic
est_time: 15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Play Go Fish by asking for ranks, collecting books of four, and ending with the most books.

## Preconditions

- A standard deck without jokers.
- Two to six players.
- A draw pile in the center after the deal.
- Players know ranks such as 2, 7, jack, and ace.

## Steps

1. **Deal the hands.** Deal seven cards each for two or three players, or five cards each for four or more players. → *Expect:* every player has the agreed starting count.
2. **Place the pond.** Put the remaining deck face down in the center. → *Expect:* the draw pile is reachable by all players.
3. **Start the turn.** The player left of the dealer asks one other player for a rank they already hold. → *Expect:* the request is legal because the asker has at least one card of that rank.
4. **Give matching cards.** If asked, hand over all cards of that rank. → *Expect:* the asker receives every matching card from that player.
5. **Continue after a hit.** The asker takes another turn after receiving one or more cards. → *Expect:* successful asking keeps control.
6. **Say go fish.** If the asked player has none, they say "go fish" and the asker draws one card. → *Expect:* a new card enters the asker's hand.
7. **Play a drawn match.** If the drawn card is the requested rank, the asker shows it and goes again. → *Expect:* a lucky draw extends the turn.
8. **Make books.** Place four of the same rank face up in front of you as soon as you collect them. → *Expect:* completed books leave your hand and count as points.
9. **End the game.** [BRANCH: pond remains | pond empty] keep drawing while cards remain, or play out hands when the pond is empty. → *Expect:* the game ends when all books are made or no legal play remains.

## Decision points

- You have several ranks → ask for the rank most likely held by the target player.
- A player asks you for a rank → remember that clue for later turns.
- A player runs out of cards while the pond remains → draw a new hand according to house rules.
- Younger players forget ranks → allow open reminders without revealing whole hands.

## Failure modes & recovery

- **F1 Asked rank not held:** detect the asker cannot show that rank if challenged → cancel the ask and choose a held rank.
- **F2 Partial handover:** detect one matching card kept back → give all matching cards and resume.
- **F3 Missed book:** detect four of a rank still in a hand → place the book immediately.
- **F4 Empty pond confusion:** detect a player told to draw from no pile → skip the draw and pass the turn.

## Verification

All completed books are face up, no cards remain in play, and the player with the most books is declared the winner.

## Variations

- Pair version: make pairs instead of books for very young players.
- Memory-heavy version: forbid writing clues down.
- Team version: partners may not show cards unless the rules allow table talk.

## Safety & privacy

Keep hands hidden, but avoid teasing players who forget a clue or rank.
⚠️ *Irreversible:* Once a card is fairly revealed or handed over, treat that information as part of the game.
