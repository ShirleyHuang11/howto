---
name: share-your-location-with-family-safely
domain: digital
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 15min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Share live or periodic location with trusted family members while limiting duration, audience, and notification exposure.

## Preconditions

- You have consent from each person whose location will be shared.
- Phones have location services enabled.
- Family members have Apple ID, Google account, or the chosen messaging app account.

## Steps

1. **Choose the sharing app.** [BRANCH: iPhone family | Android or mixed family | short trip] use Find My for iPhone groups, Google Maps Location Sharing for mixed devices, or Messages/WhatsApp for temporary sharing. → *Expect:* everyone knows which app will show the location.
2. **Review location permissions.** [BRANCH: iOS | Android] open Settings > Privacy & Security > Location Services or Settings > Location > App location permissions and allow only the chosen app. → *Expect:* the chosen app has location access and unrelated apps do not gain new access.
3. **Select recipients carefully.** Add only the family members who need access and verify names, phone numbers, or email addresses. → *Expect:* the recipient list contains no old contacts or group chats.
4. **Set a duration.** Choose one hour, until end of day, indefinitely only for trusted caregivers, or a custom trip duration. → *Expect:* the app shows when sharing will stop or that it is indefinite.
5. **Start sharing.** Confirm the sharing prompt and wait for the recipient to see your location. → *Expect:* the recipient's phone shows your approximate current location.
6. **Tune notifications.** Enable useful arrival/departure notifications only for places everyone agrees to, such as home, school, or work. → *Expect:* notifications are limited to agreed places and people.
7. **Review active sharing.** Open the app's sharing list and remove anyone who no longer needs access. → *Expect:* only intended family members remain.

## Decision points

- Sharing with a child → use the platform family controls rather than a public group chat.
- Sharing during travel only → use temporary sharing and set an end time.
- Domestic abuse, stalking, or coercion risk → do not enable sharing; check for existing hidden sharing and seek trusted help.
- Battery is low → live sharing may drain power, so use check-ins or short duration.

## Failure modes & recovery

- **F1 Recipient cannot see location:** detect stale or unavailable status → confirm internet, location permissions, and account identity.
- **F2 Wrong person added:** detect unexpected name in sharing list → stop sharing immediately and restart with the correct recipient.
- **F3 Location is inaccurate:** detect wrong map position → enable precise location for the chosen app and move outdoors briefly.
- **F4 Sharing will not stop:** detect indefinite sharing still active → remove recipients in the sharing app and revoke app location permission if needed.

## Verification

The intended family member can see your current location in the chosen app, the sharing duration is visible, and the active sharing list contains only approved recipients.

## Variations

- iOS: Find My > People > Start Sharing Location supports Apple-family sharing and notifications.
- Android or mixed devices: Google Maps > profile picture > Location sharing supports Google accounts and time limits.
- Messaging apps: temporary live location is useful for single trips but weaker for family management.

## Safety & privacy

Medium risk because location data can reveal home, school, work, routines, and sensitive visits. Share with consent, limit duration, and review active recipients regularly.
