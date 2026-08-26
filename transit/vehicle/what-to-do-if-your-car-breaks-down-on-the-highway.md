---
name: what-to-do-if-your-car-breaks-down-on-the-highway
domain: transit
subdomain: vehicle
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: high
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You get a failing vehicle out of traffic, make yourself visible, and arrange help while minimizing the risk of being struck.

## Preconditions

- The vehicle has lost power, has a flat, warning, smoke, or other problem while on a highway or fast road.
- You can still steer and brake enough to reach a safer position, or you are already stopped.
- You have hazard lights and a phone if available.

## Steps

1. **Signal trouble immediately.** Turn on hazard lights and keep both hands on the wheel. → *Expect:* nearby drivers have warning that your vehicle is not moving normally.
2. **Move out of travel lanes if possible.** Coast or drive gently to the right shoulder, breakdown lane, exit ramp, rest area, or wide median only if safer. → *Expect:* the vehicle is no longer in an active lane if reachable.
3. **Stop as far from traffic as you can.** Straighten the wheels or angle away from traffic if appropriate, set the parking brake, and leave hazards on. → *Expect:* the vehicle is stable and visible.
4. **Choose the safest occupant position.** [BRANCH: wide shoulder with barrier nearby, exit away from traffic and stand behind barrier | narrow shoulder, bridge, tunnel, heavy traffic, or no barrier, stay belted inside unless fire/smoke makes that unsafe] → *Expect:* occupants are not standing next to moving traffic.
5. **Call for help.** Contact emergency services if in a lane or dangerous spot; otherwise call roadside assistance with exact highway, direction, mile marker, exit, or GPS location. → *Expect:* help is dispatched with location details.
6. **Do not attempt exposed repairs.** ⚠️ *Hazard:* changing a tire or inspecting damage beside high-speed traffic can be fatal; wait for protected assistance if exposure is high. → *Expect:* no one is working on the traffic side of the vehicle.
7. **Use warning devices only if safe.** Place reflective triangles/flares according to local rules only when you can do so away from traffic. → *Expect:* extra visibility is added without putting you in the lane.
8. **Verify responders before exiting.** Match the tow or assistance provider to the dispatch details. → *Expect:* you interact only with expected help.

## Decision points

- Vehicle stops in a live lane → call emergency services immediately and stay belted unless there is fire or another immediate threat.
- Smoke, fire, fuel smell, or crash risk → evacuate away from traffic if safe and call emergency services.
- You are near an exit and vehicle can move safely → take the exit rather than stopping on the shoulder.

## Failure modes & recovery

- **F1 No shoulder:** detect barriers or lane blockage → keep hazards on, call emergency services, and do not stand in traffic.
- **F2 Phone has no signal:** detect failed calls → use emergency call if available, flag official help from a protected place, or ask a passenger to seek help only if safe.
- **F3 Other vehicles pass too close:** detect rocking vehicle or near misses → stay belted or move behind a barrier; do not inspect roadside damage.
- **F4 Tow cannot locate you:** detect delay or missed contact → provide direction of travel, nearest exit, mile marker, and live location if possible.

## Verification

The vehicle and occupants are out of active lanes or emergency help is notified, hazard lights are on, exact location is communicated, and roadside/tow assistance is dispatched.

## Variations

- `us`: many states have highway patrol or safety service patrols; dialing emergency services may route help for lane-blocking breakdowns.
- Night breakdown: keep interior lights off if they impair visibility, but use hazards and reflective devices when safe.
- Bad weather: staying inside may be safer than walking on a slick shoulder without a barrier.

## Safety & privacy

High risk from high-speed traffic. Confirm personal safety before leaving the vehicle, never stand between vehicles, and share live location only with emergency contacts or service providers.
