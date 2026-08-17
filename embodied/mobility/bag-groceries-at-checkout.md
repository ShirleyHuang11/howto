---
name: bag-groceries-at-checkout
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [groceries, bags, bagging-area, cans, produce, eggs, bread]
affordances: [grasp, classify, place, support, lift, balance]
workspace: checkout bagging area
safety: {hot_surfaces: false, sharp_objects: false, fragile: [eggs, bread, glass-jars, produce], human_proximity: slow}
---

## Goal

Groceries are packed into bags with heavy items low, fragile items protected, and each bag liftable.

## Preconditions

- Items have been scanned or cleared for bagging.
- Clean bags are open and within reach.
- Bagging area is stable and not blocking the cashier or other customers.

## Steps

1. **Open one bag fully.** Grip opposite bag handles or edges and spread them apart on the bagging surface. → *Expect:* the bag mouth stays open and the base is flat.
2. **Place heavy rigid items first.** Put cans, cartons, and jars upright at the bag bottom with close spacing. → *Expect:* the bag base is weighted evenly and does not tip.
3. **Add medium items around gaps.** Place boxes and firm packages beside the heavy items without crushing soft items. → *Expect:* items support each other and remain below the bag rim.
4. **Reserve fragile items.** Keep eggs, bread, chips, and soft produce out until the top layer. → *Expect:* fragile items remain outside the compression zone.
5. **Place fragile items on top.** Lower them gently with broad support under the package. → *Expect:* fragile items sit above heavier items without deformation.
6. **Check bag weight.** Lift the handles 2-5 cm with steady force, then set down if heavy. → *Expect:* the bag lifts without tearing and weight feels manageable.
7. **Start another bag if needed.** Open a new bag before the current bag bulges or exceeds comfortable weight. → *Expect:* each bag remains upright and not overfilled.
8. **Stage finished bags.** Move completed bags by handles and base support to the cart or pickup area. → *Expect:* bags stand upright and contents do not spill.

## Decision points

- Bag starts tearing → stop loading it and double-bag or redistribute weight.
- Cold or leaking items present → separate from dry paper goods when possible.
- Raw meat present → bag separately to reduce cross-contamination.

## Failure modes & recovery

- **F1 Fragile item crushed:** detect by dented bread, cracked eggs, or bruised produce → remove pressure, repack with fragile items on top, and replace damaged goods if needed.
- **F2 Bag too heavy:** detect by handle strain or difficult lift → split contents into two bags.
- **F3 Item leaks:** detect by liquid or residue inside bag → isolate the item in a separate bag and clean the bagging surface.

## Verification

Each bag can be lifted by its handles without tearing, heavy items are at the bottom, and fragile items are uncrushed at the top or in a separate bag.

## Variations

- Reusable tote: place the tote flat, square the base, and distribute weight toward the center.
- Paper bag: keep tall boxes at the sides to stiffen the bag walls.

## Safety & privacy

Move slowly around other shoppers. Keep raw meat separate from ready-to-eat food and avoid exposing payment receipts unnecessarily.
