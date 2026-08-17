---
name: book-a-multi-city-trip
domain: travel
locale: [generic]
interface: web
difficulty: advanced
est_time: 2h
risk: high
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Book a multi-city itinerary whose flights, ground transfers, dates, baggage rules, and connection protections work as one coherent trip.

## Preconditions

- You know the fixed cities, flexible cities, earliest departure, latest return, passport names, visa needs, and baggage requirements.
- You can compare airline multi-city search, one-way tickets, trains, and open-jaw options.
- You have a payment method and enough time to review every date and airport code before purchase.

## Steps

1. **Map the trip as segments.** Write each city pair, travel date, airport options, and must-arrive-by commitment in a list. → *Expect:* every movement between overnight cities has an assigned transport need.
2. **Price the protected version first.** Search the airline or alliance multi-city tool for flights on one ticket where missed connections would be protected. → *Expect:* you know the price and schedule for the low-risk baseline.
3. **Compare separate tickets deliberately.** Price one-ways, trains, and low-cost carriers, adding baggage, airport transfers, and overnight buffers. → *Expect:* any savings are visible after real fees and buffer costs.
4. **Check airport and visa traps.** Confirm airport changes within cities, Schengen or transit visa implications, overnight layovers, and minimum connection times. → *Expect:* no segment depends on an impossible terminal change or illegal transit.
5. **Build the calendar before paying.** Put each flight or train in local time with airport codes, hotel nights, and transfer windows. → *Expect:* date-line shifts, red-eyes, and missing hotel nights are visible.
6. **Review and purchase segment by segment.** Match traveler names to passports, verify baggage, seat needs, and refund/change rules, then pay only after the full route still works. → *Expect:* confirmations exist for all paid segments and none conflict.
7. **Store the master itinerary.** Save booking references, ticket numbers, train PNRs, hotel nights, and emergency alternates in one offline note. → *Expect:* the trip can be reconstructed without email search or data service.

## Decision points

- Separate tickets save little → book one protected itinerary because disruption handling is worth the price.
- Separate tickets save a lot → add an overnight or large buffer before any self-connection.
- Low-cost airport is far from the city → include transfer time and cost before choosing it.
- Checked bags needed → avoid tight self-connections where you must reclaim and recheck luggage.

## Failure modes & recovery

- **F1 Date-line error:** arrival appears before departure or hotel nights do not line up → rebuild the calendar in local time and correct the segment before purchase.
- **F2 Airport swap:** itinerary lands at one airport and departs another → add a transfer buffer or choose a same-airport route.
- **F3 Self-connection missed:** first carrier delay breaks the next separate ticket → contact the onward carrier quickly, use travel insurance if covered, and buy the next viable segment.
- **F4 Baggage fee surprise:** low fare excludes checked or cabin bags → reprice with bags and change the ticket before the airport if still cheaper.

## Verification

Every city-to-city movement has a confirmation, local-time calendar entry, baggage plan, and legal transit path, and all names and dates match the passport and intended route.

## Variations

- Open-jaw trips: fly into one city and home from another when backtracking costs more than the fare difference.
- Rail-friendly regions: trains can replace short flights and reduce airport-transfer time.
- Award bookings: saver availability may require splitting tickets, so buffers and backup flights matter more.

## Safety & privacy

High risk because multiple nonrefundable purchases can fail together. Keep passport data inside airline or rail systems, avoid sharing the full itinerary publicly, and confirm each payment screen before committing.
