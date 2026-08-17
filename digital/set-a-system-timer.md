---
name: set-a-system-timer
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Set a countdown timer on your device so it alerts you after a chosen duration.

## Preconditions

- Your device is on and notifications or sound are available.
- You know the countdown duration.

## Steps

1. **Open the timer tool.** [BRANCH: Windows | Mac | mobile-app] open Clock, Alarms & Clock, Siri, Google Assistant, or another system timer. → *Expect:* timer controls are visible.
2. **Enter the duration.** Set hours, minutes, and seconds as needed. → *Expect:* the timer shows the intended countdown length.
3. **Name the timer if available.** Add a label such as laundry, break, or oven. → *Expect:* the label appears with the timer.
4. **Start the timer.** Click or tap `Start`. → *Expect:* the countdown begins decreasing.
5. **Confirm alert settings.** Check that volume, focus mode, or notification settings will allow the timer alert. → *Expect:* the device can play or show the timer alert.

## Decision points

- You need a calendar appointment → create a reminder or event instead of a short timer.
- You need hands-free setup → use a voice assistant if available.
- The timer is safety-critical → stay nearby and use a second timer if needed.

## Failure modes & recovery

- **F1 Timer not audible:** detect muted device or blocked notifications → raise volume, disable silence mode, or use vibration.
- **F2 Wrong duration:** detect countdown length is incorrect → cancel and set the timer again.
- **F3 App closed the timer:** detect countdown disappears → reopen the clock app or set a new timer.

## Verification

The countdown is running with the intended duration and will alert through visible notification, sound, or vibration.

## Variations

- `windows`: use the Clock app's Timer tab.
- `mac`: use the Clock app on newer macOS versions or Siri.
- `mobile-app`: iOS and Android Clock apps support multiple timers.

## Safety & privacy

Timers are low risk, but do not rely on a muted or low-battery device for cooking, medication, travel, or other time-sensitive tasks.
