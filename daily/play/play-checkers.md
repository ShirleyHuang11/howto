---
name: play-checkers
domain: daily
subdomain: play
locale: [generic]
interface: physical
difficulty: basic
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Play a basic game of checkers with correct setup, diagonal movement, forced jumps, kinging, and winning conditions.

## Preconditions

- An 8 by 8 checkerboard.
- Twelve dark pieces for each player.
- Agreement to use standard American checkers rules.
- A flat surface where pieces can stay centered on squares.

## Steps

1. **Orient the board.** Put a dark square in each player's left-hand corner. → *Expect:* pieces will move on dark squares only.
2. **Set the men.** Place each player's twelve pieces on the dark squares of the three rows closest to them. → *Expect:* two empty rows remain in the middle.
3. **Choose first player.** Let the player with dark pieces move first, or agree otherwise before starting. → *Expect:* turn order is clear.
4. **Move diagonally forward.** Move one piece one dark square diagonally toward the opponent. → *Expect:* the piece lands on an empty dark square.
5. **Jump when possible.** If an opposing piece is adjacent and the next dark square beyond it is empty, jump and remove the captured piece. → *Expect:* the jumped piece leaves the board.
6. **Continue multiple jumps.** Keep jumping with the same piece if another jump is available from its new square. → *Expect:* one turn may capture several pieces.
7. **Enforce forced jumps.** [BRANCH: jump exists | no jump] make a jump if one exists, otherwise make a normal move. → *Expect:* no player ignores a capture.
8. **King a piece.** When a man reaches the far row, stack another checker on it. → *Expect:* the king can move and jump diagonally forward or backward.
9. **Win the game.** Capture all opposing pieces or block all their legal moves. → *Expect:* the opponent has no playable turn.

## Decision points

- Multiple jumps are available → choose any legal jumping path.
- A man reaches the far row during a jump → stop there unless your house rules allow more jumping as a king.
- Players know international draughts → confirm rules because board size and movement differ.
- A player misses a forced jump → rewind to the missed turn if caught immediately.

## Failure modes & recovery

- **F1 Pieces on wrong color:** detect play on light squares → reset pieces to dark squares.
- **F2 Backward man move:** detect an uncrowned piece moving backward → undo and choose a forward diagonal move.
- **F3 Missed capture:** detect a non-jump move while a jump existed → restore the board and make a jump.
- **F4 Crowded king marker:** detect stacked pieces tipping → use a flat marker or crown piece instead.

## Verification

The final board shows one player with no pieces or no legal moves, and every capture followed the forced-jump rule.

## Variations

- Some house rules allow huffing a piece that misses a jump.
- International draughts uses a 10 by 10 board and flying kings.
- Teaching games can ignore forced jumps for the first few turns, then add the rule.

## Safety & privacy

Keep small pieces away from toddlers, and settle house rules before play starts.
⚠️ *Irreversible:* Removing a captured piece changes later moves, so pause before lifting pieces during multi-jumps.
