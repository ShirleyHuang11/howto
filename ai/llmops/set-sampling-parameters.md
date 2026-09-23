---
name: set-sampling-parameters
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: [ai/llmops/call-an-llm-api]
status: draft
last_verified: 2026-09-22
---

## Goal

You choose sampling parameters that match the task and verify their effect with repeatable tests. The model output becomes as deterministic, diverse, or concise as the product requires.

## Preconditions

- A working LLM call wrapper.
- A small eval set that includes easy, ambiguous, and edge-case prompts.
- Provider documentation for supported parameters such as temperature, top_p, max tokens, stop sequences, seed, and penalties.

## Steps

1. **Classify the task type.** Mark the task as factual extraction, classification, code generation, brainstorming, summarization, or dialogue. → *Expect:* a sampling profile target such as deterministic or creative.
2. **Set conservative defaults.** For factual or schema tasks, start with low temperature such as `0` to `0.3`; for brainstorming, test higher temperature such as `0.7` to `1.0`. → *Expect:* the config file contains explicit sampling values.
3. **Cap output length.** Set `max_tokens` or equivalent from expected output length plus margin. → *Expect:* output cannot run away beyond the budget.
4. **Use stop sequences only when safe.** Add stops for known delimiters and verify they do not appear inside valid content. → *Expect:* outputs stop at intended boundaries without truncating real answers.
5. **Run a parameter sweep.** Evaluate a small grid of temperature, top_p, and max tokens on the same prompts. → *Expect:* a results table with validity, quality, diversity, length, latency, and cost.
6. **Choose and lock the profile.** Store named profiles such as `strict_json`, `concise_answer`, or `creative_ideas` in config. → *Expect:* production code references profile names instead of scattered literals.
7. **Regression-test the profile.** Re-run the eval whenever model or prompt changes. → *Expect:* output validity and quality stay above threshold.

## Decision points

- JSON or tool arguments fail validation → lower randomness and use structured output constraints.
- Outputs are repetitive or bland for ideation → increase temperature gradually and judge diversity.
- Outputs hallucinate facts → lower randomness and improve grounding rather than only changing temperature.
- Responses truncate → raise max tokens or make the prompt require shorter output.
- Provider does not support a parameter → remove it from the portable config and document branch-specific values.

## Failure modes & recovery

- **F1 Parameter ignored:** detect provider warning or unchanged behavior → verify supported API fields for the model.
- **F2 Stop sequence truncation:** detect incomplete valid output → remove or narrow the stop sequence.
- **F3 Cost blowup from max tokens:** detect long completions → lower max tokens and add concise instructions.
- **F4 Random eval flakiness:** detect inconsistent pass/fail → run multiple samples or use a seed when supported.
- **F5 Overconstrained creativity:** detect duplicate ideas across samples → raise temperature or request multiple candidates.

## Verification

Sampling is set correctly when the chosen profile passes the eval thresholds for schema validity, task quality, and cost, and a regression test confirms parameter changes alter output statistics in the expected direction, such as lower temperature reducing output variance.

## Variations

- `Anthropic`: tune `temperature`, `top_p`, `top_k` where supported, and `max_tokens`.
- `OpenAI`: tune `temperature`, `top_p`, max output tokens, penalties, and seed where supported.
- `open model`: sampler settings may include top_k, min_p, repetition penalty, and deterministic seeds.
- `structured output`: rely more on schema-constrained decoding than sampling tweaks.

## Safety & privacy

Low risk by itself, but bad sampling can produce invalid, unsafe, or costly outputs. Keep deterministic settings for compliance-sensitive tasks, cap output length, and test jailbreak and hallucination cases before changing production profiles.
