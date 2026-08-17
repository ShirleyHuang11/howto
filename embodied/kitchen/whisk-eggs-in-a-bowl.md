---
name: whisk-eggs-in-a-bowl
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 3min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [egg, bowl, whisk, fork, countertop]
affordances: [grasp, crack, pour, stir, beat, stabilize]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [bowl], human_proximity: continue}
---

## Goal

Combine egg yolks and whites in a bowl into a uniform beaten mixture ready for cooking or baking.

## Preconditions

- Eggs are cracked into a clean bowl with shells removed.
- A whisk or fork is clean.
- The bowl sits on a stable counter or mat.
- Hands or grippers are clean.

## Steps

1. **Stabilize the bowl.** Place one hand or gripper on the bowl rim or side without touching the egg. → *Expect:* the bowl does not slide when lightly nudged.
2. **Insert the whisk.** Hold the handle near its middle and lower the wires into the eggs at a shallow angle. → *Expect:* the whisk tip rests inside the liquid without scraping hard.
3. **Break the yolks.** Press and drag the whisk through each yolk before fast motion. → *Expect:* yellow yolk begins spreading through the clear whites.
4. **Whisk in small circles.** Move the wrist in tight circles while keeping the whisk tip below the liquid surface. → *Expect:* the mixture rotates in the bowl without splashing over the rim.
5. **Scrape the bowl path.** Sweep around the inner wall and across the bottom to collect streaks of white. → *Expect:* no large transparent egg-white pockets remain along the sides.
6. **Stop at uniform color.** Lift the whisk just above the surface and let liquid drip back into the bowl. → *Expect:* the eggs are evenly yellow and flow as one mixture.

## Decision points

- Bowl slides → place a damp towel or silicone mat underneath before continuing.
- Recipe asks for fluffy eggs → whisk longer with faster strokes until small bubbles appear.
- Recipe asks for lightly beaten eggs → stop once yolk and white are just combined.

## Failure modes & recovery

- **F1 Shell fragment remains:** detect a hard pale piece in the bowl → use a larger shell half or spoon edge to lift it out.
- **F2 Splashing:** detect droplets on the rim or counter → slow the stroke, lower the whisk tip, and wipe the spill.
- **F3 Unmixed white streaks:** detect clear strands clinging to the bowl → scrape the sides and whisk for another 10 seconds.
- **F4 Bowl tipping:** detect rim lifting under force → stop, recenter the bowl, and stabilize it with a wider contact.

## Verification

The bowl contains a shell-free egg mixture with uniform yellow color and no large clear streaks, and the counter is free of egg spills.

## Variations

- `fork`: tilt the fork slightly and beat with shorter strokes.
- `many-eggs`: use a larger bowl so the liquid depth stays below half the bowl height.

## Safety & privacy

Low risk. Treat raw egg as a contamination source; wash tools, hands, and any surface touched by raw egg before handling ready-to-eat food.
