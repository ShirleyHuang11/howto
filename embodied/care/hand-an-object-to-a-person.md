---
name: hand-an-object-to-a-person
domain: embodied
subdomain: care
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [object, person, hand]
affordances: [approach, orient, offer, wait, release]
workspace: care-space
safety: {hot_surfaces: false, sharp_objects: false, fragile: [object], human_proximity: pause}
---

## Goal

An object is transferred to a person only after they are ready, gripping it, and receiving the safe end or intended handle.

## Preconditions

- The person is present, awake, and able to receive the object.
- The object is safe to hand over or its hazard side can be oriented away.
- The actor can approach within comfortable reach without crowding.
- Consent or request for the handoff is clear.

## Steps

1. **Confirm intent.** Ask or verify that the person wants the object now. → *Expect:* person gives verbal, gestural, or contextual consent.
2. **Approach slowly.** Stop outside their personal space and within arm reach. → *Expect:* person can see the actor and object.
3. **Orient the safe end.** Turn handles, blunt ends, labels, or grip surfaces toward the person. → *Expect:* hazardous, hot, sharp, or messy surfaces face away from them.
4. **Announce the handoff.** State the object name and where it will be offered if speech is appropriate. → *Expect:* person attends to the object.
5. **Offer at reachable height.** Extend the object midway between actor and person, close to their dominant hand if known. → *Expect:* person can reach without leaning dangerously.
6. **Hold steady.** Keep the object still and supported while they place fingers or hand on it. → *Expect:* their grip contacts a stable part of the object.
7. **Wait for grip confirmation.** [BRANCH: verbal confirm | physical confirm] accept "got it" or detect firm opposing grip and load support. → *Expect:* person is bearing the object's weight or controlling it.
8. **Release gradually.** Open the actor's grip slowly while watching for slip. → *Expect:* object remains in the person's control.
9. **Withdraw and pause.** Move hands back without brushing their body or assistive devices. → *Expect:* person holds the object comfortably.

## Decision points

- Person does not consent → do not hand over; place the object nearby if requested.
- Person's grip is weak or uncertain → keep supporting the object and offer a different handle or surface.
- Object has a hot or sharp end → orient hazard away and verbally warn before offering.
- Person cannot reach safely → move closer only with consent or set object on a stable surface.
- Person is distracted → wait until attention returns.

## Failure modes & recovery

- **F1 Grip not established:** detect fingers touching but not closing → keep hold and cue the grip point.
- **F2 Object starts slipping:** detect downward motion → re-grip immediately if safe and reset the handoff.
- **F3 Person startles:** detect flinch or withdrawal → stop motion, move back, and ask before retrying.
- **F4 Unsafe orientation:** detect sharp, hot, or spill side facing person → rotate object before continuing.
- **F5 Reach causes imbalance:** detect person leaning or bracing unexpectedly → pull back and place object on a nearer surface.

## Verification

The person has consented, holds the object independently by a safe surface, and the actor has fully released without drop or contact.

## Variations

- `cup`: offer the handle toward the person and keep cup level until confirmed.
- `tool`: offer the handle first with the working end pointed down or away.
- `paper`: hold one corner until the person pinches the opposite edge.
- `person-with-limited-grip`: place the object into their palm or on a table only after confirming preference.

## Safety & privacy

Human proximity requires pause behavior. Consent matters before entering reach space or placing anything in a person's hand. Do not expose labels, documents, or screens to others during the transfer.
