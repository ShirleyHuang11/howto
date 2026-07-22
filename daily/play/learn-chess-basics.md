---
name: learn-chess-basics
domain: daily
subdomain: play
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Set up a chessboard, make legal beginner moves, and understand check, checkmate, castling, and a first opening idea.

## Preconditions

- A chessboard with 32 pieces.
- Two players or one learner practicing both sides.
- The board coordinates or at least the light and dark squares are visible.
- Enough table space that captured pieces do not crowd the board.

## Steps

1. **Orient the board.** Put a light square in each player's right-hand corner. → *Expect:* "white on right" is true for both players.
2. **Place the pieces.** Put rooks in corners, then knights, bishops, queen on her color, king on the remaining center square, and pawns in front. → *Expect:* both armies mirror each other.
3. **Move pawns.** Move a pawn one square forward, or two from its starting square if both squares are clear. → *Expect:* pawns move straight but capture one square diagonally.
4. **Move the pieces.** Practice rook straight lines, bishop diagonals, queen both, knight L-shapes, and king one square. → *Expect:* each piece follows its own movement pattern.
5. **Respect occupied squares.** Do not move through pieces except with knights, and capture only enemy pieces. → *Expect:* blocked lines stop sliding pieces.
6. **Identify check.** Attack the enemy king and say "check" in practice games. → *Expect:* the checked side must answer the threat.
7. **Escape check.** [BRANCH: move king | block | capture attacker] choose one legal escape. → *Expect:* the king is no longer attacked.
8. **Learn castling.** Move the king two squares toward an unmoved rook, then place that rook beside the king, only if the path and king are safe. → *Expect:* king safety improves in one special move.
9. **Try a first opening idea.** Move a center pawn, develop a knight or bishop, and aim to castle early. → *Expect:* pieces leave the back rank and the king gets safer.

## Decision points

- White moves first → alternate turns after that.
- A king is attacked and has no legal escape → that is checkmate, not a captured king.
- The king or rook has moved → castling on that side is no longer legal.
- A beginner is lost → play from a small position with kings, pawns, and one rook.

## Failure modes & recovery

- **F1 Board rotated wrong:** detect a dark square at the right corner → rotate the board and reset.
- **F2 Queen misplaced:** detect queens not on matching colors → swap queen and king before play starts.
- **F3 Illegal knight move:** detect a move that is not two plus one → return the knight and choose a legal square.
- **F4 Missed check:** detect a king left attacked after a move → undo that move and escape check.

## Verification

The learner can set up the board correctly, describe each piece move, and identify a simple checkmate position.

## Variations

- Use coordinate labels to learn notation while moving pieces.
- Start with pawn races to teach promotion before full games.
- Use a clock only after both players can make legal moves comfortably.

## Safety & privacy

Small pieces can be choking hazards, so keep them away from very young children.
⚠️ *Irreversible:* Tournament touch-move rules can make a touched piece binding, so agree whether casual practice ignores that rule.
