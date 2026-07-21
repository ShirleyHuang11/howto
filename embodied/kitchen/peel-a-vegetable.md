---
name: peel-a-vegetable
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
objects: [vegetable, peeler, cutting-board, bowl, trash-bin]
affordances: [grasp, stabilize, scrape, rotate, place]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: true, fragile: [], human_proximity: slow}
---

## Goal

The vegetable has its outer skin removed with controlled peeler strokes, and peelings are contained for cleanup.

## Preconditions

- A clean vegetable is on a stable cutting board or held over a bowl.
- A functional vegetable peeler is available with an intact blade and dry handle.
- Hands are dry enough to maintain grip, and the peel catch bowl or trash bin is within reach.

## Steps

1. **Stage the catch area.** Place the bowl or bin opening below the work path, close enough that peels drop into it without reaching across the blade. → *Expect:* the catch area sits below the vegetable and does not wobble.
2. **Grip the vegetable.** Hold one end with the support hand, fingers curled back from the peel path, or stabilize it flat on the board if it rolls. → *Expect:* the vegetable resists light pulling without slipping.
3. **Grip the peeler.** Wrap the dominant hand around the handle with the blade facing away from the body and away from the support hand. → *Expect:* the peeler edge is visible and the handle does not rotate in the hand.
4. **Start a test stroke.** Touch the blade near the far end and draw it away from the body with light pressure. → *Expect:* a thin strip of peel separates without gouging deep flesh.
5. **Peel in lanes.** Repeat long strokes from near to far, overlapping each lane slightly and keeping the wrist aligned with the blade. → *Expect:* exposed vegetable flesh forms clean parallel bands.
6. **Rotate the vegetable.** Turn it a quarter turn after each exposed band set, moving the support hand before the blade moves again. → *Expect:* unpeeled skin faces the peeler and fingers remain outside the stroke path.
7. **Trim ends carefully.** [BRANCH: flat end | rounded end] For a flat end, rest it on the board; for a rounded end, use short outward strokes only. ⚠️ *Irreversible:* cuts from the peeler edge require stopping before skin contact. → *Expect:* end skin is removed or left as a small safe patch.
8. **Set down and collect peels.** Place the peeled vegetable on the board, then move peelings into the trash or compost without touching the blade. → *Expect:* peeled vegetable is separate from waste and the peeler is at rest.

## Decision points

- Vegetable rolls under light pressure → switch to board stabilization and peel the top face before rotating.
- Peeler catches or digs → reduce pressure, lower the blade angle, and resume with shorter strokes.
- Human hand enters the stroke path → pause motion until the hand is clear.

## Failure modes & recovery

- **F1 Grip slip:** vegetable twists or peeler skids → dry the surface and hand, reset the grip, and restart with shorter strokes.
- **F2 Deep gouge:** thick flesh comes off with the peel → reduce force and use shallower blade contact on the next lane.
- **F3 Peels scatter:** strips miss the bowl or bin → move the catch area closer under the active stroke path before continuing.
- **F4 Blade nick:** skin contact or bleeding occurs → stop, put the peeler down, clean and treat the cut before resuming.

## Verification

The vegetable surface is mostly free of outer skin, remaining peel patches are intentional and small, the peeler is stationary, and loose peels are contained.

## Variations

- `carrot`: hold by the thick end first, then reverse grip for the last unpeeled section.
- `potato`: use shorter strokes around eyes and decide whether small eyes need a knife-tip task instead.
- `cucumber`: peel alternating stripes if texture or appearance matters.

## Safety & privacy

Medium risk from a sharp peeler blade near the support hand. Keep strokes away from the body, slow down near rounded ends, and pause whenever another person reaches into the workspace.
