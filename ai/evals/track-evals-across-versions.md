---
name: track-evals-across-versions
domain: ai
subdomain: evals
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [ai/evals/measure-task-accuracy]
status: draft
last_verified: 2026-09-22
---

## Goal

You track eval results over prompt, model, data, and code versions so regressions and improvements are visible over time. Each result can be traced back to the exact configuration that produced it.

## Preconditions

- A repeatable eval runner that outputs structured results.
- Version identifiers for prompt, model, code commit or build id, dataset, and retrieval index.
- A results store such as JSONL, SQLite, warehouse table, or experiment tracker.

## Steps

1. **Define result metadata.** Record `run_id`, timestamp, dataset version, model, prompt hash, code version, index version, and scorer version. → *Expect:* every run is reproducible enough to investigate.
2. **Write normalized results.** Save per-example outcomes and aggregate metrics separately. → *Expect:* you can inspect one failure or plot trends.
3. **Add comparison logic.** Compare the latest run against a baseline and previous production version. → *Expect:* deltas and confidence intervals are computed automatically.
4. **Create trend views.** Plot key metrics by version and category, including accuracy, hallucination, latency, and cost. → *Expect:* a dashboard or generated report shows historical movement.
5. **Alert on regressions.** Set thresholds for absolute score and negative deltas. → *Expect:* failing runs are flagged in CI or messaging.
6. **Archive artifacts.** Store prompts, configs, and sample outputs for each run. ⚠️ *Data leaves your control:* if using a hosted tracker, do not upload sensitive raw prompts or outputs without approval. → *Expect:* investigation does not depend on local scratch files.

## Decision points

- Metric improves but latency worsens → decide using predeclared product priorities.
- Dataset version changes → compare within the same dataset and separately show new benchmark status.
- Regression isolated to one category → block if the category is critical even when overall score passes.

## Failure modes & recovery

- **F1 Missing version metadata:** detect null prompt or dataset version → fail the run and rerun with complete config.
- **F2 Apples-to-oranges comparison:** detect different dataset versions → label as non-comparable.
- **F3 Lost artifacts:** detect output links missing → store artifacts before reporting success.
- **F4 Dashboard hides slices:** detect overall metric stable but slice regression → add per-category alerting.

## Verification

A new eval run writes complete metadata, per-example rows, aggregate metrics, and artifacts. The comparison report identifies the baseline, computes metric deltas, and exits nonzero when configured regression thresholds are breached.

## Variations

- `local JSONL`: simplest storage for small teams.
- `warehouse`: useful for joining evals with product telemetry.
- `experiment tracker`: useful for model-training workflows and artifact browsing.

## Safety & privacy

Eval history can contain sensitive prompts, outputs, and documents. Redact before exporting to hosted tools, apply retention limits, and keep access aligned with the underlying data classification.
