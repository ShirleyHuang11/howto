---
name: set-a-break-even-price
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

Set the minimum price at which a product breaks even after variable costs, fees, and any required advertising or overhead allocation.

## Preconditions

- Accurate per-unit product cost, fulfillment cost, fees, tax handling, and expected return cost.
- A decision on whether break-even includes ad spend, overhead, or only variable costs.
- Permission to change product prices.

## Steps

1. **Define the break-even scope.** Choose variable-cost break-even, contribution break-even with ads, or fully loaded break-even with overhead. → *Expect:* the calculation scope is explicit.
2. **List all per-unit costs.** Include landed cost, packaging, payment fees, platform fees, shipping subsidy, returns, and support allowance. → *Expect:* each variable cost has a value and source.
3. **Convert percentage fees into a formula.** Separate fixed fees from percentage fees so the price solves correctly. → *Expect:* the price formula accounts for fee percentages.
4. **Calculate the break-even price.** Divide fixed per-unit costs by one minus the total percentage-fee rate, then add required profit or ad allowance if included. → *Expect:* a minimum price before rounding.
5. **Check market and policy constraints.** Compare the break-even price to competitor prices, minimum advertised price, and marketplace rules. → *Expect:* you know whether the product can compete profitably.
6. **Set or record the price floor.** Save the floor in the pricing sheet, repricer, or product admin. ⚠️ *Irreversible:* do not lower live price below the floor unless leadership approves a planned loss. → *Expect:* the system or team has a clear minimum price.
7. **Test promotions against the floor.** Apply common coupons, bundles, and free-shipping thresholds to make sure they do not go below break-even. → *Expect:* planned discounts stay above the floor or are blocked.

## Decision points

- Break-even price exceeds market price → renegotiate costs, change positioning, or stop selling the product.
- Percentage fees vary by channel → calculate a separate floor for each channel.
- Product is a loss leader → document the allowed loss and success metric.

## Failure modes & recovery

- **F1 Fee formula error:** detect break-even below actual fee-adjusted cost → redo the formula separating fixed and percentage fees.
- **F2 Repricer violates floor:** detect marketplace price below minimum → pause repricing and set hard floor rules.
- **F3 Promotion leak:** detect coupon creates negative margin → exclude the SKU or raise the floor.
- **F4 Return cost ignored:** detect high returns erasing margin → add expected return cost to the calculation.

## Verification

A documented break-even price exists for the product and channel, and live pricing rules or promotion checks prevent selling below that price without explicit approval.

## Variations

- `amazon`: include referral, fulfillment, storage, refund administration, and advertising costs.
- Wholesale: account for case-pack minimums and retailer chargebacks.

## Safety & privacy

Medium risk because wrong pricing can create real losses. Protect supplier costs and confirm formulas before updating live prices or repricing tools.
