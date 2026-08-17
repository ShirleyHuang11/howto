---
name: spray-and-wipe-a-surface
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [spray-bottle, cloth, surface, paper-towel, cleaner]
affordances: [grasp, spray, wipe, fold, press, inspect]
workspace: household
safety: {hot_surfaces: false, sharp_objects: false, fragile: [electronics, decor], human_proximity: continue}
---

## Goal

Apply cleaner to a compatible surface and wipe it dry or evenly damp without streaks, residue, or overspray damage.

## Preconditions

- Cleaner is appropriate for the surface material.
- Loose items, papers, and electronics are moved away or protected.
- Cloth or paper towel is clean.
- Area has enough ventilation for the product.

## Steps

1. **Clear and inspect the surface.** Move objects aside and look for loose grit or liquid. → *Expect:* the wipe path is open and hazards are visible.
2. **Aim the spray safely.** Hold the nozzle 15 to 25 cm from the surface, pointed away from faces and electronics. → *Expect:* the spray cone lands only on the intended area.
3. **Apply a light mist.** Squeeze the trigger once or twice over the dirty area. → *Expect:* the surface is damp, not puddled.
4. **Wipe in overlapping strokes.** Fold the cloth flat and press lightly from the far edge toward the near edge. → *Expect:* soil transfers to the cloth and the surface becomes clearer.
5. **Turn the cloth to a clean face.** Refold or replace it when the wiping side looks dirty or wet. → *Expect:* later strokes do not smear residue back onto the surface.
6. **Dry and inspect.** Make final dry passes along the grain or edge direction. → *Expect:* the surface has no wet streaks, visible debris, or cleaner pools.

## Decision points

- Surface is wood, stone, screen, or unfinished material → spray the cloth instead of the surface and use compatible cleaner only.
- Soil is dried on → let cleaner dwell briefly if the label allows.
- Strong odor appears → stop spraying and increase ventilation.

## Failure modes & recovery

- **F1 Overspray:** detect droplets on nearby objects → wipe them immediately and move objects farther away.
- **F2 Streaks:** detect cloudy lines after wiping → use a clean dry cloth with lighter pressure.
- **F3 Cleaner beads up:** detect droplets not wetting the surface → confirm the surface finish and switch to a compatible product.
- **F4 Cloth saturated:** detect liquid dripping from cloth → replace or wring it before continuing.

## Verification

The cleaned surface is free of visible debris, has no standing liquid or streaks, and nearby objects are dry.

## Variations

- `glass`: use vertical strokes on one side and horizontal on the other to locate streaks.
- `food-contact`: rinse or wipe with water after cleaner if the product label requires it.

## Safety & privacy

Low risk. Do not mix cleaners, avoid spraying into air near people, and move private documents before wiping desks or counters.
