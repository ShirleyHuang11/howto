---
name: clean-a-refrigerator
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: basic
est_time: 45min
risk: low
prerequisites: [daily/food/store-leftovers]
status: draft
last_verified: 2026-07-20
---

## Goal

The refrigerator is emptied, purged of expired stowaways, wiped clean shelf by shelf, and restocked in the zone layout that keeps food safe, with the cold chain respected throughout.

## Preconditions

- A free 45 minutes, counter space to stage the contents, and a cool bag or box for the genuinely perishable during the deep phase.
- Warm water with dish soap or an all-purpose cleaner, cloths, and a bin bag standing open (`daily/home/sort-recycling` for the containers you will liberate).
- Best scheduled the day *before* grocery day, when the fridge is at its emptiest (`daily/errands/buy-groceries` synergy).

## Steps

1. **Empty one zone at a time, triaging as you go.** Everything out to the counter in its shelf-groups; meat, dairy, and delicate perishables into the cool bag. Each item passes the gate: expired, unrecognizable, or three-olives-left → bin or compost; keeper → its counter group. → *Expect:* an emptying fridge and an honest bin bag; the `daily/food/read-food-labels` date rules (use-by vs best-before) doing the judging.
2. **Remove shelves and drawers that lift out, and wash them at the sink.** Warm soapy water; glass shelves get five minutes to reach room temperature first, because hot water on cold glass is a cracking risk. → *Expect:* shelves and crisper drawers washed, rinsed, and drying on a towel.
3. **Wipe the interior top-to-bottom.** Walls, fixed shelves, door seals (fold the gasket open gently; crumbs live in its pleats), and the drip channel at the back if visible. Baking-soda water handles odors; nothing harsh, it is a food box. → *Expect:* interior surfaces clean and rinsed of any cleaner taste; the gasket pleats grit-free.
4. **Deal with the drain hole and any ice or puddle.** The small drain at the back wall clogs with crumbs and creates the mystery puddle; a cotton swab or the fridge's little cleaning tool clears it. → *Expect:* drain open, puddle history explained.
5. **Reassemble and restock by zones.** Shelves back dry; then the layout that `embodied/kitchen/store-groceries` teaches: raw meat lowest (drip containment), dairy and eggs mid, ready-to-eat up, vegetables in crispers, condiments in the door, older stock in front of newer. → *Expect:* everything back with a logic a stranger could read, the cool-bag items first.
6. **Finish the outside and the metadata.** Handle and door front wiped (the handle is the kitchen's most-touched surface), the temperature checked at 4 °C or below, and a dated note or phone reminder for the next round in two to three months. → *Expect:* clean touchpoints, verified temperature, next cycle scheduled.

## Decision points

- Freezer: the same recipe at its own session, with the extra rule that a full defrost (for iced-up freezers) needs towels, time, and the food in a genuine cool box (`daily/food/portion-and-freeze-meals` stock survives an hour; be quicker than that).
- Sticky mystery spill fossilized under a drawer: park a warm wet cloth on it for five minutes and it wipes; scraping cold spills scratches liners.
- Smell that survives cleaning: an open box of baking soda takes a week to neutralize a fridge; a persistent smell after that means a missed source (check the drain, the gasket, and the crisper undersides again).

## Failure modes & recovery

- **F1 Perishables sat out too long during an overrunning clean:** the `daily/food/store-leftovers` asymmetric rule decides the cool-bag skippers; next time the cool bag earns its two minutes of setup.
- **F2 Glass shelf cracked:** cold glass met hot water; manufacturers sell replacement shelves by model number, and the wait is a cardboard interim.
- **F3 Everything back but the door will not close flush:** a drawer or shelf is mis-seated on its rails, or a jar stands proud at the back; re-seat rather than slam.
- **F4 The purge triggered guilt-hoarding ("this might still be fine"):** the gate in step 1 is the protocol precisely so the decision is made once, by rule, not five times by mood.

## Verification

The interior is clean including gasket and drain, nothing expired went back in, zones match the layout, the temperature reads at or below 4 °C, the handle is clean, and the next session has a date.

## Variations

- Shared household fridges: label-and-date culture (`daily/food/portion-and-freeze-meals` step 4) plus this recipe quarterly is the difference between a fridge and a dispute.
- Mini-fridges and office fridges: same recipe in twenty minutes, and the office version is a rota, not a hero's burden.

## Safety & privacy

Low risk: the cold chain during the clean (cool bag), the glass-temperature caution, and food-safe cleaners only. The fridge repays the fussiness in fewer mystery smells and fewer discarded groceries.
