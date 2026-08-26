---
name: get-a-refund-for-a-cancelled-flight
domain: travel
subdomain: booking
locale: [generic, us, eu, uk]
interface: web
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You recover the refundable value of a cancelled flight when you choose not to travel on the airline's alternative.

## Preconditions

- Booking reference, ticket number, cancellation notice, passenger names, and original payment method.
- Access to the airline, travel agency, or card account used to buy the ticket.
- A decision not to accept rebooking, voucher, or travel credit unless it is clearly better.

## Steps

1. **Confirm who cancelled the flight.** Verify that the airline cancelled or significantly changed the itinerary, not that you voluntarily cancelled first. → *Expect:* a cancellation notice or changed itinerary showing the airline-initiated disruption.
2. **Identify the merchant of record.** Check the receipt to see whether the airline, online travel agency, employer travel tool, or card portal sold the ticket. → *Expect:* the correct refund channel is known.
3. **Calculate the refundable amount.** Include unused fare, taxes, carrier-imposed fees, paid seats, bags, and services not provided. → *Expect:* a target refund amount by passenger and add-on.
4. **Reject unwanted alternatives clearly.** Do not click "accept voucher" or "confirm new flight" if you want cash. → *Expect:* the booking remains eligible for a refund request rather than a voluntary exchange.
5. **Submit the official refund request.** Use the merchant's refund form, choose cancelled flight or schedule change, attach the notice, and request refund to original payment. ⚠️ *Irreversible:* confirm you do not need the replacement itinerary before cancelling remaining segments. → *Expect:* a refund confirmation number or email.
6. **Save the refund terms.** Screenshot the submitted amount, ticket numbers, and promised timeline. → *Expect:* evidence for follow-up or chargeback.
7. **Track the payment method.** Check card, bank, wallet, or agency balance until the refund posts. → *Expect:* a posted credit or a missed deadline.
8. **Escalate nonpayment.** Contact the seller with the case number; if still unresolved, complain to the aviation regulator and consider a card dispute for services not provided. → *Expect:* an escalation reference, dispute case, or refund release.

## Decision points

- You booked through an agency → request from the agency first, but cite the airline cancellation evidence.
- Partial itinerary was flown → claim only unused segments and unused ancillary services.
- Airline offers a bonus voucher → compare expiration, restrictions, and insolvency risk against cash.
- Refund deadline passes → escalate before card-dispute time limits expire.

## Failure modes & recovery

- **F1 Voucher accepted accidentally:** detect a credit issued instead of cash → immediately ask to reverse acceptance if the click was ambiguous or unlawful.
- **F2 Refund sent to closed card:** detect credit to an old account → contact the card issuer; issuers usually route credits to the replacement account or issue a check.
- **F3 Agency blames airline and airline blames agency:** detect circular denial → use the receipt merchant, ticket number, and regulator complaint to force ownership.
- **F4 Only taxes refunded:** detect missing base fare or fees → resubmit with cancellation proof and itemized receipt.
- **F5 Chargeback filed too early:** detect open refund still within promised window → wait unless the deadline is near, then dispute with documentation.

## Verification

The original payment method or agreed account shows a posted refund for the unused ticket value and eligible ancillary fees, with no replacement booking accepted.

## Variations

- `us`: cancelled flights generally entitle passengers to a refund if they choose not to travel or accept credits.
- `eu`: reimbursement or rerouting is generally owed for covered cancellations, with separate compensation possible depending on notice and cause.
- `package holiday`: the package organizer may owe the refund even when the airline operated part of the trip.

## Safety & privacy

Medium risk from money and identity data. Avoid unofficial "refund help" links in texts or emails, and do not surrender cash rights for a restricted credit without explicit confirmation.
