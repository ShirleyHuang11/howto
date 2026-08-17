---
name: skewer-food-onto-a-stick
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [skewer, food-item, cutting-board, plate, bowl]
affordances: [grasp, align, pierce, slide, space, place]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: true, fragile: [plate, bowl], human_proximity: slow}
---

## Goal

Thread prepared food pieces onto a skewer in a stable order without puncturing hands or splitting the food.

## Preconditions

- Food pieces are cut to sizes the skewer can pass through.
- Skewers are clean; wooden skewers are soaked if they will be grilled.
- A cutting board or plate is clear for assembly.
- Hands or grippers can hold food away from the skewer tip path.

## Steps

1. **Set the skewer orientation.** Hold the blunt end and point the tip down toward the board at a shallow angle. → *Expect:* the sharp tip is visible and aimed away from hands and people.
2. **Pick a food piece.** Grip it at the sides, leaving the intended centerline exposed. → *Expect:* the piece is steady and fingers are not behind the puncture path.
3. **Pierce through the center.** Press the skewer tip into the food and rotate slightly if resistance is high. → *Expect:* the tip emerges on the far side without tearing the piece apart.
4. **Slide the food down.** Push the food along the skewer toward the blunt end, leaving a small gap from other pieces. → *Expect:* the piece stays on the skewer and can rotate only slightly.
5. **Repeat with spacing.** Alternate pieces as desired and keep about 3 to 5 mm between dense pieces for cooking airflow. → *Expect:* the skewer is balanced and not overloaded.
6. **Place on a tray.** Lay the finished skewer flat with the tip pointing inward or away from the tray edge. → *Expect:* the skewer rests without rolling off and the sharp tip is not exposed outward.

## Decision points

- Food splits → use larger pieces, pierce through a thicker section, or switch to a thinner skewer.
- Food is slippery → pat dry before piercing.
- Skewer will go on a grill → leave enough bare handle for turning with tongs.

## Failure modes & recovery

- **F1 Tip points at hand:** detect fingers behind the food along the skewer axis → stop and reposition grip before pressing.
- **F2 Food cracks:** detect a split reaching the edge → remove that piece and use it loose or cut a larger replacement.
- **F3 Overloaded skewer:** detect bending or crowded pieces → remove pieces until the skewer stays straight.
- **F4 Uneven cooking layout:** detect large pieces pressed tightly together → separate pieces or rebuild with similar sizes grouped together.

## Verification

Food pieces are threaded securely with safe spacing, the skewer remains straight, and the sharp tip is oriented away from hands and tray edges.

## Variations

- `fruit-skewer`: use blunt cocktail sticks when serving children.
- `metal-skewer`: expect less flex and keep the tip especially controlled.

## Safety & privacy

Medium risk from puncture hazards. Keep the skewer tip visible, never press toward a palm, and slow down whenever a human hand enters the assembly area.
