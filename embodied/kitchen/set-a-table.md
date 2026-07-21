---
name: set-a-table
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
objects: [dining-table, plates, forks, knives, spoons, glasses, napkins, chairs]
affordances: [grasp, place, carry, align]
workspace: dining-room
safety: {hot_surfaces: false, sharp_objects: true, fragile: [plates, glasses], human_proximity: slow}
---

## Goal

The dining table is set for N diners with a complete, consistently arranged place setting at each seat.

## Preconditions

- The number of diners N and the meal type (everyday vs. multi-course) is known.
- The table surface is clear and wiped; chairs are at their seats.
- Clean tableware for N settings is available: plate, fork, knife, spoon, glass, napkin each.

## Steps

1. **Confirm the seat positions.** One setting per chair, centered on the chair's position, ~2 cm from the table edge. → *Expect:* N positions identified, evenly spaced, no setting straddling a table leg or corner awkwardly.
2. **Carry and place the plates.** Carry plates in a stable stack of ≤ N (both hands or against the chassis), then place one plate at each position's center. → *Expect:* one plate per seat, centered, ~2 cm from the edge; stack emptied without chips or clinks.
3. **Place the forks.** Fork on the *left* of each plate, tines up, aligned with the plate's bottom edge. → *Expect:* each fork parallel to the plate, consistent spacing (~1 cm from plate rim).
4. **Place the knives and spoons.** Knife on the *right* of the plate, blade facing *inward* toward the plate; spoon to the right of the knife. ⚠️ *Irreversible:* none, but blades outward read as careless and snag reaching hands — blade-in is the rule. → *Expect:* right side of each setting reads knife-then-spoon outward, blades in.
5. **Place the glasses.** Above the knife tip (upper right of the plate), upright. Fragile — individual grasps, no stacking, reduced speed over the table. → *Expect:* one glass per setting, upper right, stable and not touching other items.
6. **Place the napkins.** Folded napkin either on the plate's center or under the fork, consistently — pick one style for the whole table. → *Expect:* all N settings use the same napkin placement.
7. **Add shared items to the table's center.** Water pitcher/bottle, salt and pepper, serving trivets if hot dishes are coming, within reach of all seats. → *Expect:* shared items centered, leaving clearance in front of every setting.
8. **Final pass around the table.** Walk/scan the full circumference: every setting complete and aligned the same way; chair access unobstructed. → *Expect:* N identical complete settings; nothing missing or extra.

## Decision points

- Multi-course/formal meal → work outside-in: additional forks left (salad outermost), soup spoon outermost right, dessert cutlery horizontal above the plate; bread plate upper left.
- Fewer matching sets than diners → distribute mismatches so each *setting* is internally consistent, rather than one seat getting all odd items.
- Children's seats → sturdier tableware, glass replaced by a stable cup, knife omitted for young children.

## Failure modes & recovery

- **F1 Dropped/chipped item:** stop placement, collect all fragments (check a broom-width radius — shards travel), verify no fragments on chairs or settings, fetch a replacement.
- **F2 Table too small for N full settings:** shrink the setting (glass moved inward, shared napkin dispenser) rather than overlapping settings; overflow diners get a second table or sequential seating.
- **F3 Tableware inventory short mid-task:** count first next time (precondition); recover by washing needed items or substituting a consistent alternative for one complete category (all paper napkins, not some).

## Verification

Walking the table's full circumference: N settings, each with plate centered, fork left, knife (blade in) then spoon right, glass upper right, napkin in the chosen style; shared items reachable from every seat; no chips, water spots, or misalignments.

## Variations

- Chopstick settings (`cn`, `jp`): chopsticks on a rest to the right or below the plate (jp: horizontal below, tips left); spoon for soup; no knife at the setting.
- Buffet-style: stacks of plates and rolled cutlery at the line's start replace per-seat settings; the table gets only glasses and napkins.

## Safety & privacy

Low risk. Knives carried point-down and placed blade-in; glass and ceramic get individual grasps with reduced speed; slow all motion when diners are already seated at the table being set.
