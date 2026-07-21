---
name: turn-a-light-on-and-off
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [light-switch, light-fixture]
affordances: [locate, press, flip, rotate, observe]
workspace: household-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

A light is changed to the intended on or off state and the result is confirmed from the room illumination or switch indicator.

## Preconditions

- The switch or dimmer controlling the light is reachable.
- The actor knows the desired final state: on, off, or dimmed.
- The switch plate is dry and intact.
- The actor can observe the light fixture or the room brightness.

## Steps

1. **Locate the control.** Find the wall switch, lamp switch, pull chain, or dimmer associated with the target light. → *Expect:* the control is identified and reachable.
2. **Check current state.** Observe the fixture, room brightness, or switch indicator. → *Expect:* current on, off, or dim level is known.
3. **Position for operation.** Stand or align the manipulator close enough to move the control without leaning. → *Expect:* finger or gripper reaches the control squarely.
4. **Operate a toggle switch.** Flip the switch fully to the desired direction. [BRANCH: turn on | turn off] move to ON for light; move to OFF for dark. → *Expect:* the switch rests at its end position.
5. **Operate a rocker or button.** Press the active side or center until the switch clicks. → *Expect:* tactile or audible click occurs.
6. **Operate a dimmer variant.** Rotate, slide, or long-press to the target brightness when dimming is required. → *Expect:* brightness changes smoothly toward the target.
7. **Confirm the light state.** Look at the fixture or the illuminated area for one second. → *Expect:* final state matches the intended on, off, or dim level.
8. **Correct if the wrong light changed.** Return the first control to its prior state, then try the adjacent labeled control. → *Expect:* target light changes and unintended light is restored.

## Decision points

- Multiple switches are grouped → use labels, room context, or a one-at-a-time test.
- A dimmer has a separate push switch → press for power state, then adjust brightness.
- Light does not respond → check bulb, fixture switch, breaker, or smart control.
- Wet hands or wet plate → do not touch; dry hands and surface first.
- Someone is sleeping or sensitive to light → warn or use the lowest brightness available.

## Failure modes & recovery

- **F1 No light change:** detect unchanged brightness after operation → try the paired switch or verify power and bulb.
- **F2 Wrong fixture changes:** detect a different light responding → restore it and test another control.
- **F3 Switch feels loose or hot:** detect wobble, buzzing, or heat → stop using it and report an electrical fault.
- **F4 Dimmer flickers:** detect unstable light output → lower or raise slightly; if persistent, turn off and use another light.
- **F5 Pull chain sticks:** detect chain not returning → release tension, avoid jerking, and use another control if available.

## Verification

The target light is in the requested state and the physical control is resting in a stable position after operation.

## Variations

- `lamp-switch`: turn knob or inline rocker on the cord while stabilizing the lamp base.
- `smart-bulb`: use the physical switch only if it is part of the intended control path.
- `motion-sensor`: confirm state by waiting through the sensor delay.
- `three-way-switch`: switch position alone may not indicate state, so verify by light output.

## Safety & privacy

Low risk. Do not operate cracked, wet, hot, or buzzing switches. Changing lights can affect nearby people, visibility, and camera exposure, so confirm the space can tolerate the change.
