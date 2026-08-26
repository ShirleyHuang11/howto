---
name: restock-a-low-inventory-item
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You reorder a low-inventory ecommerce item in the right quantity and update systems so sales can continue without overspending or overselling.

## Preconditions

- Current on-hand inventory, sales velocity, open purchase orders, supplier lead time, and cash budget.
- Supplier contact or purchasing portal access.
- Admin access to inventory and purchasing records.

## Steps

1. **Confirm true available inventory.** Check on-hand, reserved, damaged, returned, and incoming quantities. → *Expect:* an accurate available-to-sell number.
2. **Estimate demand through the next lead time.** Use recent sales velocity, seasonality, campaigns, and safety stock. → *Expect:* a forecasted quantity needed before the next restock can arrive.
3. **Calculate reorder quantity.** Subtract available and incoming units from forecasted need, then respect minimum order quantity and cash constraints. → *Expect:* a proposed reorder amount with cost.
4. **Check supplier terms.** Confirm unit cost, lead time, payment terms, shipping cost, minimums, and substitution rules. → *Expect:* a purchase option that matches budget and timing.
5. **Create or approve the purchase order.** ⚠️ *Irreversible:* before sending, confirm SKU, quantity, cost, delivery address, payment terms, and cancellation policy. → *Expect:* supplier receives a correct order or purchase order.
6. **Record incoming inventory.** Add expected quantity, ETA, supplier order number, and receiving location in the inventory system. → *Expect:* staff can see incoming stock without making it prematurely sellable.
7. **Adjust selling controls.** [BRANCH: enough stock until arrival | stockout likely] Keep sales open if stock is sufficient; if stockout is likely, cap quantity, enable preorder with clear date, or pause ads. → *Expect:* customer-facing availability matches realistic supply.
8. **Track shipment and receive stock.** Monitor supplier updates, inspect received units, and reconcile quantity/condition against the purchase order. → *Expect:* inventory is increased only for sellable units actually received.

## Decision points

- Lead time is longer than stock coverage → reduce promotions, enable preorder, or source a temporary supplier.
- Supplier raises cost → recalculate margin before confirming the reorder.
- Minimum order exceeds forecast → negotiate, bundle, or accept only if storage/cash risk is justified.
- Quality issues appeared in prior batches → require inspection or samples before a large reorder.

## Failure modes & recovery

- **F1 Phantom inventory:** detect system stock that cannot be found physically → adjust inventory and investigate reservation or receiving errors before reordering.
- **F2 Supplier delay:** detect missed ETA → update customer promises, pause ads, and consider backup sourcing.
- **F3 Wrong SKU ordered:** detect mismatch in supplier confirmation → request correction immediately before shipment.
- **F4 Cash tied up in excess stock:** detect reorder quantity above realistic demand → reduce order if possible and plan promotions only within margin limits.

## Verification

A supplier order or purchase order is confirmed for the correct SKU and quantity, incoming inventory is recorded with ETA, and customer-facing availability is adjusted to prevent overselling.

## Variations

- Dropship supplier: confirm supplier stock before accepting more orders.
- Handmade goods: production capacity and material availability replace supplier lead time.
- Marketplace FBA/3PL: include inbound shipment creation, carton labels, and receiving delays.

## Safety & privacy

Medium risk because purchase orders commit money and customer promises. Confirm SKU, quantity, cost, payment terms, and delivery address before ordering.
