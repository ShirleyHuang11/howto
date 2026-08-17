---
name: roll-dough-with-a-rolling-pin
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [dough, rolling-pin, flour, countertop, parchment-paper]
affordances: [grasp, press, roll, rotate, dust, lift]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

Flatten dough into an even sheet of the target thickness without sticking, tearing, or forcing it off the work surface.

## Preconditions

- Dough is rested or warmed enough to roll without cracking.
- Rolling surface is clean and dry.
- Rolling pin is clean.
- Flour or parchment is available for sticking control.

## Steps

1. **Prepare the surface.** Dust the counter lightly with flour or place parchment flat. → *Expect:* the dough contact area has a thin nonstick layer with no flour piles.
2. **Shape the dough disk.** Place dough in the center and press it by hand into a thick, even round or rectangle. → *Expect:* the dough has no tall mound in the middle.
3. **Roll from center outward.** Hold both pin handles or ends and push forward with even downward pressure. → *Expect:* the dough lengthens in the stroke direction without sticking to the pin.
4. **Rotate and repeat.** Lift or turn the dough a quarter turn between strokes, adding a light flour dusting if needed. → *Expect:* thickness spreads evenly in multiple directions.
5. **Check thickness by sight and touch.** Compare edges and center, then roll only the thicker zones with lighter passes. → *Expect:* the sheet has a consistent thickness within the recipe tolerance.
6. **Release the dough.** Slide a hand, scraper, or parchment under an edge to confirm it moves. → *Expect:* the dough lifts without tearing and is ready for cutting or transfer.

## Decision points

- Dough sticks → dust lightly, chill briefly, or roll between parchment sheets.
- Dough springs back → let it rest covered for 5 to 10 minutes before continuing.
- Edges crack → press cracks closed and roll with less force.

## Failure modes & recovery

- **F1 Pin sticking:** detect dough clinging to the rolling pin → dust the pin lightly and peel dough back gently.
- **F2 Uneven center:** detect a raised middle after several passes → roll from the center outward with shorter strokes.
- **F3 Dough tear:** detect an opening in the sheet → pinch edges together, dust underneath, and roll lightly over the repair.
- **F4 Too thin:** detect surface showing through or dough stretching when lifted → stop rolling and patch with a trimmed piece if the recipe allows.

## Verification

The dough sheet is the intended shape and thickness, releases from the surface, and has no major tears or stuck areas.

## Variations

- `pie-dough`: rotate often and keep dough cool to preserve flaky layers.
- `pizza-dough`: stretch by hand after partial rolling if the dough resists the pin.

## Safety & privacy

Low risk. Keep flour dust away from wet floors, keep the rolling pin on the counter when not held, and avoid leaning body weight onto brittle countertops.
