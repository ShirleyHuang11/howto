---
name: process-a-return-request
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

You evaluate a customer's return request, issue the correct authorization, and set conditions so the refund is accurate after the item is received.

## Preconditions

- Customer order number, item, purchase date, delivery date, and return reason.
- Store return policy, item eligibility, and refund method rules.
- Admin access to returns, labels, and customer messaging.

## Steps

1. **Open the order record.** Verify customer, items, delivery status, payment status, and prior refunds or disputes. → *Expect:* the request is tied to the correct order.
2. **Check return eligibility.** Compare request date, item category, condition, final-sale status, and reason against policy. → *Expect:* a decision on whether the item qualifies for return.
3. **Inspect evidence if needed.** For damage, wrong item, or defect, request photos, serial numbers, packaging images, or troubleshooting results. → *Expect:* enough evidence to choose standard return, replacement, or denial.
4. **Choose the return outcome.** [BRANCH: eligible return | ineligible return | damaged/wrong item] Approve with instructions, deny with policy explanation, or offer replacement/refund path. → *Expect:* a policy-backed outcome.
5. **Create the return authorization.** Select items, quantities, return reason, expected condition, restocking fee if allowed, and refund destination. → *Expect:* an RMA or return record exists.
6. **Send label and instructions.** Provide deadline, packaging requirements, included accessories, label, and tracking if the store pays return shipping. → *Expect:* the customer knows exactly how to send the item back.
7. **Receive and inspect the return.** Compare the received item, serial number, condition, and included parts against the authorization. → *Expect:* the return is accepted, partially accepted, or escalated.
8. **Issue the refund or exchange.** ⚠️ *Irreversible:* before refunding, confirm order number, item received, amount, fees, tax, shipping refund, and payment method. → *Expect:* the refund/exchange is recorded and customer is notified.
9. **Update inventory disposition.** Restock sellable items, quarantine damaged goods, or mark unsellable. → *Expect:* inventory reflects the actual returned condition.

## Decision points

- Return window has expired → deny or offer goodwill exception according to policy.
- Item is damaged in transit → collect carrier evidence and decide whether to refund before claim completion.
- Customer asks for exchange → create replacement only after eligibility and inventory are confirmed.
- Item returned incomplete → deduct allowed amount or request missing parts before refund.

## Failure modes & recovery

- **F1 Fraudulent return:** detect wrong serial number, empty box, or different item → pause refund, document evidence, and escalate under policy.
- **F2 Label not used:** detect no tracking movement before deadline → remind customer and close request if policy allows.
- **F3 Refund amount wrong:** detect tax, discount, or shipping calculated incorrectly → correct before submission or issue an adjustment if already processed.
- **F4 Chargeback opened:** detect payment dispute during return → stop duplicate refund actions and respond through the payment processor.

## Verification

The return request has a documented approve/deny/exchange outcome, any received item has been inspected, and the final refund or replacement record matches policy and order details.

## Variations

- Marketplace order: platform rules may override store policy.
- Defective item: warranty replacement may be better than return refund.
- International return: customs forms and return shipping cost may determine whether returnless refund is cheaper.

## Safety & privacy

Medium risk because refunds move money and customer data is visible. Confirm identity through the order system, never request unnecessary personal documents, and verify amounts before issuing refunds.
