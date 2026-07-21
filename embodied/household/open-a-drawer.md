---
name: open-a-drawer
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [drawer, drawer-handle, cabinet]
affordances: [grasp, pull, stop, hold, inspect]
workspace: household-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

A drawer is opened in a straight, controlled motion to expose its contents without pulling it free or spilling items.

## Preconditions

- The drawer face and handle are reachable.
- The actor has clearance to step or roll backward as the drawer opens.
- The drawer is not known to be locked.
- Hands or grippers are dry enough to hold the handle.

## Steps

1. **Face the drawer.** Align the body or chassis with the drawer's travel direction. → *Expect:* pull direction is straight out from the cabinet face.
2. **Check surrounding clearance.** Confirm knees, feet, wheels, and nearby items are outside the drawer path. → *Expect:* drawer can open without collision.
3. **Grasp the handle.** Wrap fingers around the handle or place a firm pinch on the pull recess. → *Expect:* grip holds when lightly tensioned.
4. **Start the pull straight.** Pull outward along the drawer rails without lifting or twisting. → *Expect:* drawer begins sliding evenly.
5. **Control the speed.** Continue pulling slowly, moving the body back if needed to keep elbow and wrist aligned. → *Expect:* contents remain seated and do not surge forward.
6. **Stop before full extension.** Ease force when resistance increases or the drawer reaches useful access. → *Expect:* drawer is open and still supported by its rails.
7. **Let contents settle.** Hold the handle still for one beat. → *Expect:* loose items stop shifting.
8. **Release or maintain hold.** [BRANCH: drawer self-stable | drawer rolls] release if stable; keep a light hold if it drifts. → *Expect:* drawer stays at the selected opening distance.

## Decision points

- Drawer resists immediately → check for a latch, child lock, jammed item, or lock.
- Drawer is heavy → use two hands or open only partway.
- Drawer contains rolling items → open slowly and stop at partial extension.
- Drawer has no handle → pull from a recessed lower or upper edge without pinching fingers.
- Drawer must remain open during work → verify it does not self-close before placing hands inside.

## Failure modes & recovery

- **F1 Drawer jams:** detect stop before useful opening → push back slightly, lift or lower the front a few millimeters, and retry gently.
- **F2 Drawer overextends:** detect rail stop impact or front drop → stop pulling, support from below, and push inward until rails re-seat.
- **F3 Contents spill forward:** detect items sliding toward the front → pause, push drawer partly closed, and reopen slower.
- **F4 Handle grip slips:** detect loss of purchase → release force, dry the handle if needed, and re-grasp with a fuller wrap.
- **F5 Collision with body:** detect drawer contacting knees, feet, or base → push drawer in slightly and reposition.

## Verification

The drawer is open to the intended distance, supported by its rails, with contents visible and not spilling or shifting.

## Variations

- `soft-close`: expect resistance near the first centimeters and pull steadily until the mechanism releases.
- `push-to-open`: press the drawer face inward first, then pull from the revealed edge.
- `file-drawer`: open only one drawer at a time to prevent tipping.
- `under-bed-drawer`: kneel or squat beside the travel path rather than directly in front.

## Safety & privacy

Low risk for normal drawers. Keep fingers away from side rails and do not pull multiple tall cabinet drawers open at once. Drawer contents may be private, so expose only what the task requires.
