---
name: clean-up-a-liquid-spill
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [paper-towels, dish-towel, sponge, mop, bucket, dish-soap, trash-bin, wet-floor-sign]
affordances: [grasp, blot, wipe, wring, pour, place, spray]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: pause}
---

## Goal

A liquid spill on counter or floor is contained, fully absorbed, degreased if needed, and the surface is verified dry and safe to walk on.

## Preconditions

- Absorbents in reach: paper towels or rags for small spills, a mop and bucket for anything over roughly a liter.
- Dish soap available for oily or sticky spills.
- The spill is ordinary kitchen liquid (water, milk, juice, oil, sauce, coffee). Broken glass in the spill or hazardous chemicals change the procedure: see decision points.

## Steps

1. **Stop the source first.** Right the tipped container, close the tap, kill the burner under a boil-over. Cleaning while the source still flows is mopping a river. → *Expect:* nothing more is being added to the puddle.
2. **Guard the zone.** Warn anyone nearby ("spill here, don't walk through"), and put a chair, the mop bucket, or a wet-floor sign at the puddle's edge if you must step away even briefly. → *Expect:* no foot traffic path crosses the wet area unannounced.
3. **Dam the spread.** Lay towels around the puddle's leading edge, especially the side toward cabinets, appliance gaps, and rugs. Liquid that gets under an appliance or cabinet toe-kick is the part you can never reach. → *Expect:* puddle edge stopped; nothing advancing toward gaps.
4. **Absorb from the edges inward.** Press towels flat onto the liquid and let them wick; lift straight up when saturated. Blot, do not wipe outward: wiping spreads the spill thinner and wider. [BRANCH: small spill → paper towels to the bin | large spill → wring rags into the sink or a bucket, repeat] → *Expect:* puddle shrinking toward its center; used towels binned or wrung, not left sitting in the liquid.
5. **Degrease if the spill was oily, milky, or sugary.** Water alone leaves an invisible film that stays slippery (oil) or turns sticky and sour (milk, juice). Wipe the whole affected area with a sponge or cloth and warm water plus a drop of dish soap, then rinse-wipe with a clean damp cloth. → *Expect:* no rainbow sheen, no squeak-drag stickiness under a clean fingertip.
6. **Dry the surface completely.** Go over the area with a dry towel until a final pass picks up no moisture. → *Expect:* dry towel comes away dry.
7. **Verify with a hand and a shoe.** Press a flat palm on the counter area, or test the floor patch with a shoe-sole twist. ⚠️ *Irreversible:* slip-and-fall injuries are the whole reason this step exists; a floor that merely looks dry is the trap, thin water films are near invisible on smooth flooring. → *Expect:* no moisture on the palm; sole grips without any glide.
8. **Reset.** Bin the disposables, laundry-bin the rags (a milk rag left in the sink smells by evening), rinse the mop, remove the warning marker. → *Expect:* zone open again; no sour-smelling cloths left anywhere.

## Decision points

- Glass broke in or near the spill → shards first, liquid second: pick large pieces by hand into a bag, press a damp paper towel over the area for fragments, and only then blot; never wipe blind with a bare-handed cloth.
- Liquid reached the base of a powered appliance (kettle base, toaster, outlet strip) → unplug at the wall (dry hands) before any wet cleaning near it.
- Spill is on a rug or into a cabinet interior → blot hard now, then lift the rug or empty the shelf to dry both sides; trapped moisture molds within days.
- Chemical spill (drain cleaner, bleach mix) → not this recipe: ventilate, glove up, follow the product label.

## Failure modes & recovery

- **F1 Still slippery after cleanup:** sheen or glide underfoot on the "clean" patch → the degrease step was skipped or thin; repeat step 5 with more soap, then rinse and dry again.
- **F2 Sour smell days later:** milk or juice found a gap → pull the appliance or empty the toe-kick area, wash the hidden run with soapy water, dry fully.
- **F3 Puddle got ahead of you under an appliance:** visible liquid in the gap → slide towels flat underneath as far as they go with a spatula or mop handle; repeat with dry towels until they return dry.
- **F4 Someone walks toward the wet zone mid-cleanup:** stop everything and speak up first; a body-block beats a mid-fall grab.

## Verification

Palm test and sole-twist test both pass on the affected area, no sheen or stickiness remains, no liquid sits in any adjacent gap or under any appliance edge, used absorbents are binned or in the laundry, and the warning marker is removed only after the tests pass.

## Variations

- Hot spill (soup, boiling water): let it cool for a minute or push towels onto it with a utensil first; wringing a scalding rag burns hands.
- Sticky-sweet spills (honey, syrup): warm soapy water and patience; dry-blotting first just spreads it.

## Safety & privacy

Medium risk, almost all of it slip-and-fall, concentrated after the spill "looks" gone. The order matters: contain before absorbing, degrease before drying, verify before reopening the floor. Electricity plus water is the other hazard: dry hands, unplug at the wall.
