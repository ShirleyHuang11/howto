---
name: load-a-washing-machine
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: medium
prerequisites: [daily/home/do-the-laundry]
status: draft
last_verified: 2026-07-20
objects: [washing-machine, laundry-basket, clothes, detergent, detergent-drawer]
affordances: [door-open, grasp-fabric, place, drawer-open, pour, dial-turn, button-press]
workspace: home-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

A sorted load of laundry is in the washing machine drum, dosed, and running on the right cycle, with the pre-load checks done that prevent the classic disasters.

## Preconditions

- A sorted pile from `daily/home/do-the-laundry` steps 1 and 2: colors split, pockets emptied, zips closed, delicates and bleed-risks separated out.
- Detergent, and knowledge of the machine's drawer markings (main-wash compartment II, pre-wash I, softener flower symbol, on most front-loaders).

## Steps

1. **Check the drum before loading.** Open the door fully and look inside: forgotten laundry from the last run, a stray sock, or a resident item (the previous user's bra wire). → *Expect:* an empty drum. Wet forgotten laundry gets its own decision: re-run it or line it out, but never bury it under a new load.
2. **Run the pocket-and-fastener pass one item at a time as you load.** Even if sorting "already did it": a tissue or pen at this second gate costs seconds; missed, it costs the whole load (`daily/home/do-the-laundry` F2). Bras into a mesh bag (wires kill drums), hooks and velcro closed, prints turned inside out. → *Expect:* every item pocket-flat, fasteners closed, protectors bagged.
3. **Load loosely to the three-quarter line.** Items dropped in one at a time, not a compressed brick; a hand should fit upright between the load's top and the drum. Overloading is the most common cause of both bad cleaning and drum-bearing wear. → *Expect:* drum at most three-quarters full, contents loose.
4. **Balance heavy items.** A single duvet, towel-heavy loads, or one soaked hoodie among lights will thump the spin; distribute heavy pieces evenly or pair them with similar weights. → *Expect:* no single heavy item alone in an otherwise light load.
5. **Dose detergent into the correct compartment.** Main-wash compartment per the cap's line for the load size and soil level (`do-the-laundry` step 4's under-dosing wisdom); softener only to its max mark; pods go into the drum *under* the clothes, never the drawer. → *Expect:* right product, right compartment, at or below the line.
6. **Select cycle and temperature from the most delicate item in the load.** The care-label read from sorting governs: 30 to 40 °C normal cycle for everyday mixed cottons, delicate cycle and low spin for the fragile pile. → *Expect:* dial and options matching the load's weakest member.
7. **Close the door until it clicks, start, and confirm it took.** Watch for the door lock light and water intake sound in the first minute. Note the end time (`do-the-laundry` step 6: wet clothes wait for no one). → *Expect:* locked door, water sound, cycle time displayed, an alarm set for the end.

## Decision points

- Half loads: use the machine's half-load or eco setting rather than doubling detergent; modern sensors adjust water, but the dose is still yours.
- Mixed doubt items (the maybe-bleeds red shirt): a cold wash quarantines risk; when truly unsure, it washes alone or with darks (`do-the-laundry` step 1's rule).
- Machine smells musty at door-open: run the empty hot maintenance cycle first (`do-the-laundry`'s musty-machine decision point); washing clothes in a smelly machine launders the smell in.

## Failure modes & recovery

- **F1 Thumping, walking machine at spin:** unbalanced load; pause, redistribute or add two towels as ballast, resume. Chronic thumping on balanced loads means feet-leveling or bearings, which is a maintenance flag, not a loading fix.
- **F2 Detergent left sitting in the drawer after the cycle:** water jet misses a gunked drawer; pull the drawer out (release tab), rinse the buildup, and dose slightly lower.
- **F3 Door will not open post-cycle:** most machines hold the lock 1 to 2 minutes after the end; still locked later means water remains — run a drain/spin program before forcing anything.
- **F4 Found the tissue after all:** `daily/home/do-the-laundry` F2's confetti protocol; the second gate (step 2) exists so this stays rare.

## Verification

The drum held only checked, protected items at three-quarters loose; detergent sat in the correct compartment; the cycle matches the weakest fabric; the door locked and water flowed; and the finish alarm is set.

## Variations

- Top-loaders: same rules, agitator models load around the post evenly; pods still go under, not on top of, the clothes.
- Shared or laundromat machines: add the drum-inspection emphasis and the etiquette clock (`daily/errands/use-a-laundromat` steps 2 and 4).

## Safety & privacy

Medium risk to property, not people: the pocket gate, the mesh-bag rule, and load balance carry it. One human rule in shared homes: check the drum for others' laundry and handle it with laundromat courtesy.
