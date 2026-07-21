---
name: make-a-milkshake
domain: daily
subdomain: food
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Make a cold, thick milkshake that pours slowly, tastes like the chosen flavor, and does not become watery from overblending.

## Preconditions

- Ice cream, milk, a blender, and a chilled glass are available.
- Mix-ins such as syrup, fruit, cookies, or malt powder are ready.
- The blender jar and lid are clean and assembled correctly.

## Steps

1. **Soften the ice cream slightly.** Let it sit 5 minutes until a scoop presses in without bending the spoon. → *Expect:* the ice cream is soft at the edges but not melted.
2. **Load ice cream first.** Add 2 to 3 large scoops per serving to the blender. → *Expect:* the jar is mostly filled with ice cream, not liquid.
3. **Add minimal milk.** Start with 30 ml to 60 ml milk per serving. → *Expect:* milk sits around the ice cream but does not cover it.
4. **Add flavoring.** Add syrup, vanilla, fruit, cookies, or malt powder in small amounts. → *Expect:* flavoring is in the jar before blending starts.
5. **Pulse instead of running.** Blend in short pulses, stopping to tamp or stir with the blender off if needed. → *Expect:* the mixture moves without turning thin.
6. **Check thickness.** Stop as soon as no large ice cream chunks remain. → *Expect:* the shake mounds briefly on a spoon.
7. **Fix texture.** [BRANCH: too thick | too thin] add a splash of milk for too thick, or add more ice cream for too thin. → *Expect:* the correction changes thickness without diluting flavor.
8. **Blend once more briefly.** Pulse 1 to 3 times after any correction. → *Expect:* the shake is smooth but still cold and thick.
9. **Serve cold.** Pour into the chilled glass immediately. → *Expect:* the shake slides slowly and frost forms on the glass.
10. **Finish and clean.** Add whipped cream or toppings if using, then rinse the blender before residue dries. → *Expect:* the shake is ready and the jar rinses clean quickly.

## Decision points

- Blender stalls → stop, unplug if needed, and add a tiny splash of milk before pulsing again.
- Shake tastes weak → add more ice cream or concentrated flavor, not more milk.
- Fruit is frozen solid → chop small or let it soften briefly so it blends before the ice cream melts.

## Failure modes & recovery

- **F1 Watery shake:** detect a fast-pouring texture, recover by adding more ice cream and pulsing briefly.
- **F2 Icy chunks:** detect hard bits in the straw, recover by letting ingredients soften and blending in short pulses.
- **F3 Blender air pocket:** detect spinning blades with no movement, recover by stopping and stirring the jar contents down.
- **F4 Too sweet:** detect syrup dominating the flavor, recover by adding plain ice cream or a pinch of salt.

## Verification

The milkshake is smooth, cold, and thick enough to coat a spoon before being served.

## Variations

- `malt`: add malted milk powder with the flavoring and taste before adding extra syrup.
- `extra-thick`: use less milk and serve with a spoon instead of a straw.

## Safety & privacy

Low risk. Keep hands and utensils out of the blender while plugged in, secure the lid before pulsing, and refrigerate or discard leftovers promptly.
