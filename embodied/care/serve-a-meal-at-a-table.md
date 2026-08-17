---
name: serve-a-meal-at-a-table
domain: embodied
subdomain: care
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [person, plate, bowl, cup, utensils, table, napkin]
affordances: [ask, carry, place, orient, pour, set-down]
workspace: dining-area
safety: {hot_surfaces: true, sharp_objects: true, fragile: [plate, glass], human_proximity: slow}
---

## Goal

Serve a meal at a table so the person can eat safely, comfortably, and with the correct food and utensils.

## Preconditions

- The meal matches the person's diet, allergies, and texture needs.
- The person is seated upright enough to eat.
- The table surface is clean and within reach.

## Steps

1. **Confirm meal identity.** Check the person's name, diet instructions, allergies, and meal contents. → *Expect:* the meal is safe for this person.
2. **Clear the place setting.** Remove clutter and wipe spills from the eating area. → *Expect:* plate, cup, and utensils have stable spaces.
3. **Place the main plate.** Set it centered in front of the person or where they prefer. → *Expect:* the plate is stable and reachable.
4. **Orient utensils and napkin.** Put utensils on the usable side and napkin within reach. → *Expect:* the person can pick them up without stretching.
5. **Place drink safely.** Put the cup away from the plate edge and confirm temperature if hot. → *Expect:* the cup is upright and reachable without tipping.
6. **Announce hot, sharp, or spill risks.** Point out hot bowls, knives, or lidded containers. → *Expect:* the person knows which items need caution.
7. **Ask before cutting or opening items.** Offer assistance with packets, lids, or cutting food. → *Expect:* assistance is consented to or declined.
8. **Confirm readiness.** Check posture, call bell or phone access if relevant, and comfort before leaving. → *Expect:* the person can begin eating safely.

## Decision points

- Food does not match diet order → do not serve; replace or verify with caregiver or kitchen.
- Person is coughing, very drowsy, or not upright → pause meal and seek caregiver guidance.
- Hot item is too hot → place it out of immediate reach or let it cool.
- Person needs adaptive utensils → retrieve them before serving.

## Failure modes & recovery

- **F1 Wrong meal:** detect name, allergy, or diet mismatch → remove the tray and obtain the correct meal.
- **F2 Spill risk:** detect cup or bowl near edge → move it inward and wipe the table.
- **F3 Choking concern:** detect coughing, wet voice, or difficulty swallowing → stop serving and get trained help.
- **F4 Utensil hazard:** detect knife blade facing hand or lap → reorient or remove if not needed.

## Verification

The correct meal is placed within reach on a clean table, hazards are identified, adaptive needs are met, and the person is upright and ready to eat.

## Variations

- Bedside table: lock wheels and bring the table close without pressing against the body.
- Vision impairment: describe plate layout using clock positions.
- Shared dining room: verify the meal before placing it because trays can be similar.

## Safety & privacy

Medium risk from burns, choking, allergies, and sharp utensils. Keep diet information private, ask before assisting with food, and pause if swallowing safety is uncertain.
