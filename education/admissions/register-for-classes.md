---
name: register-for-classes
domain: education
subdomain: admissions
locale: [generic]
interface: web
difficulty: intermediate
est_time: 30min-3d
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-02
---

## Goal

You build a workable class schedule that satisfies requirements, avoids conflicts, and is officially registered in the school's system.

## Preconditions

- You have student portal access and registration date or time ticket.
- Holds, advising requirements, placement tests, and prerequisites are resolved or understood.
- You know degree, major, general education, and full-time or part-time credit requirements.

## Steps

1. **Review degree requirements.** Check major, general education, prerequisites, sequencing, and minimum credit load for aid or visa status. → *Expect:* a list of courses or categories you need this term.
2. **Check holds and advising.** Clear immunization, financial, transcript, advising, or placement holds before registration opens. → *Expect:* the portal says you are eligible to register.
3. **Build a primary schedule and backups.** Balance required courses, workload, commute, labs, and time zones for online classes. → *Expect:* you have first-choice sections plus alternatives.
4. **Validate prerequisites and restrictions.** Check major-only seats, permission numbers, co-requisites, waitlists, and repeat rules. → *Expect:* each selected class is actually available to you.
5. **Register at your assigned time.** Add courses through the official system and submit the transaction. → *Expect:* the portal shows enrolled, waitlisted, or error status for each course.
6. **Fix errors immediately.** [BRANCH: enrolled | waitlisted | blocked] Keep enrolled classes, join strategic waitlists, or contact the department/advisor for permission. → *Expect:* every problem has a next action.
7. **Confirm total credits and schedule.** Check meeting times, rooms, online modality, exam times, and tuition implications. → *Expect:* your schedule is coherent and meets credit requirements.
8. **Save proof and calendar the add/drop deadline.** Download or screenshot the schedule and note deadlines for changes. → *Expect:* you can prove enrollment and know when changes become costly.

## Decision points

- Required course is full -> join the waitlist and register for a backup that still advances requirements.
- Schedule overloads difficult classes -> trade one course for a requirement with lower workload if degree timing allows.
- Aid or visa requires full-time enrollment -> confirm credit minimum before dropping below it.

## Failure modes & recovery

- **F1 Registration hold:** detect blocked enrollment -> contact the office that placed the hold and resolve documentation or payment.
- **F2 Prerequisite error:** detect a system block despite completed work -> ask the department or advisor for override with transcript proof.
- **F3 Waitlist stall:** detect no movement near add/drop -> attend if allowed, email instructor appropriately, and keep a registered backup.
- **F4 Time conflict:** detect overlapping lecture, lab, commute, or exam time -> swap sections before the deadline.

## Verification

The student portal shows enrolled status for the intended credits, no unresolved registration errors, and the schedule meets degree, aid, and personal constraints.

## Variations

- Online asynchronous courses: check hidden requirements such as proctored exams, live sessions, or group project times.
- Cohort programs: an advisor or department may register students automatically; verify instead of duplicating registration.

## Safety & privacy

Low risk, but enrollment can affect tuition, aid, immigration, and graduation timing. Confirm deadlines before dropping classes and avoid sharing student portal credentials.
