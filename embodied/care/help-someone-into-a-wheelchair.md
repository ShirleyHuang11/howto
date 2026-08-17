---
name: help-someone-into-a-wheelchair
domain: embodied
subdomain: care
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 10min
risk: high
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [person, wheelchair, brakes, footrests, gait-belt, chair]
affordances: [ask, brake-lock, position, support, pivot, sit, stabilize]
workspace: care-space
safety: {hot_surfaces: false, sharp_objects: false, fragile: [glasses, medical-device], human_proximity: pause}
---

## Goal

Assist a person into a wheelchair only with consent, proper setup, and enough ability or trained help for a safe transfer.

## Preconditions

- The person is awake, agrees to transfer, and can participate unless trained lift equipment is being used.
- The wheelchair is the correct chair for the person.
- Brakes, footrests, and path are accessible.

## Steps

1. **Confirm readiness.** Ask about pain, dizziness, weakness, and preferred transfer method. → *Expect:* the person consents or the task pauses.
2. **Position the wheelchair.** Place it close to the stronger side if known, angled slightly toward the person. → *Expect:* the transfer path is short and clear.
3. **Lock both brakes.** Engage brakes and test that the chair does not roll. → *Expect:* the wheelchair stays still when pushed lightly.
4. **Move footrests aside.** Swing away or remove footrests before the person stands or pivots. → *Expect:* no metal parts block feet.
5. **Prepare support.** Apply a gait belt if trained and place walker or helper stance as prescribed. → *Expect:* support is ready before movement starts.
6. **Cue the stand or slide.** [BRANCH: stand-pivot | slide-board] guide the agreed method without pulling arms or lifting dead weight. → *Expect:* the person begins moving with control.
7. **Guide hips to the chair.** Keep close support while they turn or slide until hips contact the wheelchair seat. → *Expect:* the person is centered over the seat, not the wheel or armrest.
8. **Lower and settle.** Help them sit fully back, then place feet on footrests if appropriate. ⚠️ *Irreversible:* an uncontrolled fall can injure the person; stop and call for trained help if weight bearing or balance is uncertain. → *Expect:* the person is seated upright with feet supported.
9. **Confirm comfort and safety.** Check brakes, posture, clothing, tubing, and lap belt if used. → *Expect:* nothing is pinched, dragged, or unstable.

## Decision points

- Person refuses or appears confused → pause and get consent or a qualified decision-maker.
- Person cannot bear weight → do not lift manually; use trained lift equipment or additional help.
- Wheelchair moves despite brakes → do not transfer until chair or surface is stabilized.
- Pain, dizziness, or shortness of breath appears → return to a safe seated or lying position and seek help.

## Failure modes & recovery

- **F1 Knees buckle:** detect sudden lowering or loss of leg support → guide to nearest safe surface or floor and call for help.
- **F2 Chair rolls:** detect movement during transfer → stop, reseat if possible, and fix brakes or wheel chocks.
- **F3 Foot caught:** detect foot under footrest or caster → pause, support body, and free the foot before continuing.
- **F4 Off-center landing:** detect hips on wheel, armrest, or edge → keep brakes locked and reposition with consent or assistance.

## Verification

The person is seated fully in the wheelchair, brakes are locked, feet and medical devices are clear of moving parts, and the person confirms they are comfortable or stable.

## Variations

- Mechanical lift: follow the lift plan and sling instructions instead of manual transfer.
- Two-person assist: one trained helper leads the transfer and the second guards the weaker side.
- Slide board: ensure both surfaces are level and the board is secure before weight shifts.

## Safety & privacy

High risk human-contact task. Explain each touch before it happens, pause on refusal or uncertainty, protect clothing and dignity, and never manually lift a person who cannot assist.
