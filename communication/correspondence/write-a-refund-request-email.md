---
name: write-a-refund-request-email
domain: communication
subdomain: correspondence
locale: [generic]
interface: web
difficulty: basic
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You request a refund in writing with enough evidence and clarity that the seller can approve, deny, or escalate it without confusion.

## Preconditions

- Order number, purchase date, amount paid, seller name, and payment method.
- Refund policy, return window, and reason for the request.
- Photos, tracking, cancellation confirmation, defect evidence, or prior support messages if relevant.

## Steps

1. **Check the refund policy first.** Confirm the deadline, condition requirements, restocking fees, and whether shipping is refundable. → *Expect:* you know the strongest basis for the request.
2. **Gather transaction evidence.** Save receipt, order page, delivery status, photos, and support history. → *Expect:* the seller can verify the purchase and problem.
3. **State the request in the subject line.** Include order number if available. → *Expect:* the email can be routed correctly.
4. **Explain the issue factually.** Describe what happened, when, and how it differs from what was promised. → *Expect:* the problem is clear without emotional language.
5. **Ask for a specific remedy.** Request refund to original payment method, replacement, store credit, or cancellation as appropriate. → *Expect:* the seller knows the exact resolution you want.
6. **Attach evidence and set a response window.** Ask for confirmation within a reasonable time, such as five to seven business days. → *Expect:* the request is complete and trackable.
7. **Send through the official support channel.** Use the merchant's portal or support address and keep a copy. → *Expect:* you receive an email, ticket, or case number.
8. **Escalate if needed.** If ignored or unfairly denied, reply with the ticket number, then consider card dispute, platform protection, or consumer agency deadlines. → *Expect:* you have a documented escalation path.

## Decision points

- Item is defective or not as described → include photos and quote the listing or order page.
- Item was never delivered → include tracking and delivery address evidence.
- You are outside the return window → explain any delay and ask for an exception, but expect discretion.
- The merchant refuses despite clear policy coverage → preserve records for payment dispute deadlines.

## Failure modes & recovery

- **F1 Missing order details:** detect a support reply asking for basics → resend order number, date, email used, and amount.
- **F2 Policy denial:** detect denial citing a deadline or exclusion → compare it to the posted policy and respond with evidence if they are wrong.
- **F3 Return lost in transit:** detect no refund after mailing → provide tracking and carrier receipt.
- **F4 Chargeback deadline missed:** detect delay beyond card-network dispute window → escalate promptly and check the issuer's deadline.

## Verification

The refund request has been submitted through the official channel, includes order details and evidence, and you have a ticket number or written confirmation showing the requested amount and remedy.

## Variations

- `subscription`: request cancellation confirmation and refund of the specific billing period.
- `travel`: cancellation rules may depend on fare class, hotel rate type, or force majeure policy.
- Template:
  "Hello, I am requesting a refund for order [number], purchased on [date] for [amount].
  The reason is [specific issue], and I have attached [evidence].
  Please refund [amount] to the original payment method or let me know what else you need by [date]."

## Safety & privacy

Medium risk because payment rights and dispute deadlines are involved. Do not send full card numbers, passwords, or unnecessary ID; keep all refund and return evidence until funds settle.
