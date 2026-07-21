---
name: read-a-utility-meter
domain: housing
locale: [generic]
interface: mixed
difficulty: basic
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

You read a water, gas, or electric utility meter accurately enough to submit a reading or spot abnormal usage.

## Preconditions

- You know which utility meter you need to read and where it is located.
- You have safe access, a flashlight, and the account or submission portal if reporting the reading.
- You know whether the meter is digital, rolling number, or dial style.
- You do not open sealed utility equipment or enter unsafe spaces.

## Steps

1. **Match the meter to the utility.** Check the label, pipe, cable, or account meter number. → *Expect:* the meter number matches the bill or property.
2. **Clean the view without opening seals.** Wipe dust or condensation from the outside of the display only. → *Expect:* digits or dials are readable.
3. **Read digital or rolling numbers left to right.** Record the black or main digits and ignore red decimals unless your utility asks for them. → *Expect:* you have a whole-unit reading.
4. **Read dial meters carefully.** For each dial, record the lower number when the pointer is between two numbers. → *Expect:* each dial has one chosen digit.
5. **Handle opposite dial directions.** Notice that adjacent dials may rotate opposite ways, and read the printed numbers on each dial. → *Expect:* direction does not change the lower-number rule.
6. **Photograph the meter.** Take a clear photo including meter number and reading. → *Expect:* you have evidence if a digit is questioned.
7. **Submit the reading if needed.** [BRANCH: utility website | app | phone | postcard] enter digits exactly as requested. → *Expect:* the system accepts the reading or gives a confirmation.
8. **Check for unusual movement.** With water or gas appliances off, watch whether the indicator still moves. → *Expect:* no unexplained usage appears during a short check.

## Decision points

- If the display cycles through screens, wait for the usage reading labeled by the utility, such as kWh, gallons, cubic feet, or cubic meters.
- If a dial pointer sits exactly on a number, check the dial to the right to decide whether it has passed.
- If the meter is in a locked or hazardous area, ask the utility or property manager for access.
- If usage is much higher than normal, compare dates, estimated bills, and possible leaks before disputing.

## Failure modes & recovery

- **F1 Wrong meter:** detect meter number mismatch, recover by locating the meter number printed on your bill.
- **F2 Decimal included incorrectly:** detect reading rejected or wildly high, recover by following the utility's digit instructions.
- **F3 Dial read high:** detect pointer between digits, recover by using the lower digit unless the next dial has fully passed zero.
- **F4 No confirmation:** detect submission page closes without receipt, recover by resubmitting or calling with the photo.
- **F5 Leak suspected:** detect movement while all fixtures are off, recover by shutting fixtures and contacting maintenance or utility.

## Verification

The submitted or recorded reading matches a clear meter photo, uses the correct meter number, and follows the utility's requested digit format.

## Variations

- Smart meters: the utility portal may show interval usage, while the physical meter still has a display.
- Water meters: a small triangle or wheel often shows tiny continuous flow from leaks.
- Gas meters: if you smell gas, leave and call emergency service instead of reading the meter.

## Safety & privacy

Low risk if you stay outside sealed equipment. Do not tamper with utility locks or seals, and treat account numbers and meter photos as household information.
