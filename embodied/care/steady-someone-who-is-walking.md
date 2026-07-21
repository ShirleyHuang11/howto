---
name: steady-someone-who-is-walking
domain: embodied
subdomain: care
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 5min
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [person, walking-path, cane, walker, chair]
affordances: [ask, approach, offer-arm, match-pace, observe-footing, pause]
workspace: care
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: pause}
---

## Goal

A walking person receives consensual, side-by-side steadying support while maintaining their own balance and direction.

## Preconditions

- The person is awake, responsive, and able to state or show whether help is wanted.
- The walking path has enough room for two people or a mobility aid.
- A chair, wall, rail, or other stopping point is nearby if balance worsens.
- Emergency help is available if the person falls, has chest pain, faints, or cannot bear weight.

## Steps

1. **Ask before touching.** Say what support you can offer and wait for consent. → *Expect:* the person agrees, declines, or requests a specific kind of help.
2. **Move to the support side.** Stand slightly behind and to the side the person chooses, leaving their feet and aid clear. → *Expect:* you can see their footing without blocking the path.
3. **Offer an arm or forearm.** Present your forearm for them to hold instead of grabbing their hand or shoulder. → *Expect:* the person controls the contact and grip pressure.
4. **Start at their pace.** Take small steps that match their cadence and stride length. → *Expect:* neither person is pulling the other forward.
5. **Watch the walking surface.** Scan for rugs, cords, wet spots, thresholds, and uneven flooring. → *Expect:* hazards are seen before the person reaches them.
6. **Pause for instability.** [BRANCH: steady | unsteady] continue if gait is stable, or stop and guide toward a chair or rail if it is not. → *Expect:* support changes before balance is lost.
7. **Turn slowly.** For corners or direction changes, cue the turn and move in a wide arc. → *Expect:* feet turn without crossing or tangling.
8. **Release only when stable.** Stop at the destination and confirm they are seated or standing securely before letting go. → *Expect:* the person is supported by the chair, rail, walker, or their own stance.

## Decision points

- Person declines help -> keep space, remove hazards if appropriate, and ask whether they want you nearby.
- Person uses a walker or cane -> do not move the aid for them unless asked or trained.
- Person becomes dizzy, weak, confused, or short of breath -> stop walking and seek medical help.
- Path narrows -> pause and pass one at a time, or choose another route.

## Failure modes & recovery

- **F1 No consent:** the person pulls away or says no, step back and switch to verbal support.
- **F2 Pulling imbalance:** your pace moves ahead of theirs, slow down and return to side-by-side position.
- **F3 Footing hazard:** shoe, cane, or foot catches on an object, stop and clear the hazard before continuing.
- **F4 Near fall:** knees buckle or body drops, do not yank upward; help them lower safely and call for assistance.

## Verification

The person reaches the destination without a fall, with consent maintained and stable support present until seated or balanced.

## Variations

- `walker`: walk beside and slightly behind, keeping hands off the walker unless asked.
- `stairs`: use trained stair-assist technique or choose an elevator or ramp.
- `clinical-setting`: follow the care plan, gait belt procedure, and fall-response protocol.

## Safety & privacy

High risk because falls can cause serious injury. Touch requires consent, human proximity requires pausing when uncertain, and medical symptoms require escalation rather than continued walking.
