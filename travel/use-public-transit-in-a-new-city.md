---
name: use-public-transit-in-a-new-city
domain: travel
locale: [generic]
interface: mixed
difficulty: basic
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Use buses, trains, trams, or metros in an unfamiliar city with the right map, fare, validation method, timing, and basic safety habits.

## Preconditions

- You know your lodging address and at least one destination.
- You have a charged phone or printed map.
- You have local currency, a payment card, or the city's transit app available.

## Steps

1. **Get the official map or app.** Download the transit agency app or save the route map from the agency website. → *Expect:* you can identify nearby stops and major lines.
2. **Locate your nearest stop.** Find the stop name, direction, and walking route from your lodging. → *Expect:* you can reach the correct platform or curb without guessing.
3. **Choose a fare product.** [BRANCH: single ride | day pass | stored value] compare your planned rides with pass cost and transfer rules. → *Expect:* the chosen fare covers the expected trips.
4. **Learn validation rules.** Check whether you must tap in, tap out, stamp a paper ticket, scan a code, or carry proof of payment. → *Expect:* you know what makes the fare valid before boarding.
5. **Buy from an official source.** Use a station machine, staffed counter, agency app, or accepted contactless card. → *Expect:* ticket, pass, or payment method is ready before travel.
6. **Plan around peak times.** Check whether rush hour crowding, limited luggage space, or reduced late-night service affects the trip. → *Expect:* departure time accounts for crowding and service frequency.
7. **Board in the correct direction.** Match the platform or stop sign to the line endpoint and destination sequence. → *Expect:* the next vehicle is going toward your destination.
8. **Validate before or at boarding.** Complete the required tap, stamp, or scan. ⚠️ *Irreversible:* inspectors may fine invalid tickets even if you paid, so validate before sitting down. → *Expect:* the reader, stamp, or app shows a valid ride.
9. **Monitor your stop.** Follow the route on the map and move toward the exit one stop early. → *Expect:* you exit at the planned stop without rushing.

## Decision points

- You will ride three or more times in a day → a day pass may beat single fares.
- Ticket machines are confusing or only local language → use the official app or staffed counter if available.
- Area feels unsafe late at night → choose a busier route, licensed taxi, or rideshare instead.
- Luggage is large → avoid peak times and check whether airport or express services handle bags better.

## Failure modes & recovery

- **F1 Unvalidated ticket:** detect no timestamp, beep, or app activation, recover by validating immediately before inspection.
- **F2 Wrong direction:** detect stops counting away from destination, recover by exiting at the next safe stop and crossing to the opposite direction.
- **F3 Pass not accepted:** detect reader rejection, recover by checking zone, operator, and pass activation status.
- **F4 Last service missed:** detect no more departures, recover by using the saved backup taxi or night bus route.
- **F5 Pickpocket risk:** detect crowding or distraction, recover by moving valuables to a closed front pocket or bag.

## Verification

You completed the ride on the intended line, with a valid fare, correct stop exit, and no fare inspection or safety issue.

## Variations

- Proof-of-payment systems: there may be no gate, but inspectors can check tickets anywhere.
- Zone fares: airport and suburban trips may cost more than central rides.
- Contactless cities: one card per person is often required for caps and transfers.
- Cash buses: exact fare may be required and drivers may not make change.

## Safety & privacy

Medium risk from fines, theft, and getting stranded. Use official fare channels, keep valuables controlled in crowds, and avoid sharing live travel plans publicly.
