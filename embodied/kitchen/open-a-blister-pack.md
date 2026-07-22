---
name: open-a-blister-pack
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
objects: [blister-pack, foil, pill, plastic-dome, tray]
affordances: [grasp, peel, press, bend, catch, inspect]
workspace: kitchen counter
safety: {hot_surfaces: false, sharp_objects: false, fragile: [pill], human_proximity: slow}
---

## Goal

One pill or item is removed from the blister pack intact, caught on a clean surface or in a hand, and the remaining blisters stay sealed.

## Preconditions

- Correct blister cell is identified from the label or dosing plan.
- Hands are dry and a clean catching surface is ready.
- Children and pets are not close enough to grab a dropped pill.

## Steps

1. **Select one cell.** Hold the pack flat and isolate the blister containing the intended pill. → *Expect:* the chosen dome is centered and adjacent doses remain untouched.
2. **Inspect the backing.** Look for a peel tab, perforation, paper layer, or plain foil backing. → *Expect:* the opening method is visible.
3. **Prepare to catch.** Cup one hand or place the pack over a clean tray, palm, or small dish. → *Expect:* there is a target directly below the pill path.
4. **Peel from the corner if present.** [BRANCH: peel tab present → lift the corner and pull foil back | no tab → go to push-through] use fingernail pressure only on the foil corner. → *Expect:* foil separates without bending the pill.
5. **Push through if needed.** Support the foil side with one hand and press the center of the plastic dome with the thumb pad, using steady pressure rather than a jab. → *Expect:* foil splits and the pill drops onto the catch surface.
6. **Avoid crushing force.** If the pill resists, bend the pack slightly along the perforation or peel more foil before pressing again. → *Expect:* pill remains whole with no powder dust.
7. **Collect the pill.** Pinch the pill gently at its edges or slide it from the tray into the intended container or hand. → *Expect:* pill is controlled and does not roll.
8. **Inspect the pack.** Confirm only the chosen cell is opened and no loose foil fragments cling to the pill. → *Expect:* remaining cells are sealed and the removed item is clean.

## Decision points

- Pill is softgel or fragile → prefer peeling foil instead of pushing hard through backing.
- Blister is child-resistant laminate → peel the paper layer first if instructions show a two-stage opening.
- Pill drops to floor → do not use it unless the medication instructions and cleanliness permit recovery.

## Failure modes & recovery

- **F1 Pill cracks:** powder, split coating, or broken softgel appears → set it aside and follow label or pharmacist guidance before use.
- **F2 Foil will not peel:** corner delaminates without opening → switch to push-through with the pack supported close to the target.
- **F3 Pill launches away:** sudden foil rupture sends it sideways → search immediately, keep children and pets away, and use a deeper tray next time.
- **F4 Wrong cell opened:** label or day marker does not match → leave the pill contained safely and verify dosage before taking anything.

## Verification

Exactly one intended pill is out of the blister, intact and accounted for, with the remaining blister cells sealed.

## Variations

- Perforated strip: tear the single cell free before opening so the rest of the pack stays flat.
- Large tablet: press near the centerline of the dome, not on a corner, to prevent tilting and jamming.
- Non-medicine blister packaging: the same catch and peel logic applies, but contamination risk is lower.

## Safety & privacy

Low to medium risk depending on contents. Treat loose medicine as unsafe around children and pets, avoid crushing tablets unless directed, and keep labels private if medication information is sensitive.
