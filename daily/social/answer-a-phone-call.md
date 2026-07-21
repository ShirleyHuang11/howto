---
name: answer-a-phone-call
domain: daily
subdomain: social
locale: [generic]
interface: phone-call
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
---

## Goal

An incoming phone call is handled appropriately: answered and concluded politely with any needed information exchanged — or correctly declined — without falling for a scam call.

## Preconditions

- A phone that is ringing or about to be answered.
- Enough quiet to hear; if in a meeting/cinema/quiet car, the correct action may be to decline (see Decision points).

## Steps

1. **Glance at the caller ID before answering.** [BRANCH: known contact → answer warmly | unknown number → answer neutrally, guard up | obvious spam pattern → let it ring to voicemail] → *Expect:* you know which stance you're taking before speaking.
2. **Answer and identify the exchange.** Known: "Hi <name>." Unknown: "Hello?" and let *them* state who they are and why they're calling — you are not obliged to confirm your name to an unknown caller. → *Expect:* the caller states an identity and a purpose.
3. **Establish the purpose.** If it's unclear after their opener, ask: "What is this regarding?" → *Expect:* a concrete purpose you can act on: information, a request, a scheduling matter.
4. **Handle the substance.** Answer, take notes for anything with numbers/dates/names, and read critical details back ("So that's Tuesday the 4th at 3 pm?"). → *Expect:* both sides confirm the key facts; notes captured.
5. **Refuse sensitive disclosures to inbound callers.** Banks, tax offices, and couriers do not ask for full passwords, PINs, or one-time codes on calls *they* placed. ⚠️ *Irreversible:* a read-out 2FA code hands over the account — never read codes to any inbound caller; hang up and call the institution's official number yourself. → *Expect:* any such request is declined; legitimate callers accept the call-back offer, scammers pressure you.
6. **Close the call.** Summarize any agreed action ("I'll send that today"), exchange goodbyes, and let the closing be mutual rather than hanging up mid-sentence. → *Expect:* both parties said a closing; call ended.
7. **Act on the outcome immediately.** Calendar the appointment, write the task, or save the number with a name. → *Expect:* nothing from the call exists only in memory.

## Decision points

- Can't talk now but it's a known contact → answer briefly: "Can I call you back in an hour?" or decline with a text reply — both beat silent ignoring for relationships.
- Robocall/recorded voice → hang up without pressing any "press 1 to unsubscribe" options (they confirm live numbers).
- Caller claims emergency involving a family member and demands money/gift cards → classic scam pattern: hang up, call the family member directly.

## Failure modes & recovery

- **F1 Missed the caller's name/organization:** ask directly — "Sorry, could you repeat who's calling?"; it is never rude.
- **F2 Bad connection:** say you'll call back, hang up, and redial; don't guess at half-heard details.
- **F3 Realized mid-call it's a scam:** hang up without explanation or argument; block the number; if you disclosed anything, act on it now (change the password, call the bank).

## Verification

The call ended with a mutual close; you can state who called, why, and what was agreed; agreed actions are captured outside your head; and no code, PIN, or password was disclosed to an inbound caller.

## Variations

- Business context: answer with name/organization ("<Company>, <name> speaking"); note-taking is the default, not the exception.
- Voicemail follow-up: a missed unknown call with no voicemail rarely warrants a callback; with a voicemail, verify any callback number independently if the message requests personal data.

## Safety & privacy

Low physical risk; the real risk is social engineering. The one hard rule is step 5: identity, codes, and payment details flow only on calls *you* initiate to numbers *you* looked up.
