---
name: prepare-for-outpatient-surgery
domain: healthcare
subdomain: navigation
locale: [generic, us]
interface: mixed
difficulty: advanced
est_time: 1d-7d
risk: high
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You prepare for same-day surgery so check-in, anesthesia, discharge, medications, and home recovery are organized before the procedure.

## Preconditions

- Surgery date, facility address, surgeon and anesthesia instructions, and insurance authorization status.
- Current medication list, allergies, medical history, and required pre-op testing.
- A responsible adult escort and home support plan.

## Steps

1. **Confirm the procedure and logistics.** Verify surgery name, side/site if applicable, arrival time, facility, surgeon, and expected discharge plan. → *Expect:* the schedule and procedure details match your understanding.
2. **Complete pre-op requirements.** Finish labs, imaging, clearance visits, consent forms, and insurance authorization by the deadline. → *Expect:* the surgery office says you are cleared administratively and medically.
3. **Review medication and fasting instructions.** Ask specifically about blood thinners, diabetes medicines, GLP-1 medicines, supplements, and morning-of-surgery medications. → *Expect:* you have a written medication and fasting plan.
4. **Arrange escort and supervision.** Confirm who will drive you home and stay with you if required after anesthesia. → *Expect:* the escort's name and phone number are ready for the facility.
5. **Prepare the home recovery area.** Stock dressings, ice packs, easy food, prescribed equipment, and a clear path to bathroom and bed. → *Expect:* recovery supplies are in place before surgery day.
6. **Follow pre-op bathing, fasting, and arrival instructions.** ⚠️ *Safety-critical:* confirm the correct surgery, site, allergies, and medication holds before check-in and consent. → *Expect:* the facility can proceed without preventable cancellation.
7. **Review discharge instructions before leaving.** Confirm pain medicines, wound care, activity limits, warning signs, and follow-up appointment. → *Expect:* you and the escort understand home instructions.

## Decision points

- Fever, new infection, chest pain, severe shortness of breath, or major health change before surgery → call the surgical team immediately.
- Escort unavailable → tell the facility; many outpatient surgeries will be canceled without a safe ride.
- Instructions conflict between surgeon and anesthesia team → call for clarification before surgery day.

## Failure modes & recovery

- **F1 Missing authorization:** detect insurance or facility says approval is absent → call the surgeon's office and insurer before proceeding.
- **F2 Fasting violation:** detect you ate or drank after the cutoff → tell anesthesia honestly; they decide whether to delay.
- **F3 Wrong-site concern:** detect consent, bracelet, or staff statement mismatches the planned site → stop and require correction before sedation.
- **F4 No discharge plan:** detect unclear wound care or medication instructions → ask for written clarification before leaving.

## Verification

The surgery office confirms pre-op requirements are complete, you have written fasting and medication instructions, an escort is confirmed, home recovery supplies are ready, and discharge instructions are understood.

## Variations

- `us`: preauthorization, facility fees, anesthesiology billing, and pathology billing may come from separate entities.
- Local anesthesia only: escort rules may be lighter, but confirm with the facility rather than assuming.

## Safety & privacy

High risk because surgery, anesthesia, and medication holds can cause serious harm if mishandled. Confirm identity, procedure, site, allergies, and consent before sedation, and escalate urgent symptoms by phone or emergency care.
