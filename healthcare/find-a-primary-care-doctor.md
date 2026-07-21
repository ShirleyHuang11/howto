---
name: find-a-primary-care-doctor
domain: healthcare
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Identify a primary care doctor or clinic that fits your insurance, location, care needs, and appointment timeline.

## Preconditions

- Your insurance plan name and member ID, if insured.
- Your address, transportation constraints, preferred language, and schedule limits.
- A list of medical needs that matter for primary care, such as chronic conditions, medications, or preventive care.

## Steps

1. **Define the type of clinician.** [BRANCH: family medicine | internal medicine | pediatrics | nurse practitioner or physician assistant] Choose based on age and care needs. → *Expect:* search is limited to suitable primary care clinicians.
2. **Check the insurance network.** Use the insurer directory and the clinic website, then plan to confirm by phone. → *Expect:* candidate is listed as in network for your specific plan.
3. **Filter for accepting new patients.** Look for online booking, directory status, or call the office. → *Expect:* clinic confirms new patient availability.
4. **Check practical fit.** Compare location, transit, parking, hours, telehealth, language, accessibility, and lab availability. → *Expect:* the office is realistic for repeat visits.
5. **Review credentials and scope.** Confirm board certification or clinic role, hospital affiliation if relevant, and whether they manage your conditions. → *Expect:* clinician can handle your routine care needs.
6. **Call with specific questions.** Ask whether they take your plan, accept new patients, and how soon a new-patient visit is available. → *Expect:* staff gives a clear appointment option or wait time.
7. **Ask about referrals.** If your insurance requires referrals, ask how the office handles specialist referrals and prior authorizations. → *Expect:* you know whether this doctor can coordinate needed care.
8. **Book the first visit.** Schedule a new-patient physical, problem visit, or medication review depending on urgency. → *Expect:* you receive date, time, location, and check-in instructions.
9. **Transfer records.** Request records from prior clinicians and prepare medication list before the visit. → *Expect:* the new office has or expects your history.

## Decision points

- Urgent symptoms → use urgent care, emergency care, or nurse advice line instead of waiting for a new-patient appointment.
- Insurer directory conflicts with clinic → trust the clinic and insurer confirmation over a stale directory listing.
- Long wait but good fit → book it and ask to join the cancellation list.
- Complex condition → ask whether the clinician is comfortable coordinating with your specialists.

## Failure modes & recovery

- **F1 Out-of-network surprise:** detect clinic or insurer cannot confirm coverage, recover by getting plan-specific confirmation before booking.
- **F2 Not accepting patients:** detect no new-patient slots, recover by asking for another clinician in the same practice.
- **F3 Wrong visit type:** detect appointment booked as short follow-up, recover by rescheduling as new-patient or longer visit.
- **F4 Records missing:** detect office lacks history, recover by bringing copies and submitting release forms.

## Verification

You have a booked new-patient appointment with a clinician confirmed as accepting new patients and in network for your specific insurance plan, if applicable.

## Variations

- No insurance: ask clinics about cash prices, sliding-scale programs, community health centers, or membership models.
- Pediatric care: confirm vaccination policy, after-hours advice, and newborn or school forms.
- Language access: request interpreter services when booking, not at arrival.

## Safety & privacy

Medium risk because medical and insurance information is sensitive. Use official clinic or insurer channels, avoid sending medical details through unsecured forms, and seek urgent care for severe symptoms.
