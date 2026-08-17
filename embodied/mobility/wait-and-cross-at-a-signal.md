---
name: wait-and-cross-at-a-signal
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: basic
est_time: 3min
risk: high
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [crosswalk, signal-button, curb, traffic-light, vehicles]
affordances: [button-press, wait, scan, walk, stop, yield]
workspace: street-crossing
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: slow}
---

## Goal

Wait for the pedestrian signal and cross the street only when traffic behavior and signal state make crossing safe.

## Preconditions

- The crossing is a marked crosswalk or a legally permitted crossing point.
- The destination curb or refuge island is visible.
- The actor can hear or see enough traffic cues to judge movement.

## Steps

1. **Stop before the curb.** Stand back from traffic with toes, wheels, cane, or stroller behind the edge. → *Expect:* no body part extends into the roadway.
2. **Press the pedestrian button if present.** Press once and remain near the crossing. → *Expect:* button feedback appears or the request is queued.
3. **Wait for the walk signal.** Do not start on a red hand or no-walk indication. → *Expect:* the walk symbol, audible cue, or allowed crossing phase begins.
4. **Scan all traffic lanes.** Look left, right, ahead, and behind for turning vehicles and bikes. → *Expect:* vehicles are stopped or yielding in every lane you will enter.
5. **Enter decisively.** Start walking within the crosswalk, keeping a steady pace. → *Expect:* movement is visible to drivers and aligned with the marked path.
6. **Keep scanning while crossing.** Watch turning lanes and vehicles that may pass stopped traffic. → *Expect:* no vehicle enters your path without stopping.
7. **Continue if countdown starts.** [BRANCH: already in crosswalk | still at curb] finish crossing if already started, or wait for the next cycle if still at the curb. → *Expect:* no late start occurs during the flashing phase.
8. **Clear the roadway.** Step fully onto the far curb or refuge island before stopping. ⚠️ *Irreversible:* entering moving traffic cannot be undone instantly; confirm stopped or yielding vehicles before step 5. → *Expect:* the body is out of all traffic lanes.

## Decision points

- A driver waves you through against the signal → obey the signal and traffic law, not the wave alone.
- Vehicle blocks the crosswalk → wait or route behind only when traffic is stopped and visibility is clear.
- Signal never changes → use another marked crossing or call the local reporting number if needed.
- Emergency vehicle approaches → remain on curb or finish to the nearest safe refuge.

## Failure modes & recovery

- **F1 Turning vehicle conflict:** detect vehicle rolling into crosswalk → stop, retreat if near curb, or continue only if that is safer.
- **F2 Late start:** detect flashing hand before entry → stay at curb for next cycle.
- **F3 Hidden lane danger:** detect one lane stopped and another moving → wait until all lanes are stopped.
- **F4 Dropped item:** detect item in roadway → do not retrieve until the signal and traffic make it safe.

## Verification

The person reaches the far curb or refuge island inside the crosswalk, without any vehicle needing abrupt braking or evasive movement.

## Variations

- Accessible pedestrian signal: use audible or vibrotactile cues, then still scan traffic.
- Median refuge: repeat the signal wait from the island for the second half.
- Leading pedestrian interval: begin during the early walk phase while still checking turning vehicles.

## Safety & privacy

High risk because vehicles can cause serious injury. Treat uncertainty as a stop condition, slow around other pedestrians, and avoid exposing phone screens or documents while standing at the curb.
