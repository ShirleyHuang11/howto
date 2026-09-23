---
name: add-a-critic-to-an-agent
domain: ai
subdomain: agents
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Your agent uses a critic step to catch factual, schema, safety, and tool-use errors before final output or action. Success means the critic improves measured quality without becoming an unbounded extra loop.

## Preconditions

- A draft-producing agent step and a way to inspect tool results, citations, and final output.
- A critic prompt or model configuration with a clear rubric.
- An eval set with known errors or quality labels.

## Steps

1. **Define the critic rubric.** Include checks for instruction compliance, factual grounding, citation support, schema validity, safety, and missing user requirements. → *Expect:* the rubric is represented as structured fields with pass/fail or numeric scores.
2. **Provide evidence, not hidden reasoning.** Send the draft, relevant tool outputs, citations, and user requirements to the critic; exclude secrets and unnecessary private context. ⚠️ *Data leaves your control:* if the critic is a third-party model, redact sensitive content before sending. → *Expect:* critic input contains only fields required by the rubric.
3. **Require structured critic output.** Return `{"pass": boolean, "issues": [...], "required_fixes": [...]}` with severity and evidence references. → *Expect:* critic responses parse and validate.
4. **Apply bounded revision.** If the critic fails the draft, run one or two revision cycles with the required fixes; do not loop indefinitely. → *Expect:* revision count never exceeds the configured maximum.
5. **Gate high-severity issues.** Block final output or action if the critic flags unsupported claims, invalid schema, unsafe content, or missing approval. → *Expect:* high-severity failures stop with a typed reason.
6. **Measure critic value.** Compare agent performance with and without the critic on a held-out set. → *Expect:* quality improves enough to justify added latency and cost.

## Decision points

- Draft must be strict JSON → run deterministic schema validation before or alongside the critic.
- Critic flags fixable quality issues → revise once and recheck.
- Critic flags missing evidence or unsafe action → stop and retrieve evidence or request approval.
- Critic adds cost without metric gains → narrow the rubric or disable for low-risk tasks.

## Failure modes & recovery

- **F1 Critic rubber-stamps:** detect high pass rate on seeded bad drafts → sharpen rubric and include negative examples.
- **F2 Critic overblocks:** detect many false positives → calibrate severity thresholds and add deterministic validators.
- **F3 Infinite revise-critic loop:** detect repeated revisions → enforce `max_critic_rounds`.
- **F4 Critic hallucinated issue:** detect issue without evidence reference → require evidence IDs and ignore unsupported critic claims.

## Verification

Run an A/B eval on held-out cases with seeded citation errors, schema errors, and unsafe actions. The critic-enabled agent must reduce severe errors by the configured amount, keep p95 latency and cost within budget, validate every critic JSON response, and stop rather than act on any high-severity unresolved issue.

## Variations

- `same-model critic`: simpler and cheaper, but more correlated with the draft's blind spots.
- `stronger-model critic`: better for high-stakes review; use selectively due to cost.
- `deterministic critic`: use validators for schemas, citations, permissions, and numeric checks before model judgment.

## Safety & privacy

Medium risk because a critic may receive sensitive drafts and evidence and may block or approve important actions. Redact critic inputs, cap revision loops, rely on deterministic checks for hard constraints, and require human approval for irreversible actions even if the critic passes them.
