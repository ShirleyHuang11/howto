---
name: ride-a-scooter-share
domain: transit
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [have-payment-method]
status: draft
last_verified: 2026-07-20
---

## Goal

A shared electric scooter is unlocked through the app, ridden safely by local road rules, and parked in a legal zone so the trip ends both physically and in the app with no lingering charge.

## Preconditions

- The operator's app installed with payment set up, and location plus camera permissions granted (the app needs both to unlock and to photograph the parked scooter).
- Legal riding age and, where required, a driver's license on file (some jurisdictions verify one before the first ride).
- Awareness of local rules: helmet law, whether sidewalk riding is banned, and the operator's service-zone map, which you should open before committing to a destination.

## Steps

1. **Open the app and check the scooter before unlocking.** Confirm battery range covers your trip, then squeeze the brake, wiggle the stem for looseness, and glance at the tires. A wobbly stem or dead battery is a different scooter's problem. → *Expect:* a scooter that brakes firmly with a stem that does not shift, and battery range comfortably above your distance.
2. **Scan to unlock.** Point the camera at the QR code on the handlebar or deck, or type the scooter ID. → *Expect:* a beep or light, an audible motor arm, and the app showing an active trip with the meter running.
3. **Fit a helmet if you have one.** Some operators clip a helmet to the scooter; many riders carry their own. → *Expect:* helmet on and strapped before you touch the throttle.
4. **Start moving with one deliberate kick.** These scooters need a manual push before the throttle engages, a safety feature to prevent lurching. Keep both hands on the bars. → *Expect:* the motor picks up smoothly after your first kick; no sudden jolt.
5. **Ride by local rules, predictably.** Use bike lanes or the road where the law directs (sidewalk riding is banned in most cities), signal turns, obey the speed cap the app enforces, and never carry a passenger. Slow zones on the map throttle you down automatically. → *Expect:* steady progress; the app may chime and cut speed in a geofenced slow zone.
6. **End the trip only in a legal parking zone.** This is where money and fines leak. Park upright on its stand, off the pedestrian path, not blocking ramps or doorways, inside the app's permitted zone. Then end the trip and take the required parking photo. ⚠️ *Irreversible in effect:* an out-of-zone or blocked-path parking triggers a fine, and a trip you never end keeps billing. → *Expect:* the app confirms the trip ended, accepts the photo, and shows a final price matching the distance and time.
7. **Confirm the receipt.** Check trip history for the closed ride and its charge. → *Expect:* one closed trip at the expected rate, no ongoing hold.

## Decision points

- Destination is outside the service zone: the motor will cut out at the boundary and you cannot end the trip there. Plan to park just inside the zone and walk the rest.
- No-parking zone at your destination (common near transit stations and plazas): the app refuses to end the trip. Move to the nearest permitted zone shown on the map.
- Helmet law in force and no helmet available: legally you should not ride. Choose another mode rather than risk the fine and the injury.

## Failure modes & recovery

- **F1 Scooter will not unlock after payment:** wait, retry the scan once, then pick another scooter. The failed hold is auto-refunded or released by support.
- **F2 Throttle dead or brake weak mid-ride:** brake to a stop safely, end the trip at the nearest legal spot, report the scooter in the app, and unlock a replacement. The report usually waives the short broken trip.
- **F3 App will not end the trip (spinner, photo rejected):** confirm you are in a parking zone, retake the photo in better light, toggle the app. If it still spins, contact support in-app with the time and a screenshot; that settles the billing.
- **F4 Fined for bad parking:** appeal with your own photo if the spot was legal; otherwise pay and recalibrate your read of the zone map, which is rarely where intuition puts it.

## Verification

The app shows the trip closed at the expected price with the parking photo accepted, the scooter stands upright in a legal zone off the pedestrian path, and you reached your destination without a traffic incident.

## Variations

- `eu` cities often cap speed at 20 to 25 km/h and mandate bike-lane use with steep sidewalk-riding fines; `us` systems vary by city, some requiring a scanned license; dense Asian megacities may restrict scooters to specific corridors entirely.
- Seated scooter and moped-style share variants exist in some fleets and add a helmet-in-topbox step and a license check.

## Safety & privacy

Medium risk is traffic and fall risk, worst at the start (the lurch) and on wet or gravel surfaces. Helmet, two hands, predictable lines, and a pre-ride brake check carry most of it. The app logs your route and holds a payment method, as with `transit/rent-a-shared-bike`; review location-history settings once if that bothers you.
