---
name: assist-someone-into-a-coat
domain: embodied
subdomain: care
locale: [generic]
interface: physical
difficulty: basic
est_time: 3min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [person, coat, sleeve, zipper, chair, medical-device]
affordances: [ask, orient, guide, insert, adjust, fasten]
workspace: care-space
safety: {hot_surfaces: false, sharp_objects: false, fragile: [glasses, medical-device], human_proximity: pause}
---

## Goal

Help a person put on a coat without forcing joints, disturbing devices, or compromising comfort.

## Preconditions

- The person wants the coat and can indicate discomfort.
- The coat is the correct size and orientation.
- Any IV line, oxygen tube, sling, or sensitive side is known.

## Steps

1. **Ask preference and limits.** Confirm which arm should go first and whether any side hurts. → *Expect:* the person gives a preference or agrees to proceed.
2. **Open the coat fully.** Unzip or unbutton it and find the inside of each sleeve. → *Expect:* sleeves are clear and not twisted.
3. **Support the first sleeve.** Hold the cuff open near the person's hand without pulling the arm. → *Expect:* the person can place their hand into the sleeve.
4. **Guide fabric over the arm.** Slide the sleeve up while the person moves as able. → *Expect:* fabric passes the elbow without snagging.
5. **Bring the coat behind the shoulders.** Keep the collar low and avoid brushing face, glasses, or tubing. → *Expect:* the back panel rests behind the person.
6. **Guide the second sleeve.** Offer the sleeve opening and let the person insert the second hand. → *Expect:* both arms are inside sleeves.
7. **Settle the coat.** Smooth shoulders, cuffs, and back hem while asking about comfort. → *Expect:* the coat sits evenly and does not pull.
8. **Fasten only if requested.** Zip, button, or snap from bottom to top while avoiding skin and devices. → *Expect:* closure is secure or intentionally left open.

## Decision points

- One arm is painful or weak → dress that arm first and remove it last.
- Tubing or wires are present → route the coat around them without disconnecting anything.
- Person says stop → stop immediately and remove or adjust the coat.
- Coat is too tight → choose another coat rather than forcing sleeves.

## Failure modes & recovery

- **F1 Sleeve twist:** detect tight spiral or blocked hand → pull sleeve back and reorient before retrying.
- **F2 Joint strain:** detect grimace, guarding, or verbal pain → stop and lower the arm to a comfortable position.
- **F3 Device snag:** detect tug on tubing, monitor lead, or sling → stop and free the device before moving fabric.
- **F4 Zipper catches:** detect resistance or trapped fabric → back the zipper down and clear the fold.

## Verification

The coat is on with both arms placed comfortably, no device or skin is pinched, and the person confirms the fit is acceptable.

## Variations

- Seated person: keep the back hem clear of wheels or chair hardware.
- One-sided weakness: start with the weaker or painful arm.
- Front-opening jacket: fasten only after checking breathing comfort.

## Safety & privacy

Human proximity requires pause behavior. Ask before touching, preserve modesty when adjusting clothing, and never force a limb through resistance.
