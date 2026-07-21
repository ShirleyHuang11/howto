---
name: turn-a-stove-burner-on-and-off
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 2min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [stove, burner, knob, pan, match, lighter]
affordances: [identify, turn, press, ignite, observe, verify]
workspace: kitchen
safety: {hot_surfaces: true, sharp_objects: false, fragile: [], human_proximity: slow}
---

## Goal

The intended stove burner is turned on to a controlled heat level and later fully turned off with the correct knob verified.

## Preconditions

- The stovetop is clear of paper, towels, packaging, and loose utensils.
- The correct pan or pot is centered on the target burner if cooking will begin.
- Ventilation is available, and the actor can see the burner and knob labels.

## Steps

1. **Identify the target burner.** Match the burner position to the printed knob diagram before touching the knob. → *Expect:* the selected knob corresponds to the intended front, rear, left, or right burner.
2. **Clear the area.** Move flammable items and handles away from adjacent burners. → *Expect:* only heat-safe cookware is near the burner.
3. **Prepare ignition.** [BRANCH: electric | gas] For electric, set hand on the knob; for gas, have the igniter, match, or built-in spark ready. → *Expect:* ignition method is available before gas flow starts.
4. **Turn on gradually.** Press or turn the correct knob to the ignition or low setting, following the knob's required push-turn motion. → *Expect:* the target burner starts heating or gas clicks for ignition.
5. **Verify active heat.** For gas, confirm a stable blue flame around the ring; for electric, confirm indicator light or visible coil glow. → *Expect:* only the intended burner is active.
6. **Adjust to target.** Rotate the knob slowly to low, medium, or high while watching the flame size or heat indicator. → *Expect:* heat output changes smoothly and cookware remains centered.
7. **Turn off deliberately.** Rotate the same knob back to OFF until it stops. ⚠️ *Irreversible:* leaving gas or heat on can cause fire, burns, or gas buildup, so verify before walking away. → *Expect:* the knob pointer aligns exactly with OFF.
8. **Off-verify.** Look at the burner, indicator light, and flame area for five seconds. → *Expect:* flame is out, indicator is off or cooling, and no gas smell increases.

## Decision points

- Flame does not ignite within a few seconds → turn knob OFF, wait for gas to dissipate, then retry once.
- Wrong burner activates → turn it OFF immediately, wait for hot surfaces to cool, and restart identification.
- Gas smell persists after OFF → do not relight; ventilate and leave the area if smell grows.

## Failure modes & recovery

- **F1 Wrong knob:** adjacent burner heats or lights → turn that knob OFF, mark the correct mapping visually, and restart.
- **F2 No ignition:** clicking occurs without flame → turn OFF, wait, then use the approved ignition method or stop.
- **F3 Flame unstable:** flame lifts, sputters, or burns yellow → lower setting; if unstable persists, turn OFF and do not use.
- **F4 Off not confirmed:** knob looks near but not at OFF → turn until the stop is reached and recheck flame or indicator.

## Verification

The intended burner can be observed active when on, and after shutdown its matched knob is at OFF with no flame and no active heat indicator.

## Variations

- `induction`: burner may not heat without compatible cookware, so verify by display and pan response.
- `sealed-electric`: glow fades slowly after OFF, so treat the surface as hot until the hot-surface light clears.
- `gas-manual-light`: light source is active before turning gas on, and face stays back from the burner.

## Safety & privacy

Medium risk from flame, gas, and hot surfaces. Keep body parts above and away from the burner, keep handles turned inward, and slow or pause when another person reaches near the stovetop.
