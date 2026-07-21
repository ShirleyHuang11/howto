---
name: take-blood-pressure-at-home
domain: healthcare
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

A home blood pressure reading is taken under consistent resting conditions, logged accurately, and escalated when readings are concerning.

## Preconditions

- Validated upper-arm blood pressure monitor, correct cuff size, chair, table, and log.
- No caffeine, nicotine, exercise, or large meal in the previous 30 minutes if possible.
- A plan for whom to contact about unusually high or low readings.

## Steps

1. **Prepare the setting.** Sit in a quiet place with the monitor on a table. → *Expect:* the cuff hose can reach the arm without pulling.
2. **Rest first.** Sit quietly for 5 minutes before measuring. → *Expect:* breathing and heart rate feel settled.
3. **Set posture.** Keep back supported, feet flat, legs uncrossed, and arm supported at heart level. → *Expect:* the body feels relaxed and symmetrical.
4. **Place the cuff.** Wrap the cuff on bare upper arm, with the artery mark over the inner arm and lower edge about 2 cm above the elbow. → *Expect:* the cuff is snug enough for two fingertips under the edge.
5. **Stay still and silent.** Press start and do not talk, text, or move during inflation. → *Expect:* the cuff inflates, pauses, and deflates automatically.
6. **Read the numbers.** Note systolic, diastolic, pulse, arm used, date, time, and any symptoms. → *Expect:* the log has a complete entry.
7. **Repeat correctly.** Wait 1 minute and take a second reading. → *Expect:* two readings are available under the same conditions.
8. **Average routine readings.** If tracking for a clinician, average the two readings unless instructed otherwise. → *Expect:* the recorded value reflects repeated measurement, not a single spike.
9. **Respond to concerning values.** [BRANCH: very high with symptoms | very high without symptoms | unusually low with symptoms] follow your clinician's plan or urgent guidance. → *Expect:* abnormal readings are not ignored.
10. **Store the device.** Remove cuff, power off, and keep the log accessible for appointments. → *Expect:* readings can be reviewed later with context.

## Decision points

- Reading is 180 systolic or higher, or 120 diastolic or higher, with chest pain, shortness of breath, weakness, confusion, or vision changes → seek emergency care.
- Reading is very high without symptoms → rest 5 minutes, repeat, and contact a clinician promptly if it remains high.
- Cuff does not fit the arm range printed on it → use the correct cuff before trusting the number.

## Failure modes & recovery

- **F1 Cuff over clothing:** detect sleeve under cuff; remove clothing from the upper arm and repeat.
- **F2 Arm below heart:** detect arm hanging or unsupported; support it on a table and repeat after rest.
- **F3 Talking or movement:** detect interrupted inflation or odd result; wait 1 minute and measure again silently.
- **F4 Irregular rhythm alert:** detect monitor warning symbol; repeat once and share the alert with a clinician.

## Verification

Two seated, rested readings are logged with date, time, arm, systolic, diastolic, pulse, and symptom context.

## Variations

- Morning and evening log: measure before medication or meals only if your clinician asked for that pattern.
- Wrist monitor: keep wrist exactly at heart level and understand it is more position-sensitive.
- Caregiver measurement: explain each cuff inflation before starting and stop if the person feels faint.

## Safety & privacy

Medium risk because readings can affect medical decisions. Do not change prescribed medication based only on one home reading unless a clinician has given that instruction.
