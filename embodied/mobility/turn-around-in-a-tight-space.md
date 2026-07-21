---
name: turn-around-in-a-tight-space
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [walls, furniture, floor]
affordances: [scan, step, pivot, pause, stabilize]
workspace: building-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [furniture], human_proximity: slow}
---

## Goal

The actor reverses facing direction in a confined area using small controlled steps and repeated clearance checks.

## Preconditions

- The floor surface is stable and not slippery.
- There is enough room for at least a multi-step turn in place.
- Carried objects are secure and not protruding unexpectedly.
- Nearby people, walls, and furniture can be observed or sensed.

## Steps

1. **Stop before turning.** Halt forward motion and center weight over the feet or base. → *Expect:* actor is still and balanced.
2. **Scan the full turn area.** Look or sense left, right, behind, floor level, and shoulder height. → *Expect:* nearest obstacles and free side are identified.
3. **Choose turn direction.** Select the side with greater clearance for shoulders, hips, load, and feet. → *Expect:* turn path is planned.
4. **Shorten stance.** Bring feet or wheelbase into a compact stable position without crossing legs. → *Expect:* support base fits within the available floor area.
5. **Take the first small step.** Move the lead foot or base a few degrees into the turn. → *Expect:* no contact with obstacle and balance remains stable.
6. **Pivot the body after the foot.** Rotate hips, torso, and carried load to follow the lead direction. → *Expect:* body orientation changes without dragging or twisting.
7. **Repeat small steps.** Continue step, pivot, pause cycles until near the target direction. [BRANCH: enough clearance | tight clearance] continue normally if clear; reduce step size and re-scan more often if tight. → *Expect:* orientation changes progressively.
8. **Re-scan after halfway.** Check the new blind side and floor before finishing. → *Expect:* no newly exposed obstacle blocks completion.
9. **Finish and stabilize.** Align feet or base in the new direction and pause. → *Expect:* actor faces the opposite direction without contact or sway.

## Decision points

- Clearance is less than foot length or base width → back out instead of turning in place.
- A carried object extends beyond body width → set it down or rotate it vertically.
- A person enters the space → pause until they pass or coordinate verbally.
- Floor has a rug edge or threshold → step over it deliberately during the turn.
- Balance degrades → stop, widen stance if possible, and use a support surface.

## Failure modes & recovery

- **F1 Foot crosses and traps:** detect legs crossing or wheel bind → stop, uncross with a small backward step, and restart.
- **F2 Shoulder or load contacts wall:** detect touch or scrape → stop rotation, step away from contact, and reduce turn radius.
- **F3 Loss of orientation:** detect uncertainty about facing direction → pause and re-scan landmarks before moving.
- **F4 Backward obstacle appears:** detect contact behind heel or base → shift forward and choose the other turn direction.
- **F5 Person too close:** detect human within arm length → pause and ask them to clear space.

## Verification

The actor faces the intended new direction, remains balanced, and has made no contact with nearby walls, furniture, objects, or people.

## Variations

- `with-walker`: lift or roll the walker a small angle first, then step feet inside its frame.
- `with-long-load`: rotate the load vertically or carry it close to the torso.
- `narrow-hall`: use a three-point turn with small forward and backward adjustments.
- `wheeled-robot`: rotate in increments and verify rear-swing clearance after each increment.

## Safety & privacy

Low risk but close to people or fragile furniture requires slower movement. Keep turns segmented, never blind, and pause when human proximity reduces clearance.
