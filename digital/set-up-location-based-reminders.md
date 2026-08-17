---
name: set-up-location-based-reminders
domain: digital
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Create a reminder that alerts when you arrive at or leave a specific place, with location permissions limited to the reminder app.

## Preconditions

- The phone has location services enabled.
- The reminder app supports location alerts.
- You know the address or place name for the reminder.

## Steps

1. **Choose the reminder app.** [BRANCH: iPhone | Android] use Apple Reminders on iPhone or Google Keep, Google Assistant, Tasks where supported, or another trusted reminder app on Android. → *Expect:* the chosen app can create location-based alerts.
2. **Check app location permission.** [BRANCH: iOS | Android] use Settings > Privacy & Security > Location Services or Settings > Location > App location permissions. → *Expect:* the reminder app has location access while needed.
3. **Create the reminder text.** Write a specific action such as "Buy printer paper" or "Return library book." → *Expect:* the reminder clearly says what to do.
4. **Add the location trigger.** Choose Arriving, Leaving, Getting in car, or Getting out of car if available, then enter the address or saved place. → *Expect:* the app shows a map pin or named place.
5. **Adjust the radius if available.** Make the trigger area large enough for the parking lot or building entrance but not the whole neighborhood. → *Expect:* the reminder has a reasonable geofence.
6. **Save and sync.** Save the reminder and confirm it appears on the correct list or account. → *Expect:* the reminder remains visible after closing and reopening the app.
7. **Test with a nearby place if practical.** Create a temporary test reminder for a nearby location and delete it after it fires. → *Expect:* location alerts work on the device.

## Decision points

- Reminder must fire at a store chain → use a specific branch address, not only the brand name.
- Battery saving is aggressive → allow background location or disable battery restriction for the reminder app.
- Shared reminder list → consider whether the place reveals private routines.

## Failure modes & recovery

- **F1 Reminder never fires:** detect no alert at the place → check precise location, background permission, and battery optimization.
- **F2 Alert fires too early:** detect reminder away from the target → reduce geofence radius or choose a more precise address.
- **F3 Wrong account used:** detect reminder missing on another device → create it in the synced account used on that device.
- **F4 Location unavailable:** detect app cannot add a place → enable location services and check internet access.

## Verification

The reminder shows the correct text, place, arrival or departure trigger, and account/list, and a test or future visit produces the expected alert.

## Variations

- iPhone: Reminders supports location alerts from the detail button when location permission is enabled.
- Android: support varies by app and manufacturer; Google Assistant and Keep behavior may change by account.
- Car reminders: some phones can trigger reminders when connecting to or disconnecting from car Bluetooth.

## Safety & privacy

Low risk. Location reminders reveal routines to the app and any shared list members, so avoid sensitive places on shared accounts.
