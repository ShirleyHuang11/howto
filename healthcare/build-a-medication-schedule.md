---
name: build-a-medication-schedule
domain: healthcare
locale: [generic]
interface: mixed
difficulty: basic
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Create a clear medication schedule that shows what to take, when to take it, how to remember it, and when to refill it.

## Preconditions

- Current prescription bottles, over-the-counter medicines, supplements, and written instructions are available.
- A phone, paper chart, pill organizer, or other reminder tool is available.
- The person using the schedule can read the labels or has a helper who can confirm them.

## Steps

1. **Gather every medicine.** Put prescriptions, over-the-counter medicines, vitamins, supplements, eye drops, inhalers, and as-needed medicines in one place. → *Expect:* nothing currently taken is left out of view.
2. **Copy the label details.** For each item, write the name, strength, dose, route, timing instructions, prescribing clinician, and reason if known. → *Expect:* each medicine has a matching line in the schedule.
3. **Mark special instructions.** Note food rules, empty-stomach rules, bedtime rules, missed-dose instructions, and medicines that should not be crushed. → *Expect:* timing constraints are visible next to the medicine name.
4. **Choose daily time blocks.** [BRANCH: simple routine | complex routine] Use morning, midday, evening, and bedtime for simple plans; use exact clock times for complex plans. → *Expect:* every dose appears in one time block.
5. **Check for conflicts.** Compare labels for duplicate ingredients, spacing rules, and warning stickers; ask a pharmacist or doctor to check interactions before using a new combined schedule. → *Expect:* unclear combinations are flagged for professional review.
6. **Set up a pill organizer.** Fill only the medicines that are safe to pre-sort, keeping liquids, inhalers, refrigerated medicines, and original-package items separate. → *Expect:* compartments match the written schedule.
7. **Add reminders.** Set phone alarms, calendar alerts, smart speaker reminders, or a paper checklist for each dose time. → *Expect:* each scheduled dose has a reminder or visible check box.
8. **Add refill dates.** Count remaining doses and set refill reminders several days before running out, earlier for mail-order or controlled medicines. → *Expect:* each ongoing medicine has a refill-ahead date.
9. **Confirm with the user.** Read the schedule aloud and compare it against the bottles before the first use. ⚠️ *Irreversible:* taking the wrong dose can cause harm; confirm medicine, dose, and time before swallowing. → *Expect:* the user or helper agrees the schedule matches the labels.

## Decision points

- A label conflicts with a doctor's verbal instruction → call the doctor or pharmacist before following the schedule.
- A medicine is taken only as needed → keep it in a separate as-needed section with maximum daily dose.
- The user has memory, vision, or dexterity limits → use larger print, caregiver checks, blister packs, or pharmacy packaging.

## Failure modes & recovery

- **F1 Missing medicine:** detect an empty schedule line or bottle not listed → add it before filling the organizer.
- **F2 Interaction concern:** detect duplicate active ingredients, warning stickers, or new side effects → pause the change and ask a pharmacist or doctor.
- **F3 Missed dose:** detect an unchecked dose or full compartment after the scheduled time → follow the label's missed-dose instructions or call the pharmacist.
- **F4 Refill gap:** detect fewer doses than days until refill → request the refill now and ask the pharmacy about a short supply if needed.

## Verification

Every current medicine appears once with dose, time, special instructions, reminder method, and refill date, and a pharmacist or doctor has been asked about any interaction concern.

## Variations

- Pharmacy blister packs: ask the pharmacy to package doses by date and time, then keep the written schedule as the master copy.
- Shared caregiving: place one current schedule where caregivers can mark doses without duplicating instructions.
- Travel: carry medicines in original containers plus a printed schedule.

## Safety & privacy

Medication names and diagnoses are private health information. Medium risk comes from missed doses, double doses, and interactions; confirm uncertain instructions with a pharmacist or doctor.
