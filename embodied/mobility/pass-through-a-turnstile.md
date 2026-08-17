---
name: pass-through-a-turnstile
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [turnstile, fare-card, gate, bag, indicator-light]
affordances: [tap, push, wait, threshold-cross, retrieve]
workspace: station-entrance
safety: {hot_surfaces: false, sharp_objects: false, fragile: [phone], human_proximity: slow}
---

## Goal

Enter or exit through a turnstile or fare gate with body, bags, and fare media clear of the mechanism.

## Preconditions

- The turnstile or gate is for the intended direction.
- Fare card, ticket, phone, or credential is ready.
- Bags are close to the body and not dragging.

## Steps

1. **Choose an open lane.** Select a turnstile showing a green arrow, unlocked gate, or correct direction sign. → *Expect:* the lane appears available for passage.
2. **Queue behind the line.** Leave the person ahead enough space to clear the gate. → *Expect:* the lane is empty before you present fare.
3. **Present fare or credential.** Tap, scan, insert, or show the credential as the device requires. → *Expect:* light, tone, or screen confirms acceptance.
4. **Collect the ticket if returned.** Take any paper ticket or card before moving through. → *Expect:* no fare media remains in the slot or reader area.
5. **Move through promptly.** Push the bar or walk through the open panels with bags kept close. → *Expect:* body and belongings pass before the gate resets.
6. **Clear the exit side.** Continue several steps beyond the turnstile before stopping. → *Expect:* the next person can use the lane.

## Decision points

- Fare is rejected → step aside and reload, retry, or ask staff instead of blocking the lane.
- Bags or mobility aid will not fit → use the accessible gate.
- Gate closes early → stop before forcing it and present fare again or ask staff.
- Emergency gate is alarmed → use only during emergencies or staff direction.

## Failure modes & recovery

- **F1 Card not read:** detect red light or no tone → remove metal overlap, use one card, and tap again.
- **F2 Bag catches:** detect resistance at bar or panel → stop, back up if possible, free the bag, and retry.
- **F3 Tailgating pressure:** detect someone crowding from behind → pause before presenting fare and allow space.
- **F4 Wrong direction lane:** detect no-entry sign or people coming toward you → leave the lane and choose another.

## Verification

The person and all carried items are fully on the far side of the correct turnstile, fare media is retained, and the lane behind is clear.

## Variations

- Wide accessible gate: wait for panels to open fully and cross without touching them.
- Paper ticket gate: insert in the marked slot and retrieve from the exit slot.
- Staffed entry: present pass to the attendant and follow their lane instruction.

## Safety & privacy

Low physical risk, with pinch points and crowding. Slow near people, keep payment media shielded, and do not reveal account balances or personal pass details unnecessarily.
