---
name: clean-up-your-inbox
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Your inbox contains only messages that still need attention, while older mail is archived, filtered, or unsubscribed from without losing important records.

## Preconditions

- You can access your email account on web or mobile.
- You have at least 30 minutes for the first sweep.
- You know any labels, folders, or categories you already rely on.

## Steps

1. **Sort by newest first.** Open the inbox and keep the default recent view so you see current obligations first. → *Expect:* the top of the inbox reflects recent mail.
2. **Do a quick sweep.** Select obvious newsletters, receipts, alerts, and completed threads from the last few pages. → *Expect:* a batch of low-value messages is selected.
3. **Archive instead of deleting.** Move selected messages to Archive or All Mail unless they are spam or truly unwanted. → *Expect:* the inbox count drops while search can still find the messages.
4. **Unsubscribe from repeat noise.** Open recurring senders you no longer read and use the unsubscribe link or built-in unsubscribe button. → *Expect:* the sender confirms removal or says it may take a few days.
5. **Create simple folders or labels.** [BRANCH: folders | labels] make only broad containers such as Receipts, Travel, Work, School, or Action. → *Expect:* the list is short enough to remember.
6. **Add filters for predictable mail.** Route receipts, statements, newsletters, or alerts to labels and optionally skip the inbox. → *Expect:* future matching messages file themselves.
7. **Process action mail.** For each remaining message, reply, turn it into a task, schedule time, or leave it in the inbox only if it truly needs action. → *Expect:* the inbox is mostly actionable.
8. **Set an inbox-zero-ish rule.** Pick a sustainable target, such as under 20 messages or no unread messages, instead of chasing perfection. → *Expect:* you have a clear stopping point for routine cleanup.

## Decision points

- You are nervous about losing mail → archive, do not delete, and rely on search.
- A sender keeps returning after unsubscribe → mark as spam only if the messages are unsolicited or deceptive.
- You have thousands of messages → clean by sender or category first, not message by message.

## Failure modes & recovery

- **F1 Important email disappeared:** detect when a needed thread is not in the inbox, recover by searching All Mail or Archive and moving it back.
- **F2 Filter catches too much:** detect when unrelated messages skip the inbox, recover by narrowing the sender, subject, or keyword rule.
- **F3 Unsubscribe link looks suspicious:** detect mismatched domains or odd login prompts, recover by using the email app's unsubscribe button or blocking the sender.
- **F4 Cleanup stalls:** detect when you are reading every message, recover by batching old mail by sender and archiving whole groups.

## Verification

The inbox shows only current action items or your chosen small threshold, and at least one recurring noise source is unsubscribed or filtered.

## Variations

- `gmail`: Archive removes the Inbox label; labels can coexist, so one message can be both Receipts and Travel.
- `outlook`: Archive and folders are separate destinations; Sweep can move or delete repeat sender mail.
- `work-email`: follow retention rules and avoid deleting records that may be required later.

## Safety & privacy

Email can be a legal and financial record. Use archive for uncertainty, delete only spam or messages you are sure you do not need, and be careful with unsubscribe links from suspicious senders.
