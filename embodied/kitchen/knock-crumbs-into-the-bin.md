---
name: knock-crumbs-into-the-bin
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [plate, cutting-board, crumbs, trash-bin, compost-bin, brush]
affordances: [grasp, carry, tilt, tap, sweep, release]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [plate], human_proximity: continue}
---

## Goal

Move loose crumbs from a plate, board, or counter into the correct bin without scattering them onto the floor.

## Preconditions

- Crumbs are dry or only lightly moist.
- Trash, compost, or disposal target is open and reachable.
- The item holding crumbs is cool and safe to handle.
- No utensils or wanted food pieces are mixed into the crumbs.

## Steps

1. **Choose the bin.** [BRANCH: trash | compost] use compost for accepted food scraps and trash for contaminated or non-compostable crumbs. → *Expect:* the correct bin is open before lifting crumbs.
2. **Lift the crumb surface.** Grasp the plate or board level with two stable contact points. → *Expect:* crumbs remain on the surface during the lift.
3. **Move over the bin opening.** Hold the crumb side fully inside the bin perimeter. → *Expect:* falling crumbs would land inside the bin.
4. **Tilt and tap.** Angle the surface downward and tap the far edge lightly with a hand or brush. → *Expect:* crumbs slide or fall into the bin.
5. **Sweep remaining crumbs.** Use a brush, paper towel, or hand edge to push stuck crumbs toward the lowered side. → *Expect:* only tiny residue remains on the surface.
6. **Return and inspect.** Bring the plate or board back level before moving away from the bin. → *Expect:* no visible crumb trail appears between bin and counter.

## Decision points

- Crumbs are wet or sticky → wipe instead of tapping.
- Crumbs contain broken glass or ceramic → use `embodied/household/pick-up-broken-glass` rather than bare wiping.
- Bin lid is foot-operated → open it before lifting the crumb surface.

## Failure modes & recovery

- **F1 Crumbs scatter:** detect crumbs landing outside the bin → stop tapping, lower the item farther into the opening, and sweep the floor.
- **F2 Wanted item falls:** detect utensil or food piece sliding toward the bin → level the surface and remove the item before continuing.
- **F3 Bin overfull:** detect crumbs resting near the rim → compact or replace the bag before adding more debris.
- **F4 Sticky residue remains:** detect crumbs adhered to sauce or oil → wipe with a damp cloth and clean the surface.

## Verification

The original surface has no loose crumbs, the crumbs are inside the correct bin, and the floor around the bin is clean.

## Variations

- `countertop`: sweep crumbs into a dustpan or held plate before tipping into the bin.
- `toaster-tray`: remove the tray over the sink or bin before dumping.

## Safety & privacy

Low risk. Check for sharp fragments before sweeping by hand, and keep fragile plates away from the bin rim.
