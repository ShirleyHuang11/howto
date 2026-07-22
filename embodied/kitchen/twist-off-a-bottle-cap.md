---
name: twist-off-a-bottle-cap
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
objects: [bottle, cap, seal-ring, label, liquid]
affordances: [grasp, brace, twist, break-seal, remove, reseal]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [glass-bottle], human_proximity: continue}
---

## Goal

The bottle cap is loosened counterclockwise, removed without spilling, and optionally tightened again to reseal.

## Preconditions

- Bottle is upright and not under unsafe pressure or heat.
- Cap is a twist-off style, not a pry-off crown.
- Hands and cap are dry enough for grip.

## Steps

1. **Stabilize the bottle.** Hold the bottle body below the neck with the non-turning hand. → *Expect:* bottle stays upright.
2. **Grip the cap.** Wrap fingers and thumb around the cap ridges with firm even pressure. → *Expect:* cap skin contact does not slip.
3. **Brace the base.** Press the bottle lightly against the counter or hold it close to the body. → *Expect:* bottle resists rotation.
4. **Twist counterclockwise.** Turn the cap left while the bottle hand holds steady. → *Expect:* cap begins to rotate relative to the bottle.
5. **Feel the seal break.** Continue through the first pop, crack, or drop in resistance. → *Expect:* tamper ring separates or threads loosen.
6. **Remove the cap.** Keep twisting until threads disengage, then lift the cap straight up. → *Expect:* bottle mouth is open and liquid remains below the rim.
7. **Use the contents.** [BRANCH: pour | sip | inspect] keep the bottle upright between actions. → *Expect:* controlled access to the liquid.
8. **Tighten to reseal.** Place cap squarely and twist clockwise until snug. → *Expect:* cap stops without cross-threading.

## Decision points

- Cap slips → dry the cap, use a rubber grip, or increase contact area.
- Cap deforms without turning → verify it is not a pry-off or safety cap.
- Carbonated bottle hisses strongly → pause opening until pressure settles.

## Failure modes & recovery

- **F1 Cross-thread on reseal:** cap tilts or jumps threads → remove, place squarely, and restart clockwise.
- **F2 Spill on opening:** bottle tilts during twist → return upright, wipe liquid, and brace lower.
- **F3 Seal ring binds:** cap turns but ring catches → keep cap aligned and continue with steady torque.
- **F4 Glass instability:** bottle rocks on counter → move to a flat dry surface before adding torque.

## Verification

The cap is removed or resealed as intended, the bottle remains upright, and no liquid is spilled outside the target area.

## Variations

- Child-resistant cap: push downward while turning counterclockwise.
- Wide-mouth jar-like bottle: use the same opposing grip with a larger hand span.

## Safety & privacy

Low risk. Watch for glass breakage, sharp cap edges, and pressure release from carbonated liquids.
