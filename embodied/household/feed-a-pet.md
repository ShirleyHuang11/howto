---
name: feed-a-pet
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [food-container, measuring-cup, food-bowl, water-bowl, pet-food, dish-soap]
affordances: [grasp, scoop, pour, place, wipe, lid-open, lid-close]
workspace: household
safety: {hot_surfaces: false, sharp_objects: false, fragile: [food-bowl, water-bowl], human_proximity: continue}
---

## Goal

The pet receives a measured portion of the correct food at its scheduled time, with fresh water in a clean bowl beside it.

## Preconditions

- The pet's food, in date, stored in a sealed container (open kibble bags go stale and rancid within weeks).
- A real measuring cup with volume marks. The number one cause of pet obesity is "one scoop" with an unmarked mug that holds double the intended portion.
- Known daily ration for this animal, from the vet or the bag's chart by weight, split across the day's scheduled meals.
- Food and water bowls, plus a washing setup.

## Steps

1. **Confirm it is a scheduled mealtime.** Pets solicit food at any hour; the schedule is the source of truth, not the begging. → *Expect:* current time matches a feeding slot and this meal was not already given by someone else in the household.
2. **Check and refresh the water first.** Dump old water, rinse the bowl, refill with fresh. Do this every visit, not only when the bowl is empty: the slick film on the bowl wall is bacterial growth, not water residue. → *Expect:* water bowl full of clean water, no film on the wall, bowl stable on the floor.
3. **Inspect the food bowl.** [BRANCH: bowl clean and dry → proceed | residue, crust, or grease film → wash with dish soap and hot water, dry, then proceed] → *Expect:* a bowl you would eat from yourself; chin acne in cats and dogs traces to dirty plastic bowls more often than to diet.
4. **Measure the portion.** Level the measuring cup at the exact per-meal amount; do not round up "because they seem hungry". For wet food, portion by can fraction or by weight per the label. → *Expect:* the measured amount matches the per-meal ration; no heaping.
5. **Deliver the bowl.** Place it at the usual feeding spot, away from the litter box for cats. Multi-pet homes: separate feeding stations out of sight of each other, or the fast eater takes both. → *Expect:* each animal at its own bowl; no bowl swapping.
6. **Observe the start of eating.** Watch the first minute. Appetite is the cheapest health signal a keeper has: refusal of a normally loved food is worth noting the same day. → *Expect:* the pet eats with normal enthusiasm.
7. **Close and store the food.** Reseal the container fully; return wet food remainders to the refrigerator, covered, and use within the label window. → *Expect:* container sealed, no food accessible for self-service raids.
8. **Clear uneaten wet food after 30 to 60 minutes.** Kibble may stand until the next meal if the animal grazes; wet food may not. → *Expect:* no spoiling wet food left at the station; bowl washed or soaking.

## Decision points

- Switching food brands or formulas → transition over 7 to 10 days, mixing increasing fractions of the new food; an abrupt switch reliably causes diarrhea.
- Pet on medication given with food → a small portion first with the pill confirmed swallowed, then the rest of the meal.
- Multiple household members feeding → a physical checklist or a moved marker at the feeding station; double-feeding by miscommunication is the most common portion failure.
- Pet skips one meal but drinks and behaves normally → note it and watch the next meal; a cat refusing food beyond about 24 hours is a same-day vet call, not a wait.

## Failure modes & recovery

- **F1 Double feeding:** detected by a second empty bowl or a family member's mention → skip nothing, just log it, and slightly trim the next meal; institute the checklist from the decision point.
- **F2 Gorging then vomiting (dogs):** whole kibble comes back up minutes after a raced meal → switch to a slow-feeder bowl or spread kibble on a flat tray; do not immediately refeed.
- **F3 Ants or pests at the station:** trail visible to the bowl → wash the area, elevate bowls onto a tray with a water moat, and stop leaving kibble standing.
- **F4 Wrong food dispensed (another pet's or spoiled):** detect by smell, label, or the wrong container → take the bowl up immediately, even mid-meal; one interrupted meal is cheaper than a night of illness.

## Verification

The correct animal ate a measured portion at the scheduled time; the water bowl holds fresh clean water; the food container is sealed and stored; no wet food is standing past its window; the feeding area is free of scattered food.

## Variations

- Automatic feeders: they cover the schedule and portion but not water freshness, bowl hygiene, or the eating-check; those remain manual daily tasks.
- Cats vs dogs: cats feed better with multiple small meals and quiet stations; dogs tolerate two larger meals and benefit from slow-feeders.
- Raw or fresh-food diets: treat like human raw meat handling: dedicated utensils, immediate refrigeration, and a hot-soap wash of everything it touched.

## Safety & privacy

Low risk. The real hazards are slow ones: chronic overportioning (obesity is the most common preventable pet condition) and dirty water bowls. Keep human foods toxic to pets (chocolate, grapes, xylitol, onions, alliums) out of reach of the feeding area, and wash hands after handling raw diets.
