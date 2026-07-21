---
name: track-a-delivery
domain: shopping
locale: [generic]
interface: web
difficulty: basic
est_time: 10min
risk: low
prerequisites: [shopping/buy-a-product-online]
status: draft
last_verified: 2026-07-20
---

## Goal

You know where an ordered package is, when it will arrive, and it ends up in your hands — including when tracking stalls or delivery fails.

## Preconditions

- An order confirmation with an order number; a tracking number once the seller ships.
- Access to the ordering account or the confirmation email.

## Steps

1. **Find the tracking number.** Order history → the order → "Track", or the shipping-confirmation email. → *Expect:* a carrier name and tracking number (or an in-portal tracking view).
2. **Open the tracking page.** Use the order portal's link, or type the carrier's site and paste the number. Ignore "your package has a problem" texts/emails you didn't expect — that's the top smishing lure; only trust tracking you navigate to yourself. → *Expect:* a status timeline: label created → in transit → out for delivery → delivered.
3. **Interpret the current status.** "Label created" for days = seller hasn't handed it over yet (seller's issue, not carrier's). "In transit" gaps of 24–48 h between scans are normal. → *Expect:* an estimated delivery date consistent with the seller's promise.
4. **Prepare for the delivery day.** Ensure the address has a deliverable point (reachable mailbox/doorstep/locker); enable carrier notifications if offered; authorize a safe place or neighbor if you'll be out. → *Expect:* delivery-day instructions set where the carrier supports them.
5. **On "out for delivery": be reachable.** Signature-required packages fail without a receiver. → *Expect:* delivery scan by end of day: "delivered" with a location note, or an attempted-delivery notice.
6. **Verify receipt immediately after the delivered scan.** Check doorstep/mailbox/locker/reception. [BRANCH: package in hand → step 7 | "delivered" but nothing there → F2] → *Expect:* the physical package matches the order; packaging intact.
7. **Inspect contents promptly.** Damage or wrong item → photograph everything as found (before discarding packaging) and go to `shopping/return-a-product`'s damaged-item path. → *Expect:* contents correct and intact; order can be marked complete.

## Decision points

- Estimated date slips past when you need the item → check for intercept/hold options; for gifts or trips, buy locally and return the late one within window.
- Attempted delivery notice left → follow its exact re-delivery or pickup instructions (usually a code and a pickup point with an ID requirement, held ~7 days).
- Package routed to a pickup locker → collect within the locker window (often 2–3 days) using the code sent to you.

## Failure modes & recovery

- **F1 Tracking stalled >3 business days with no scan:** contact the *seller* first (they own the carrier relationship and can open a trace); carriers rarely act for recipients on seller-paid shipments.
- **F2 Marked delivered but missing:** check all doors, neighbors, household members, and the delivery photo if provided; wait a few hours (premature scans happen); then report to the seller for refund/reshipment — most platforms side with the buyer on no-photo deliveries.
- **F3 Customs hold (international):** respond to any duty-payment request through the carrier's official site only (paste the tracking yourself — duty-payment texts are a scam genre); unpaid duties return the package.

## Verification

The package is physically in your possession, its contents verified against the order, and the tracking timeline shows delivered — or a seller-acknowledged trace/refund case exists.

## Variations

- Marketplace consolidated shipping (`cn` platforms): one order may split into several trackings — check each item's own status.
- Apartment buildings: "delivered" often means the mailroom/reception — that's the first place to check in F2.

## Safety & privacy

Low risk. The main hazard is fake delivery texts phishing for card details — the step-2 rule (navigate to tracking yourself, never via unexpected links) is the whole defense.
