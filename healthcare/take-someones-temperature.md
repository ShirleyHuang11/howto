---
name: take-someones-temperature
domain: healthcare
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

A temperature is measured with an age-appropriate digital thermometer method and documented with the site used.

## Preconditions

- This is basic measurement guidance, not a substitute for medical care, pediatric advice, or first aid training.
- Call emergency services for fever with trouble breathing, confusion, stiff neck, seizure lasting more than 5 minutes, severe dehydration, or a child left in a hot car.
- Contact a clinician promptly for any infant under 3 months with a rectal temperature of 100.4 F or 38 C or higher.
- Use a digital thermometer, not a glass mercury thermometer.
- Clean the thermometer before and after use, and do not use the same probe for rectal and oral temperatures unless it has disposable covers and is intended for both.

## Steps

1. **Choose the method.** [BRANCH: infant | child or adult] use rectal for infants when appropriate, oral for cooperative older children and adults, temporal or ear when suitable, and armpit when a rough screen is acceptable. → *Expect:* the site matches age and cooperation.
2. **Read device instructions.** Check how to turn on, place, and wait for the thermometer model. → *Expect:* the device is ready and understood.
3. **Clean the probe.** Wipe with alcohol or wash with soap and lukewarm water, then dry. → *Expect:* the probe is clean before contact.
4. **Prepare the person.** Wait after hot or cold drinks for oral readings, and keep the person still. → *Expect:* the reading is less likely to be distorted.
5. **Take an oral reading.** Place the tip under the tongue toward the back, close lips, and wait for the beep. → *Expect:* the display shows a stable oral temperature.
6. **Take a rectal reading when indicated.** Lubricate the tip, insert only about 1/2 to 1 inch for an infant or as directed, hold the thermometer, and wait for the beep. → *Expect:* the display shows a core temperature without letting go of the device.
7. **Take a temporal or ear reading.** Position exactly as the device instructions say, with a clean forehead path or properly placed ear probe. → *Expect:* the sensor has a clear reading path.
8. **Take an armpit reading.** Place the tip high in a dry armpit, hold the arm snugly against the body, and wait for the beep. → *Expect:* the display shows an axillary temperature.
9. **Record the result.** Write the number, F or C, method, time, symptoms, and medicines given. → *Expect:* the reading can be interpreted later.
10. **Decide on care.** Compare the result and symptoms with age-based medical guidance, and call a clinician or emergency services for red flags. → *Expect:* the number is not interpreted without context.

## Decision points

- Infant under 3 months has rectal temperature 100.4 F or 38 C or higher → contact a clinician urgently.
- Adult temperature is 103 F or 39.4 C or higher, or fever has severe symptoms → seek medical care.
- Reading does not match how the person looks → repeat with correct placement or a more reliable method.
- Ear pain, earwax, or poor fit affects ear reading → use another method.
- Person is confused, struggling to breathe, or seizing → call emergency services.

## Failure modes & recovery

- **F1 Site not recorded:** detect a number without oral, rectal, ear, temporal, or armpit label, recover by documenting the method.
- **F2 Oral reading distorted:** detect recent hot or cold drink, recover by waiting and repeating.
- **F3 Unsafe rectal technique:** detect unsupported infant or deep insertion, recover by stopping and using clinician guidance.
- **F4 Dirty thermometer:** detect probe not cleaned after use, recover by cleaning before storage or reuse.

## Verification

The temperature is recorded with units, measurement site, time, symptoms, and escalation decision based on age and red flags.

## Variations

- Infant: rectal readings are often most accurate, but follow clinician advice and device instructions.
- Older child: oral is useful only if the child can keep lips closed and follow directions.
- Shared thermometer: use disposable probe covers when available and clean between users.

## Safety & privacy

Low to medium risk because fever decisions depend on age, symptoms, and method. Call emergency services for severe symptoms, get first aid training, and use this recipe as measurement support rather than professional medical advice.
