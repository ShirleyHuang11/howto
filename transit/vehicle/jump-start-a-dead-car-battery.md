---
name: jump-start-a-dead-car-battery
domain: transit
subdomain: vehicle
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 30min
risk: high
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You safely use jumper cables or a jump pack to start a vehicle with a discharged 12-volt battery.

## Preconditions

- Jumper cables and a working donor vehicle, or a charged jump starter rated for the vehicle.
- Both vehicles use compatible 12-volt systems unless the manual says otherwise.
- No cracked, frozen, leaking, or visibly bulging battery.

## Steps

1. **Check for battery damage first.** Look for leaking acid, swelling, cracks, heavy corrosion, or a frozen battery. ⚠️ *Hazard:* do not jump-start a damaged or frozen battery because it can explode. → *Expect:* the battery appears intact enough to jump or the task is stopped.
2. **Position safely.** Park the donor vehicle close enough for cables but with vehicles not touching; shift to Park or Neutral and set parking brakes. → *Expect:* both vehicles are stable and accessories are off.
3. **Identify terminals and ground.** Find positive (+) and negative (-) battery posts, and an unpainted metal engine or chassis ground on the dead vehicle. → *Expect:* you know all connection points before touching cables.
4. **Connect positive to dead battery.** Clamp red to the dead battery's positive terminal. → *Expect:* the clamp is secure and not touching metal elsewhere.
5. **Connect positive to donor battery.** Clamp the other red end to the donor battery's positive terminal. → *Expect:* both red clamps are on positive posts.
6. **Connect negative to donor battery.** Clamp black to the donor battery's negative terminal. → *Expect:* the donor negative clamp is secure.
7. **Connect final negative to ground.** Clamp the last black end to unpainted metal on the dead vehicle, away from the battery and fuel lines. ⚠️ *Hazard:* make this final connection away from the dead battery to reduce spark risk. → *Expect:* all cables are connected in the correct order.
8. **Start the donor or power on the jump pack.** Let it run or supply power for a few minutes. → *Expect:* the dead vehicle has enough charge to attempt a start.
9. **Start the dead vehicle.** Crank for no more than a few seconds at a time. → *Expect:* the engine starts or the starter behavior improves.
10. **Remove cables in reverse order.** Remove black ground, black donor negative, red donor positive, then red dead positive. Keep clamps from touching. → *Expect:* cables are off safely and both engines keep running.
11. **Recharge by driving.** Drive for at least 20-30 minutes or use a battery charger. → *Expect:* the vehicle restarts later or battery testing shows it needs replacement.

## Decision points

- Dead vehicle does not crank after several minutes → stop and check cable contact, battery condition, starter, or call roadside assistance.
- Battery is repeatedly dead → test battery, alternator, and parasitic drain.
- Hybrid or EV → follow the owner's manual exactly; jump points may be under the hood and procedures vary.

## Failure modes & recovery

- **F1 Sparks at battery:** stop, disconnect in reverse order, and reconnect with the final negative clamp on a proper ground away from the battery.
- **F2 Alarm sounds or electronics act strangely:** unlock with the key fob, wait, and follow the manual's reset procedure.
- **F3 Vehicle starts then dies:** alternator or charging system may be failing; seek service instead of driving far.
- **F4 Cables heat up:** shut everything off and disconnect; cables may be too small or connected incorrectly.

## Verification

The dead vehicle starts, jumper cables are removed without incident, and the vehicle either restarts after charging or is scheduled for battery/charging-system service.

## Variations

- `jump-pack`: connect red positive, black to chassis ground, power on the pack, start the vehicle, then power off and remove clamps.
- `remote-posts`: some vehicles provide under-hood jump posts; use those instead of hidden battery terminals.
- `manual-transmission`: push-starting is a separate procedure and only works for some vehicles.

## Safety & privacy

High risk from battery explosion, acid, fire, and vehicle movement. Confirm polarity before connecting, make the final negative connection to a ground away from the dead battery, and stop if the battery is damaged.
