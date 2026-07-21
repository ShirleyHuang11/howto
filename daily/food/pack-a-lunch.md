---
name: pack-a-lunch
domain: daily
subdomain: food
locale: [generic]
interface: physical
difficulty: basic
est_time: 15min
risk: low
prerequisites: [daily/food/store-leftovers]
status: draft
last_verified: 2026-07-20
---

## Goal

A lunch is packed the night before or morning-of that survives until noon — safe at temperature, not soggy, not leaking in the bag — and actually gets eaten.

## Preconditions

- Food to pack: leftovers (`daily/food/store-leftovers`), sandwich makings (`daily/food/make-a-sandwich`), or assembled components (grain + protein + veg).
- Leak-worthy containers (test: sealed, inverted over the sink, shaken), cutlery, and a bag; an ice pack for anything perishable without midday refrigeration.

## Steps

1. **Choose the menu by noon-condition, not by now-condition.** The question is "what is this like after 4 hours in a bag?" — dressed salads wilt, crispy things soften, yesterday's stew improves. → *Expect:* a menu that answers the noon question well.
2. **Pack wet and dry apart.** Dressing in its own tiny jar; sauce under the protein, not over the grain; crunchy toppings in a fold of foil/small box; the sandwich rules from `daily/food/make-a-sandwich` apply verbatim. → *Expect:* nothing crisp touching anything wet across the containers.
3. **Cool hot food before sealing.** Steam sealed in a box = condensation = sog + a food-safety warm zone. Fridge-cold leftovers pack straight; hot-packed food only in a proper vacuum food jar preheated with boiling water. → *Expect:* boxes sealed at fridge-cold, or a genuinely hot vacuum jar — nothing lukewarm.
4. **Seal and leak-test the risky container.** Lids fully clicked; the inverted-shake over the sink for anything liquid. → *Expect:* dry hands after the shake test.
5. **Assemble the bag with thermal logic.** Perishables + ice pack together (they insulate each other), heavy flat items at the bottom, the banana somewhere it won't be archaeology by noon. Cutlery and a napkin in. → *Expect:* a packed bag where fragile items sit protected and cold sits with cold.
6. **Stage it where you cannot leave without it.** Fridge overnight (bag or boxes) with the bag handle through your keys/by the door ritual — morning-you forgets; night-you plans around that. → *Expect:* a staging arrangement that makes forgetting harder than remembering.
7. **At lunch: temperature-check your judgment.** Perishables that spent the morning warm (no ice pack, hot office) get the `store-leftovers` sniff-and-asymmetry rule before eating. → *Expect:* lunch eaten with the cold chain honored or consciously judged.

## Decision points

- Fridge at destination → the ice pack becomes optional and hot-food rules relax; no fridge and no ice pack → menu shifts to shelf-stable-until-noon (hard cheese, whole fruit, PB-style sandwiches, unopened yogurt is *not* on this list).
- Kids' lunches → smaller portions, zero prep needed at eating time (pre-peel, pre-cut), and the reality check: pack what they eat, not what you wish they ate — returned-uneaten is the failure mode.
- Microwave available at noon → pack reheatable in a microwave-safe box, sauce-in; the crisp-preservation problem disappears and the menu widens.

## Failure modes & recovery

- **F1 Leak in the bag:** the shake test lapsed — triage the bag now (paper towels, rinse), and demote that container to dry-goods duty permanently.
- **F2 Lunch forgotten at home:** the staging ritual failed — today is a bought-lunch day; tonight, move the staging to literally-blocking-the-door.
- **F3 Soggy by noon anyway:** trace which wet-dry boundary failed (usually dressing pre-mixed or hot-sealed steam) and fix that specific boundary next pack.
- **F4 Lunch skipped, still in the bag at 6pm:** perishables with a dead ice pack follow the discard asymmetry; the menu may also be telling you something — pack food you look forward to.

## Verification

At noon: food safe (cold chain intact or menu shelf-stable), textures as designed (crisp is crisp, dressed-at-eating), nothing leaked, cutlery present, and the lunch was eaten rather than surrendered to the office fridge's archaeology layer.

## Variations

- Bento culture (`jp`): compartmentalization is the native solution to the wet-dry problem; cooled-before-boxing is standard practice for rice.
- Meal-prep Sundays: five identical packed lunches trade variety for the decision-free morning — the staging step becomes grab-any-box.

## Safety & privacy

Low risk with one real line: the perishable-warm-hours rule inherited from `daily/food/store-leftovers` — an insulated bag and ice pack buy the morning, not the whole day.
