---
name: request-a-prescription-refill-online
domain: healthcare
subdomain: navigation
locale: [generic, us]
interface: web
difficulty: basic
est_time: 15min
risk: medium
prerequisites: [healthcare/navigation/set-up-a-patient-portal-account]
status: draft
last_verified: 2026-08-25
---

## Goal

You request a medication refill through the pharmacy or patient portal and confirm it is processing before you run out.

## Preconditions

- The medication name, dose, prescribing clinician, and current pharmacy.
- Enough medication remaining for normal processing time; urgent needs may require a call.
- Portal or pharmacy account access.

## Steps

1. **Check the prescription label.** Confirm remaining refills, expiration date, prescribing clinician, and pharmacy phone number. → *Expect:* you know whether this is a refill or a renewal request.
2. **Sign in to the correct portal.** Use the pharmacy website/app for refills remaining or the patient portal for no-refill renewal requests. → *Expect:* the medication appears in your account.
3. **Select the exact medication.** Match name, strength, form, and dosing schedule; avoid selecting an old duplicate. → *Expect:* the correct prescription is selected.
4. **Confirm pickup or delivery details.** Choose pharmacy location, shipping address, and timing. → *Expect:* the portal shows the right destination and estimated availability.
5. **Submit the refill or renewal request.** ⚠️ *Confirm first:* medication, dose, patient, and pharmacy are correct before submitting. → *Expect:* a confirmation number, status, or message appears.
6. **Track status until accepted.** Look for "in process," "ready," "provider review," or "needs authorization." → *Expect:* you know whether action is still needed.
7. **Follow up before the gap becomes unsafe.** If it stalls, call the pharmacy or prescriber with the prescription details. → *Expect:* a staff member explains the blocker or next step.

## Decision points

- Label shows zero refills or prescription expired → request renewal from the prescriber, not only the pharmacy.
- Controlled substance or specialty medication → expect stricter timing, identity checks, or required visits.
- Medication is urgent or running out today → call the pharmacy and prescriber rather than relying only on a portal message.

## Failure modes & recovery

- **F1 Refill too soon:** detect an insurance or pharmacy rejection → ask the pharmacy for the next eligible fill date or vacation override options.
- **F2 Prior authorization required:** detect "insurance approval needed" → ask the prescriber's office to submit or renew the authorization.
- **F3 Out of stock:** detect delayed availability → ask the pharmacy to check nearby locations or contact the prescriber for an alternative.
- **F4 Wrong medication selected:** detect a mismatch after submission → call the pharmacy immediately to cancel or correct before dispensing.

## Verification

The portal or pharmacy account shows the correct medication as processing or ready, with the right patient, dose, quantity, pharmacy, and pickup or delivery plan.

## Variations

- `us`: insurance may require mail order, specialty pharmacy, step therapy, or prior authorization for some medications.
- Auto-refill: useful for stable maintenance medicines, but still review each fill for dose changes.

## Safety & privacy

Medium risk because medication errors can harm health. Confirm patient, drug, dose, and pharmacy before submission, and contact a clinician or pharmacist for medical questions or side effects.
