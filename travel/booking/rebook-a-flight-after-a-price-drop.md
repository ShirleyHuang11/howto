---
name: rebook-a-flight-after-a-price-drop
domain: travel
subdomain: booking
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

You capture savings from a post-purchase fare drop by rebooking, changing, or canceling and repurchasing without losing the original trip.

## Preconditions

- Existing booking confirmation, ticket numbers, fare rules, and original total price.
- Current lower fare for the same or acceptable itinerary.
- Knowledge of cancellation, change-fee, travel-credit, and refund rules.

## Steps

1. **Confirm the current lower fare is real.** Search the same route, date, cabin, passengers, bags, and booking channel. → *Expect:* a bookable replacement fare below your original net cost.
2. **Read the original fare rules.** Check refundability, change fees, cancellation deadline, credit expiration, and whether basic economy is restricted. → *Expect:* you know the cost to change or cancel.
3. **Calculate net savings.** Subtract change fees, lost seat or bag fees, agency fees, and credit restrictions from the fare difference. → *Expect:* a positive savings amount or a decision not to proceed.
4. **Use the airline change/reprice tool first.** Try changing to the same flight or acceptable alternate at the lower price. → *Expect:* the tool displays refund, credit, or additional collection amount.
5. **If needed, hold or book the replacement before canceling.** [BRANCH: refundable or 24-hour-free-cancel replacement, book first | no free-cancel replacement, use same-session change path] → *Expect:* you do not lose the trip while trying to save money.
6. **Submit the change or cancellation only after review.** ⚠️ *Irreversible:* confirm passenger, flight, date, credit amount, refund method, and expiration before changing or canceling. → *Expect:* the airline issues a new confirmation, refund, or travel credit.
7. **Verify the new itinerary and funds.** Check ticketed status, seat assignments, bags, and refund or credit balance. → *Expect:* the lower-cost itinerary is active and savings are recorded.
8. **Cancel duplicate holds or alerts.** Remove any extra booking or price alert that could cause confusion. → *Expect:* only the intended itinerary remains active.

## Decision points

- Savings are issued only as travel credit → proceed only if you can use the credit before expiration.
- Seat or bag purchases do not transfer → include replacement costs in net savings.
- Original fare is basic economy → rebooking may be blocked or uneconomical.
- Booking was through an agency → agency fees and slower support may erase savings.

## Failure modes & recovery

- **F1 Fare disappears mid-change:** detect lower fare unavailable at final step → keep original booking and continue monitoring.
- **F2 Duplicate booking:** detect two active reservations for same traveler → cancel the unwanted one within the free window.
- **F3 Lost seat assignments:** detect seats removed after reissue → reselect seats or request refund for paid seats if not transferable.
- **F4 Credit expiration surprise:** detect short expiration on fare credit → calendar the deadline and use credit before it expires.

## Verification

The airline shows the intended active ticket, and the refund, credit, or lower reissued fare produces documented net savings after all fees and lost add-ons.

## Variations

- `us`: some airlines allow no-fee changes on many non-basic fares, but fare difference and credit rules vary.
- Award ticket: rebooking may redeposit miles or reduce mileage cost, with separate redeposit fees.

## Safety & privacy

Medium risk because cancellation or reissue can strand the traveler. Confirm the replacement itinerary and net savings before canceling the original, and keep all confirmation emails.
