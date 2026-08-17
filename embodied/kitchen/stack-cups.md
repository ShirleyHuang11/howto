---
name: stack-cups
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [cups, cupboard, shelf]
affordances: [grasp, lift, align, lower, stack]
workspace: kitchen counter or cupboard
safety: {hot_surfaces: false, sharp_objects: false, fragile: [cups], human_proximity: continue}
---

## Goal

Cups are nested or stacked upright in a stable vertical group on the shelf or counter.

## Preconditions

- Cups are empty, dry, and cool.
- Cup diameters are compatible for stacking or nesting.
- The target surface is flat and reachable.

## Steps

1. **Clear the target surface.** Sweep the placement area with a light open-hand pass and remove loose items. → *Expect:* a flat area wider than the largest cup is unobstructed.
2. **Place the base cup.** Grasp the largest cup around the side wall, keep the open rim facing upward, and lower it until the base contacts the surface. → *Expect:* the cup stands upright without wobble.
3. **Select the next cup.** Choose a cup with an equal or smaller rim diameter and grip it near the upper side wall. → *Expect:* the cup is controlled with the open rim still facing upward.
4. **Align over the base.** Center the next cup above the base cup with rims parallel and vertical axes aligned. → *Expect:* the lower cup rim is evenly visible around the upper cup.
5. **Lower gently.** Descend with light force until the upper cup settles into or onto the lower cup. → *Expect:* contact is quiet and the stack height stops changing.
6. **Repeat for remaining cups.** Add cups largest to smallest, re-centering after each placement. → *Expect:* the stack remains vertical and no cup edge catches.
7. **Check stability.** Release the stack, then lightly tap the shelf beside it without touching the cups. → *Expect:* cups remain upright and do not slide.

## Decision points

- Cups have handles that collide → rotate each handle to the same side or make a separate stack.
- Stack leans after a placement → remove the top cup and re-center before continuing.
- Cup surfaces are wet → dry them before stacking to reduce slipping.

## Failure modes & recovery

- **F1 Cup jams:** detect by stopped descent with one rim tilted → lift straight up, rotate 30 degrees, and lower again with less force.
- **F2 Stack wobbles:** detect by visible leaning or rocking after release → remove upper cups and rebuild with the widest cup at the bottom.
- **F3 Cup chips or cracks:** detect by sharp edge or visible fracture → stop stacking and move the damaged cup to disposal or repair.

## Verification

All cups are empty, upright, vertically aligned, and stable for 5 seconds after release with no cup contacting a fragile neighboring item.

## Variations

- Mugs with handles: stack only if designed to nest; otherwise place side by side with handles alternating.
- Tall plastic tumblers: allow deeper nesting but keep the stack below shelf clearance.

## Safety & privacy

Use low grip and lowering force around ceramic or glass cups. No private information is handled.
