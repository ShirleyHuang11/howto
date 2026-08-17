---
name: nest-mixing-bowls
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
objects: [mixing-bowls, shelf, counter]
affordances: [grasp, lift, sort-by-size, align, lower, nest]
workspace: kitchen counter or cupboard
safety: {hot_surfaces: false, sharp_objects: false, fragile: [ceramic-bowls, glass-bowls], human_proximity: continue}
---

## Goal

Mixing bowls are nested largest-to-smallest in a compact, stable stack.

## Preconditions

- Bowls are empty, dry, and cool.
- A clean counter or shelf space is available.
- Any lids or loose tools have been removed from the bowls.

## Steps

1. **Sort bowls by size.** Place bowls in a row from largest rim diameter to smallest. → *Expect:* each bowl is visible and no bowl is hidden inside another.
2. **Place the largest bowl.** Grasp both sides near the rim, keep the opening upward, and lower it onto the target surface. → *Expect:* the largest bowl sits flat and centered.
3. **Lift the next smaller bowl.** Use two opposing side grasps and keep fingers clear of the lower rim. → *Expect:* the bowl is level with its open side facing upward.
4. **Center it above the lower bowl.** Align the bowl axes and keep the rims parallel. → *Expect:* the lower bowl rim appears evenly around the lifted bowl.
5. **Nest with light downward force.** Lower until the smaller bowl contacts the inside of the larger bowl and stops moving. → *Expect:* the smaller bowl rests inside without rocking.
6. **Continue smallest last.** Repeat the same centered lowering for each remaining bowl. → *Expect:* each added bowl sits below the rim height of the bowl beneath it when possible.
7. **Final stability check.** Release both hands and observe the nested set from the side. → *Expect:* the stack is compact, level, and does not tip.

## Decision points

- Bowls are the same size → stack no more than two identical bowls unless they seat flat.
- Bowl has a spout or handle → align protrusions to avoid rim pressure.
- Stack exceeds shelf height → split into two nested sets.

## Failure modes & recovery

- **F1 Bowl wedged tight:** detect by no vertical play after placement → lift the upper bowl with two hands and rebuild with a larger lower bowl.
- **F2 Rim-on-rim contact:** detect by upper bowl rocking on the lower rim → recenter or choose a different nesting order.
- **F3 Slippery bowl:** detect by sliding during grip → dry the outside surface and retry with a wider grip.

## Verification

The nested bowls remain upright and compact after release, with the largest bowl on the bottom and no rim carrying an off-center load.

## Variations

- Stainless bowls: expect more sliding; use lower acceleration and a centered two-hand grasp.
- Glass bowls: reduce impact force and keep a padded surface nearby.

## Safety & privacy

Fragile bowls can crack from edge impacts. Keep fingers out from between nested rims during lowering.
