---
name: compare-total-trip-cost
domain: travel
subdomain: booking
locale: [generic]
interface: web
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You choose between travel options using total trip cost, not isolated flight, hotel, or car prices.

## Preconditions

- Candidate destinations or itineraries, dates, travelers, and required comfort level.
- Budget cap and decision criteria such as time, refundability, and location.
- Access to booking sites, maps, and card or loyalty benefit details.

## Steps

1. **Create comparable options.** Define each option with the same traveler count, trip length, baggage needs, and lodging standard. → *Expect:* a like-for-like set of alternatives.
2. **Price transportation door to door.** Include flights, trains, baggage, seats, transfers, parking, tolls, fuel, rideshares, and extra travel time. → *Expect:* transportation total for each option.
3. **Price lodging all-in.** Include nightly rate, taxes, resort fees, cleaning fees, deposits, breakfast, parking, and location-related transit costs. → *Expect:* lodging total for each option.
4. **Add activity and food differences.** Estimate mandatory tickets, local meal costs, groceries, childcare, pet care, and seasonal surcharges. → *Expect:* destination-specific daily cost estimate.
5. **Account for points and credits conservatively.** Value points at realistic cash savings, include fees, and subtract expiring credits only if they would otherwise go unused. → *Expect:* net cash cost and separate points cost.
6. **Score flexibility and risk.** Note refundable deadlines, change fees, weather risk, visa risk, and connection risk. → *Expect:* a non-price risk note for every option.
7. **Compare against the cap.** Rank options by all-in cash cost, points used, time burden, and cancellation exposure. → *Expect:* one preferred option and at least one backup.
8. **Save the evidence before booking.** Keep screenshots or a simple spreadsheet with final checkout totals. → *Expect:* a decision record that can be checked after purchase.

## Decision points

- Cheapest option consumes much more time → decide whether the savings justify lost hours.
- Option relies on nonrefundable bookings → keep a refundable backup or require larger savings.
- Points redemption saves little cash → preserve points and pay cash.
- Destination costs differ sharply → a cheap flight may lose to a pricier flight with cheaper lodging.

## Failure modes & recovery

- **F1 Search-result teaser price:** detect final checkout is higher → update the comparison with checkout total only.
- **F2 Missing local transport:** detect remote hotel requires expensive rides → add daily transport or choose a better location.
- **F3 Currency mismatch:** detect prices in different currencies → convert using a realistic card rate and include foreign transaction fees.
- **F4 Points overvalued:** detect redemption still requires high fees → compare to cash fare and use a conservative cents-per-point value.

## Verification

A saved comparison shows each viable option's all-in cash cost, points cost, flexibility deadlines, and the selected option is within the stated budget cap.

## Variations

- `family-travel`: baggage, room occupancy, food, and transport scale nonlinearly with children.
- `international`: visas, roaming, foreign transaction fees, and airport transfers matter more.
- `road-trip`: fuel, parking, tolls, mileage wear, and overnight stops replace airfare.

## Safety & privacy

Medium risk because booking decisions involve substantial money. Avoid storing full card numbers in comparison notes and verify totals directly on trusted checkout pages.
