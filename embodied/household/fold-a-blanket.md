---
name: fold-a-blanket
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 4min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [blanket, bed, table, shelf]
affordances: [grasp, lift, align, smooth, fold, stack]
workspace: household
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

A blanket is folded into a flat, compact shape with aligned edges and stacked where it will stay stable.

## Preconditions

- The blanket is dry and free of items hidden inside it.
- A clean bed, table, couch, or floor area is available for spreading.
- The storage shelf, chair, or basket has enough space for the folded size.
- Hands can reach two corners at a time, or a second person can help with a large blanket.

## Steps

1. **Shake out the blanket.** Lift one edge and give a small shake to release twists and hidden objects. → *Expect:* the blanket hangs freely with no hard objects inside.
2. **Spread it flat.** Lay the blanket on the work surface with the long edges visible. → *Expect:* the fabric is open enough to identify all corners.
3. **Match the first corners.** Bring two adjacent corners together along the long edge. → *Expect:* one long edge is doubled and roughly aligned.
4. **Halve the blanket.** Bring the opposite corners to the matched corners, making a rectangle. → *Expect:* all four corners are grouped and edges are close.
5. **Smooth the surface.** Sweep hands from the folded edge outward to push out air and wrinkles. → *Expect:* the rectangle lies flatter and does not bulge.
6. **Fold into thirds.** Fold one short side toward the center, then fold the other side over it. → *Expect:* the width is compact and the edges form a neat stack.
7. **Fold once more if needed.** [BRANCH: shelf is narrow | blanket is already shelf-sized] fold in half for narrow storage or leave it as is. → *Expect:* the folded blanket matches the storage space.
8. **Place it stable.** Set the folded blanket flat with the heaviest fold at the bottom. → *Expect:* the stack stays level and does not slide.

## Decision points

- Blanket is larger than arm span -> fold on a bed or ask another person to hold two corners.
- Blanket is thick or puffy -> use halves instead of tight thirds to avoid a rounded pile.
- Storage is a basket -> fold to basket width, then roll loosely if stacking is unstable.
- Blanket is damp -> dry it before folding to avoid odor or mildew.

## Failure modes & recovery

- **F1 Corners mismatch:** edges spiral or one corner hangs low, reopen to the last fold and realign corners.
- **F2 Bulging center:** air is trapped between layers, smooth from the fold toward open edges.
- **F3 Unstable stack:** folded blanket tips or slides, rotate it so the broadest face is down.
- **F4 Hidden item:** a remote or toy falls out, remove it and repeat the first smoothing pass.

## Verification

The blanket is dry, folded flat with corners aligned, and rests in storage without sliding or tipping.

## Variations

- `weighted-blanket`: fold on a bed and avoid lifting the whole blanket at once.
- `throw-blanket`: two half folds may be enough for couch storage.
- `linen-closet`: fold to the shelf depth so the clean edge faces outward.

## Safety & privacy

Low risk. Keep feet clear of trailing fabric, avoid twisting while lifting heavy blankets, and check for personal items before stacking.
