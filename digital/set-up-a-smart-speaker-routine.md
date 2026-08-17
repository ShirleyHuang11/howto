---
name: set-up-a-smart-speaker-routine
domain: digital
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Create a smart speaker routine that performs the intended actions reliably without exposing private commands or controlling sensitive devices unexpectedly.

## Preconditions

- The smart speaker is already set up and online.
- The phone has the Alexa, Google Home, or Apple Home app installed.
- Devices used in the routine already work manually.

## Steps

1. **Choose a simple routine goal.** Pick a morning, bedtime, leaving home, arrival, or reminder routine with a clear trigger. → *Expect:* the routine has one primary purpose.
2. **Open routine automation settings.** [BRANCH: Alexa | Google Home | Apple Home] open Alexa > More > Routines, Google Home > Automations, or Home > Automation/Shortcuts. → *Expect:* the app shows routine or automation creation controls.
3. **Set the trigger.** Choose voice phrase, time, sunrise/sunset, alarm dismissal, device state, or location if supported. → *Expect:* the trigger is visible and specific.
4. **Add actions in order.** Add lights, speaker volume, weather, calendar, music, announcements, plugs, or thermostat changes one at a time. → *Expect:* the action list matches the intended sequence.
5. **Avoid risky actions.** Do not include door unlocking, oven controls, or security disarming unless the platform requires explicit confirmation and the household agrees. → *Expect:* sensitive devices are absent or protected by confirmation.
6. **Choose target speaker or room.** Set where audio plays and which devices respond. → *Expect:* the routine will not announce private information in the wrong room.
7. **Test and adjust.** Run the routine manually, then trigger it normally once. → *Expect:* each action runs in order with acceptable volume and timing.

## Decision points

- Routine includes location triggers → consider privacy and battery impact before enabling location access.
- Multiple household members use the speaker → avoid personal calendar or commute details on shared speakers.
- Devices are in bedrooms → check volume and lights before using early morning or late night routines.

## Failure modes & recovery

- **F1 Routine does not start:** detect no response to trigger → check exact phrase, schedule timezone, and speaker internet.
- **F2 Action skipped:** detect one device unchanged → confirm the device works manually and is assigned to the correct room.
- **F3 Wrong speaker responds:** detect audio in another room → set the playback device or room explicitly.
- **F4 Private info announced:** detect calendar or message details on shared speaker → remove that action or limit personal results.

## Verification

The routine appears in the smart-home app, runs from its normal trigger, performs each action in order, and avoids unintended sensitive device or private-information behavior.

## Variations

- Alexa: Routines can use voice, schedule, smart-home, alarm, and location triggers.
- Google Home: Household and personal automations have different sharing behavior.
- Apple Home: Some automations require a home hub such as HomePod or Apple TV.

## Safety & privacy

Low to medium risk depending on connected devices. Be cautious with locks, cameras, alarms, location triggers, and personal announcements on shared speakers.
