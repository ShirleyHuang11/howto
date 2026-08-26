---
name: reprice-inventory-dynamically
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: advanced
est_time: 1h-2h
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You adjust product prices using inventory, demand, competitor, and margin signals while enforcing a hard price floor and audit trail.

## Preconditions

- Current inventory, sales velocity, landed cost, margin floor, competitor prices, and demand signals.
- Permission to edit prices or configure a repricing tool.
- A policy for minimum advertised price, fairness, and legal compliance.

## Steps

1. **Define repricing rules.** Set the business goal, such as clearing aging stock, protecting margin, matching market price, or slowing sales of scarce inventory. → *Expect:* a written repricing objective for each SKU group.
2. **Calculate price floors and ceilings.** Include full cost, marketplace fees, shipping, returns allowance, and any brand or legal price limits. → *Expect:* every SKU has a minimum and maximum allowed price.
3. **Segment inventory.** Group SKUs by stock level, age, seasonality, sales velocity, and replacement lead time. → *Expect:* products with similar pricing logic are grouped together.
4. **Gather market signals.** Review competitor all-in prices, buy-box status, conversion rate, ad cost, and cart abandonment. → *Expect:* current demand and competition data for each group.
5. **Choose price changes.** Apply conservative increments, such as lowering slow movers within floor limits or raising scarce fast movers within ceiling limits. → *Expect:* proposed prices that satisfy the rule set.
6. **Preview margin and order impact.** Model expected gross margin, inventory depletion date, and customer-facing totals after discounts. → *Expect:* the change does not create loss-making or misleading prices.
7. **Apply the repricing update.** ⚠️ *Irreversible:* before saving live, confirm SKU mapping, floor/ceiling, currency, sale badges, and channel because customers can order at the new price. → *Expect:* live prices update only for intended SKUs.
8. **Monitor results.** Track conversion, revenue, margin, buy-box status, stockout risk, and customer complaints after the change. → *Expect:* evidence that repricing moved the target metric without breaking constraints.
9. **Roll back or iterate.** Restore prior price if performance worsens or if a rule violation appears. → *Expect:* each SKU has a current price and reason recorded.

## Decision points

- Inventory is perishable or seasonal → prioritize sell-through date over maximum margin.
- Competitor price is below your floor → do not match; improve offer, bundle, or stop bidding.
- Product is scarce with long restock lead time → raise price or limit promotions to slow depletion.
- Repricing tool uses automation → start with approval mode before fully automatic changes.

## Failure modes & recovery

- **F1 Price below floor:** detect a live price that loses money → pause automation, restore floor price, and audit affected orders.
- **F2 Wrong SKU mapped:** detect a price change on the wrong variant → revert immediately and correct feed mapping.
- **F3 Race to the bottom:** detect repeated competitor matching that erodes margin → switch to floor-based or value-based rules.
- **F4 Customer trust issue:** detect complaints about volatile or unfair pricing → stabilize prices and document promotion windows.
- **F5 Feed delay:** detect marketplace still showing old prices → check feed status and avoid duplicate updates until sync completes.

## Verification

The intended SKUs have live prices within approved floor/ceiling bounds, the repricing reason is recorded, and monitoring confirms no unintended SKU, currency, or discount-stack violation.

## Variations

- Marketplace repricing: buy-box and competitor feed latency matter more.
- Owned store: conversion, margin, and email/ad campaign timing may matter more.
- Perishable inventory: expiration date and disposal cost become core pricing inputs.

## Safety & privacy

Medium risk because automated prices can create real financial harm. Enforce floor/ceiling limits, keep an audit trail, and avoid discriminatory or deceptive pricing practices.
