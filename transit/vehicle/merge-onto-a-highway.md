---
name: merge-onto-a-highway
domain: transit
subdomain: vehicle
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 5min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You enter highway traffic smoothly at a safe speed, choose a gap, and merge without forcing other drivers to brake or swerve.

## Preconditions

- You are legally licensed, alert, and driving a roadworthy vehicle.
- Your mirrors are adjusted and you understand local right-of-way rules for merge lanes.
- The ramp and highway conditions allow normal acceleration; in heavy rain, snow, or poor visibility, use extra following distance.

## Steps

1. **Scan before the ramp opens.** Look ahead for ramp length, lane drops, stopped traffic, and highway speed. → *Expect:* you know whether this is a normal acceleration lane, a short ramp, or a congested merge.
2. **Signal early.** Turn on the indicator toward the highway before you begin matching traffic. → *Expect:* drivers behind and beside you can see your intent.
3. **Accelerate in the ramp lane.** Build speed to roughly match the highway traffic while staying within the ramp and posted limits. → *Expect:* your vehicle is close enough to traffic speed that merging will not require a sudden slowdown.
4. **Find a gap, not a car.** Check mirrors and glance over your shoulder toward the target lane, then choose the open space between vehicles. → *Expect:* you have identified one usable gap and know whether you need to speed up slightly or ease off.
5. **Adjust speed smoothly.** [BRANCH: gap is ahead, accelerate gently into it | gap is behind, ease off and let the vehicle pass] Do not stop at the end of the ramp unless traffic is stopped or a yield/stop sign requires it. → *Expect:* your car is aligned with the selected gap.
6. **Merge with steady steering.** Move into the lane once your front and rear clearance are safe, keeping your signal on until the lane change is complete. → *Expect:* you are centered in the highway lane without cutting off another vehicle.
7. **Cancel the signal and reestablish space.** Match the flow of traffic and leave at least a safe following interval. → *Expect:* your vehicle is stable in the lane with predictable spacing ahead and behind.

## Decision points

- Ramp has a posted yield sign → you must yield to highway traffic and may need to slow or stop if no gap exists.
- Ramp lane continues as an added lane → continue in that lane until it is safe to change lanes; do not force an immediate merge.
- Traffic is bumper-to-bumper → signal, match the low speed, and zipper merge one vehicle at a time where the lane ends.
- A driver speeds up to block your gap → abandon that gap and choose the next one; do not compete.

## Failure modes & recovery

- **F1 Too slow at lane end:** detect highway traffic closing quickly behind you → keep scanning, use the shoulder only if necessary to avoid a collision, and merge at the first safe gap.
- **F2 Blind-spot vehicle:** detect a horn, vehicle alongside, or mirror surprise → hold your lane, cancel the merge, and choose a new gap.
- **F3 Short ramp panic:** detect that the acceleration lane is ending faster than expected → prioritize steering control, brake only as needed, and merge behind traffic rather than in front of it.
- **F4 Missed merge:** detect no safe opening before the lane ends → continue onto the shoulder only long enough to stop safely or reenter when legal and safe.

## Verification

You are fully centered in a highway lane, traveling with traffic flow, your signal is off, and no surrounding driver had to brake or swerve because of your merge.

## Variations

- `us`: many ramps are acceleration lanes; yield signs still override the general pattern.
- `uk-au-nz`: merge direction and lane position may be opposite on left-driving roads; the same gap-selection logic applies.
- Metered ramp: obey the ramp signal first, then accelerate and merge from the release point.

## Safety & privacy

Medium risk because a poor merge can cause a crash. Do not text, force a gap, stop unnecessarily in an acceleration lane, or rely only on mirrors; shoulder-check before moving laterally.
