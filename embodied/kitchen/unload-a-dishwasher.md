---
name: unload-a-dishwasher
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: medium
prerequisites: [embodied/kitchen/load-a-dishwasher]
status: draft
last_verified: 2026-07-20
objects: [dishwasher, plates, bowls, cups, glasses, cutlery, cutlery-basket, cabinets, drawers]
affordances: [door-open, rack-slide, grasp, place, carry, cabinet-open, drawer-open]
workspace: kitchen
safety: {hot_surfaces: true, sharp_objects: true, fragile: [glasses, plates, bowls], human_proximity: pause}
---

## Goal

A finished dishwasher is emptied with everything dry, intact, and stored in its home location, leaving the machine ready for the next load.

## Preconditions

- The wash cycle is complete (indicator shows done/clean; drum quiet). Interrupting a running machine mid-cycle is a different act and drops hot water on the door.
- Storage locations for each category are known: plate cabinet, glass shelf, cutlery drawer, pot cupboard. Unknown homes: stage on the counter and ask, rather than inventing new homes (`embodied/household/tidy-a-room`'s stage-don't-decide principle).

## Steps

1. **Open the door and pause for the steam.** Crack the door and wait a few seconds; a just-finished machine vents hot moist air at face height. → *Expect:* steam dispersed; contents hot-to-warm but touchable.
2. **Check the cycle actually cleaned.** Glance at a few items: food residue or gritty film means the load re-runs (or the spray arm was blocked, `embodied/kitchen/load-a-dishwasher` F1), and unloading dirty dishes into cabinets is the failure to avoid at all costs. → *Expect:* clean, hot items throughout.
3. **Unload the bottom rack first.** The reason is physics: cup hollows on the top rack pool water, and pulling the top rack first rains that water onto the dry plates below. Plates in carried stacks sized to your grip (four to six), pots by their handles, straight to their cabinets. → *Expect:* bottom rack empty; nothing dripped on.
4. **Unload the top rack, tipping pooled water into the sink.** Glasses and cups get individual or two-at-a-time grasps, fragile rules in force: no glass-on-glass clinking, reduced speed, full control before release (`embodied/mobility/carry-and-deliver-an-item` step 6's release-is-commitment). → *Expect:* pooled water in the sink, not the floor; glasses shelved upright or rim-down per the cabinet's convention.
5. **Unload cutlery by grasping handles, never blades.** Knives from the basket by their handles regardless of orientation (`load-a-dishwasher` step 5 put blades down; trust but verify by sight before reaching), sorted directly into the drawer's slots. → *Expect:* cutlery sorted, no blade grasped, drawer closed.
6. **Wipe and close the machine.** A quick swipe of the door gasket's ledge where debris collects, filter checked if the machine's schedule calls for it, racks in, door closed, and the clean-indicator reset if the model has one. → *Expect:* machine empty, dry-ish, and unambiguously ready for dirty dishes, so the next person never plays the clean-or-dirty guessing game.

## Decision points

- Still-wet plastic items (plastic never dries in dishwashers): a flick over the sink and a moment in the rack or towel, not wet into a closed cabinet where damp breeds smell.
- Someone else's kitchen: counter-staging by category beats confident wrong shelving; ten seconds of asking beats a week of the owner hunting mugs.
- Hot-glass caution: fresh out of a hot cycle, glass is more thermal-shock fragile; a few minutes of door-open cooling costs nothing before handling stemware.

## Failure modes & recovery

- **F1 Dropped and broke an item:** stop unloading; collect large shards by hand (protected), then damp-paper-towel the fines (`daily/home/wash-dishes-by-hand` F4's glass protocol), check the machine drum floor too, and report the casualty to the owner rather than burying it in the recycling.
- **F2 Gritty film on everything:** the load was dirty or the machine needs salt/rinse-aid or a filter clean; re-run the load and service the consumables (`load-a-dishwasher`'s hard-water variation).
- **F3 Top-rack water rained on dry plates:** the bottom-first order was skipped; towel the plates and file the order as the recipe's one real trick.
- **F4 No home found for an item:** counter staging plus a question; the wrong cabinet is where items go to be lost (`tidy-a-room` F1's lesson).

## Verification

The machine is empty with racks in and door closed, every item is dry, intact, and in its home (or staged-with-question), no blade was grasped, no water hit the floor, and the clean/dirty state of the machine is unambiguous to the next user.

## Variations

- Drawer dishwashers unload one drawer at a time with no rain problem, which deletes step 3's ordering but nothing else.
- Shared households: unloading-promptly is the etiquette twin of `daily/errands/use-a-laundromat` step 4; a clean full machine blocks the sink's queue exactly like a squatted washer.

## Safety & privacy

Medium risk from three familiar sources: steam at opening, blades in the basket, and fragile glass at speed. The pause, the handle-only rule, and the release-is-commitment discipline are the whole protocol.
