---
name: pick-up-an-object-from-the-floor
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
objects: [floor-object, floor]
affordances: [approach, squat, grasp, lift, stabilize]
workspace: household-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [floor-object], human_proximity: continue}
---

## Goal

An object resting on the floor is lifted to a stable carried position without dropping it or losing balance.

## Preconditions

- The object is visible, reachable, and safe to touch.
- The floor around the object has enough stance space for two feet or a stable chassis.
- The object weight is within the actor's lifting capacity.
- At least one hand or gripper is free.

## Steps

1. **Approach with a clear path.** Move toward the object until it is centered between the feet or directly in front of the base. → *Expect:* object is within comfortable arm reach and no obstacle blocks the stance.
2. **Stop and classify the object.** Estimate size, weight, fragile surfaces, and best grip points before lowering. → *Expect:* a planned grip location and lifting direction are identified.
3. **Set a stable stance.** Place feet shoulder-width apart, one foot slightly forward if needed, with knees unlocked. → *Expect:* body weight is balanced over the base of support.
4. **Bend using knees and hips.** Squat or hinge down with the back neutral, keeping the object close to the centerline. → *Expect:* hand or gripper reaches the object without overextending.
5. **Form the grip.** Close fingers or gripper around solid sides, under an edge, or through a handle. [BRANCH: handle available | no handle] use the handle if present; otherwise use opposing sides. → *Expect:* object resists a light upward test without slipping.
6. **Lift with legs.** Press through the feet and extend knees and hips while keeping the object close to the torso or chassis. → *Expect:* object leaves the floor smoothly without twisting the spine or base.
7. **Pause at knee height.** Hold for one beat and check grip, object orientation, and balance. → *Expect:* no wobble, sliding, or unexpected weight shift.
8. **Bring to carry height.** Raise or tuck the object to a stable carried position that does not block vision or foot placement. → *Expect:* object is secure and the actor can stand upright.
9. **Re-scan before moving.** Look at the floor path and nearby people before taking a step. → *Expect:* route is clear enough to continue.

## Decision points

- Object is too heavy → stop before lifting; use a cart, second person, or divide the load.
- Object is wet, oily, or flexible → choose a larger contact area and lift slowly from underneath.
- Object is fragile → support from below and avoid squeezing side walls.
- Object is sharp or contaminated → use gloves, a tool, or a different recipe.
- Balance feels unstable during descent → stand back up without the object and reset stance.

## Failure modes & recovery

- **F1 Grip slips:** detect motion between hand and object → set the object down, choose a wider grip, and retry.
- **F2 Back strain starts:** detect pain or rounding under load → lower the object immediately and use a lower squat or assistance.
- **F3 Object catches on floor:** detect scraping or no vertical movement → stop lifting, free the caught edge, and lift straight up.
- **F4 Vision is blocked:** detect inability to see the next step area → lower the carry height or switch to two-handed front carry.
- **F5 Balance shifts backward:** detect heel lift or sway → lower the object close to the body and widen stance.

## Verification

The object is off the floor, held securely at carry height, and the actor is upright with stable balance for at least two seconds.

## Variations

- `small-object`: pinch or scoop with one hand after confirming it is not sharp.
- `box`: grip opposite lower corners and keep the box face level.
- `soft-item`: gather enough material to prevent dragging before lifting.
- `wheeled-base`: lock or steady wheels before lowering the manipulator.

## Safety & privacy

Low risk when the object is light and known. Do not lift unknown sharp, hot, leaking, or biohazard objects with bare hands. Keep the load close to reduce tipping and strain.
