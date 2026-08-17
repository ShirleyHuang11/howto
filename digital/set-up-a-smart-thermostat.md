---
name: set-up-a-smart-thermostat
domain: digital
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min-2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Install and configure a smart thermostat so heating and cooling work correctly, schedules are sensible, and account/location settings are private.

## Preconditions

- You have the thermostat, phone app, Wi-Fi password, and HVAC system information.
- You can turn off HVAC power at the breaker.
- Your wiring is compatible, including a C-wire or supported adapter if required.

## Steps

1. **Confirm compatibility.** Use the vendor compatibility checker and photograph the old thermostat wiring before removing anything. → *Expect:* wire labels and compatibility result are saved.
2. **Turn off HVAC power.** Switch off the HVAC breaker or furnace switch and confirm the old thermostat display turns off. → *Expect:* the thermostat has no power.
3. **Label and move wires.** Label each wire by terminal, remove the old base, and connect wires to the matching terminals on the new base. → *Expect:* each wire is secure in a labeled terminal.
4. **Attach the thermostat and restore power.** Mount the display, turn the breaker back on, and wait for startup. → *Expect:* the thermostat powers on and begins setup.
5. **Configure equipment type.** In the app or thermostat, select heat pump, conventional, boiler, furnace, stages, fuel type, and accessories accurately. → *Expect:* the thermostat accepts the equipment configuration.
6. **Connect Wi-Fi and account.** Join the home Wi-Fi network and sign in with the vendor account. → *Expect:* the app shows the thermostat online.
7. **Test heat, cool, and fan.** Run each mode briefly and listen for the correct equipment. → *Expect:* warm air, cool air, and fan behavior match the selected test.
8. **Set schedule and privacy options.** Configure comfort temperatures, away behavior, geofencing only if wanted, and household access. → *Expect:* schedules and permissions match the household's routine.

## Decision points

- No C-wire → use the vendor adapter, choose a battery-compatible model, or call an HVAC technician.
- Heat pump with auxiliary heat → verify labels carefully because wrong setup can be costly.
- Rental home → get permission before replacing the thermostat.
- Geofencing unwanted → use schedules without location access.

## Failure modes & recovery

- **F1 Thermostat will not power on:** detect blank display → turn power off and recheck C/R wiring and panel door switch.
- **F2 Heating cools or cooling heats:** detect wrong air temperature → stop test and correct heat-pump reversing valve or equipment type.
- **F3 HVAC short-cycles:** detect rapid on/off cycles → restore previous thermostat or call a technician.
- **F4 App cannot connect:** detect offline status → check 2.4 GHz support, Wi-Fi password, and signal strength.

## Verification

The thermostat appears online in the app, heat/cool/fan tests operate the correct equipment, the schedule is active, and household access and location settings are intentional.

## Variations

- Heat pump systems: reversing valve and auxiliary heat setup require extra care.
- Radiator or boiler systems: compatibility depends on voltage and control type.
- Multi-zone homes: each zone may need its own compatible thermostat.

## Safety & privacy

Medium risk because wiring mistakes can damage HVAC equipment and location features reveal occupancy patterns. Turn off power and limit geofencing and shared access.
