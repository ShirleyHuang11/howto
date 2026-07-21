---
name: stand-up-from-a-chair
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [chair, seat, armrests]
affordances: [foot-place, lean, push, rise, stabilize]
workspace: building-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

The actor rises from a chair to a stable standing posture and pauses before taking the first step.

## Preconditions

- The chair is stable and not sliding.
- Feet can contact the floor with enough traction.
- The path in front of the chair is clear.
- Hands or armrests are available if support is needed.

## Steps

1. **Check the floor path.** Look for objects, cords, rugs, or people in front of the chair. → *Expect:* standing space and first-step area are clear.
2. **Move hips forward.** Scoot toward the front third of the seat while keeping balance. → *Expect:* feet can move underneath the knees.
3. **Place feet back.** Set both feet flat, hip-width apart, with heels slightly behind knees if possible. → *Expect:* shins angle forward and feet can push.
4. **Set hands for support.** Place hands on armrests, seat edges, or thighs, not on a moving table. → *Expect:* support points are stable.
5. **Lean forward.** Bring nose and chest over the toes while keeping the back long. → *Expect:* weight shifts from seat toward feet.
6. **Push up.** Press through feet and support points while extending knees and hips. → *Expect:* hips lift from the seat.
7. **Stand fully.** Straighten to upright without stepping unless balance requires it. → *Expect:* knees and hips are extended and torso is vertical.
8. **Steady before moving.** Pause for two seconds and check for dizziness, sway, or foot slip. → *Expect:* balance is stable.
9. **Take the first step only after stable.** Move in the intended direction with eyes on the path. → *Expect:* step begins without stumble or chair contact.

## Decision points

- Dizziness occurs → sit back down if possible and wait before retrying.
- Chair has wheels → lock wheels or hold armrests while rising.
- Feet cannot move back enough → scoot forward or choose a higher seat.
- No armrests → use thighs and stronger forward lean.
- Holding an object → place it down before standing unless it is very light.

## Failure modes & recovery

- **F1 Feet slide forward:** detect loss of traction → sit back down, reposition feet, and clear slick surfaces.
- **F2 Chair moves:** detect backward slide or swivel → pause, lock or brace chair, and retry.
- **F3 Insufficient lift:** detect hips not clearing seat → scoot forward, lean farther over toes, and push through legs.
- **F4 Backward fall risk:** detect shoulders behind hips after lift → lean forward again or sit back safely.
- **F5 Lightheadedness:** detect dizziness or visual change → sit immediately and wait for recovery.

## Verification

The actor is standing upright, no longer supported by the chair, balanced for at least two seconds, and ready to step.

## Variations

- `low-chair`: use armrests or a raised cushion to reduce required leg force.
- `soft-sofa`: scoot farther forward because the cushion edge compresses.
- `with-cane`: stand first, then take the cane into the support hand before stepping.
- `robot-base`: verify center of mass stays inside wheel or foot support polygon during lift.

## Safety & privacy

Low risk for most actors. Pause after standing because dizziness and balance shifts often appear after the lift, not before it. Assistance requires consent and clear communication.
