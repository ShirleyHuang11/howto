---
name: remember-birthdays
domain: daily
subdomain: social
locale: [generic]
interface: mixed
difficulty: basic
est_time: 1h
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
---

## Goal

A one-time setup after which the birthdays of everyone you care about surface automatically with enough lead time, and each person gets an effort level that matches the relationship: nobody important is forgotten, and nobody gets an awkwardly overdone gesture.

## Preconditions

- A calendar you actually look at daily (phone default calendar is fine; the system fails on a calendar you never open).
- A list of people whose birthdays matter to you; if you do not have dates, willingness to ask directly ("when's your birthday? I'm terrible at remembering and I'm fixing that") which nobody minds.
- Ten minutes of honest triage about who belongs in which tier.

## Steps

1. **Collect the dates.** Sources in order of reliability: asking the person, family members, past chat messages ("happy birthday!" scrollback), social profiles. Record day and month; year is optional and sometimes sensitive. → *Expect:* a list of names with dates; unknowns flagged to ask at the next natural contact.
2. **Tier the list.** Tier 1: partner, immediate family, closest friends (call or see them, often a gift). Tier 2: good friends, close colleagues (personal message, occasional gift). Tier 3: broader circle (short warm message, no gift). → *Expect:* every name has exactly one tier; when torn, tier down; a sincere message beats a hollow gift.
3. **Create recurring annual calendar events.** One all-day event per person, repeating yearly, named plainly ("Maya's birthday"). Put the tier and any gift notes in the event description. → *Expect:* each event shows as repeating annually, verified by jumping to next year.
4. **Set two alerts per event, tier-dependent.** Tier 1: 2 weeks before (gift or plan lead time) plus day-of morning. Tier 2: 3 days before plus day-of. Tier 3: day-of only. → *Expect:* alert settings visible on each event; the early alert exists because day-of is too late for gifts, cards, or restaurant bookings.
5. **Act on the early alert immediately, not later.** When the 2-week or 3-day alert fires, do the lead-time action in that moment: order the gift, book the table, mail the card. Deferring reproduces the original problem. → *Expect:* the lead-time action done or scheduled the same day the alert fires.
6. **Send the day-of message in the morning, and make it specific.** One line beats a paragraph: reference something real ("hope the new job is treating you well") rather than bare "HBD". [BRANCH: Tier 1 → call or in-person, message as fallback only | Tier 2-3 → message] → *Expect:* message sent before noon their time; morning greetings land as "they thought of me," evening ones as "they almost forgot."
7. **Capture new people and corrections as they occur.** New close friend, a date you got wrong, a relationship that faded: edit the calendar within a day of learning, since "I'll add it later" is where the system leaks. → *Expect:* the calendar matches your actual current circle.

## Decision points

- The person hates birthday attention → a private low-key message; never the group-chat announcement or office ambush. Note the preference in the event description.
- Birthday lands on Feb 29 → celebrate Feb 28 or Mar 1 in off years; ask them which they prefer once and record it.
- You learn the birthday only on the day, mid-conversation → greet warmly now, add the calendar event within the hour.
- A close friendship has faded → quietly downgrade the tier rather than sending increasingly hollow Tier 1 gestures; the calendar should track reality.
- Timezone differences (Tier 1 abroad) → set the day-of alert to their morning, not yours.

## Failure modes & recovery

- **F1 Alert fatigue:** too many people added, alerts get swiped away unread → prune Tier 3 aggressively; a system covering 25 people that you obey beats one covering 80 that you ignore.
- **F2 Missed it anyway:** you discover the birthday a day or a week late → send the belated message immediately and name it plainly ("I'm late and sorry, happy birthday for Tuesday"); a warm late message beats silence, and pretending you didn't miss it reads worse than owning it.
- **F3 Wrong date on record:** you greet them on the wrong day → thank whoever corrects you, fix the event immediately, and check the repeat rule actually saved.
- **F4 Social-media dependency:** you relied on platform notifications, then left the platform or they hid their birthday → the calendar is the primary system precisely because platforms churn; treat platform reminders as a backup signal only.
- **F5 Gift panic on day-of:** the early alert was ignored → same-day options in order: experience booking (dinner), digital gift card with a personal note, or an honest "your gift is arriving late, it was worth it." Rushed generic gifts to Tier 1 people read as exactly what they are.

## Verification

Every person you would be embarrassed to forget has a yearly repeating event with tier-appropriate alerts, next year's occurrences are visible in the calendar, and across the next few months of birthdays: zero Tier 1-2 birthdays pass unacknowledged, and day-of messages go out in the recipient's morning.

## Variations

- Paper variant: a birthday book plus a monthly ritual of copying the month's birthdays somewhere visible; works, but has no alerts, so the monthly ritual is load-bearing.
- Couples/household: a shared calendar for the joint social circle prevents both people assuming the other one sent the greeting.
- Contacts-app birthday fields: many phones auto-surface these; fine as a data source, but set explicit alerts, since silent list entries do not interrupt you.

## Safety & privacy

Low risk. Birth dates are identity data (used in verification questions), so avoid posting full birth dates publicly and be sparing about recording birth years of others. A private calendar is the right container; a public spreadsheet of friends' birth dates is not.
