---
name: shelter-during-severe-weather
domain: daily
subdomain: home
locale: [generic]
interface: mixed
difficulty: basic
est_time: 10min
risk: high
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

A household moves to the safest available shelter area during severe weather and monitors official instructions.

## Preconditions

- Severe weather warning, tornado warning, hurricane warning, destructive wind, lightning, hail, flash flood, or official shelter instruction is active.
- Use official local alerts over this general recipe.
- Call emergency services for injury, trapped people, fire, gas leak, downed power line contact, or life-threatening flooding.
- Do not drive or walk through floodwater.
- Keep phones charged and alerts audible when possible.

## Steps

1. **Check the warning type.** Read or listen for tornado, severe thunderstorm, hurricane, flash flood, or other local alert details. → *Expect:* the immediate hazard is identified.
2. **Bring people inside.** Move household members and pets indoors away from windows. → *Expect:* everyone is out of wind, hail, and lightning.
3. **Choose the safest shelter.** [BRANCH: tornado or extreme wind | flood threat] use basement or lowest interior room for wind; move to higher ground for flooding. → *Expect:* shelter matches the hazard.
4. **Avoid windows and exterior walls.** Stay in an interior room, hallway, closet, or bathroom when wind is the threat. → *Expect:* glass and debris exposure is reduced.
5. **Protect heads and bodies.** Use helmets, mattresses, blankets, sturdy shoes, and coats if available. → *Expect:* impact injury risk is reduced.
6. **Keep emergency supplies nearby.** Bring phone, flashlight, weather radio, shoes, medications, and basic kit. → *Expect:* essentials are reachable if damage occurs.
7. **Monitor official updates.** Use weather radio, local alerts, or emergency management messages. → *Expect:* you know when danger continues or changes.
8. **Stay sheltered until all clear.** Do not leave because weather sounds calmer; wait for official all-clear or warning expiration. → *Expect:* second waves or eyewall calm do not catch you exposed.
9. **Avoid post-storm hazards.** Watch for downed lines, gas smell, flooding, unstable trees, and broken glass. → *Expect:* immediate aftermath risks are recognized.
10. **Call for emergency help if needed.** Report injuries, trapped people, fire, gas leaks, or dangerous flooding. → *Expect:* urgent response is requested for life-safety problems.

## Decision points

- Tornado warning → lowest level, smallest interior room, protect head, stay away from windows.
- Flash flood warning → move to higher ground and never enter floodwater.
- Lightning nearby → stay indoors away from corded electronics, plumbing, and open porches.
- Mobile home during tornado warning → go to a designated sturdy shelter if reachable before danger arrives.
- Official evacuation order → evacuate by the instructed route if there is time and it is safe.

## Failure modes & recovery

- **F1 Wrong shelter for flood:** detect moving to basement during rising water → recover by moving to higher floor or roof access if trapped and calling emergency services.
- **F2 Window watching:** detect people near glass → recover by moving them to an interior space.
- **F3 Driving into water:** detect planned travel through flooded roads → recover by turning around and choosing higher ground.
- **F4 All-clear assumed:** detect leaving during a lull → recover by checking official alerts before exiting shelter.

## Verification

Everyone is in the safest available shelter for the active hazard, official alerts are being monitored, emergency supplies are nearby, and emergency services are called for injuries or immediate life threats.

## Variations

- High-rise: use an interior hallway or stairwell area away from windows unless flooding or fire instructions say otherwise.
- Hurricane: prepare before arrival, then shelter away from windows and beware calm during the eye.
- Winter storm: shelter indoors, conserve heat safely, and never run generators or grills indoors.

## Safety & privacy

High risk because severe weather can injure, trap, flood, or expose people to downed utilities. Follow local officials, avoid floodwater and power lines, and share location only with emergency contacts and responders as needed.
