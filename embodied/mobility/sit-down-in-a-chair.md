---
name: sit-down-in-a-chair
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
affordances: [approach, turn, contact-detect, descend, stabilize]
workspace: building-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

The actor sits in a chair with controlled descent, full seat contact, and stable posture before releasing support.

## Preconditions

- The chair is present, stable, and oriented for sitting.
- The seat is clear of objects, liquids, and unstable cushions.
- There is enough space to turn and back up to the chair.
- The actor can support body weight during descent.

## Steps

1. **Inspect the chair.** Check seat, legs, wheels, and armrests for stability. → *Expect:* chair appears able to support sitting.
2. **Approach from the front.** Move close enough to turn with the chair behind the actor. → *Expect:* seat front is within one backward step.
3. **Turn until aligned.** Rotate so the back of legs or rear base faces the seat. → *Expect:* body centerline aligns with the chair center.
4. **Back up slowly.** Move backward until the seat edge contacts the backs of legs or is detected by touch. → *Expect:* seat edge is felt at both legs or centered behind the base.
5. **Reach for support if available.** Place hands on armrests, seat edges, or stable thighs. → *Expect:* support points can take partial weight.
6. **Start controlled descent.** Bend knees and hips, sending hips back over the seat, not straight down in front of it. → *Expect:* body lowers while seat contact remains behind.
7. **Commit to the seat.** Continue lowering until weight transfers to the chair. → *Expect:* seat supports most body weight without sliding.
8. **Settle posture.** Shift hips fully back and place feet flat or base stable. → *Expect:* torso is upright and balanced.
9. **Release support.** Let go of armrests only after stability is confirmed. → *Expect:* actor remains seated without hand support.

## Decision points

- Chair has wheels → hold it, lock wheels if possible, or brace against a wall before sitting.
- Seat edge is not felt → do not descend; step forward, realign, and try again.
- Chair is low → use armrests and descend more slowly.
- Chair is unstable or broken → choose another chair.
- Carrying an object → place it down before sitting unless it is small and secure.

## Failure modes & recovery

- **F1 Chair moves backward:** detect seat edge retreating → stop descent, hold support, and reposition or lock the chair.
- **F2 Actor misses center:** detect one-sided seat contact → rise slightly, shuffle sideways, and lower again.
- **F3 Descent too fast:** detect uncontrolled drop → grip armrests, slow knees, and stop if possible.
- **F4 Object on seat:** detect pressure or obstruction under the actor → stand back up and clear the seat.
- **F5 Feet slide:** detect loss of traction → pause, reposition feet flat, and use armrests.

## Verification

The actor is fully seated on the chair, weight is supported by the seat, feet or base are stable, and hands can release support.

## Variations

- `armchair`: use both armrests for descent and final repositioning.
- `stool`: verify height and no back support; descend with extra control.
- `wheelchair-transfer`: lock brakes and follow a transfer-specific routine.
- `low-sofa`: widen stance and use hands for a deeper controlled descent.

## Safety & privacy

Low risk for stable chairs. Never descend until the seat edge is felt or visually confirmed behind the actor. Respect personal space if another person assists.
