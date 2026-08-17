---
name: staple-papers-together
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
objects: [stapler, paper-stack, staple, desk]
affordances: [align, grasp, insert, press, release, inspect]
workspace: household
safety: {hot_surfaces: false, sharp_objects: true, fragile: [], human_proximity: continue}
---

## Goal

Fasten a stack of papers with one staple in the intended corner or edge so pages stay aligned and turn easily.

## Preconditions

- Stapler contains staples and closes normally.
- Paper stack is within the stapler capacity.
- Pages are in the correct order and orientation.
- Desk surface is flat.

## Steps

1. **Square the paper stack.** Tap the bottom and side edges on the desk until corners align. → *Expect:* page edges form one clean rectangle.
2. **Choose staple location.** Usually use the upper-left corner, angled about 45 degrees across the corner. → *Expect:* the intended staple path crosses all pages away from text.
3. **Insert the stack into the stapler.** Slide the corner between base and head until the staple mark is under the driver. → *Expect:* paper lies flat and reaches the target depth.
4. **Press straight down.** Hold the stack still and compress the stapler in one firm motion. → *Expect:* a click or snap occurs and the stapler head returns up.
5. **Remove and inspect.** Pull the papers out flat and look at both sides of the staple. → *Expect:* the staple crown is flush and both legs are folded through the stack.

## Decision points

- Stack is too thick → split into smaller sets or use a heavy-duty stapler.
- Pages must be scanned later → staple at a corner that can be removed without tearing text.
- Stapler is empty → reload before pressing again.

## Failure modes & recovery

- **F1 Misaligned pages:** detect shifted edges after stapling → remove staple carefully, realign, and staple again.
- **F2 Staple jams:** detect head stuck or no staple delivered → open the stapler and remove bent staples before retrying.
- **F3 Staple does not penetrate:** detect legs not through all pages → use fewer pages or a stronger stapler.
- **F4 Sharp leg exposed:** detect a staple leg sticking up → flatten it with a staple remover edge or replace the staple.

## Verification

All intended pages are attached in order by a flush staple, and both staple legs are folded without sharp protrusions.

## Variations

- `top-edge`: use two staples along the top for landscape packets.
- `temporary`: use a paper clip instead when holes or marks are not acceptable.

## Safety & privacy

Low risk. Staple points are sharp; keep fingers out from under the stapler head and avoid stapling confidential papers into the wrong packet.
