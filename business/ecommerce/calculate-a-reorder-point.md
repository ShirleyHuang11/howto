---
name: calculate-a-reorder-point
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You calculate the inventory level at which a product should be reordered so stock arrives before expected demand consumes the remaining units.

## Preconditions

- Recent daily or weekly sales history for the SKU.
- Supplier lead time, including production, transit, receiving, and quality check.
- Current safety stock policy or enough data to estimate buffer stock.

## Steps

1. **Choose the SKU and unit of measure.** Confirm whether the calculation is per each, case, bundle, or variant. → *Expect:* one unambiguous SKU and inventory unit.
2. **Calculate average daily demand.** Use a representative sales period and exclude documented stockout days, launch spikes, or one-off promotions unless they will repeat. → *Expect:* an average units-sold-per-day figure.
3. **Determine realistic lead time.** Add supplier processing, production, shipping, customs, receiving, and inspection days. → *Expect:* a lead-time estimate in days.
4. **Set safety stock.** Use an existing buffer or calculate it from demand variability and lead-time uncertainty. → *Expect:* a safety stock quantity in the same unit as the SKU.
5. **Compute the reorder point.** Multiply average daily demand by lead time, then add safety stock. → *Expect:* a reorder point: `(daily demand x lead time) + safety stock`.
6. **Compare to current inventory.** Include on-hand, committed, inbound, and backordered units according to the inventory system's rules. → *Expect:* current available inventory is either above or at/below reorder point.
7. **Create an alert or purchase draft.** Configure an inventory alert, replenishment task, or draft purchase order at the calculated threshold. → *Expect:* the system will prompt reorder before stock drops too low.
8. **Review after each cycle.** Compare forecasted demand and lead time to actual results. → *Expect:* the reorder point is adjusted when demand or supplier reliability changes.

## Decision points

- Demand is seasonal → calculate using comparable seasonal periods, not the recent average alone.
- Supplier lead time is unstable → increase safety stock or use a higher percentile lead time.
- Product is perishable or trend-sensitive → cap reorder quantity even if the reorder point says to buy soon.

## Failure modes & recovery

- **F1 Stockout days lower the demand estimate:** detect zero sales when inventory was unavailable → exclude stockout days or estimate lost sales.
- **F2 Lead time is too optimistic:** detect late arrivals against the planned date → update lead time with actual supplier performance.
- **F3 Unit mismatch:** detect reorder point in cases but inventory counted in eaches → convert all quantities to one unit.
- **F4 Promotions distort demand:** detect spikes tied to a sale → calculate a normal baseline and a separate promo plan.

## Verification

The SKU has a documented reorder point equal to average daily demand times lead time plus safety stock, and an alert or purchasing trigger is set at that inventory level.

## Variations

- Marketplace fulfillment: include transfer and receiving time into the marketplace warehouse.
- Made-to-order products: reorder point may apply to raw materials instead of finished goods.
- Subscription products: use committed subscription demand separately from one-time sales.

## Safety & privacy

Medium risk because reorder decisions can tie up cash or cause stockouts. Use accurate sales and inventory data, document assumptions, and require approval before placing large purchase orders.
