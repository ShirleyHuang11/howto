---
name: use-kitchen-tongs
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [kitchen-tongs, food-item, plate, pan, bowl]
affordances: [grasp, squeeze, lift, rotate, release, place]
workspace: kitchen
safety: {hot_surfaces: true, sharp_objects: false, fragile: [plate, bowl], human_proximity: slow}
---

## Goal

Grip, lift, turn, or transfer a food item with kitchen tongs without dropping it or touching unsafe surfaces.

## Preconditions

- Tongs are clean and unlocked.
- The target food item is visible and reachable.
- A receiving surface, plate, pan area, or bowl is stable.
- Hands or gripper can squeeze the tong handles with controlled force.

## Steps

1. **Pick up the tongs by the handles.** Grasp both handles near the hinge-facing half, keeping tips pointed away from faces and edges. → *Expect:* the tongs are held as one tool and the tips open and close when squeezed.
2. **Test the closing force.** Squeeze until the tips meet, then relax until they open about 3 to 5 cm. → *Expect:* the spring action returns the tips open and the tool does not twist in the grip.
3. **Approach the food from the sides.** Align the two tips around the widest stable part of the item, not under liquid or against the pan wall. → *Expect:* the food sits centered between the tong tips.
4. **Clamp with just enough pressure.** Close until the food resists sliding, avoiding crushing soft items. → *Expect:* the food moves with the tongs during a 1 cm test lift.
5. **Lift and move slowly.** Raise only high enough to clear the surface, keep the item over the pan or counter path, and rotate the wrist as needed. → *Expect:* the food stays captured and no drips or crumbs fall outside the work area.
6. **Release at the destination.** Lower until the food touches the plate, bowl, or pan, then open the tips smoothly. → *Expect:* the food lands flat or in the intended orientation and the tongs come away cleanly.

## Decision points

- Food is fragile → clamp nearer the center with lower force and support it from below with a spoon if needed.
- Food is hot or oily → keep the travel path short and avoid hovering over hands or people.
- Tips are silicone-coated → use on nonstick pans; bare metal tips can scratch coatings.

## Failure modes & recovery

- **F1 Food slips:** detect item sliding downward during the test lift → lower it immediately and regrip a wider or less greasy section.
- **F2 Food is crushed:** detect deformation or juices forced out → reduce squeeze force and grip closer to a firm edge.
- **F3 Tong tips cross:** detect one tip riding over the other → release, realign the hinge and tips, then close again.
- **F4 Hot surface contact:** detect handle or hand near pan wall → back out, regrip farther from the hinge, and approach from a cooler side.

## Verification

The food item is transferred, turned, or placed at the target location, and the tongs are still under control with no dropped item or unintended surface contact.

## Variations

- `salad-tongs`: use a lighter squeeze and scoop from below for loose leaves.
- `grill-tongs`: use a longer tool and keep the hand outside the heat plume.

## Safety & privacy

Medium risk around hot pans. Keep tong handles away from burners, keep tips pointed down over the work surface, and slow down when a human hand is within the transfer path.
