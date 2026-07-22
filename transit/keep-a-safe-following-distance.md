---
name: keep-a-safe-following-distance
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

Maintain enough following distance to stop or react safely as speed, weather, visibility, and vehicle size change.

## Preconditions

- You are driving a vehicle with working brakes, tires, mirrors, and lights.
- You are on a road where you can see the vehicle ahead and adjust speed.
- You are sober, alert, and not using a handheld device.

## Steps

1. **Pick a fixed marker.** Choose a sign, shadow, bridge, lane stripe, or crack that the vehicle ahead will pass. → *Expect:* the marker is stationary and easy to count from.
2. **Count when the vehicle ahead passes it.** Say "one thousand one, one thousand two, one thousand three" until your front bumper reaches the marker. → *Expect:* the count gives your following gap.
3. **Keep at least three seconds in good conditions.** Ease off the accelerator until you have a full three-second gap. → *Expect:* you are not closing on the vehicle ahead during normal flow.
4. **Add time for bad conditions.** Use four to six seconds or more in rain, darkness, glare, fog, snow, gravel, heavy traffic, or when tired. → *Expect:* stopping room grows with risk.
5. **Add time behind big vehicles.** Stay farther back from trucks, buses, trailers, motorcycles, and vehicles carrying loads. → *Expect:* you can see around hazards and avoid debris or sudden stops.
6. **Protect your escape space.** Avoid driving boxed in beside another vehicle when possible, and keep a lane or shoulder option visible. → *Expect:* you have somewhere to go if braking alone is not enough.
7. **Respond to tailgaters calmly.** [BRANCH: maintain speed | change lanes | pull over] keep steady speed, move right when safe, or let them pass; do not brake-check. → *Expect:* pressure behind you decreases without creating a new hazard.
8. **Reset after every merge.** When someone cuts into your gap, lift off and rebuild the space instead of defending it. → *Expect:* the three-second buffer returns.
9. **Brake early and smoothly.** Signal slowing with brake lights before hard braking is needed. → *Expect:* drivers behind have more warning and the vehicle stays stable.

## Decision points

- Speeds rise → distance in feet must grow even if the time gap stays three seconds.
- Visibility drops → double the gap and consider slowing below the speed limit.
- Following a motorcycle → increase space because motorcycles can stop quickly and riders are vulnerable.
- Tailgater stays aggressive → change lanes or exit when safe rather than engaging.

## Failure modes & recovery

- **F1 Gap too short:** you reach the marker before three seconds → ease off until the count reaches three.
- **F2 Repeated cut-ins:** traffic fills every gap → keep rebuilding space and avoid sudden acceleration.
- **F3 Panic braking ahead:** brake firmly, steer straight if possible, and use escape space only when clear.
- **F4 Tailgater pressure:** you feel pushed to speed → maintain legal speed and let them pass at the first safe opportunity.
- **F5 Big vehicle blocks view:** you cannot see traffic ahead → increase distance or change lanes safely.

## Verification

You maintain at least a three-second following gap in good conditions and a longer gap whenever weather, visibility, load, fatigue, or vehicle type increases stopping risk.

## Variations

- Heavy vehicles or towing: use much longer gaps because stopping distance increases.
- Wet roads: begin with at least four seconds and add more if tires or visibility are poor.
- Night driving: add distance because hazard recognition takes longer.
- Stop-and-go traffic: keep enough space to see the rear tires of the vehicle ahead touching the road.

## Safety & privacy

High risk because following too closely causes rear-end crashes. Do not use the phone, do not retaliate against tailgaters, and treat extra space as active crash prevention rather than lost progress.
