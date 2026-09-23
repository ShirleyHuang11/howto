---
name: evaluate-an-agent-end-to-end
domain: ai
subdomain: agents
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [ai/agents/log-agent-traces]
status: draft
last_verified: 2026-09-22
---

## Goal

You evaluate a full agent workflow across model decisions, tool use, final answers, cost, and safety behavior. Success means a held-out test set passes defined thresholds before the agent ships.

## Preconditions

- A versioned eval dataset with representative tasks, expected outcomes, and allowed tools.
- A deterministic-ish test harness with fixed model parameters where possible and mocked external side effects.
- Trace logging is enabled so failures can be inspected by case ID.

## Steps

1. **Define end-to-end success criteria.** Specify task success, tool correctness, final-answer quality, safety blocks, latency, and cost thresholds. → *Expect:* a machine-readable eval config contains all pass/fail thresholds.
2. **Build a labeled held-out dataset.** Include normal, ambiguous, tool-failure, adversarial, and permission-gated cases. → *Expect:* each case has an ID, input, expected final state, and scoring method.
3. **Mock or sandbox side-effecting tools.** Replace email, payments, deletes, and deployments with test doubles that record intended actions. ⚠️ *Irreversible:* never run evals against production side-effecting tools unless explicitly approved and isolated. → *Expect:* eval runs create no real external writes.
4. **Run the agent with tracing and fixed config.** Record model version, prompt version, tool versions, seed if supported, and dataset version. → *Expect:* every eval result links to a trace and reproducibility metadata.
5. **Score each case programmatically.** Use exact match for state changes, schema validation for structured output, retrieval checks for citations, and calibrated LLM judges only where objective checks are insufficient. → *Expect:* each case has numeric scores and pass/fail labels.
6. **Gate release on aggregate and slice metrics.** Fail the build if overall success, safety, or key slices fall below thresholds. → *Expect:* the CI job exits nonzero when thresholds are missed.

## Decision points

- Tool-use errors dominate failures → fix tool schemas, argument repair, or retry policy before prompt tuning.
- Final answers are weak despite correct tools → improve synthesis prompt or add a critic.
- Safety cases fail → do not ship; tighten guardrails and approval gates.
- Metrics pass overall but fail a critical slice → block release for that slice even if the average looks acceptable.

## Failure modes & recovery

- **F1 Eval contamination:** detect cases copied into prompts or few-shot examples → remove contaminated cases and create a fresh holdout split.
- **F2 Flaky scores:** detect high variance across repeated runs → add deterministic checks, widen dataset, or run multiple trials.
- **F3 Judge bias:** detect LLM judge disagreeing with human labels → calibrate with a rubric and spot-check disagreements.
- **F4 Real side effect during eval:** detect external write IDs in traces → revoke test credentials and force sandbox-only tools.

## Verification

Run the eval command, for example `agent-eval run --config eval.yaml --dataset heldout.jsonl`. The run passes only if overall task success is at or above the configured threshold, safety cases are 100% passing, side-effecting tools have zero production writes, p95 latency and average cost are within budget, and every failed case has a trace link.

## Variations

- `unit-style agents`: score exact final state and tool sequence with mocks.
- `RAG agents`: require gold document recall plus grounded final citations.
- `browser or computer-use agents`: use visual or DOM assertions and run inside an isolated environment.

## Safety & privacy

Medium risk from API spend, third-party judge calls, and accidental side effects. Use sandbox credentials, redact sensitive eval data before sending to model providers, cap per-run cost, and require human review for release when safety or irreversible-action cases fail.
