---
name: fold-a-tshirt
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [t-shirt, folding-surface]
affordances: [grasp-fabric, smooth, fold, flip, place]
workspace: home-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

A clean, dry t-shirt is folded into a flat, compact rectangle that stacks stably in a drawer or on a shelf.

## Preconditions

- The t-shirt is clean and fully dry (folding damp fabric breeds mildew and wrinkles).
- A flat folding surface (table/bed) larger than the spread shirt is clear.

## Steps

1. **Spread the shirt face-down on the surface.** Chest down, back up, collar away from you. Grasp the hem and give one straightening shake before laying down. → *Expect:* shirt lies flat, sleeves out to the sides, no major folds trapped under it.
2. **Smooth the fabric.** Two flat-hand (or flat-gripper) sweeps outward from the spine to the edges. → *Expect:* no wrinkles or bunched fabric; seams lie straight.
3. **Fold the first side in.** Grasp the shirt's left shoulder and left hem corner; fold the left third over the back, sleeve included, so the fold line runs shoulder-to-hem. → *Expect:* left edge now runs parallel to the shirt's centerline, about a third of the way across.
4. **Fold the left sleeve back.** Fold the protruding sleeve back toward the left edge so it lies within the folded panel. → *Expect:* no sleeve fabric sticks out past the folded edge.
5. **Repeat steps 3–4 on the right side.** → *Expect:* a long rectangle roughly one-third the original width; both sleeves contained; edges parallel.
6. **Fold the rectangle in half (or thirds) hem-to-collar.** Grasp the hem edge, fold up to just below the collar; for deep shelves fold once (half), for drawers fold twice (thirds). → *Expect:* a compact rectangle, collar visible on top face when flipped.
7. **Flip it face-up and place it on the stack.** → *Expect:* the shirt front/graphic faces up, rectangle sits flat without springing open.

## Decision points

- Vertical/file folding (drawer stands shirts on edge, KonMari-style) → in step 6 fold to thirds and stand the packet on its folded edge; it should stand unsupported — if it flops, one more fold.
- Long-sleeve shirt → in step 4, fold the sleeve diagonally down along the body so the cuff lands near the hem, then continue normally.
- Shirt is wrinkled beyond smoothing → folding sets wrinkles; shake it out and re-dry briefly or iron before folding.

## Failure modes & recovery

- **F1 Result is a parallelogram, not a rectangle:** the side folds weren't parallel to the centerline — unfold to step 2 and re-crease with the fold line vertical.
- **F2 Sleeve pokes out of the packet:** reopen the offending side only, retuck (step 4), refold.
- **F3 Fabric drags/static clings during grasp:** grasp with more fabric in the grip (pinches tear knit fabric); release and re-grasp rather than pulling.
- **F4 Stack topples when placed:** stacks over ~8 shirts buckle — start a second stack, or switch to vertical filing.

## Verification

The folded shirt is a flat rectangle with no protruding sleeves, front face up, roughly consistent with the others in the stack, and the stack (or file row) remains stable after placement.

## Variations

- Two-second "pinch fold" (shoulder + mid-chest pinch, flip through): faster for humans, needs practiced bimanual coordination — the panel method above is the robot-friendly canonical path.
- Delicate/printed shirts: fold with the print inward-facing at step 6 to protect the graphic in deep stacks.

## Safety & privacy

Minimal risk. Fabric manipulation demands low grip force and slack management — deformable-object handling is the skill being exercised; nothing here can hurt anyone except a toppling stack.
