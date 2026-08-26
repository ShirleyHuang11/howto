---
name: handle-an-order-dispute
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: advanced
est_time: 1h
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You respond to an ecommerce order dispute with evidence, policy-aligned resolution, and no duplicate refund or missed deadline.

## Preconditions

- Dispute notice, order number, deadline, dispute reason, and payment processor or marketplace case ID.
- Access to order history, tracking, customer messages, fraud signals, and refund records.
- Store policy for refunds, replacements, chargebacks, and goodwill resolutions.

## Steps

1. **Record the dispute deadline.** Open the case and note response due date, reason code, disputed amount, and required evidence type. → *Expect:* a clear deadline and case scope.
2. **Freeze duplicate actions.** Check whether refunds, replacements, or return requests are already open and avoid separate compensation outside the dispute. → *Expect:* one coordinated resolution path.
3. **Gather order evidence.** Collect order confirmation, billing/shipping match, IP/device fraud checks if available, fulfillment record, tracking, delivery proof, and customer messages. → *Expect:* an evidence packet tied to the disputed order.
4. **Match evidence to reason code.** [BRANCH: item not received | not as described | unauthorized | duplicate charge] Select proof relevant to the specific claim rather than uploading everything. → *Expect:* the response directly answers the dispute reason.
5. **Decide contest or accept.** Compare evidence strength, customer history, cost, policy, and likelihood of winning. → *Expect:* a documented decision to fight, refund, or settle.
6. **Submit the response or resolution.** ⚠️ *Irreversible:* before submitting, confirm case ID, amount, evidence files, customer, and whether accepting creates a refund or fee. → *Expect:* the dispute portal shows a submitted response or accepted liability.
7. **Message the customer only if appropriate.** Keep communication factual and avoid pressuring them to withdraw a chargeback. → *Expect:* any customer message is logged and consistent with platform rules.
8. **Monitor outcome.** Track provisional credit, processor decision, fees, and order status until the case closes. → *Expect:* the dispute is resolved, won, lost, or awaiting processor review.
9. **Update prevention controls.** Adjust fraud filters, shipping signature rules, product descriptions, or support workflows based on the root cause. → *Expect:* one specific change reduces repeat disputes.

## Decision points

- Tracking shows no delivery scan → refund or replace may be stronger than contesting.
- Unauthorized claim has high fraud signals → submit fraud-screening, AVS/CVV, and delivery evidence.
- Not-as-described claim matches a real listing error → accept responsibility and fix the page.
- Deadline is too close → submit the strongest complete evidence now rather than waiting for perfect data.

## Failure modes & recovery

- **F1 Missed response deadline:** detect case auto-lost or deadline passed → document loss, update alerts, and seek processor appeal only if allowed.
- **F2 Duplicate refund:** detect manual refund plus chargeback debit → contact processor/platform with transaction IDs to prevent double loss if possible.
- **F3 Irrelevant evidence:** detect weak response rejected for wrong proof → map future evidence to reason code and use templates.
- **F4 Customer harassment risk:** detect staff asking customer to cancel chargeback improperly → stop contact and keep communication within policy.

## Verification

The dispute case has a submitted response or accepted resolution before the deadline, evidence is stored with the order, no duplicate refund is pending, and the final outcome is tracked.

## Variations

- Marketplace dispute: platform may require specific uploads and customer-facing replies.
- Card chargeback: processor rules and reason codes control evidence requirements.
- PayPal/wallet dispute: delivery proof and message history inside the wallet may matter most.

## Safety & privacy

Medium risk because disputes affect money and expose customer data. Use only necessary evidence, avoid sensitive unrelated information, and never pressure a customer outside allowed dispute procedures.
