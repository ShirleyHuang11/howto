---
name: calculate-a-product-margin
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: basic
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

Calculate a product's gross and contribution margin so pricing, discounts, and ads can be judged against real profitability.

## Preconditions

- Product selling price, product cost, packaging cost, payment fees, shipping subsidy, marketplace fees, and expected return cost.
- Access to order data or finance records.
- A target margin percentage or dollar contribution.

## Steps

1. **Collect the selling price.** Use the actual customer-paid item price after automatic discounts but before taxes collected on behalf of authorities. → *Expect:* one net item revenue value.
2. **Collect product and packaging costs.** Include landed cost, duties, inbound freight allocation, inserts, and packaging. → *Expect:* a complete unit cost before selling fees.
3. **Add transaction and platform fees.** Include payment processing, marketplace commission, app fees per order, and currency conversion if relevant. → *Expect:* variable selling fees are assigned to the unit.
4. **Add fulfillment costs.** Include pick-pack, postage, shipping subsidy, and expected reshipment or return cost. → *Expect:* fulfillment cost per sold unit is estimated.
5. **Calculate gross margin.** Subtract product and packaging cost from net item revenue, then divide by net item revenue. → *Expect:* a gross margin percentage.
6. **Calculate contribution margin.** Subtract all variable costs from net item revenue, then divide by net item revenue. → *Expect:* a contribution margin percentage and dollar contribution.
7. **Compare against the target.** Decide whether the product can support discounts, ads, bundles, or free shipping. → *Expect:* the product is classified as above target, near target, or below target.

## Decision points

- Product has high return rate → include expected return cost before approving ads or discounts.
- Shipping is customer-paid → include only the subsidy or undercharge, not the full postage.
- Marketplace collects fees differently by category → use the exact category fee schedule.

## Failure modes & recovery

- **F1 Cost omission:** detect margin that ignores fulfillment or payment fees → recalculate with all variable costs.
- **F2 Discount mismatch:** detect using list price instead of actual sold price → use order-level realized revenue.
- **F3 Currency error:** detect costs and revenue in different currencies → convert using documented rates.
- **F4 Average hides variants:** detect one variant losing money → calculate margin by SKU, not just product family.

## Verification

The product has a documented gross margin and contribution margin using actual selling price and all relevant variable costs, and the result is compared to the target margin.

## Variations

- `marketplace`: include referral fees, closing fees, fulfillment fees, storage fees, and advertising fees separately.
- Digital goods: replace shipping and packaging with platform fees, support cost, and refund allowance.

## Safety & privacy

Medium risk because incorrect margin can drive money-losing decisions. Use real cost records and keep supplier pricing and customer order exports private.
