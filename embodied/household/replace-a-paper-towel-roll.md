---
name: replace-a-paper-towel-roll
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
objects: [paper-towel-roll, cardboard-tube, holder, spring-rod, sheet]
affordances: [grasp, compress, remove, insert, align, tear]
workspace: household
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

The empty tube is removed, a new roll is loaded in the intended feed direction, and sheets tear cleanly from the holder.

## Preconditions

- Replacement roll is nearby and wrapper is removed.
- Holder style is identified as spring rod, side arm, or vertical post.
- Counter or wall area around the holder is clear.

## Steps

1. **Remove the empty tube.** Pull the cardboard tube off the holder or rod. → *Expect:* holder is exposed and free of paper scraps.
2. **Release the rod.** For a spring holder, compress one end and lift it out of its socket. → *Expect:* rod comes free without bending.
3. **Check roll orientation.** Decide whether sheets should feed over the front or under from the back. → *Expect:* loose sheet points toward the normal pull direction.
4. **Load the roll.** Slide the rod through the tube or place the roll over the post. → *Expect:* roll rotates around its center.
5. **Reseat the rod.** Compress the spring end, place both ends into sockets, then release. → *Expect:* rod tips lock into both supports.
6. **Center the roll.** Shift the roll so it does not rub either side. → *Expect:* roll spins with light resistance.
7. **Start the sheet.** Pull the loose edge forward to the perforation. → *Expect:* one sheet presents beyond the roll.
8. **Perform a tear test.** Hold the roll or use the holder edge and pull down at the perforation. → *Expect:* one sheet detaches cleanly.

## Decision points

- Roll feeds backward for the household preference → remove and flip it.
- Spring rod is stuck → compress the smaller end first and avoid prying the brackets.
- Vertical post holder → skip rod steps and lift the roll straight off and on.

## Failure modes & recovery

- **F1 Rod not seated:** roll falls when pulled → reinsert both rod ends until each rests in its socket.
- **F2 Roll rubs:** sheets drag or tear raggedly → center the roll and remove wrapper remnants.
- **F3 Sheet unravels:** roll spins too freely → steady the roll with the off hand during tearing.
- **F4 Wrong orientation:** loose sheet hides behind roll → flip the roll and repeat the tear test.

## Verification

A new roll is secured on the holder, rotates freely, feeds in the chosen direction, and releases one sheet at a perforation.

## Variations

- Ratchet holder: press the side release before removing the core.
- Adhesive starter tab: peel the tab away before installing so the first sheet can feed.

## Safety & privacy

Low risk. Keep fingers out of spring sockets during reseating to avoid a small pinch.
