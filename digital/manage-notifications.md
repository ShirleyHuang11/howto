---
name: manage-notifications
domain: digital
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
---

## Goal

Your phone interrupts you only for things that actually deserve an interruption. Every app's notifications are triaged into keep, silence, or off; a priority/focus mode protects your attention when needed; and the badge count reflects real, unread items rather than noise.

## Preconditions

- Access to notification settings (iPhone: Settings > Notifications; Android: Settings > Notifications > App settings).
- A few minutes and the honesty to admit most apps do not need to buzz you.

## Steps

1. **Open the per-app notification list.** Both platforms list every app that can notify you, often with how many you got recently. → *Expect:* a long list, most of which you never consciously chose to enable.
2. **Triage each app into three buckets.** For every app decide: interrupt me (messages from people, calls, calendar, security alerts), silent/no-buzz (news, social, shopping: allowed but quiet), or off entirely (games, promos, "we miss you" apps). → *Expect:* each app assigned; the interrupt bucket is short, a handful at most.
3. **Turn off the noise.** For the "off" bucket, disable Allow Notifications. For the "silent" bucket, keep them delivered to the notification list but turn off sound, vibration, and lock-screen banners. → *Expect:* those apps stop making sound or popping up, while still logging quietly if you left them silent.
4. **Shape the important ones.** For the interrupt bucket, enable sound and banners, and on iPhone consider marking key ones Time Sensitive so they cut through Focus modes. → *Expect:* only your short interrupt list can make noise or vibrate.
5. **Kill badge dots that are not real.** Turn off the red badge for apps whose count is meaningless (social apps inflating a "3" to pull you in). Keep badges only where the number means genuine unread items (messages, email, tasks). → *Expect:* the badges left on your home screen correspond to things you would actually want to clear.
6. **Set up a priority / focus mode.** iPhone: Focus (Do Not Disturb, Work, Sleep) with an allow-list of people and apps. Android: Do Not Disturb with priority exceptions and a schedule. Allow only favorite contacts and repeat callers to break through. → *Expect:* a mode that, when on, silences everything except your named exceptions, and a schedule (e.g. sleep hours) that turns it on automatically.
7. **Configure repeat-caller and emergency bypass.** So a genuine emergency (someone calling twice) still reaches you even in Do Not Disturb. → *Expect:* the "allow repeated calls" / emergency bypass option is on.
8. **Live with it for a few days, then adjust.** Any app that buzzed you and made you think "why did I get this" gets demoted; anything you missed gets promoted. → *Expect:* after tuning, notifications feel like signal, and reaching for the phone is a choice, not a reflex.

## Decision points

- Unsure whether to silence an app → default to silent, not off. Silent keeps the information reachable without the interruption; you can promote it later if it earns it.
- Work and personal on one phone → use separate Focus modes with different allow-lists and schedules rather than one blunt Do Not Disturb.
- You keep missing genuinely important alerts → the interrupt bucket is too big and diluted; shrink it so the alerts that remain stand out.

## Failure modes & recovery

- **F1 Missed something important after silencing:** promote that specific app to the interrupt bucket or mark it Time Sensitive; do not undo the whole triage over one miss.
- **F2 Badge count will not clear:** it is often a hidden unread (an archived email, a pending update). Open the app's inbox/list to clear it, or turn the badge off if the number is not actionable.
- **F3 Focus mode silenced a real call:** add that person to the allow-list and enable repeat-caller bypass so a second call breaks through.
- **F4 Notifications creep back after an app update:** apps re-enable themselves on update. Re-check the per-app list periodically and re-silence the offenders.

## Verification

Only a short, deliberate set of apps can make sound or vibrate; the rest are silent or off; badges remain only where the count is real; and a scheduled focus/priority mode silences everything except named exceptions while still letting a repeated emergency call through.

## Variations

- `computer`: same triage on desktop notifications and a focus/do-not-disturb mode; browser sites also ask to notify, so deny by default and allow only the few you want.
- Minimalist approach: turn everything off except calls and direct messages, and check apps on your own schedule instead of being pulled in.

## Safety & privacy

Low risk. One privacy note: lock-screen previews can show message contents to anyone who glances at your phone. Set sensitive apps (messages, banking, 2FA) to hide previews until unlocked, so a notification announces that something arrived without displaying what it says.
