---
name: childproof-a-kitchen
domain: housing
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 1h-3h
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Reduce kitchen risks to children by controlling access to hazards, securing appliances, and making daily cooking safer.

## Preconditions

- You have cabinet latches, drawer latches, appliance locks, stove knob covers, cord shorteners, and wall anchors if needed.
- You know the child's age, reach, climbing ability, and typical supervision pattern.
- You can move hazardous items to higher or locked storage.
- You have permission to install hardware in cabinets or walls if renting.

## Steps

1. **Inspect from a child's height.** Crouch and look for handles, cords, knobs, cleaners, knives, glass, magnets, and small items. → *Expect:* hazards are visible from the child's perspective.
2. **Lock chemical storage.** Move cleaners, dishwasher tablets, alcohol, medicines, and pest products to high locked cabinets. → *Expect:* poisons are not reachable through a low cabinet door.
3. **Install cabinet and drawer latches.** Fit latches on low cabinets, utensil drawers, trash pullouts, and any drawer with sharp or heavy items. → *Expect:* a child cannot open them with normal pulling.
4. **Move sharp and heavy items up high.** Store knives, graters, peelers, food processor blades, cast iron, glassware, and small appliances out of reach. → *Expect:* dangerous items are not available even if a latch fails.
5. **Control the stove.** Add stove knob covers, use back burners, turn pot handles inward, and fit a stove guard if needed. → *Expect:* a child cannot easily turn on heat or pull hot cookware down.
6. **Manage cords and appliances.** Push kettles, toasters, slow cookers, and coffee makers back from edges and shorten cords. → *Expect:* cords cannot be pulled from below.
7. **Secure climb and tip hazards.** Anchor freestanding shelves, lock step stools away, and keep chairs away from counters when unsupervised. → *Expect:* the child has fewer ways to reach counters or pull furniture over.
8. **Check choking and burn hazards.** Remove magnets, batteries, plastic bags, matches, lighters, and hot liquids from reach. → *Expect:* small and hot hazards are outside the child's access zone.
9. **Test and maintain.** [BRANCH: latch holds | latch fails] keep working hardware or replace with stronger hardware. → *Expect:* controls survive normal household use.

## Decision points

- Child climbs well → treat counters and upper drawers as reachable.
- Gas stove present → prioritize knob covers and adult-only ignition control.
- Open shelving → move dangerous items or add doors and locks.
- Rental restrictions → use removable locks where appropriate, but do not compromise safety for aesthetics.

## Failure modes & recovery

- **F1 Latch defeats easily:** detect child opening it → replace with a stronger latch or change storage location.
- **F2 Poison left out during cleaning:** detect active product on counter → keep products in hand or locked away, never unattended.
- **F3 Cord remains reachable:** detect dangling cord → shorten, reroute, or move appliance.
- **F4 Stove control still turns:** detect knob cover gap or loose fit → replace with compatible covers or remove knobs when allowed.
- **F5 Adult forgets new workflow:** detect cabinets left open → simplify storage and add self-closing or visual checks.

## Verification

A child-height walkthrough finds no reachable cleaners, sharp tools, heavy pull-down items, stove controls, hot appliance cords, choking hazards, or unsecured climb and tip hazards.

## Variations

- `toddler`: prioritize latches, stove knobs, cords, and choking hazards.
- `school-age`: add knife rules, microwave rules, and supervised cooking boundaries.
- `small-kitchen`: use high locked bins if cabinet space is limited.
- `rental`: document removable hardware and ask permission for anchors where required.

## Safety & privacy

Childproofing reduces risk but does not replace supervision. High risk comes from burns, poisoning, choking, cuts, appliance pulls, and furniture tip-over. Keep emergency numbers and poison-control contact information accessible to caregivers.
