---
name: step-onto-a-moving-walkway
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [moving-walkway, handrail, comb-plate, luggage, floor]
affordances: [approach, wait, step, grip, balance, ride]
workspace: transit-concourse
safety: {hot_surfaces: false, sharp_objects: false, fragile: [luggage], human_proximity: slow}
---

## Goal

Step onto a moving walkway and ride it without tripping, blocking others, or losing luggage.

## Preconditions

- The walkway is operating in the intended direction.
- Shoes, wheels, and bags are clear of loose straps or dangling items.
- The rider can stand steadily or has chosen an alternate route.

## Steps

1. **Approach the entry straight on.** Align feet and luggage with the moving belt direction. → *Expect:* the comb plate is directly ahead.
2. **Watch the belt speed.** Pause long enough to match timing and locate the handrail. → *Expect:* the moving surface direction and speed are clear.
3. **Grip the handrail.** Place one hand on the moving rail before stepping. → *Expect:* the hand moves with the walkway.
4. **Step over the comb plate.** Put one foot fully onto the moving surface, then bring the second foot on. → *Expect:* both feet are on the belt and balance is steady.
5. **Bring luggage on fully.** Roll or carry bags past the entry teeth without leaving straps behind. ⚠️ *Irreversible:* caught straps can be pulled into machinery; confirm straps are lifted or contained before entry. → *Expect:* no item trails over the comb plate.
6. **Stand or walk with the flow.** Keep to the local standing side if others pass. → *Expect:* people can pass without brushing you.
7. **Prepare to exit early.** Look ahead and gather bags before the end. → *Expect:* feet and luggage are ready before the exit plate.
8. **Step off cleanly.** Walk over the exit comb plate and continue forward before stopping. → *Expect:* you are on stationary floor clear of the exit.

## Decision points

- Walkway is stopped or reversed → treat it as a flat path only if signs allow use.
- Balance feels uncertain → use the adjacent walkway or elevator instead.
- Crowd blocks the exit → stop walking, hold rail, and step off when space opens.
- Wheeled luggage catches → release forward pull and lift or back it free only if safe.

## Failure modes & recovery

- **F1 Foot hesitation:** detect one foot on moving belt and one on fixed floor → commit the second foot or step back before stretching.
- **F2 Bag lag:** detect luggage still on fixed floor → pull it fully on or step off and retry.
- **F3 Exit crowding:** detect people stopped at the end → call out politely and prepare to step to the side.
- **F4 Handrail mismatch:** detect hand pulled ahead or behind → adjust grip without leaning.

## Verification

The rider and all luggage are on stationary floor beyond the exit, clear of the comb plate and not obstructing following passengers.

## Variations

- With stroller or wheelchair: use elevator or signed accessible route unless the device is explicitly permitted.
- Long walkway: stand to one side and keep bags in front or beside you.
- Airport carts: use only if carts are allowed on that walkway.

## Safety & privacy

Medium risk from moving machinery and crowd pressure. Slow near others, contain straps and loose clothing, and avoid displaying travel documents while managing luggage.
