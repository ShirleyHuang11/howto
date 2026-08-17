---
name: help-someone-drink-from-a-cup
domain: embodied
subdomain: care
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 3min
risk: high
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [person, cup, straw, napkin, chair, table]
affordances: [ask, grasp, tilt, hold, pause, wipe]
workspace: care-space
safety: {hot_surfaces: true, sharp_objects: false, fragile: [cup], human_proximity: pause}
---

## Goal

Help a person take a drink from a cup while minimizing choking, spills, burns, and loss of control.

## Preconditions

- The person is awake, agrees to drink, and is allowed oral fluids.
- The drink type, thickness, and temperature match their care instructions.
- The person is upright enough for safe swallowing.

## Steps

1. **Confirm consent and drink type.** Ask if they want a sip and verify the cup contents. → *Expect:* the person agrees and the drink is appropriate.
2. **Check posture.** Ensure head and torso are upright, not lying back. → *Expect:* the person's mouth and throat are positioned for swallowing.
3. **Check temperature.** Test or confirm that the drink is not too hot. → *Expect:* temperature is safe for the person's mouth.
4. **Offer the cup or straw.** Bring it into view and within comfortable reach. → *Expect:* the person can see or feel the cup before contact.
5. **Support without forcing.** Hold the cup steady while the person controls lip contact or straw use. → *Expect:* lips seal or straw is positioned without pushing.
6. **Tilt slowly for a small sip.** Raise the cup only enough for a controlled amount. → *Expect:* liquid reaches the mouth without flooding.
7. **Pause for swallow.** Lower the cup and wait for the person to swallow and breathe normally. → *Expect:* no coughing, wet voice, or distress appears.
8. **Repeat only if safe.** [BRANCH: wants more | stop] continue small sips if requested, otherwise set cup down. → *Expect:* drinking ends by consent or after safe sips.
9. **Wipe and settle.** Offer a napkin and place the cup in a stable reachable place if allowed. → *Expect:* face, clothing, and cup area are clean and comfortable.

## Decision points

- Person coughs, chokes, or voice changes → stop immediately and seek trained help.
- Drink is not permitted or wrong thickness → do not give it; verify care instructions.
- Person refuses → set the cup down and do not continue.
- Person cannot sit upright → pause until safer positioning or trained help is available.

## Failure modes & recovery

- **F1 Too much liquid:** detect gulping, overflow, or panic → lower cup immediately and allow breathing.
- **F2 Cough after sip:** detect coughing or watery eyes → stop, keep upright, and alert caregiver if persistent.
- **F3 Hot drink discomfort:** detect flinch or complaint → remove cup and cool or replace the drink.
- **F4 Straw misplaced:** detect straw pressing gums or cheek → reposition gently after asking.

## Verification

The person has taken only consented, controlled sips, remains upright, shows normal breathing and voice, and the cup is set down securely.

## Variations

- Thickened liquids: use the prescribed consistency only and avoid unapproved straws if restricted.
- Hand-over-hand support: let the person keep contact with the cup while assistance steadies it.
- Lidded cup: check vent and spout flow before offering.

## Safety & privacy

High risk from choking, aspiration, burns, and forced intake. Explain each movement, stop on coughing or refusal, and keep hydration or medical restrictions private.
