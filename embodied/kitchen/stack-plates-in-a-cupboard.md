---
name: stack-plates-in-a-cupboard
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 3min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [plates, cupboard, shelf]
affordances: [grasp, lift, align, lower, stack]
workspace: kitchen cupboard
safety: {hot_surfaces: false, sharp_objects: false, fragile: [plates], human_proximity: slow}
---

## Goal

Plates are stacked flat in a cupboard with aligned edges and stable shelf clearance.

## Preconditions

- Plates are clean, dry, and cool.
- Cupboard shelf is clear and rated for the plate weight.
- Plate sizes are compatible or can be separated by size.

## Steps

1. **Clear the shelf.** Remove loose objects from the intended stack footprint. → *Expect:* a flat shelf area wider than the plate diameter is open.
2. **Place the largest plate first.** Grip opposite rim edges with both hands and lower the plate flat onto the shelf. → *Expect:* the plate sits level with no rocking.
3. **Lift the next plate level.** Hold opposite sides and keep the eating surface facing upward. → *Expect:* the plate remains horizontal during movement.
4. **Align over the stack.** Center the plate above the lower plate with rims matching. → *Expect:* the lower rim is evenly visible around the top plate.
5. **Lower with minimal impact.** Descend slowly until ceramic contacts ceramic. → *Expect:* the plate lands quietly and does not slide.
6. **Repeat by size.** Continue largest to smallest, keeping each plate centered. → *Expect:* the stack remains vertical and edges form an even column.
7. **Check clearance and weight.** Release the stack and observe shelf sag and door clearance. → *Expect:* the shelf stays level and the cupboard door can close.

## Decision points

- Different plate sizes are mixed → create separate stacks by diameter.
- Stack grows tall or heavy → split into two shorter stacks.
- Plate has chips or cracks → remove it from normal storage.

## Failure modes & recovery

- **F1 Plate slides:** detect by rim offset after lowering → lift the top plate and re-center with slower descent.
- **F2 Stack wobbles:** detect by rocking after release → remove plates until stable and inspect for uneven plate shapes.
- **F3 Shelf clearance fails:** detect by door or upper shelf contacting stack → lower stack height or move plates.

## Verification

The plate stack is centered, flat, stable after release, and the cupboard door closes without touching it.

## Variations

- Fine china: place felt or paper separators between plates.
- Deep plates: stack separately from flat dinner plates to avoid rocking.

## Safety & privacy

Plates are fragile and can injure if dropped. Use two-hand grips and avoid stacking above comfortable shoulder height.
