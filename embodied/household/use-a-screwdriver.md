---
name: use-a-screwdriver
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 3min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
objects: [screwdriver, screw, bit, screw-head, workpiece]
affordances: [grasp, match, seat, push, turn, stop]
workspace: household
safety: {hot_surfaces: false, sharp_objects: true, fragile: [screw-head], human_proximity: slow}
---

## Goal

The screw is tightened or loosened with the correct driver, without stripping the head or damaging the workpiece.

## Preconditions

- Screw head is accessible and visible.
- Driver or bit set includes the correct head type and size.
- Workpiece is stable enough to resist turning force.

## Steps

1. **Identify the head.** Inspect for Phillips, flat, Torx, hex, or square drive. → *Expect:* matching bit type is selected.
2. **Match the size.** Test the bit in the head without turning. → *Expect:* bit fills the recess with little wobble.
3. **Seat the bit.** Place the tip straight into the screw head along the screw axis. → *Expect:* driver shaft aligns with the screw.
4. **Brace the workpiece.** Hold the object or surface so it cannot spin or shift. → *Expect:* screw remains the only moving part.
5. **Push while turning.** Apply inward pressure and rotate clockwise to tighten, counterclockwise to loosen. → *Expect:* screw turns without the bit climbing out.
6. **Use short resets.** Lift and regrip the handle when wrist range ends. → *Expect:* pressure stays axial and the bit stays seated.
7. **Stop at snug.** [BRANCH: tightening | loosening] stop when resistance rises sharply or the screw releases. → *Expect:* screw is secure or free without stripped edges.
8. **Inspect the head.** Remove the driver straight out and check the recess. → *Expect:* head shape remains crisp.

## Decision points

- Bit cams out repeatedly → choose a larger or correct bit before continuing.
- Screw is frozen → add penetrating oil or use a manual impact driver rather than more force.
- Workpiece is delicate → use hand torque, not a drill driver.

## Failure modes & recovery

- **F1 Stripping starts:** recess edges turn shiny or rounded → stop, improve bit fit, and press harder while turning slower.
- **F2 Wrong direction:** screw moves opposite the goal → reverse rotation using righty-tighty, lefty-loosey.
- **F3 Driver slips:** tip jumps out of the head → reseat squarely and reduce sideways force.
- **F4 Over-tightened screw:** material compresses or cracks → back off slightly and inspect for damage.

## Verification

The screw reaches the intended tight or loose state, the head remains usable, and the workpiece surface is not gouged.

## Variations

- Ratcheting driver: set the ratchet direction before applying force.
- Powered driver: start slow, use a clutch, and finish by hand when precision matters.

## Safety & privacy

Low risk, but screwdriver tips and screws can puncture skin. Keep the off hand behind the tip path and slow down near fragile finishes.
