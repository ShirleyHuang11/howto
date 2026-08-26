---
name: coordinate-a-hospital-discharge
domain: healthcare
subdomain: navigation
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 1h-2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You help ensure a hospital discharge has safe transportation, medications, equipment, services, instructions, and follow-up in place.

## Preconditions

- Patient consent or legal authority to coordinate, if you are not the patient.
- Contact information for the nurse, case manager, social worker, pharmacy, and primary clinician.
- Home address, caregiver availability, mobility limits, and insurance information.

## Steps

1. **Ask for the expected discharge date and barriers.** Speak with the nurse or case manager about what must happen before discharge. → *Expect:* discharge timing and unresolved tasks are clear.
2. **Confirm destination and supervision.** Identify whether the patient is going home, to rehab, skilled nursing, assisted living, or another facility. → *Expect:* the receiving place and caregiver plan are documented.
3. **Review medications before leaving.** Ask for a reconciled list showing new, stopped, changed, and continued medications. → *Expect:* there is one current medication plan.
4. **Arrange prescriptions.** Confirm bedside delivery, retail pickup, mail order, or facility pharmacy, and whether prior authorization is pending. → *Expect:* first doses after discharge are available.
5. **Secure equipment and services.** Confirm walker, oxygen, wound supplies, home health, therapy, nursing, or durable medical equipment delivery. → *Expect:* required equipment/services have vendor names and delivery times.
6. **Schedule follow-up.** Book primary-care, specialist, lab, imaging, wound, therapy, or anticoagulation appointments within the discharge timeframe. → *Expect:* appointments or referral requests are listed with dates.
7. **Plan transportation.** Match transport to mobility and medical needs, such as family car, wheelchair van, ambulance, or facility transport. → *Expect:* pickup time and destination are confirmed.
8. **Get teach-back on care tasks.** Have staff demonstrate wound care, injections, drains, oxygen, mobility precautions, diet, or device use. → *Expect:* patient or caregiver can repeat the instructions correctly.
9. **Do not leave with unresolved safety gaps.** ⚠️ *Hazard:* if the patient cannot obtain medications, breathe safely, transfer safely, or has no necessary supervision, ask for case management review before discharge. → *Expect:* major safety gaps are addressed or formally escalated.

## Decision points

- Patient cannot safely go home → ask about rehab, skilled nursing, home health, or delaying discharge until services are arranged.
- Insurance denies equipment or facility placement → ask the case manager about alternatives, appeals, or self-pay estimates.
- Caregiver is unavailable → tell the team before discharge, not after arrival home.

## Failure modes & recovery

- **F1 Medication unavailable:** detect pharmacy out of stock or prior authorization pending → ask hospital team for alternate medication, starter supply, or urgent authorization.
- **F2 Equipment not delivered:** detect oxygen, bed, walker, or supplies missing → call case manager/vendor before transport leaves.
- **F3 Instructions unclear:** detect caregiver cannot perform wound or device care → request another teaching session or home health referral.
- **F4 Follow-up not scheduled:** detect "follow up in 1 week" without appointment → call the clinic before or immediately after discharge.

## Verification

Before departure, the patient has discharge papers, available medications, required equipment or service confirmations, transport arranged, follow-up plan, and warning signs understood by patient or caregiver.

## Variations

- `us`: case managers often coordinate insurance authorization for skilled nursing, rehab, home health, and durable medical equipment.
- Pediatric discharge: confirm weight-based dosing, school/daycare restrictions, and caregiver training.
- No caregiver: ask about social work, home health, community services, or facility placement options.

## Safety & privacy

Medium risk because unsafe discharge can cause falls, medication errors, or readmission. Confirm consent before discussing records, and escalate missing medication, oxygen, mobility, or supervision needs before leaving.
