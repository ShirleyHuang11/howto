---
name: ladle-soup-into-a-bowl
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 3min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [ladle, soup, pot, bowl, trivet]
affordances: [grasp, scoop, lift, carry, pour, stabilize]
workspace: kitchen
safety: {hot_surfaces: true, sharp_objects: false, fragile: [bowl], human_proximity: slow}
---

## Goal

Transfer hot soup from a pot into a bowl using a ladle without splashing or overfilling.

## Preconditions

- Pot of soup is stable on a burner turned off, trivet, or counter-safe surface.
- Bowl is heat-safe and stable near the pot.
- Ladle is clean and fits inside the pot.
- Humans are outside the immediate splash path.

## Steps

1. **Set the bowl near the pot.** Place it on a flat surface within one short ladle travel distance. → *Expect:* the bowl does not wobble and its opening is unobstructed.
2. **Grip the ladle handle.** Hold near the end with the bowl of the ladle hanging level. → *Expect:* the ladle can rotate without hitting the pot rim.
3. **Dip below the soup surface.** Lower the ladle bowl-first and draw it toward the center of the pot. → *Expect:* the ladle fills without scraping the pot hard.
4. **Lift and pause over the pot.** Raise the ladle just above the soup and let excess drip back for one second. → *Expect:* the outside of the ladle is not streaming liquid.
5. **Move over the serving bowl.** Keep the ladle level and low while crossing the gap. → *Expect:* the soup remains inside the ladle.
6. **Pour against the bowl interior.** Tilt the ladle so soup runs down the inner side of the bowl, repeating until filled below the rim. → *Expect:* soup sits at least 2 cm below the bowl rim with no splash outside.

## Decision points

- Soup contains large solids → scoop from the pot bottom and pour more slowly.
- Bowl is small → use partial ladles and stop before the safe carry level.
- Soup is boiling → wait until bubbling stops before ladling.

## Failure modes & recovery

- **F1 Splash on rim:** detect droplets outside the bowl → slow the pour and aim at the inner wall, then wipe the rim.
- **F2 Overfilled bowl:** detect soup within 1 cm of rim → remove a partial ladle before carrying.
- **F3 Ladle drips on counter:** detect a drip trail → pause longer over the pot and wipe the path.
- **F4 Pot shifts:** detect pot movement during dipping → stop and stabilize the pot handle with a mitt or move pot to a safer surface.

## Verification

The bowl contains soup below carry height, the pot remains stable, and no hot liquid is on the counter, floor, or outside of the bowl.

## Variations

- `cream-soup`: use slower pours because thick soup clings to the ladle.
- `no-ladle`: use a heat-safe measuring cup with the same low, level carry.

## Safety & privacy

Medium risk from hot liquid and hot pot surfaces. Keep hands away from steam, keep people clear of the pour path, and wipe spills before carrying the bowl.
