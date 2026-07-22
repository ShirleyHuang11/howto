---
name: use-a-tape-measure
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
objects: [tape-measure, hook, blade, lock, edge, mark]
affordances: [hook, extend, align, read, lock, retract]
workspace: household
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: slow}
---

## Goal

A distance is measured from a hooked or aligned edge, read at the correct mark, and the tape is retracted under control.

## Preconditions

- Tape measure blade moves freely and the hook is not bent.
- Start and end points are visible.
- Nearby people are clear of the blade path.

## Steps

1. **Choose the start point.** Place the hook on an outside edge or butt the case against an inside surface. → *Expect:* zero reference is physically anchored.
2. **Extend the blade.** Pull the case away in line with the measurement path. → *Expect:* blade stays straight without twisting.
3. **Hook the edge.** Let the hook catch fully over the edge, then add light tension. → *Expect:* hook seats squarely and does not slide.
4. **Align to the end point.** Keep the blade parallel to the measured span. → *Expect:* markings cross the target point cleanly.
5. **Lock if needed.** Press the lock before moving your reading hand away. → *Expect:* blade length holds without retracting.
6. **Read the mark.** Look straight down at the end point and note the nearest printed mark. → *Expect:* measurement is read without parallax shift.
7. **Release the hook.** [BRANCH: hooked edge | free measurement] unhook gently or keep the blade supported. → *Expect:* blade remains under hand control.
8. **Retract controlled.** Press the lock open and feed the blade back slowly. → *Expect:* hook returns to the case without snapping.

## Decision points

- Hook cannot catch → press the hook against the start line and have a second hand hold it.
- Long span sags → support the blade midway or measure in shorter segments.
- Inside dimension → add the case length if printed, or use the case as the end stop.

## Failure modes & recovery

- **F1 Hook slips:** zero point moves during reading → rehook and repeat with lighter outward pull.
- **F2 Blade bends:** tape kinks or collapses → shorten the unsupported span and re-extend.
- **F3 Misread mark:** result seems off by a large fraction → reread from directly above and confirm units.
- **F4 Snapback:** blade retracts fast toward fingers → release grip, let it finish, then inspect for cuts or pinches.

## Verification

The measured value corresponds to a stable start reference and visible end mark, and the tape blade is fully retracted without injury.

## Variations

- Metric tape: read centimeter and millimeter marks instead of inches and fractions.
- Soft target: mark the endpoint with a pencil before removing the tape.

## Safety & privacy

Low risk. The main hazards are pinched fingers, blade-edge cuts, and snapback at the hook, so keep a hand on the blade during retraction.
