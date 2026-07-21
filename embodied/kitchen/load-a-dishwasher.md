---
name: load-a-dishwasher
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 15min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [dishwasher, plates, bowls, cups, glasses, cutlery, pots, detergent-pod, cutlery-basket]
affordances: [door-open, rack-slide, grasp, place, scrape, button-press, dispenser-open]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: true, fragile: [glasses, plates, bowls], human_proximity: pause}
---

## Goal

All dirty dishes from the sink/counter are loaded into the dishwasher, detergent is dosed, and a wash cycle is running.

## Preconditions

- Dishwasher is empty of clean dishes (or clean items have been put away first).
- Dirty dishes are gathered at the sink/counter area.
- Detergent (pod or powder) is available.
- Items are dishwasher-safe; set aside wood, cast iron, and delicate/hand-wash-only items.

## Steps

1. **Open the dishwasher door fully and slide out the bottom rack.** → *Expect:* door rests horizontal; bottom rack glides out without obstruction.
2. **Scrape food solids off each dish into the trash/compost.** No pre-rinsing needed beyond solids. → *Expect:* no bones, pits, or food chunks remain on any item.
3. **Load the bottom rack: plates and large items.** Plates vertical in the tines, faces toward the center; pots and pans face-down at the sides/back. Nothing blocks the detergent dispenser's swing path or the spray arm's rotation. → *Expect:* spin the lower spray arm one turn by hand — it clears everything.
4. **Slide out the top rack and load cups, glasses, and bowls face-down at an angle.** Glasses between tines, not over them; fragile glasses not touching each other. → *Expect:* no item rocks when the rack is jiggled; no two glasses in contact.
5. **Load cutlery into the basket, handles down** — except sharp knives, handles up (or flat in a dedicated top tray). ⚠️ *Irreversible:* blade-up knives are a laceration hazard to humans unloading — always handles-up for blades. → *Expect:* cutlery loosely mixed (not nested); knife blades all pointing down or lying flat.
6. **Slide both racks in and check clearance.** → *Expect:* racks seat fully; tall items don't block the upper spray arm.
7. **Open the detergent dispenser, insert one pod (or fill powder to the line), and snap it shut.** → *Expect:* dispenser clicks closed with the pod inside.
8. **Close the door until it latches and select the normal cycle; press start.** → *Expect:* latch clicks; cycle indicator lights; water-fill sound begins within ~1 min. If a human opens the door area, pause motion until clear.

## Decision points

- Load exceeds capacity → run this load and stage the remainder; never force-stack (blocks spray coverage).
- Heavily burnt pot → set aside for hand-wash/soaking rather than occupying half the bottom rack.
- No pods left → powder or gel per the dispenser markings; never hand-dish soap (foam flood, F3).

## Failure modes & recovery

- **F1 Item blocks a spray arm (arm won't spin in step 3/6):** relocate or remove the tallest/deepest item; re-check both arms.
- **F2 Door won't latch:** a rack is not fully seated or a handle protrudes — reseat racks, rotate the offending item, retry.
- **F3 Wrong detergent used (foam leaking):** stop the cycle, let foam settle, run a rinse cycle empty; wipe the floor.
- **F4 Cycle doesn't start after latch:** check child-lock indicator and the water supply valve; hold start 3 s (some models require it).

## Verification

Door latched, cycle running (indicator on, water audible), sink/counter clear of dishwasher-safe dirty dishes, hand-wash items staged separately, and no knife loaded blade-up.

## Variations

- Drawer dishwashers: single-drawer loads skip the rack split; capacity halves.
- Hard-water regions: add rinse aid / salt when their indicator lights are on (extra check before step 8).

## Safety & privacy

Sharp objects (knives) in steps 2 and 5 — grasp by handles only. Fragile glassware in step 4 — reduced grip force, no glass-on-glass contact. Pause all rack/door motion when a human is within the door's swing radius.
