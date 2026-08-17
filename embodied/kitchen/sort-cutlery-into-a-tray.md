---
name: sort-cutlery-into-a-tray
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [cutlery, tray, forks, spoons, knives]
affordances: [grasp, classify, orient, place, align]
workspace: kitchen drawer or counter
safety: {hot_surfaces: false, sharp_objects: true, fragile: [], human_proximity: slow}
---

## Goal

Clean cutlery is grouped by type in the correct tray compartments with handles aligned.

## Preconditions

- Cutlery is clean and dry enough to store.
- The tray is empty or has visible compartments.
- Sharp knives, if present, are safe to handle by their handles.

## Steps

1. **Open or expose the tray.** Pull the drawer straight out or place the tray on the counter. → *Expect:* all compartments are visible and reachable.
2. **Identify compartments.** Inspect existing labels or contents to map forks, spoons, knives, and small utensils. → *Expect:* each cutlery type has a chosen compartment.
3. **Pick one utensil by the handle.** Grasp near the handle midpoint, keeping tips and blades pointed away. → *Expect:* the utensil is controlled without contacting the eating end.
4. **Classify the utensil.** Observe its shape: tines, bowl, blade, or specialty profile. → *Expect:* the matching compartment is selected.
5. **Place handle-aligned.** Lower the utensil into the compartment with handle ends facing the same direction as existing pieces. → *Expect:* it lies flat and does not bridge across dividers.
6. **Repeat one utensil at a time.** Continue until the unsorted pile is empty, slowing near sharp knives. → *Expect:* each compartment accumulates only one utensil class.
7. **Straighten each group.** Use light side pressure to align handles and tips within each compartment. → *Expect:* utensils are nested flat and drawer clearance is unobstructed.

## Decision points

- Unknown utensil type → place in a miscellaneous compartment rather than mixing with forks or knives.
- Tray compartment is full → start a second neat layer in the same orientation.
- Sharp knife encountered → grasp only the handle and keep the blade below hand height.

## Failure modes & recovery

- **F1 Wrong compartment:** detect by utensil shape not matching neighbors → lift it by the handle and move it to the correct compartment.
- **F2 Utensils jam drawer:** detect by raised handle or divider bridge → flatten and redistribute the tall pieces.
- **F3 Pointed end contacts hand:** detect by tip or blade facing the gripper → release to the tray, regrasp by handle, and continue slowly.

## Verification

Forks, spoons, knives, and specialty utensils are separated by compartment, lie flat, and the drawer or tray can close without contact.

## Variations

- Mixed-size cutlery: group small spoons or dessert forks in the shortest compartment.
- Knife block present: place sharp preparation knives in the block, not the tray.

## Safety & privacy

Sharp objects require handle-only grasps and slow motion near humans. No private information is involved.
