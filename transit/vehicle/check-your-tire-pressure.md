---
name: check-your-tire-pressure
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

You measure each tire's pressure when the tires are cold and compare it with the vehicle manufacturer's recommended PSI.

## Preconditions

- A working tire pressure gauge.
- The vehicle has been parked for at least 3 hours or driven less than about 1 mile.
- The tire-pressure label in the driver's door jamb or the owner's manual is available.

## Steps

1. **Find the correct PSI.** Read the tire placard on the driver's door jamb, fuel door, glovebox, or owner's manual; do not use the maximum PSI molded on the tire sidewall. → *Expect:* you have front, rear, and spare tire target pressures.
2. **Remove one valve cap.** Put it somewhere safe. → *Expect:* the metal valve stem is exposed.
3. **Press the gauge straight onto the valve.** Push firmly until the hissing stops and the gauge gives a reading. → *Expect:* a stable PSI reading appears.
4. **Write down the reading.** Note the tire position: left front, right front, left rear, right rear, and spare if accessible. → *Expect:* each checked tire has a recorded PSI.
5. **Replace the valve cap.** Screw it on snugly by hand. → *Expect:* the valve is covered and protected from dirt.
6. **Repeat for every tire.** Include the spare if the vehicle has an inflatable spare. → *Expect:* all tire pressures are recorded.
7. **Compare readings with the placard.** Identify tires that are below, above, or at the recommended cold pressure. → *Expect:* you know which tires need air added or released.

## Decision points

- Tire is more than a few PSI low → add air soon using `transit/vehicle/add-air-to-a-tire`.
- One tire is repeatedly low → inspect for puncture, valve leak, or rim damage.
- Pressure warning light remains after correction → drive a short distance if the manual says so, then reset TPMS only after pressures are correct.

## Failure modes & recovery

- **F1 Gauge hisses continuously:** reseat the gauge squarely on the valve and try again.
- **F2 Reading changes wildly:** check when tires are cold and try a second gauge.
- **F3 Valve cap is stuck:** use gentle hand pressure or pliers lightly; replace damaged caps.
- **F4 Tire is visibly flat:** do not drive on it; inflate where parked or install the spare.

## Verification

Each tire has a recorded cold PSI reading and you know whether it matches the vehicle placard's recommended pressure.

## Variations

- `truck-rv`: front and rear pressures may differ significantly by load; follow the placard or load table.
- `motorcycle-bicycle`: use the vehicle or tire maker's recommended pressure range for the load and tire type.
- Digital gauge: wait for the reading to stabilize before removing it.

## Safety & privacy

Low risk, but underinflated tires can overheat and fail. Check pressure when tires are cold and never inflate based only on the tire sidewall maximum.
