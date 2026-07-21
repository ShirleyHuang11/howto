---
name: book-a-flight
domain: travel
locale: [generic]
interface: web
difficulty: intermediate
est_time: 1h
risk: high
prerequisites: [accounts/log-in, have-payment-method]
status: draft
last_verified: 2026-07-20
---

## Goal

A flight is booked for the right person, dates, and route, at an acceptable price, with the confirmation and ticket number in hand.

## Preconditions

- Trip parameters: origin, destination, dates (or date flexibility), passenger count.
- Each traveler's name **exactly as printed on the passport/ID** — this is the detail that voids tickets.
- Passport validity for international trips (many countries require 6 months beyond travel) and visa awareness for the destination.
- A payment card; ideally one with travel protections.

## Steps

1. **Search broad first.** A meta-search (flexible-dates view on) across the route: see the price landscape by day and carrier. → *Expect:* you know the cheap days, typical price, and which airlines fly it.
2. **Select a candidate itinerary and scrutinize it.** Layover length (90 min+ for international connections; tight domestic connections fail on any delay), airport changes within a city (a trap), arrival time vs. your ground plans, and the *fare class's* baggage and change rules. → *Expect:* an itinerary you'd accept even on a mildly bad day, with known bag allowance.
3. **Price the same itinerary on the airline's own site.** Often equal or near it — and booking direct makes every future change/cancellation far easier than through an intermediary. → *Expect:* a direct price within a few dollars of the meta-search; if the OTA is dramatically cheaper, read its change-policy fine print before being tempted.
4. **Enter passenger details against the passport, character by character.** Name spelling, birth date, passport number where asked. ⚠️ *Irreversible:* name errors can mean denied boarding or paid correction — verify each field against the physical document, not memory. → *Expect:* details matching the document exactly.
5. **Decline or accept extras deliberately.** Seats, bags, insurance — priced à la carte. Add checked bags *now* if you'll need them (airport prices are punitive); skip seat fees on couples-who-can-sit-apart; consider insurance only if you understand what it actually covers. → *Expect:* extras chosen on purpose, not by default checkbox.
6. **Review the final screen fully, then pay.** Route, dates, times (AM/PM!), passengers, total. ⚠️ *Irreversible:* most cheap fares are nonrefundable past the cooling-off window — this screen is the commitment. → *Expect:* payment accepted; confirmation page with a booking reference (PNR).
7. **Capture the confirmation.** Email with PNR and the 13-digit e-ticket number saved; add flights to your calendar with the airport and terminal. → *Expect:* booking retrievable on the airline's site with PNR + name (test it once now).

## Decision points

- 24-hour cooling-off (`us` bookings and many others) → mistakes found today are free to fix: re-check everything within the window.
- Basic-economy vs. standard fare gap is small → the flexibility and bag inclusion usually earn it back on any trip with a suitcase.
- One-way pairs vs. round-trip → price both; on many routes two one-ways cost the same and halve change fees.

## Failure modes & recovery

- **F1 Price jumped at checkout:** the fare bucket sold out mid-session — accept the new price or restart the search; "waiting it out" resolves either way, and calendars help you not chase.
- **F2 Typo discovered after booking:** inside 24 h → cancel/rebook or free-correct (call the airline now); outside → airlines correct minor misspellings, usually by phone, sometimes for a fee — do it well before travel.
- **F3 Confirmation email never arrived but card was charged:** retrieve by PNR/name on the airline site (step 7's test); no PNR anywhere + a charge → call the airline with the charge details before rebooking, or you'll own two tickets.
- **F4 Schedule change email later ("your flight moved 5 hours"):** significant changes entitle you to free rebooking or refund — reply to the options promptly; ignoring them accepts the new times.

## Verification

The booking retrieves on the airline's own site showing correct names, route, and dates; the e-ticket number is saved; bags you'll need are attached to the fare; and the calendar holds the flights with times cross-checked AM/PM.

## Variations

- Points/miles bookings: same verification discipline; taxes still hit a card, and award seats have their own change rules.
- Multi-city trips: book as one multi-city itinerary when a delay on leg one must protect leg two; separate tickets carry no such protection.

## Safety & privacy

High risk is financial: nonrefundable money against exact-match identity documents. The two ⚠️ checks (passport-exact names, final-screen review) plus booking direct are where the risk is spent or saved. Passport numbers only go into airline/government forms — never "visa help" sites you didn't independently verify.
