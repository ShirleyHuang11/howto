---
name: verify-a-purchase-confirmation
domain: digital
subdomain: transactions
locale: [generic]
interface: web
difficulty: basic
est_time: 15min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You confirm that a purchase actually went through once, for the correct item, amount, merchant, and delivery or access details.

## Preconditions

- Recent online purchase attempt and access to email, merchant account, and payment account.
- Expected merchant name, order total, item/service details, and delivery method.
- Order number if shown on the checkout success page.

## Steps

1. **Start with the merchant confirmation page.** Record order number, timestamp, total, items, delivery address, and estimated delivery or access date. → *Expect:* a visible order reference or clear pending message.
2. **Check confirmation email.** Verify sender domain, order number, item details, total, and links without clicking suspicious buttons. → *Expect:* email matches the checkout result.
3. **Check merchant order history.** Log in directly to the merchant site or app and open the order. → *Expect:* the order appears with the same status and details.
4. **Check payment activity.** Compare authorization or charge amount, merchant descriptor, and currency against the expected total. → *Expect:* one matching authorization or charge, not duplicates.
5. **Verify fulfillment details.** Confirm shipping address, pickup location, digital delivery email, traveler name, or license key recipient. → *Expect:* delivery/access information is correct.
6. **Save proof.** Store the receipt, invoice, order page PDF, or screenshot in a place you can find later. → *Expect:* proof includes order number, merchant, amount, and date.
7. **Act quickly on mismatches.** If item, address, date, or amount is wrong, use cancel/change support immediately. ⚠️ *Irreversible:* some orders ship or digital goods activate quickly, reducing refund options. → *Expect:* correction, cancellation, or support case number if needed.
8. **Monitor final settlement.** Recheck when the charge posts or shipment occurs. → *Expect:* posted amount and fulfillment status still match the order.

## Decision points

- Payment shows pending but no order exists → contact merchant before retrying.
- Two orders or two charges appear → cancel duplicate and document both references.
- Email exists but account has no order → verify whether guest checkout, marketplace seller, or phishing is involved.
- Digital access is delivered immediately → check refund limits before downloading or activating.

## Failure modes & recovery

- **F1 Fake confirmation email:** detect mismatched domain or links → navigate directly to merchant account and report phishing.
- **F2 Duplicate authorization:** detect two pending holds → wait for holds to drop only if one order exists; contact merchant if both become orders.
- **F3 Wrong address:** detect shipping mismatch → change before fulfillment or request carrier intercept if already shipped.
- **F4 Price mismatch:** detect charged total differs from receipt → ask merchant for adjustment or dispute with saved receipt.

## Verification

Merchant order history, confirmation email, and payment activity all show one matching purchase with the correct order number, item/service, amount, and fulfillment details.

## Variations

- `guest-checkout`: email receipt may be the only order access; save it carefully.
- `marketplace`: seller, platform, and payment descriptors may differ; match order ID and total.
- `digital-download`: confirmation may double as access credential, so store it securely.

## Safety & privacy

Medium risk because receipts expose address, purchases, and payment metadata. Save confirmations securely and use direct merchant login rather than email links when anything looks unusual.
