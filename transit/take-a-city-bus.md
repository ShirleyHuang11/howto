---
name: take-a-city-bus
domain: transit
locale: [generic]
interface: physical
difficulty: basic
est_time: 40min
risk: low
prerequisites: [have-payment-method, know-destination]
status: draft
last_verified: 2026-07-20
---

## Goal

Travel to a destination on a scheduled city bus, boarding the right route in the right direction and alighting at the right stop.

## Preconditions

- Destination is known and served by a bus route.
- Accepted payment: transit card, contactless card, exact cash, or transit app (many systems don't give change).

## Steps

1. **Plan route and stop.** Maps app or posted route map: route number, boarding stop, direction (by terminus/major street), alighting stop, and expected arrival time of the next bus. → *Expect:* "Route N toward T, board at S1, alight at S2, next bus ~M min."
2. **Get to the boarding stop on the correct side of the street.** Direction of travel = side of the street; confirm the stop's sign lists your route number. → *Expect:* stop sign shows route N; the maps arrival estimate is counting down.
3. **Identify and hail your bus.** Read the headsign (route number + terminus) as the bus approaches; signal with a raised arm where hailing is customary. → *Expect:* the bus with your route number pulls in and opens its doors.
4. **Board and pay.** [BRANCH: tap card/phone at reader | coins in farebox | show driver a pass] Boarding door varies (front-door in most systems). → *Expect:* reader beeps/green light or driver nods; take a transfer slip if the system issues them.
5. **Take a seat or hold on; track your position.** Follow stops on the in-bus display or your maps app blue dot. → *Expect:* announced/displayed stops match your planned sequence.
6. **Request your stop.** One stop before yours, press the stop-request button or pull the cord. → *Expect:* "stop requested" light/chime turns on.
7. **Alight at the destination stop.** Exit via the rear door where customary; tap out if the system requires it. → *Expect:* you are at S2; street signs match the planned alighting point.

## Decision points

- Two branches share a route number → verify the headsign's terminus, not just the number.
- Bus is full and skips the stop → wait for the next; recheck arrival estimates.
- Night service replaces the day route → night routes renumber and reroute; re-plan rather than assuming.

## Failure modes & recovery

- **F1 Wrong direction:** alight at the next stop, cross the street, take the same route number back.
- **F2 Payment rejected and no alternative:** ask the driver — many systems let you ride and pay later, or a fellow rider may tap for cash; otherwise alight before departure.
- **F3 Missed your stop:** request the next stop, walk back or check if a return bus is faster.
- **F4 Bus never arrives:** check the operator's live status for detours/cancellations; re-plan via an alternate route or the subway.

## Verification

You are at the planned alighting stop (street signage matches), having paid exactly one fare, within roughly the planned travel time.

## Variations

- Rear-door boarding systems (some European cities): validate your ticket at machines inside the bus — inspectors fine unvalidated tickets.
- Flag-stop rural services: buses stop only when hailed; missing step 3 means the bus passes.

## Safety & privacy

Low risk. Hold handrails while the bus moves; keep bags on your lap, not the aisle; near-empty late-night buses — sit near the driver.
