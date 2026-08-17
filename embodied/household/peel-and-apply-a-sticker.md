---
name: peel-and-apply-a-sticker
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 3min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [sticker, backing-paper, target-surface, cloth, card]
affordances: [grasp, peel, align, press, smooth, inspect]
workspace: household
safety: {hot_surfaces: false, sharp_objects: false, fragile: [decor, electronics], human_proximity: continue}
---

## Goal

Separate a sticker from its backing and attach it smoothly to a clean target surface in the intended position.

## Preconditions

- Target surface is compatible with adhesive.
- Surface is clean, dry, and free of loose dust.
- Sticker is not torn and still attached to backing.
- Placement position is known before peeling.

## Steps

1. **Clean the target spot.** Wipe dust or moisture away and let the area dry. → *Expect:* the surface looks dry and debris-free.
2. **Plan alignment.** Hold the sticker over the target without peeling and note edges or marks for placement. → *Expect:* the final position is visually clear.
3. **Peel one edge.** Bend the backing away from a sticker corner and lift only 1 to 2 cm of adhesive. → *Expect:* the sticker edge separates without curling into itself.
4. **Anchor the exposed edge.** Place the exposed adhesive on the target at the planned line and press lightly. → *Expect:* the sticker is attached at one edge and still adjustable by the backing.
5. **Remove backing while smoothing.** Pull the backing away slowly while pressing from the anchored edge outward with a finger or card. → *Expect:* the sticker lays down without trapped bubbles or wrinkles.
6. **Seal the edges.** Press along the perimeter and across the center with even pressure. → *Expect:* all edges adhere flat and no corner lifts.

## Decision points

- Sticker is removable vinyl → lift and realign early if placement is wrong.
- Sticker is paper or security adhesive → treat placement as final once pressed.
- Surface is curved → apply from the center outward in smaller sections.

## Failure modes & recovery

- **F1 Bubble trapped:** detect raised pocket under sticker → push it toward the nearest edge with a card.
- **F2 Sticker folds onto itself:** detect adhesive-to-adhesive contact → peel apart slowly from the fold; discard if torn.
- **F3 Poor adhesion:** detect edges lifting after pressing → clean and dry surface again, then replace with a new sticker if adhesive is contaminated.
- **F4 Misalignment:** detect edge off the planned line before full contact → lift the unattached portion and re-anchor.

## Verification

The sticker is attached at the intended location with flat edges, no major bubbles, and no visible dust or moisture under the adhesive.

## Variations

- `label`: write on the label before peeling when the surface is hard to write on.
- `screen-protector-style`: use a dust-removal step and hinge tape for precise alignment.

## Safety & privacy

Low risk. Confirm the surface owner permits adhesive marks, and avoid covering labels, vents, sensors, or private identifying information unintentionally.
