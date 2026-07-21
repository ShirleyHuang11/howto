---
name: open-a-can-with-a-can-opener
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [can, manual-can-opener, lid, bowl, sponge]
affordances: [grasp, clamp, knob-turn, rotate, lift, rinse]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: true, fragile: [bowl], human_proximity: slow}
---

## Goal

A sealed food can is opened cleanly, with the lid controlled and sharp metal edges kept away from hands.

## Preconditions

- The can is intact, not bulging, leaking, badly rusted, or spurting.
- A manual can opener is clean and turns freely.
- A stable counter, sink, and receiving bowl are available.
- Hands are dry enough to grip the opener and can.

## Steps

1. **Inspect the can.** Check for bulging ends, deep dents on seams, leaks, rust holes, or sour smell. → *Expect:* the can appears safe to open, or it is discarded unopened.
2. **Set the can on a stable surface.** Place it upright near the counter edge with the label facing out if helpful. → *Expect:* the can does not wobble when touched.
3. **Open the can opener jaws.** Spread the handles so the cutting wheel and feed wheel can straddle the rim. → *Expect:* the opener mouth fits over the can lip.
4. **Clamp the wheel on the rim.** Seat the cutting wheel on the top inside edge and squeeze the handles firmly. → *Expect:* the opener grips the rim without sliding.
5. **Turn the knob forward.** Rotate the knob steadily while holding the handles closed. → *Expect:* the can rotates under the opener and a cut line appears around the lid.
6. **Continue around the circle.** Keep turning until the cut nearly meets the start point. [BRANCH: leave a small hinge | cut fully free] leave 1 cm attached for control, or finish the circle if draining. → *Expect:* the lid is loose but not flying loose.
7. **Lift the lid safely.** Use the opener tip, a spoon handle, or the uncut hinge to lift the lid away from your fingers. ⚠️ *Irreversible:* the cut lid and can rim are sharp, so never slide a finger along the edge. → *Expect:* the can is open and fingers never touch the cut metal.
8. **Pour or scoop contents.** Transfer food to a bowl or pot, then place the lid inside the empty can for disposal if local practice allows. → *Expect:* food is out, and sharp pieces are contained.

## Decision points

- Can is bulging, leaking, or sprays when punctured → stop, bag it, and discard according to local food safety guidance.
- Opener slips repeatedly → clean the rim, dry your hands, and reclamp from a new spot.
- You need to drain liquid → cut fully around, hold lid down with a spoon, and pour away from hands.
- A child or pet is close → pause until there is clear space around the sharp lid.

## Failure modes & recovery

- **F1 Opener will not bite:** detect spinning without cutting → reseat the cutting wheel just inside the rim and squeeze harder.
- **F2 Jagged partial cut:** detect torn metal or missed sections → reclamp before the gap and turn slowly through it.
- **F3 Lid falls into food:** detect lid submerged in contents → lift it with a fork or tongs, not fingers.
- **F4 Sharp trash exposure:** detect loose lid in trash bag → tuck it inside the can or wrap it before disposal.

## Verification

The can is open, contents are usable, and the sharp lid and rim are controlled so no bare finger contacts cut metal.

## Variations

- `safety-opener`: side-cut openers leave a smoother lid but still require controlled lifting.
- `pull-tab-can`: lift the ring slowly and keep fingers away from the torn lid edge.
- `left-handed`: rotate the can or opener to keep the knob hand comfortable and stable.

## Safety & privacy

Medium risk from sharp metal and spoiled cans. Discard suspect cans without tasting. Move slowly around other people, and wash the opener after contact with can liquid or food.
