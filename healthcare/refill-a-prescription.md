---
name: refill-a-prescription
domain: healthcare
locale: [generic]
interface: mixed
difficulty: basic
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-20
---

## Goal

An ongoing medication is refilled *before* the current supply runs out, picked up or delivered, and verified to be the right drug at the right dose.

## Preconditions

- An existing prescription for a medication you take regularly, and the label/bottle (it carries the prescription number, pharmacy, prescriber, and refills-remaining count).
- Roughly 5–7 days of supply still left — the whole recipe exists to run *ahead* of the empty bottle.

## Steps

1. **Read the label for the two numbers that decide everything.** Refills remaining, and the prescription's validity/date. [BRANCH: refills > 0 and in-date → pharmacy path (step 2) | refills exhausted or expired → prescriber path (step 3)] → *Expect:* you know which path you're on before contacting anyone.
2. **Pharmacy path: request the refill.** Pharmacy app/website with the Rx number, the phone line's refill option, or in person. State/enter the Rx number and confirm pickup vs delivery. → *Expect:* an acknowledged request with a ready-by time (hours to a day, typically). Skip to step 5.
3. **Prescriber path: request a renewal.** Message the prescriber's practice (portal or phone): medication, dose, pharmacy on file, and a line on how it's going ("stable on this dose"). Many systems let the *pharmacy* initiate this request for you — asking them first can be the faster door. → *Expect:* renewal sent to the pharmacy within the practice's stated turnaround (often 1–3 working days — hence the 5–7 day buffer).
4. **Confirm the renewal landed as a fillable prescription.** Pharmacy notifies, or you check the app after the turnaround. → *Expect:* the pharmacy now shows it fillable; you're on the step-2 path to a ready-by time.
5. **Collect or receive.** Pickup: ID (and payment where applicable) at the counter — some medication classes require signature/ID by law. Delivery: someone present if signature-required. → *Expect:* a labeled bag/bottle handed over or delivered.
6. **Verify before first dose.** ⚠️ *Irreversible:* taking the wrong drug/dose — check the label against your last bottle: drug name, strength, dosing instructions, your name. Generic substitutions change the pill's *look* legitimately — the label, not the color, is the truth; ask the pharmacist to confirm any surprise. → *Expect:* label matches (or the pharmacist explained the substitution); questions about interactions/changes answered at the counter, which is free expertise.
7. **Set the next-refill trigger.** Calendar note at supply-minus-a-week, or enroll in the pharmacy's auto-refill/reminder program for stable long-term meds. → *Expect:* future refills start themselves; this recipe stops requiring memory.

## Decision points

- Controlled/restricted medications → shorter validity, no phone refills in many systems, sometimes monthly prescriber contact required — learn your medication's class once and calendar accordingly; buffers matter double here.
- Cost surprise at the counter (coverage change, deductible) → ask the pharmacist *before* paying: generic options, coverage alternatives, discount programs — they know the workarounds; don't silently skip doses over price (tell the prescriber — cheaper equivalents usually exist).
- Travel coming → request an early/extended fill citing travel; insurers and systems have vacation-supply provisions.

## Failure modes & recovery

- **F1 Ran out before acting (the recipe's target failure):** tell the pharmacist — for many maintenance medications they can give an emergency bridge supply while the renewal processes; urgent-care/telehealth can bridge prescriptions too. Never double-dose to "catch up" after missed days without asking.
- **F2 Renewal request sitting unanswered past turnaround:** call the practice referencing the request date; have the pharmacy re-send it (a second door); persistent gaps → book a med-review appointment (`healthcare/book-a-doctors-appointment`) — some renewals legitimately require one.
- **F3 Pharmacy out of stock:** they can order (days) or transfer the prescription to a nearby branch/competitor with stock — ask for the transfer; shortages of specific drugs are real, and the pharmacist knows the substitution options to raise with your prescriber.
- **F4 Label discrepancy at step 6:** don't take it — back to the counter; dispensing errors are rare but this check is the layer that catches them.

## Verification

The medication in hand matches your regimen (name, strength, instructions, your name on the label), supply runs past the next renewal horizon, refills-remaining is known, and a trigger (calendar or auto-refill) exists so the next cycle starts before the buffer.

## Variations

- `uk`: repeat prescriptions via GP portal/nominated pharmacy, electronic end-to-end; `us`: insurer formularies and 90-day mail-order options change the cost math — worth one ask; `jp`/`cn`: hospital-attached dispensing means the renewal and the appointment are often the same event.
- App-first pharmacies: steps 2–5 collapse into taps and a delivery — step 6's verification survives every automation.

## Safety & privacy

Medium risk, medically real: the buffer (preconditions), the label check (step 6 ⚠️), and never-silently-stopping are the three lines that carry it. Medication details are sensitive — pharmacy counters have queues; the consultation room exists and you can ask for it.
