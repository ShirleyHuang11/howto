---
name: set-screen-time-limits
domain: digital
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Set realistic device limits that reduce unwanted screen time without breaking essential access.

## Preconditions

- Access to the phone, tablet, or computer settings.
- Device passcode or parent account access if managing a child device.
- A rough idea of which apps or time windows cause problems.

## Steps

1. **Open the built-in screen-time tool.** [BRANCH: iOS | Android | desktop] use Screen Time, Digital Wellbeing, Family Link, or the operating system's focus controls. → *Expect:* the device shows usage, app timers, downtime, or focus settings.
2. **Review actual usage first.** Look at the last 7 days, not just today. → *Expect:* the biggest apps and peak time windows are visible.
3. **Choose app limits for specific drains.** Set timers on social, video, games, or shopping apps rather than every app. → *Expect:* only selected apps will lock or warn after the limit.
4. **Choose downtime for daily boundaries.** Set a sleep, work, school, or family window when most apps are blocked. → *Expect:* the schedule has start and end times.
5. **Keep essentials allowed.** Add phone, maps, messages, calendar, banking, transit, medical, or work apps as needed. → *Expect:* important tasks still work during limits.
6. **Use honest defaults.** Start with a limit you can actually follow, such as 30 minutes less than current use. → *Expect:* the limit is challenging but not instantly ignored.
7. **Handle kids differently from self-limits.** [BRANCH: child | self] for kids, set a parent passcode and content rules. for self, avoid making the override too easy. → *Expect:* the person subject to the limit cannot casually remove it.
8. **Plan for the override trap.** Decide when "one more minute" or "ignore today" is allowed before the prompt appears. → *Expect:* overrides have a rule, not a mood.
9. **Turn on notifications or reports.** Enable weekly summaries or parent reports if useful. → *Expect:* usage feedback arrives without manually checking every day.
10. **Review after one week.** Tighten, loosen, or move limits based on actual misses. → *Expect:* the rule matches behavior better than the first guess.

## Decision points

- Limits block work, school, medical, or travel tasks → add those apps to always-allowed.
- You override every day → reduce the limit more gradually or add friction with a passcode held by someone else.
- Child finds bypasses → update OS, remove alternate browsers, and check family settings.
- Shared device → use profiles or account-based controls where possible.

## Failure modes & recovery

- **F1 Overbroad lockout:** essential apps stop working, recover by editing always-allowed apps.
- **F2 Passcode forgotten:** parent or screen-time passcode is lost, recover through official account recovery.
- **F3 Override habit:** prompts become automatic dismissals, recover by disabling easy overrides or lowering ambition.
- **F4 Wrong device only:** limits set on tablet but phone remains unrestricted, recover by enabling cross-device sharing or repeating setup.

## Verification

During the chosen limit window, a restricted app shows a timer, warning, or block while essential apps remain usable.

## Variations

- iOS: Screen Time can sync across devices signed into the same Apple ID.
- Android: Digital Wellbeing varies by manufacturer, while Family Link manages child accounts.
- Work profiles: employer-managed apps may have separate controls or restrictions.

## Safety & privacy

Usage reports can reveal habits, locations, and relationships. For children, explain the rule and avoid sharing reports beyond caregivers who need them.
