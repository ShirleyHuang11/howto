---
name: decide-fine-tune-vs-rag-vs-prompt
domain: ai
subdomain: finetuning
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

You choose prompt engineering, retrieval, or fine-tuning using evidence from a labeled task set. The decision is backed by measurable failure categories, quality scores, latency, and cost.

## Preconditions

- A representative eval set with inputs, expected outputs or rubrics, and business-critical edge cases.
- You can call at least one baseline model through an API or local runtime.
- A spreadsheet or notebook for logging quality, latency, and cost per option.

## Steps

1. **Define the target behavior and acceptance threshold.** Write the task contract, allowed sources, output format, and a pass threshold such as `exact_match >= 0.90`, `judge_score >= 0.80`, or `citation_recall@3 >= 0.90`. → *Expect:* a machine-checkable metric and threshold.
2. **Label the current failures.** Run the baseline prompt on 50-200 examples and tag failures as `format`, `missing_knowledge`, `style`, `reasoning`, `tool_use`, or `policy`. → *Expect:* a table where every failed example has one primary failure tag.
3. **Try the cheapest prompt fix first.** Add concise instructions, examples, schema constraints, and validation retries without changing the model or adding data infrastructure. → *Expect:* a new eval result with quality, p50/p95 latency, and mean input/output tokens.
4. **Test retrieval when failures require fresh or private knowledge.** [BRANCH: vector search | keyword search | hybrid search] Index the required documents, retrieve top-k chunks, and rerun the eval with cited context. → *Expect:* retrieval metrics such as `recall@3` and task quality improve on `missing_knowledge` failures.
5. **Test fine-tuning only for repeated behavior not solved by context.** Prepare 100-1000 high-quality examples for style, format, classification boundaries, or tool-call selection; hold out at least 20%. ⚠️ *Data leaves your control:* if using a hosted fine-tuning API, redact secrets and confirm training-data retention terms first. → *Expect:* a training/validation split and a dry-run data validation report with no schema errors.
6. **Compare options on a decision matrix.** Score prompt, RAG, and fine-tune by quality lift, maintenance burden, latency, cost, data exposure, and rollback ease. → *Expect:* one option clears the threshold with the smallest operational burden.
7. **Write the decision record.** Record the chosen approach, rejected alternatives, metrics, and conditions that would trigger reconsideration. → *Expect:* a short ADR or notebook cell with links to eval artifacts.

## Decision points

- Failures are mostly formatting or tone → improve prompting or constrained decoding before fine-tuning.
- Failures are missing, changing, or customer-specific facts → use RAG before fine-tuning.
- Failures are stable classification boundaries or repeated tool-call patterns → consider fine-tuning.
- No option clears the acceptance threshold → do not ship; expand data, change model, or narrow scope.
- Fine-tuning improves quality but worsens latency or cost beyond budget → prefer prompt/RAG or a smaller model.

## Failure modes & recovery

- **F1 Misdiagnosed knowledge gap:** detect by examples answerable only from private docs → build retrieval and measure `recall@k` before training.
- **F2 Tiny eval set overfits the decision:** detect large score swings when adding examples → increase held-out cases and stratify by failure type.
- **F3 Fine-tune memorizes examples:** detect high train score and low validation score → deduplicate, add validation data, and reduce training epochs.
- **F4 RAG hides bad retrieval:** detect plausible answers with wrong citations → require cited chunk ids and check answer support against retrieved text.
- **F5 Cost surprise:** detect projected monthly spend over budget → estimate per-request tokens and traffic before choosing.

## Verification

The decision is complete when a script or notebook computes all candidate metrics on the same held-out eval set and writes a table where the selected option meets the declared quality threshold, stays within the latency and cost budget, and has a recorded decision rationale.

## Variations

- `Anthropic`: compare Claude Sonnet for baseline and Claude Haiku-class models for lower-cost routing.
- `OpenAI`: compare a frontier model baseline, a smaller model with RAG, and a fine-tuned smaller model when available.
- `open model`: evaluate local inference cost, GPU memory, and serving throughput alongside quality.
- `regulated data`: prefer prompt/RAG inside your infrastructure unless a hosted provider contract allows training on the data.

## Safety & privacy

Medium risk because the decision may route private data into retrieval stores or hosted training. Redact PII before external calls, keep a data inventory, cap experiment spend, and require human review before launching a paid fine-tune or exposing customer data to a third-party API.
