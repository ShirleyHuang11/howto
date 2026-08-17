---
name: walk-a-dog-on-a-leash
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: basic
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [dog, leash, collar, harness, waste-bag, door]
affordances: [clip, grip, walk, stop, wait, pick-up]
workspace: sidewalk
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: slow}
---

## Goal

Walk a leashed dog outside, keeping the dog controlled, away from hazards, and returned safely.

## Preconditions

- The dog is allowed to go out and is wearing a fitted collar or harness.
- A leash and waste bags are available.
- Local weather and pavement temperature are safe for the dog.

## Steps

1. **Attach the leash.** Clip to the harness or collar ring and tug lightly to check closure. → *Expect:* the clip stays attached and rotates freely.
2. **Prepare the exit.** Hold the leash short enough to prevent bolting before opening the door. → *Expect:* the dog waits within reach.
3. **Exit together.** Open the door only as wide as needed and step out with the dog controlled. → *Expect:* both handler and dog are outside with the leash in hand.
4. **Walk with slack control.** Keep the leash loose but short enough to stop lunges toward streets, people, or animals. → *Expect:* the dog moves ahead or beside you without dragging you.
5. **Pause at crossings.** Stop before curbs and driveways, scan traffic, then cross directly. → *Expect:* the dog remains out of the roadway until you move.
6. **Manage interactions.** [BRANCH: greet | avoid] allow greeting only with both handlers' consent, otherwise create distance. → *Expect:* no unplanned contact occurs.
7. **Pick up waste.** Bag feces immediately and carry it to an approved bin. → *Expect:* the sidewalk or grass is left clean.
8. **Return and enter safely.** Shorten the leash at the door, enter, then remove the leash only after the door is closed. → *Expect:* the dog is indoors or in the intended secure area.

## Decision points

- Dog pulls hard or lunges → stop, shorten the leash, and create distance from the trigger.
- Pavement is too hot or icy → shorten the walk, use shade, or skip until safe.
- Off-leash dog approaches → keep your dog close, avoid tension, and leave the area.
- Dog shows distress → turn back and contact the owner or veterinarian if severe.

## Failure modes & recovery

- **F1 Clip failure:** detect leash detaching or collar slipping → calmly secure the dog in an enclosed area and reattach equipment.
- **F2 Leash tangle:** detect leash around legs, wheels, or posts → stop before pulling and unwind it.
- **F3 Waste bag missing:** detect no bag after defecation → get a bag immediately and return to clean the spot.
- **F4 Traffic drift:** detect dog stepping toward road → stop, shorten leash, and move away from curb.

## Verification

The dog completes the walk, returns to the secure home or yard area, leash equipment is removed only after containment, and any waste has been disposed of.

## Variations

- Reactive dog: maintain larger distance from people and animals and avoid greetings.
- Night walk: use lights or reflective gear and keep crossings extra conservative.
- Multiple dogs: walk only as many as can be controlled without crossed leashes.

## Safety & privacy

Medium risk from traffic, bites, falls, and escaped animals. Slow near other people and animals, respect requests not to approach, and avoid exposing addresses or access codes while entering.
