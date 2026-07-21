---
name: spot-a-phone-scam
domain: digital
locale: [generic]
interface: phone-call
difficulty: basic
est_time: 5min
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

A suspicious phone call is handled without giving money, codes, account access, or private information, and legitimate issues are verified by calling back through official numbers.

## Preconditions

- You received an unexpected call, voicemail, or robocall.
- The caller claims urgency, authority, a prize, a family emergency, tech support, debt, delivery, bank fraud, or government action.
- You can find official contact information independently.

## Steps

1. **Pause the conversation.** Do not answer security questions, confirm personal details, or follow instructions while surprised. → *Expect:* the caller has not received useful information.
2. **Listen for pressure and secrecy.** Scam callers push fear, time limits, "do not tell anyone", arrest threats, account closure, or family emergency stories. → *Expect:* pressure makes the call untrusted.
3. **Listen for payment tells.** Gift cards, crypto, wire transfer, payment apps, remote access software, and one-time codes are red flags. → *Expect:* any such demand is treated as scam evidence.
4. **Refuse remote control or code sharing.** Do not install apps, read verification codes, or approve login prompts for a caller. → *Expect:* no account or device access has been granted.
5. **End the call politely or silently.** Say you will call back through the official number, then hang up. → *Expect:* the caller cannot keep escalating pressure.
6. **Find the official number yourself.** Use the number on your card, statement, official website, app, or prior verified contact. → *Expect:* the number is independent of the incoming call or voicemail.
7. **Call back and verify.** Ask whether the claimed issue exists. → *Expect:* the real organization confirms, denies, or documents next steps.
8. **Report and block scam calls.** Use phone blocking, carrier spam tools, and appropriate fraud reporting channels. → *Expect:* the number is blocked and the call is recorded for reference.

## Decision points

- [BRANCH: caller claims emergency | routine issue] Emergencies still need independent verification through another family member, official dispatch, hospital, bank, or agency number.
- Caller says not to hang up → that instruction itself is a scam tell.
- Caller knows personal information → continue to verify independently because leaked data is common.
- Caller is from your bank about fraud → hang up and call the number on the card or in the banking app.

## Failure modes & recovery

- **F1 Shared a one-time code:** detect code read aloud or approved prompt; recover by changing password, signing out sessions, and calling the account provider.
- **F2 Sent money:** detect transfer, gift card purchase, crypto payment, or wire; recover by contacting the payment provider immediately and reporting fraud.
- **F3 Installed remote-access software:** detect new support app or screen sharing; recover by disconnecting internet, uninstalling the app, and getting trusted security help.
- **F4 Real call mishandled:** detect official callback confirms a real issue; recover by continuing through the official number, not the original caller.

## Verification

No money, codes, remote access, or private information were given to the incoming caller, and any claimed issue was checked through an official callback number.

## Variations

- `voicemail`: do not call back the number in the voicemail unless it matches an official source.
- Elder support: set a family rule that money emergencies require a callback to a known number.
- Business calls: verify payment or vendor changes through existing internal contacts.

## Safety & privacy

High risk because phone scams combine pressure with isolation. Hanging up is a valid security action, and official callback verification beats caller ID, which can be spoofed.
