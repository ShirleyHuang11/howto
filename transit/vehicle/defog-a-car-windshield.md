---
name: defog-a-car-windshield
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

You clear interior fog from the windshield and keep visibility safe before and during driving.

## Preconditions

- The vehicle's blower works.
- You can safely stop or remain parked until visibility is adequate.
- Windows and vents are not blocked by objects.

## Steps

1. **Stop driving if visibility is poor.** Pull over safely or stay parked. → *Expect:* you are not driving blind.
2. **Turn on front defrost.** Select the windshield defrost mode and set fan speed high. → *Expect:* air is directed at the windshield.
3. **Use air conditioning if available.** Turn A/C on even in cool weather to dry the air. → *Expect:* fog begins shrinking as moisture is removed.
4. **Set temperature to warm for cold-weather fog.** Warm air holds more moisture and heats the glass. → *Expect:* the windshield clears from the defrost vents outward.
5. **Turn off recirculation.** Use fresh outside air unless outside conditions make it worse. → *Expect:* humid cabin air is replaced.
6. **Crack windows briefly if needed.** Open side windows slightly to equalize humidity. → *Expect:* fog clears faster.
7. **Clear remaining moisture gently.** Use a clean microfiber cloth only while stopped. → *Expect:* no film or smears block view.
8. **Keep settings active while driving.** Reduce fan speed only after the glass stays clear. → *Expect:* visibility remains stable.

## Decision points

- Fog is outside the glass → use wipers, washer fluid, and exterior defrost heat instead of wiping inside.
- Fog returns with recirculation on → switch back to fresh air.
- Windows fog when passengers enter wet → increase fan, use A/C, and crack windows.

## Failure modes & recovery

- **F1 Windshield smears after wiping:** clean interior glass with glass cleaner when parked.
- **F2 Defroster blows cold forever:** engine may not be warm, coolant may be low, or HVAC needs service.
- **F3 A/C button will not engage:** use fresh air, heat, high fan, and cracked windows; service the system later.
- **F4 Fog appears oily or sweet-smelling:** possible heater-core leak; stop using defrost and seek service.

## Verification

The windshield and front side windows are clear enough to see traffic, pedestrians, lane markings, and mirrors before the vehicle moves.

## Variations

- `automatic-climate-control`: press the front defrost button; the system usually sets fan, A/C, and fresh air automatically.
- `humid-summer`: use cool A/C and fresh air to dry the windshield.
- `cold-winter`: use warm defrost, A/C if available, and avoid recirculation.

## Safety & privacy

Medium risk because poor visibility can cause a crash. Do not drive until the windshield is clear, and do not wipe glass by hand while moving.
