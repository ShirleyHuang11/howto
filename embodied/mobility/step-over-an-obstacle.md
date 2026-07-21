---
name: step-over-an-obstacle
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: basic
est_time: 2min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [obstacle, floor, shoe, handrail, cane]
affordances: [look, balance, lift-foot, step, weight-shift, clear, stabilize]
workspace: walkway
safety: {hot_surfaces: false, sharp_objects: false, fragile: [carried-item], human_proximity: slow}
---

## Goal

Step over a visible obstacle without tripping, kicking it, or losing balance, while keeping attention on the path ahead.

## Preconditions

- The obstacle is low enough to step over safely.
- Floor on both sides is stable and not slippery.
- Shoes or feet have enough traction.
- Hands are free or a support is available if balance is uncertain.

## Steps

1. **Slow before reaching it.** Shorten stride and stop if needed. → *Expect:* both feet are under control before the obstacle.
2. **Assess height and width.** Look at the tallest part and the landing area beyond it. → *Expect:* you know whether stepping over is realistic.
3. **Choose the lead leg.** Use the stronger or more comfortable leg first. → *Expect:* lead foot can lift higher than the obstacle.
4. **Move close enough.** Stand about one foot length before the obstacle. → *Expect:* the lead foot does not need to stretch far forward.
5. **Shift weight to the support leg.** Press down through the standing foot and steady with a rail, cane, or wall if available. → *Expect:* balance feels stable before lifting.
6. **Lift the lead foot high.** Bend hip and knee so toes clear the obstacle. → *Expect:* the lead foot passes above the highest point.
7. **Place the lead foot beyond it.** Land flat on clear floor, not on the obstacle edge. → *Expect:* the lead foot bears weight securely.
8. **Shift weight forward.** Bring body weight over the lead foot before moving the trailing foot. → *Expect:* the trailing foot feels light enough to lift.
9. **Clear the trailing foot.** Lift the knee and toes rather than dragging. → *Expect:* the trailing foot passes over without touching.
10. **Look ahead and continue.** Return gaze to the path after both feet clear. → *Expect:* walking resumes without a stumble.

## Decision points

- If the obstacle is above mid-shin or unstable → go around or move it instead of stepping over.
- If carrying something blocks view → set it down or ask for help before crossing.
- If balance is poor → use a handrail, cane, or another person trained to assist.
- If the floor beyond is wet or cluttered → clear or avoid the path first.

## Failure modes & recovery

- **F1 Toe catches:** detect contact with the obstacle → stop, regain balance, and lift the knee higher on the next attempt.
- **F2 Overreach:** detect a long stretched landing → step closer before crossing or choose another route.
- **F3 Trailing foot drag:** detect scraping after the first foot lands → shift weight fully forward, then lift the trailing knee.
- **F4 Balance loss:** detect wobble or arm flailing → pause, grab stable support, and do not continue until steady.

## Verification

Both feet pass completely over the obstacle and land on stable floor beyond it, with no contact that moves the obstacle and no loss of balance.

## Variations

- With cane: plant the cane on the far side or beside the support foot according to personal gait training.
- On stairs: avoid stepping over objects on stairs; remove the obstacle first.
- Robot pathing: treat unknown soft objects as obstacles to route around rather than step over.

## Safety & privacy

Medium risk from trips and falls. Do not step over sharp, rolling, high, or unstable objects, and do not prioritize speed over a clear landing zone.
