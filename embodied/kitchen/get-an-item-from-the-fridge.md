---
name: get-an-item-from-the-fridge
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [fridge, door, shelf, food-item, container]
affordances: [open, locate, grasp, lift, carry, close]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [jar, bottle], human_proximity: continue}
---

## Goal

The requested item is retrieved from the refrigerator and the door is closed promptly.

## Preconditions

- The refrigerator is reachable and can be opened without blocking the walkway.
- The requested item is known by name, appearance, or location.
- Hands are clean and dry enough to grip cold containers.

## Steps

1. **Approach and check clearance.** Stand beside the door swing path with feet stable. → *Expect:* the door can open without hitting body, cabinets, or people.
2. **Open the door.** Pull the handle smoothly until shelves are visible, keeping the door under control. → *Expect:* interior light turns on and cold shelves are accessible.
3. **Locate the item.** Scan shelves from top to bottom, then door bins, using label, shape, or parent-task cue. → *Expect:* the target item or a likely candidate is visible.
4. **Clear access.** Move blocking items only as far as needed and keep them upright. → *Expect:* a direct hand path reaches the target.
5. **Grasp securely.** Hold jars and bottles around the body, cartons at the sides, and open containers from below. → *Expect:* the item lifts without slipping or tilting.
6. **Withdraw level.** Pull the item straight out, clearing shelf lips and nearby containers. → *Expect:* no neighboring item falls or drags forward.
7. **Close the door.** Push the door shut with hand or hip after the item is clear. → *Expect:* gasket contacts the frame and interior light turns off.
8. **Set or deliver.** Place the cold item on the counter or carry it level to the next task. → *Expect:* the item rests upright and condensation or cold surface is manageable.

## Decision points

- Item is not visible → check common zones, then stop and ask rather than rearranging the entire fridge.
- Container feels slippery from condensation → use two hands or dry the outside before carrying.
- Door alarm sounds → close the door and resume searching later if needed.

## Failure modes & recovery

- **F1 Wrong item:** label or contents do not match → return it to the original location and search again.
- **F2 Neighbor item shifts:** another container moves toward the edge → stabilize it before removing the target.
- **F3 Door left open:** cold air continues escaping → close immediately, then continue with the retrieved item.
- **F4 Loose lid:** container lid flexes or lifts → support from below and avoid tilting until set down.

## Verification

The requested item is outside the fridge, upright and under control, and the refrigerator door is fully closed.

## Variations

- `freezer`: expect frost, heavier door resistance, and colder surfaces that reduce grip time.
- `shared-fridge`: preserve item positions and labels when moving blockers.
- `fragile-jar`: use two hands and avoid gripping only the lid.

## Safety & privacy

Low risk. Close the door promptly for food safety, keep cold items upright, and do not inspect private containers beyond what is needed to identify the requested item.
