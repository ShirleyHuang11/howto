---
name: sort-laundry-into-lights-and-darks
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [laundry, hamper, garment, towel, pocket, basket]
affordances: [sort, inspect, empty, place, separate]
workspace: laundry-area
safety: {hot_surfaces: false, sharp_objects: true, fragile: [button, zipper], human_proximity: continue}
---

## Goal

Sort dirty laundry into light and dark loads while removing pocket hazards and separating items that need special handling.

## Preconditions

- Dirty laundry is gathered in one area.
- At least two baskets, piles, or machine loads can be separated.
- Care labels can be checked for unusual items.

## Steps

1. **Create sorting spaces.** Designate one area for lights and one for darks. → *Expect:* two clearly separate piles or baskets exist.
2. **Inspect each item.** Pick up one garment at a time and check color, fabric, and care label if uncertain. → *Expect:* the item's load category is known.
3. **Empty pockets.** Remove tissues, coins, keys, pens, and sharp objects. → *Expect:* pockets are flat and no hard items remain.
4. **Place lights together.** Put white, pale, and light-gray washable items in the light pile. → *Expect:* light pile contains no saturated dark dyes.
5. **Place darks together.** Put black, navy, red, denim, and strong colors in the dark pile. → *Expect:* dark pile contains items likely to bleed or shed dye.
6. **Separate special items.** Set delicates, wool, dry-clean-only, heavily soiled, or new bright items aside. → *Expect:* special-care items are not mixed into standard loads.
7. **Check pile size.** Keep each load loose enough for water and agitation. → *Expect:* no load is packed tight before washing.

## Decision points

- New red, dark denim, or bright garment → wash with darks or separately.
- Care label says hand wash or dry clean → set aside.
- Item is wet or mildewed → wash promptly and separate from dry laundry if needed.
- Biohazard or chemical contamination exists → follow household or facility safety procedure.

## Failure modes & recovery

- **F1 Hidden tissue:** detect paper in pocket or lint-covered item → remove tissue and shake item before washing.
- **F2 Color uncertainty:** detect medium or patterned item → sort by darkest dominant dye or wash separately.
- **F3 Sharp object:** detect pin, key, or tool → remove it and check for fabric damage.
- **F4 Overfilled load:** detect compacted pile or washer drum packed full → split into smaller loads.

## Verification

Laundry is divided into light, dark, and special-care groups, with pockets emptied and no sharp or hard objects left in standard wash piles.

## Variations

- Cold-wash routine: some households combine more colors, but new dark or red items still need caution.
- Shared laundry room: keep personal items contained and do not leave pockets contents on machines.
- Towels and linens: sort separately if lint transfer or washing temperature differs.

## Safety & privacy

Low risk, with possible sharp pocket items and private belongings. Handle personal items discreetly and return valuables or documents to the owner.
