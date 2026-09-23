---
name: add-a-usage-policy-check
domain: ai
subdomain: safety
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Check each request against your product and provider usage policy before the LLM performs work, with auditable allow/block/escalate decisions.

## Preconditions

- A current usage policy covering prohibited content, regulated domains, automation limits, and user eligibility.
- A request schema with user identity, task type, input content, jurisdiction if relevant, and requested tools.
- A classifier or rules engine that returns structured policy decisions.

## Steps

1. **Convert policy into machine rules.** Map policy clauses to categories, examples, severity, and allowed actions. → *Expect:* a versioned policy config can be loaded by the app.
2. **Collect minimal decision context.** Pass only needed fields such as task type, user role, content summary, and requested tool. → *Expect:* the checker has enough context without unnecessary PII.
3. **Run the policy check.** [BRANCH: deterministic rules | classifier | LLM policy judge] Evaluate before model calls or tool execution. ⚠️ *Data leaves your control:* hosted policy checks receive request text and metadata. → *Expect:* one structured decision: `allow`, `block`, `escalate`, or `clarify`.
4. **Enforce the decision.** Block prohibited requests, ask clarifying questions for ambiguous ones, and allow permitted requests to proceed. → *Expect:* prohibited requests never reach the expensive or risky action path.
5. **Evaluate on policy cases.** Test each policy category with positive, negative, and borderline examples. → *Expect:* policy accuracy and false-positive rates are reported per category.
6. **Log decision provenance.** Store policy version, rule/classifier version, decision, and reason code. → *Expect:* decisions can be audited and reproduced.

## Decision points

- Category accuracy below threshold → add examples, clarify policy text, or route category to human review.
- Policy changes upstream → update config and rerun full policy regression suite.
- Request is in a regulated domain → require specialized gating, disclaimers, or licensed-human review as applicable.

## Failure modes & recovery

- **F1 Policy drift:** detect provider or product policy changed but config did not → schedule policy review and block deployment on stale versions.
- **F2 Missing context:** detect wrong decision because user role/tool was absent → make required context explicit in the request schema.
- **F3 Overbroad block:** detect legitimate requests blocked → add allowed examples and refine categories.
- **F4 Enforcement gap:** detect blocked decision but downstream call still happened → add integration tests around the gate.

## Verification

The policy-check test suite validates every decision JSON against the schema, achieves at least 0.95 macro accuracy on labeled policy cases, records policy version for every decision, and integration tests prove blocked requests do not call the model or tools.

## Variations

- `rules engine`: best for clear product limits and eligibility checks.
- `classifier`: useful for content-heavy policy categories.
- `LLM policy judge`: flexible for nuanced cases; calibrate with human labels and pin versions.

## Safety & privacy

Keep the policy current, minimize context sent to third-party checkers, preserve auditability, and avoid using policy checks as the only protection for high-risk tool actions.
