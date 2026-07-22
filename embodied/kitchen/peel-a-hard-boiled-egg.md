---
name: peel-a-hard-boiled-egg
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
objects: [hard-boiled-egg, shell, membrane, bowl, water]
affordances: [grasp, tap, crack, roll, peel, rinse]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [egg], human_proximity: continue}
---

## Goal

The shell and membrane are removed from the hard-boiled egg while keeping the cooked white mostly intact.

## Preconditions

- Egg is fully cooked and cool enough to hold.
- Sink, bowl, or trash is ready for shell fragments.
- Running water is available if the shell sticks.

## Steps

1. **Hold the egg gently.** Cup it in one hand with enough support to prevent dropping. → *Expect:* shell stays intact until tapped.
2. **Crack all over.** Tap the egg against the counter, rotating to make many small cracks. → *Expect:* shell shows a network of cracks.
3. **Roll under the palm.** Roll the egg with light downward pressure to loosen the membrane. → *Expect:* shell crackles and separates slightly from the white.
4. **Find the fat end.** Locate the wider end where the air pocket usually sits. → *Expect:* shell feels slightly easier to lift there.
5. **Start under the membrane.** Pick away shell at the fat end until the thin membrane lifts with it. → *Expect:* a flap of shell and membrane comes free.
6. **Peel in sections.** Pull shell pieces away following the curve of the egg. → *Expect:* white surface appears with minimal gouging.
7. **Use running water.** [BRANCH: shell loosens | shell sticks] rinse under a thin stream while peeling under the membrane. → *Expect:* water slips between shell and white.
8. **Rinse and inspect.** Wash off fragments and place the peeled egg in a bowl. → *Expect:* no shell grit remains on the egg.

## Decision points

- Shell sticks tightly → return to the fat end and find the membrane layer.
- Egg is warm and soft → cool in water before applying more pressure.
- Appearance matters → peel more slowly with smaller pieces.

## Failure modes & recovery

- **F1 White gouges:** chunks tear out with shell → get under the membrane and use water to separate layers.
- **F2 Shell fragments remain:** gritty bits cling to wet white → rinse and rub lightly with fingertips.
- **F3 Egg splits:** pressure is too high or egg is undercooked → reduce rolling force and handle in a bowl.
- **F4 Dropped egg:** peeled surface contacts counter or floor → rinse if clean counter, discard if floor contamination is likely.

## Verification

The egg has no shell or membrane patches visible, no gritty fragments remain, and the cooked white is intact enough for the intended use.

## Variations

- Batch peeling: crack and roll several eggs first, then peel each under water.
- Very fresh egg: expect more sticking and use smaller peel motions.

## Safety & privacy

Low risk. Treat the egg as fragile and keep shell fragments out of food-prep areas where they can contaminate other dishes.
