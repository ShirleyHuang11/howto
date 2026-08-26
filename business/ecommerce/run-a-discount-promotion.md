---
name: run-a-discount-promotion
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

You create a discount promotion with controlled eligibility, margin protection, and a verified customer checkout experience.

## Preconditions

- Promotion goal, eligible products, start/end dates, budget, and success metric.
- Minimum margin or maximum discount limit for each included product.
- Ecommerce admin access to discounts, coupons, or automatic promotions.

## Steps

1. **Define the promotion objective.** Choose whether the goal is inventory clearance, first purchase, average-order-value lift, retention, or campaign attribution. → *Expect:* a measurable objective and target audience.
2. **Select eligible products and customers.** Include only SKUs, collections, customer segments, or channels that fit the objective. → *Expect:* a precise eligibility list.
3. **Calculate margin impact.** Model discount amount, shipping subsidy, platform fees, returns, and ad spend against the floor margin. → *Expect:* a maximum safe discount and expected contribution margin.
4. **Create the discount rule.** Configure code or automatic discount, value, minimum order, usage limits, start/end time, customer eligibility, and stacking rules. → *Expect:* a draft or saved promotion with bounded rules.
5. **Write customer-facing terms.** State eligible items, expiration, exclusions, minimums, and whether the discount combines with other offers. → *Expect:* the offer terms match the actual rule.
6. **Test checkout scenarios.** Try eligible and ineligible products, minimum order edge cases, existing coupons, and mobile checkout. → *Expect:* the discount applies only where intended.
7. **Launch the promotion.** ⚠️ *Irreversible:* before activation, confirm dates, timezone, discount value, eligibility, usage caps, and stacking because customers can redeem immediately. → *Expect:* the promotion is active and visible to the intended audience.
8. **Monitor redemptions and margin.** Track code usage, order values, inventory, customer segment, and net margin during the promotion. → *Expect:* redemptions stay within budget and inventory constraints.
9. **End and review.** Disable or let the promotion expire, then compare results against the objective. → *Expect:* the discount is no longer redeemable and performance is recorded.

## Decision points

- Goal is new-customer acquisition → restrict to first-order customers and prevent self-referral abuse.
- Goal is clearance → exclude low-stock items and set a quantity budget.
- Margin goes below floor in testing → reduce discount, add minimum order, or exclude low-margin products.
- Promotion is shared publicly unexpectedly → enforce usage caps or customer eligibility.

## Failure modes & recovery

- **F1 Discount stacks unexpectedly:** detect multiple offers combining below margin floor → disable stacking or pause the promotion.
- **F2 Wrong timezone:** detect early or late activation → correct schedule and communicate if customers were affected.
- **F3 Ineligible products discounted:** detect orders with excluded SKUs receiving the code → pause, fix rules, and audit affected orders.
- **F4 Abuse by repeat accounts:** detect suspicious repeated redemptions → tighten customer eligibility, usage limits, and fraud review.

## Verification

The promotion is active only for the intended products/customers/time window, test carts show the correct discount behavior, and redemption/margin tracking is in place.

## Variations

- Marketplace coupon: platform may control placement, funding, and stacking rules.
- Email-only promotion: use single-use or segment-limited codes to reduce leakage.
- Clearance sale: combine discount rules with inventory caps and no-backorder settings.

## Safety & privacy

Medium risk because discount rules directly affect order revenue. Confirm margin, eligibility, usage limits, and customer-facing terms before activation, and do not expose private customer segments in public offer copy.
