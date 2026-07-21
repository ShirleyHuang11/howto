---
name: place-an-object-on-a-shelf
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
objects: [object, shelf]
affordances: [carry, reach, align, place, release]
workspace: household-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [object], human_proximity: continue}
---

## Goal

An object is placed fully on a shelf with clearance from the edge and enough stability to remain there unattended.

## Preconditions

- The shelf is reachable and rated for the object's weight.
- The shelf surface is visible or can be felt safely.
- The carried object is stable in the hand or gripper.
- The target area is not occupied by unstable items.

## Steps

1. **Approach the shelf squarely.** Move until the shelf is centered in front of the body or manipulator. → *Expect:* target shelf is within reach without leaning far forward.
2. **Confirm shelf height.** Raise an empty hand or the object close to the shelf plane without contact. → *Expect:* the placement height is known and shoulder or actuator range is comfortable.
3. **Inspect the landing area.** Look for obstacles, lips, loose papers, or nearby fragile items. → *Expect:* a flat landing zone larger than the object base is identified.
4. **Raise the object near the body.** Lift to shelf height with elbows bent or manipulator joints inside normal range. → *Expect:* object remains level and controlled.
5. **Clear the front edge.** Move the object forward until the entire base passes over the shelf edge. → *Expect:* no part of the object is hanging below or catching on the edge.
6. **Lower onto the shelf.** Descend vertically until the base makes contact, keeping fingers clear of pinch points. → *Expect:* the shelf supports the object's weight.
7. **Slide inward if needed.** Push gently away from the front edge until the object is fully inside the shelf footprint. → *Expect:* the object's center of mass is behind the shelf edge.
8. **Release gradually.** Open fingers or gripper while maintaining a light guard nearby. → *Expect:* object stays in place without tilting or rolling.
9. **Withdraw without contact.** Move the hand back along the entry path. → *Expect:* nearby shelf items remain undisturbed.

## Decision points

- Shelf is above comfortable reach → use a step stool, lower shelf, or request assistance.
- Object base is round or unstable → place it in a bin, against a backstop, or on a flat side.
- Shelf flexes under load → remove the object and choose a stronger shelf.
- Landing area is crowded → clear space before raising the object.
- Actor must stretch on toes → stop and use a height aid.

## Failure modes & recovery

- **F1 Object catches on lip:** detect forward motion blocked at shelf edge → lift slightly, move farther inward, and lower again.
- **F2 Object tips after contact:** detect tilt or rocking → re-grip before release and rotate to a flatter support face.
- **F3 Shelf item shifts:** detect adjacent item moving → pause, stabilize both items, and create more clearance.
- **F4 Grip cannot release cleanly:** detect fingers trapped under the object → lift a few millimeters, reposition fingers, and lower again.
- **F5 Shelf overload appears:** detect bending, creaking, or sliding → remove the object and select another location.

## Verification

The object rests fully on the shelf, at least one object depth from the front edge when space allows, and remains still after release.

## Variations

- `high-shelf`: use two-stage placement onto a stable intermediate surface before final placement.
- `fragile-object`: use two hands and release only after no rocking is visible.
- `narrow-shelf`: orient the longest dimension parallel to the shelf back.
- `lidded-container`: keep the lid side upright unless labeled otherwise.

## Safety & privacy

Low risk for light objects. Avoid overhead placement of heavy, sharp, or fragile items where a fall could strike a person. Keep the line of sight open during the reach.
