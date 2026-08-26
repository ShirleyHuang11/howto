---
name: find-an-error-fare
domain: travel
subdomain: booking
locale: [generic]
interface: web
difficulty: advanced
est_time: 1h
risk: medium
prerequisites: [accounts/log-in, have-payment-method]
status: draft
last_verified: 2026-08-25
---

## Goal

You identify a likely error fare, book it quickly if it fits your constraints, and wait for ticketing confirmation before making nonrefundable plans.

## Preconditions

- Flexible travel dates, destination tolerance, passport or ID readiness, and payment method.
- A maximum price and a clear understanding that airlines may cancel obvious mistake fares.
- Ability to act quickly without ignoring visa, schedule, or safety requirements.

## Steps

1. **Monitor reputable fare-alert sources.** Use deal sites, fare newsletters, airline searches, and flexible-date tools. → *Expect:* a candidate fare far below normal market price.
2. **Validate the fare independently.** Search the same route and dates on the airline site and at least one comparison tool. → *Expect:* the low price appears on a bookable checkout path.
3. **Check trip feasibility quickly.** Verify dates, airports, baggage, visa or entry needs, overnight layovers, and total trip cost. → *Expect:* no non-price constraint makes the trip unacceptable.
4. **Book through the safest available channel.** Prefer airline-direct if the error fare is available there; otherwise use a reputable seller with clear cancellation terms. → *Expect:* checkout still shows the low all-in price.
5. **Purchase only within your risk cap.** ⚠️ *Irreversible:* confirm passenger names, dates, airports, and total charge before submitting, and accept that the fare may later be voided. → *Expect:* a booking confirmation and payment receipt.
6. **Wait for ticket numbers before planning further.** Do not book nonrefundable hotels, tours, or positioning flights until ticketed and stable. → *Expect:* the airline record shows ticket numbers or remains pending.
7. **Monitor for cancellation or schedule changes.** Check email and airline reservation status for several days. → *Expect:* the ticket remains active or the airline cancels and refunds it.
8. **Lock in dependent travel only after confirmation.** Once ticketed and not canceled, book lodging and related travel with compatible cancellation terms. → *Expect:* the broader trip plan no longer depends on an unconfirmed fare.

## Decision points

- Fare appears only through a questionable seller → skip unless the savings justify support and refund risk.
- Passport or visa requirements are uncertain → do not book until eligibility is clear.
- The itinerary requires separate positioning flights → wait before buying those flights.
- Airline cancels the mistake fare → accept refund unless local law or policy gives a clear appeal path.

## Failure modes & recovery

- **F1 Unticketed hold:** detect reservation code but no ticket number → contact the seller and avoid dependent purchases.
- **F2 Airline cancellation:** detect voided fare email → confirm refund to original payment method and restart search.
- **F3 Hidden trip cost:** detect expensive baggage, visa, or positioning needs → cancel within any free-cancellation window if total cost exceeds cap.
- **F4 Bad seller refund delay:** detect cancellation but no refund → open a support case and card dispute if the refund deadline passes.

## Verification

The booking has an airline ticket number for each traveler at the error-fare price, or if canceled the full charge has been refunded and no nonrefundable dependent travel was purchased.

## Variations

- `us`: airline-direct purchases may have a 24-hour cancellation option when booked sufficiently before departure.
- International: entry, transit, and passport validity rules can erase the value of a cheap fare.

## Safety & privacy

Medium risk because mistake fares can be canceled and payment is immediate. Do not buy nonrefundable add-ons until ticketing is confirmed, and avoid sellers with weak refund records.
