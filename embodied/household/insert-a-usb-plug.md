---
name: insert-a-usb-plug
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [usb-plug, usb-port, cable, device]
affordances: [grasp, inspect, orient, align, insert]
workspace: desk or device area
safety: {hot_surfaces: false, sharp_objects: false, fragile: [usb-port, connector], human_proximity: continue}
---

## Goal

The USB plug is fully seated in the matching port without forcing or damaging the connector.

## Preconditions

- The plug type matches the port type.
- The device and port are accessible and stable.
- Cable slack is available so the connector is not under tension.

## Steps

1. **Stabilize the device.** Hold or brace the device so the port does not move during insertion. → *Expect:* the port opening remains stationary.
2. **Grip the plug shell.** Hold the rigid connector body, not the flexible cable. → *Expect:* the plug tip is visible and controlled.
3. **Inspect orientation.** Compare the plug shape to the port shape and rotate until keyed edges match. → *Expect:* the plug face matches the port opening.
4. **Align straight to the port.** Bring the plug tip to the port centerline without side angle. → *Expect:* the plug touches the port opening evenly.
5. **Insert with light pressure.** Push along the port axis using steady low force. → *Expect:* the plug slides inward without scraping or bending.
6. **Seat fully.** Stop when resistance increases at the end of travel. → *Expect:* little or no metal connector remains visible and the plug feels secure.
7. **Release and check cable slack.** Let go of the connector and route the cable without pulling sideways. → *Expect:* the connector stays seated and the cable has a gentle bend.

## Decision points

- Plug does not start within light pressure → withdraw and rotate or confirm port type.
- USB-C plug fits both orientations → use the orientation with least cable strain.
- Port is loose or damaged → stop and avoid further insertion force.

## Failure modes & recovery

- **F1 Wrong orientation:** detect by blocked entry with keyed mismatch → withdraw, rotate 180 degrees if applicable, and realign.
- **F2 Side loading:** detect by connector entering at an angle → back out and push straight along the port axis.
- **F3 Cable tension pulls plug out:** detect by connector backing out after release → reroute cable for slack and reseat.

## Verification

The connector is fully seated, remains in place after release, and the device detects the connection if powered.

## Variations

- Micro-USB: inspect the trapezoid shape carefully because it is not reversible.
- USB-C: either orientation is acceptable, but the plug should still enter straight.

## Safety & privacy

Do not force a connector into a mismatched port. Connected devices may expose data or begin charging automatically.
