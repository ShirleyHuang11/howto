---
name: use-an-elevator
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [elevator, call-button, floor-button-panel, elevator-door]
affordances: [button-press, threshold-cross, wait, position-hold]
workspace: building-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: pause}
---

## Goal

You (or the robot) travel from the current floor to a target floor by elevator, sharing the car safely with other passengers.

## Preconditions

- The target floor number is known and reachable by this elevator bank (some banks serve only certain floors — check the posted range).
- The elevator lobby is reachable; any access control (badge reader) can be satisfied.

## Steps

1. **Press the call button for the travel direction.** Up or down relative to your current floor; press once. → *Expect:* the button illuminates; if already lit, someone has called it — don't re-press.
2. **Position beside the doors, not in front of them.** Leave the door zone clear for exiting passengers. → *Expect:* clear sightline to the arriving car without blocking egress.
3. **Wait for arrival and check the direction indicator.** → *Expect:* chime and lit arrow matching your direction; a car going the wrong way is not yours — keep waiting.
4. **Let exiting passengers out first, then board.** Pause at the threshold if anyone is exiting; cross the threshold at normal speed — the door-edge sensors will hold the doors, but do not linger in the doorway. → *Expect:* you are inside; doors remain open a few seconds.
5. **Press the target floor button.** If blocked from the panel by other passengers, ask: "Could you press 5, please?" → *Expect:* the floor button illuminates.
6. **Move to a free spot and hold position during travel.** Face the doors, keep clear of others' personal space; with a cart/robot chassis, occupy a rear corner. ⚠️ *Irreversible:* doors closing on a trailing part (cable, cart, limb) — everything crosses the threshold together in step 4, nothing trails. → *Expect:* doors close; floor indicator counts toward your floor.
7. **Exit when the indicator shows your floor and doors open.** Verify the floor number on the door frame or lobby signage before fully committing — cars stop at other floors for other passengers. → *Expect:* lobby signage confirms the target floor.

## Decision points

- Car arrives full → step back, let it go, press the call button again.
- Someone runs for the closing doors → press and hold "door open" (◄►) if you are at the panel.
- Fire alarm active → do not use the elevator at all; take the stairs (a robot should hold position out of egress paths and await instruction).
- Freight vs. passenger elevator → carts, large robots, and bulky loads belong in the freight car where one exists.

## Failure modes & recovery

- **F1 Doors begin closing while boarding:** the edge sensor reopens them on contact/interruption; step back cleanly rather than forcing through.
- **F2 Wrong floor button pressed:** on many panels a double-press or long-press cancels; otherwise ride past and return.
- **F3 Car stops between floors / doors don't open:** press the door-open button once, then the alarm/intercom button and report position; never pry doors or attempt to climb out — wait for trained rescue.
- **F4 Access-controlled floor rejects the selection:** the floor needs a badge tap before or while pressing — tap, then press; without credentials, travel to the nearest allowed floor.

## Verification

You are standing in the lobby of the target floor (signage matches), clear of the door zone, with nothing left behind in the car.

## Variations

- Destination-dispatch systems: you enter the floor on a lobby keypad *before* boarding and are assigned a lettered car — there is no floor panel inside; steps 1 and 5 merge.
- Robot integration: buildings with elevator APIs let robots call/hold cars electronically — steps 1, 5 become API calls, but threshold and positioning behavior (4, 6) is identical.

## Safety & privacy

Medium risk around door mechanics and shared close quarters: pause all motion when humans are boarding/exiting, never trail anything through the threshold, and yield the car entirely during alarms.
