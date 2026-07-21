---
name: put-away-clean-dishes
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [dish-rack, dishwasher, plates, bowls, glasses, mugs, cutlery, pots, cutlery-tray, cabinet, drawer, dish-towel]
affordances: [grasp, stack, place, carry, drawer-open, cabinet-open, sort, wipe]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: true, fragile: [glasses, plates, bowls, mugs], human_proximity: slow}
---

## Goal

Every clean dish from the rack or dishwasher is dry and stored in its home location, cabinets and drawers are closed, and the rack or dishwasher is empty and ready for the next load.

## Preconditions

- A finished load: air-dried rack dishes, or a completed dishwasher cycle.
- Known "homes" for each category. In an unfamiliar kitchen, open cabinets and match what is already inside before placing anything.
- A dry dish towel for items that are still wet.

## Steps

1. **Confirm dryness before anything moves.** Feel the undersides of a few plates and the recessed rims of upside-down mugs and bowls: these trap water even when tops look dry. [BRANCH: dry → proceed | wet spots → towel-dry each piece as you pick it up] → *Expect:* no piece goes into a closed cabinet wet; trapped water breeds smell and spots.
2. **If unloading a dishwasher, do the bottom rack first.** The top rack's cupped items hold puddles that dump onto the bottom rack's dry dishes if you open top-first. → *Expect:* bottom rack cleared with its contents still dry.
3. **Batch by category, not by grab order.** Gather all plates into one stack in hand (4 to 6 max), all glasses in a next pass, cutlery last. One cabinet trip per category instead of one trip per item. → *Expect:* each carry targets exactly one destination; total trips roughly equal to number of categories.
4. **Carry stacks low and level with two hands.** Plates flat against the chest height, never balanced one-handed above shoulder height. → *Expect:* stack arrives at the cabinet without a wobble.
5. **Place plates onto existing stacks, respecting stack limits.** Lower the new stack on top gently; keep any single stack to roughly 8 to 10 dinner plates, and never mix sizes in one stack (small on large slides). → *Expect:* stacks stable and straight; shelf not visibly bowing; a plate can be removed one-handed from the top.
6. **Store glasses and mugs standing, not nested.** Same-shape glasses in rows, open side per house convention (up on closed shelves, down on open shelves that collect dust). Nested glasses stick and crack when separated. → *Expect:* each glass free-standing with a finger's clearance to its neighbors.
7. **Sort cutlery into its tray slots, points down out of the basket.** Grab dishwasher-basket cutlery by the handles, never a fistful of blades. Knives that are sharp go in a block or blade-guard slot, not loose in the tray. → *Expect:* each slot single-category; nothing sharp pointing up where a reaching hand lands.
8. **Big items last: pots, pans, boards.** Heavy pieces to low shelves, lids nested with their pots or in the lid rack. → *Expect:* nothing heavy stored above shoulder height.
9. **Close every door and drawer, and reset the station.** Fold the towel to dry, leave the rack empty (or dishwasher open a crack to air out). → *Expect:* all cabinets flush shut; counters clear; nothing left orphaned on the counter.

## Decision points

- An item has no obvious home → put it on the counter in plain sight and ask, or match the closest category; do not invent a new home in someone else's kitchen.
- A chip or crack is spotted while handling → set the piece aside, do not stack it; a cracked plate under load splits and cuts.
- Someone is working at the counter you need → slow, announce ("behind you, opening this cabinet"), and never reach over their knife or pan.

## Failure modes & recovery

- **F1 Overloaded stack shifts when the cabinet door closes:** clinking or a visible lean → reopen, split the stack in two, re-square both.
- **F2 Wet dish discovered inside a closed cabinet later:** musty smell or water spots → pull the neighbors, towel everything, and leave the cabinet open an hour.
- **F3 Nested glasses stuck together:** never force or twist dry → inner glass filled with cold water, outer dipped in warm water, then they separate; forcing shatters the inner one in your hand.
- **F4 Dropped ceramic while carrying:** stop, keep others (and pets) out, pick large shards by hand into a bag, then damp-paper-towel the floor for fragments before resuming.

## Verification

The rack or dishwasher is empty, every item sits dry in its home category (no mixed stacks, no nested glasses, no blade pointing up), all doors and drawers are closed, and the counter holds nothing but items awaiting a decision.

## Variations

- Open shelving: glasses and mugs stored rim-down against dust; wipe the shelf edge weekly.
- Shared or unfamiliar kitchen: photograph cabinet interiors before the first unload; matching beats guessing.

## Safety & privacy

Low risk. What actually causes injuries here: fistfuls of upturned knives in the cutlery basket, over-tall mixed plate stacks, stuck nested glasses forced apart, and heavy pots stored overhead. All four are prevented by the steps above, none by care alone.
