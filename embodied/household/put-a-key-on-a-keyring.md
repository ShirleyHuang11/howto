---
name: put-a-key-on-a-keyring
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [key, split-ring, keyring, table]
affordances: [grasp, pry, insert, slide, rotate, inspect]
workspace: household
safety: {hot_surfaces: false, sharp_objects: true, fragile: [], human_proximity: continue}
---

## Goal

Attach a key securely onto a split keyring without bending the key, dropping it, or injuring fingertips.

## Preconditions

- Key has an intact hole near its head.
- Split ring has a visible opening and is not deformed.
- Work surface is clear so dropped parts are easy to find.
- Fingernails, a coin, or a ring opener is available if the split ring is stiff.

## Steps

1. **Place parts on the table.** Set the key and ring flat with the ring opening visible. → *Expect:* both parts are stable and easy to grasp.
2. **Open the split ring slightly.** Lift the outer wire end with a fingernail, coin edge, or opener. → *Expect:* a small gap appears without overbending the ring.
3. **Insert the key hole.** Slide the key hole onto the raised wire end, keeping the key flat. → *Expect:* the key is captured between the ring layers.
4. **Rotate the key around the ring.** Push the key along the ring spiral until it passes the opening and reaches the main loop. → *Expect:* the key moves smoothly and does not pop off.
5. **Release and inspect.** Let the ring close and tug the key lightly. → *Expect:* the key hangs inside the closed loop and cannot leave through the opening.

## Decision points

- Ring is too stiff → use a split-ring opener instead of forcing with fingernails.
- Key hole is too small → choose a smaller ring or intermediate jump ring.
- Key is already labeled or directional → orient it to match the rest of the key set.

## Failure modes & recovery

- **F1 Ring overbends:** detect a gap that stays open → replace the ring or pinch it closed with pliers if undamaged.
- **F2 Key slips off:** detect key leaving before full rotation → restart with the key hole deeper under the lifted wire.
- **F3 Finger pinch:** detect skin caught between ring layers → release pressure and use a tool to hold the gap.
- **F4 Wrong key added:** detect label or shape mismatch → rotate it back off before adding other keys.

## Verification

The key is fully inside the split ring, the ring closes without a gap, and a light tug does not detach the key.

## Variations

- `key-fob`: attach the fob by its metal eyelet, not through soft plastic.
- `many-keys`: add largest keys first so smaller keys do not block rotation.

## Safety & privacy

Low risk. Split rings can pinch or scratch; avoid exposing key labels or addresses while organizing keys in public.
