---
name: plug-in-a-charger
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 3min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [charger, power-outlet, device, cord, plug]
affordances: [inspect, orient, insert, route, observe]
workspace: household
safety: {hot_surfaces: false, sharp_objects: false, fragile: [device-screen], human_proximity: continue}
---

## Goal

A compatible charger is safely plugged into power, connected to the device, and confirmed charging with the cord routed where it will not trip or strain anyone.

## Preconditions

- The charger, cable, device, and wall outlet are accessible.
- The outlet is dry, unobstructed, and not visibly damaged.
- The charger is rated for the device or came with it.
- There is a safe path for the cord that avoids walkways and pinch points.

## Steps

1. **Inspect the charger.** Look over the block, plug blades, and cable for frays, exposed wire, scorch marks, or bent metal. → *Expect:* all parts are intact and dry.
2. **Choose the outlet.** Use a firm wall outlet or grounded power strip that is not overloaded. → *Expect:* the outlet face is stable and has room for the plug.
3. **Orient the plug.** Match the plug blade shape to the outlet slot shape before pushing. → *Expect:* the plug lines up without twisting.
4. **Insert the plug firmly.** Push straight in while supporting the charger body, not the cable. → *Expect:* the plug sits fully seated with little or no metal blade visible.
5. **Connect the device end.** Align the charging connector with the device port and insert gently. → *Expect:* the connector seats without scraping or force.
6. **Confirm charging.** Look for the battery icon, charging light, sound, or lock-screen message. → *Expect:* the device reports charging within a few seconds.
7. **Route the cord.** Lay the cable along an edge, behind furniture, or away from feet and chair wheels. → *Expect:* the cable has slack at both ends and does not cross a walking path.
8. **Recheck heat later.** After several minutes, touch near the charger body lightly if safe. → *Expect:* it may be warm but not hot, buzzing, or smelling burnt.

## Decision points

- No charging indicator -> try the other side of a reversible connector, another outlet, or a known-good cable.
- Plug feels loose -> move to another outlet; do not wedge paper, foil, or objects around it.
- Cable must cross a walkway -> choose a closer outlet or make the cord visible and flat until moved.
- Device port resists -> stop and inspect for debris or the wrong connector shape.

## Failure modes & recovery

- **F1 Damaged cable:** exposed wire, kinks, or heat appear, unplug from the wall and replace the charger.
- **F2 Partial plug insertion:** metal blades remain visible or charger wiggles, remove it and insert straight into a firmer outlet.
- **F3 No charge:** device battery stays unchanged, test outlet power and swap cable or charger.
- **F4 Trip hazard:** cord lies across foot traffic, reroute along a wall or unplug until a safer location is available.

## Verification

The charger is fully seated, the device shows a charging indicator, and the cord is routed with slack outside normal walking paths.

## Variations

- `usb-c`: the connector is reversible, but it still should insert straight without force.
- `power-strip`: use a strip with a switch and rating label, and keep high-draw appliances off the same strip.
- `shared-space`: route the cord where other people will see it or cannot step through it.

## Safety & privacy

Medium risk comes from damaged electrical parts and trip hazards. Do not use frayed cords, wet outlets, hot chargers, or improvised outlet fixes.
