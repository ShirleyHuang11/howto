---
name: spot-a-scam-text-message
domain: digital
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 5min
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

A suspicious text message is identified as scam or legitimate without clicking its link, and scam messages are reported and blocked.

## Preconditions

- You received an unexpected SMS, MMS, RCS, or messaging-app text.
- The message asks for action, money, login, delivery fees, tolls, account verification, or personal details.
- You can contact the supposed sender through an official app, website, or phone number.

## Steps

1. **Stop before tapping anything.** Treat links, attachments, and phone numbers in the message as untrusted. → *Expect:* no link has opened and no reply has been sent.
2. **Read the pressure pattern.** Look for urgency, threats, prizes, failed delivery, unpaid toll, bank lock, tax refund, or "reply YES" prompts. → *Expect:* pressure or reward language raises suspicion.
3. **Inspect the sender and link preview.** Long-press only if your phone previews safely; otherwise do not interact. → *Expect:* the sender is a short code, unknown number, or spoofable name, and any link domain can be judged.
4. **Compare against your real account.** Open the company's official app or type its website yourself. → *Expect:* the real account either confirms the issue or shows nothing is pending.
5. **Verify through an official channel.** Call the number on your card, statement, delivery account, or government website, not the text. → *Expect:* confirmation comes from a source independent of the message.
6. **Do not reply to scam texts.** Replying can confirm your number is active. → *Expect:* the conversation remains unanswered.
7. **Report and block.** Use the phone's Report Junk/Spam option or forward SMS scams to the carrier reporting number where available, then block the sender. → *Expect:* the thread is marked reported or the sender is blocked.
8. **Act if you already clicked or entered data.** Change affected passwords, enable 2FA, contact the bank/card issuer, and watch accounts. → *Expect:* exposed accounts are secured through official apps or websites.

## Decision points

- [BRANCH: you have an account with the sender | you do not] Having an account only means verify independently; not having one usually makes the text disposable.
- Text asks for gift cards, crypto, wire transfer, or payment app transfer → treat as scam and do not pay.
- Text contains a real personal detail → still verify independently, because breached data is commonly used in scams.
- Delivery or toll message arrives near a real trip → check the official carrier, store, toll, or postal account yourself.

## Failure modes & recovery

- **F1 Clicked the link:** detect opened page or app; recover by closing it, not entering data, and checking accounts through official channels.
- **F2 Entered password or code:** detect submitted login or one-time code; recover by changing the password, revoking sessions, and enabling 2FA immediately.
- **F3 Paid the scam:** detect card, bank, gift card, crypto, or payment app transfer; recover by contacting the payment provider quickly and reporting fraud.
- **F4 Blocked a legitimate alert:** detect real account shows the issue; recover by using the official app or website, not by unblocking and following the original text.

## Verification

No scam link was used for login or payment, the issue was checked through an official channel, and scam messages were reported and blocked.

## Variations

- `messaging-app`: report inside WhatsApp, Signal, Messenger, or similar apps, then block the sender.
- Two-factor codes: never share a one-time code with anyone who contacted you first.
- Work phones: forward suspicious texts to the security team if company policy provides a reporting path.

## Safety & privacy

High risk because smishing can steal credentials, money, and verification codes. The rule is simple: do not click, do not reply, and verify from your own trusted route.
