---
name: measure-your-heart-rate
domain: healthcare
locale: [generic]
interface: physical
difficulty: basic
est_time: 3min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

You measure a pulse accurately, identify whether it is resting or active, and know when the number or symptoms need medical care.

## Preconditions

- A clock, timer, or phone stopwatch.
- You are seated or safely standing, not driving or operating equipment.
- If you have chest pain, fainting, severe shortness of breath, or stroke symptoms, skip measurement and call emergency services.

## Steps

1. **Rest before a resting reading.** Sit quietly for 5 minutes if you want a resting heart rate. → *Expect:* breathing and movement settle.
2. **Choose a pulse site.** [BRANCH: wrist | neck] use the wrist below the thumb, or the side of the neck beside the windpipe if the wrist is hard to feel. → *Expect:* a clear rhythmic beat under two fingertips.
3. **Use two fingers.** Place index and middle fingers gently; do not use your thumb because it has its own pulse. → *Expect:* you feel the person's pulse, not your thumb's.
4. **Count for 15 seconds.** Start at zero when the timer begins and count each beat for 15 seconds. → *Expect:* a beat count for the interval.
5. **Multiply by four.** Convert the 15-second count to beats per minute. → *Expect:* a heart-rate number in bpm.
6. **Use a longer count if irregular.** If beats skip or vary, count for 60 seconds instead. → *Expect:* a more accurate number for an irregular rhythm.
7. **Label the context.** Record whether the reading was resting, after walking, during exercise, anxious, feverish, or after caffeine. → *Expect:* the number has useful context.
8. **Compare to typical ranges.** Many adults rest around 60 to 100 bpm, while trained athletes may be lower and active heart rates rise with exertion. → *Expect:* you know whether the reading fits the situation.

## Decision points

- Resting pulse is repeatedly over 100 bpm or under 50 bpm with symptoms → contact a clinician.
- Pulse is irregular, new, or paired with dizziness, chest pain, fainting, or shortness of breath → seek urgent care.
- Measuring during exercise → compare with your personal exercise plan, not the resting range.

## Failure modes & recovery

- **F1 Cannot find the wrist pulse:** move fingers slightly toward the thumb side or try the neck gently.
- **F2 Pressing stops the pulse:** lighten pressure until the beat returns.
- **F3 Count seems inconsistent:** repeat after one minute of rest and count for 60 seconds.
- **F4 Symptoms worsen while measuring:** stop and seek urgent help instead of perfecting the number.

## Verification

A beats-per-minute value is recorded with its context, and any urgent symptoms or repeated abnormal resting readings are escalated appropriately.

## Variations

- Children: normal rates vary strongly by age, so use pediatric guidance rather than adult ranges.
- Wearables: useful for trends, but confirm surprising readings manually.
- Fever or dehydration: heart rate may rise until the underlying issue improves.

## Safety & privacy

Low risk. Call emergency services for chest pain, fainting, severe shortness of breath, stroke symptoms, or a very fast or very slow pulse with weakness, confusion, or dizziness.
