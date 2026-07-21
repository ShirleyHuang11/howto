---
name: give-a-medication-reminder
domain: embodied
subdomain: care
locale: [generic]
interface: physical
difficulty: advanced
est_time: 10min
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [medication-schedule, pill-container, label, water-glass, care-log]
affordances: [speak, read-label, present-item, record-entry]
workspace: home-care
safety: {hot_surfaces: false, sharp_objects: false, fragile: [water-glass], human_proximity: slow}
---

## Goal

At the scheduled time, the person is reminded to take a specific medication, the reminder is matched to the correct labeled dose, the outcome (taken, refused, deferred) is confirmed, and the event is logged for caregivers.

## Preconditions

- An authoritative medication schedule exists (times, drug names, doses) set by a caregiver or clinician.
- Medications are in labeled containers; the robot can read the label text.
- A care log the robot can write to. The robot only prompts and records; it does not choose, alter, or dispense doses.

## Steps

1. **Trigger on the scheduled time, not on convenience.** Prompt within the schedule's window, not early to batch tasks nor late because you were busy. → *Expect:* current time falls inside the prescribed window for this specific dose.
2. **Match the label to the schedule before speaking.** Read the container label and confirm drug name and dose match the schedule entry exactly. ⚠️ *Irreversible:* a wrong drug or dose taken cannot be undone. If the label does not match the schedule, do not prompt for it; flag the caregiver. → *Expect:* label name and dose are an exact match to the schedule line.
3. **Give a clear, specific reminder.** Name the medication and the time, not just "take your pills." Keep it calm and unhurried. → *Expect:* the person acknowledges and understands which medication is due.
4. **Present the aid, not the decision.** Point to or bring the correctly labeled container and a glass of water. Let the person handle and take the dose themselves. → *Expect:* the person has the right container and water in reach.
5. **Confirm the outcome.** Watch or ask to confirm what actually happened. [BRANCH: taken → record time and dose | deferred ("in a minute") → set a short re-prompt and log the deferral | refused → go to refusal handling] → *Expect:* an unambiguous outcome, not an assumption that presenting equals taking.
6. **Handle refusal without pressure.** Do not argue, coax repeatedly, or physically insist. Ask once if they want to wait a few minutes, then record the refusal and notify the caregiver per the plan. → *Expect:* refusal recorded and escalated; the person is not badgered.
7. **Log the event immediately.** Write the drug, dose, scheduled time, actual time, and outcome (taken / deferred / refused) while it is fresh. → *Expect:* a complete, timestamped entry a caregiver can read later.

## Decision points

- Dose window has passed and it was missed → do not double up or improvise timing; log the miss and notify the caregiver, who decides.
- Person says they already took it → do not assume; check the container or the log before deciding, and flag if it cannot be confirmed (double-dose risk).
- Label unreadable or container empty → do not substitute another pill; stop and escalate.

## Failure modes & recovery

- **F1 Wrong medication presented:** label does not match schedule → do not prompt; halt and alert the caregiver before anything is taken.
- **F2 Assumed-taken error:** logged as taken without confirming → treat unconfirmed as not taken; re-confirm and correct the log.
- **F3 Repeated refusal:** person declines across multiple prompts → stop prompting, escalate to the caregiver; do not turn a reminder into coercion.
- **F4 Double-dose risk:** uncertainty about whether an earlier dose was taken → default to not prompting again and flag the caregiver rather than risk a second dose.

## Verification

The care log shows a timestamped entry for the scheduled dose with a confirmed outcome, the medication presented matched the schedule's drug and dose, and any refusal or miss was escalated to the caregiver rather than resolved by the robot.

## Variations

- `pill-organizer`: when a caregiver has pre-sorted a day-of-week organizer, match the compartment to the day and time instead of reading each bottle, but still confirm the compartment is the right one.
- Multiple concurrent medications: prompt and confirm each drug as its own line item and log separately; never merge into one "took the morning meds" entry.

## Safety & privacy

High risk: a wrong drug, wrong dose, or double dose can cause serious harm, so the robot never dispenses or chooses medication and always defers timing changes to a human. Human proximity is slow and calm. Medication data is health information: store the log securely and share only with authorized caregivers.
