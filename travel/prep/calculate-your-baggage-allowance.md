---
name: calculate-your-baggage-allowance
domain: travel
subdomain: prep
locale: [generic]
interface: web
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You determine exactly what luggage you can bring, what it will cost, and which airline's rules apply before arriving at the airport.

## Preconditions

- Full itinerary, ticket confirmation, fare class, loyalty status, and operating airlines.
- Bag dimensions and estimated packed weights.
- Airline baggage pages or booking-management portal.

## Steps

1. **Identify every operating airline.** Check the itinerary for the airline actually flying each segment, not just the marketing carrier. → *Expect:* you know which carriers may apply baggage rules.
2. **Find the fare and cabin rules.** Look up the ticket's cabin, fare family, route, and whether bags were included or prepaid. → *Expect:* the base allowance is clear for carry-on, personal item, and checked bags.
3. **Check route-specific exceptions.** International, basic economy, island, regional, partner, and government-regulated routes can differ. → *Expect:* the allowance reflects the actual origin and destination.
4. **Measure and weigh each bag.** Include wheels, handles, packed contents, and any expansion. → *Expect:* each bag's dimensions and weight are known.
5. **Apply status, card, or bundle benefits.** Confirm whether loyalty status, credit card, military, student, or fare bundle benefits apply to this ticket. → *Expect:* any free-bag benefit is documented and not assumed.
6. **Calculate total fees.** Add first bag, second bag, overweight, oversized, sports-equipment, and special-item fees for each direction. → *Expect:* you know the likely airport or prepaid cost.
7. **Save the evidence.** Screenshot the allowance page, booking baggage screen, and prepaid receipt if you pay in advance. → *Expect:* proof is available if airport staff see different information.
8. **Repack to fit the rules.** Move items between bags or reduce contents before airport arrival. → *Expect:* bags fit the chosen allowance and avoid surprise fees where possible.

## Decision points

- Multiple airlines on one ticket → use the airline baggage rule shown on the ticket and confirm with the operating carrier if unclear.
- Separate tickets → each ticket may have its own allowance and bag fees.
- Basic economy or low-cost carrier → assume stricter carry-on rules until confirmed.
- Bag is near the limit → reduce weight at home because airport scales and sizers control acceptance.

## Failure modes & recovery

- **F1 Allowance page conflicts with booking:** detect different bag counts or weights → contact the airline and save the written answer.
- **F2 Airport charges unexpected fee:** detect staff applying a different rule → show screenshots and receipt; pay under protest if needed to travel and request refund later.
- **F3 Bag exceeds weight:** detect overweight at check-in → move items, buy another bag allowance, or pay overweight fee.
- **F4 Partner airline refuses benefit:** detect loyalty or card benefit not honored → confirm whether the benefit applies only to specific operating carriers.

## Verification

For each traveler and direction, you have a documented carry-on, personal-item, checked-bag, weight, size, and fee allowance matching the operating airline and fare.

## Variations

- `us-domestic`: credit-card free-bag benefits often require booking with the card and apply only to that airline's flights.
- `international`: baggage may use piece concept or weight concept depending on carrier and route.
- `low-cost-carrier`: cabin bags may be paid add-ons and personal-item dimensions can be strictly enforced.

## Safety & privacy

Medium risk because baggage mistakes can cost money or strand essential items. Keep documents, medication, valuables, lithium batteries, and irreplaceable items in your personal item regardless of allowance.
