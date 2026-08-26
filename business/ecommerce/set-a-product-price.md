---
name: set-a-product-price
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You set a product price that covers costs, fits market positioning, and is entered correctly in the ecommerce system.

## Preconditions

- Unit cost, payment fees, packaging, shipping subsidy, labor, returns allowance, and target margin.
- Competitor and substitute-product price references.
- Admin permission to edit product pricing.

## Steps

1. **Calculate landed unit cost.** Include product cost, freight, duties, packaging, payment fees, platform fees, fulfillment labor, and expected returns. → *Expect:* a per-unit cost number that reflects selling reality.
2. **Choose the margin target.** Set minimum gross margin and preferred gross margin based on category, cash needs, and acquisition costs. → *Expect:* a minimum viable price and a target price.
3. **Map the market range.** Compare direct competitors, substitutes, brand positioning, review strength, and shipping terms. → *Expect:* a realistic price band customers already understand.
4. **Select the list price.** Choose a price that meets the minimum margin and supports the product's positioning. → *Expect:* a final list price with a documented rationale.
5. **Decide discount boundaries.** Define the lowest promotional price, coupon exclusions, wholesale price, and bundle impact. → *Expect:* a floor price that protects margin during promotions.
6. **Enter pricing fields.** Add price, compare-at/reference price only if truthful, cost field, tax category, and variant-specific prices. → *Expect:* the admin record reflects the intended price for each variant.
7. **Preview checkout totals.** Add the product to cart and check tax, shipping, discounts, and currency conversion if relevant. → *Expect:* the customer-facing total matches expectations.
8. **Publish the price.** ⚠️ *Irreversible:* before saving live, confirm SKU, channel, price, discount eligibility, and currency because customers can place orders immediately. → *Expect:* the live product page and checkout show the correct price.
9. **Monitor early performance.** Track conversion, abandoned carts, margin, ad spend, and support questions after the price changes. → *Expect:* data showing whether the price is sustainable.

## Decision points

- Price needed for margin exceeds market range → reduce costs, improve positioning, bundle value, or reconsider selling the item.
- Competitors hide shipping in item price → compare all-in delivered price, not list price alone.
- Product has variants with different costs → price variants separately rather than averaging into a loss.
- Demand spikes after launch → consider inventory and brand impact before raising price.

## Failure modes & recovery

- **F1 Decimal or currency error:** detect a live price that is 10x too high or low → pause sales if needed, correct price, and review affected orders.
- **F2 Discount stacking loss:** detect coupons combining below floor price → adjust promotion rules and exclude the product.
- **F3 Margin ignored:** detect revenue growth with negative contribution margin → recalculate full cost and raise price or stop ads.
- **F4 Reference-price violation:** detect an unsubstantiated compare-at price → remove it and keep records supporting any future reference price.

## Verification

The live product price and checkout total match the documented list price, each variant meets or intentionally flags the minimum margin, and discount rules cannot push the item below its floor price.

## Variations

- Marketplace: fees and shipping requirements may differ by category and seller tier.
- International store: include currency conversion, VAT/GST display rules, and duties.
- Subscription product: calculate acquisition payback and churn, not just first-order margin.

## Safety & privacy

Medium risk because incorrect prices create real orders and customer disputes. Confirm currency, variant, discount stacking, and compare-at legality before publishing.
