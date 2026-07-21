---
name: give-childrens-medicine-safely
domain: healthcare
locale: [generic]
interface: physical
difficulty: basic
est_time: 15min
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

A child receives the correct medicine dose at the correct time using the proper measuring device, with overdose risks avoided.

## Preconditions

- You have the original medicine package, child-specific label, dosing device, child weight, and a way to record time given.
- The medicine is intended for children and is not expired, damaged, or prescribed to someone else.
- Seek professional or emergency care when there is accidental double dosing, overdose concern, breathing trouble, extreme sleepiness, allergic reaction, or the child is under the minimum age on the label.
- Call a clinician or poison control if dosing is unclear.

## Steps

1. **Read the full label.** Check active ingredient, child age limits, warnings, dose chart, and maximum daily doses. → *Expect:* the medicine is appropriate for the child.
2. **Confirm the child's weight.** Use weight-based dosing when the label or clinician provides it. → *Expect:* the dose matches weight rather than guesswork.
3. **Check for duplicate ingredients.** Compare with other medicines, especially cough, cold, fever, allergy, and pain products. → *Expect:* the same active ingredient is not being doubled.
4. **Use the right device.** Measure liquid medicine with the supplied syringe, dosing cup, or oral dispenser, not a kitchen spoon. → *Expect:* the marked dose can be read accurately.
5. **Measure at eye level.** Draw or pour exactly to the correct line. → *Expect:* the dose line matches the intended amount.
6. **Give the medicine safely.** Have the child upright and give liquid slowly toward the cheek. → *Expect:* the child swallows without choking.
7. **Record the dose.** Write medicine name, amount, time, and who gave it. → *Expect:* another caregiver can see what was given.
8. **Set the next allowed time.** Follow the label or prescription interval exactly. → *Expect:* the next dose is not too soon.
9. **Store it securely.** Close the cap and put medicine out of sight and reach. → *Expect:* the child cannot access it.
10. **Watch for side effects.** Monitor rash, vomiting, unusual sleepiness, agitation, breathing changes, or worsening illness. → *Expect:* concerning reactions trigger care.

## Decision points

- Dose chart conflicts with a clinician's instructions → call the clinician or pharmacist before giving it.
- Child spits out or vomits medicine → ask a clinician or pharmacist before repeating the dose.
- [BRANCH: over-the-counter medicine | prescription medicine] over-the-counter dosing follows the label, while prescription dosing follows the child's prescription.
- ⚠️ *Irreversible:* Do not give an extra dose to make up for uncertainty because overdoses cannot be taken back.

## Failure modes & recovery

- **F1 Kitchen spoon used:** detect unmarked spoon measurement, recover by remeasuring with an oral syringe or dosing cup before giving.
- **F2 Double ingredient:** detect the same active ingredient in two products, recover by stopping and asking a pharmacist.
- **F3 Too-soon dose:** detect interval not yet passed, recover by waiting until the next allowed time.
- **F4 Overdose concern:** detect too much given or uncertain amount, recover by calling poison control or emergency services.

## Verification

The child received only the intended child-appropriate dose, it was recorded with time, and the next safe dosing time is clear.

## Variations

- Infant medicine: get clinician guidance for age and weight before dosing.
- Multiple caregivers: keep one shared log visible.
- School or travel: use the original container and written instructions.

## Safety & privacy

High risk because dosing mistakes can seriously harm children. Seek professional or emergency care when overdose, allergic reaction, breathing symptoms, severe sleepiness, or unclear instructions occur.
