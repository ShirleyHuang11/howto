---
name: ask-a-happy-customer-for-a-review
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: basic
est_time: 15min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You ask a satisfied customer for an honest review in a compliant way that does not pressure them, manipulate ratings, or expose private data.

## Preconditions

- Completed order with delivery confirmed and no unresolved support issue.
- Review platform rules for incentives, timing, and prohibited language.
- Approved customer messaging channel or review-request tool.

## Steps

1. **Identify eligible customers.** Filter for delivered orders, enough time to use the product, no open return/dispute, and no recent complaint. → *Expect:* a list of customers likely to have a fair post-purchase opinion.
2. **Check consent and channel rules.** Confirm the customer can receive transactional or review-request messages under platform and email/SMS rules. → *Expect:* only permitted recipients remain.
3. **Write a neutral request.** Ask for an honest review, avoid asking only for positive ratings, and do not condition benefits on review content. → *Expect:* message copy complies with review rules.
4. **Include the correct review link.** Use the product or order-specific review URL from the platform/tool. → *Expect:* the customer can reach the review form with minimal friction.
5. **Disclose any incentive if allowed.** If offering a coupon or loyalty points, state that it is for any honest review and confirm platform rules allow it. → *Expect:* incentive terms are transparent and compliant.
6. **Send the review request.** ⚠️ *Irreversible:* before sending, confirm recipient list, message text, incentive terms, and unsubscribe/compliance settings because customers receive it immediately. → *Expect:* the review request is sent or scheduled.
7. **Monitor responses.** Track review submissions, replies, unsubscribes, and complaints. → *Expect:* you know whether the request generated reviews without compliance issues.
8. **Respond appropriately.** Thank reviewers or route negative feedback to support without asking them to change ratings improperly. → *Expect:* customer feedback is handled professionally.

## Decision points

- Customer has an unresolved problem → solve the issue before requesting a review.
- Platform forbids incentives → do not offer coupons, gifts, or entries tied to reviews.
- Customer leaves negative review → respond with help and facts, not pressure.
- Product is sensitive/private → use extra care in message wording and avoid exposing product details in subject lines.

## Failure modes & recovery

- **F1 Review gating:** detect workflow asking only happy customers to review publicly → remove gating and request honest reviews from eligible customers consistently.
- **F2 Incentive violation:** detect platform policy forbids rewarded reviews → cancel incentive campaign and document correction.
- **F3 Wrong recipient:** detect message sent to customer with open dispute → apologize, stop further requests, and resolve support issue.
- **F4 Spam complaints:** detect high unsubscribe or complaint rate → reduce frequency, improve consent filters, and use transactional limits correctly.

## Verification

The review request was sent only to eligible customers through an allowed channel, with neutral honest-review language, compliant incentive handling if any, and recorded delivery or schedule status.

## Variations

- Marketplace order: use the marketplace's built-in review request button if required.
- Post-purchase email tool: automate timing but suppress open returns, disputes, and unsubscribed customers.
- B2B customer: ask account contact for testimonial permission separately from product review.

## Safety & privacy

Medium risk because customer contact data and platform reputation are involved. Do not buy reviews, review-gate, disclose sensitive purchases unnecessarily, or message customers without permitted consent.
