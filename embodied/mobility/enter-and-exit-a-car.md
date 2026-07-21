---
name: enter-and-exit-a-car
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [car, door, seat, seatbelt, curb]
affordances: [grasp, door-open, door-close, sit, pivot, buckle, stand]
workspace: roadside
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: slow}
---

## Goal

You enter a parked car, seat yourself, and buckle in, then later exit safely onto a clear space, without a door strike, a fall, or stepping into traffic.

## Preconditions

- The car is stopped and, ideally, parked with the engine off or in park.
- You know which side is the curb side versus the traffic side; whenever possible, enter and exit on the curb side.
- Hands are free enough to grasp the door and frame; set loads down or hand them in separately.

## Steps

1. **Check the door-swing zone before opening.** Glance for passing cyclists, cars, other opening doors, and low posts or curbs the door edge could hit. On the traffic side, this check is the difference between a routine exit and a dooring. → *Expect:* clear arc for the door swing; no approaching bike or vehicle in the lane beside the door.
2. **Open the door only as far as needed.** Wide enough to enter, not flung to its stop where it can strike an adjacent car or spring back on a slope. → *Expect:* door held at a controlled opening; it stays where you put it.
3. **Enter seat-first, not head-first.** Turn your back to the seat opening, lower onto the seat edge, then pivot both legs in together as a unit. Leading with the head or one leg is how people bang their skull on the frame or half-miss the seat. → *Expect:* you are seated on the cushion with both feet swinging in as a pair, head clearing the frame.
4. **Settle and clear the door path.** Feet and clothing fully inside; check no coat hem, bag strap, or belt is in the door gap. → *Expect:* nothing crossing the door threshold.
5. **Close the door to the latch.** Pull it firmly to the first full latch; a half-latched door reads as closed but opens in motion. → *Expect:* a solid single clunk, not a soft partial one; the ajar indicator, if any, is off.
6. **Buckle immediately, before the car moves.** Draw the belt smoothly (a jerk locks the retractor), seat the lap belt low across the hips not the belly, and click the tongue home. ⚠️ *Irreversible:* an unbelted occupant in a crash cannot be undone; buckle before the vehicle rolls, every time. → *Expect:* an audible click, belt lying flat across hips and chest, no slack or twist.
7. **Exit prep: confirm the car is stopped and check traffic.** Before touching the handle to leave, confirm the vehicle is fully stopped and parked, then check over your shoulder and through the window for approaching traffic and cyclists on your side. → *Expect:* car stationary; your side clear of moving traffic.
8. **Unbuckle, then crack the door and re-check.** Release the belt and guide it back (do not let it snap). Open the door a hand's width first and look again, especially on the traffic side. [BRANCH: curb side → open and exit | traffic side → open narrowly, verify clear, exit quickly and close] → *Expect:* a confirmed-clear gap before the door opens wide.
9. **Exit legs-first.** Pivot both feet out to the ground together, plant them, grasp the frame or door, then stand. Stepping out one leg while still seated twisted is the common slip, especially onto a curb or in the wet. → *Expect:* both feet planted on stable ground, then a controlled stand.
10. **Close the door and step clear.** Firm it to the latch, step onto the curb or away from the lane. → *Expect:* door latched, you standing clear of the traffic lane.

## Decision points

- Only the traffic-side door is available (curb-side blocked) → treat every step of the door check as if a bike is coming, open narrowly, exit briskly, and close; do not linger in the door gap.
- High vehicle (SUV, truck, van) → use the grab handle and step, enter feet-to-step then up-and-in rather than the low-car pivot; the seat-first rule still holds for the final sit.
- Low sports car or deep bucket seat → sit onto the seat edge higher than expected, then slide down and in; exiting, scoot forward to the edge first to get your feet under you before standing.
- Child seat or passenger who needs help → belt them before you take your own driver seat, and exit them on the curb side always.

## Failure modes & recovery

- **F1 Door strikes an adjacent car or post:** felt or heard on opening → stop the swing immediately, close slightly, and reposition your entry; on a slope, keep a hand on the door the whole time so it cannot swing free.
- **F2 Belt retractor locks and will not extend:** it jammed from a fast pull → let it fully retract, then draw it out slowly and steadily; leaning back off the belt anchor helps release it.
- **F3 Slip on exit (wet ground, curb, ice):** detected as a foot sliding as you stand → sit back down, get both feet planted flat first, use the frame handhold, and stand only when balanced.
- **F4 Door not fully latched:** a warning light or wind noise once moving → do not open it in motion; pull over when safe, then reopen and firm it to the latch.

## Verification

You are seated with the belt clicked, lying flat and low across the hips, before the car moved; on exit, the vehicle was confirmed stopped, your side was checked clear, you exited legs-first onto stable ground, and the door is latched with you standing clear of traffic.

## Variations

- Locale drive side: in left-hand-traffic countries (UK, Japan, Australia) the curb side and traffic side are mirrored; the checks are identical, the geometry flips.
- Ride-hail or taxi: always exit curb-side onto the sidewalk, never into the road; this is the single most enforced rule in dooring-prevention campaigns for passengers.
- Reduced mobility: a swivel cushion or a firm grab handle turns the pivot into one smooth motion; lead with the strong side and let the handhold, not a twist, take the load.

## Safety & privacy

Medium risk from two hazards: dooring a passing cyclist or vehicle on the traffic side, and falls while entering or exiting onto curbs or wet ground. The habits that prevent both are the door-swing check before every opening and the legs-together pivot instead of a one-leg twist. Buckle before the car moves, without exception.
