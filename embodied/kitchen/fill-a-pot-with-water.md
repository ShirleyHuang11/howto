---
name: fill-a-pot-with-water
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 3min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [pot, faucet, water, sink]
affordances: [grasp, carry, place, faucet-operate, fill, lift]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

A pot is filled with the requested amount of water and carried without sloshing or strain.

## Preconditions

- The pot is clean, empty, and has handles that can be gripped with both hands.
- The sink is clear enough for the pot base to sit flat under the faucet.
- The fill target is known: measured amount, recipe line, or safe headroom.

## Steps

1. **Inspect the pot.** Check that the pot has no residue, loose handle, or obstruction inside. → *Expect:* the interior is clean and both handles are usable.
2. **Place under the tap.** Set the pot flat in the sink with the faucet aimed near the center of the base. → *Expect:* the pot is stable and the stream will not hit the rim.
3. **Start water gently.** Open the cold tap partway to avoid splashing from the empty base. → *Expect:* water enters the pot with limited splash.
4. **Fill to target.** Watch the water level rise to the recipe amount, marked line, or no more than two-thirds full for carrying. → *Expect:* water stops below the safe carry line.
5. **Shut off fully.** Close the tap before lifting the pot. → *Expect:* the stream stops and no new water enters the pot.
6. **Test weight.** Grip both handles and lift one centimeter to assess load. → *Expect:* the pot feels controllable and level.
7. **Carry with two hands.** Hold the pot close to the torso, elbows bent, and keep the rim level while moving. → *Expect:* the water surface stays below the rim without sloshing over.
8. **Set down level.** Lower the pot onto the target burner or counter before releasing either handle. → *Expect:* the pot base contacts the surface evenly and the water settles.

## Decision points

- Pot is too heavy after filling → remove water with a cup or pour some out before carrying.
- Faucet cannot reach the pot center → reduce flow and aim at the inner wall to prevent splash.
- Target is unknown → fill halfway for boiling tasks unless the parent recipe specifies more.

## Failure modes & recovery

- **F1 Splashing:** water hits the rim or sprays out → lower flow and reposition the pot center under the faucet.
- **F2 Overfilled:** water sits near the rim → pour off water until carrying headroom returns.
- **F3 Unbalanced lift:** one side dips during pickup → set down, regrip both handles symmetrically, and lift again.
- **F4 Drips on floor:** water trails during carry → set pot down, wipe the floor, and resume with a slower level carry.

## Verification

The pot contains the intended amount of water, remains below a safe carry line, and is placed level at the destination with no active spill.

## Variations

- `measured-fill`: use a measuring cup first, then pour into the pot to avoid guessing.
- `large-stockpot`: fill in place on the stove with a pitcher if carrying full weight is unsafe.
- `filtered-water`: fill from a pitcher in batches, keeping the pot on the counter.

## Safety & privacy

Low risk unless the pot becomes too heavy. Use two hands, keep the load close, and reduce volume before carrying if wrist or shoulder control degrades.
