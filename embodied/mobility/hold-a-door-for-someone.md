---
name: hold-a-door-for-someone
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [door, door-handle, person, threshold]
affordances: [grasp, push, pull, hold-open, step-aside]
workspace: indoor-doorway
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: slow}
---

## Goal

A door is held open for an approaching person so they can pass through without breaking stride or touching the door, then the door is handed off or released cleanly without letting it swing back into anyone.

## Preconditions

- A person is approaching the doorway within a reasonable range and heading through it.
- The door's swing direction and mechanism (push, pull, or self-closing) are readable.
- The robot can reach and hold the door edge or handle without blocking the opening.

## Steps

1. **Judge the approach distance.** Hold the door only if the person is close enough to reach it in a few seconds (roughly within 3 to 4 meters and clearly heading in). Beyond that, holding forces them to hurry, which is worse than not holding. → *Expect:* a person who will arrive within a couple of seconds, not one you make jog across a lobby.
2. **Position to the hinge side, out of the path.** Stand on the side the door opens toward so your body is beside the opening, not in the doorway itself. → *Expect:* the full width of the doorway is clear for the person to walk through.
3. **Take the door by its edge or handle.** Grip near the outer edge (more leverage, less force) rather than the middle. For a pull door, open it and hold; for a push door, hold it open against its closer. → *Expect:* the door held stationary at a comfortable open angle, not drifting.
4. **Keep hands and fingers off the pinch zones.** Grasp the face or handle, never the hinge gap or the latch edge where the person will pass. → *Expect:* no body part between the door and the frame at the hinge.
5. **Signal and let them pass.** A small still gesture or steady hold tells them to go first; hold until they are through. [BRANCH: their hands are full or they use a mobility aid → hold the full time and give extra clearance | they reach to take the door → hand off, see next step] → *Expect:* the person passes through without touching the door or slowing.
6. **Hand off or release cleanly.** If they take the door, wait until you feel them holding its weight before you let go. If not, keep hold until they are fully clear, then let it close under control (guide a heavy or fast closer, do not just drop it). → *Expect:* the door never swings back onto the person or clips their heels.
7. **Decide when not to hold.** Do not hold a door that is a fire door meant to stay latched, do not block a busy two-way doorway by standing in it, and do not hold for someone who has clearly waved you through first. → *Expect:* fire and self-closing safety doors returned to closed; no doorway congestion created.

## Decision points

- Person is far but approaching → make eye contact and gesture rather than committing to a long awkward hold.
- Two-way heavy traffic → step through yourself and keep moving instead of jamming the opening.
- Automatic or revolving door → do not intervene; let the mechanism work.

## Failure modes & recovery

- **F1 Misjudged distance:** person is farther than they looked and now feels rushed → wave them to take their time or release and re-offer as they arrive.
- **F2 Door slips from grip:** heavy closer overcomes the hold → step clear of the swing path, warn the person, and let it close on empty space, never toward them.
- **F3 Blocking the opening:** standing in the doorway backs up traffic → shift fully to the hinge side or pass through and hold from the far side.
- **F4 Handoff dropped early:** released before they had the weight → apologize, re-catch if reachable; next time wait to feel the transfer.

## Verification

The person passed through the doorway without touching the door or breaking stride, no one was struck by the door on its return, no fire or safety door was propped, and the doorway was never blocked.

## Variations

- `heavy-institutional`: strong closers on hospital and office doors need a firm two-point hold and controlled release; budget more force.
- Outward-swinging door toward the approaching person: open it toward yourself and stand well aside so the swing arc stays clear of them.

## Safety & privacy

Low risk: the hazards are pinched fingers at the hinge and the door swinging back onto someone. Human proximity is slow: hold extra clearance for people with full hands or mobility aids. Do not prop fire-rated doors. No personal data involved.
