---
name: close-a-jar-lid
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 2min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [jar, lid, counter, cloth]
affordances: [grasp, align, rotate, press, inspect]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [glass-jar], human_proximity: continue}
---

## Goal

A jar lid is seated on matching threads, tightened until snug, and checked for a usable seal without cracking the jar or deforming the lid.

## Preconditions

- The jar rim is clean, intact, and free of food that would block the seal.
- The lid belongs to the jar and has no bent edge, rust, or damaged gasket.
- The jar is on a stable counter or held low over a counter in case it slips.
- Hands are dry enough to maintain grip, or a clean cloth is available.

## Steps

1. **Place the jar upright.** Set the jar on a flat counter with the opening facing straight up. → *Expect:* the jar stands stable and does not rock.
2. **Inspect the rim and lid.** Check the glass rim, lid threads, and gasket area for chips, crumbs, or residue. → *Expect:* the contact surfaces look clean and continuous.
3. **Position the lid level.** Set the lid on the jar mouth without turning yet, centered and flat. → *Expect:* the lid rests evenly, not tipped to one side.
4. **Find the thread start.** Turn the lid slightly counterclockwise until it drops or clicks into the thread start. → *Expect:* the lid sits lower and no longer skates across the rim.
5. **Tighten clockwise.** Rotate the lid clockwise with light downward pressure, keeping it level. → *Expect:* the lid advances smoothly with no scraping or jump.
6. **Stop at snug.** Tighten until resistance increases, then stop without forcing. ⚠️ *Irreversible:* excess torque can crack fragile glass or deform the lid; confirm the lid is aligned before adding force. → *Expect:* the lid is secure and the jar is undamaged.
7. **Check the seal.** Hold the jar upright and gently try to wiggle the lid without loosening it. → *Expect:* the lid does not wobble or lift.
8. **Store upright.** Place the jar where it will not be knocked over. → *Expect:* the jar remains closed and stable.

## Decision points

- Lid resists immediately -> remove it, realign from the thread start, and retry Step 4.
- Lid spins without tightening -> inspect for mismatched lid size or stripped threads, then use another lid.
- Jar contains hot contents -> let it cool to safe handling temperature before tightening fully.
- Jar is wet or oily -> wipe the grip surfaces or use a cloth before turning.

## Failure modes & recovery

- **F1 Cross-threaded lid:** lid tilts or binds within the first turn, remove it and restart from the thread start.
- **F2 Damaged gasket:** lid tightens but leaks on a gentle tilt, replace the lid or transfer contents to another jar.
- **F3 Slipping grip:** hand slides on glass or metal, dry the jar and use a cloth for friction.
- **F4 Glass crack:** a chip or crack appears, stop using the jar and transfer contents to a safe container.

## Verification

The lid is level, snug, not forced, and stays attached when the upright jar is gently wiggled by the lid.

## Variations

- `wide-mouth`: use two hands on the lid edge to keep pressure even during alignment.
- `vacuum-seal`: after cooling, press the center button if present and confirm it does not pop up.
- `plastic-lid`: tighten only until the lid stops; plastic threads strip more easily than metal.

## Safety & privacy

Medium physical risk comes from fragile glass and hand strain. Keep the jar low over a counter, avoid forcing misaligned threads, and discard cracked glass immediately.
