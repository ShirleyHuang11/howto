---
name: take-a-temperature-correctly
domain: healthcare
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

You take a temperature with the right method for the person, avoid common timing errors, and know when fever needs medical advice.

## Preconditions

- A working thermometer and, if needed, disposable covers.
- The person can safely cooperate with the chosen method.
- For infants under 3 months with a rectal temperature of 100.4 F or 38 C or higher, call a clinician promptly.

## Steps

1. **Choose the method.** [BRANCH: oral | ear | forehead] use oral for cooperative older children and adults, ear with correct fit, or forehead with the device instructions. → *Expect:* the method matches the person and thermometer.
2. **Wait after mouth changes.** For oral readings, wait 15 to 30 minutes after hot or cold drinks, eating, smoking, or chewing gum. → *Expect:* mouth temperature is not distorted.
3. **Clean the thermometer.** Wash or wipe the probe as instructed and add a disposable cover if required. → *Expect:* clean device ready for use.
4. **Take an oral reading.** Place the tip under the tongue, close lips, breathe through the nose, and wait for the beep or required time. → *Expect:* a stable oral temperature displays.
5. **Take an ear reading.** Use the correct probe cover, aim as instructed toward the eardrum, and avoid an ear with pain, drainage, or heavy wax. → *Expect:* a stable ear temperature displays.
6. **Take a forehead reading.** Sweep or hold the sensor exactly as the device directs on dry skin. → *Expect:* a stable forehead temperature displays.
7. **Record method and number.** Write the temperature, time, method, and any fever medicine taken. → *Expect:* the reading can be interpreted later.
8. **Interpret fever.** In many adults, 100.4 F or 38 C or higher is a fever, but method, age, baseline, and symptoms matter. → *Expect:* the number is not interpreted alone.

## Decision points

- Child is very young, medically fragile, unusually sleepy, dehydrated, breathing hard, has stiff neck, seizure, purple rash, or fever lasting several days → seek medical advice.
- Oral reading seems inconsistent → repeat after waiting, or use another method and record the method.
- Ear pain or drainage → avoid ear measurement in that ear and consider medical evaluation.

## Failure modes & recovery

- **F1 Reading is unexpectedly high or low:** repeat once using correct placement and timing.
- **F2 Thermometer has no cover or low battery:** replace supplies before relying on the number.
- **F3 Forehead skin is sweaty:** dry the skin and repeat according to instructions.
- **F4 Symptoms look serious despite modest fever:** seek care based on symptoms, not the number alone.

## Verification

A temperature is recorded with method and time, common timing errors were avoided, and age-specific or symptom-based red flags are escalated.

## Variations

- Rectal temperature: often used for infants when instructed, with a dedicated thermometer and careful technique.
- Basal body temperature: use the same method at the same time daily for trend tracking.
- After fever reducers: record the medication time because it changes interpretation.

## Safety & privacy

Low risk from measurement itself. Seek urgent care for infant fever under 3 months, breathing trouble, stiff neck, seizure, confusion, dehydration, purple rash, or any person who looks seriously ill.
