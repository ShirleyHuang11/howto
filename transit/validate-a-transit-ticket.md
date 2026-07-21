---
name: validate-a-transit-ticket
domain: transit
locale: [generic]
interface: physical
difficulty: basic
est_time: 3min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Activate a transit ticket correctly so it is valid for inspection until the trip is complete.

## Preconditions

- A paper ticket, smartcard, mobile ticket, or contactless payment card.
- You know the operator's rule for validating before boarding, onboard, or at the gate.
- The ticket is for the correct zone, route, date, or fare class.

## Steps

1. **Read the ticket instructions.** Look for "validate before boarding," "tap in," "stamp," "activate," or "not valid until." → *Expect:* you know whether action is required before travel.
2. **Find the validator.** [BRANCH: station | platform | onboard] look near entrances, platform ramps, bus doors, tram doors, or fare gates. → *Expect:* you can see a machine, gate reader, or app activation button.
3. **Validate before the required point.** If the system requires pre-boarding validation, do it before stepping onto the vehicle. → *Expect:* the ticket is active before inspection can occur.
4. **Insert, tap, scan, or activate.** Use the arrow direction for paper tickets, tap the card flat, scan the code, or press activate in the app. → *Expect:* the validator beeps, stamps, opens, or shows a green check.
5. **Check the confirmation.** Read the timestamp, zone, remaining rides, or app countdown. → *Expect:* the visible proof matches this trip.
6. **Handle transfer rules.** If transfers are included, note the expiration time or required tap-out. → *Expect:* you know whether another validation is needed later.
7. **Keep the ticket until exit.** Store paper or card where you can reach it for inspectors and exit gates. → *Expect:* proof of payment is available throughout the ride.
8. **Do not validate twice unless required.** Double stamping can consume another ride or start a new fare. → *Expect:* only the required ride or time window is used.
9. **Tap out if the system requires it.** [BRANCH: tap-out required | no tap-out] use the exit validator for distance fares; skip if flat fare rules say no. → *Expect:* fare is closed correctly and overcharges are avoided.
10. **Keep proof after leaving if needed.** Hold the receipt or used ticket until beyond the paid area. → *Expect:* a late inspection or exit check can still be answered.

## Decision points

- No validator is visible before boarding → ask staff or the driver before sitting down.
- Machine is broken → photograph the machine ID and use another validator if possible.
- Mobile ticket has an activation countdown → wait to activate until close to boarding, unless rules require earlier.
- Inspector says ticket is unvalidated → explain immediately and show evidence of machine failure if true.

## Failure modes & recovery

- **F1 Missed pre-boarding validation:** you boarded with an unstamped ticket, recover by finding onboard staff before inspection if available.
- **F2 Validator rejected ticket:** red light or error appears, recover by flipping ticket direction, trying another reader, or asking staff.
- **F3 Accidental double use:** second tap consumes fare, recover by saving receipts and requesting operator support.
- **F4 Ticket discarded early:** exit gate or inspector asks again, recover by using app history or payment record if accepted.

## Verification

The ticket, card, or app shows a current validated ride or open paid journey, and you still possess it until exiting the system.

## Variations

- Proof-of-payment systems: there may be no gate, but inspectors can fine unvalidated riders.
- Distance-based rail: tap-in and tap-out may both be required to calculate fare.
- Paper tram tickets: the machine may punch or print a timestamp instead of opening a gate.

## Safety & privacy

Medium risk because fines can exceed the fare. Keep payment cards secure, avoid blocking doors while validating, and do not discard proof until outside the paid area.
