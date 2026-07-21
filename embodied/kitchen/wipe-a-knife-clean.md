---
name: wipe-a-knife-clean
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 1min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [knife, cloth, towel, sink]
affordances: [grasp, wipe, pinch, rotate, inspect, place]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: true, fragile: [], human_proximity: slow}
---

## Goal

Residue is removed from both sides of a knife blade without contacting the cutting edge.

## Preconditions

- The knife handle is dry enough to grip securely.
- A clean cloth or towel is available and large enough to cover the blade spine.
- The workspace is clear, with no person reaching near the blade.

## Steps

1. **Set blade orientation.** Hold the knife by the handle with the cutting edge facing away from the wiping hand. → *Expect:* the edge is visible and points away from fingers and body.
2. **Fold the cloth.** Fold the cloth into a thick pad wider than the blade height. → *Expect:* fingers can pinch cloth without protruding past its edge.
3. **Place cloth on spine.** Lay the cloth over the dull spine side first, not over the cutting edge. → *Expect:* cloth covers the blade face while fingers remain above the spine.
4. **Wipe first side.** Pinch lightly through the cloth near the spine and pull from handle toward tip. → *Expect:* residue transfers to the cloth in a straight pass.
5. **Rotate safely.** Turn the knife so the opposite face is accessible while the edge still points away. → *Expect:* the cutting edge never faces the wiping hand.
6. **Wipe second side.** Repeat handle-to-tip strokes with cloth pressure directed against the blade face, not across the edge. → *Expect:* visible residue leaves the second side.
7. **Inspect without touch.** Hold the knife still and look along both faces for remaining food. → *Expect:* blade faces appear clean and dry enough for the next step.
8. **Place the knife down.** Set it flat on the board or sink edge with blade fully supported. ⚠️ *Irreversible:* edge contact can cut skin or cloth, so never draw fingers along the edge. → *Expect:* knife is stationary with handle reachable.

## Decision points

- Sticky residue remains → rinse the blade under controlled water, then repeat the spine-side cloth wipe.
- Cloth becomes thin or bunched → refold before continuing.
- Person reaches nearby → pause with the knife still until the workspace is clear.

## Failure modes & recovery

- **F1 Cloth snags:** fabric catches on the edge → stop pulling, move cloth away from the spine side, and refold.
- **F2 Grip slips:** handle rotates in the hand → set the knife down, dry the handle, and regrip.
- **F3 Residue near tip:** food remains at the point → wipe handle-to-tip with smaller pressure, keeping fingers behind cloth.
- **F4 Finger near edge:** wiping hand crosses edge line → stop and reset blade orientation before another pass.

## Verification

Both blade faces are visibly clean, the cutting edge was not touched, and the knife is resting flat with the handle accessible.

## Variations

- `serrated-knife`: wipe along the blade face and avoid dragging cloth into the teeth.
- `chef-knife`: use a larger folded towel so the broad blade is fully covered.
- `between-cuts`: quick wipe is acceptable only if the next food-contact step stays sanitary.

## Safety & privacy

Medium risk from the sharp blade. Keep the edge pointed away, cloth over the spine side, and pause if another person or hand enters the knife workspace.
