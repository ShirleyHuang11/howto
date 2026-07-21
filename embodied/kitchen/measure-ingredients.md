---
name: measure-ingredients
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [measuring-cup, liquid-measuring-cup, measuring-spoon, kitchen-scale, ingredient, knife, bowl]
affordances: [scoop, pour, level, tare, read-marking, pack, transfer]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: true, fragile: [glass-measuring-cup, bowl], human_proximity: continue}
---

## Goal

Measure dry, liquid, and weighed ingredients accurately enough for cooking or baking, then transfer them without spills or cross-contamination.

## Preconditions

- Recipe amount and unit are known.
- Dry measuring cups or spoons, liquid cup, and scale are available as needed.
- Ingredients are within date and safe to use.
- Work surface is clean and stable.

## Steps

1. **Identify the measurement type.** [BRANCH: dry volume | liquid volume | weight] match the tool to the recipe unit. → *Expect:* cup, spoon, liquid cup, or scale is selected before opening ingredients.
2. **Stage the receiving bowl.** Place the bowl close to the measuring area. → *Expect:* measured ingredients travel only a short distance.
3. **Use dry cups for dry volume.** Scoop flour, sugar, grains, or similar dry ingredients into the exact cup. → *Expect:* ingredient mounds slightly above the rim.
4. **Level dry ingredients.** Sweep a straight edge across the rim without compacting unless instructed. → *Expect:* the surface is flat and flush with the cup edge.
5. **Pack brown sugar when asked.** Press brown sugar firmly into the cup, then level it. → *Expect:* sugar holds the cup shape when tipped out.
6. **Use liquid cups for liquids.** Set the cup on the counter and pour to the mark. → *Expect:* the meniscus sits at the target line when viewed at eye level.
7. **Use spoons for small amounts.** Fill the spoon over the ingredient container or a scrap bowl, then level if dry. → *Expect:* the spoon is full to the rim, not heaped unless specified.
8. **Weigh for baking precision.** Put the bowl on the scale, press tare, then add ingredient to the target grams. → *Expect:* scale reads the recipe weight with the container excluded.
9. **Transfer cleanly.** Tip the measured ingredient into the mixing bowl and tap gently if needed. → *Expect:* nearly all measured material lands in the bowl.
10. **Separate wet and dry tools.** Keep wet spoons out of dry containers unless the recipe is finished with them. → *Expect:* containers remain dry and unclumped.

## Decision points

- If a baking recipe gives grams → use the scale because flour volume varies by scoop style.
- If the recipe says sifted flour → sift before or after measuring according to the wording.
- If measuring sticky ingredients → oil the spoon lightly before honey, syrup, or molasses.
- If the scale drifts → replace batteries or move it to a flatter surface.

## Failure modes & recovery

- **F1 Compacted flour:** detect dense scoops or heavy batter → spoon flour into the cup next time and level gently.
- **F2 Wrong cup type:** detect liquid filled to a dry cup brim or dry ingredient in a liquid cup → remeasure with the correct tool.
- **F3 Scale includes bowl weight:** detect impossible high reading before adding ingredient → press tare with the empty bowl on the scale.
- **F4 Ingredient contamination:** detect wet crumbs in a dry container → remove affected clumps and use a clean dry spoon.

## Verification

Each ingredient amount matches the recipe unit using the appropriate tool, and measured ingredients are in the bowl without visible spills or contaminated containers.

## Variations

- No scale: fluff flour, spoon into the cup, and level for the closest volume substitute.
- Metric recipes: weigh solids in grams and liquids by milliliters if the recipe provides them.
- Mise en place: measure all ingredients into separate small bowls before cooking starts.

## Safety & privacy

Low risk. Watch glass cups near counter edges, keep knife blades pointed away while leveling, and clean allergen-containing powders or nut ingredients from shared surfaces.
