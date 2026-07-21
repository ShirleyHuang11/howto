---
name: close-curtains-and-blinds
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [curtain, blind, cord, wand, remote, window, tieback]
affordances: [grasp, pull, slide, rotate, press-button, release, align]
workspace: room-with-window
safety: {hot_surfaces: false, sharp_objects: false, fragile: [window-glass, curtain-rod], human_proximity: continue}
---

## Goal

Close curtains or blinds evenly for privacy, light control, or sleep, without tangling cords or stressing the window hardware.

## Preconditions

- Window covering is installed and reachable.
- Hands are dry and free of sticky residue.
- Floor near the window is clear.
- Children and pets are away from dangling cords.

## Steps

1. **Identify the control.** [BRANCH: curtain | cord blind | wand blind | motorized blind] locate the fabric edge, cord, wand, chain, switch, or remote. → *Expect:* the correct control is in hand before pulling.
2. **Release tiebacks.** Undo hooks, magnets, or fabric ties holding curtains open. → *Expect:* fabric hangs freely.
3. **Close curtains by sliding.** Hold the leading edge or pull wand and move fabric along the rod or track. → *Expect:* panels meet or overlap at the center.
4. **Lower blinds if raised.** Pull the cord toward the center to unlock, guide it slowly, then move it back to lock. → *Expect:* the bottom rail descends evenly and stops at the sill.
5. **Tilt blind slats.** Rotate the wand or pull the tilt cords until slats overlap closed. → *Expect:* outside view is blocked while slats remain aligned.
6. **Use motor controls gently.** Press close or down once and wait for movement to finish. → *Expect:* the blind travels without repeated button presses.
7. **Even the bottom edge.** Adjust one side only if the rail or curtain hem is noticeably crooked. → *Expect:* the lower edge is level enough that it does not snag.
8. **Check privacy from inside.** Step back and look for gaps at the center, sides, and sill. → *Expect:* no direct line of sight remains through the covering.
9. **Secure cords safely.** Wind loose cords on a cleat or place them high out of reach. → *Expect:* no loop hangs where a child or pet could reach it.

## Decision points

- If the goal is privacy but some daylight is wanted → tilt slats upward rather than fully lowering blackout coverings.
- If the cord resists → stop pulling and inspect for a lock, knot, or caught slat.
- If curtains are on rings → move several rings at once to avoid bending one ring.
- If the covering is motorized and silent → check remote battery or wall switch power.

## Failure modes & recovery

- **F1 Cord tangle:** detect twisted or knotted cord → support the blind, loosen the knot by hand, and avoid yanking.
- **F2 Crooked blind:** detect one side higher → raise fully, then lower slowly while keeping cords even.
- **F3 Curtain snag:** detect fabric catching on rod, ring, or furniture → back up slightly and free the snag before continuing.
- **F4 Hardware strain:** detect rod flexing or bracket movement → stop, close by hand closer to the support, and schedule repair.

## Verification

The curtains or blinds cover the window evenly, block direct view through the window, and all cords are secured away from children and pets.

## Variations

- Blackout curtains: overlap center edges and press sides toward the wall for fewer light leaks.
- Vertical blinds: rotate vanes open before drawing them across, then rotate closed.
- Sheer plus curtain: close the sheer for daytime privacy and the heavier curtain for night.

## Safety & privacy

Low risk. Cord loops are a serious strangulation hazard for children and pets, so secure them high. Closing coverings improves privacy but may also reduce visibility of exits or outdoor hazards.
