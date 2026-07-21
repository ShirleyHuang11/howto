---
name: grease-a-baking-pan
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [baking-pan, butter, oil, cooking-spray, flour, parchment-paper, paper-towel]
affordances: [grasp, spread, spray, dust, shake, line, press]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [glass-baking-dish], human_proximity: continue}
---

## Goal

Coat a baking pan so batter or dough releases cleanly after baking, with corners, edges, and optional parchment handled correctly.

## Preconditions

- Clean dry baking pan matched to the recipe size.
- Butter, neutral oil, shortening, or cooking spray.
- Flour, cocoa, or parchment if the recipe calls for extra release.
- Counter space for turning and tapping the pan.

## Steps

1. **Read the recipe instruction.** Check whether it says grease, grease and flour, line with parchment, or leave ungreased. → *Expect:* the pan treatment matches the recipe.
2. **Inspect the pan.** Remove crumbs, water, labels, or old oil. → *Expect:* the inside surface is clean and dry.
3. **Choose the fat.** [BRANCH: butter | oil | spray] use softened butter for flavor, oil for neutral coating, or spray for speed. → *Expect:* the fat can cover the pan in a thin film.
4. **Coat the bottom.** Rub or spray across the flat base from center to corners. → *Expect:* the bottom has a continuous shine with no dry patches.
5. **Coat corners and edges.** Push fat into seams, corners, and up the sides to the expected batter height. → *Expect:* corner lines look glossy, not pale.
6. **Remove puddles.** Wipe extra oil or thick butter lumps with a paper towel. → *Expect:* the coating is thin and even.
7. **Dust with flour if needed.** Add a spoonful of flour, tilt and tap until it clings to all greased surfaces. → *Expect:* a light powder film covers bottom and sides.
8. **Tap out excess.** Turn the pan over the sink or trash and tap gently. → *Expect:* loose flour falls out and no thick patches remain.
9. **Add parchment option.** For cakes or bars, press parchment onto the greased bottom, leaving handles if useful. → *Expect:* parchment lies flat and sticks lightly.
10. **Final check before batter.** Look along the corners and side walls. → *Expect:* every surface the batter touches is greased, lined, or deliberately bare.

## Decision points

- If baking chocolate cake → use cocoa instead of flour to avoid white dust on dark cake.
- If using silicone pans → grease only if the recipe or pan history suggests sticking.
- If batter is very delicate → parchment on the bottom gives a cleaner release than grease alone.
- If making angel food cake → follow the recipe if it says ungreased, because climbing the pan may be required.

## Failure modes & recovery

- **F1 Dry corner:** detect matte metal or glass in a seam → rub fat into the corner before adding batter.
- **F2 Flour clumps:** detect white lumps in butter streaks → tap out and wipe lightly, then dust again.
- **F3 Parchment curls:** detect lifted edges → dab grease under the paper and press it flat.
- **F4 Over-sprayed pan:** detect oil pooling at the bottom → wipe to a thin film so batter does not fry at the edges.

## Verification

The pan has a continuous thin release layer on all recipe-specified surfaces, with optional flour or parchment evenly applied and no loose piles.

## Variations

- Bundt pan: use a brush or paper towel to reach every groove.
- Muffin tin: grease each cup rim as well as the cup interior.
- Bread loaf: parchment sling along the long sides makes lifting easier.

## Safety & privacy

Low risk. Keep spray away from open flames, keep glass pans away from counter edges, and wash oily hands before handling knives, hot pans, or appliance controls.
