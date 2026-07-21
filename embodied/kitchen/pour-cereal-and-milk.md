---
name: pour-cereal-and-milk
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [bowl, cereal-box, cereal-bag, milk-container, spoon]
affordances: [grasp, open, pour, tilt, set-down, carry]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [bowl], human_proximity: continue}
---

## Goal

A bowl contains cereal and milk at a comfortable level, with no overflow, spills, or crushed packaging left open.

## Preconditions

- A clean bowl and spoon are available.
- Cereal is edible and the inner bag is open or can be opened.
- Milk is fresh and pourable.
- A clear counter or table space is available.

## Steps

1. **Place the bowl on a flat surface.** Center it away from the counter edge. → *Expect:* the bowl stays stable when lightly tapped.
2. **Open the cereal carefully.** Open the box top and inner bag without tearing a giant side hole. → *Expect:* the bag opening forms a controlled spout.
3. **Pour cereal first.** Tilt the box or bag slowly over the bowl until the bowl is about half to two-thirds full. → *Expect:* cereal lands in the bowl with headroom left.
4. **Set the cereal down upright.** Close or fold the inner bag before returning attention to the bowl. → *Expect:* the cereal package does not keep spilling.
5. **Open the milk container.** Remove cap or open spout and check smell if freshness is uncertain. → *Expect:* milk smells normal and the opening is clear.
6. **Pour milk to the target level.** [BRANCH: light milk | milk-heavy] pour around the cereal edges until the lower cereal floats, or continue until milk sits just below the top cereal layer. → *Expect:* liquid stays below the bowl rim.
7. **Stop before overflow.** Level the container upright when milk is 1 to 2 cm below the rim. ⚠️ *Irreversible:* spilled milk soaks cereal and surfaces quickly, so stop early rather than trying to fill to the brim. → *Expect:* the bowl can be lifted without sloshing.
8. **Carry and set down smoothly.** Put spoon in the bowl, lift with one or two hands, and set it on the eating surface before releasing. → *Expect:* the bowl arrives level, with no trail of milk or cereal.

## Decision points

- Bowl is too small → switch bowls before adding milk.
- Cereal bag tears wide open → fold the tear into a spout or pour cereal into a storage container.
- Milk is sour, chunky, or past safe use → do not pour it, and choose another milk or dry cereal.
- You need to carry across a room → carry the bowl and spoon separately if the bowl is very full.

## Failure modes & recovery

- **F1 Cereal avalanche:** detect cereal bouncing out of the bowl → lower the box, reduce tilt, and sweep dry pieces back or discard.
- **F2 Milk overpour:** detect milk near the rim → stop, sip or spoon out a little, then wipe the bowl exterior.
- **F3 Soggy delay:** detect cereal sitting too long before eating → pour a smaller bowl next time or add milk at the table.
- **F4 Sticky spill:** detect milk on counter or floor → wipe immediately with a damp cloth, then dry the walking surface.

## Verification

The bowl contains cereal and milk below the rim, the spoon is present, packages are closed, and the counter or table is dry.

## Variations

- `milk-first`: possible, but cereal floats and splashes more easily, so pour lower and slower.
- `plant-milk`: shake the container before opening if the label says separation is normal.
- `child-serving`: use a wider bowl, less milk, and carry it for the child if needed.

## Safety & privacy

Low risk. The main hazards are broken bowls, slippery milk spills, and spoiled dairy. Keep glass bowls away from counter edges and clean spills before anyone steps on them.
