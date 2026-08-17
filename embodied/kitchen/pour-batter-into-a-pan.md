---
name: pour-batter-into-a-pan
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
objects: [mixing-bowl, batter, baking-pan, spatula, countertop]
affordances: [grasp, tilt, pour, scrape, level, stabilize]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [mixing-bowl, glass-baking-dish], human_proximity: continue}
---

## Goal

Move batter from a mixing bowl into a prepared pan with even distribution and minimal spill.

## Preconditions

- Pan is greased, lined, or otherwise prepared as the recipe requires.
- Batter is mixed and ready to bake.
- Pan sits on a stable counter near the bowl.
- Spatula or scraper is clean and reachable.

## Steps

1. **Set the pan close to the bowl.** Place the pan flat with its long side facing the pour path. → *Expect:* the pan is stable and reachable without stretching.
2. **Grip the bowl securely.** Use two hands or one hand plus support under the base. → *Expect:* the bowl can tilt without slipping.
3. **Start a slow pour.** Tilt the bowl lip over the center of the pan and let batter flow in a thick ribbon. → *Expect:* batter lands inside the pan and begins spreading outward.
4. **Scrape remaining batter.** Hold the bowl tilted and draw the spatula along the inner wall toward the lip. → *Expect:* most batter leaves the bowl without dripping down the outside.
5. **Distribute the batter.** Use the spatula to push batter into corners and level high ridges. → *Expect:* the batter covers the pan bottom at an even depth.
6. **Clean the rim.** Wipe batter from the pan rim or outside wall before moving it. → *Expect:* the pan can be lifted without sticky trails or burnt-on drips.

## Decision points

- Batter is very thin → pour lower and slower to prevent waves over the pan edge.
- Batter is thick → use the spatula as the primary transfer tool after the first pour.
- Pan is already hot → use oven mitts and treat the task as medium risk.

## Failure modes & recovery

- **F1 Batter misses pan:** detect batter on the counter → stop tilting, wipe the spill, and move the bowl lip farther inside the pan boundary.
- **F2 Batter piles in one corner:** detect uneven depth → spread with broad spatula strokes from high to low areas.
- **F3 Bowl slips:** detect grip sliding on a wet bowl → set it down, wipe the outside, and restart with two-hand support.
- **F4 Liner shifts:** detect parchment sliding with the batter → hold one dry corner down while spreading gently.

## Verification

The batter is inside the prepared pan, spread to the required corners or shape, with the pan exterior clean enough to handle.

## Variations

- `muffin-pan`: pour or scoop into each cup to the same fill height.
- `springform-pan`: verify the latch and base are sealed before pouring thin batter.

## Safety & privacy

Low risk unless the pan is hot. Clean spills before opening the oven because batter on the floor or pan exterior can slip, smoke, or burn.
