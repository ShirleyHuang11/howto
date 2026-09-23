---
name: add-an-output-moderation-layer
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

Moderate model outputs before users see them, blocking or rewriting responses that violate policy while measuring safety and helpfulness impact.

## Preconditions

- A written output policy and severity actions.
- A moderation classifier, ruleset, or LLM judge that returns structured labels.
- A test set containing safe outputs, unsafe outputs, and borderline outputs.

## Steps

1. **Define output categories and actions.** Map categories to `allow`, `revise`, `refuse`, `escalate`, or `block`. → *Expect:* policy rules are machine-readable and versioned.
2. **Insert moderation after generation.** Send the candidate output plus minimal context to the moderation layer before returning it to the user. ⚠️ *Data leaves your control:* hosted moderation receives generated text and may receive user context. → *Expect:* unsafe candidate outputs are intercepted.
3. **Validate structured moderation results.** Require JSON with category, confidence, action, and explanation code. → *Expect:* malformed moderation results fail closed for high-risk categories.
4. **Apply the action deterministically.** Return the original, a safe revision, a refusal, or an escalation message based on policy. → *Expect:* every candidate output produces exactly one user-visible outcome.
5. **Evaluate moderation quality.** Compute unsafe-output recall, safe-output false-positive rate, latency, and cost. → *Expect:* critical unsafe output recall meets threshold without unacceptable overblocking.
6. **Add observability.** Log action counts, policy version, model version, and sampled redacted examples. → *Expect:* dashboards show moderation rates and drift over time.

## Decision points

- Unsafe recall below target → block more categories or add a stronger classifier before launch.
- False positives too high → revise category definitions and add benign examples.
- Rewriting changes factual meaning → prefer refusal or escalation over automatic rewrite.

## Failure modes & recovery

- **F1 Malformed moderation JSON:** detect parse or schema failure → retry once and then fail closed where severity is unknown.
- **F2 Leakage through streaming:** detect tokens sent before moderation → buffer output until moderation completes or moderate chunks with holdback.
- **F3 Unsafe rewrite:** detect rewritten answer still violates policy → run the rewrite through the same moderation layer.
- **F4 Context omission:** detect classifier misses because it lacks necessary context → pass minimal relevant context with redaction.

## Verification

The output moderation eval suite shows critical unsafe-output recall at least 0.98, safe-output false-positive rate at most 0.05, all moderation decisions validate against the schema, and streaming integration tests prove unmoderated text is not delivered.

## Variations

- `post-generation classifier`: simple to integrate; adds latency.
- `streaming moderation`: lower perceived latency; requires buffering and chunk-level tests.
- `rewrite layer`: useful for tone or privacy fixes; must be re-moderated.

## Safety & privacy

Output moderation reduces but does not eliminate harm. Avoid sending unnecessary user context to external moderators, prevent unmoderated streaming leakage, log only redacted examples, and fail closed for severe categories.
