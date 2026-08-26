---
name: handle-a-stockout
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You stop overselling a stocked-out item, communicate realistic options to customers, and preserve demand without making false promises.

## Preconditions

- Product SKU, current inventory, open orders, incoming stock ETA, and supplier status.
- Ecommerce admin access to inventory, product status, and customer messages.
- Store policy for backorders, substitutions, cancellations, and refunds.

## Steps

1. **Confirm the stockout.** Check physical stock, reserved units, pending returns, 3PL inventory, and open orders. → *Expect:* a verified shortage quantity by SKU/variant.
2. **Stop new oversells.** Set available inventory to zero, disable oversell, pause affected ads, or mark the variant unavailable. → *Expect:* customers can no longer buy stock you cannot fulfill unless preorder is intentional.
3. **Prioritize open orders.** Sort orders by payment time, service level, fraud status, and promised ship date. → *Expect:* a fulfillment priority list and a count of orders needing action.
4. **Find recovery supply.** Check incoming purchase orders, supplier stock, transfers, substitutions, or returned sellable units. → *Expect:* a realistic earliest fulfillment date or confirmation that none is available.
5. **Choose customer options.** [BRANCH: restock soon | restock uncertain] Offer wait/backorder if ETA is credible; otherwise offer substitution, cancellation, or refund. → *Expect:* a policy-consistent option for every affected order.
6. **Notify affected customers.** Send clear messages with apology, new ETA or options, response deadline, and refund path. → *Expect:* customers know what will happen and how to choose.
7. **Process cancellations or refunds.** ⚠️ *Irreversible:* before refunding or canceling, confirm order number, customer choice, amount, and whether inventory should be released. → *Expect:* canceled/refunded orders are updated correctly.
8. **Capture future demand.** Enable back-in-stock alerts or preorder only with accurate timing and payment disclosure. → *Expect:* interested customers can opt in without being misled.
9. **Fix the cause.** Update reorder points, safety stock, feed sync, promotion rules, or supplier monitoring. → *Expect:* a specific prevention change is recorded.

## Decision points

- Restock ETA is firm and soon → offer delayed shipment with opt-out refund.
- Restock ETA is uncertain → do not take paid backorders unless policy and disclosure support it.
- High-value customers are affected → consider expedited replacement or goodwill credit within policy.
- Marketplace order has ship-deadline penalties → cancel through the correct reason code and document stockout.

## Failure modes & recovery

- **F1 Inventory sync lag:** detect sales continuing after stock is zero → pause channel feed and force an inventory update.
- **F2 Customer misses notice:** detect no response before promised ship date → follow policy, usually refund rather than silently delay.
- **F3 Supplier ETA slips:** detect restock date moving again → proactively update waiting customers and offer cancellation.
- **F4 Wrong cancellation reason:** detect marketplace penalty risk → use the accurate stockout/backorder reason and keep supplier evidence.

## Verification

The stocked-out SKU cannot be newly oversold, every affected order has a documented fulfill/wait/substitute/refund outcome, and the product page or alert mechanism shows accurate availability.

## Variations

- Marketplace channel: cancellation codes and late-shipment metrics may constrain options.
- Subscription box: substitute policy must match subscriber terms.
- Preorder business: keep payment timing, ETA, and cancellation rights visible.

## Safety & privacy

Medium risk because customers have paid or may pay based on availability. Do not hide delays, do not charge for uncertain stock without clear terms, and include only necessary order details in customer messages.
