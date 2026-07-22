---
name: set-a-recurring-reminder
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

A reminder repeats on the right schedule or trigger, alerts you in the right place, and gets reviewed often enough that ignored reminders do not pile up.

## Preconditions

- You have a reminders, tasks, calendar, or notes app that can send notifications.
- Notifications are allowed for that app.
- You know the action, repeat pattern, and whether it depends on time or location.

## Steps

1. **Choose the right app.** Use reminders or tasks for actions, calendar for appointments, and medication or finance apps for regulated routines when appropriate. → *Expect:* the reminder lives where you will actually act on it.
2. **Create the reminder.** Enter a short verb-first title such as "Take trash out" or "Pay rent." → *Expect:* the reminder is easy to understand at a glance.
3. **Set the first due time.** Choose the first date and time when the action should happen. → *Expect:* the initial alert is scheduled.
4. **Add the repeat rule.** [BRANCH: daily | weekly | monthly | custom] choose the recurrence that matches the real-world routine. → *Expect:* future occurrences appear or the rule is shown.
5. **Use a location trigger if better.** For errands, add a location such as arriving at home, work, or a store instead of a fixed time. → *Expect:* the app shows the location condition.
6. **Set notification behavior.** Allow alerts, sound, lock-screen visibility, or priority only if the reminder should interrupt you. → *Expect:* the reminder can notify you at the intended moment.
7. **Practice snooze discipline.** If you snooze, choose a real next action time rather than repeatedly pushing it by a few minutes. → *Expect:* snoozed reminders remain intentional.
8. **Schedule a review.** Weekly or monthly, delete stale reminders, adjust repeat rules, and promote missed reminders to a better app or time. → *Expect:* the list stays trusted and current.

## Decision points

- The task must happen at an exact time → use a time reminder or calendar event, not a location trigger.
- The task happens when you arrive somewhere → location triggers can work better than guessing a time.
- You ignore the alert repeatedly → change the timing, reduce noise, or decide the task is not worth recurring.

## Failure modes & recovery

- **F1 Reminder does not alert:** detect a missed notification, recover by checking app notification permission, focus mode, battery restrictions, and alert time.
- **F2 Repeats on wrong day:** detect future occurrences on the wrong schedule, recover by editing the recurrence rule from the series, not just one instance.
- **F3 Location trigger fails:** detect no alert after arrival, recover by enabling location permission and using a broader location radius.
- **F4 Reminder pileup:** detect many overdue reminders, recover by completing, deleting, or rescheduling each during a weekly review.

## Verification

The reminder shows the correct next occurrence, repeat rule, trigger type, and notification setting, and it appears in your review list.

## Variations

- `iphone`: Reminders supports date, time, location, tags, lists, and repeated custom schedules.
- `android`: Google Tasks, Calendar, Keep, and assistant reminders vary in repeat and location support.
- `work`: task managers may support recurrence on completion, which is better for chores that should repeat after you actually finish them.

## Safety & privacy

Reminders can reveal routines, medications, addresses, bills, and family obligations on the lock screen. Hide sensitive notification previews and avoid location triggers for places you do not want stored.
