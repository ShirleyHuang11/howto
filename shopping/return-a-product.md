---
name: return-a-product
domain: shopping
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [shopping/buy-a-product-online]
status: draft
last_verified: 2026-07-20
---

## Goal

A purchased product is returned to the seller and the refund (or exchange) is confirmed back to your payment method.

## Preconditions

- The order number and receipt are available.
- The item is in returnable condition per the seller's policy (packaging, tags, unused — check the policy's exact words).
- The return window has not lapsed.

## Steps

1. **Read the return policy for this order.** Find window length, condition requirements, who pays return shipping, and refund method. → *Expect:* you can state deadline, cost, and refund destination before acting.
2. **Initiate the return in the order system.** Order history → the item → "Return or replace". Select a reason code honestly — "defective" and "changed mind" trigger different flows and fee treatment. → *Expect:* the system offers return methods (drop-off, pickup, mail) and shows any deducted fees.
3. **Choose refund or exchange, and a return method.** [BRANCH: refund | exchange for variant] → *Expect:* a return authorization with a shipping label, QR code, or drop-off instructions.
4. **Pack the item.** Original packaging and all accessories/tags included; photograph the item and the packed box as evidence of condition. → *Expect:* photos stored; box sealed with the label or QR ready.
5. **Hand the package over.** Drop off at the designated carrier/locker or hand to pickup. Get a receipt or scan confirmation. ⚠️ *Irreversible:* once handed over you cannot retrieve contents — double-check you didn't include unrelated items. → *Expect:* tracking shows the return in transit within a day.
6. **Track until received.** → *Expect:* tracking flips to "delivered to seller", then the order system marks the return received.
7. **Confirm the refund.** → *Expect:* refund issued notice, and the amount posts to the original payment method within the stated processing window (often 5–10 business days).

## Decision points

- Return window already lapsed → contact support anyway (goodwill exceptions exist); otherwise consider resale.
- Item arrived damaged/not-as-described → use the dispute/claim flow instead of a standard return; seller usually pays shipping and the ⚠️ evidence photos from step 4 become essential.
- Refund amount is short (restocking/shipping deduction) → check whether the deduction matches policy; if not, F3.

## Failure modes & recovery

- **F1 No return option in order history:** third-party marketplace seller — message the seller directly; escalate to the marketplace's guarantee program if no response within its SLA.
- **F2 Return delivered but not acknowledged:** wait the stated processing days, then open a claim with the delivery scan receipt from step 5.
- **F3 Refund missing or short:** contact support with order number, tracking, and photos; escalate to a card chargeback only after the seller's process fails — chargebacks are slow and may close the account.

## Verification

The refund for the expected amount is visible as posted (not pending) on the payment method's statement, and the order history shows the return closed.

## Variations

- In-store purchases: steps 2–5 collapse into bringing item + receipt to the service desk; refund often lands instantly on the card.
- `cn` marketplaces: return windows are commonly 7 days no-reason; pickup couriers handle step 5.

## Safety & privacy

Medium risk: money in transit. Keep every artifact (photos, drop-off receipt, tracking number) until the refund posts — they are your only leverage in disputes.
