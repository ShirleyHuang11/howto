---
name: decide-few-shot-vs-zero-shot
domain: ai
subdomain: prompting
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Choose zero-shot or few-shot prompting using a labeled development set, so the selected prompt has a measured accuracy and cost profile instead of relying on intuition.

## Preconditions

- You can call at least one chat or text-generation model through an SDK or API.
- A small labeled set of 30-100 representative inputs with expected outputs.
- A scoring script for the task, such as exact match, schema validity plus field F1, or a rubric judge.

## Steps

1. **Define the task contract.** Write the input fields, allowed output labels or schema, and the metric you will optimize. → *Expect:* a `task.yaml` or equivalent with output constraints and a scoring function name.
2. **Create a zero-shot prompt.** State the role, task, constraints, and output format without examples. → *Expect:* one prompt template that renders for every dev example.
3. **Create a few-shot prompt.** Add 3-8 diverse, correctly labeled examples before the live input; keep the same output format as zero-shot. → *Expect:* a second prompt template with examples covering common edge cases.
4. **Run both prompts on the same dev set.** [BRANCH: Anthropic | OpenAI | open model] Use temperature `0` or the provider's most deterministic setting and log raw responses, latency, token counts, and cost. ⚠️ *Data leaves your control:* if using an external API, redact secrets and PII before sending examples. → *Expect:* two result files with one row per example and prompt variant.
5. **Score correctness and format compliance.** Parse outputs, validate schemas, and compute the primary metric plus invalid-output rate. → *Expect:* a table with `accuracy`, `invalid_rate`, `avg_input_tokens`, `avg_output_tokens`, and `avg_latency_ms`.
6. **Choose the simpler prompt unless few-shot wins materially.** Require a predeclared margin, such as `+3 percentage points` accuracy or `+0.05` macro-F1, to justify the extra tokens. → *Expect:* a selected prompt variant and a recorded reason.
7. **Lock a regression test.** Save the selected prompt and dev set in version control or your prompt registry, with the measured baseline. → *Expect:* CI can rerun the evaluation and compare against the baseline.

## Decision points

- Few-shot improves metric by less than the margin → use zero-shot and save token budget.
- Few-shot improves rare classes but hurts common classes → use stratified metrics or add better examples.
- Both variants fail format validation → fix output constraints before comparing task quality.
- Dev set is smaller than 30 examples → treat the result as directional and gather more labels.

## Failure modes & recovery

- **F1 Example leakage:** detect examples copied into the output → add a delimiter around examples and explicitly mark the live input.
- **F2 Overfitted examples:** detect high dev score but low held-out score → rotate examples and evaluate on a separate holdout.
- **F3 Token budget blowup:** detect few-shot prompt exceeding context or cost limits → reduce examples, shorten examples, or switch to zero-shot.
- **F4 Invalid labels:** detect labels outside the allowed set → use constrained decoding or schema validation with retry.

## Verification

Run an evaluation script that renders both prompts for the same labeled set. The selected variant must have `invalid_rate <= 0.02`, meet or beat the baseline metric, and, if few-shot is selected, improve the primary metric by at least the predeclared margin while staying under the per-request token budget.

## Variations

- `classification`: compare macro-F1 and per-class recall, not just accuracy.
- `extraction`: compare JSON-schema validity plus field-level precision, recall, and F1.
- `local model`: repeat with a larger few-shot set because smaller open models often benefit more from demonstrations.

## Safety & privacy

This is usually low risk, but examples can contain real user data. Redact PII before sending prompts to third-party APIs, cap evaluation cost, and avoid putting proprietary examples in prompts that may be logged outside your infrastructure.
