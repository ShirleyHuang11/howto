---
name: make-nachos
domain: daily
subdomain: food
locale: [generic]
interface: physical
difficulty: basic
est_time: 15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Nachos come out crisp, evenly cheesy, and topped in the right order so hot toppings stay hot and cold toppings stay fresh.

## Preconditions

- Tortilla chips, melting cheese, and desired toppings.
- Sheet pan, parchment or foil, oven, and oven mitts.
- Meat, beans, or vegetables are cooked before assembly.

## Steps

1. **Preheat the oven.** Set it to 400 F or 205 C and line a sheet pan. → *Expect:* the oven is hot before chips go in.
2. **Sort toppings by temperature.** [BRANCH: hot toppings like beans, meat, peppers | cold toppings like salsa, crema, avocado, cilantro] → *Expect:* cold toppings are held back.
3. **Spread one chip layer.** Arrange chips in a shallow layer instead of a tall pile. → *Expect:* most chips touch the pan and remain visible.
4. **Cheese every chip.** Scatter grated cheese over the layer, reaching edges and corners. → *Expect:* each cluster has visible cheese.
5. **Add hot toppings lightly.** Spoon warm beans or meat in small dots, then add a little more cheese to glue them down. → *Expect:* toppings are distributed without burying the chips.
6. **Bake, do not microwave.** Bake 5 to 8 minutes until cheese melts and edges toast. → *Expect:* cheese bubbles and chips stay crisp.
7. **Finish with cold toppings.** Add salsa, sour cream, avocado, herbs, and lime after baking. → *Expect:* cold toppings look fresh and do not soak the whole pan.
8. **Serve immediately.** Put the pan on a trivet and eat while cheese is stretchy. → *Expect:* chips lift with toppings attached.

## Decision points

- Feeding a crowd → make two sheet pans instead of one overloaded pan.
- Using liquid salsa → serve it on the side or spoon only small amounts.
- Cheese is not melting → switch to grated Monterey Jack, cheddar, Oaxaca, or a blend.

## Failure modes & recovery

- **F1 Soggy center:** detect limp chips under wet toppings, recover by using less salsa and baking in a single layer.
- **F2 Bare chips:** detect chips with no cheese, recover by adding a second cheese sprinkle before baking.
- **F3 Burned edges:** detect dark chip tips, recover by lowering oven to 375 F and pulling earlier.
- **F4 Cold beans:** detect cool spoonfuls after baking, recover by warming beans before assembly.

## Verification

At least five random chips across the pan have melted cheese, and the center chips are still crisp when lifted.

## Variations

- Broiler finish: broil only 30 to 60 seconds and watch constantly.
- Skillet nachos: use a cast-iron skillet but still keep the layer shallow.
- Vegan: use hot beans as the anchor and add cold avocado after baking.

## Safety & privacy

Low risk from hot pans and molten cheese. Use oven mitts, keep the sheet pan stable, and warn eaters that toppings can be hotter than chips.
