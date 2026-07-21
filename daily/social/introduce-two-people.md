---
name: introduce-two-people
domain: daily
subdomain: social
locale: [generic]
interface: mixed
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
---

## Goal

Two people you know are introduced to each other, in person or by message, with enough context that a conversation can start without you, and with consent obtained where the introduction creates obligations.

## Preconditions

- Two people who would plausibly benefit from knowing each other, and their names retrievable (`daily/social/remember-names` is the upstream dependency everyone feels here).
- For introductions that create work (job referrals, sales, asks for help): the consent of the person receiving the ask, obtained beforehand. Surprise-obligation introductions spend your credibility with both parties.

## Steps

1. **In person: catch the moment before it becomes awkward.** Someone joins your conversation, or you are standing with two mutually unknown people: introduce within the first seconds, before parallel small talk makes it strange. → *Expect:* the introduction happening early, not after ten minutes of the two nodding at each other namelessly.
2. **Say both names clearly, with one hook each.** "Maya, this is Tom — we studied together and he just moved here. Tom, Maya runs the climbing gym I keep telling you about." The hook is the gift: it hands them their first topic. → *Expect:* each person holding the other's name plus one conversational handle.
3. **Bridge them, then step back or stay, by reading the purpose.** If the point was connecting them: one seeding question ("Tom's been looking for a gym, actually") and let them run. If it is simply group courtesy: the conversation continues with everyone named. → *Expect:* the two talking to each other, not through you.
4. **By message (the email/text intro): get the double opt-in first.** Ask the busier or receiving party privately: "May I connect you with X about Y?" Only after yes, send the intro. → *Expect:* consent in hand before any names meet in one thread.
5. **Write the intro message with symmetric hooks and a clear reason.** Both names, one line each about who they are, one line on why this connection ("You are both building in robotics education; I suspect a coffee would be worth it"), and a handoff ("I'll let you take it from here"). → *Expect:* a short message either party could act on without asking you anything.
6. **Exit the thread and let it live or die on its own.** Your job ends at the handoff; chasing ("did you two ever meet?") once, later, is friendly; refereeing the connection is not your role. → *Expect:* the two people owning the follow-up.

## Decision points

- Hierarchy and formality: name the senior or honored person first in formal contexts; in casual ones, order is free and warmth beats protocol.
- Forgotten name mid-introduction: the honest escape is graceful: "I'm so sorry, remind me of your name?" or engineer the self-introduction ("Have you two met?" makes them exchange names themselves).
- Whether to introduce at all: two people who would merely be polite to each other need group courtesy naming only; the full bridged introduction is for genuine mutual value.

## Failure modes & recovery

- **F1 The intro thread goes silent:** it happens and it is theirs; one light nudge after a couple of weeks if you care ("no pressure, but I still think you two would hit it off"), then release.
- **F2 You introduced without consent and the receiver is annoyed:** apologize to them privately (`daily/social/apologize-well`), absorb the lesson, and shield them ("no obligation at all — my enthusiasm ran ahead of my manners").
- **F3 Mangled a name or a detail in the hook:** correct it immediately and lightly; the correction costs a second, the uncorrected version compounds.
- **F4 The two turn out to know each other (badly):** "Ah, you've met!" and steer the group topic somewhere neutral; you could not have known, and dwelling makes it heavier.

## Verification

Both people hold each other's name and a hook, the conversation runs without you as its switchboard, message intros had consent before names met, and the follow-up belongs visibly to them, not to you.

## Variations

- Professional networking events run this recipe on loop; the double opt-in rule matters most where the ask is employment or money.
- Cultures with card-exchange rituals (`jp` business settings) or honorific orders formalize step 2; the hook-giving survives every formality level.

## Safety & privacy

Low risk with one line: an introduction shares personal information (names, affiliations, sometimes contact details) — the double opt-in exists because that information plus an obligation is not yours to give away.
