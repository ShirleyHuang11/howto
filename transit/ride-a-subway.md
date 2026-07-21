---
name: ride-a-subway
domain: transit
locale: [generic, us-nyc, jp-tokyo, cn-beijing]
interface: physical
difficulty: basic
est_time: 30min
risk: low
prerequisites: [have-payment-method, know-destination]
status: draft
last_verified: 2026-07-20
---

## Goal

Travel from your current location to a destination using the local subway/metro system.

## Preconditions

- A destination station or address is known.
- A payment method the local system accepts: contactless bank card, transit card, transit app, or cash for ticket machines.

## Steps

1. **Plan the route.** Use a maps app or the station's route map: identify boarding station, line, direction (by terminus), any transfers, and exit station. → *Expect:* a written/remembered plan: "Line X toward Terminus Y, change at Z, exit at W."
2. **Find and enter the nearest station.** Look for the system's logo/signage at street level. → *Expect:* you are in a station hall with fare gates and a system map that shows your planned line.
3. **Obtain or validate fare.** [BRANCH: tap-to-pay bank card | transit card with balance | ticket machine | transit app QR] At a machine: select destination or fare type, pay, take the ticket/card. ⚠️ *Irreversible:* multi-day passes and non-refundable tickets — confirm fare type before paying. → *Expect:* you hold a valid fare medium for this trip.
4. **Pass the fare gate.** Tap or insert; walk through on green/open. → *Expect:* gate opens and (on card systems) displays balance or fare; if rejected, F1.
5. **Navigate to the correct platform.** Follow signs for your line *and direction* (terminus name from step 1). → *Expect:* platform signage lists your destination or the correct terminus.
6. **Board the train.** Let passengers exit first; move inside the car. → *Expect:* the in-car line map matches your line; next-station announcements begin.
7. **Monitor stops and transfer if planned.** At a transfer, follow the connecting line's signs (repeat step 5). → *Expect:* each announced station matches your route plan in sequence.
8. **Exit at the destination station.** Leave the train, follow Exit/Way Out signs, tap out where the system requires it. → *Expect:* fare gate opens on tap-out (distance-fare systems) and you reach street level near the target address.

## Decision points

- Line suspended or station closed → check posted service notices; reroute via the maps app or fall back to a bus.
- Distance-based system and you bought too cheap a ticket → use a fare-adjustment machine near the exit gates before tapping out.
- Last train of the night is near → verify the timetable before entering the paid area.

## Failure modes & recovery

- **F1 Fare rejected at gate:** try an adjacent gate; insufficient balance → top up at a machine; foreign card rejected → buy a single ticket; else ask station staff.
- **F2 Boarded the wrong direction:** exit at the next station, cross to the opposite platform (may require staying inside the paid area — follow signs), reverse.
- **F3 Missed the stop:** stay calm, exit at the next station, take the return train one stop.
- **F4 Lost item on the train:** report to station staff immediately with car position and time; systems track train sets.

## Verification

You are at street level at the destination station, the exit signage names the street/landmark you targeted, and (on tap-out systems) the fare was deducted exactly once.

## Variations

- `us-nyc`: flat fare, OMNY contactless tap at every entry, no tap-out.
- `jp-tokyo`: distance-based fare; IC cards (Suica/Pasmo) tap in and out; fare-adjustment machines at exits; lines run by different operators may require passing through transfer gates.
- `cn-beijing`: security screening of bags at station entry precedes the fare gate; QR payment in the local transit app is dominant.

## Safety & privacy

Low risk. Keep belongings in front of you in crowds; stand behind the platform safety line; note the car number when traveling late at night.
