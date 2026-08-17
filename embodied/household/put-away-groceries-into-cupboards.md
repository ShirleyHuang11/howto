---
name: put-away-groceries-into-cupboards
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [groceries, cupboard, shelf, bag, can, box]
affordances: [sort, lift, open, place, stack, close]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [glass-jar], human_proximity: continue}
---

## Goal

Move shelf-stable groceries from bags into cupboards so items are visible, stable, and grouped with similar goods.

## Preconditions

- Perishable items have been separated for refrigerator or freezer storage.
- Cupboard shelves are clean enough and have available space.
- Damaged or leaking packages can be identified.

## Steps

1. **Sort shelf-stable items.** Separate cans, jars, boxes, snacks, baking items, and cleaning products. → *Expect:* items with different storage needs are in groups.
2. **Check for damage.** Inspect packages for leaks, broken seals, dents, or cracked glass. → *Expect:* unsafe items are set aside.
3. **Open the target cupboard.** Choose the shelf where similar items already live. → *Expect:* the storage location is visible and reachable.
4. **Place heavy items low.** Put cans, jars, and bulk goods on lower or sturdier shelves. → *Expect:* shelves do not bow and items sit flat.
5. **Place fragile items securely.** Set glass jars and bottles away from shelf edges. → *Expect:* fragile containers cannot roll or fall when the door moves.
6. **Group labels outward.** Arrange items so labels or contents can be seen without unstacking. → *Expect:* the next user can identify items quickly.
7. **Keep food separate from chemicals.** Store cleaners away from edible goods. → *Expect:* no chemical container shares a spill path with food.
8. **Close bags and cupboards.** Fold reusable bags, discard empty bags, and close doors. → *Expect:* the floor and counter are clear.

## Decision points

- Item requires refrigeration after opening or immediately → move it to cold storage instead.
- Cupboard is full → consolidate duplicates or ask where overflow belongs.
- Package is leaking or bulging → isolate it and follow disposal guidance.
- Heavy item must go overhead → choose a lower shelf if possible.

## Failure modes & recovery

- **F1 Shelf overload:** detect sagging or crowded stacking → redistribute heavy items to lower shelves.
- **F2 Hidden duplicate:** detect older item behind new item → rotate older item forward.
- **F3 Glass near edge:** detect jar or bottle close to falling → move it inward or to a bin.
- **F4 Chemical mix-up:** detect cleaner beside food → move cleaner to household-supply storage.

## Verification

All shelf-stable groceries are off counters and floors, stored in appropriate cupboards with heavy items stable, fragile items away from edges, and food separated from chemicals.

## Variations

- Pantry bins: place like items in labeled bins instead of loose shelf groups.
- High cupboards: use a step stool only if stable, otherwise choose a reachable shelf.
- Bulk items: decant only into clean labeled containers with dates if that is household practice.

## Safety & privacy

Low risk from lifting, falling jars, and food safety. Do not store allergens or restricted foods where they could be mistaken for general use.
