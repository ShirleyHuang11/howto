---
name: handle-a-price-match-request
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: intermediate
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

Evaluate a customer's price-match request and either issue an approved adjustment or decline with a clear policy-based explanation.

## Preconditions

- Access to the customer's order or cart and the store's price-match policy.
- The competitor URL, screenshot, or quote supplied by the customer.
- Permission level for issuing discounts, refunds, or store credit.

## Steps

1. **Capture the request details.** Record customer identity, product SKU, requested competitor price, date, and source URL. → *Expect:* a complete ticket or note with the claimed lower price.
2. **Verify product equivalence.** Compare model, size, color, condition, warranty, seller, shipping, and taxes. → *Expect:* either an exact match or a documented mismatch.
3. **Check policy eligibility.** Confirm the competitor, sale type, time window, stock status, and exclusions. → *Expect:* the request is classified as eligible or ineligible under policy.
4. **Calculate the true comparable price.** Include competitor shipping, required memberships, coupons, and tax treatment where policy allows. → *Expect:* a final comparable price difference.
5. **Choose the adjustment method.** [BRANCH: pre-purchase coupon | post-purchase partial refund | store credit | decline] Match the remedy to policy and payment status. → *Expect:* the next action is approved and documented.
6. **Apply the adjustment if approved.** ⚠️ *Irreversible:* confirm SKU, amount, and order before issuing money or credit. → *Expect:* the customer receives the promised discount, refund, or credit.
7. **Reply with the decision.** Explain the outcome, amount, and any remaining steps in plain language. → *Expect:* the customer has a clear answer tied to the policy.

## Decision points

- Competitor item is out of stock → decline if policy requires in-stock availability.
- Competitor is a third-party marketplace seller → verify authorized-seller rules before matching.
- Adjustment would sell below cost → escalate if policy permits manager exceptions only.

## Failure modes & recovery

- **F1 Fake or stale listing:** detect a screenshot without a live matching page → ask for a current URL or decline due to unverifiable price.
- **F2 Wrong SKU matched:** detect variant mismatch after approval → cancel unused coupon or correct the refund before communicating.
- **F3 Double adjustment:** detect a coupon plus refund for the same match → reverse the duplicate where possible and document the correction.
- **F4 Customer disputes denial:** detect repeated objections → cite the exact eligibility failure and offer escalation only if new evidence is provided.

## Verification

The request has a recorded eligibility decision, any approved adjustment has the exact authorized amount applied to the correct order or customer, and the customer has been notified.

## Variations

- `us`: advertised-price and manufacturer minimum-advertised-price rules may affect what can be matched.
- Subscription products: compare first-term and renewal pricing separately.

## Safety & privacy

Medium risk because adjustments move money. Verify the competitor evidence and customer account before issuing refunds, coupons, or credit.
