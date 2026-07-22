---
name: dispense-tape-from-a-roll
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
objects: [tape-roll, tape-end, dispenser, serrated-edge, package]
affordances: [grasp, find-edge, pull, tension, tear, adhere]
workspace: kitchen counter
safety: {hot_surfaces: false, sharp_objects: true, fragile: [], human_proximity: continue}
---

## Goal

A controlled strip of tape is pulled, torn on the serrated edge, applied without folding onto itself, and the tape end remains findable.

## Preconditions

- Tape roll is mounted in a dispenser or held so it can rotate freely.
- Target surface is clean and dry enough for adhesion.
- Serrated cutting edge is visible and not covered by old adhesive.

## Steps

1. **Find the tape end.** Rotate the roll slowly and feel for the raised edge with a thumb pad or fingernail. → *Expect:* a small tab lifts from the roll.
2. **Peel a starter tab.** Pinch the lifted edge between thumb and index finger and pull it free by a few centimeters. → *Expect:* tape separates as a flat ribbon, sticky side down.
3. **Anchor the dispenser.** Hold the dispenser body or roll core with the opposite hand so only the roll turns. → *Expect:* dispenser stays in place under pulling force.
4. **Pull the desired length.** Draw the tape straight out with steady tension, keeping the strip away from itself and the counter. → *Expect:* strip remains flat and does not twist.
5. **Set against the serrated edge.** Angle the tape downward over the cutter with the planned cut line touching the teeth. → *Expect:* tape stretches tight across the full cutter width.
6. **Tear with a snap.** Pull down and slightly forward in one short motion while keeping the dispenser anchored. → *Expect:* tape separates cleanly at the teeth.
7. **Apply from one end.** Place one end on the target, then smooth along the strip with a fingertip using light pressure. → *Expect:* tape lies flat with no bubbles or folded sticky spots.
8. **Stick the tab back.** Press the remaining tape end to the dispenser lip or fold a tiny nonsticky handle at the end. → *Expect:* next-use tab is visible and can be pinched.

## Decision points

- Tape tears lengthwise before the cutter → discard the split segment and restart with a wider grip on the end.
- Tape has no dispenser → hold the roll core with two fingers and tear against scissors or a known safe edge.
- Archival or painted surface → test adhesion on a hidden area before applying.

## Failure modes & recovery

- **F1 End cannot be found:** tape edge blends into the roll → rub around the roll with a fingernail until a lip catches, then mark it with a folded tab.
- **F2 Tape folds onto itself:** sticky sides touch → peel apart slowly from the fold edge or discard if the adhesive is contaminated.
- **F3 Ragged tear:** tape was slack at the cutter → re-tension across the teeth and tear with a shorter downward motion.
- **F4 Weak adhesion:** strip lifts after smoothing → clean and dry the target, then apply a fresh strip with firmer fingertip pressure.

## Verification

The tape strip is adhered flat to the intended surface and the remaining roll has a reachable tab on or near the dispenser edge.

## Variations

- Packing tape: use the dispenser brake or thumb on the roll to control heavy unwind speed.
- Painter tape: tear more slowly and smooth lightly to avoid stretching the paper backing.
- Double-sided tape: keep liner on until the strip is positioned, then peel the liner from a corner.

## Safety & privacy

Low risk. Serrated cutters can scratch skin, and tape can damage paper, paint, or labels when removed, so verify the surface before pressing hard.
