---
name: drive-safely-in-snow-and-ice
domain: transit
subdomain: vehicle
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 30min
risk: high
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You drive only when necessary in snow or ice, using slower speeds, larger gaps, and gentle controls to maintain traction.

## Preconditions

- Tires have adequate tread and are appropriate for winter conditions.
- Windows, roof, lights, mirrors, and license plates are cleared.
- You have enough fuel or battery charge, warm clothing, and a charged phone.

## Steps

1. **Decide if driving is necessary.** Check road conditions, closures, and weather alerts. → *Expect:* you know whether to delay, reroute, or proceed.
2. **Prepare the vehicle completely.** Clear snow and ice from glass, roof, hood, lights, mirrors, sensors, and plates. → *Expect:* visibility and vehicle lighting are unobstructed.
3. **Start gently.** Accelerate slowly to avoid wheel spin. → *Expect:* the vehicle moves without slipping.
4. **Increase following distance dramatically.** Leave 8-10 seconds or more on snow and ice. → *Expect:* you can stop without abrupt braking.
5. **Brake early and smoothly.** Use steady pressure with ABS; do not pump ABS brakes. → *Expect:* the vehicle slows while remaining steerable.
6. **Steer and accelerate one task at a time.** Avoid braking hard while turning. → *Expect:* tires are not asked for more grip than they have.
7. **Handle a skid correctly.** Look and steer where you want to go, ease off pedals, and avoid overcorrection. → *Expect:* the vehicle gradually realigns.
8. **Avoid cruise control.** Keep direct control of throttle on slippery roads. → *Expect:* speed responds to traction changes.
9. **Stop if conditions exceed control.** Pull into a safe lot or exit, not the travel lane. → *Expect:* you wait out conditions rather than continuing unsafely.

## Decision points

- Freezing rain or black ice is reported → delay travel unless truly essential.
- Vehicle cannot climb a hill without spinning → back down only if safe, reroute, or wait for treatment.
- Snowplow approaches → give it space and avoid passing unless clearly safe and legal.

## Failure modes & recovery

- **F1 Wheels spin from a stop:** ease off, straighten wheels, use gentle throttle, and try a higher gear or traction mode if available.
- **F2 ABS vibrates under braking:** keep steady pressure and steer; the pulsing is normal.
- **F3 Car slides through a turn:** ease off pedals and steer toward the intended path; do not yank the wheel.
- **F4 Stuck in snow:** clear around tires, use traction material, rock gently only if manual permits, and stop before overheating the transmission.

## Verification

The trip is completed or postponed without uncontrolled skids, blocked visibility, or driving faster than traction allows.

## Variations

- `awd-4wd`: helps acceleration but does not shorten stopping distance on ice.
- `winter-tires`: improves grip but still requires slower speed and longer following distance.
- `ev-hybrid`: use low regenerative braking settings if strong regen causes sliding.

## Safety & privacy

High risk because snow and ice can remove steering and braking control. Delay nonessential trips, clear the whole vehicle, and use very gentle inputs with large following distances.
