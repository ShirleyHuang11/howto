---
name: plug-in-a-lamp
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [lamp, plug, cord, outlet, switch]
affordances: [inspect, grasp, align, insert, route, switch-toggle]
workspace: household
safety: {hot_surfaces: false, sharp_objects: false, fragile: [lamp-bulb, lamp-shade], human_proximity: slow}
---

## Goal

A lamp is plugged into a suitable outlet, the cord is routed safely, and the switch turns the light on and off.

## Preconditions

- The lamp, plug, cord, bulb, and shade are present.
- The outlet is dry, intact, and not overloaded.
- Hands are dry.
- The lamp is on a stable table, floor, or stand before power is connected.

## Steps

1. **Inspect the lamp cord.** Look for cuts, exposed wire, scorch marks, loose prongs, cracked plug body, or a crushed section. → *Expect:* the cord and plug look intact, or the lamp is not used.
2. **Check the outlet area.** Confirm the outlet cover is secure, dry, and not already crowded with high-power devices. → *Expect:* the socket is accessible and safe to approach.
3. **Place the lamp first.** Put the lamp where it will be used, with shade clear of curtains, paper, and bedding. → *Expect:* the lamp stands upright without wobbling.
4. **Orient the plug.** Match the wide prong to the wide slot if the plug is polarized, and do not force a mismatch. → *Expect:* the plug lines up naturally with the outlet.
5. **Insert firmly.** Hold the plug body, not the cord, and push straight in until seated. ⚠️ *Irreversible:* forcing a damaged plug or outlet can cause shock or fire, so stop if there is cracking, sparking, heat, or resistance. → *Expect:* no metal prong remains exposed.
6. **Route the cord.** [BRANCH: along wall | across open path] tuck along the wall or furniture edge, or choose another outlet instead of crossing a walkway. → *Expect:* feet, chair legs, doors, and wheels will not snag it.
7. **Switch test.** Turn the lamp switch on, then off, then on if light is desired. → *Expect:* the bulb responds without flicker, buzzing, sparks, or heat at the plug.
8. **Final position check.** Adjust shade and lamp base after switching off if your hand needs to go near the bulb. → *Expect:* the shade is straight and the lamp illuminates the intended area.

## Decision points

- Cord or plug is damaged → do not plug it in until repaired or replaced.
- Outlet sparks, feels hot, smells burnt, or will not hold the plug → stop using that outlet and seek repair.
- Lamp flickers after bulb is tightened and tested → unplug it and inspect bulb type, switch, and cord.
- Cord must cross a walkway → use a different outlet or a proper cord cover for temporary use.

## Failure modes & recovery

- **F1 Plug will not fit:** detect blocked insertion or wrong prong shape → realign, check polarization, and never shave or bend prongs.
- **F2 Lamp does not turn on:** detect no light after switch test → check bulb seating, bulb condition, outlet power, and wall switch.
- **F3 Cord becomes a trip hazard:** detect cord in a walking path → reroute along a wall or move the lamp.
- **F4 Outlet or plug warms:** detect heat, buzzing, smell, or discoloration → switch off, unplug by the plug body, and stop using it.

## Verification

The lamp stands stable, the plug is fully seated in a safe outlet, the cord is out of traffic paths, and the switch controls the light normally.

## Variations

- `switched-outlet`: leave the lamp switch on and use the wall switch for control.
- `extension-cord`: use only a rated cord temporarily, fully uncoiled and out of walkways.
- `smart-plug`: plug the smart plug into the outlet first, then the lamp into the smart plug.

## Safety & privacy

Medium risk because household electricity can shock or start fires when cords, outlets, or plugs are damaged. Keep cords dry, avoid overloading adapters, and never unplug by yanking the cord.
