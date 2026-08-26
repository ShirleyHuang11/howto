---
name: handle-an-overheating-engine
domain: transit
subdomain: vehicle
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: high
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You reduce engine load, stop safely, avoid burn injuries, and prevent further engine damage when the temperature warning rises.

## Preconditions

- The temperature gauge is high, a temperature warning is on, steam is visible, or coolant smell is present.
- You can reduce speed and pull over safely.
- You have a phone for assistance if the vehicle cannot continue.

## Steps

1. **Turn off air conditioning and reduce load.** Switch off A/C, reduce speed, and avoid hard acceleration. → *Expect:* engine load drops immediately.
2. **Turn cabin heat on if tolerable.** Set heat and fan high to pull some heat from the engine. → *Expect:* warm air enters the cabin and temperature may stabilize briefly.
3. **Pull over safely.** Signal, leave traffic, and stop in a safe area as soon as practical. → *Expect:* the vehicle is stationary away from active traffic if possible.
4. **Shut off the engine.** Put the vehicle in park, set the parking brake, and turn on hazard lights. → *Expect:* the engine stops producing heat.
5. **Do not open a hot radiator or pressure cap.** ⚠️ *Hazard:* pressurized coolant can erupt and cause severe burns; wait until fully cool before opening any coolant cap. → *Expect:* no cap is opened while steam, heat, or pressure may remain.
6. **Inspect from a safe distance.** Look for steam, leaks, broken belt, fan damage, or coolant under the vehicle without reaching into hot or moving parts. → *Expect:* obvious external signs are noted.
7. **Decide whether to add coolant or tow.** [BRANCH: engine fully cooled and reservoir is low with correct coolant/water available, top up reservoir only as manual allows | active leak, repeated overheating, no coolant, warning persists, or unknown cause, call roadside assistance] → *Expect:* the vehicle is not restarted unless conditions are safe.
8. **Restart only for a short test if safe.** Watch the gauge and warning lights; stop again if temperature rises. → *Expect:* temperature remains normal or towing is chosen.

## Decision points

- Temperature warning is red or steam is visible → stop as soon as safe and shut off the engine.
- Coolant is leaking quickly → do not drive; arrange towing.
- You are on a highway shoulder → prioritize personal safety and call roadside assistance instead of roadside repairs.

## Failure modes & recovery

- **F1 Cap opened too soon:** detect hiss, steam, or hot spray → move away, stop turning the cap, cool completely, and seek medical help for burns.
- **F2 Temperature drops then rises again:** detect repeated overheating after restart → stop driving and tow; the underlying problem remains.
- **F3 No heat from vents:** detect cold air despite high temperature → coolant may be very low; stop and do not continue.
- **F4 Warning ignored:** detect loss of power, knocking, or smoke → shut down and tow; severe engine damage may already be occurring.

## Verification

The vehicle is safely stopped or operating at normal temperature after a cautious test, no hot caps were opened, and towing or repair is arranged if overheating persists or coolant is leaking.

## Variations

- Hybrid/EV: cooling systems may serve electronics and batteries; follow manufacturer warnings and do not inspect high-voltage components.
- Mountain driving or towing: reduce load, downshift as appropriate, and stop earlier because overheating can return quickly.
- Cold weather: coolant concentration matters for freeze protection after adding water temporarily.

## Safety & privacy

High risk from burns, roadside traffic, and engine damage. Confirm the engine is cool before opening any cap and do not drive with a persistent temperature warning.
