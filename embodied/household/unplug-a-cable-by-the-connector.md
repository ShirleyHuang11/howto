---
name: unplug-a-cable-by-the-connector
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
objects: [cable, connector, port, device]
affordances: [grasp, stabilize, pull, release, inspect]
workspace: desk or device area
safety: {hot_surfaces: false, sharp_objects: false, fragile: [connector, port], human_proximity: continue}
---

## Goal

The cable is disconnected by pulling the connector body, leaving the cable and port undamaged.

## Preconditions

- It is safe and permitted to disconnect the device.
- The connector body is accessible.
- Any required shutdown or eject step has already been completed.

## Steps

1. **Stabilize the device or socket.** Hold the device body or wall plate near the port. → *Expect:* the port does not move when lightly touched.
2. **Grip the connector body.** Pinch or hold the rigid plug shell, not the flexible cable. → *Expect:* grip force is on the connector housing.
3. **Align with the port axis.** Set the pull direction straight out from the port opening. → *Expect:* the connector is not angled up, down, or sideways.
4. **Pull steadily.** Apply smooth outward force along the connector axis. → *Expect:* the connector slides out without bending.
5. **Clear the port.** Continue pulling until the metal or plastic tip fully exits. → *Expect:* the plug is free and no part remains seated.
6. **Inspect both ends.** Look at the connector and port for bent pins, cracks, or debris. → *Expect:* connector and port appear intact.
7. **Place the cable safely.** Lay the cable end on the desk or coil it loosely away from walkways. → *Expect:* the connector is not dangling under strain.

## Decision points

- Connector has side tabs or latch → press the release before pulling.
- Plug resists unusually → stop and check for screws, clips, or locking features.
- Device is transferring data → wait for activity to stop or perform a software eject first.

## Failure modes & recovery

- **F1 Cable is pulled instead of connector:** detect by cable jacket stretching or bending → release, regrip the connector body, and pull straight.
- **F2 Connector stuck:** detect by no movement under moderate force → inspect for latch or debris and avoid additional force.
- **F3 Port shifts:** detect by socket movement during pull → brace the device closer to the port and retry gently.

## Verification

The connector is fully removed, the port and plug are visibly undamaged, and the cable is stored without tension.

## Variations

- Power plug: grip the plug body and keep fingers away from prongs.
- Ethernet cable: depress the plastic latch before pulling.

## Safety & privacy

Disconnecting data cables can interrupt transfers. Do not pull by the cable, and avoid touching exposed electrical contacts.
