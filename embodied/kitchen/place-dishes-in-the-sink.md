---
name: place-dishes-in-the-sink
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 3min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [dish, cup, bowl, sink]
affordances: [grasp, carry, lower, stack, release]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [dish, cup, bowl], human_proximity: continue}
---

## Goal

Dishes are placed in the sink without dropping, chipping, or creating an unstable stack.

## Preconditions

- The sink basin has enough open space for the dishes.
- Hands are dry enough to grip glass, ceramic, or wet plates.
- Any food scraps have been cleared according to the parent cleanup task if required.

## Steps

1. **Inspect the sink.** Look for knives, glass shards, or fragile items hidden under water. → *Expect:* the landing area is visible and safe.
2. **Choose one load.** Carry only the number of dishes that can be held without shifting, usually one to three items. → *Expect:* each item is supported from below or by a secure rim grip.
3. **Grip the dish.** Hold plates by opposite edges, bowls under the base, and cups around the body near the bottom. → *Expect:* the item does not tilt when lifted.
4. **Move to the basin.** Carry at waist height and keep the load close to the body. → *Expect:* dishes remain separated enough not to knock.
5. **Lower, do not drop.** Bring the dish to within one centimeter of the sink surface or stack before release. → *Expect:* contact is quiet and controlled.
6. **Stack by shape.** Put plates vertical or nested together, bowls nested, and cups upright or sideways where they cannot roll. → *Expect:* the stack sits stable without leaning.
7. **Protect fragile rims.** [BRANCH: glassware present | no glassware] Place glassware away from heavy plates; continue normal stacking otherwise. → *Expect:* fragile items are not bearing heavy load.
8. **Check clearance.** Remove hands slowly and nudge any unstable piece into a safer position. → *Expect:* no dish shifts after release.

## Decision points

- Sink contains standing water → place items slowly where the bottom can be felt and seen.
- Sharp object is visible → place dishes away from it or remove the sharp object first with appropriate care.
- Stack begins leaning → split into a second stack or stop adding dishes.

## Failure modes & recovery

- **F1 Dish slips:** grip starts to fail → lower immediately to the nearest surface rather than catching midair.
- **F2 Chip contact:** dish strikes another hard edge → stop, inspect for chips, and retire damaged food-contact pieces.
- **F3 Stack unstable:** items slide after release → unload the top item and rebuild by matching shapes.
- **F4 Hidden obstruction:** item cannot sit flat → lift it back out and clear the basin before retrying.

## Verification

All carried dishes rest inside the sink or intended basin area, the stack is stable, and no fragile item is chipped or supporting excessive weight.

## Variations

- `dishwasher-prep`: place dishes on the counter or rack instead of deep in the sink.
- `small-sink`: use fewer items per stack and keep cups separate.
- `soaking`: fill only after the stack is stable and sharp items are absent.

## Safety & privacy

Low risk, driven by fragile dishware and hidden sharp items. Lower each item into place, keep glassware visible, and avoid reaching blindly into cloudy water.
