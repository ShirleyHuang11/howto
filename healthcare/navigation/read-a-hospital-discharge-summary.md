---
name: read-a-hospital-discharge-summary
domain: healthcare
subdomain: navigation
locale: [generic]
interface: web
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You extract the practical instructions from a discharge summary so you know what happened, what to take, and what follow-up is required.

## Preconditions

- The discharge summary, after-visit summary, medication list, and any printed instructions.
- Access to the patient portal if records are electronic.
- A current medication list from before the hospital stay.

## Steps

1. **Find the main diagnosis and reason for admission.** Look for "discharge diagnosis," "principal diagnosis," or "hospital course." → *Expect:* you can state why you were hospitalized.
2. **Read the medication changes first.** Identify new medications, stopped medications, changed doses, and how long each should be taken. → *Expect:* you have a before-and-after medication list.
3. **Check activity, diet, wound, and device instructions.** Look for restrictions, home oxygen, drains, catheters, braces, or equipment. → *Expect:* daily care instructions are separated from background notes.
4. **List required follow-up.** Capture appointment type, clinic name, timeframe, labs, imaging, therapy, and pending test results. → *Expect:* every follow-up item has an owner and deadline.
5. **Identify warning signs.** Copy symptoms that require calling the doctor, returning to the ER, or calling emergency services. → *Expect:* urgent symptoms are easy to find.
6. **Reconcile confusing terms.** Write down abbreviations or unclear instructions to ask about. → *Expect:* unresolved questions are collected in one list.
7. **Call before changing unclear instructions.** If medication or care instructions conflict, call the discharging unit, primary-care office, pharmacist, or specialist. → *Expect:* a licensed professional clarifies the conflict.
8. **Share with caregivers and clinicians.** Send or bring the summary to your primary-care clinician and anyone helping with care. → *Expect:* the care team has the same discharge information.

## Decision points

- Medication list conflicts with bottles at home → call the pharmacist or discharging clinician before taking the next uncertain dose.
- Follow-up appointment is not scheduled → call the listed clinic and state the discharge timeframe.
- Pending results are listed → ask who will review them and how you will be notified.

## Failure modes & recovery

- **F1 Missing discharge papers:** detect no summary in hand or portal → call hospital medical records or the discharging unit.
- **F2 Conflicting medication instructions:** detect two lists disagree → do not guess; ask a pharmacist or clinician to reconcile.
- **F3 Follow-up missed:** detect no appointment before the recommended deadline → call the clinic and mention recent hospitalization.
- **F4 Red flag ignored:** detect symptoms listed under "return precautions" → call the instructed number, go to the ER, or call emergency services as directed.

## Verification

You have a current medication list, scheduled or requested follow-up appointments, known warning signs, and a list of clarified or pending questions.

## Variations

- `us`: hospitals commonly provide an After Visit Summary and portal access; you can request records through the hospital health information management department.
- Surgery discharge: prioritize wound care, activity limits, infection signs, and drain/device instructions.
- Language access: request translated discharge instructions or interpreter support before leaving when possible.

## Safety & privacy

Medium risk because discharge mistakes can cause medication harm or readmission. Confirm unclear medication changes before acting, store records privately, and escalate warning signs promptly.
