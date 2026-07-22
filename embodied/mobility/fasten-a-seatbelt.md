---
name: fasten-a-seatbelt
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
objects: [seatbelt, latch-plate, buckle, lap-belt, shoulder-belt]
affordances: [grasp, pull, align, insert, click, tension, untwist]
workspace: vehicle seat
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: slow}
---

## Goal

The seatbelt lies flat across hips and chest, the latch plate is clicked into the buckle, and the belt is confirmed latched without twists.

## Preconditions

- Occupant is seated upright with back against the seat.
- Seatbelt webbing, buckle, and latch plate are reachable and not trapped in the door.
- Clothing or bags are not blocking the belt path.

## Steps

1. **Find the latch plate.** Grasp the metal or plastic latch plate, not the loose webbing edge. → *Expect:* latch plate is controlled and belt can extend from the retractor.
2. **Pull smoothly across the body.** Draw the belt from shoulder side across chest and hips in one steady motion. → *Expect:* webbing extends without locking or jerking.
3. **Place the lap belt low.** Guide the lower belt across the hips and upper thighs, below the soft abdomen. → *Expect:* lap webbing lies flat and low.
4. **Place the shoulder belt.** Lay the upper belt across the center of the chest and shoulder, not the neck or under the arm. → *Expect:* shoulder webbing contacts the torso without cutting into the neck.
5. **Insert the latch plate.** Align the latch tongue with the buckle slot and push straight in until it clicks. → *Expect:* a distinct click is heard or felt.
6. **Check the latch.** Tug the latch plate upward and away from the buckle using moderate force. → *Expect:* latch plate stays locked in the buckle.
7. **Fix twists.** [BRANCH: belt flat → continue | twist present → feed the twist back toward the latch plate or shoulder guide until flat] → *Expect:* webbing lies flat from retractor to buckle.
8. **Remove slack.** Pull the shoulder belt upward near the chest and let the retractor take up slack. → *Expect:* belt fits snugly while allowing normal breathing.

## Decision points

- Belt locks while pulling out → let it retract slightly, then pull again more slowly.
- Buckle is hidden beside the seat → locate it by touch before moving the latch plate across the body.
- Shoulder belt touches the neck → adjust seat, belt height, or seating posture if the vehicle allows.

## Failure modes & recovery

- **F1 False latch:** latch plate enters wrong buckle or does not click → release, identify the matching buckle, and insert again until the click is clear.
- **F2 Twisted webbing:** belt edge rolls or crosses itself → untwist before driving because twisted webbing concentrates force.
- **F3 Lap belt too high:** belt crosses abdomen → pull the lap section downward onto the hips and remove slack.
- **F4 Shoulder belt under arm:** belt misses chest → route it over the shoulder and across the sternum.

## Verification

The latch remains locked under a tug, lap belt is low on the hips, shoulder belt crosses the chest, and all webbing is flat.

## Variations

- Rear middle seat: use the correct ceiling or seatback anchor and matching buckle if the belt has two latch points.
- Pregnant occupant: place the lap belt below the belly across the hips and keep the shoulder belt between the breasts.
- Booster seat rider: route the belt through the booster guides according to the booster instructions.

## Safety & privacy

Medium risk. A misrouted belt can increase injury in a crash, so never place the shoulder belt behind the back or under the arm, and confirm the latch before the vehicle moves.
