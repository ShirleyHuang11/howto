---
name: respond-to-a-buyer-message
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

Respond to a buyer message accurately, safely, and within marketplace or store service expectations.

## Preconditions

- Access to the buyer message, order details, product listing, and store policies.
- Permission to answer, refund, replace, discount, or escalate if needed.
- Awareness of platform rules about off-platform contact and prohibited claims.

## Steps

1. **Read the full thread and order record.** Check the buyer's question, order status, shipping details, and prior promises. → *Expect:* the buyer's issue and context are clear.
2. **Classify the message.** Identify whether it is a product question, shipping issue, return request, complaint, scam attempt, or policy-sensitive topic. → *Expect:* the response path is known.
3. **Verify facts before replying.** Check inventory, tracking, delivery estimate, return window, sizing, compatibility, or warranty terms. → *Expect:* the answer is based on current records.
4. **Draft a concise response.** Address the buyer by issue, answer directly, and state the next action or timeline. → *Expect:* the message is clear and does not overpromise.
5. **Keep the conversation on-platform.** Decline requests for external payment, private links, gift cards, or moving the dispute elsewhere. → *Expect:* the reply complies with platform protection rules.
6. **Send or escalate.** ⚠️ *Irreversible:* before sending, confirm order number, amount, and promises because messages become part of the dispute record. → *Expect:* the buyer receives the response or the ticket is assigned to the right team.
7. **Set a follow-up reminder if needed.** Track promised shipping updates, refunds, replacements, or supplier answers. → *Expect:* unresolved buyer issues have an owner and due time.

## Decision points

- Buyer asks for a refund → check policy and order status before promising money.
- Buyer reports safety issue → escalate immediately and stop selling affected inventory if credible.
- Buyer asks to pay outside the platform → refuse and keep all transactions protected.

## Failure modes & recovery

- **F1 Wrong order referenced:** detect buyer correction or mismatch → apologize, correct the record, and resend accurate information.
- **F2 Scam pressure:** detect overpayment, off-platform link, or courier trick → do not click links or move payment; report if platform supports it.
- **F3 Late response penalty:** detect service-level warning → prioritize open buyer messages and use templates for common cases.
- **F4 Promise cannot be met:** detect inventory or carrier failure → update the buyer quickly with realistic options.

## Verification

The buyer has received an accurate on-platform reply, any promised action is recorded with an owner, and no prohibited off-platform payment or private data exchange occurred.

## Variations

- `marketplace`: response time can affect seller metrics, so answer within the platform's service window.
- Direct store: use helpdesk macros but personalize order-specific facts.

## Safety & privacy

Medium risk because messages can trigger refunds, disputes, or fraud. Keep payment on-platform, share only order-relevant data, and confirm facts before promising compensation.
