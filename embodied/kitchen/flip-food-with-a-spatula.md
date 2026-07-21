---
name: flip-food-with-a-spatula
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
objects: [spatula, pan, food]
affordances: [grasp, slide, lift, rotate, place]
workspace: kitchen
safety: {hot_surfaces: true, sharp_objects: false, fragile: [], human_proximity: slow}
---

## Goal

A piece of food is turned over in a pan using a spatula while keeping it intact and inside the pan.

## Preconditions

- The pan is stable on the burner or counter, with enough open surface for the food to land.
- A spatula thin enough for the food edge is available.
- The food has cooked enough on the first side to release or partially release.

## Steps

1. **Stabilize the pan.** Hold or brace the pan handle so the cooking surface does not slide. → *Expect:* the pan resists light spatula pressure.
2. **Choose the entry edge.** Identify the thinnest or loosest food edge and approach from a low angle. → *Expect:* the spatula tip can touch under the edge without pushing the food away.
3. **Slide under.** Push the spatula forward with shallow pressure, keeping the blade nearly parallel to the pan. → *Expect:* at least half the food is supported on the spatula.
4. **Release stuck spots.** Wiggle or scrape with short strokes rather than prying upward. → *Expect:* the food separates without tearing.
5. **Lift low.** Raise the spatula only a few centimeters above the pan. → *Expect:* the food stays balanced and close to the landing surface.
6. **Commit the flip.** Rotate the wrist in one smooth motion toward the empty landing area. → *Expect:* the food turns over once without pausing on edge.
7. **Catch and settle.** Lower the spatula as the food lands, then slide it out from underneath. → *Expect:* the food rests flat on its second side.
8. **Correct placement.** [BRANCH: centered | near rim] Leave it if centered; nudge it inward if near the rim. → *Expect:* the food is fully inside the pan and away from the edge.

## Decision points

- Food tears during entry → wait longer for browning or use a wider spatula.
- Food is too large for one spatula → use a second tool for support.
- Oil splatters during lift → lower the height and reduce pan heat if needed.

## Failure modes & recovery

- **F1 Spatula misses center:** food droops off one side → set it down, re-enter deeper, and lift again.
- **F2 Food sticks:** underside resists sliding → scrape gently along the pan surface and delay the flip.
- **F3 Flip overshoots:** food lands near the rim → nudge inward before continuing cooking.
- **F4 Breakage:** food splits during rotation → turn pieces separately and reduce force on future flips.

## Verification

The food is turned onto its opposite side, remains in the pan, and is stable enough to continue cooking without immediate correction.

## Variations

- `pancake`: wait for set edges and surface bubbles before the first flip.
- `egg`: use a flexible spatula and a very low lift to prevent yolk rupture.
- `cutlet`: support the heavy end first and flip toward open pan space.

## Safety & privacy

Medium risk when flipping over hot oil or a hot pan. Keep the lift low, avoid splashing toward the body, and slow when another hand or utensil enters the pan area.
