---
name: guide-someone-by-the-arm
domain: embodied
subdomain: care
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 5min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [person, arm, walkway]
affordances: [ask-consent, offer-arm, walk, warn, pause]
workspace: care-space
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: pause}
---

## Goal

A person is guided through a space by consented arm contact, matched pace, and clear warning of obstacles or changes in terrain.

## Preconditions

- The person wants guidance and can communicate comfort or discomfort.
- The destination or route is known.
- The path can be traveled at a slow pace.
- The actor can walk or move steadily beside the person.

## Steps

1. **Ask for consent.** Ask whether the person wants arm guidance and which side they prefer. → *Expect:* person gives clear consent and side preference.
2. **Describe the route briefly.** Name the destination and any immediate obstacle such as a doorway, ramp, or step. → *Expect:* person knows the first movement segment.
3. **Offer the arm.** Place the actor's forearm or elbow near the person's hand without grabbing them. → *Expect:* person can choose where to hold.
4. **Wait for their hold.** Pause until they take the arm, sleeve, or elbow at their preferred grip pressure. → *Expect:* contact is initiated by the person.
5. **Start slowly.** Move at their pace with half steps until rhythm is matched. → *Expect:* both bodies move together without pulling.
6. **Maintain side-by-side alignment.** Keep the guiding arm relaxed and slightly ahead only enough to signal direction. → *Expect:* person follows without shoulder twist or forced reach.
7. **Warn before obstacles.** Announce turns, narrow spaces, floor changes, ramps, steps, doors, and people before reaching them. → *Expect:* person has time to adjust gait.
8. **Pause on uncertainty.** [BRANCH: obstacle clear | obstacle uncertain] continue if clear; stop and re-scan if crowded, narrow, or unclear. → *Expect:* movement resumes only when path is safe.
9. **End the guide deliberately.** Stop at the destination, state arrival, and wait for them to release or transfer support. → *Expect:* person is stable before contact ends.

## Decision points

- Person declines contact → do not guide by the arm; offer verbal directions or another aid.
- Person grips too tightly or reports pain → stop and offer a different side or method.
- Narrow doorway approaches → guide arm slightly back and pass single-file if they consent.
- Step or curb appears → stop before it and describe up or down before moving.
- Crowded area appears → slow to pause behavior and create space.

## Failure modes & recovery

- **F1 Consent unclear:** detect silence, hesitation, or withdrawal → stop and ask again before contact.
- **F2 Pace mismatch:** detect pulling, lagging, or arm tension → slow down and let the person set pace.
- **F3 Obstacle warning late:** detect abrupt stop or stumble → pause, stabilize, and give earlier warnings after recovery.
- **F4 Grip slips:** detect loss of contact → stop immediately and re-offer the arm.
- **F5 Person becomes unsteady:** detect sway, stumble, or distress → pause, support only as consented, and seek assistance if needed.

## Verification

The person reaches the destination or next stable waypoint, remains balanced, and releases or continues the guide by explicit consent.

## Variations

- `low-vision`: give clock-face or left-right obstacle descriptions before turns and steps.
- `walker-user`: do not take the walker; walk beside and describe path clearance.
- `crowded-hall`: pause more often and let other people pass before proceeding.
- `stairs`: use a stair-specific assistance routine and handrail when available.

## Safety & privacy

Human proximity requires pause behavior and active consent. Never grab, pull, or steer a person by force. Keep route descriptions discreet when they involve medical, mobility, or personal information.
