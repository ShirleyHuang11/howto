---
name: read-a-checkout-total-before-paying
domain: digital
subdomain: transactions
locale: [generic]
interface: web
difficulty: basic
est_time: 15min
risk: medium
prerequisites: [have-payment-method]
status: draft
last_verified: 2026-08-25
---

## Goal

You review the final checkout total and terms before paying so you do not approve hidden fees, wrong quantities, subscriptions, or unwanted add-ons.

## Preconditions

- You have items or services in an online cart and are at the payment review step.
- You know your maximum acceptable total and required delivery or service terms.
- You have not clicked the final pay, place order, subscribe, or book button yet.

## Steps

1. **Pause on the final review screen.** Do not rely on the cart subtotal or advertised price. → *Expect:* the page shows the final order summary or a button that will place the order.
2. **Read every price line.** Check item subtotal, quantity, discounts, shipping, service fees, taxes, tips, deposits, currency, and total due today. → *Expect:* the final total and any future amount are known.
3. **Look for recurring terms.** Search the page for subscription, auto-renew, trial, monthly, membership, installment, deposit, or due later. → *Expect:* you know whether this is one-time payment or recurring billing.
4. **Check fulfillment details.** Verify delivery address, pickup location, dates, cancellation window, return policy, and seller. → *Expect:* the purchase will go to the correct place under acceptable terms.
5. **Remove unwanted add-ons.** [BRANCH: warranty, donation, insurance, expedited shipping, tip, membership, or bundle added unintentionally, remove it | desired add-on, keep it after confirming price] → *Expect:* only intentional items and services remain.
6. **Compare against your cap.** If the total exceeds your maximum, adjust shipping, remove items, find a discount, or abandon the cart. → *Expect:* the final total is at or below your cap or you decide not to buy.
7. **Confirm once and pay.** ⚠️ *Irreversible:* before clicking the final button, confirm total, currency, seller, quantity, delivery, and recurring terms. → *Expect:* the site returns an order confirmation or payment receipt at the reviewed total.
8. **Save the confirmation.** Store the receipt or screenshot showing the total and order number. → *Expect:* you have proof of what you approved.

## Decision points

- Button text says subscribe, start trial, or join → treat it as recurring until proven otherwise.
- Total changed after entering address → re-read taxes, shipping, and delivery fees.
- Currency is foreign or dynamic → check conversion and foreign transaction fees before paying.
- Marketplace seller changed at checkout → re-check seller legitimacy and return policy.

## Failure modes & recovery

- **F1 Hidden add-on remains:** detect a warranty, donation, or membership on the receipt → cancel quickly if possible or request removal/refund.
- **F2 Quantity mismatch:** detect multiples ordered accidentally → cancel before fulfillment or start a return.
- **F3 Recurring charge accepted:** detect subscription terms after purchase → cancel renewal immediately and save proof.
- **F4 Price changed after payment:** detect receipt total above reviewed amount → contact merchant with screenshots and dispute if unresolved.

## Verification

Payment is submitted only after the final total, currency, quantity, seller, delivery terms, and recurring status are reviewed and within the chosen cap, and the saved confirmation matches that approved total.

## Variations

- `travel`: check resort fees, baggage, seat, cleaning, occupancy, and cancellation charges.
- `food-delivery`: tip, service fee, delivery fee, small-order fee, and menu markups can all change the total.
- `tickets`: check transfer restrictions, seat details, resale fees, and all-in pricing.

## Safety & privacy

Medium risk because the final click authorizes payment. Slow down before the irreversible step, remove unwanted add-ons, and keep proof of the total you approved.
