---
name: sweep-a-floor-with-a-broom
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [broom, dustpan, trash-bin, chairs]
affordances: [grasp, sweep-stroke, lift, place, pour, crouch]
workspace: household-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: slow}
---

## Goal

A hard floor is free of visible crumbs, dust, and debris, with everything collected into the dustpan and binned, and moved furniture returned to place.

## Preconditions

- A broom with bristles that still hold their shape (splayed bristles scatter instead of gather).
- A dustpan and a reachable trash bin.
- Hard flooring (wood, tile, laminate, vinyl); carpet needs a vacuum, not this recipe.
- Loose obstacles (chairs, mats, cables) can be lifted or shifted.

## Steps

1. **Clear the floor first.** Lift chairs onto the table or shift them out, shake mats outside, pick up cables and large litter by hand. → *Expect:* open floor with only sweepable debris left on it.
2. **Pick a collection spot and a direction.** Sweep from the far corner toward one open spot near the exit or bin, never toward already-cleaned floor. → *Expect:* a mental lane map: perimeter and corners first, open middle last.
3. **Sweep with short, overlapping pull strokes.** Hold the broom like a canoe paddle (one hand on top, one mid-shaft), bristles at a low angle, and pull debris toward you in 30 to 50 cm strokes. Do not flick: long fast strokes launch fine dust airborne. → *Expect:* debris moves in a growing line ahead of the bristles; no dust cloud rising.
4. **Work edges and corners with the broom's corner.** Use the bristle tip edge to rake debris out of corners and along baseboards into the open, then rejoin the main pattern. → *Expect:* baseboard lines free of the gray dust ribbon that collects there.
5. **Merge into one pile per zone.** In large or multi-room spaces, build a small pile per zone rather than pushing one pile long distances; long pushes shed a trail. → *Expect:* one compact pile in each zone, floor behind you clean.
6. **Hold the dustpan and load the pile.** Crouch, press the dustpan lip flat and firm against the floor, and sweep the pile in with short strokes. → *Expect:* bulk of the pile inside the pan on the first pass.
7. **Beat the dustpan line.** A thin line of fine dust always remains at the pan lip. Back the pan up 20 cm and sweep the line in again at a shallower angle; repeat once or twice more. → *Expect:* the line shrinks each pass to nearly nothing. Line will not shrink → F2.
8. **Empty the pan into the bin low and slowly.** Tip it deep inside the bin to avoid puffing dust back out. → *Expect:* pan empty, no dust plume.
9. **Restore the room.** Return chairs, mats, and anything moved. → *Expect:* room in its original arrangement over clean floor.

## Decision points

- Debris includes broken glass → do not use bare hands at the pan; sweep glass gently, collect with dustpan into a rigid container or wrapped bundle, then damp-paper-towel the area for invisible slivers, and treat sharp risk as active.
- Mostly fine dust on smooth flooring → a dust mop or slightly dampened broom outperforms dry bristles, which just redistribute it.
- People or pets crossing the workspace → pause the stroke and let them pass; a mid-stroke broom is a trip hazard at ankle height.

## Failure modes & recovery

- **F1 Dust cloud rising while sweeping:** strokes are too long and fast → shorten the stroke, lower the bristle angle, and slow down; lightly misting the pile settles it.
- **F2 Persistent dustpan line:** the pan lip is worn or the floor is uneven → step the pan back and take the line at a near-flat broom angle, or finish the last line with a damp paper towel; that is standard practice, not failure.
- **F3 Debris stuck to the floor (dried spills, sticky spots):** bristles skip over them → stop sweeping, scrape with a plastic scraper or wipe with a damp cloth, dry, then resume.
- **F4 Broom sheds bristles or scatters instead of gathering:** splayed or clogged head → pull trapped hair and lint from the bristles first; if still scattering, the broom is end-of-life for fine debris.

## Verification

Sight down the floor at a low angle against the light: no crumbs, hair, or dust ribbons along baseboards or in corners, the dustpan is emptied and stowed, and the furniture is back in place.

## Variations

- Outdoor sweeping (patio, steps): stiff-bristle push broom, sweep with the wind at your back, and skip the fine-dust standards.
- Soft dual-bristle indoor brooms: fine flagged tips gather dust well but clog with hair faster; clean the head more often.

## Safety & privacy

Low risk overall. The real hazards are secondary: broken glass in the debris (never handle near the pan bare-handed) and the trip hazard of a broom or pile left mid-floor. Slow the stroke whenever a person or pet is within reach of the broom head.
