---
name: set-up-voicemail
domain: digital
locale: [generic]
interface: phone-call
difficulty: basic
est_time: 15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Your voicemail answers missed calls with a clear greeting, has a private PIN, notifies you when a message arrives, and has enough space for new messages.

## Preconditions

- Your phone can make calls on the mobile network.
- You know your carrier account PIN or phone unlock code if asked.
- You are somewhere quiet enough to record a short greeting.

## Steps

1. **Open voicemail setup.** In the Phone app, open Voicemail or press and hold `1` to call the voicemail system. → *Expect:* voicemail opens or a recorded setup menu answers.
2. **Create or confirm the PIN.** Choose a PIN that is not your birthday, phone number, or a repeated digit pattern. → *Expect:* the system accepts the PIN and asks for the next setup item.
3. **Record a short greeting.** Say your name and that callers should leave a message; avoid explaining why you missed the call. → *Expect:* playback sounds clear and includes the right name.
4. **Save the greeting.** [BRANCH: custom greeting | default greeting] keep the custom greeting if it sounds professional, or use the default greeting if you need privacy. → *Expect:* the voicemail menu marks the chosen greeting as active.
5. **Turn on message notifications.** In Phone or carrier voicemail settings, allow voicemail alerts, badges, and transcription if you want it. → *Expect:* missed voicemail messages can show a notification.
6. **Check existing messages.** Play old messages, write down anything needed, then archive or delete messages you no longer need. → *Expect:* the inbox list is short and current.
7. **Fix a full mailbox.** Delete old saved messages, then open the deleted or trash folder and clear it if your carrier has one. → *Expect:* the mailbox storage warning disappears or the message count drops.
8. **Test from another phone.** Call your number, let it go to voicemail, leave a short test, then retrieve it. → *Expect:* the greeting plays, the test message arrives, and you can play it back.

## Decision points

- You do not want strangers hearing your name → use the default greeting or record only your phone number.
- The voicemail app and long-press `1` show different inboxes → use the carrier voicemail reached by long-press `1` as the source of truth.
- You receive many work calls → choose a custom greeting that includes a callback expectation, such as leaving a name, number, and reason.

## Failure modes & recovery

- **F1 Forgot PIN:** detect when the voicemail system rejects the code, recover by resetting the voicemail PIN through carrier account settings or support.
- **F2 Greeting will not save:** detect when the old greeting still plays, recover by rerecording in a quieter place and staying under the carrier time limit.
- **F3 No notification appears:** detect after the test message arrives only inside voicemail, recover by allowing Phone app notifications and checking carrier visual voicemail settings.
- **F4 Mailbox still full:** detect when callers hear the mailbox is full, recover by clearing deleted messages and saved messages, then wait a few minutes for carrier storage to update.

## Verification

A test caller hears the active greeting, can leave a message, and your phone shows or lists that message while the mailbox has room for more.

## Variations

- `iphone`: Phone > Voicemail usually supports visual voicemail, greeting, and password options in one place if the carrier supports it.
- `android`: labels vary by Phone app and carrier; long-press `1` is the most common fallback.
- `work-phone`: follow employer rules for greeting wording and retention before deleting messages.

## Safety & privacy

Voicemail can contain private names, health details, financial details, and callback numbers. Keep the PIN private, delete messages you no longer need, and do not include travel plans or sensitive schedule details in the greeting.
