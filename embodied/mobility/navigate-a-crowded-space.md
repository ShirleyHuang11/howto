---
name: navigate-a-crowded-space
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [self, crowd, obstacles, exits]
affordances: [walk, turn, pace-match, yield, announce, pause]
workspace: crowded-public-space
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: slow}
---

## Goal

You cross a crowded space (station concourse, market, sidewalk, event floor) to your destination smoothly, without collisions, without blocking others, and without causing the pile-ups that sudden moves create.

## Preconditions

- A known destination or at least a heading; wandering aimlessly in a crowd is what makes you an obstacle.
- Hands and bags managed close to your body so you present a predictable, narrow profile.
- Awareness that human_proximity here is the entire task: everyone around you is continuously close and moving.

## Steps

1. **Read the flow before entering.** Pause at the edge and watch for a few seconds: crowds self-organize into lanes moving opposite directions. Find the lane heading your way. → *Expect:* you can name which side moves toward your destination and roughly how fast.
2. **Enter by merging, not cutting.** Step into the near lane at its pace, as you would merging onto a road, rather than crossing all lanes at once. → *Expect:* you join a stream without anyone breaking stride around you.
3. **Match the pace of your lane.** Move at the speed of the people ahead, not your own preferred speed. Walking much faster forces constant passing; much slower makes you a dam. → *Expect:* the gap to the person ahead stays roughly constant; no one is stacking up behind you.
4. **Aim your eyes and body where you intend to go.** People read your shoulders and gaze to predict your path and yield accordingly; a fixed forward gaze telegraphs your line. → *Expect:* oncoming people drift to give you a lane; you and approaching walkers resolve the classic shuffle by both committing to one side early.
5. **Pass on a consistent side and signal it.** [BRANCH: quiet crowd → drift to the passing side, a beat of eye contact suffices | dense or noise-free needed → a light "on your left" or a raised hand as you approach] Overtake decisively on the locale's passing side, then return to lane. → *Expect:* a clean pass with the overtaken person aware of you; no clip of shoulders or bags.
6. **Never stop dead in the stream.** If you must check a phone, map, or bag, drift to the edge or an eddy (a pillar, a wall, a corner) first. A sudden stop mid-flow causes the person behind to collide and cascades backward. → *Expect:* when you halt, you are out of the moving lane against a fixed edge, facing so you do not block.
7. **Signal turns and exits early.** Before cutting across lanes to a doorway or stairwell, glance back, angle your body toward it a few steps ahead, and cross at a shallow diagonal. → *Expect:* you reach the exit lane without forcing anyone to brake; cross-traffic anticipates your diagonal.
8. **Arrive and clear.** At your destination, step fully out of the flow before stopping to orient or wait. → *Expect:* you are stationary in an eddy or against an edge, not marooned in a lane.

## Decision points

- Two oncoming people and you keep mirroring into each other → commit hard to one side and slightly exaggerate the move; the deadlock breaks when one party is unambiguous.
- Pushing a stroller, cart, or wheeling luggage → you are now wider and slower; take the outer lane, signal turns earlier, and never reverse without looking back.
- Crowd density rising toward a crush (shoulder-to-shoulder, involuntary movement) → this is a safety situation, not a navigation one; move with the crowd, stay upright, keep toward the edges and away from walls and barriers, and head for open space.
- Carrying a child or leading someone → keep them on your non-passing side and slightly behind, and announce stops to them so they do not cause the sudden-stop cascade.

## Failure modes & recovery

- **F1 Boxed in with no lane toward your goal:** detected as being carried the wrong way → do not fight across; ride the current to the next opening or eddy, then re-read the flow and merge again.
- **F2 Near-collision from an overtaker you did not hear:** felt as a sudden presence at your shoulder → do not stop or veer abruptly, hold your line for a beat and let them complete the pass, then adjust.
- **F3 You caused a stack-up behind you:** noticed as bunching or a bump from behind → you slowed or drifted unpredictably; pick up to lane pace or pull to the edge, do not apologize by stopping, which worsens it.
- **F4 Dropped item in the flow:** → do not stoop in the lane; step to the edge if the item is retrievable safely, or let it go in a dense crush where stooping risks a fall.

## Verification

You reached your destination without a collision; you did not stop dead in a moving lane at any point; passes were made on a consistent side with awareness; and when you halted you were in an eddy or against an edge, out of the flow.

## Variations

- Locale passing side: keep-right cultures (US, continental Europe) pass and yield to the right; keep-left cultures (UK, Japan, Australia) mirror it. Match the local default rather than imposing your own.
- Robot or assistive-device navigation: encode lane-reading as flow-field estimation, pace-matching as speed regulation to the local median, and the no-sudden-stop rule as a hard deceleration limit; announce passes with an audible cue.
- Dense market or festival with cross-flows: lanes break down; shift to short committed moves between eddies, more eye contact, and lower speed.

## Safety & privacy

Low risk in ordinary crowds. The one escalation to respect: a dense crowd can become a crush, where the danger is compressive, not tripping. If movement becomes involuntary, stop navigating and prioritize staying upright, keeping space in front of your chest to breathe, and edging toward open ground. Keep valuables secured and close in dense crowds where pickpocketing is easiest.
