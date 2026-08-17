---
name: push-a-wheelchair
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [wheelchair, person, handles, brakes, footrests, doorway]
affordances: [ask, grip, push, brake-lock, turn, threshold-cross]
workspace: indoor-walkway
safety: {hot_surfaces: false, sharp_objects: false, fragile: [medical-device], human_proximity: pause}
---

## Goal

Move a seated wheelchair user a short distance while preserving their control, comfort, and safety.

## Preconditions

- The person agrees to be pushed and states the destination.
- Feet, clothing, bags, and medical tubing are clear of wheels.
- The chair is functional and the route is visible.

## Steps

1. **Ask permission and destination.** Confirm where to go and whether the person wants help. → *Expect:* the person gives consent and a destination.
2. **Check the chair setup.** Confirm brakes release, footrests support feet, and loose items are clear of spokes. → *Expect:* the chair can roll without dragging or catching.
3. **Grip both handles.** Stand behind the chair with hands on push handles and feet ready to step. → *Expect:* the chair is controlled from both sides.
4. **Announce movement.** Say that you are starting before pushing. → *Expect:* the person is not startled and can brace if needed.
5. **Push smoothly.** Move at walking speed and keep enough clearance from walls, furniture, and people. → *Expect:* the chair tracks forward without jolts.
6. **Slow for turns and thresholds.** Approach squarely, reduce speed, and lift only if trained and necessary. → *Expect:* wheels cross without stopping abruptly.
7. **Stop beside the destination.** Position the chair with room for transfer or conversation. → *Expect:* the person is near the requested place and not blocking a walkway.
8. **Lock the brakes before release.** Engage both brakes and confirm the chair does not roll. → *Expect:* the chair remains stationary when handles are released.

## Decision points

- Person says stop or changes destination → stop immediately and follow the updated instruction.
- Route has a steep ramp or curb → use an accessible route or get trained assistance.
- Person needs to self-propel → move behind or beside them without taking control.
- Chair pulls to one side → stop and inspect wheels, brakes, or floor obstacles.

## Failure modes & recovery

- **F1 Foot slips from footrest:** detect foot near floor or caster → stop, lock brakes, and help reposition only with consent.
- **F2 Wheel catches obstacle:** detect sudden resistance → stop, back up slightly, clear the obstacle, and retry squarely.
- **F3 Person startles:** detect flinch or verbal distress → stop and explain before resuming.
- **F4 Brake left on:** detect dragging or uneven rolling → stop and release the engaged brake.

## Verification

The person is at the requested destination, the wheelchair brakes are locked, feet and belongings are clear of wheels, and the helper has released the handles.

## Variations

- Outdoor path: avoid gravel, steep slopes, and wet curb cuts when possible.
- Elevator: board backward only if needed for space, then turn safely inside.
- Tight doorway: protect hands and elbows by centering the chair before crossing.

## Safety & privacy

Medium risk from falls, collisions, and loss of autonomy. Ask before touching the chair, pause on any refusal or distress, and do not discuss the person's condition with bystanders.
