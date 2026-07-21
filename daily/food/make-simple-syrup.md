---
name: make-simple-syrup
domain: daily
subdomain: food
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Sugar and water are dissolved into a clear simple syrup for drinks, desserts, or cocktails.

## Preconditions

- Granulated sugar, potable water, saucepan or heatproof jar, spoon, and clean bottle are available.
- The storage bottle has a lid and can be refrigerated.
- The intended ratio is known before measuring.

## Steps

1. **Choose the ratio.** [BRANCH: 1:1 by volume for standard syrup | 2:1 sugar to water for rich cocktail syrup] → *Expect:* measured sugar and water match the drink recipe.
2. **Combine sugar and water.** Add both to a small saucepan or heatproof jar. → *Expect:* sugar is fully wetted with no dry mound.
3. **Warm gently.** Heat over low to medium heat, or add hot water to the jar and stir. → *Expect:* liquid warms without a hard boil.
4. **Dissolve, not reduce.** Stir until the liquid turns clear. → *Expect:* no sugar grains scrape under the spoon.
5. **Stop heating.** Remove from heat as soon as dissolved. → *Expect:* volume has not noticeably boiled away.
6. **Cool uncovered.** Let syrup cool until no steam rises. → *Expect:* bottle will not trap pressure or condensation.
7. **Bottle cleanly.** Pour into a clean labeled bottle. → *Expect:* syrup is clear and the lid closes tightly.
8. **Refrigerate.** Store 1:1 syrup chilled and use within about 1 month. → *Expect:* bottle sits cold and dated.

## Decision points

- Cocktail recipe gives ounces → use equal volumes for 1:1 unless it specifies rich syrup.
- Sugar will not dissolve → warm slightly and stir longer instead of boiling hard.
- Syrup crystallizes → rewarm with a spoonful of water and stir until clear.
- Flavoring is wanted → steep herbs, citrus peel, or spice while warm, then strain.
- Shelf life matters → make rich syrup or smaller batches.

## Failure modes & recovery

- **F1 Grainy syrup:** detect crystals on the spoon or bottle bottom; recover by reheating with a little water.
- **F2 Caramel taste:** detect amber color or cooked sugar smell; recover by remaking at lower heat.
- **F3 Mold:** detect cloudiness, fizz, or surface spots; recover by discarding the syrup and sanitizing the bottle.
- **F4 Wrong sweetness:** detect drinks tasting weak or cloying; recover by labeling the ratio and adjusting recipe amounts.
- **F5 Sticky spill:** detect syrup on counter or bottle threads; recover by wiping with hot water before it dries.

## Verification

The syrup is clear, fully liquid, labeled with its ratio, and has no visible sugar crystals after cooling.

## Variations

- Cold-process bar syrup: shake superfine sugar with water until clear.
- Demerara syrup: use raw sugar for a deeper flavor in spirit-forward cocktails.
- Honey syrup: mix 2 parts honey with 1 part warm water for easier pouring.

## Safety & privacy

Low risk from hot liquid and glass. Do not cap steaming syrup tightly, and refrigerate to limit spoilage.
