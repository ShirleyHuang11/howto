---
name: store-groceries
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 20min
risk: low
prerequisites: [daily/errands/buy-groceries]
status: draft
last_verified: 2026-07-20
objects: [grocery-bags, refrigerator, freezer, pantry-shelves, countertop, fruit-bowl]
affordances: [grasp, place, door-open, drawer-open, rotate-stock, carry]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [eggs, glass-jars], human_proximity: continue}
---

## Goal

All grocery bags are unpacked with every item stored in its correct zone — cold chain preserved, older stock rotated forward, fragile items intact, bags cleared.

## Preconditions

- Grocery bags are on the kitchen counter/floor after a shopping trip.
- Fridge, freezer, and pantry have usable space (or space can be made by discarding expired items en route).

## Steps

1. **Triage all bags by temperature class first.** One fast pass: frozen → chilled → everything else, grouped on the counter. Cold items have been warming since checkout — they get priority, not bag order. → *Expect:* three counter groups; frozen and chilled identified within the first minute.
2. **Load the freezer.** Frozen group in first, flat items stacked, new stock *behind or below* existing (older gets used first). → *Expect:* freezer closed with everything frozen inside; nothing left sweating on the counter.
3. **Load the fridge by zone.** Raw meat/fish: bottom shelf (drip containment — never above ready-to-eat). Dairy and eggs: middle/upper shelves, *not* the door (its temperature swings). Vegetables/fruit: crisper drawers. Condiments and juices: the door. Rotate: new milk behind old milk. → *Expect:* each chilled item in its zone; older duplicates in front of newer.
4. **Handle the counter-dwellers correctly.** Bananas, tomatoes, onions, garlic, potatoes, and most whole melons prefer room temperature — bowl or pantry basket, with potatoes/onions dark and *separated from each other* (they spoil each other faster). Bread: breadbox/counter (fridge staling is real), or freezer for the long haul. → *Expect:* no cold-sensitive produce accidentally refrigerated.
5. **Stock the pantry with rotation.** Cans, jars, dry goods to their shelves; new behind old (first-in-first-out); heavy items at waist height or lower, light on top. Fragile jars placed with clearance, not slid against neighbors. → *Expect:* shelves stocked, older stock at the front edge, nothing precarious above head height.
6. **Close the loop.** Fold/store reusable bags at their spot (or by the door for the car); wipe any drips; discard anything expired that surfaced while making space. → *Expect:* empty counters, stored bags, and a fridge/pantry you got slightly *more* organized, not less.

## Decision points

- Eggs: refrigerate in `us` (washed eggs), room temperature acceptable in much of `eu`/`jp` (unwashed) — follow the local supply chain's convention, and keep them in their carton either way (it's their armor and their date label).
- Package too big for its zone (bulk pack) → decant a working portion to the zone and store the remainder sealed in the pantry/freezer — don't wedge.
- Something arrived damaged/leaking (cracked egg, split yogurt) → deal with it now: use, transfer to a container, or discard and note for a refund claim (`shopping/return-a-product`).

## Failure modes & recovery

- **F1 Chilled item discovered hours later in a forgotten bag:** the `daily/store-leftovers` asymmetric rule governs — meat/dairy/seafood warm too long: discard; hardy items: judgment. The step-1 triage exists to make this failure structurally rare.
- **F2 Fridge won't fit everything:** eject the expired and the near-empty ("three olives in brine") first; consolidate duplicates; only then consider what can safely live in the pantry.
- **F3 Jar slipped and broke:** contain glass + contents before continuing (`embodied/carry-and-deliver-an-item` F2 procedure); shoes on until swept.
- **F4 Crushed bread/eggs found at unpacking:** heavy-over-fragile happened at bagging — salvage, and feed the lesson back to `daily/errands/buy-groceries` step 7.

## Verification

Counters and bags are empty, frozen/chilled items reached their zones promptly, meat sits below ready-to-eat food, cold-sensitive produce is out of the fridge, stock is rotated old-in-front, and nothing expired is hiding where the new stock went.

## Variations

- Small-fridge households (`jp`, `eu` compact kitchens): the pantry/counter classification does more work; shopping cadence (smaller, more frequent) is the real storage strategy.
- Meal-prep households: step 5 gains a decant stage — proteins portioned for the freezer in meal units before storing.

## Safety & privacy

Low risk. The two food-safety rules doing the work: cold-first triage and raw-meat-below. Everything else is inventory hygiene that pays out as less waste and faster cooking.
