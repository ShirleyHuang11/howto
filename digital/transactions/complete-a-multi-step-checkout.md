---
name: complete-a-multi-step-checkout
domain: digital
subdomain: transactions
locale: [generic]
interface: web
difficulty: intermediate
est_time: 15min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You complete an online checkout accurately, avoid unwanted add-ons, and receive a valid order confirmation.

## Preconditions

- Items or services selected, shipping address, contact details, and payment method.
- Maximum total price including shipping, tax, fees, and discounts.
- Account access if checkout requires login.

## Steps

1. **Review the cart contents.** Confirm item names, variants, sizes, quantities, dates, subscriptions, and delivery method. → *Expect:* cart contains only intended purchases.
2. **Check seller and return terms.** Verify merchant identity, delivery estimate, return window, warranty, cancellation policy, and support channel. → *Expect:* the purchase source and remedy path are acceptable.
3. **Enter shipping or service details.** Use the correct recipient, address, phone, email, and delivery instructions. → *Expect:* address validation succeeds or the exact intended address is selected.
4. **Apply discounts and credits.** Enter promo codes, gift cards, store credits, or loyalty rewards and verify the reduction. → *Expect:* checkout total decreases by the expected amount.
5. **Choose payment deliberately.** Select card, wallet, virtual card, or financing based on protection, fees, and budget. → *Expect:* payment method is accepted and no unwanted financing is selected.
6. **Remove unwanted extras.** Decline preselected insurance, tips, subscriptions, donations, expedited shipping, or bundles unless intentional. → *Expect:* final review shows only chosen add-ons.
7. **Perform the final review.** Compare total price against your cap, shipping date, billing address, and refund policy. ⚠️ *Irreversible:* clicking place order authorizes payment and may start fulfillment immediately. → *Expect:* final checkout page is correct and within budget.
8. **Place the order once.** Submit payment and wait for completion without refreshing. → *Expect:* order confirmation page with order number.
9. **Save and verify confirmation.** Check email or account order history for status, total, merchant, and delivery details. → *Expect:* a saved confirmation matching the intended purchase.

## Decision points

- Total exceeds cap after tax or shipping → remove items, change shipping, or abandon checkout.
- Discount fails → verify exclusions and decide whether to proceed without it.
- Delivery estimate is too late → choose another seller before payment.
- Payment authentication fails → retry once through the bank prompt, then use another protected method.

## Failure modes & recovery

- **F1 Duplicate order:** detect two confirmations or charges → contact merchant immediately to cancel one before fulfillment.
- **F2 Wrong variant ordered:** detect mismatch in confirmation → use cancellation or change window immediately.
- **F3 Hidden subscription:** detect recurring terms in cart or receipt → cancel subscription and request refund if enrollment was unclear.
- **F4 Payment charged but no order:** detect card authorization without confirmation → check account history and contact merchant before placing another order.

## Verification

The merchant account or email shows one order confirmation number with the intended items, delivery details, and final total at or below the price cap.

## Variations

- `marketplace`: check seller ratings, fulfillment source, and return responsibility.
- `digital-goods`: delivery may be immediate and refunds limited after access.
- `tickets-travel`: names, dates, and cancellation terms matter more than shipping.

## Safety & privacy

Medium risk because payment and address data are exposed. Use trusted checkout pages, avoid saved cards on shared devices, and confirm the final total before authorizing payment.
