---
name: replace-a-smoke-alarm
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

An expired or failed smoke alarm is replaced with the right type, tested, and dated so the household knows when it must be replaced again.

## Preconditions

- You can reach the alarm safely with a stable step ladder.
- You have a replacement alarm, fresh batteries if required, a pencil, and the old alarm model or manual.
- For hardwired alarms, you know the breaker and are comfortable confirming power is off.

## Steps

1. **Check the replacement rule.** Read the manufacture date on the old alarm and replace it if it is 10 years old or older. → *Expect:* you have confirmed replacement is needed.
2. **Silence and remove the old unit.** Twist it off the base and disconnect the battery or plug. [BRANCH: battery-only | hardwired] hardwired units require breaker power off before unplugging the harness. → *Expect:* the old alarm is down and no live work is exposed.
3. **Match the alarm type.** Replace like with like where code or system design requires it, such as smoke, heat, photoelectric, ionization, or combination CO. → *Expect:* the new unit matches the location and old function.
4. **Mount the new base.** Use the supplied base and screws, drilling only where you have checked for wires or pipes. → *Expect:* the base is tight and flat.
5. **Connect power or battery.** Plug in the harness or install the battery, then seat the alarm on the base. → *Expect:* the alarm chirps or shows a ready light.
6. **Test the alarm.** Press and hold the test button until it sounds, warning nearby people first. → *Expect:* the alarm sounds clearly and interconnected alarms respond if fitted.
7. **Log the date.** Write the installation date and replacement year on the unit or household maintenance log. → *Expect:* the next 10-year deadline is visible.

## Decision points

- Hardwired connector does not match → use an approved adapter only if the alarm maker lists it, otherwise replace the base and harness according to code.
- Alarm is part of a monitored system → call the monitoring company before testing or replacing.
- Local rules require specific placement → follow local code over package diagrams.
- Alarm fails the test → replace the battery once, then exchange the unit if it still fails.

## Failure modes & recovery

- **F1 Alarm chirps after install:** detect periodic chirping, recover by seating the battery, closing the battery drawer, and checking the expiry date.
- **F2 No sound on test:** detect silence during the button test, recover by checking power and returning a defective unit.
- **F3 Interconnect does not trigger:** detect only one alarm sounding, recover by checking compatibility and wiring.
- **F4 Base holes are loose:** detect wobble on the ceiling or wall, recover with appropriate anchors or a new mounting location.

## Verification

The installed alarm sounds on its test button and has an installation date plus a replacement date no more than 10 years out.

## Variations

- `rental-home`: notify the landlord or building manager if alarms are hardwired or code-controlled.
- `co-combination`: follow CO alarm placement rules as well as smoke alarm rules.
- `sealed-battery`: the whole alarm is replaced when the sealed battery expires.

## Safety & privacy

Medium risk because smoke alarms are life-safety devices and hardwired units may carry mains voltage. Do not leave a sleeping area unprotected while waiting for parts.
