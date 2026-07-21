---
name: make-a-bed-neatly
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [mattress, fitted-sheet, flat-sheet, duvet, duvet-cover, pillow, pillowcase]
affordances: [grasp, lift, tuck, pull-taut, smooth, fold, place]
workspace: household
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: pause}
---

## Goal

The bed is made with wrinkle-free tensioned sheets in the correct layer order, the duvet squared to the mattress, and pillows placed. Written so a bimanual robot can execute it as a sequence of graspable, verifiable states.

## Preconditions

- A cleared mattress: nothing (person, pet, laundry) on it. Human_proximity is pause because tensioning and lifting sweep the whole bed surface.
- The correct linens for the mattress size, right-side-out, and the deep-pocket depth of the fitted sheet matching the mattress thickness.
- Access to all four sides of the bed, or the ability to reach across for the far side.

## Steps

1. **Strip check.** [BRANCH: bed already bare → skip to step 2 | linens on it → remove and clear] Confirm the mattress top is empty and the fitted sheet, if present, is being changed or reused per plan. → *Expect:* bare mattress top, all four corners visible, no bunched fabric underneath.
2. **Orient the fitted sheet.** Identify the deeper pockets, which are the short ends on most sheets, and align them to the head and foot. Reading the sheet wrong here forces a full restart, so verify before the first corner. → *Expect:* short-end pockets aligned to short mattress ends, sheet label at a bottom corner.
3. **Seat two diagonal corners first.** Pull the sheet fully over one top corner, then the diagonally opposite bottom corner. Diagonals distribute tension so the sheet cannot walk off a corner as you work the next. → *Expect:* two opposite corners fully seated, elastic gripping under the mattress edge.
4. **Seat the remaining two corners and tension.** Fit the last two corners, then run both hands from center to edges to pull the top surface flat. → *Expect:* no wrinkles or slack on the sleeping surface; a flat hand sweep meets no ridges; corners stay put under a tug.
5. **Lay the flat sheet.** Spread it wrong-side-up (so the finished hem shows when folded down), top hem level with the mattress head, even overhang on both long sides. → *Expect:* equal side overhang within a hand's width; top hem square to the head edge.
6. **Add the duvet, squared.** Lay the duvet over the flat sheet, its top edge one hand-width below the mattress head so the flat sheet can fold back over it. Square the duvet: equal overhang left and right, foot edge parallel to the mattress foot. → *Expect:* duvet centered, side overhangs equal, foot edge parallel not skewed.
7. **Fold the flat sheet back over the duvet's top edge.** Turn the top sheet down over the duvet in a crisp band. → *Expect:* an even fold line running straight across the bed, hem side showing.
8. **Optional hospital corners on the foot (flat-sheet beds).** Tuck the foot overhang under, lift the side drape to a 45-degree fold, tuck the underneath, drop the top flap. → *Expect:* a clean angled corner at each foot corner; drape hangs flat.
9. **Place pillows.** Insert into cases (grasp the pillow by a short end, gather the case, pull it over), then set them squared at the head, standing or flat per style. → *Expect:* pillows fully in cases with corners filled, top edges aligned, centered on the bed width.
10. **Final smooth.** One pass with a flat hand over the whole visible surface. → *Expect:* no wrinkles across the duvet top; overhangs even on both sides; the bed looks symmetric from the foot.

## Decision points

- Fitted sheet keeps popping off a corner → the pocket depth is smaller than the mattress; add sheet suspenders or a deeper sheet rather than fighting it.
- Duvet inside cover has shifted into a lump → do the cover-shake or roll method to redistribute fill before squaring, not after.
- No flat sheet in the setup (duvet-only, common in Europe) → skip steps 5, 7, and 8; square and center the duvet directly.

## Failure modes & recovery

- **F1 Diagonal wrinkle across the fitted sheet:** appears after all four corners are on → one corner seated with the sheet rotated; unseat the nearest corner, re-square, reseat. Center-out tensioning prevents recurrence.
- **F2 Uneven side overhang:** one side drapes to the floor, the other rides up → the top layer was laid off-center; lift and recentre rather than tugging one side, which only transfers the error.
- **F3 Pillow corners empty:** case put on without filling the corners → reach in and push each pillow corner into its case corner; a robot should grasp-and-seat each corner explicitly.
- **F4 Sheet reads inside-out mid-make:** seam or label showing on top → catch it at step 2; if found later, the flat sheet can be flipped in place, but a fitted sheet must be fully restripped.

## Verification

Flat-hand sweep across the sleeping and duvet surfaces meets no ridges; both long-side overhangs are equal within a hand's width; the duvet foot edge is parallel to the mattress foot; pillows are cased with filled corners and aligned at the head; viewed from the foot, the bed is left-right symmetric.

## Variations

- Robot execution: represent each corner as a discrete grasp-stretch-seat primitive with a post-condition tug test; tension checks become flatness scans of the surface point cloud.
- Duvet-only (continental) style: no flat sheet or hospital corners; the neatness criterion is duvet squareness and even fill.
- Two-person make: partners work opposite long sides, mirroring each tuck; halves the time and improves tension symmetry.

## Safety & privacy

Low risk. Lifting a mattress corner is the only physical load; lift with the legs and keep the far-side reach within balance to avoid a twisting strain. No privacy exposure.
