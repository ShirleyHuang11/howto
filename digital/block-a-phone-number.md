---
name: block-a-phone-number
domain: digital
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 5min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Calls and messages from a specific phone number are blocked on your phone, and obvious spam can also be reported through the platform or carrier.

## Preconditions

- The unwanted number appears in your recent calls, messages, voicemail, or contacts.
- You understand that blocking is per device or account and may not stop calls from new spoofed numbers.

## Steps

1. **Open the number source.** [BRANCH: call log | messages | contacts] start from Recents, the conversation thread, voicemail, or the contact card. → *Expect:* the exact number or contact is visible.
2. **Confirm the number is the one to block.** Check area code, name, and recent time so you do not block a legitimate contact by mistake. → *Expect:* the unwanted caller is identified.
3. **Open the info or details screen.** On iPhone, tap the info button or contact card; on Android, tap the number, details, or three-dot menu depending on the phone app. → *Expect:* blocking or spam options appear.
4. **Block the number.** Choose Block Caller, Block/report spam, or Block number, then confirm. → *Expect:* the phone shows the number as blocked.
5. **Report spam when appropriate.** If the call or text was scam, robocall, phishing, or harassment, use Report Junk, Report Spam, or the carrier spam option when shown. → *Expect:* the report is submitted without needing to reply to the sender.
6. **Check message handling.** Know that blocked callers may still leave voicemail in a blocked folder, and texts may be hidden rather than visibly rejected. → *Expect:* you know where blocked items would appear if needed.
7. **Repeat across linked devices if needed.** Tablets, computers, messaging apps, and carrier services may have separate block lists. → *Expect:* the block applies where you actually receive calls or messages.

## Decision points

- Unknown caller but not repeated → silence unknown callers or use spam filtering instead of blocking one spoofed number.
- Harassment or threats → save evidence before blocking and consider carrier, employer, school, or law-enforcement reporting.
- Business line or shared phone → confirm with the account owner before blocking a customer or vendor.
- Caller uses many numbers → enable carrier spam protection and app-level filters in addition to blocking.

## Failure modes & recovery

- **F1 Block option is hard to find:** detect: details screen lacks Block, recover: open the Phone app's Recents list or Messages thread and use the three-dot menu.
- **F2 Calls still arrive:** detect: same person reaches you from different numbers, recover: use silence unknown callers, carrier spam tools, or stricter Do Not Disturb rules.
- **F3 Legitimate contact was blocked:** detect: expected calls or texts stop, recover: open Blocked Contacts or Blocked Numbers and unblock the contact.
- **F4 Voicemail still appears:** detect: blocked voicemail lands in a filtered folder, recover: delete it without listening if unwanted and ask the carrier about voicemail blocking.
- **F5 Spam report sends content:** detect: the phone warns that message content may be shared, recover: cancel if sensitive or report only through the carrier.

## Verification

The phone's blocked list includes the exact number, and new calls or messages from that number no longer appear in the normal inbox or call flow.

## Variations

- `ios`: Phone, Recents, info button, Block Caller; Messages uses the sender card and Info.
- `android`: Phone app labels vary, but Recents, number details, and Block/report spam is the common path.
- `whatsapp`: Blocking in WhatsApp only affects WhatsApp calls and messages, not cellular calls.
- `carrier`: Carrier spam apps can filter spoofed robocalls before the phone receives them.

## Safety & privacy

Blocking usually does not notify the caller directly, but they may infer it from failed calls or missing replies. For threats, stalking, or legal issues, preserve screenshots, call logs, voicemails, and message exports before cleaning anything up.
