---
name: load-items-onto-a-checkout-belt
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [checkout-belt, groceries, divider, cart, basket, cashier]
affordances: [lift, place, sort, slide, wait, release]
workspace: store-checkout
safety: {hot_surfaces: false, sharp_objects: false, fragile: [eggs, glass-jar], human_proximity: slow}
---

## Goal

Place items from a cart or basket onto a checkout belt so they can be scanned without damage, mixing, or delay.

## Preconditions

- The checkout lane is open and the belt belongs to the selected cashier or station.
- Items are contained in a cart, basket, or bag within reach.
- Fragile or leak-prone items are identifiable.

## Steps

1. **Wait for space on the belt.** Stand behind the customer ahead until their items are separated. → *Expect:* a clear belt section is available.
2. **Place a divider if needed.** Set the divider between the previous order and your first item. → *Expect:* the cashier can see where your order begins.
3. **Load heavy items first.** Put cans, boxes, and dense items flat on the belt. → *Expect:* heavy items are stable and not resting on fragile goods.
4. **Group similar items.** Place chilled, produce, boxed, and cleaning items in loose groups. → *Expect:* items are easy to scan and bag together.
5. **Protect fragile items.** Put eggs, bread, chips, glass, and soft produce near the end or in a clear safe spot. → *Expect:* fragile items are not under heavier items.
6. **Keep hazards upright.** Place liquids, powders, and chemical containers upright with caps visible. → *Expect:* no leaking or rolling occurs.
7. **Move the cart forward.** Advance only when the customer ahead clears and the cashier is ready. → *Expect:* you remain with your order without crowding.
8. **Place a final divider.** If another customer is waiting, mark the end of your items. → *Expect:* the next order stays separate.

## Decision points

- Belt is wet or dirty → ask for it to be wiped or keep leak-sensitive items in the cart until safe.
- Item is too heavy for the belt → leave it in the cart and tell the cashier.
- Barcode or produce sticker is hidden → turn the item so it can be found without crushing it.
- Checkout is self-service → load a few items at a time according to bagging area limits.

## Failure modes & recovery

- **F1 Item rolls:** detect bottle or can moving → rotate it lengthwise or place it against a stable item.
- **F2 Orders mix:** detect divider missing or items touching another order → stop and separate before scanning.
- **F3 Fragile item crushed:** detect bread, eggs, or produce under weight → move it to the end or hand it to cashier.
- **F4 Leak appears:** detect wet belt or dripping package → isolate the item and ask staff for cleanup.

## Verification

All intended purchase items are on the belt or declared as staying in the cart, separated from adjacent orders, with fragile and leaking items protected.

## Variations

- Self-checkout: scan directly from cart or basket and obey the bagging scale prompts.
- Bulk store: leave oversized items in the cart with barcodes facing the cashier.
- Reusable bags: keep empty bags separate until the cashier or bagger needs them.

## Safety & privacy

Low risk from lifting, crowding, and spills. Slow around other shoppers, avoid placing private pharmacy or identity items face-up longer than needed, and ask before reaching across another person.
