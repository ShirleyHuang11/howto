---
name: switch-off-a-power-strip
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [power-strip, power-switch, plug, indicator-light]
affordances: [locate, inspect, press, observe]
workspace: household-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

A power strip is switched off in a safe order and the off state is confirmed by the switch position or indicator light.

## Preconditions

- The actor can access the power strip without pulling on cords.
- Devices connected to it can tolerate power loss.
- Hands, floor, and power strip are dry.
- The switch and indicator are visible or reachable.

## Steps

1. **Identify the correct strip.** Trace or visually confirm the strip serving the intended devices. → *Expect:* target power strip is distinguished from nearby strips.
2. **Check connected devices.** Look for computers, medical devices, chargers, lamps, or appliances attached to the strip. → *Expect:* no critical device requires continuous power.
3. **Stop sensitive devices first.** Shut down or unplug devices that need an orderly power-off before using the strip switch. → *Expect:* devices that could lose data are already off or safe.
4. **Stabilize the strip.** Hold the strip body or press it gently against the floor or desk without touching plug prongs. → *Expect:* strip does not slide when the switch is pressed.
5. **Locate the main switch.** Find the rocker, toggle, or push button, usually near the cord entry. → *Expect:* switch actuator and current indicator state are known.
6. **Press to off.** Move the switch to OFF or press the unlit side until it clicks. ⚠️ *Irreversible:* active device power may be cut; confirm step 2 before pressing. → *Expect:* switch rests in the off position.
7. **Confirm indicator off.** Observe the lamp or LED on the strip and any powered devices. → *Expect:* strip indicator is dark and connected devices lose standby lights as expected.
8. **Leave cords undisturbed.** Release the strip and route feet or wheels away from cords. → *Expect:* plugs remain seated and cords are not under tension.

## Decision points

- A device appears critical or unknown → ask the owner before switching off.
- Strip is warm, buzzing, or smells burnt → stop, avoid touching plugs, and disconnect upstream only if safe.
- Switch label is unclear → use indicator light and device response to verify.
- Strip is behind furniture → move furniture enough to see, not by pulling cords.
- Wet area is present → do not operate until dry.

## Failure modes & recovery

- **F1 Wrong strip selected:** detect unintended device response → switch it back on if safe and identify the correct strip.
- **F2 Switch does not move:** detect stuck actuator → stop pressing and unplug upstream only if instructed.
- **F3 Indicator stays on:** detect lit LED after switch off → check whether it is a surge indicator or whether switch is not fully off.
- **F4 Plug loosens:** detect partial plug exposure → keep fingers off prongs and push plug fully in only if power is off and dry.
- **F5 Device alarms:** detect beeping or warning lights → restore power if safe and notify the owner.

## Verification

The intended power strip switch is in the off position and its power indicator or connected device indicators confirm no output power.

## Variations

- `surge-protector`: note that a protected or grounded light may remain on even when load power is off.
- `rack-strip`: turn off downstream devices before the rack strip.
- `foot-switch`: press with the foot only if the switch is designed for it and the stance is stable.
- `smart-strip`: use the physical switch only for the intended whole-strip power cut.

## Safety & privacy

Medium risk because power loss can interrupt equipment or data. Never operate wet electrical gear, never touch exposed prongs, and confirm with a person before cutting power to unknown or assistive devices.
