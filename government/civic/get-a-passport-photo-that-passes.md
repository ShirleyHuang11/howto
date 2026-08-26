---
name: get-a-passport-photo-that-passes
domain: government
subdomain: civic
locale: [generic, us]
interface: mixed
difficulty: basic
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You produce a passport photo that meets official size, lighting, background, pose, and recency rules so the passport application is not delayed.

## Preconditions

- Current passport photo requirements for the country issuing the passport.
- A plain white or off-white background, even lighting, and a camera or professional photo service.
- No eyeglasses unless the passport authority allows a documented medical exception.

## Steps

1. **Check the issuing country's current rules.** For a US passport, use the State Department passport photo page. → *Expect:* you know the required print size, head size, background, expression, and digital upload rules.
2. **Set up a plain background and light.** Stand several feet from a white or off-white wall with no shadows, texture, objects, or filters. → *Expect:* the background is evenly lit and blank.
3. **Prepare appearance.** Remove eyeglasses, hats, headphones, face coverings, and uniforms unless allowed for religious or medical reasons. → *Expect:* the full face and eyes are visible.
4. **Take the photo straight on.** Face the camera directly with a neutral expression or natural smile if allowed, both eyes open, head centered, and shoulders visible. → *Expect:* the image is sharp, in color, and not tilted.
5. **Crop to the official dimensions.** For US printed photos, make a 2 by 2 inch photo with the head 1 to 1 3/8 inches from chin to top of head. → *Expect:* the photo matches the official composition template.
6. **Check digital requirements if uploading.** For US online use, keep the image square, color, recent, unaltered, and within the portal's pixel and file-size limits. → *Expect:* the upload checker accepts the image or gives a specific fix.
7. **Print on photo-quality paper if mailing.** Use matte or glossy photo paper, not ordinary printer paper. → *Expect:* the printed photo has correct dimensions and no visible pixels, smears, or shadows.
8. **Do a final rejection scan.** Look for shadows, red-eye, glare, eyeglasses, heavy editing, wrong size, old photo, cropped hair, or busy background. → *Expect:* none of the common rejection reasons apply.

## Decision points

- Infant or small child → lay the child on a white sheet or use a covered car seat; no other person may appear in the image.
- Religious head covering → keep it on only if worn daily for religious reasons and the full face is visible.
- Medical device or glasses exception → include required medical documentation if the passport authority requires it.
- Online renewal rejects the upload → follow the portal's error message instead of editing heavily or using filters.

## Failure modes & recovery

- **F1 Head size wrong:** detect by measuring chin-to-head distance on the print → recrop from the original photo and reprint.
- **F2 Background shadows:** detect gray areas or wall texture → retake farther from the wall with softer front lighting.
- **F3 Glasses glare or frames:** detect visible glasses → retake without eyeglasses unless a documented medical exception applies.
- **F4 Digital upload rejected:** detect a portal rejection → upload the unfiltered original, adjust crop only, and check file size and dimensions.
- **F5 Photo too old:** detect that appearance changed or photo is older than allowed → retake within the required recency window.

## Verification

The final photo is recent, in color, correctly sized or accepted by the upload checker, has a plain white or off-white background, and shows a centered full-face view with no disallowed accessories.

## Variations

- `us`: printed passport photos are 2 by 2 inches; the photo must generally be taken within the last 6 months.
- `uk/eu/canada`: dimensions, background tolerance, expression rules, and digital codes differ; use the issuing authority's photo checker.
- `retail photo service`: ask for the country-specific passport format and still inspect the result before leaving.

## Safety & privacy

Medium risk because a rejected photo can delay travel or identity paperwork. Do not use AI retouching, beautification filters, or altered backgrounds beyond ordinary cropping accepted by the passport authority.
