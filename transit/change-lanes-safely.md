---
name: change-lanes-safely
domain: transit
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Change lanes with a deliberate mirror-signal-blindspot-maneuver sequence and enough gap to avoid forcing other drivers to brake or swerve.

## Preconditions

- You are driving a vehicle with adjusted mirrors, working turn signals, and clear windows.
- Lane markings allow a lane change.
- You are alert, sober, and able to keep both hands available for steering.

## Steps

1. **Plan the lane change early.** Identify why you need the lane: exit, turn, passing, obstruction, or lane ending. → *Expect:* the maneuver is not a last-second reaction.
2. **Check mirrors first.** Look at rearview and side mirror for vehicles approaching in the target lane. → *Expect:* you know the traffic pattern behind and beside you.
3. **Signal before moving.** Turn on the signal for several blinks before crossing the lane line. → *Expect:* nearby drivers get clear notice of your intent.
4. **Check the blind spot.** Turn your head briefly toward the target lane while keeping the vehicle straight. → *Expect:* motorcycles, small cars, and fast overtaking vehicles are not hidden beside you.
5. **Judge the gap.** Confirm the target lane has space ahead and behind, and that your move will not make another driver brake hard. → *Expect:* the lane change can happen at traffic speed.
6. **Move smoothly, not suddenly.** [BRANCH: accelerate slightly | hold speed | wait] match the target lane speed, steer gently across the line, or stay put if the gap is not real. → *Expect:* the vehicle crosses predictably.
7. **Change one lane at a time.** Finish in the first target lane, straighten, cancel or reset the signal, then reassess before another lane change. → *Expect:* no diagonal sweep surprises other drivers.
8. **Rebuild following distance.** Once in the lane, leave at least a three-second gap where speed allows. → *Expect:* you are not tailgating the vehicle you moved behind.
9. **Cancel the signal and rescan.** Confirm the signal is off and mirrors show stable spacing. → *Expect:* the lane change is complete and traffic around you is steady.

## Decision points

- Solid line or restricted lane → do not change lanes until markings permit it.
- Blind spot is occupied → hold your lane and keep signaling only if you still intend to move.
- Exit is approaching too fast → continue to the next exit rather than cutting across lanes.
- A driver speeds up to close the gap → let them pass and take the next opening.

## Failure modes & recovery

- **F1 Vehicle in blind spot:** head check reveals someone beside you → stay in lane, cancel or keep signal as appropriate, and wait.
- **F2 Gap collapses:** traffic in target lane brakes or accelerates → abandon the maneuver and continue straight.
- **F3 Signal left on:** other drivers think you still intend to move → cancel it immediately after completing the change.
- **F4 Drifting while checking:** the car moves during the head check → correct gently, refocus forward, and delay the lane change.
- **F5 Forced merge pressure:** lane ends or obstruction approaches → slow, signal, and merge zipper-style when a safe gap appears.

## Verification

The vehicle moves one lane only after mirror, signal, blind-spot check, and gap confirmation, without causing nearby traffic to brake or swerve.

## Variations

- Highways: plan earlier because speed makes gaps close quickly.
- City streets: watch for bikes, buses, parked cars, pedestrians, and turn-only lanes.
- Heavy rain or darkness: use longer gaps and slower steering inputs.
- Large vehicles: allow more room because blind spots and vehicle length are greater.

## Safety & privacy

High risk because unsafe lane changes cause side-swipes and multi-vehicle crashes. Never cut across multiple lanes, never rely only on blind-spot monitors, and do not use a phone or navigation screen during the maneuver.
