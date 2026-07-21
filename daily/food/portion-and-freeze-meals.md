---
name: portion-and-freeze-meals
domain: daily
subdomain: food
locale: [generic]
interface: physical
difficulty: basic
est_time: 30min
risk: medium
prerequisites: [daily/food/store-leftovers]
status: draft
last_verified: 2026-07-20
---

## Goal

A batch-cooked meal is divided into labeled single portions and frozen so that future weeknights have a freezer full of real dinners instead of one giant mystery block.

## Preconditions

- A large cooked batch (stew, curry, soup, sauce, chili, cooked grains) inside its safe window (`daily/food/store-leftovers` step 1's two-hour rule governs here too).
- Freezer-safe containers or bags in meal sizes, a marker and tape or freezer labels, and freezer space checked before you start ladling.

## Steps

1. **Cool the batch fast in shallow layers.** Divide the pot across shallow containers or a sheet pan so the heat escapes quickly; steaming-hot food straight into the freezer taxes it and warms the neighbors. → *Expect:* food dropped to warm-not-hot within the safe window.
2. **Portion by how you actually eat.** One-person meals freeze in one-person sizes; family dinners in family sizes. A frozen four-portion block serves one person exactly as badly every time. → *Expect:* containers filled to realistic meal sizes, with sauce distributed evenly across them.
3. **Leave expansion headroom and exclude air.** Rigid containers: a couple of centimeters of headspace (liquids expand frozen). Bags: fill, press flat, squeeze the air out, seal. Flat bags freeze fast, stack like books, and thaw in minutes (`daily/food/defrost-frozen-food`'s water bath loves them). → *Expect:* headroom in boxes, flat air-free bags.
4. **Label everything, now, with contents and date.** The marker step feels skippable tonight and is the entire difference between a freezer and an archaeology site in eight weeks. → *Expect:* every container answering "what and when" at a glance.
5. **Freeze smart.** Flat bags on a tray until solid (then file them vertically), boxes with air gaps around them for the first hours, nothing warm buried in the middle of the existing stock. → *Expect:* everything frozen solid within a day, stored findably.
6. **Run the rotation.** New stock behind or below old (`embodied/kitchen/store-groceries`'s first-in-first-out), and a use-by horizon of roughly 2 to 3 months for best quality (safe longer, but quality fades). An inventory list on the freezer door repays its thirty seconds weekly. → *Expect:* oldest meals surfacing first; the list matching reality.

## Decision points

- What freezes well: stews, curries, soups, sauces, chili, cooked beans and grains, bakes. What disappoints: potato chunks (grainy), pasta cooked to al dente (softens; undercook it if freezing), dairy-heavy sauces (can split; stir hard on reheat), raw salad anything.
- Freeze before or after the week's fridge portion: split the batch on cooking day (some to fridge for this week per `store-leftovers`, rest frozen immediately) rather than freezing week-old leftovers at their quality floor.
- Reheating destination: fridge-thaw overnight then normal reheat is best; bag-in-water-bath then pot works same-day; microwave-from-frozen works with the stir-and-stand discipline of `daily/food/use-a-microwave`.

## Failure modes & recovery

- **F1 Unlabeled UFOs (unidentified frozen objects):** thaw one as soup roulette, and label the survivors today; the rule exists because everyone breaks it exactly once per lesson.
- **F2 Freezer burn (dry, pale patches):** air was left in the package; trim affected spots, eat soon, and squeeze bags flatter next time.
- **F3 One giant block frozen solid:** portion discipline failed at step 2. Thaw the whole thing in the fridge, repackage into portions, refreeze what you have not reheated (cooked food thawed in the fridge tolerates one such round with quality loss).
- **F4 Cracked container or burst bag:** overfilled headroom or brittle cheap plastic; transfer the contents, and retire that container type from freezer duty.

## Verification

Every portion is meal-sized, labeled with contents and date, frozen flat or with headroom, filed with the oldest in front, and the first weeknight test (grab, thaw, reheat, eat) took under fifteen active minutes.

## Variations

- Ingredient-level freezing runs on the same rules: smoothie fruit bags (`daily/food/make-a-smoothie`), chopped onion tubs, portioned raw proteins frozen flat in marinades that season as they thaw.
- Ice-cube-tray freezing suits concentrates: stock, herb-in-oil, tomato paste, lemon juice; cubes decant into a labeled bag.

## Safety & privacy

Medium risk shares `store-leftovers`' physics: the fast-cool window at the front, honest labeling in the middle, and proper thawing (`defrost-frozen-food`) at the exit. The freezer forgives almost everything except warm food, air, and anonymity.
