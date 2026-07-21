---
name: set-up-email-filters
domain: digital
locale: [generic]
interface: web
difficulty: basic
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Create email rules that label, archive, or route predictable messages so the inbox stays useful without hiding important mail.

## Preconditions

- You can sign in to the email account in a browser or full-featured mail app.
- You have examples of messages you want to filter.
- You know which messages still need inbox visibility.
- You can access spam, trash, archive, and label or folder settings.

## Steps

1. **Pick one message type.** Start with a newsletter, receipt, alert, or recurring sender instead of building many rules at once. → *Expect:* one sample email is open or selected.
2. **Choose the filter criteria.** Use sender for reliable sources, subject words for recurring notices, and recipient address for aliases. → *Expect:* the preview finds the intended messages and few unrelated ones.
3. **Decide the action.** [BRANCH: label only | label and archive | forward | delete] use label only for important mail, label and archive for low-urgency mail, and delete only for obvious junk. → *Expect:* the rule action matches how quickly you need to see the messages.
4. **Create a clear label or folder.** Use names like Newsletters, Receipts, Travel, or School instead of vague names like Misc. → *Expect:* the destination is easy to scan later.
5. **Apply the rule to matching old mail if useful.** Select the option to filter existing conversations only after checking the preview. → *Expect:* old matching messages move or gain labels as expected.
6. **Keep subscriptions separate from filters.** For unwanted legitimate marketing, use unsubscribe first; filter only if unsubscribe fails or you still need records. → *Expect:* future unwanted mail should decrease rather than just disappear.
7. **Create a newsletter folder.** Send non-urgent reading to a newsletter label or folder and archive it from the inbox. → *Expect:* newsletters remain searchable without crowding daily mail.
8. **Test with a recent message.** Search the sender or subject and confirm the label, archive state, and inbox visibility. → *Expect:* the rule affects the intended messages only.

## Decision points

- The sender uses many addresses → filter by domain or stable subject phrase instead.
- Important notices are mixed with promotions → label only, do not archive, until the criteria are precise.
- A message is spam or phishing → mark it as spam instead of making a normal filter.
- You use multiple mail apps → create server-side filters in webmail so they apply everywhere.

## Failure modes & recovery

- **F1 Important mail hidden:** detect by missing messages later found in archive or label, recover by narrowing the rule and moving messages back to inbox.
- **F2 Rule catches unrelated mail:** detect by preview or label containing wrong senders, recover by adding sender, subject, or recipient conditions.
- **F3 Duplicate filters conflict:** detect by mail getting two labels or unexpected deletion, recover by merging or disabling overlapping rules.
- **F4 Unsubscribe ignored:** detect by continued marketing after several days, recover by filtering to newsletter or spam depending on legitimacy.

## Verification

A test search shows matching messages have the intended label or folder, inbox state is correct, and unrelated messages are unaffected.

## Variations

- Gmail: use Search options, Create filter, Apply label, and Skip the Inbox.
- Outlook web: use Rules from Settings or the message menu.
- Apple Mail: local rules may run only when the app is open, so prefer provider rules for always-on filtering.

## Safety & privacy

Low risk, but bad filters can hide bills, security alerts, or legal notices. Avoid automatic delete for anything tied to money, identity, work, or travel.
