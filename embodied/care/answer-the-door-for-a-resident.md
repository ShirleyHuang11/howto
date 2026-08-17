---
name: answer-the-door-for-a-resident
domain: embodied
subdomain: care
locale: [generic]
interface: physical
difficulty: basic
est_time: 3min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [door, peephole, lock, resident, visitor, intercom]
affordances: [ask, listen, look, unlock, open, speak, close]
workspace: residence-entry
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: pause}
---

## Goal

Respond to a door knock or bell for a resident while preserving their consent, privacy, and physical security.

## Preconditions

- The resident is present or has given a standing instruction.
- Door access rules for the home or facility are known.
- The responder can see, hear, or communicate with the visitor safely.

## Steps

1. **Check with the resident.** Ask whether they expect anyone and whether they want the door answered. → *Expect:* the resident gives permission or says not to answer.
2. **Approach without opening.** Keep the door locked while moving to a peephole, window, camera, or intercom. → *Expect:* visitor identity can be assessed without entry.
3. **Identify the visitor.** Ask who they are and why they are there. → *Expect:* the visitor states a name, role, or delivery purpose.
4. **Confirm with the resident.** Relay identity quietly and ask whether to admit, decline, or take a message. → *Expect:* resident instruction is clear.
5. **Open only as instructed.** [BRANCH: admit | decline | package] unlock and open for approved entry, speak through the door for decline, or receive package without granting entry. → *Expect:* the visitor gets the intended response.
6. **Maintain doorway control.** Stand clear of the swing path and avoid blocking the resident's mobility route. → *Expect:* the door can be closed quickly if needed.
7. **Close and relock.** Shut the door after the interaction and re-engage locks. → *Expect:* the entry returns to secure status.
8. **Report the outcome.** Tell the resident who came and what was done. → *Expect:* the resident knows the final status.

## Decision points

- Resident does not consent → do not open; offer to take a message if appropriate.
- Visitor claims emergency or official status → verify through known channels or call emergency services if immediate danger exists.
- Visitor pressures entry → keep door closed and seek help.
- Resident cannot answer → follow documented instructions or facility policy.

## Failure modes & recovery

- **F1 Unknown visitor:** detect unclear identity or purpose → do not open and ask them to contact resident by phone.
- **F2 Door left unlocked:** detect unlocked latch after interaction → lock immediately and confirm.
- **F3 Privacy leak:** detect visitor asking personal details → decline to share and refer to resident-approved contact.
- **F4 Resident changes mind:** detect instruction changes during opening → close the door and follow the latest instruction.

## Verification

The door interaction matches the resident's instruction, the door is closed and locked afterward, and no unauthorized person has entered.

## Variations

- Apartment intercom: verify visitor before buzzing anyone into the building.
- Care facility: follow sign-in and visitor policy before entry.
- Delivery: request no-contact placement when resident does not want direct interaction.

## Safety & privacy

Medium risk from unauthorized entry and disclosure. Resident consent controls the interaction; do not reveal health, mobility, schedule, or living status to visitors.
