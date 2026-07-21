---
name: plan-a-multi-leg-journey
domain: transit
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Plan a journey with two or more legs so the timing, tickets, transfers, and backup option are clear before departure.

## Preconditions

- You know the origin, destination, date, earliest departure, and latest acceptable arrival.
- You can access a journey planner, agency timetable, or map.
- You have a payment method accepted by each operator.

## Steps

1. **Enter the full door-to-door trip.** Use a journey planner with the exact date and time, including walking start and end points. → *Expect:* at least two candidate itineraries appear.
2. **Inspect each leg.** Note mode, line, direction, platform or stop, departure time, and arrival time. → *Expect:* every leg has a concrete boarding point and time.
3. **Check transfer buffers.** Compare each transfer time with walking distance, station complexity, crowds, and delay risk. → *Expect:* each handoff has a buffer you could actually make.
4. **Compare ticket structure.** [BRANCH: single through ticket | separate tickets] check whether one fare protects the connection or each leg is independent. → *Expect:* you know who is responsible if an early leg is late.
5. **Price the full trip.** Add fares, reservation fees, luggage fees, and any peak surcharges. → *Expect:* the total cost is known before purchase.
6. **Choose the itinerary.** Prefer the option that meets arrival needs with realistic transfers, not only the shortest app estimate. → *Expect:* one primary journey is selected.
7. **Pick a backup.** Identify a later connection, alternate route, taxi segment, or overnight fallback before leaving. → *Expect:* there is a named plan if one leg fails.
8. **Buy or reserve carefully.** Purchase required tickets and reservations only after checking date, direction, passenger count, and transfer stations. ⚠️ *Irreversible:* nonrefundable tickets may lock the route, so confirm every leg before paying. → *Expect:* confirmations or tickets are saved.
9. **Create a trip sheet.** Save offline screenshots with times, ticket references, station maps, and support contacts. → *Expect:* you can navigate even with weak signal.

## Decision points

- Transfer is under 10 minutes in an unfamiliar station → choose an earlier first leg or a later connection.
- Separate tickets are much cheaper → accept them only if you can absorb missed-connection costs.
- Last leg is the final service of the day → add a larger buffer or choose an earlier departure.
- Mobility, luggage, or children slow walking → increase every transfer buffer before buying.

## Failure modes & recovery

- **F1 Missed connection:** detect arrival after the next leg closes boarding, recover by using the backup or asking the operator about rebooking rights.
- **F2 Ticket not valid on operator:** detect scanner rejection or fare notice, recover by buying the correct segment and saving proof for a refund request.
- **F3 Planner hides walking time:** detect a transfer that requires crossing streets or terminals, recover by checking station maps and adding walking buffer.
- **F4 Service disruption:** detect cancellation or severe delay alert, recover by switching to the preselected alternate route.
- **F5 Dead phone:** detect low battery before boarding, recover by printing tickets or saving them to a second device.

## Verification

You have a primary itinerary with every leg, transfer buffer, fare or ticket rule, confirmation, and backup option saved offline.

## Variations

- Intercity rail: seat reservations and missed-connection protection depend on ticket type.
- Airport transfer: include security, bag claim, and terminal change time.
- Rural bus: check return service before committing, since gaps can be hours.
- Cross-border route: allow time for passport checks and ticket inspections.

## Safety & privacy

Medium risk from missed paid travel and late arrival. Keep ticket barcodes private, share your itinerary only with trusted contacts, and avoid tight late-night transfers in unfamiliar areas.
