---
name: pump-your-own-gas
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

You refuel the vehicle with the correct fuel, pay safely, and leave the pump area without spills or damage.

## Preconditions

- The vehicle uses gasoline or diesel and you know the required fuel type and octane from the fuel door or owner's manual.
- You have a payment method accepted by the station.
- The engine, smoking materials, and open flames are off.

## Steps

1. **Park with the fuel door beside the pump.** Stop close enough for the hose to reach without stretching across traffic. → *Expect:* the vehicle is in park, engine off, and the fuel door is accessible.
2. **Confirm the fuel type.** Read the fuel door label and pump handle labels before lifting a nozzle. ⚠️ *Irreversible:* putting diesel in a gasoline vehicle or gasoline in a diesel vehicle can cause major damage; confirm before pumping. → *Expect:* you have selected the correct nozzle and grade.
3. **Pay or authorize the pump.** Use the card reader, mobile app, or cashier, shielding your PIN and checking for loose card-skimmer parts. → *Expect:* the pump display authorizes fueling and resets to zero.
4. **Open the tank and insert the nozzle fully.** Remove the cap if present, place it in its holder, and seat the nozzle securely. → *Expect:* the nozzle stays in the filler neck without leaking.
5. **Pump fuel at a normal rate.** Squeeze the handle and use the latch only if allowed locally; stay near the vehicle. → *Expect:* gallons/liters and price increase steadily.
6. **Stop at the first automatic click.** Do not top off after the nozzle shuts off. → *Expect:* fueling stops without overflow.
7. **Return the nozzle and close the tank.** Let drips fall into the filler neck, return the handle, tighten the cap until it clicks if applicable, and close the fuel door. → *Expect:* the tank is sealed and the pump session ends.
8. **Collect the receipt and leave carefully.** Check mirrors and pedestrians before pulling away. → *Expect:* you have proof of purchase and the area around the pump is clear.

## Decision points

- You selected the wrong fuel but have not pumped → hang up the nozzle, cancel, and restart with the correct one.
- You pumped the wrong fuel → do not start the engine; push the vehicle away only if safe and call roadside assistance or a mechanic.
- Pump will not authorize → try another pump or pay inside; do not leave your card unattended.
- Fuel spills → stop pumping, notify station staff, and avoid starting the vehicle if there is a large spill near hot surfaces.

## Failure modes & recovery

- **F1 Nozzle keeps clicking off:** detect repeated shutoff immediately → reseat the nozzle, slow the flow, or use another pump.
- **F2 Card reader looks tampered with:** detect loose, bulky, or mismatched parts → cancel and pay inside or use another station.
- **F3 Fuel cap warning later:** detect a check-engine or fuel-cap message → retighten the cap and drive normally; if it persists, service the vehicle.
- **F4 Overflow:** detect fuel spilling from the filler → release the handle, return the nozzle, alert staff, and wash fuel from skin.

## Verification

The fuel gauge has increased, the fuel door and cap are closed, the correct fuel appears on the receipt or pump display, and no active spill remains.

## Variations

- `us`: some states or stations restrict self-service; follow attendant instructions where required.
- Diesel vehicle: use the diesel nozzle only and avoid DEF filler confusion; DEF is not diesel fuel.
- Motorcycle or portable container: fill slowly, keep containers on the ground, and do not fill in a trunk or truck bed liner.

## Safety & privacy

Medium risk from fire, fumes, payment theft, and vehicle damage. Turn the engine off, do not smoke, do not reenter and build static repeatedly while fueling, and confirm fuel type before pumping.
