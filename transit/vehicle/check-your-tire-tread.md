---
name: check-your-tire-tread
domain: transit
subdomain: vehicle
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You determine whether each tire has enough tread and even wear to keep driving safely or needs inspection or replacement.

## Preconditions

- The vehicle is parked on level ground, in park, with parking brake set.
- Tires are cool enough to touch and visible around the vehicle.
- You have a tread-depth gauge or a local coin test suitable for your country.

## Steps

1. **Inspect all four tires visually.** Look for cords, bulges, cracks, nails, cuts, uneven shoulders, and low-looking tires. → *Expect:* obvious damage is found or ruled out before measuring.
2. **Measure tread in three channels per tire.** Use a tread-depth gauge at inner, center, and outer grooves, avoiding raised wear bars. → *Expect:* each tire has recorded tread depths across its width.
3. **Compare to legal and safe limits.** Many places set a legal minimum near 2/32 inch or 1.6 mm, but wet-weather grip declines before that. → *Expect:* each tire is classified as healthy, near replacement, or unsafe.
4. **Check the wear bars.** Look for rubber bars running across grooves; if they are flush with tread, the tire is at minimum depth. → *Expect:* wear-bar status agrees with the measurement.
5. **Look for uneven patterns.** Inner-edge wear, cupping, one-sided wear, or center-only wear may indicate alignment, suspension, or inflation problems. → *Expect:* abnormal wear is documented with photos if present.
6. **Repeat after turning the front wheels if needed.** Turn the steering wheel while parked to expose the inside edges of front tires. → *Expect:* hidden inner shoulders have been checked.
7. **Plan service if needed.** [BRANCH: tire at or below legal limit, replace promptly | uneven or damaged tire, schedule inspection | all tires healthy, recheck monthly] → *Expect:* there is a clear next action for each tire.

## Decision points

- Any cord, bulge, sidewall crack, or rapid air loss → do not rely on tread depth; replace or tow as needed.
- One tire much more worn than the matching tire → inspect alignment, suspension, and inflation.
- Winter driving expected → replace earlier if tread is shallow; winter traction needs deeper tread than dry pavement.

## Failure modes & recovery

- **F1 Gauge reads inconsistently:** detect large differences from repeated measurements in the same groove → reseat the gauge flat and measure again.
- **F2 Coin test ambiguous:** detect uncertainty about the visible mark → use a real tread-depth gauge or tire shop measurement.
- **F3 Hidden inner-edge wear:** detect outer tread looks fine but steering vibration or pull exists → turn wheels and inspect the inner shoulders.
- **F4 Tire shop recommends replacement:** detect a recommendation without measurements → ask for tread depth, date code, damage location, and whether replacement should be axle-paired.

## Verification

Each tire has a recorded tread-depth reading for inner, center, and outer grooves, and any tire at the limit, damaged, or unevenly worn has a replacement or inspection plan.

## Variations

- `us`: common minimum is 2/32 inch; tire shops and gauges often report in 32nds of an inch.
- `eu-uk`: common minimum is 1.6 mm across required tread areas; rules vary by vehicle class.
- All-wheel drive: some manufacturers require matched tread depth across all tires; check the owner's manual before replacing only one.

## Safety & privacy

Medium risk because poor tread affects braking and hydroplaning. Confirm damage and low tread before long trips, and do not drive at highway speeds on a tire showing cord, bulges, or sidewall failure.
