---
name: bring-a-blanket-to-someone
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
objects: [blanket, person, chair, bed, medical-device]
affordances: [ask, carry, unfold, drape, adjust, release]
workspace: care-space
safety: {hot_surfaces: false, sharp_objects: false, fragile: [medical-device], human_proximity: pause}
---

## Goal

Bring and place a blanket for someone so they are warmer without restricting movement, breathing, or medical equipment.

## Preconditions

- The person wants a blanket or has requested warmth.
- A clean, dry blanket is available.
- The person's tubes, cords, call button, and mobility aids are visible.

## Steps

1. **Confirm preference.** Ask whether they want the blanket and where they want it placed. → *Expect:* the person gives consent and placement preference.
2. **Select a clean blanket.** Choose one appropriate for warmth and size. → *Expect:* blanket is dry, odor-free, and not visibly soiled.
3. **Carry it clear of the floor.** Hold folded fabric away from spills, wheels, and footwear. → *Expect:* the blanket remains clean during transport.
4. **Unfold near the person.** Keep fabric away from face, food, and devices. → *Expect:* edges are controlled and visible.
5. **Drape as requested.** Place it over lap, shoulders, or bed area without covering face or controls. → *Expect:* the person is covered where requested.
6. **Free devices and hands.** Keep call button, oxygen tube, IV line, walker, and wheelchair controls accessible. → *Expect:* no equipment is trapped under fabric.
7. **Check comfort.** Ask if the blanket is too heavy, too warm, or needs adjustment. → *Expect:* the person confirms comfort or requests a change.

## Decision points

- Person declines → leave the blanket nearby only if requested.
- Fever, overheating, or breathing discomfort is present → check with caregiver before adding warmth.
- Blanket may tangle in wheels or bed rails → tuck or reposition away from moving parts.
- Skin is fragile or painful → place fabric lightly and avoid dragging.

## Failure modes & recovery

- **F1 Device covered:** detect hidden call button, tube, or control → uncover and route it above the blanket.
- **F2 Face covered:** detect fabric near mouth or nose → remove from face immediately.
- **F3 Wheel tangle:** detect blanket near wheelchair wheels → lift and fold it onto lap.
- **F4 Too warm:** detect sweating or complaint → remove or replace with lighter covering.

## Verification

The blanket is cleanly placed where requested, the person's face, hands, call controls, and medical devices remain accessible, and the person confirms comfort.

## Variations

- Bed use: keep blanket below shoulders unless the person asks otherwise.
- Wheelchair use: keep lower edges above wheels and footrests.
- Weighted blanket: use only if the person already uses one and wants it.

## Safety & privacy

Low risk, but human contact still requires consent. Avoid covering the face, restraints, alarms, or call button, and preserve modesty when adjusting around the torso or legs.
