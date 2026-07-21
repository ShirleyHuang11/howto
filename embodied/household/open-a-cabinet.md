---
name: open-a-cabinet
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
objects: [cabinet-door, cabinet-handle, cabinet-frame]
affordances: [grasp, pull, push, hinge-swing, hold]
workspace: household-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

A cabinet door is opened far enough for access while maintaining clearance for the door swing and nearby items.

## Preconditions

- The cabinet is reachable and not intentionally locked.
- The actor can identify the door edge, handle, and hinge side.
- The swing area in front of the cabinet is clear.
- Any carried load is secure or set down.

## Steps

1. **Identify the hinge side.** Look for visible hinges or infer from the handle side. → *Expect:* predicted swing arc and pull direction are known.
2. **Stand outside the swing arc.** Position the body or chassis slightly to the handle side. → *Expect:* the door can open without striking the actor.
3. **Check adjacent clearance.** Inspect nearby walls, handles, appliances, and fragile objects in the arc. → *Expect:* no object blocks the first 90 degrees of motion.
4. **Grasp the handle or edge.** Use a full grip on the handle, knob, or safe outer edge. → *Expect:* grip is secure without fingers near the hinge gap.
5. **Release the latch.** Pull or press as the mechanism requires, using low force first. [BRANCH: pull door | push-latch door] pull a handle door; press and release a push-latch door. → *Expect:* door separates from the frame.
6. **Swing the door open.** Move the door through its hinge arc slowly, keeping wrist aligned with the handle path. → *Expect:* door opens without scraping or rebound.
7. **Stop at useful clearance.** Hold at 70 to 110 degrees unless the hinge or wall stop limits travel sooner. → *Expect:* cabinet interior is accessible and the door is not forced.
8. **Hold or park the door.** Keep a hand on springy or self-closing doors; release only if the door remains still. → *Expect:* door stays open at the selected angle.
9. **Re-scan the opening.** Check shelves and loose contents before reaching inside. → *Expect:* no item is falling or leaning out.

## Decision points

- Door opens toward another person → pause and communicate before moving the door farther.
- Hinges are hidden and direction is uncertain → pull lightly from the handle side and stop if resistance is high.
- Magnetic latch holds strongly → pull steadily, not with a jerk.
- Door is glass-fronted → support the handle side and avoid twisting.
- Door must be left open → confirm it does not block a walkway.

## Failure modes & recovery

- **F1 Door will not separate:** detect latch hold after gentle pull → check lock, push-latch action, or blocked contents before retrying.
- **F2 Door hits an obstacle:** detect contact in the swing arc → stop, close slightly, clear the obstacle, and reopen.
- **F3 Hinge binds:** detect scraping or uneven motion → stop before damage and report or use another cabinet.
- **F4 Contents shift outward:** detect item leaning past the shelf edge → hold the door still and stabilize the item before reaching further.
- **F5 Door rebounds closed:** detect spring or slope return → keep a hand on the handle while accessing the cabinet.

## Verification

The cabinet door is open to a stable access angle, the swing arc is clear, and no contents are falling from the cabinet.

## Variations

- `double-door`: open the primary latched door first, then the secondary door if needed.
- `overhead-cabinet`: stand close, keep the door above shoulder path, and watch for head clearance.
- `floor-cabinet`: squat rather than bending at the waist for low handles.
- `push-latch`: press once, wait for the door to pop out, then pull from the edge.

## Safety & privacy

Low risk. Keep fingers out of hinge gaps and avoid opening into a walkway without checking for people. Cabinets may contain private or hazardous items, so access only the needed compartment.
