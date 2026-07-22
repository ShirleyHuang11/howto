---
name: use-a-pulse-oximeter
domain: healthcare
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

You obtain a more reliable pulse oximeter reading, understand SpO2 and pulse, and know when low oxygen needs urgent care.

## Preconditions

- A working fingertip pulse oximeter with batteries.
- Warm hands, a place to sit still, and no immediate emergency symptoms.
- If breathing is severely difficult, lips look blue, confusion occurs, or chest pain is present, call emergency services instead of relying on the device.

## Steps

1. **Warm the hand.** Rub hands together or warm them indoors before measuring. → *Expect:* fingers are warm and pink enough for blood flow.
2. **Remove barriers.** Take off dark nail polish, artificial nails, or anything squeezing the finger if possible. → *Expect:* the sensor has a clear path through the nail bed.
3. **Sit still.** Rest the hand at chest level and keep the finger still. → *Expect:* motion does not scramble the signal.
4. **Clip the device on.** Insert the finger fully so the nail faces the display or as the device instructions show. → *Expect:* the oximeter turns on and begins detecting.
5. **Wait for a stable reading.** Give it 30 to 60 seconds until numbers stop jumping. → *Expect:* SpO2 and pulse are steady for several seconds.
6. **Read both numbers.** SpO2 is oxygen saturation percentage; pulse is beats per minute. → *Expect:* you record both values, not just one.
7. **Repeat if surprising.** Try another warm finger and compare with how you feel. → *Expect:* a confirmed reading or a reason to distrust the device.
8. **Interpret cautiously.** Many healthy people read 95% to 100% at sea level; 92% or lower, or a clear drop from your usual, deserves medical advice. → *Expect:* the number is judged with symptoms and baseline.

## Decision points

- SpO2 is 90% or lower → seek urgent medical care, especially if new or paired with symptoms.
- SpO2 is 91% to 94% and new, persistent, or worsening → call a clinician promptly.
- Cold hands, motion, dark polish, poor circulation, or some skin and nail factors may distort readings → correct what you can and repeat.

## Failure modes & recovery

- **F1 No reading appears:** replace batteries, warm the finger, and try a different finger.
- **F2 Numbers jump constantly:** keep still, rest the hand, and wait longer.
- **F3 Pulse differs wildly from manual pulse:** trust symptoms and repeat manually using `healthcare/measure-your-heart-rate`.
- **F4 Low number but you feel very ill:** seek care rather than troubleshooting the device.

## Verification

A stable SpO2 and pulse are recorded after warm, still measurement, and any low oxygen threshold or serious symptom is escalated.

## Variations

- High altitude: usual SpO2 may be lower; compare with local medical guidance and your baseline.
- Chronic lung or heart disease: follow the action plan from your clinician, which may use personalized thresholds.
- Children: use a pediatric-sized device when needed and seek care promptly for breathing distress.

## Safety & privacy

Medium risk because false reassurance can delay care. Call emergency services for severe breathing trouble, blue lips or face, confusion, chest pain, fainting, or SpO2 around 90% or lower.
