---
name: respond-to-a-fall
domain: embodied
subdomain: care
locale: [generic]
interface: physical
difficulty: advanced
est_time: 20min
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [person, floor, phone, blanket, care-log]
affordances: [observe, speak, call-emergency, place-item, record-entry]
workspace: home-care
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: pause}
---

## Goal

After a person falls, they are assessed before any movement, emergency help is called when thresholds are met, they are kept calm and comfortable, and the event is documented, without the robot lifting them prematurely.

## Preconditions

- The robot witnessed or discovered a person on the floor after a fall.
- A means to call emergency services and to reach the designated caregiver.
- The robot does not attempt to lift or drag the person as its default action.

## Steps

1. **Stop and do not lift immediately.** ⚠️ *Irreversible:* moving someone with a fracture, spinal injury, or head trauma can cause permanent harm. Do not haul them up because it seems helpful. → *Expect:* the person stays where they landed until assessed.
2. **Check responsiveness and breathing.** Speak to them, ask if they can hear you, look for breathing and any obvious severe bleeding or deformity. → *Expect:* a clear read on whether they are conscious and breathing normally.
3. **Call emergency services at the hard thresholds.** [BRANCH: unconscious, not breathing normally, seizing, severe bleeding, a visibly deformed or painful hip/leg, hit their head, on blood thinners, or cannot get up → call emergency services now, then the caregiver | alert and uninjured and says they are fine → go to the assisted-recovery branch] → *Expect:* for any threshold hit, emergency services are contacted before any attempt to move them.
4. **Keep them still and talk to them.** Ask them not to rush to get up. Tell them help is coming if you called. Keep your presence calm and steady. → *Expect:* the person stays calm and does not scramble to stand on a possibly injured limb.
5. **Ask what hurts before any recovery.** Have them slowly check whether they can move fingers, arms, and legs and where the pain is, without forcing anything. → *Expect:* a clear picture of pain and mobility that confirms whether self-recovery is safe.
6. **Assist recovery only if clearly uninjured.** If they are alert, pain-free, and want to get up, let them do the work in stages (roll to side, to hands and knees, up to a sturdy chair) while you steady the chair and spot them. Do not pull them up by the arms. → *Expect:* the person rises under their own power in stages; the robot stabilizes furniture, never bears their weight up.
7. **Comfort and monitor after.** Provide a blanket for shock or cold, stay with them, and watch for delayed symptoms (dizziness, confusion, worsening pain). → *Expect:* the person is warm, seated or resting, and observed for a change.
8. **Document the fall.** Log the time, what was seen, injuries reported, whether emergency services or the caregiver were called, and the outcome. → *Expect:* a complete timestamped entry and the caregiver notified regardless of severity.

## Decision points

- They insist they are fine but hit their head or are on blood thinners → still escalate; delayed bleeds are the danger, and this overrides their reassurance.
- They cannot get up after several minutes though seemingly uninjured → do not keep trying to lift; call for help to avoid a long lie on the floor.
- You are unsure whether it is safe to move them → default to not moving and to calling for guidance.

## Failure modes & recovery

- **F1 Premature lift:** pulled them up before assessing → stop; if injury is now suspected, keep them still and call emergency services.
- **F2 Under-triage:** treated a head or hip injury as minor → re-apply the call thresholds and escalate even if late.
- **F3 Long lie:** person left on the floor while deciding → a prolonged lie is itself dangerous; call for help promptly rather than deliberating.
- **F4 Missed delayed symptom:** new confusion or dizziness after recovery → treat as an emergency and call, do not wait to see if it passes.

## Verification

The person was assessed before any movement, emergency services were called whenever a threshold was met, no premature lift occurred, the person is comfortable and monitored, and a timestamped log entry with caregiver notification exists.

## Variations

- `facility`: many facilities require any fall to be reported and a nurse assessment before the resident is moved at all; follow the local no-lift policy.
- Solo robot without call access: the first action becomes summoning a human by the fastest available channel before anything else.

## Safety & privacy

High risk: premature movement and under-triage are the two ways this goes badly, so the defaults are do not lift and escalate on any threshold. Human proximity is pause: hold position and assess rather than acting on the body. The fall record is sensitive health data; share only with the authorized care team and emergency responders.
