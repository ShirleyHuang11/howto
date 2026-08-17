---
name: edit-a-photo-on-your-phone
domain: daily
subdomain: play
locale: [generic]
interface: physical
difficulty: basic
est_time: 15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Turn a phone photo into a cleaner finished image using crop, exposure, color, and sharpening adjustments.

## Preconditions

- A phone with a built-in photo editor or editing app.
- One photo you are allowed to edit and save.
- Enough storage to keep the original or a duplicate.

## Steps

1. **Duplicate the photo.** Make a copy before editing if your app allows it. → *Expect:* the original image remains available.
2. **Straighten and crop.** Level obvious horizons, then crop out weak edges without cutting important details. → *Expect:* the subject feels intentionally placed in the frame.
3. **Correct brightness.** Raise exposure if the image is dull or lower highlights if bright areas lack detail. → *Expect:* important parts of the photo are readable without washed-out whites.
4. **Tune contrast gently.** Add a small amount of contrast or black point until the image has shape. → *Expect:* the photo looks clearer without crushed shadows.
5. **Adjust color.** Warm or cool the white balance until skin, paper, or neutral walls look believable. → *Expect:* colors look natural or intentionally stylized.
6. **Add restrained detail.** Apply light sharpening or structure and avoid heavy clarity on faces. → *Expect:* edges look crisp at normal viewing size without gritty texture.
7. **Compare before and after.** Toggle the original view and reduce any adjustment that calls attention to itself. → *Expect:* the edited version improves the photo while still looking credible.
8. **Save or export.** Save a copy at full quality if the app offers that option. → *Expect:* the finished edit appears in the photo library and can be shared.

## Decision points

- Photo is underexposed → lift exposure and shadows before adding contrast.
- Photo has blown highlights → lower highlights first and accept that pure white detail may not return.
- Social posting is the goal → crop to the platform shape before doing fine edits.

## Failure modes & recovery

- **F1 Overedited skin:** detect by waxy or gritty faces → reduce clarity, sharpening, and skin smoothing.
- **F2 Strange color:** detect by gray whites or orange skin → reset white balance and adjust warmth slowly.
- **F3 Cropped too tight:** detect by missing hands, feet, or object edges → restore the crop or start from the duplicate.
- **F4 Lost original:** detect by no untouched version remaining → use undo or restore original before making a new duplicate.

## Verification

The final saved image is level, intentionally cropped, naturally colored or deliberately styled, and visibly improved when compared with the original.

## Variations

- Black-and-white edit: focus on exposure and contrast instead of color temperature.
- Food photo: keep whites neutral and avoid oversaturating reds and greens.
- Night photo: reduce noise expectations and avoid pushing shadows too far.

## Safety & privacy

Low risk. Avoid sharing private faces, addresses, license plates, or location metadata unless everyone involved agrees.
