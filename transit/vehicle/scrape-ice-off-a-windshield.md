---
name: scrape-ice-off-a-windshield
domain: transit
subdomain: vehicle
locale: [generic]
interface: physical
difficulty: basic
est_time: 15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You remove ice and snow from the windshield and visibility areas without damaging glass, wipers, or paint.

## Preconditions

- Ice scraper and snow brush.
- Winter washer fluid in the reservoir.
- Vehicle is parked safely with exhaust area clear if the engine will run.

## Steps

1. **Clear the tailpipe first if starting the engine.** Remove snow around the exhaust outlet. → *Expect:* exhaust can vent safely.
2. **Start defrost if safe.** Turn on front and rear defrost, heat, and fan while staying with the vehicle. → *Expect:* glass begins warming from inside.
3. **Brush loose snow off the roof, hood, windows, lights, and mirrors.** → *Expect:* snow will not slide onto the windshield or blow into traffic.
4. **Lift wipers only if they are not frozen to the glass.** If stuck, warm them with defrost first. → *Expect:* wiper rubber is not torn.
5. **Scrape from the edges inward.** Use the plastic scraper flat against the glass, working in overlapping passes. → *Expect:* ice breaks loose without gouging trim.
6. **Use de-icer if needed.** Apply automotive de-icer or winter washer fluid; never pour hot water on cold glass. → *Expect:* stubborn ice softens without thermal shock.
7. **Clear all required visibility areas.** Finish windshield, front side windows, rear window, mirrors, lights, and license plate. → *Expect:* the vehicle is visible and the driver can see.
8. **Test wipers gently.** Run them only after ice is removed from the blade path. → *Expect:* wipers move freely and clear melted residue.

## Decision points

- Ice is thick and bonded → allow more defrost time and use de-icer rather than metal tools.
- Wipers are frozen down → free them gradually; do not yank the arms.
- Snow is heavy on roof → remove it before driving so it does not slide or fly off.

## Failure modes & recovery

- **F1 Scraper scratches trim:** keep the scraper on glass only and use a brush near paint or rubber.
- **F2 Wiper rubber tears:** replace the blade before driving in precipitation.
- **F3 Washer spray freezes:** switch to lower-temperature washer fluid after thawing lines.
- **F4 Interior fog forms:** use `transit/vehicle/defog-a-car-windshield`.

## Verification

Windshield, side windows, rear window, mirrors, lights, roof snow, and license plate are cleared enough for safe legal driving.

## Variations

- `ice-storm`: expect longer defrost time and use de-icer sparingly in layers.
- `heated-windshield`: use the vehicle's heated glass function but still scrape gently.
- `covered-parking`: use a windshield cover before storms to reduce scraping.

## Safety & privacy

Low risk, but blocked visibility and flying roof snow can cause crashes. Never use hot water on frozen glass, never use metal scrapers, and ensure the tailpipe is clear before idling.
