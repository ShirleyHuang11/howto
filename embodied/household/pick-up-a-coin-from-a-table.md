---
name: pick-up-a-coin-from-a-table
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [coin, table, container]
affordances: [locate, pinch, slide, lift, place]
workspace: table or desk
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

A coin is lifted from a table and placed into a target hand, dish, or container.

## Preconditions

- Coin is visible and reachable on a stable table.
- Target placement location is known.
- Table surface is dry and clear near the coin.

## Steps

1. **Locate the coin edge.** View the coin from above and identify an accessible rim. → *Expect:* the coin boundary is visible against the table.
2. **Place fingertips near the rim.** Bring thumb and index finger to opposite sides without pushing the coin away. → *Expect:* both fingertips contact the coin edge or table beside it.
3. **Pinch lightly.** Apply inward pressure on the coin rim while keeping fingers vertical. → *Expect:* the coin resists sliding and is captured between fingertips.
4. **Lift straight up.** Raise the coin 2-5 cm above the table with steady grip. → *Expect:* the coin clears the table and remains between fingertips.
5. **Move over the target.** Translate the coin slowly above the hand, dish, or container opening. → *Expect:* the coin is centered over the intended drop area.
6. **Release low.** Lower close to the target surface and relax the pinch. → *Expect:* the coin lands in the target with minimal bounce.

## Decision points

- Coin is too flat to pinch → slide it to the table edge or onto a thin card, then lift.
- Coin is sticky or wet → wipe the surface or use a broader pinch.
- Multiple coins overlap → lift the top coin first or separate them by sliding.

## Failure modes & recovery

- **F1 Coin slides away:** detect by coin moving before pinch capture → reduce horizontal force and approach from opposite sides.
- **F2 Coin drops early:** detect by coin leaving fingertips before target → stop, locate it, and repeat with a firmer rim pinch.
- **F3 Target miss:** detect by coin landing outside the container → pick it up again and release closer to the target center.

## Verification

The coin is no longer on the table and is resting in the specified target location.

## Variations

- Smooth tabletop: press down lightly before pinching to prevent sliding.
- Coin near edge: slide partly over the edge and pinch the overhanging portion.

## Safety & privacy

Coins can be dirty and may represent money. Avoid dropping them where they can roll under furniture or become a choking hazard.
