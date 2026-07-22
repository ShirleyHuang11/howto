---
name: set-up-a-shared-family-calendar
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Your household has one shared calendar for family events, with members added, colors and notifications set, and editing rights controlled.

## Preconditions

- Each family member who will use the calendar has an email or account for the calendar platform.
- You can access calendar settings on web or mobile.
- The household agrees which events belong on the shared calendar.

## Steps

1. **Create a separate calendar.** Make a new calendar named Family, Household, or another shared name instead of sharing your personal calendar. → *Expect:* a new empty calendar appears in your calendar list.
2. **Set the calendar description.** Add a short note such as "shared appointments, school dates, travel, and household reminders." → *Expect:* members can recognize the calendar's purpose.
3. **Add family members.** Invite each person by email or account address. → *Expect:* every member appears as pending or accepted.
4. **Choose who can edit.** [BRANCH: adults edit | everyone edits] give edit rights to people who schedule events and view rights to people who only need awareness. → *Expect:* permissions differ by member if needed.
5. **Color-code the calendar.** Pick a distinct color for the shared calendar, and optionally use event titles or emojis avoided here for each person. → *Expect:* family events stand out from personal events.
6. **Set default notifications.** Add reminders such as one day before and one hour before for events where advance notice matters. → *Expect:* new family events include useful alerts.
7. **Add key recurring events.** Enter school schedules, practices, trash pickup, medication reminders, custody exchanges, or bill dates as appropriate. → *Expect:* repeated family obligations appear on future dates.
8. **Test on each device.** Ask members to accept, show the calendar, and create or view a harmless test event. → *Expect:* everyone sees the same shared calendar on phone and web.

## Decision points

- Young children need visibility only → give view access or use a supervised family account.
- Some events are sensitive → keep them on a private calendar and add only a vague busy block to the family calendar.
- Notifications overwhelm people → reduce default alerts and set extra reminders only on high-stakes events.

## Failure modes & recovery

- **F1 Member cannot see calendar:** detect when the calendar is missing, recover by confirming the invite email and asking them to enable the calendar checkbox.
- **F2 Events appear on personal calendar:** detect when a new event is not shared, recover by changing the event's calendar field to the family calendar.
- **F3 Someone edits by accident:** detect unexpected changes, recover by lowering that person's permission and restoring the event from history or trash if available.
- **F4 Alerts annoy everyone:** detect repeated complaints or ignored alerts, recover by changing default notifications and using event-specific alerts.

## Verification

Each intended member can see the shared family calendar, and only the intended people can create or edit events on it.

## Variations

- `google-family`: Google can create family calendars automatically for family groups, but permissions may be tied to the group.
- `apple-family`: Family Sharing can expose a shared Family calendar across iCloud devices.
- `mixed-platform`: a shared Google or Outlook calendar is often easier across iPhone, Android, and web.

## Safety & privacy

Family calendars can reveal children’s locations, routines, school names, medical visits, and travel dates. Share with household members only and review access after moves, separations, caregiver changes, or device handoffs.
