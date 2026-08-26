---
name: recognize-a-subscription-trap
domain: finance
subdomain: optimize
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

You identify risky subscription offers before signing up, avoid hidden recurring charges, and document cancellation terms if you proceed.

## Preconditions

- The offer page, checkout page, terms, and price details.
- A payment method you can monitor or a virtual card if available.
- A personal maximum price after any trial or promotion.

## Steps

1. **Find the recurring-price disclosure.** Look for renewal price, billing frequency, trial length, taxes, shipping, and add-ons. → *Expect:* the real post-promotion cost is known.
2. **Read cancellation terms before checkout.** Check whether cancellation is online, by phone, before a deadline, or subject to return shipping or minimum term. → *Expect:* you know exactly how and when to cancel.
3. **Inspect prechecked boxes and bundles.** Remove add-ons, insurance, newsletters, or extra shipments you do not want. → *Expect:* cart contains only the intended product or service.
4. **Check seller reputation and contact paths.** Search for complaint patterns about impossible cancellation, unauthorized renewals, or refund refusal. → *Expect:* no unresolved pattern suggests a trap, or you decide to walk away.
5. **Use a controlled payment method if proceeding.** Choose a virtual card, spending limit, or account alerts where available. → *Expect:* the payment method can be monitored or limited.
6. **Save the terms at signup.** ⚠️ *Irreversible:* before entering payment, confirm renewal price, cancellation deadline, and refund policy. → *Expect:* screenshots or PDFs capture the exact offer terms.
7. **Set a cancellation reminder before the renewal deadline.** Place the reminder several days before the trial ends. → *Expect:* calendar alert includes the cancellation link or phone number.
8. **Verify first charge and subscription status.** Check the account and bank after signup. → *Expect:* the charge matches the disclosed amount and the subscription page shows the expected plan.

## Decision points

- Cancellation requires phone only → proceed only if the value justifies retention pressure.
- Renewal price is hidden until after payment → abandon checkout.
- Reviews show repeated unauthorized charges → choose a different seller.
- Trial requires return shipping of physical goods → include shipping cost and deadline in the decision.

## Failure modes & recovery

- **F1 Hidden continuity plan:** detect unexpected recurring shipment or membership → cancel immediately and dispute if disclosure was unclear.
- **F2 Impossible cancellation:** detect broken links or unanswered phone lines → send written cancellation through every official channel and save proof.
- **F3 Price jump after trial:** detect higher-than-expected renewal → request refund using saved terms and dispute if denied.
- **F4 Add-on charge:** detect extra plan or warranty in receipt → remove the add-on and request reversal before the refund window closes.

## Verification

Before signup, the renewal price, billing date, cancellation method, and refund terms are documented; after signup, the account shows only the intended subscription and a reminder is scheduled before renewal.

## Variations

- `us`: some states require online cancellation for subscriptions bought online, but rules vary.
- Mobile-app subscription: cancellation may be managed through the app store rather than the merchant.

## Safety & privacy

Medium risk because subscriptions create recurring charges. Do not enter payment when renewal terms are hidden, use alerts, and keep cancellation proof until at least one billing cycle after cancellation.
