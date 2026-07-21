---
name: put-on-a-backpack
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [backpack, shoulder-straps]
affordances: [grasp, lift, insert-arm, adjust-strap, balance]
workspace: household-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [backpack], human_proximity: continue}
---

## Goal

A backpack is worn with both straps on the shoulders, the load settled against the back, and balance checked before walking.

## Preconditions

- The backpack is zipped or closed enough that contents will not spill.
- Both shoulder straps are free and not twisted.
- The backpack weight is within comfortable carrying range.
- The actor has standing room and at least one hand free.

## Steps

1. **Place the backpack upright.** Hold or set it so the shoulder straps face the actor. → *Expect:* top handle and both straps are visible.
2. **Check strap orientation.** Untwist straps and loosen tight adjusters if needed. → *Expect:* each strap forms an open loop.
3. **Grip the top handle or one strap.** Lift the backpack close to the torso. → *Expect:* pack weight is controlled and not swinging.
4. **Thread the first arm.** Insert one arm through the nearest strap until the strap rests on that shoulder. → *Expect:* one strap is seated and the pack hangs on one side.
5. **Swing the pack onto the back.** Move the pack behind the torso while keeping the first shoulder engaged. → *Expect:* backpack panel contacts the back.
6. **Thread the second arm.** Reach the free arm back and through the second strap. [BRANCH: standing | seated] standing actors lean slightly forward; seated actors keep the pack supported by the seat or lap. → *Expect:* both straps are over shoulders.
7. **Settle the load.** Shrug shoulders and pull the lower pack down or back until it lies flat. → *Expect:* weight feels centered and the pack is not twisted.
8. **Adjust straps.** Pull adjuster tails evenly or loosen if straps bite into shoulders. → *Expect:* pack sits close to the back without restricting arm motion.
9. **Check balance before stepping.** Stand still for two seconds and shift weight gently left and right. → *Expect:* no backward pull, side sway, or loose dangling strap hazard.

## Decision points

- Backpack is too heavy → set it down and remove items or ask for help.
- One strap is trapped under the pack → remove the first strap and reset orientation.
- Shoulder mobility is limited → put the pack on from a chair, table, or with assistance.
- Long loose straps hang near wheels or feet → secure them before moving.
- Pack contains fragile items → avoid swinging and keep it upright.

## Failure modes & recovery

- **F1 Strap twist:** detect pressure edge or rotated strap → remove that arm, untwist, and reinsert.
- **F2 Load pulls backward:** detect leaning or heel pressure → tighten straps, lighten pack, or use a chest strap.
- **F3 Second arm misses strap:** detect hand searching behind back without loop contact → hold strap forward with the other hand and retry.
- **F4 Contents shift sharply:** detect sudden side load → stop, set pack down, and redistribute contents.
- **F5 Strap slips off shoulder:** detect falling strap → tighten or use both straps fully before walking.

## Verification

Both shoulder straps are worn, the backpack lies against the back, straps are adjusted, and the actor can stand steady without holding the pack.

## Variations

- `heavy-pack`: place it on a table at waist height, back into the straps, then stand.
- `single-strap-use`: acceptable only for light loads and short distance.
- `chest-strap`: clip after shoulder straps are seated, then tighten lightly.
- `wheelchair-user`: position the pack on lap or chair back according to safe reach and chair stability.

## Safety & privacy

Low risk for moderate loads. Avoid sudden twisting while one strap is on. Do not inspect private contents unless closure, weight, or sharp protrusions affect safe wearing.
