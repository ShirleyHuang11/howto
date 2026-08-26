---
name: issue-a-partial-refund
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: intermediate
est_time: 15min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You issue a partial refund for a specific order reason without refunding too much, duplicating compensation, or losing the dispute evidence trail.

## Preconditions

- Order number, customer request, item affected, and reason for adjustment.
- Store policy for partial refunds, shipping refunds, taxes, and goodwill credits.
- Admin access to payments/refunds and customer messaging.

## Steps

1. **Open and verify the order.** Confirm customer, payment status, fulfillment status, item, quantity, and prior refunds or chargebacks. → *Expect:* you are working on the correct paid order with no duplicate open compensation.
2. **Validate the refund reason.** Review evidence for damage, late delivery, missing accessory, price adjustment, service failure, or negotiated resolution. → *Expect:* a documented reason that supports a partial refund.
3. **Calculate the refund amount.** Include item portion, tax adjustment, shipping if applicable, discounts, and maximum allowed goodwill amount. → *Expect:* a precise refund amount and what it covers.
4. **Confirm customer agreement when needed.** For negotiated settlements, state the amount and whether it resolves the issue. → *Expect:* customer acceptance is recorded in the order thread.
5. **Check inventory impact.** Decide whether any item is returned, kept, replaced, or written off. → *Expect:* refund action will not incorrectly restock inventory.
6. **Enter the partial refund.** Select the item or custom amount, reason code, tax/shipping treatment, and internal note. → *Expect:* the refund preview matches the intended amount.
7. **Submit the refund.** ⚠️ *Irreversible:* before confirming, verify order number, customer, refund amount, payment method, inventory action, and that no duplicate refund exists. → *Expect:* payment processor records a partial refund transaction.
8. **Notify the customer.** Send the amount, expected posting time, and any remaining action required. → *Expect:* the customer has clear confirmation of the refund.

## Decision points

- Customer also opened a payment dispute → handle through the dispute workflow to avoid double refunding.
- Partial refund would exceed item value → choose replacement, full return, or manager approval.
- Refund is for late carrier delivery → check shipping guarantee and carrier claim rules.
- Customer demands off-platform compensation → decline and keep refund inside the order system.

## Failure modes & recovery

- **F1 Duplicate refund:** detect prior refund or open dispute for same issue → stop and reconcile before issuing more money.
- **F2 Tax mismatch:** detect platform recalculating tax unexpectedly → preview total and adjust line-item selection.
- **F3 Wrong payment method:** detect multiple captures or split tender → select the original eligible transaction.
- **F4 Customer says refund not received:** detect processor status posted but bank delay → provide transaction timing and trace only through approved payment support.

## Verification

The order shows a partial refund transaction for the correct amount and reason, no duplicate refund or inventory error exists, and the customer has been notified of the posting timeline.

## Variations

- Marketplace order: partial refunds may require platform reason codes and may affect seller metrics.
- Subscription order: decide whether the credit applies to the current charge or next renewal.
- B2B invoice: issue a credit memo rather than card refund if accounting requires it.

## Safety & privacy

Medium risk because the action moves money and exposes order data. Confirm the customer/order, amount, payment method, and dispute status before submitting.
