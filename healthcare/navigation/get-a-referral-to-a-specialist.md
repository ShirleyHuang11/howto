---
name: get-a-referral-to-a-specialist
domain: healthcare
subdomain: navigation
locale: [generic, us]
interface: mixed
difficulty: intermediate
est_time: 30min-1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You obtain the referral or order needed to see a specialist and confirm the specialist can schedule you under your insurance or care system rules.

## Preconditions

- Your insurance plan details, primary care provider information, and reason for specialist care.
- Any relevant test results, visit notes, imaging reports, or symptom timeline.
- Access to the patient portal or clinic phone number.

## Steps

1. **Check whether a referral is required.** Review insurance rules, HMO/PPO requirements, and the specialist office's scheduling policy. → *Expect:* you know whether you need a formal referral, prior authorization, or just a recommendation.
2. **Identify the specialty and urgency.** Describe the problem, duration, severity, and any red flags the primary care office should know. → *Expect:* the request points to the right specialty and priority.
3. **Contact the primary care office.** Use the portal, phone, or visit request to ask for a referral and include preferred specialist names if any. → *Expect:* the office opens a referral request or asks for an appointment.
4. **Provide supporting records.** Upload or offer test results, imaging, discharge papers, and prior notes. → *Expect:* the referring clinician has enough information to justify the referral.
5. **Confirm the referral details.** Ask for specialist name, diagnosis/reason, number of visits if applicable, expiration date, and whether insurance authorization is included. → *Expect:* the referral is complete enough for scheduling.
6. **Send records to the specialist.** Confirm fax number, portal transfer, or electronic referral route. → *Expect:* the specialist office can see the referral and records.
7. **Schedule and verify coverage.** Book the appointment and confirm the specialist is in network for your plan. → *Expect:* you have an appointment date and coverage is not just assumed.

## Decision points

- Symptoms are severe or suddenly worsening → seek urgent or emergency care instead of waiting for routine referral processing.
- Insurance requires primary-care referral → do not self-schedule until the referral is accepted.
- Specialist requires records review before scheduling → ask what exact records are missing and who must send them.

## Failure modes & recovery

- **F1 Referral not received:** detect specialist says there is no referral → ask the primary care office to resend and confirm fax or electronic destination.
- **F2 Wrong specialty:** detect specialist declines as inappropriate → ask the referring clinician for a corrected specialty or triage advice.
- **F3 Out-of-network appointment:** detect insurance will not cover the specialist → use the plan directory and call to confirm alternatives.
- **F4 Referral expired:** detect scheduling after the valid window → request renewal before the visit.

## Verification

The specialist office confirms receipt of the referral and required records, the appointment is scheduled, and insurance or clinic rules show the referral is valid for that visit.

## Variations

- `us`: HMO and managed Medicaid plans often require PCP referrals; PPO plans may not, but prior authorization can still apply.
- National health systems: the primary clinician may control referral priority and waiting-list placement.

## Safety & privacy

Medium risk because delays or wrong routing can affect care and costs. Do not send medical records to unverified offices, and escalate urgent symptoms by phone or emergency services rather than portal messaging.
