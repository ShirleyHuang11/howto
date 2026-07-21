---
name: keep-a-daily-care-log
domain: embodied
subdomain: care
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [care-log, clock, meals, medication-schedule, mobility-aid]
affordances: [observe, record-entry, timestamp, flag-alert]
workspace: home-care
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

A running log of a person's day (meals, fluids, medications, activity, mood, and notable events) is kept in objective, timestamped language, with defined thresholds flagged for the caregiver and a clean handoff at shift change.

## Preconditions

- A care log the robot can write to, shared with the human care team.
- A known baseline for this person (usual routine, normal intake, known conditions) provided by caregivers.
- Agreed flag thresholds from the care plan (what counts as too little food, too few fluids, a fall, a skipped med).

## Steps

1. **Record on the event, not from memory.** Enter each item as it happens with a timestamp, rather than reconstructing the day at the end. → *Expect:* entries carry the actual clock time they occurred.
2. **Log the core categories.** Capture meals and how much was eaten, fluids, medications (taken/refused/missed), toileting if in the plan, activity and mobility, sleep, and mood or behavior changes. → *Expect:* each category has entries or an explicit "none observed" for the period.
3. **Write objectively, describe don't diagnose.** Record what you observed: "ate about half the lunch, left the vegetables," not "poor appetite"; "walked to the kitchen with the walker, steady," not "doing well." → *Expect:* entries a different caregiver could verify from the same observation.
4. **Note deviations from baseline.** When something differs from this person's normal (ate much less, more confused, did not get up), record the observation and the baseline it differs from. → *Expect:* the deviation is explicit, not buried in routine notes.
5. **Flag at the plan's thresholds.** [BRANCH: within normal range → log only | crosses a threshold (skipped meal, low fluids, a fall, refused medication, new confusion) → log and raise a caregiver alert] → *Expect:* every threshold crossing produces both a log entry and an alert, not just a note.
6. **Keep opinions and identity separate.** Record behavior and facts, not judgments about the person; do not speculate about causes you cannot observe. → *Expect:* no diagnostic or evaluative language in the factual log.
7. **Hand off at shift change.** Summarize the period for the incoming caregiver: what happened, any open flags, anything to watch. Confirm the summary is received. → *Expect:* the next caregiver acknowledges the flags and open items; nothing time-sensitive is lost in the gap.

## Decision points

- Unsure whether something meets a threshold → log it and flag anyway; a false flag costs less than a missed one.
- Person asks the robot not to log something embarrassing → still record objectively per the care plan, but note the request; do not omit safety-relevant facts.
- Conflicting observations between the robot and a caregiver → record both without overwriting; the human team reconciles.

## Failure modes & recovery

- **F1 End-of-day batching:** entries written from memory hours later → times and details drift; switch to logging at the moment of the event.
- **F2 Subjective language:** "seemed fine / seemed off" → not verifiable; rewrite as the concrete observation behind the impression.
- **F3 Missed flag:** a threshold crossed but only logged, not alerted → audit thresholds against the plan and raise the alert late rather than not at all.
- **F4 Lost handoff:** shift changed with an open flag unacknowledged → escalate directly to the caregiver until confirmed received.

## Verification

The log for the period contains timestamped, objective entries across the core categories, every care-plan threshold crossing has a matching caregiver alert, and the shift-change handoff was acknowledged with all open flags carried forward.

## Variations

- `facility`: institutional logs may require a fixed form and specific vital-sign fields on a schedule; follow the facility template while keeping the objective-language rule.
- Dementia care: emphasize behavior, orientation, and mood-change entries, since these deviations are the earliest signals for the care team.

## Safety & privacy

Medium risk: the harm here is an omitted or misrecorded observation that delays care, so accuracy and threshold flagging matter more than brevity. Human proximity is continue. The log is sensitive health and personal information: store it securely and share only with the authorized care team.
