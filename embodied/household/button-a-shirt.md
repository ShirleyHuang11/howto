---
name: button-a-shirt
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
objects: [shirt, button, buttonhole, placket, collar]
affordances: [grasp, align, pinch, push-through, pull, smooth]
workspace: household
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

The shirt front is closed with each button seated through its matching buttonhole, the plackets aligned, and the collar button handled last if used.

## Preconditions

- Shirt is on the wearer or laid flat with the front panels accessible.
- Buttons and buttonholes are intact and visible.
- Hands are dry enough to pinch small fabric and buttons without slipping.

## Steps

1. **Find the bottom pair.** Trace both plackets to the lowest button and its same-height hole. → *Expect:* button and hole edges meet without diagonal pull.
2. **Align the plackets.** Hold the button side flat behind the hole side so hems and seam lines match. → *Expect:* both front edges stack evenly.
3. **Pinch the button.** Grip the button rim between thumb and index finger, not the thread shank. → *Expect:* button tilts while remaining attached and centered.
4. **Open the hole.** With the other thumb and index finger, spread the buttonhole lips into a narrow oval. → *Expect:* the slot exposes enough space for the button edge.
5. **Angle the button through.** Lead one edge of the button through the hole, then roll the rest of the button after it. → *Expect:* part of the button appears on the outside face.
6. **Pull the fabric over.** Draw the hole-side placket around the button while pushing the button forward gently. → *Expect:* button pops fully through and lies flat.
7. **Continue bottom-up.** Repeat each matched pair upward, checking alignment after every button. [BRANCH: skipped hole | correct pair] → *Expect:* no puckers or crossed plackets appear.
8. **Button the collar last.** If desired, use lighter force at the neck and stop if it constricts. → *Expect:* collar closes without pressure on the throat.

## Decision points

- Button will not fit → verify the correct hole before adding force.
- Plackets look twisted → undo to the last aligned button and restart from that point.
- Collar feels tight → leave it open or use a top button extender.

## Failure modes & recovery

- **F1 Mismatched button:** hem lengths differ or fabric spirals → unbutton upward to the first mismatch and redo bottom-up.
- **F2 Button stuck halfway:** button edge catches on thread → flatten the button, back it out, reopen the hole, and retry at a shallower angle.
- **F3 Fabric pinched:** wrinkle trapped under the button → pull the surrounding placket flat and reseat the button.
- **F4 Loose button:** button wobbles or thread stretches → avoid tugging and schedule repair before washing.

## Verification

All chosen buttons pass through their matching holes, both plackets hang evenly from hem to collar, and no button is under visible strain.

## Variations

- `left-over-right`: reverse hand roles while keeping the same bottom-up matching rule.
- Thick buttons: widen the hole with both thumbs and roll the button through more slowly.

## Safety & privacy

Low risk. Avoid pressing hard at the collar or pulling loose buttons, since thread failure can detach a small part.
