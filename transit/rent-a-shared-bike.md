---
name: rent-a-shared-bike
domain: transit
locale: [generic]
interface: mixed
difficulty: basic
est_time: 30min
risk: medium
prerequisites: [have-payment-method]
status: draft
last_verified: 2026-07-20
---

## Goal

A shared bike (docked or dockless) is unlocked, ridden to your destination, and returned correctly, so the trip ends both physically and in the app.

## Preconditions

- The local system's app installed with payment set up, or a station kiosk that sells day passes.
- Basic riding competence and awareness of local cycling rules (which side, helmet law, whether sidewalks are legal).
- A destination within the system's coverage area. Check the app's map for stations or the dockless service zone before committing.

## Steps

1. **Find a bike and give it a twenty-second check before unlocking.** Tires firm, brakes grab when squeezed, saddle clamp holds, chain seated, no obvious damage. Skip a bad bike; there is always another. → *Expect:* a bike that passes all four checks. Report clearly broken ones in the app, which usually also flags them for others.
2. **Unlock through the app or kiosk.** Scan the QR code or enter the bike number; docked systems release with a click, dockless locks snap open. → *Expect:* the lock opens and the app shows an active trip with the meter running.
3. **Adjust the saddle before riding off.** Correct height puts your leg nearly straight at the pedal's bottom. One lever, two seconds, and it changes the whole ride. → *Expect:* comfortable extension on a test pedal.
4. **Ride by local rules, predictably.** Bike lanes where they exist, hand signals for turns, lights on at night (shared bikes have built-in lights that run automatically), and no phone in hand. `embodied/mobility/cross-a-street` logic applies at every junction, from the saddle. → *Expect:* steady progress; the app's map can wait for red lights.
5. **End the trip correctly. This is where the money leaks.** Docked: push the bike firmly into a dock until the light confirms, and check the app shows the trip closed. Dockless: park within the service zone in a legal spot (not blocking sidewalks, ramps, or doorways), close the lock, and confirm the app ended the trip. ⚠️ *Irreversible in effect:* an unclosed trip keeps billing for hours and an out-of-zone drop incurs fines. The confirmation screen is the actual end of the ride, not the kickstand. → *Expect:* app shows trip ended with a final price that matches expectations.
6. **Note the receipt.** Trip history keeps the record for any dispute. → *Expect:* one closed trip at the advertised rate.

## Decision points

- Full dock at your destination: the app shows nearby dock availability and most systems grant free overtime to reach an alternative when you tap the full-dock option. Use it rather than improvising.
- E-bike versions: same recipe, plus a battery-level check at step 1; a dead e-bike is a heavy bike.
- Helmet: bring your own where the law or your judgment says so. Some systems lend them; many riders reasonably decline shared helmets.
- Day pass vs per-ride: three or more short hops usually make the day pass cheaper. The math takes ten seconds at the kiosk screen.

## Failure modes & recovery

- **F1 Bike will not unlock after payment:** try once more, then pick another bike; the app refunds or support releases the failed hold. Do not wrestle the lock.
- **F2 Mechanical failure mid-ride:** stop safely, end the trip at the nearest legal spot, report the bike in the app, and unlock a replacement. The report usually waives the awkward short trip.
- **F3 Trip will not end (no dock light, app spinner):** re-seat the bike in a different dock, toggle the app, and if it still spins, contact support through the app immediately with the time and station. Screenshots of the stuck screen settle billing disputes.
- **F4 Fined for bad parking (dockless):** appeal with a photo if the spot was legal; otherwise pay it and update your mental map of the zone. Repeat fines usually mean the zone boundary is not where you think it is.

## Verification

The trip shows as closed in the app at the expected price, the bike is docked or legally parked with the lock engaged, and you arrived where you intended without traffic incident.

## Variations

- `cn` dockless fleets (Meituan, HelloBike class): QR unlock and zone parking at massive scale, with credit-score-like penalties for bad parking; `eu` docked systems (Vélib class) reward dock returns with pricing; `us` hybrid systems vary city by city.
- Cargo and child-seat variants exist in some systems and have their own tier in the app.

## Safety & privacy

Medium risk is traffic risk. The pre-ride check, saddle height, predictable riding, and phone-away rules carry it. The app records your trips, as with `transit/hail-a-rideshare`; check the privacy settings once if route history bothers you.
