---
name: fold-a-towel
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [towel, table, shelf, hamper]
affordances: [grasp, shake, align, fold, stack, smooth]
workspace: household
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

A clean towel is folded into a neat rectangle that stacks evenly on a shelf or displays with the smooth edge facing out.

## Preconditions

- The towel is clean and dry.
- You have a flat surface, bed, table, or clear counter.
- Hands are clean and dry.
- The storage shelf or stack location has enough space.

## Steps

1. **Shake the towel open.** Hold two corners and give one controlled shake away from faces and objects. → *Expect:* the towel hangs flat enough to see its long and short edges.
2. **Lay it face down.** Put the towel on the surface with the display side down if one side looks better. → *Expect:* the better side will end up outside after folding.
3. **Smooth the fabric.** Run both hands from the center outward to remove twists and bunched corners. → *Expect:* edges lie straight and corners are visible.
4. **Fold one long side to the center.** Bring the left long edge inward about one-third of the towel width. → *Expect:* the fold line is straight from top to bottom.
5. **Fold the other long side over it.** Bring the right long edge across to make a long narrow rectangle. → *Expect:* the towel is in thirds with aligned edges.
6. **Fold the towel in half crosswise.** Bring the short ends together without stretching the fabric. → *Expect:* the towel becomes a shorter rectangle with corners matched.
7. **Make the display fold.** [BRANCH: shelf stack | visible display] fold in half again for compact storage, or fold one end under so the smooth folded edge faces outward. → *Expect:* the front edge is smooth and no raw corners face out.
8. **Stack without crushing.** Place the towel on the pile with folded edges aligned. → *Expect:* the stack stays level and does not lean.

## Decision points

- Towel is damp → hang it to dry before folding to prevent odor.
- Shelf is shallow → fold into thirds lengthwise, then thirds crosswise for a shorter rectangle.
- Decorative band should show → lay the towel face down and choose the final fold so the band faces front.
- Stack is leaning → refold the largest towels to the same footprint.

## Failure modes & recovery

- **F1 Corners do not meet:** detect diagonal edges after the first fold → unfold to the last straight fold and realign.
- **F2 Bulky middle:** detect a lump that will not stack → smooth before each fold and avoid trapping a corner.
- **F3 Damp smell:** detect musty odor while folding → stop, rewash or dry fully, and clean the shelf if needed.
- **F4 Uneven stack:** detect towels sliding or leaning → place largest towels on bottom and match fold sizes.

## Verification

The folded towel is dry, rectangular, smooth on the visible side, and stackable without leaning or unfolding.

## Variations

- `bath-sheet`: fold lengthwise in thirds, then crosswise in thirds to reduce bulk.
- `hand-towel`: use halves instead of thirds if the shelf is wide.
- `hotel-display`: keep the decorative band visible and face the clean folded edge outward.

## Safety & privacy

Low risk. Avoid folding damp towels into closed storage because mildew can spread. Keep stacks low enough that they do not fall when one towel is pulled out.
