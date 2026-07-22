---
name: set-up-a-slow-cooker
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: basic
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Load and run a slow cooker so food cooks evenly, reaches a safe finish temperature, and stays safe until serving.

## Preconditions

- The slow cooker, insert, lid, cord, and outlet are clean, dry, and undamaged.
- Ingredients are thawed unless the appliance manual specifically allows frozen items.
- You have a recipe with cooking time, liquid amount, and safe internal temperature for any meat.
- A food thermometer is available for checking doneness.

## Steps

1. **Place the cooker safely.** Set it on a flat, heat-safe counter with the cord away from the edge. → *Expect:* the cooker is stable and not crowded by flammable items.
2. **Prep ingredients evenly.** Cut dense vegetables and meat into similar sizes so they cook at a predictable rate. → *Expect:* pieces are ready to layer without large frozen centers.
3. **Layer dense foods first.** Put potatoes, carrots, onions, or other firm vegetables on the bottom near the heat. → *Expect:* dense ingredients sit closest to the insert base.
4. **Add protein and softer items.** Place meat or beans above dense vegetables, with delicate vegetables saved for later if the recipe says so. → *Expect:* ingredients are arranged by cooking speed.
5. **Add the right liquid level.** Pour in the recipe's liquid, usually enough to cover the bottom and partially surround ingredients. → *Expect:* the cooker is not dry and not filled past the max line.
6. **Choose low or high.** [BRANCH: low | high] use low for longer gentle cooking or high for a shorter cook when the recipe allows it. → *Expect:* the setting matches the recipe time.
7. **Keep the lid closed.** Avoid lifting the lid unless adding timed ingredients or checking near the end. → *Expect:* steam stays inside and cooking time remains predictable.
8. **Check finish temperature.** Use a thermometer in the thickest part of meat or the center of the dish. → *Expect:* food reaches the recipe's safe temperature before serving.
9. **Use keep-warm correctly.** Switch to keep-warm after food is fully cooked, not as a cooking setting. → *Expect:* hot food stays above 140 F until served.
10. **Store leftovers promptly.** Portion leftovers into shallow containers within 2 hours. → *Expect:* food cools quickly in the refrigerator.

## Decision points

- The recipe includes poultry → cook until the thickest piece reaches 165 F.
- The cooker is less than half full or more than two-thirds full → adjust batch size for even cooking.
- Food is not at temperature at the planned time → continue cooking with the lid on and recheck.
- Power goes out during cooking → discard perishable food if it sat in the danger zone for an unsafe period.

## Failure modes & recovery

- **F1 Food undercooked:** detect by low thermometer reading or hard dense vegetables → recover by continuing on high with the lid on and rechecking.
- **F2 Dry insert:** detect by scorching smell or no visible liquid early in cooking → recover by adding hot liquid if the food is still safe.
- **F3 Overfilled cooker:** detect by bubbling near the lid or food above the max line → recover by removing some ingredients to another pot.
- **F4 Unsafe holding:** detect by food below 140 F on keep-warm → recover by reheating to a safe temperature or discarding if time is uncertain.

## Verification

The slow cooker is stable, the lid has stayed closed during cooking, and the finished food has reached the safe internal temperature for its ingredients.

## Variations

- Beans: boil kidney beans separately as directed before slow cooking because some beans need high heat for safety.
- Dairy sauces: add milk, cream, or cheese near the end to reduce curdling.
- Delicate vegetables: add peas, spinach, or herbs in the final part of cooking.

## Safety & privacy

Medium risk because unsafe temperatures can cause foodborne illness. Thaw ingredients safely, verify meat with a thermometer, keep hot food above 140 F, refrigerate leftovers promptly, and do not use a cracked insert or damaged cord.
