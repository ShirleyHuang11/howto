---
name: pour-from-a-carton
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [carton, cap, cup, bowl, liquid]
affordances: [grasp, open, align, tilt, pour, close]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [cup, bowl], human_proximity: continue}
---

## Goal

Liquid is poured from a carton into a target container at a controlled rate with enough headroom to prevent spill.

## Preconditions

- The carton contains the intended liquid and is not expired if the label is relevant.
- The target cup, bowl, or measuring vessel is clean and stable.
- The carton cap or seal can be opened without tearing the spout.

## Steps

1. **Inspect and orient.** Hold the carton upright and locate the spout, fill weight, and cap. → *Expect:* the spout faces the target side and the carton is not leaking.
2. **Open the cap.** Twist or flip the cap fully open and keep it attached or set it in a clean visible place. → *Expect:* the pouring opening is unobstructed.
3. **Position the target.** Place the target on the counter below the spout path rather than holding it in midair. → *Expect:* the target remains stable and has visible headroom.
4. **Grip for control.** Use one hand around the carton body and the other under the base if it is heavy. → *Expect:* the carton can tilt without buckling.
5. **Tip spout down.** Tilt slowly until the liquid just begins to flow from the lower edge of the spout. → *Expect:* a narrow stream enters the target.
6. **Control rate.** Increase tilt only enough to maintain a steady stream, watching the rising fill level. → *Expect:* liquid level rises smoothly without splashing the rim.
7. **Stop before full.** Return the carton upright when the target has required amount or at least two centimeters headroom. → *Expect:* flow stops before reaching the rim.
8. **Prevent the drip.** Hold upright over the target for a beat, then move the carton away and close the cap. → *Expect:* final drops land in the target and the cap seals.

## Decision points

- Carton is nearly full → use two hands and a smaller tilt angle because flow starts abruptly.
- Carton is nearly empty → tilt farther and expect intermittent flow.
- Foam forms in the target → stop earlier to preserve headroom.

## Failure modes & recovery

- **F1 Glugging stream:** liquid pulses and splashes → reduce tilt and rotate the spout so air can enter above the stream.
- **F2 Drip after pour:** drop trails onto counter → pause over target longer and wipe the carton lip.
- **F3 Overfill:** liquid approaches the rim → stop immediately and sip or transfer some out before moving the target.
- **F4 Cap misplaced:** cap is not visible after opening → keep carton upright, find cap, and close before storage.

## Verification

The target contains the desired liquid below its rim, the carton is upright and closed, and no active drip remains on the spout.

## Variations

- `milk-carton`: smell check may be part of the parent food-safety recipe.
- `broth-carton`: shake before opening only if the label calls for it.
- `measuring-cup`: read the meniscus at counter height before stopping.

## Safety & privacy

Low risk. Use headroom, keep the target on a surface, and close the carton before returning it to storage so it cannot spill in the fridge.
