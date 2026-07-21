---
name: read-a-prescription-label
domain: healthcare
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Read a prescription label well enough to take the right medicine, dose, route, and schedule, and know when to ask a pharmacist for clarification.

## Preconditions

- The prescription container, any pharmacy leaflet, and enough light to read small print.
- Your name and date of birth to confirm the medicine is yours.
- Access to the pharmacy phone number if anything is unclear.

## Steps

1. **Confirm the patient.** Check the name and date of birth or other identifier on the label. → *Expect:* the prescription belongs to the person who will take it.
2. **Read the drug name and strength.** Identify brand or generic name and the amount per tablet, capsule, mL, patch, or inhalation. → *Expect:* you know exactly which medicine and strength you have.
3. **Read the dose.** Find how much to take each time, such as 1 tablet, 5 mL, 2 puffs, or apply thin layer. → *Expect:* dose unit matches the medicine form.
4. **Read frequency and timing.** Identify how often and when, such as once daily, every 8 hours, with food, or at bedtime. → *Expect:* you can place each dose on a daily schedule.
5. **Read the route.** Confirm whether to take by mouth, inhale, inject, apply to skin, place in eye or ear, or use another route. → *Expect:* route is clear and matches the container.
6. **Check warnings and stickers.** Read auxiliary stickers about drowsiness, alcohol, sun exposure, food, driving, shaking, refrigeration, or finishing the course. → *Expect:* special handling or activity limits are known.
7. **Check quantity and refills.** Find how many doses were dispensed, number of refills, and refill expiration date if printed. → *Expect:* you know when to request more.
8. **Check expiration and discard date.** Note the use-by date and any short expiration after mixing or opening. → *Expect:* medicine is current and storage rules are clear.
9. **Ask before guessing.** If any instruction conflicts or is unclear, call the pharmacist or prescriber before taking it. → *Expect:* unclear directions are resolved by a professional.

## Decision points

- Label says `as needed` → identify the symptom, maximum daily amount, and minimum spacing between doses.
- Liquid medicine → use an oral syringe or dosing cup marked in the same units, not a kitchen spoon.
- Multiple medicines look similar → separate them and confirm name and strength before each dose.
- Instruction conflicts with prescriber notes → call the pharmacy or prescriber before changing the dose.

## Failure modes & recovery

- **F1 Wrong patient:** detect name does not match, recover by not taking it and calling the pharmacy.
- **F2 Dose confusion:** detect unclear units or split-tablet instruction, recover by asking the pharmacist to explain and demonstrate if needed.
- **F3 Missed warning:** detect side effects or storage mistake, recover by reading stickers and calling pharmacy for next steps.
- **F4 Refill gap:** detect few doses left and no refill plan, recover by requesting refill several days before running out.

## Verification

You can state the medicine name, strength, dose, frequency, route, key warnings, refill status, and expiration without guessing.

## Variations

- Taper schedule: follow the printed calendar or prescriber instructions exactly and ask for a written schedule if unclear.
- Controlled substance: refills and transfer rules may be stricter.
- Refrigerated medicine: confirm allowed room-temperature time for travel.

## Safety & privacy

Medium risk because medication mistakes can cause harm. Never take a prescription labeled for someone else, and keep labels private because they reveal health information.
