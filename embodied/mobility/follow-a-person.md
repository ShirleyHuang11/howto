---
name: follow-a-person
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [person, floor, corridor, doorway]
affordances: [locomote, turn, stop, track-target]
workspace: indoor-public
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: slow}
---

## Goal

Stay a comfortable, consistent distance behind a designated person as they walk through a building, keeping visual contact through turns and doorways without crowding, blocking, or losing them.

## Preconditions

- One specific person is designated as the leader (by appearance, badge, or an explicit "follow me").
- The route is walkable for the robot: no stairs-only segments, clearances wide enough for the chassis.
- Sensors can see the leader's torso/legs; lighting is adequate.

## Steps

1. **Lock onto the leader.** Capture a stable appearance signature (clothing color, height, gait) plus current position. → *Expect:* a single tracked target with a confidence estimate, not a cluster of nearby people.
2. **Set the follow distance.** Hold roughly 1.5 to 2 meters on open floor, closing to about 1 meter in tight or crowded spaces so others cannot cut between you. → *Expect:* gap steady within a person's stride length, not oscillating.
3. **Match speed, do not chase.** Accelerate smoothly when the gap grows, ease off before you reach them. Never approach from directly behind at speed. → *Expect:* the leader does not glance back or slow, meaning they do not feel crowded.
4. **Handle corners by cutting the delay, not the corner.** When the leader turns, follow their actual path around the pivot rather than the shortest diagonal, which would put you in oncoming traffic or against the wall. → *Expect:* you round the corner on the same side of the corridor they did.
5. **At a corner or doorway, close the gap first.** Before a blind turn, shorten distance to about 1 meter so the leader stays in view around the edge. [BRANCH: leader visible through turn → resume normal gap | leader momentarily occluded → hold last-seen heading and continue to the corner] → *Expect:* re-acquisition of the same signature within 2 to 3 seconds of the turn.
6. **Yield at pinch points.** In doorways and narrow passages, let the leader clear the gap fully before entering; do not shoulder through beside them. → *Expect:* single-file passage, no contact with the frame or the person.
7. **Run the lost-contact protocol if the target drops.** ⚠️ *Irreversible:* do not lock onto a wrong person and walk off with a stranger. On loss, stop, scan the last-seen bearing and the two adjacent exits, and re-match on the full signature (not color alone). → *Expect:* either re-acquisition of the correct leader or a clean stop-and-wait, never a confident latch onto someone new.

## Decision points

- Two people match the signature → do not guess; stop and request confirmation or wait for the real leader to move distinctively.
- Leader stops and turns to face you → hold position at conversational distance (about 1.2 meters), do not keep closing.
- Crowd density spikes → tighten to 1 meter and reduce speed rather than pushing the original gap.

## Failure modes & recovery

- **F1 Target swap:** confidence drops as a similar-dressed person crosses → freeze, re-match on height and gait, resume only above a set confidence threshold.
- **F2 Lost at a corner:** leader gone after a blind turn → advance to the pivot point, scan both branches, hold if ambiguous rather than picking a hallway.
- **F3 Crowding the leader:** they keep glancing back or slowing → increase gap by half a meter and drop speed.
- **F4 Doorway jam:** door closes between you and the leader → stop, do not force the door on them; wait for it to reopen or for the leader to hold it.

## Verification

The robot ends adjacent to the leader at the destination, having maintained visual contact for the whole route, with no collisions, no wrong-person follows, and no instance of blocking a doorway or the leader's path.

## Variations

- `outdoor`: widen the base gap to 2 to 3 meters for higher walking speeds and account for sun glare washing out the appearance signature.
- Escort mode: some tasks want the robot slightly ahead and to one side rather than behind; the distance and yielding rules still apply, mirrored.

## Safety & privacy

Medium risk: the main hazards are colliding with the leader or bystanders and mistakenly following a stranger. Human proximity is slow: reduce speed near people and never accelerate toward someone's back. Appearance signatures are held only for the duration of the follow and discarded afterward.
