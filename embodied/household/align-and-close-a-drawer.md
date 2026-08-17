---
name: align-and-close-a-drawer
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [drawer, handle, runners, cabinet]
affordances: [grasp, align, push, observe, release]
workspace: cabinet or desk
safety: {hot_surfaces: false, sharp_objects: false, fragile: [drawer-face], human_proximity: slow}
---

## Goal

The drawer is aligned on its runners and closed flush with the cabinet or desk front.

## Preconditions

- Drawer contents do not protrude above the drawer sides.
- The drawer runners or slides are visible enough to assess alignment.
- No fingers or objects are in the closing path.

## Steps

1. **Inspect the gap.** Look along both drawer sides and the top edge. → *Expect:* any skew or obstruction is visible.
2. **Grip the handle centered.** Place hand at the middle of the handle or front face to avoid twisting. → *Expect:* pull or push force will be centered.
3. **Square the drawer.** If one side is ahead, pull back slightly and guide the front until both side gaps match. → *Expect:* the drawer front is parallel to the cabinet face.
4. **Push straight inward.** Apply steady centered pressure along the drawer travel direction. → *Expect:* the drawer slides inward without scraping.
5. **Slow near closure.** Reduce force in the final few centimeters to avoid slamming. → *Expect:* the drawer face approaches the cabinet evenly.
6. **Seat flush.** Push gently until the latch or stop engages. → *Expect:* the drawer front is flush or evenly recessed with adjacent surfaces.
7. **Release and observe.** Remove hand and watch for rebound. → *Expect:* the drawer stays closed and aligned.

## Decision points

- Contents block closure → reopen and lower or move the obstruction.
- Drawer is off its runner → lift slightly and reseat before pushing.
- Soft-close mechanism engages → let it pull the drawer in without added force.

## Failure modes & recovery

- **F1 Drawer binds:** detect by scraping or stopped travel → pull back, realign side gaps, and retry with centered pressure.
- **F2 Object blocks closure:** detect by spring-back or visible protrusion → reopen and move the blocking item below the drawer rim.
- **F3 Fingers near pinch point:** detect by hand or person near side gap → pause and clear the area before closing.

## Verification

The drawer front is flush and parallel to the cabinet, stays closed after release, and no contents protrude.

## Variations

- File drawer: ensure hanging folders sit below the top rail before closing.
- Soft-close drawer: push only until the mechanism catches, then release.

## Safety & privacy

Pinch points exist along the drawer sides. Drawer contents may be private; avoid exposing or rearranging unrelated items.
