---
name: use-a-hole-punch
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [hole-punch, paper-stack, paper-guide, desk, binder]
affordances: [align, insert, press, release, empty, inspect]
workspace: household
safety: {hot_surfaces: false, sharp_objects: true, fragile: [], human_proximity: continue}
---

## Goal

Punch clean holes in a paper stack at positions that fit the intended binder or fastener.

## Preconditions

- Hole punch matches the binder pattern.
- Paper stack is within the punch capacity.
- Paper guide is set for the page size if available.
- Desk surface is stable.

## Steps

1. **Square the papers.** Tap the stack edges on the desk to align pages. → *Expect:* all page corners line up.
2. **Set the paper guide.** Slide the guide to the page size mark or center mark. → *Expect:* the stack will enter to the same depth across pages.
3. **Insert the stack.** Push the edge into the slot until it contacts the back stop and side guide. → *Expect:* paper lies flat and hole positions are aligned.
4. **Press the handle fully.** Apply downward force until the punch completes its travel. → *Expect:* a firm cut is felt and paper dots drop into the catch tray.
5. **Release and remove.** Let the handle return before pulling the stack out. → *Expect:* the papers slide out without tearing.
6. **Inspect and empty if needed.** Check hole edges and empty the catch tray if it is near full. → *Expect:* holes are clean and the punch is not packed with paper dots.

## Decision points

- Stack is too thick → punch fewer pages at a time.
- Holes must align with an existing packet → use an already punched sheet as a guide.
- Catch tray is full → empty it before punching to avoid jams.

## Failure modes & recovery

- **F1 Partial holes:** detect crescent cuts or attached paper dots → repunch a smaller stack aligned to the same guide.
- **F2 Misplaced holes:** detect holes too close to text or edge → reprint or use reinforcement only if the binder can still hold.
- **F3 Jammed punch:** detect handle not returning → remove paper, empty the tray, and clear stuck dots.
- **F4 Torn edge:** detect ripped paper near holes → reduce stack size and press straight down.

## Verification

The papers have clean holes in matching positions, fit onto the binder rings or fastener, and are not torn at the punched edge.

## Variations

- `single-hole`: align the mark under the one punch opening and press once.
- `adjustable-three-hole`: lock all punch heads before inserting paper.

## Safety & privacy

Low risk. Punch blades are enclosed but sharp; keep fingers out of the slot and confirm private pages are in the intended stack before punching.
