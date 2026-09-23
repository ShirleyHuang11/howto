---
name: build-an-eval-set
domain: ai
subdomain: evals
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

You create a representative, versioned evaluation set with inputs, expected behavior, metadata, and machine-checkable labels. The eval set is ready to run in CI or a notebook and catches real product failures rather than toy cases.

## Preconditions

- A clear task definition, target users, and failure types you care about.
- Access to safe sample logs, synthetic examples, or domain documents; redact PII before use.
- A tabular format such as JSONL or CSV and a schema validator such as `jsonschema` or `pydantic`.

## Steps

1. **Define the eval contract.** Write the fields each example must contain, such as `id`, `input`, `expected`, `category`, `source`, and `must_not`. → *Expect:* a documented schema with required fields and allowed category values.
2. **Sample realistic cases.** Pull examples from production logs only after redaction, support tickets, hand-written edge cases, and synthetic adversarial prompts. ⚠️ *Data leaves your control:* if you use an external model to synthesize or label examples, remove secrets and user identifiers first. → *Expect:* a draft set covering common, edge, and harmful inputs.
3. **Balance the set.** Cap overrepresented categories and intentionally include rare but costly failures. → *Expect:* category counts where no single category dominates unless that mirrors the task distribution by design.
4. **Write machine-checkable labels.** Use exact answers, regexes, JSON schemas, rubric fields, or acceptable document ids instead of prose-only notes. → *Expect:* each row can be graded by code or a deterministic pre-check.
5. **Validate the file.** Run a schema check such as `python -m jsonschema eval.schema.json eval.jsonl` or a short loader that parses every JSONL line. → *Expect:* every row parses and validates without missing ids or duplicate ids.
6. **Freeze a first version.** Save the set as `evals/<task>/v001.jsonl` and record dataset hash with `sha256sum`. → *Expect:* a stable file path and hash that future runs can compare against.

## Decision points

- Sensitive production logs needed → redact locally and keep raw logs out of the eval repository.
- Labels are subjective → add a rubric and double-label a sample before scaling.
- Eval is too easy → add recent known failures and adversarial boundary cases before using it as a gate.

## Failure modes & recovery

- **F1 Leaky labels:** detect model sees `expected` in the prompt → separate input files from answer keys and inspect prompts.
- **F2 Duplicate examples:** detect repeated ids or near-identical inputs → deduplicate by id and embedding/text similarity.
- **F3 Unrepresentative set:** detect high eval score but user complaints persist → add examples from recent failures and stratify by category.
- **F4 Invalid rows:** detect JSON parse or schema errors → reject the dataset version until validation passes.

## Verification

`python validate_eval_set.py evals/<task>/v001.jsonl` exits 0, reports zero duplicate ids, zero schema errors, at least 30 examples, and every declared category has at least one example. The file hash is recorded beside the eval config.

## Variations

- `classification`: store `expected_label` and allowed labels.
- `rag`: store `query`, `gold_doc_ids`, and optionally answer rubric.
- `tool-use`: store available tools, expected tool name, and required arguments.

## Safety & privacy

Treat eval data like product data. Redact names, emails, account numbers, secrets, and confidential documents before sharing with a third-party API or committing to a repo. Put a hard budget on synthetic generation and reviewer labeling.
