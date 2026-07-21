---
name: change-bed-sheets
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [bed, mattress, fitted-sheet, flat-sheet, duvet-cover, pillowcase, pillow, laundry-basket]
affordances: [grasp, lift, pull, tuck, align, shake, fold]
workspace: bedroom
safety: {hot_surfaces: false, sharp_objects: false, fragile: [lamp, bedside-glass], human_proximity: continue}
---

## Goal

Remove used bed linens and make the bed with clean fitted sheet, top layer, and pillowcases so the sleeping surface is smooth and ready.

## Preconditions

- Clean fitted sheet sized for the mattress.
- Clean flat sheet, duvet cover, blanket, or comforter as used by the bed.
- Clean pillowcases for each pillow.
- Laundry basket or hamper nearby.

## Steps

1. **Clear the bed area.** Move phones, books, glasses, and breakables from the bed and nearby edges. → *Expect:* bedding can move without knocking items down.
2. **Strip pillowcases.** Pull each pillowcase off by turning it inside out around the pillow. → *Expect:* pillows are bare and used cases are in the laundry basket.
3. **Remove top layers.** Fold back blanket, duvet, or flat sheet and place washable used linens in the basket. → *Expect:* only the fitted sheet remains on the mattress.
4. **Remove the fitted sheet.** Lift one corner at a time and release the elastic from under the mattress. → *Expect:* the mattress surface is bare.
5. **Check the mattress pad.** Smooth it or replace it if wet or dirty. → *Expect:* the pad lies flat with corners secured.
6. **Orient the clean fitted sheet.** Find the long side and corner seams before stretching it onto the bed. → *Expect:* seams line up with mattress corners.
7. **Secure fitted corners.** Hook the far corners first, then near corners, lifting the mattress just enough to tuck elastic under. → *Expect:* elastic wraps under all four corners.
8. **Smooth the fitted sheet.** Pull wrinkles toward the edges and tuck any loose sides. → *Expect:* the sleeping surface is flat and taut.
9. **Add flat sheet or duvet.** [BRANCH: flat sheet | duvet] align the top edge evenly, or shake the duvet into place. → *Expect:* both sides hang about the same length.
10. **Tuck or fold the foot.** For a flat sheet, tuck the foot end under the mattress. → *Expect:* the sheet stays anchored when lightly pulled.
11. **Dress pillows.** Insert pillows into clean cases, corners first, then shake and flatten. → *Expect:* pillow corners fill the case corners.
12. **Finish the top.** Place pillows at the head and smooth the top layer. → *Expect:* the bed looks even and ready to use.

## Decision points

- If a fitted corner pops off → rotate the sheet or use deeper-pocket sheets.
- If using a duvet cover → turn the cover inside out, grab duvet corners, and shake it down.
- If making hospital corners → tuck the foot, lift the side flap at 45 degrees, tuck the hanging side, then fold the flap down.
- If linens are damp → do not make the bed until they are fully dry.

## Failure modes & recovery

- **F1 Wrong sheet size:** detect corners cannot reach or fabric sags badly → replace with the correct mattress size.
- **F2 Corner releases:** detect elastic popping off after smoothing → secure far corners deeper under the mattress.
- **F3 Duvet bunches:** detect lumpy cover → hold two corners and shake from the head end.
- **F4 Back strain:** detect awkward lifting or twisting → work one corner at a time and bend knees instead of hunching.

## Verification

The mattress is covered by a clean fitted sheet with all four corners secured, top bedding is even, and every pillow has a clean pillowcase.

## Variations

- Minimal bed: fitted sheet and pillowcase only.
- Layered bed: add flat sheet, blanket, duvet, and decorative pillows in that order.
- Shared bed: work from opposite sides to reduce lifting and walking.

## Safety & privacy

Low risk. Watch for fragile items on bedside tables, avoid twisting while lifting a heavy mattress, and place soiled linens directly into laundry rather than on shared furniture.
