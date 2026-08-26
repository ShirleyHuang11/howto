---
name: respond-to-a-dashboard-warning-light
domain: transit
subdomain: vehicle
locale: [generic]
interface: mixed
difficulty: basic
est_time: 15min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You identify whether a dashboard warning means stop immediately, drive cautiously to service, or schedule routine maintenance.

## Preconditions

- The vehicle is running or in accessory mode and a warning light or message is visible.
- You can pull over safely if the light indicates an urgent condition.
- The owner's manual is in the vehicle or available online for the exact year, make, and model.

## Steps

1. **Note the color and symbol.** Red usually means stop or urgent safety issue; amber/yellow usually means service soon; green/blue usually indicates a system is active. → *Expect:* you have classified the warning's urgency.
2. **Reduce demand on the vehicle.** Turn off cruise control and avoid hard acceleration while you assess the warning. → *Expect:* the vehicle is being driven gently or is safely stopped.
3. **Pull over for red or flashing warnings.** [BRANCH: red oil pressure, brake, temperature, battery/charging, or flashing check-engine light, move to a safe stop | steady amber light, continue cautiously if the car behaves normally] → *Expect:* urgent warnings are handled from a safe stopped position.
4. **Read the exact message or manual entry.** Match the symbol and text to the owner's manual, not a generic icon chart alone. → *Expect:* you know the manufacturer's meaning and recommended action.
5. **Check obvious safe items.** If parked safely, check fuel cap tightness, visible low tire, coolant temperature gauge, or open door/trunk indicators without opening hot or moving parts. → *Expect:* simple causes are corrected or ruled out.
6. **Decide the next move.** [BRANCH: unsafe to drive, call roadside assistance | safe but needs service, book repair/diagnostic | routine reminder, schedule maintenance] → *Expect:* you have a specific action rather than ignoring the warning.
7. **Record the warning.** Photograph the light/message and note date, mileage, driving conditions, and symptoms. → *Expect:* you have information a mechanic or roadside provider can use.

## Decision points

- Flashing check-engine light → reduce speed and load, stop driving as soon as safe, and arrange service; it can indicate misfire damaging the catalytic converter.
- Oil pressure or overheating warning → stop promptly and shut off the engine when safe.
- Brake warning with soft pedal or poor stopping → do not continue driving; call for a tow.
- Tire pressure light steady → check pressures soon; if handling feels abnormal, stop immediately.

## Failure modes & recovery

- **F1 Unknown symbol:** detect a symbol you cannot identify → use the owner's manual or manufacturer's app by VIN/model before driving farther.
- **F2 Warning disappears:** detect the light turning off after restart → still record it and schedule diagnosis if it repeats or involved brakes, oil, temperature, or charging.
- **F3 Multiple warnings at once:** detect many lights after a battery or charging issue → treat it as potentially electrical and seek service instead of guessing each system failed.
- **F4 Vehicle enters limp mode:** detect reduced power or speed limit → move out of traffic and arrange service or towing.

## Verification

The warning has been matched to the owner's manual, urgent conditions have been stopped safely, and a repair, tow, or maintenance appointment is documented if required.

## Variations

- `ev`: high-voltage battery, propulsion, and charging warnings can require manufacturer-specific instructions; do not inspect orange high-voltage cables.
- `us`: OBD-II scanners can read many check-engine codes, but codes are diagnostic clues, not final repairs.
- Older vehicles: warning symbols may be less descriptive; the printed manual matters more.

## Safety & privacy

Medium risk because some warnings indicate immediate safety or engine-damage hazards. Confirm the warning type before deciding to continue, and avoid sharing VIN, location, or license plate publicly when asking for help online.
