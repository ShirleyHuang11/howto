---
name: rinse-a-vegetable
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [vegetable, faucet, sink, towel, colander]
affordances: [grasp, faucet-operate, rotate, rub, shake, place]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

A vegetable is rinsed under running water, loosened surface dirt is removed, and excess water is shaken off before use.

## Preconditions

- The sink is clear and clean enough for food contact.
- The vegetable is whole or large enough to handle under the stream.
- A towel, cutting board, bowl, or colander is ready for the rinsed vegetable.

## Steps

1. **Inspect the vegetable.** Look for heavy dirt, damaged spots, or stickers. → *Expect:* visible debris and labels are identified before rinsing.
2. **Start cool water.** Open the faucet to a gentle stream that will not splash out of the sink. → *Expect:* steady cool water falls into the basin.
3. **Place under stream.** Hold the vegetable with fingers away from the drain and rotate it into the water. → *Expect:* the first surface is fully wetted.
4. **Rub the surface.** Use fingertips to rub along the skin while water runs over the contact area. → *Expect:* dirt releases and flows away.
5. **Rotate and repeat.** Turn the vegetable until all sides, ends, and creases pass under the stream. → *Expect:* no dry unwashed patch remains.
6. **Check stubborn spots.** [BRANCH: dirt remains | surface clean] Rub remaining dirt with firmer fingertip pressure; proceed if clean. → *Expect:* stuck particles are removed or marked for trimming.
7. **Shake off water.** Hold over the sink and shake with short downward motions. → *Expect:* loose drops fall into the basin.
8. **Set down cleanly.** Place the vegetable on a clean towel, board, or colander away from dirty sink surfaces. → *Expect:* rinsed vegetable rests on a clean surface.

## Decision points

- Leafy vegetable → separate leaves enough for water to reach inner folds.
- Delicate vegetable → reduce water flow and rub lightly to avoid bruising.
- Heavy dirt → rinse, rub, and rinse again before moving to a cutting board.

## Failure modes & recovery

- **F1 Vegetable slips:** item starts falling toward the sink → catch against the basin wall, rinse again, and improve grip.
- **F2 Splashing:** water hits the item and sprays outward → lower the flow or angle the vegetable into the stream.
- **F3 Dirt remains:** particles stay in creases → rotate under water and rub that area again.
- **F4 Clean item touches dirty basin:** contamination occurs → repeat the rinse before use.

## Verification

All visible surfaces of the vegetable have been rinsed and rubbed, no loose dirt is visible, and the vegetable rests on a clean surface.

## Variations

- `berries`: use a colander and gentle flow, with no hard rubbing.
- `leafy-greens`: rinse leaves individually or agitate in a bowl of clean water.
- `root-vegetable`: scrub with a brush if the parent recipe requires skin-on use.

## Safety & privacy

Low risk. Keep the faucet flow controlled to prevent slippery floors, and avoid placing clean food back onto sink surfaces that contacted dirty dishes.
