---
name: replace-a-trash-bag
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [trash-can, trash-bag, liner, lid, drawstring]
affordances: [grasp, lift, tie, pull, unfold, line]
workspace: household
safety: {hot_surfaces: false, sharp_objects: true, fragile: [], human_proximity: continue}
---

## Goal

Remove a full trash bag and install a clean liner so the can is ready for new trash without leaks or exposed edges.

## Preconditions

- Replacement bag fits the trash can.
- Full bag is not too heavy to lift safely.
- Trash route or holding spot is clear.
- Hands or grippers can avoid touching loose waste.

## Steps

1. **Open or remove the lid.** Lift the lid or swing it clear without touching the trash surface. → *Expect:* the liner rim is visible around the can.
2. **Free the bag edge.** Pull the liner edge or drawstrings inward from the can rim. → *Expect:* the bag mouth can close above the trash.
3. **Close the full bag.** Tie drawstrings or twist the neck and knot it above the waste level. → *Expect:* trash is enclosed and the bag can be lifted from the closed neck.
4. **Lift straight up.** Pull the bag out without dragging against sharp can edges. → *Expect:* the bag clears the can without tearing or leaking.
5. **Insert the new bag.** Open a clean liner, push its bottom to the can base, and fold the top edge over the rim. → *Expect:* the liner reaches the bottom and stays captured around the rim.
6. **Reinstall the lid.** Set the lid back or close it, then place the full bag at the disposal point. → *Expect:* the can opens normally and the full bag remains closed.

## Decision points

- Bag is leaking → place it inside a second bag before moving it far.
- Trash contains visible sharp items → lift slowly and keep the bag away from legs.
- Can interior is dirty → wipe and dry it before installing the new liner.

## Failure modes & recovery

- **F1 Bag tears:** detect stretching, holes, or falling trash → lower it into the can and double-bag before lifting again.
- **F2 New liner floats above bottom:** detect empty space under the bag → press the liner bottom down along the can walls.
- **F3 Liner slips inside:** detect bag edge falling below rim → refold more material over the rim or use a larger liner.
- **F4 Odor or spill in can:** detect wet residue after removal → clean and dry the can before relining.

## Verification

The full bag is closed and removed, and the trash can has a clean liner seated at the bottom with its edge secured over the rim.

## Variations

- `drawstring-bag`: cinch both strings evenly before tying.
- `small-bin`: invert the bag over the rim first, then push the center down.

## Safety & privacy

Low risk, with possible sharp waste. Avoid compressing unknown trash by hand and treat documents or medication packaging as privacy-sensitive before disposal.
