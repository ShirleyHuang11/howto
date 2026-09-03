---
name: enroll-a-child-in-school
domain: education
subdomain: k12
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 2h-14d
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-02
---

## Goal

You enroll a child in the correct school or program with required documents, records, and start-date logistics complete.

## Preconditions

- The child's legal name, date of birth, guardian information, and prior school details if any.
- Address or residency information for the school attendance area.
- Access to required documents such as birth certificate, immunization record, proof of residence, and prior transcripts where applicable.

## Steps

1. **Identify the correct school or enrollment office.** Use the district, local authority, or school website to confirm boundaries, grade placement, and registration process. → *Expect:* you know where to apply.
2. **Check age and eligibility rules.** Confirm cutoff dates, kindergarten or grade requirements, language programs, and special program deadlines. → *Expect:* the child is matched to the right grade or program.
3. **Gather required documents.** Collect identity, guardianship, residency, immunization, health, and prior school records. → *Expect:* the application packet is complete or missing items are known.
4. **Submit the enrollment application.** Complete the online form or in-person packet with accurate names, contacts, emergency contacts, and household information. → *Expect:* the school receives the application and gives a receipt or confirmation.
5. **Request records transfer if needed.** Contact the prior school for transcripts, attendance, discipline, special education, 504, or health records. → *Expect:* the receiving school knows where records are coming from.
6. **Confirm health and immunization requirements.** Schedule any required physical, vaccine documentation, or exemptions allowed by local rules. → *Expect:* health clearance is accepted or pending steps are documented.
7. **Arrange services and supports.** Share existing IEP, 504, language-learning, gifted, transportation, meal, medication, or custody documents with the appropriate office. → *Expect:* support teams know the child is enrolling.
8. **Confirm start logistics.** Verify first day, schedule, bus or pickup plan, lunch account, school supplies, device access, and portal login. → *Expect:* the child can attend on the assigned start date.

## Decision points

- Required document is missing → ask the enrollment office for accepted alternatives or provisional enrollment rules.
- Child has an IEP or 504 plan → notify the school before the first day and request a transfer or review meeting.
- Custody or guardianship is complex → provide only official documents requested by the school.

## Failure modes & recovery

- **F1 Wrong school boundary:** detect application returned or delayed → confirm address with the district enrollment office.
- **F2 Incomplete documents:** detect pending status → ask for a written missing-items list and deadlines.
- **F3 Records do not transfer:** detect missing grades or services → request records again and give the receiving school prior contacts.
- **F4 Start-day logistics fail:** detect no bus, schedule, or lunch access → call the school office before the first day.

## Verification

The school confirms enrollment, start date, grade placement, required documents, portal access, transportation or pickup plan, and any needed supports.

## Variations

- `us`: public schools commonly require proof of residence, immunization records, and prior school records; McKinney-Vento rules may protect enrollment for students experiencing homelessness.
- Charter, magnet, or selective programs: application deadlines and lotteries may apply before enrollment.
- International move: ask about transcript translation, grade equivalency, language assessment, and visa or residency documentation.

## Safety & privacy

Medium risk because enrollment uses child identity, health, residency, custody, and education records. Submit documents only through official school channels and keep copies of confirmations.
