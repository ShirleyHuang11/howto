---
name: use-cruise-control
domain: transit
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Use cruise control on suitable roads while staying responsible for speed, steering, braking, and traffic conditions.

## Preconditions

- You are licensed and familiar with the vehicle's basic controls.
- Road, weather, and traffic conditions are stable enough for steady-speed driving.
- You know where the cruise on, set, adjust, resume, and cancel controls are.

## Steps

1. **Choose the right road.** Use cruise control on open highways or steady roads, not in city traffic, heavy congestion, construction, rain, snow, ice, or winding roads. → *Expect:* the vehicle can hold speed without frequent braking.
2. **Reach a legal steady speed.** Accelerate manually to a safe speed at or below the limit. → *Expect:* traffic flow and road conditions support that speed.
3. **Turn cruise on.** Press the cruise or driver-assist power button without taking eyes off the road for long. → *Expect:* the dashboard shows cruise is available or armed.
4. **Set the speed.** Press SET when the car is stable in the lane. → *Expect:* the vehicle maintains the current speed without your foot on the accelerator.
5. **Keep your foot ready.** Rest your right foot where you can brake quickly, not tucked away or crossed. → *Expect:* you can cancel immediately if traffic changes.
6. **Adjust in small increments.** Use plus or minus controls for 1 mph or 1 km/h changes, or hold only when you intentionally want larger changes. → *Expect:* speed changes smoothly.
7. **Cancel before conflict.** [BRANCH: brake | cancel button | clutch] brake, press cancel, or depress clutch in a manual car before traffic, curves, exits, or poor traction. → *Expect:* you regain full manual speed control.
8. **Use resume only when still safe.** Press RES only after confirming the saved speed is legal and appropriate for current traffic. → *Expect:* the car returns to the prior set speed without surprising you.
9. **Stay engaged.** Scan mirrors, maintain lane position, and monitor speed downhill because some systems may exceed the set speed. → *Expect:* cruise assists speed, but you remain the driver.

## Decision points

- Road is wet or icy → do not use cruise control because traction changes can require immediate throttle control.
- Traffic speed varies often → leave cruise off until the road opens.
- Adaptive cruise is available → still watch cut-ins, stopped traffic, and lane changes; it is not self-driving.
- Speed limit changes → adjust or cancel before entering the lower-speed zone.

## Failure modes & recovery

- **F1 Car accelerates unexpectedly:** resume recalls a higher speed → brake or cancel, then set the correct speed.
- **F2 Downhill speed creep:** vehicle exceeds set speed → brake manually and select a lower gear if appropriate.
- **F3 Traffic bunches up:** you are closing on another vehicle → cancel early and drive manually.
- **F4 Poor traction starts:** rain, snow, or gravel appears → cancel and control speed with gentle inputs.
- **F5 Control confusion:** you cannot find cancel quickly → tap the brake and leave cruise off until parked and familiar.

## Verification

Cruise control is used only on a suitable road, maintains a legal set speed, and is canceled before traffic, weather, or road geometry requires manual control.

## Variations

- Adaptive cruise: set following distance conservatively and remember it may not recognize all hazards.
- Manual transmission: clutch input usually cancels cruise, and downshifts remain your job.
- Rental cars: learn the controls while parked before relying on them.
- Mountain roads: cruise may be inappropriate where grades and curves require active speed management.

## Safety & privacy

Medium risk because misuse can contribute to a crash. Cruise control does not reduce driver responsibility, does not replace braking judgment, and should never be used when tired, impaired, distracted, or in poor traction conditions.
