---
name: use-a-pizza-cutter
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 3min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [pizza-cutter, pizza, cutting-board, plate, tray]
affordances: [grasp, press, roll, stabilize, cut, lift]
workspace: kitchen
safety: {hot_surfaces: true, sharp_objects: true, fragile: [plate], human_proximity: slow}
---

## Goal

Cut a pizza or flat baked item into portions using a rolling pizza cutter without dragging toppings or damaging the surface.

## Preconditions

- Pizza sits on a cutting board, pan, or tray safe for cutting.
- Cutter wheel is clean and rotates freely.
- Pizza is cool enough that steam will not burn the operator.
- The surface is stable and not near an edge.

## Steps

1. **Grip the cutter handle.** Hold with the wheel vertical and fingers behind the guard or handle. → *Expect:* the wheel points down and away from hands.
2. **Stabilize the pizza surface.** Hold the pan, board, or tray edge away from the cut line. → *Expect:* the pizza does not slide when touched by the wheel.
3. **Place wheel at the crust edge.** Align the wheel with the intended diameter or cut path. → *Expect:* the cutter is perpendicular to the pizza surface.
4. **Roll through with steady pressure.** Push from one edge to the opposite edge in a single line. → *Expect:* crust and toppings separate along the path.
5. **Repeat for portions.** Rotate the board or change cutter angle for the next cut while keeping hands out of the wheel path. → *Expect:* slices have distinct boundaries.
6. **Check and finish attached spots.** Re-roll only over connected cheese or crust, then lift the cutter clear. → *Expect:* each slice can separate without tearing adjacent slices.

## Decision points

- Pizza is on a nonstick pan → transfer to a cutting board or use a plastic-safe cutter.
- Toppings drag with the wheel → pause between cuts and clear the wheel with a utensil.
- Crust is very thick → use two passes with firm downward pressure rather than sawing.

## Failure modes & recovery

- **F1 Surface slips:** detect board or pan moving during the cut → stop, brace the surface, or place a towel underneath.
- **F2 Incomplete cut:** detect cheese strands or crust bridges → repeat along the same line with more pressure.
- **F3 Wheel jam:** detect toppings stuck in the axle → set cutter down, clear with a brush or utensil, and wash if needed.
- **F4 Hand in path:** detect stabilizing fingers ahead of the wheel → pause and move the hand to the board edge.

## Verification

The pizza is divided into intended portions, each slice separates cleanly, and the cutter wheel has not contacted hands or an unsafe surface.

## Variations

- `flatbread`: use lighter pressure to avoid cracking thin crust.
- `dessert-bars`: chill soft bars first so the cutter leaves clean lines.

## Safety & privacy

Medium risk from the sharp wheel and hot food. Keep the wheel path clear, treat hot pans as hot surfaces, and wash the cutter with the wheel facing away.
