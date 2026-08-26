---
name: sell-on-facebook-marketplace
domain: shopping
subdomain: marketplace
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You list an item on Facebook Marketplace, screen buyers, and complete a local or shipped sale without exposing yourself to common payment or meetup scams.

## Preconditions

- A Facebook account with Marketplace access.
- The item cleaned, photographed, and ready to hand over or ship.
- A safe public meetup location or packing materials for shipping.

## Steps

1. **Confirm the item can be sold.** Check Marketplace rules for prohibited goods and local legal limits. → *Expect:* the item is allowed and can be listed without risking account removal.
2. **Research local asking prices.** Search similar Marketplace listings and adjust for condition, urgency, and whether delivery is included. → *Expect:* a target price and a private minimum.
3. **Prepare photos and details.** Photograph the item in good light, including flaws, labels, accessories, and scale when relevant. → *Expect:* a complete photo set ready for upload.
4. **Create the listing.** Choose category, condition, price, location radius, pickup or shipping option, and a title with searchable terms. → *Expect:* the draft accurately represents the item and location.
5. **Write a clear description.** Include measurements, model, what's included, defects, pickup area, and whether price is firm. → *Expect:* buyers can decide without sending basic questions.
6. **Publish the listing.** ⚠️ *Irreversible:* confirm price, location visibility, photos, and whether shipping is enabled before going live. → *Expect:* the listing appears in Marketplace and on your selling dashboard.
7. **Screen messages.** Prioritize buyers who ask specific questions and agree to platform or in-person terms; ignore overpayment, courier, code, or off-platform payment stories. → *Expect:* one credible buyer is selected.
8. **Set the payment and handoff plan.** [BRANCH: local sale, meet in a public daylight spot and accept cash or a payment you verify in your own app | shipped sale, use Marketplace checkout and ship only after payment confirmation] → *Expect:* both parties agree on time, place or shipping, and payment method.
9. **Complete the exchange.** ⚠️ *Irreversible:* verify payment is real before handing over or shipping the item. → *Expect:* the item leaves your possession only after confirmed payment.
10. **Mark the item sold.** Archive messages and save proof of payment, shipment, or meetup agreement. → *Expect:* the listing is marked sold and records are available if a dispute arises.

## Decision points

- Buyer asks for your phone number to send a verification code → stop; it is likely an account takeover attempt.
- Buyer wants home pickup → use a public safe-exchange location unless the item is too large to move.
- Multiple buyers are interested → hold only for someone who commits to a concrete pickup time or pays through an approved checkout flow.
- Shipping a high-value item → prefer Marketplace checkout with tracking and seller protection terms you understand.

## Failure modes & recovery

- **F1 Verification-code scam:** detect a request to read back a code → block and report; never share security codes.
- **F2 Fake payment screenshot:** detect a screenshot but no money in your account → keep the item and require verifiable payment.
- **F3 No-show buyer:** detect missed meetup with excuses → move to the next buyer and avoid long holds.
- **F4 Last-minute renegotiation:** detect a buyer lowering the price at pickup → accept only if above your minimum; otherwise leave.
- **F5 Unsafe meetup:** detect pressure for a private or late-night location → reschedule to a public safe-exchange spot or cancel.

## Verification

The Marketplace listing is marked sold, the item has been handed over or shipped with tracking, and payment is confirmed in your own account with no pending safety issue.

## Variations

- `us`: many police departments provide safe-exchange locations for local sales.
- Large furniture: disclose stairs, elevator access, and pickup requirements before the buyer arrives.
- Shipping enabled: use the address and label flow supplied by Marketplace, not a buyer-sent address.

## Safety & privacy

Medium risk from payment fraud and personal meetups. Limit location details until a buyer is credible, meet publicly when possible, keep conversations in Messenger, and verify money before release.
