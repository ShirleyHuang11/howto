---
name: press-an-elevator-call-button
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [elevator-panel, call-button, indicator]
affordances: [approach, identify, press, release, observe]
workspace: elevator lobby
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: slow}
---

## Goal

The correct elevator call button is pressed and the call indicator confirms the request.

## Preconditions

- Elevator lobby is accessible.
- Desired travel direction is known if separate up and down buttons are present.
- The button panel is reachable without blocking others.

## Steps

1. **Approach the panel.** Stop at arm's length with a clear path for other people. → *Expect:* the call buttons and direction labels are visible.
2. **Identify the desired button.** Locate up, down, or the single call button based on intended travel. → *Expect:* the selected button matches the desired direction.
3. **Position fingertip or tool.** Align the contact point with the center of the selected button face. → *Expect:* the contact point is centered and clear of neighboring buttons.
4. **Press straight inward.** Apply light forward force until the button depresses or clicks. → *Expect:* the button moves inward or gives tactile feedback.
5. **Release fully.** Remove contact without sliding across adjacent buttons. → *Expect:* the button returns or remains lit after release.
6. **Observe the indicator.** Watch for button illumination, chime, or display change. → *Expect:* the selected call indicator is lit or the elevator arrival display changes.

## Decision points

- Both directions are needed by mistake → wait for the correct elevator and avoid pressing both unless necessary.
- Button is already lit → do not press again; the call is already registered.
- Panel is crowded → wait until there is clear hand space.

## Failure modes & recovery

- **F1 No indicator:** detect by no light, sound, or display change after press → press once more with centered contact, then try another panel if available.
- **F2 Wrong direction selected:** detect by the opposite arrow lit → press the correct direction if separate service is available and board only the intended car.
- **F3 Door area obstructed:** detect by people or objects in the doorway → pause movement and keep clear until the area opens.

## Verification

The intended call button indicator is lit or the elevator display/chime shows that a car has been summoned.

## Variations

- Touch panels: tap the labeled area once with a dry fingertip.
- Accessibility buttons: use the larger accessible call button when standard buttons are unreachable.

## Safety & privacy

Move slowly near other people and do not block doors or wheelchair access. No private information is required.
