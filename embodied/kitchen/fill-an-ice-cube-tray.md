---
name: fill-an-ice-cube-tray
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 3min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [ice-cube-tray, faucet, water-pitcher, freezer, towel]
affordances: [grasp, carry, pour, fill, level, place]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

Fill an ice cube tray with water and place it level in the freezer without spilling into the freezer or onto the floor.

## Preconditions

- Ice cube tray is clean and not cracked.
- Potable water is available.
- Freezer has a flat open space for the tray.
- Carry path from sink to freezer is clear.

## Steps

1. **Inspect the tray.** Hold it level and check each cube pocket for dirt, old ice, or cracks. → *Expect:* all pockets are empty, clean, and able to hold water.
2. **Position under water source.** Set the tray on the sink base or counter under the faucet, or hold a pitcher above one corner. → *Expect:* the tray is level and supported.
3. **Fill slowly across pockets.** Run a thin stream and move it from pocket to pocket until each is nearly full. → *Expect:* water reaches just below the top edge of each pocket.
4. **Correct the level.** Pour off excess from overfilled pockets or add water to low pockets. → *Expect:* no water sheet connects across the tray top.
5. **Carry with two-hand support.** Hold both short ends level and move at low speed toward the freezer. → *Expect:* water surfaces stay inside the pockets.
6. **Place flat in the freezer.** Slide the tray onto a level shelf without tilting it upward at the back. → *Expect:* the tray rests flat and water remains in the pockets.

## Decision points

- Freezer shelf is crowded → clear a level space before filling the tray.
- Tray has a lid → fill first, then snap the lid on while the tray sits on a counter.
- Flexible silicone tray → support it from below with a plate during carry.

## Failure modes & recovery

- **F1 Overfilled tray:** detect water pooled over dividers → pour a small amount into the sink and re-level.
- **F2 Tray flexes:** detect pockets changing shape during lift → place the tray on a rigid plate and carry both together.
- **F3 Spill on floor:** detect wet path or drops → set tray down, wipe floor immediately, then refill low pockets.
- **F4 Freezer tilt:** detect water running to one side after placement → move the tray to a flatter shelf or shim space with a flat bin.

## Verification

The tray is in the freezer on a flat surface, each pocket contains water below the rim, and no standing water remains on the floor or freezer shelf.

## Variations

- `filtered-water`: fill from a pitcher on the counter for better control.
- `covered-tray`: leave a small headspace so the lid does not displace water.

## Safety & privacy

Low risk. Wipe spills promptly because clear water on hard floors is a slip hazard.
