---
name: board-a-bus-with-a-mobility-aid
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 5min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [bus, mobility-aid, ramp, curb, fare-card, priority-area]
affordances: [wait, signal, ramp-cross, brake-lock, fare-tap, position-hold]
workspace: bus-stop
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: pause}
---

## Goal

Board a bus while using a wheelchair, walker, scooter, cane, or similar mobility aid, then settle in a safe riding position.

## Preconditions

- The bus route and direction match the intended trip.
- The mobility aid is under control and fits the doorway or ramp.
- Fare media or proof of payment is ready if required.

## Steps

1. **Wait in the boarding zone.** Position where the driver can see the mobility aid without blocking exiting passengers. → *Expect:* the bus can stop with the front or accessible door near you.
2. **Signal the driver.** Raise a hand, make eye contact, or move toward the marked accessible boarding point. → *Expect:* the driver stops and prepares the kneeling bus, ramp, or lift if needed.
3. **Let passengers exit first.** Hold position until the doorway and ramp path are clear. → *Expect:* no one is crossing the threshold toward you.
4. **Align with the ramp or step.** Face straight toward the entry path and keep wheels, cane tip, or walker feet centered. → *Expect:* the aid is square to the ramp or first step.
5. **Board at controlled speed.** [BRANCH: ramp | no ramp] use the ramp slowly, or step up only if the aid and body can clear the step safely. → *Expect:* all wheels, feet, and carried items are inside the bus.
6. **Pay or confirm fare.** Tap the card, show pass, or follow the driver's instruction before moving deeper into the bus. → *Expect:* fare reader or driver indicates acceptance.
7. **Move to the secure area.** Take the shortest clear path to a priority seat, securement area, or open standing space. → *Expect:* the aid is out of the aisle as much as possible.
8. **Stabilize for travel.** Lock brakes, hold a rail, sit if appropriate, and accept securement straps when required. ⚠️ *Irreversible:* bus motion can begin before balance is recovered; confirm the body and aid are stable before releasing support. → *Expect:* the bus can move without the aid rolling or tipping.

## Decision points

- Ramp or lift is unavailable → do not force boarding; ask for the next accessible bus or alternate transport.
- Bus is too crowded to reach a safe area → wait for space, ask the driver for help, or skip this bus.
- Driver requests rear-door boarding → follow only if the accessible path is clear and fare rules permit it.
- Mobility aid snags on threshold → stop and reverse slightly before trying a straighter alignment.

## Failure modes & recovery

- **F1 Ramp gap:** detect a wheel, walker foot, or cane tip dropping into a gap → stop, back up if stable, and ask the driver to adjust the ramp.
- **F2 Aid rolls during fare payment:** detect unintended movement → lock brakes or brace against a rail before continuing.
- **F3 Passenger crowding:** detect blocked doorway or aisle → pause and ask for space instead of pushing through.
- **F4 Wrong bus:** detect route number or destination mismatch → step back before boarding or exit before the bus departs.

## Verification

The rider and mobility aid are fully inside the correct bus, fare is accepted or acknowledged, and the rider is seated, secured, or braced outside the doorway and main aisle.

## Variations

- Low-floor bus: kneeling and ramp deployment may replace lift boarding.
- Paratransit vehicle: driver securement and seatbelt steps are mandatory before travel.
- Cane user: use the handrail and step only when both feet can clear the threshold without rushing.

## Safety & privacy

Medium risk from vehicle movement, pinch points, and crowding. Pause around people entering or exiting, keep brakes locked when stationary, and do not announce disability or destination details louder than needed.
