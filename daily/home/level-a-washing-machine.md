---
name: level-a-washing-machine
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

The washing machine stands level and stable so it does not walk, bang, or shake across the floor during spin.

## Preconditions

- Washer is empty, reachable at the front feet, and on a firm floor.
- You have a spirit level, wrench or pliers for the lock nuts, and a flashlight.
- Transit bolts have already been removed on new machines.

## Steps

1. **Confirm the cause.** Push each top corner diagonally and listen for rocking before adjusting anything. → *Expect:* one or more feet lifts or taps if the washer is unstable.
2. **Check side-to-side and front-to-back level.** Place the level on the top front edge, then the side edge. → *Expect:* you know which direction needs adjustment.
3. **Loosen the foot lock nuts.** Turn each accessible lock nut upward from the floor. [BRANCH: front feet only | four adjustable feet] adjust the design your washer uses. → *Expect:* the feet can turn independently.
4. **Adjust the low side.** Turn feet to raise the low corner or lower the high corner, working in small half-turns. → *Expect:* the bubble moves toward center.
5. **Stabilize the stance.** Press each corner again and adjust until the washer does not rock. → *Expect:* all feet touch firmly.
6. **Lock the nuts.** Hold each foot still and tighten the lock nut against the washer base. → *Expect:* the feet no longer turn by hand.
7. **Run a spin test.** Run a rinse and spin with a few towels, then watch the first high-speed spin. → *Expect:* vibration is brief and the washer stays in place.

## Decision points

- Floor flexes under the washer → level the machine, then consider a laundry-rated anti-vibration platform.
- Washer is new and shakes violently → check transit bolts before further foot adjustment.
- Load is one heavy item → redistribute or add towels, because leveling cannot fix an unbalanced load.
- Feet are seized or missing pads → replace the feet or pads before testing again.

## Failure modes & recovery

- **F1 Washer still walks:** detect movement during spin, recover by rechecking all feet contact and lock nuts.
- **F2 Lock nut loosens:** detect a changed level after one load, recover by holding the foot with pliers while tightening the nut.
- **F3 Drain hose pulls tight:** detect hose tension after moving the machine, recover by repositioning before running water.
- **F4 Cabinet hits wall:** detect knocking at spin speed, recover by leaving clearance and confirming the machine is stable.

## Verification

During a spin test with towels, the washer stays in position and no corner rocks when pressed afterward.

## Variations

- `stacked-unit`: level the washer base first and get help because the center of gravity is higher.
- `tile-floor`: rubber pads can help grip after the feet are level.
- `pedestal`: level the pedestal according to its manual, then lock the washer to it.

## Safety & privacy

Medium risk from moving a heavy appliance and from hoses pulled loose. Keep hands clear of pinch points and do not run the washer if water or power connections are strained.
