---
name: verify-an-order-for-fraud
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

You review a flagged ecommerce order and decide whether to fulfill, hold, cancel, or request verification using evidence that reduces chargeback and customer harm.

## Preconditions

- Access to the order record, payment risk signals, customer history, and fulfillment controls.
- Store policy for fraud review, cancellation, and identity verification.
- The order has not yet shipped.

## Steps

1. **Open the order risk summary.** Review AVS, CVV, IP location, billing/shipping mismatch, proxy indicators, order velocity, and payment processor score. → *Expect:* a list of specific risk signals, not just a generic label.
2. **Compare customer and order history.** Check account age, prior successful orders, chargebacks, returns, and recent address changes. → *Expect:* context showing whether this behavior is normal for the customer.
3. **Assess item and fulfillment risk.** Note high-resale goods, expedited shipping, freight forwarding, gift cards, or digital delivery. → *Expect:* an order-level risk rating tied to what could be lost.
4. **Look for benign explanations.** Identify legitimate reasons such as traveling customer, gift shipment, corporate card, or recent move. → *Expect:* possible low-risk explanations are documented.
5. **Contact the customer through trusted channels if needed.** Use the email or phone already on the order; do not ask for full card numbers or sensitive documents unless policy requires secure upload. → *Expect:* the customer confirms or fails to confirm key order details.
6. **Decide the action.** [BRANCH: low risk, release fulfillment | uncertain, hold and request verification | high risk, cancel and void/refund] → *Expect:* the order status reflects the chosen action.
7. **Document the review.** Record evidence, customer response, decision, reviewer, and timestamp in the order notes. → *Expect:* another staff member can understand why the order was approved or stopped.
8. **Release or stop fulfillment.** ⚠️ *Irreversible:* once shipped or digitally delivered, recovery may be impossible, so confirm payment status and risk decision first. → *Expect:* fulfillment is either released with tracking or the order is canceled/refunded according to policy.

## Decision points

- Digital goods or gift cards → require much stronger confidence before delivery.
- AVS fails but repeat customer history is clean → consider manual confirmation rather than automatic cancellation.
- Customer cannot be reached and item is high value → hold or cancel instead of shipping under uncertainty.

## Failure modes & recovery

- **F1 False positive cancellation:** detect a legitimate customer complaining after cancellation → apologize, explain security review briefly, and invite reorder with verified payment.
- **F2 Chargeback after approval:** detect processor dispute → submit order notes, AVS/CVV results, delivery proof, and customer communications.
- **F3 Verification phishing risk:** detect staff asking for full card or ID over email → stop the request and use only approved secure verification channels.
- **F4 Fulfillment released too early:** detect warehouse pick/ship before review completes → mark high-risk orders as hold-before-fulfillment by automation rule.

## Verification

The flagged order has a documented fraud review with a final action, and no physical or digital fulfillment occurs until the payment and risk decision support release.

## Variations

- Stripe Radar: review rule triggers, risk score, and 3D Secure outcome.
- Shopify Fraud Analysis: combine platform indicators with customer history and fulfillment risk.
- B2B orders: verify purchase order and company domain before treating mismatch as fraud.

## Safety & privacy

Medium risk because money, identity, and fraud evidence are involved. Never request full card details, minimize identity data collection, and require explicit confirmation before shipping a high-risk order.
