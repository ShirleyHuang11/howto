---
name: sharpen-a-pencil
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
objects: [pencil, sharpener, blade, shavings, point]
affordances: [grasp, insert, rotate, inspect, clear, dispose]
workspace: household
safety: {hot_surfaces: false, sharp_objects: true, fragile: [pencil-point], human_proximity: continue}
---

## Goal

The pencil is sharpened to a centered usable point, and shavings are contained or cleared.

## Preconditions

- Sharpener hole fits the pencil diameter.
- Shavings container or trash is nearby.
- Pencil is dry and not cracked along the wood casing.

## Steps

1. **Inspect the pencil end.** Check whether the core is centered and the wood is intact. → *Expect:* pencil can enter the sharpener without splinters catching.
2. **Insert squarely.** Push the pencil straight into the sharpener hole along its axis. → *Expect:* pencil seats against the blade with no side angle.
3. **Steady the sharpener.** Hold the sharpener body or place it flat on the table. → *Expect:* sharpener does not rotate with the pencil.
4. **Turn steadily.** Rotate the pencil clockwise with light inward pressure. → *Expect:* continuous shavings form and resistance stays smooth.
5. **Pause and check.** Remove the pencil after several turns and inspect the exposed graphite. → *Expect:* wood tapers evenly toward a point.
6. **Continue if needed.** [BRANCH: dull point | sharp point] reinsert squarely for a few more turns or stop. → *Expect:* point reaches the needed length without breaking.
7. **Clear shavings.** Empty the sharpener chamber or brush loose shavings into trash. → *Expect:* blade path and table are free of debris.
8. **Test lightly.** Touch the point to scrap paper with normal writing pressure. → *Expect:* line appears without the point snapping.

## Decision points

- Lead breaks repeatedly → reduce pressure and inspect for a dropped or cracked pencil.
- Sharpener clogs → empty shavings before continuing.
- Colored pencil wax drags → use slower turns and stop at a shorter point.

## Failure modes & recovery

- **F1 Off-center point:** wood exposes more on one side → reinsert straighter and rotate with less side load.
- **F2 Broken tip:** point snaps during or after sharpening → sharpen fewer turns and test gently.
- **F3 Jammed shavings:** pencil stops turning smoothly → remove pencil, clear chamber, and resume.
- **F4 Blade contact risk:** fingers approach exposed blade → hold the sharpener body by its sides only.

## Verification

The pencil writes a clear line, the point is centered enough for use, and shavings are removed from the work area.

## Variations

- Hand-crank sharpener: insert until clamped, crank until resistance drops, then release.
- Mechanical pencil: advance lead instead of using a blade sharpener.

## Safety & privacy

Low risk from the sharpener blade and fragile point. Do not insert fingertips into the blade opening.
