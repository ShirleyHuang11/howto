---
name: make-drip-coffee
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: medium
prerequisites: [daily/food/boil-water]
status: draft
last_verified: 2026-07-20
objects: [drip-coffee-maker, carafe, filter-paper, ground-coffee, water-pitcher, mug]
affordances: [lid-open, scoop, pour, button-press, grasp-handle]
workspace: kitchen
safety: {hot_surfaces: true, sharp_objects: false, fragile: [carafe, mug], human_proximity: pause}
---

## Goal

A carafe of brewed coffee sits on the coffee maker's warming plate, and one mug is filled and delivered to the counter.

## Preconditions

- Drip coffee maker is on a stable counter, plugged in, and empty of previous grounds.
- Supplies within reach: filter paper, ground coffee, water source, clean mug.
- Carafe is clean and seated on the warming plate.

## Steps

1. **Open the water reservoir lid and fill with water.** Pour to the marked line for the target number of cups (e.g., the "4" line for 4 cups). → *Expect:* water level gauge reads at the target line; no overflow.
2. **Open the filter basket and insert a filter paper.** Splay the paper so it sits flush against the basket walls. → *Expect:* filter paper conforms to the basket; no folded-over edges.
3. **Scoop ground coffee into the filter.** One level scoop (~7 g) per cup of water. → *Expect:* grounds sit level in the filter; basket closes without resistance.
4. **Confirm the carafe is seated on the warming plate, lid aligned under the drip outlet.** → *Expect:* carafe clicks/rests fully back; anti-drip valve is engaged by the lid.
5. **Press the brew button.** → *Expect:* indicator light turns on; within ~60 s, gurgling begins and coffee drips into the carafe. If nothing after 90 s, F1.
6. **Wait for the brew cycle to finish.** Do not remove the carafe mid-brew unless the machine's pause-and-serve is confirmed. → *Expect:* dripping stops; the machine sputters, then quiets; carafe level matches the water volume from step 1.
7. **Pour one mug.** Grasp the carafe handle, pour slowly into the mug to ~2 cm below the rim, return the carafe to the warming plate. ⚠️ *Irreversible:* hot-liquid spill — pour over the counter, never over the floor or near a person; pause pouring if a human enters arm's reach. → *Expect:* mug filled to target level; no spill on the counter.
8. **Deliver the mug to the designated counter position.** Carry level, at slow speed. → *Expect:* mug at rest at the target position, contents not spilled.

## Decision points

- Reservoir already contains water of unknown age → empty and refill fresh.
- No filter paper available → check for a built-in permanent mesh filter; if none, stop (grounds in the carafe is a failed brew).
- Machine has a grinder/strength setting → default to medium; do not explore settings mid-task.

## Failure modes & recovery

- **F1 No brewing after 90 s:** check power at the outlet and that the reservoir lid is fully closed (interlock); re-press brew once; else report machine fault.
- **F2 Overflow at the filter basket:** too much coffee or a collapsed filter — power off, wait for dripping to stop, remove basket over the sink, restart from step 2 with a fresh filter.
- **F3 Carafe not seated, coffee pooling on the plate:** power off, re-seat carafe, wipe the plate after it cools; brewed volume is partially lost — assess whether remaining volume meets the goal.
- **F4 Spill during pour:** set the carafe down first, then wipe with a towel; verify no liquid reached electrical parts before resuming.

## Verification

Carafe on the warming plate contains brewed coffee (level ≈ water volume minus one mug), the filled mug rests at the delivery position, warming plate area is dry, and the machine's indicator shows brew complete/keep-warm.

## Variations

- Machines with thermal carafes have no warming plate — verification drops the plate checks.
- Pre-ground vs whole-bean machines: whole-bean adds a hopper-fill step before step 3.

## Safety & privacy

Hot surfaces (warming plate) and hot liquid throughout steps 5–8. Fragile objects: carafe, mug — grasp force appropriate to glass/ceramic. Pause all motion with hot liquid in hand when a human enters the workspace.
