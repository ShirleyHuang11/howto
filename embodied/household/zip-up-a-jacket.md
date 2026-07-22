---
name: zip-up-a-jacket
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
objects: [jacket, zipper, slider, insertion-pin, zipper-box, hem]
affordances: [grasp, align, insert, brace, pull, guide]
workspace: household
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

The jacket zipper is started cleanly, pulled straight to the desired height, and closed without fabric caught in the teeth.

## Preconditions

- Jacket is on the wearer or laid front-up with the zipper halves accessible.
- Slider is at the bottom box and the teeth are free of lint or fabric folds.
- Hem is not twisted and both zipper tapes can meet without tension.

## Steps

1. **Lower the slider fully.** Pull the tab down until the slider rests against the zipper box. → *Expect:* the box opening is exposed and stationary.
2. **Align the zipper halves.** Bring the insertion pin side to the box side with both hems at the same height. → *Expect:* zipper tapes lie parallel.
3. **Seat the insertion pin.** Push the pin straight down into the box until it bottoms out. → *Expect:* no gap remains between pin tip and box floor.
4. **Hold the hem.** Pinch both lower hems together below the slider to keep the pin seated. → *Expect:* the bottom stays aligned when the tab is touched.
5. **Pull straight up.** Draw the tab upward along the centerline with steady light force. → *Expect:* teeth interlock immediately above the slider.
6. **Guide fabric away.** Keep loose lining, scarf edges, or shirt fabric outside the slider path. → *Expect:* slider moves without scraping or bunching.
7. **Continue to height.** [BRANCH: full close | partial vent] stop at the planned position without yanking. → *Expect:* zipper track is closed below the slider.
8. **Settle the front.** Smooth both sides downward and release the hem grip. → *Expect:* jacket front hangs flat with the slider staying in place.

## Decision points

- Slider rises but teeth split below → pin was not fully seated, so unzip and restart.
- Force increases sharply → stop before the slider bites fabric and inspect the path.
- Bottom edges are uneven → realign hems before inserting the pin.

## Failure modes & recovery

- **F1 Pin not seated:** zipper separates from the bottom → pull slider down, push pin fully into the box, then retry.
- **F2 Fabric caught:** slider stops and cloth wrinkles into it → reverse a few millimeters, pull fabric sideways, and continue gently.
- **F3 Teeth misaligned:** track feels rough or diagonal → unzip fully and restart with both tapes parallel.
- **F4 Tab slips:** grip loses contact → pinch the tab hole or use a larger fingertip pad instead of fingernails.

## Verification

The zipper is closed from the box to the chosen height, the bottom remains joined, and the slider moves no fabric other than the zipper tape.

## Variations

- Two-way zipper: seat both sliders at the box before inserting the pin.
- Stiff outdoor jacket: brace the hem more firmly and pull in shorter increments.

## Safety & privacy

Low risk. Keep skin, hair, and loose clothing away from the slider path, especially near the neck.
