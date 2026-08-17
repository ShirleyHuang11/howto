---
name: turn-a-doorknob
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
objects: [door, doorknob, latch, frame]
affordances: [grasp, rotate, push, pull, release]
workspace: doorway
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: slow}
---

## Goal

The doorknob is rotated enough to retract the latch and the door is moved open or confirmed unlocked.

## Preconditions

- The door is permitted to be opened.
- The knob is reachable and not visibly damaged.
- The swing path is clear of people and objects.

## Steps

1. **Approach the latch side.** Stand beside the door swing path, not directly in front of it. → *Expect:* the knob and door edge are visible.
2. **Grip the knob.** Wrap fingers around the knob with palm centered and thumb opposing. → *Expect:* the hand has full contact without slipping.
3. **Rotate toward the latch release.** Turn clockwise or counterclockwise with moderate wrist torque until resistance changes. → *Expect:* the latch retracts or the knob reaches its stop.
4. **Apply door motion.** While holding the rotation, push or pull the door in the opening direction. → *Expect:* the door edge separates from the frame.
5. **Open to safe clearance.** Move the door slowly until there is enough passage width. → *Expect:* the gap is stable and no person is contacted.
6. **Release the knob.** Let the knob rotate back after the latch clears the strike plate. → *Expect:* the knob returns and the door remains in the desired open position.

## Decision points

- Knob turns but door does not open → check whether the door should push or pull.
- Knob does not turn → confirm lock status or stop if access is not authorized.
- Person is near the swing path → pause until clear.

## Failure modes & recovery

- **F1 Latch binds:** detect by knob turned but door stuck at frame → push the door closed slightly, keep knob turned, then pull or push again.
- **F2 Hand slips:** detect by loss of rotational control → dry the knob or use a firmer full-hand grip.
- **F3 Door swings too fast:** detect by rapid movement after latch release → catch the knob or door edge and slow the swing.

## Verification

The latch is retracted during motion and the door opens enough for the intended passage without contacting people or obstacles.

## Variations

- Lever handle: press the lever downward instead of rotating a knob.
- Heavy door: use the other hand on the door surface for controlled movement after latch release.

## Safety & privacy

Only open doors when authorized. Move slowly near people, pets, or unseen spaces behind the door.
