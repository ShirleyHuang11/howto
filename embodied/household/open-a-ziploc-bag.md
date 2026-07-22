---
name: open-a-ziploc-bag
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
objects: [ziploc-bag, seal-track, lip, contents]
affordances: [pinch, pull-apart, slide, inspect, hold-open]
workspace: household
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

The bag seal is separated along the track and the mouth is open enough to add or remove contents.

## Preconditions

- Bag is upright if it contains loose or liquid contents.
- Both top lips of the seal are reachable.
- Hands are dry enough to grip the plastic.

## Steps

1. **Support the bag.** Hold the body below the seal so contents stay low. → *Expect:* bag remains upright and stable.
2. **Find the seam lips.** Feel for the two raised tracks at the top opening. → *Expect:* each hand contacts a different side of the seam.
3. **Pinch both sides.** Grip the front lip with one hand and the back lip with the other. → *Expect:* the two plastic layers are controlled separately.
4. **Start separation.** Pull the lips apart near one corner with steady outward force. → *Expect:* a small gap opens in the seal.
5. **Open along the track.** Move the pull across the seam or slide fingers as the track separates. → *Expect:* the gap travels across the full width.
6. **Check for missed sections.** Look and feel for any still-linked zipper ridges. → *Expect:* both lips are loose from corner to corner.
7. **Hold the mouth open.** Roll or spread the top edges away from each other. → *Expect:* contents can pass without rubbing the seal.
8. **Verify open state.** [BRANCH: add item | remove item] pass fingers or the target object through the mouth. → *Expect:* nothing catches on a closed segment.

## Decision points

- Seal is greasy or wet → wipe the lips dry before pulling.
- Contents may spill → set the bag in a bowl or keep the bottom supported.
- Child-resistant double seal → separate one track at a time.

## Failure modes & recovery

- **F1 Only one lip held:** both fingers pinch the same layer → reset grip so layers pull in opposite directions.
- **F2 Track tears:** plastic stretches or rips below the seal → stop pulling outward and open from the other corner.
- **F3 Partial opening:** center remains closed → pinch next to the closed area and peel along it.
- **F4 Spill risk:** contents climb toward the mouth → lower the bag body and reduce tilt before continuing.

## Verification

The seal track is separated across the full mouth and an object can enter or exit without pushing through a closed section.

## Variations

- Slider bag: hold the bag body and move the slider fully to the open end.
- Frozen bag: warm the seal briefly in hand before pulling to reduce stiffness.

## Safety & privacy

Low risk. Keep powders or liquids upright and avoid tearing the bag if it stores food or personal items.
