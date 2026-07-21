---
name: gather-items-into-a-basket
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [basket, household-items]
affordances: [scan, grasp, carry, place, balance]
workspace: household-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [household-items], human_proximity: continue}
---

## Goal

Multiple household items are collected into a basket, placed rather than tossed, balanced for carrying, and moved without spills.

## Preconditions

- A basket or bin is available and structurally sound.
- Target items are known or visually identifiable.
- Items are safe to touch and small enough for the basket.
- The route between items has walkable clearance.

## Steps

1. **Inspect the basket.** Check handles, bottom, and interior for damage or contaminants. → *Expect:* basket can hold the planned load.
2. **Plan pickup order.** Scan the room and choose nearby items first, with heavy or flat items before fragile ones. → *Expect:* a route and placement order are known.
3. **Place the basket near the first item.** Set it on the floor, table, or hip-height surface within reach. → *Expect:* basket is stable and open side faces up.
4. **Pick up the first item.** Grip the item securely using its handle, sides, or underside. → *Expect:* item is controlled without dragging or scraping.
5. **Place, not toss.** Lower the item into the basket until it contacts the bottom or another stable item. → *Expect:* item remains where placed and basket does not tip.
6. **Repeat with balance checks.** Add items around the center, distributing weight left and right. → *Expect:* basket remains level after each placement.
7. **Protect fragile items.** Put fragile or soft items on top or in a separated area. [BRANCH: fragile present | no fragile] cushion and isolate fragile items; continue normal loading otherwise. → *Expect:* fragile items are not under heavy load.
8. **Stop before overfilling.** Leave handle access and line of sight to the basket rim. → *Expect:* no item rises above the rim in a way that can fall during carry.
9. **Lift and carry the basket.** Use both handles or support the bottom, then move slowly with the load close. → *Expect:* basket stays level and items do not shift out.

## Decision points

- Item is heavy → place it first and near the basket center, or carry separately.
- Item is dirty, wet, sharp, or leaking → use a liner, gloves, or exclude it.
- Basket becomes unbalanced → set it down and redistribute contents.
- Route includes stairs or tight spaces → reduce load before carrying.
- Target list is incomplete → gather only clearly identified items.

## Failure modes & recovery

- **F1 Basket tips:** detect rim drop or handle twist → set it down, remove top items, and rebalance.
- **F2 Item falls out:** detect item crossing rim during movement → stop, retrieve it, and lower stack height.
- **F3 Fragile item is compressed:** detect bending, cracking, or pressure → remove it and place it on top or carry separately.
- **F4 Handle strain appears:** detect creak, tear, or flex → support the bottom and reduce load.
- **F5 Pickup route becomes blocked:** detect obstacle or person in path → pause, reroute, or move the basket closer.

## Verification

All intended safe items are inside the basket, the load is balanced, handles or bottom are supported, and no item falls during a short carry test.

## Variations

- `laundry-basket`: place soft items freely but keep small hard objects out of fabric folds.
- `cleaning-caddy`: keep bottles upright and separate cloths from chemicals.
- `toy-bin`: put large flat toys first and small loose pieces last.
- `fragile-collection`: carry fewer items and use padding between hard surfaces.

## Safety & privacy

Low risk. Do not gather private documents, medications, sharp objects, or unknown liquids unless the task explicitly requires them. Balance matters more than speed.
