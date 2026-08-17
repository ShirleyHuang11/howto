---
name: screw-a-cap-onto-a-bottle
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [bottle, cap, threads, countertop]
affordances: [grasp, align, rotate, tighten, inspect, stabilize]
workspace: household
safety: {hot_surfaces: false, sharp_objects: false, fragile: [glass-bottle], human_proximity: continue}
---

## Goal

Thread a cap onto a bottle straight and tighten it enough to close the bottle without cross-threading or cracking it.

## Preconditions

- Bottle and matching cap are clean enough for their contents.
- Bottle mouth and cap threads are visible.
- Bottle stands upright on a stable surface.
- No debris blocks the threads or seal.

## Steps

1. **Stabilize the bottle.** Hold the bottle body upright near its shoulder or base. → *Expect:* the bottle does not tip when touched at the mouth.
2. **Place the cap level.** Set the cap centered on the bottle mouth with its open side downward. → *Expect:* the cap sits flat rather than tilted.
3. **Find the thread start.** Rotate the cap counterclockwise lightly until it drops or clicks into the thread start. → *Expect:* the cap settles level on the mouth.
4. **Turn clockwise gently.** Rotate with light downward pressure for the first full turn. → *Expect:* the cap advances downward evenly without wobbling.
5. **Tighten to seal.** Continue turning until resistance increases, then stop at snug hand-tight force. → *Expect:* the cap no longer spins freely and sits evenly against the bottle neck.
6. **Check closure.** Lift or gently invert only if the contents allow it. → *Expect:* no liquid leaks and the cap remains straight.

## Decision points

- Cap tilts or binds → back it off and restart from the thread start.
- Bottle is carbonated → tighten without shaking and do not squeeze flexible sides.
- Cap has a tamper band → confirm it belongs to the bottle before forcing it.

## Failure modes & recovery

- **F1 Cross-threading:** detect tilted cap or sudden resistance early → unscrew completely and realign before tightening.
- **F2 Loose cap:** detect cap spinning or leaking → turn clockwise until snug, checking for damaged threads.
- **F3 Cracked cap:** detect split plastic or failed seal → replace the cap.
- **F4 Bottle slips:** detect rotation of the bottle body → dry the outside and stabilize against the counter.

## Verification

The cap is level, hand-tight, seated against the bottle neck, and the bottle does not leak during a gentle closure check.

## Variations

- `child-resistant-cap`: press down while turning if the cap marking requires it.
- `wide-mouth-jar`: use two hands and check the gasket or liner before tightening.

## Safety & privacy

Low risk. Avoid over-tightening glass bottles, and treat medicine or chemical bottles as privacy- and safety-sensitive by confirming the correct cap and label.
