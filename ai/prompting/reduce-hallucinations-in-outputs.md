---
name: reduce-hallucinations-in-outputs
domain: ai
subdomain: prompting
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You reduce unsupported claims by grounding outputs in provided evidence, requiring uncertainty when evidence is missing, and measuring factuality on a labeled set.

## Preconditions

- A task where factual correctness matters.
- Source documents, retrieval results, or trusted database records.
- A labeled eval set with questions, allowed evidence ids, and expected answers.

## Steps

1. **Define what counts as grounded.** Require every factual claim to be supported by a provided source id or marked unknown. → *Expect:* a rubric with `supported`, `unsupported`, and `insufficient_evidence` labels.
2. **Constrain the model to supplied context.** Tell it to answer only from the provided evidence and to say `I don't know` when evidence is absent. → *Expect:* outputs include citations or an explicit insufficient-evidence marker.
3. **Lower randomness for factual tasks.** Use deterministic settings unless diversity is intentionally needed. → *Expect:* repeated calls on the same input return materially similar answers.
4. **Add citation checking.** Programmatically verify cited ids exist in the retrieved context. → *Expect:* invalid citation ids fail validation.
5. **Run a groundedness eval.** Score answers with exact checks where possible and a judge rubric for support. ⚠️ *Data leaves your control:* if using an external judge model on private records, redact or approve data first. → *Expect:* factuality, citation validity, and abstention metrics.
6. **Tune retrieval or prompt based on failures.** Fix missing evidence with retrieval changes; fix unsupported synthesis with prompt and validation changes. → *Expect:* unsupported-claim rate drops on held-out cases.

## Decision points

- Evidence is missing from top results → improve retrieval before changing generation.
- Citations are valid but do not support claims → add sentence-level citation requirements or a verifier.
- Abstention rate is too high → check whether the context actually contains answers before loosening the prompt.

## Failure modes & recovery

- **F1 Fabricated citation:** detect cited id not in context → reject output and retry with valid id list.
- **F2 Unsupported synthesis:** detect answer claims absent from source text → require quote spans or sentence-level citations.
- **F3 Over-abstention:** detect `I don't know` for answerable cases → improve retrieval recall and examples.
- **F4 Stale knowledge:** detect model using outdated prior knowledge → restate that provided context is authoritative.

## Verification

Run `python eval_groundedness.py --cases grounded_eval.jsonl --min-supported 0.90 --max-unsupported 0.03`; at least 90% of answerable cases are supported by valid citations, unsupported claims are at most 3%, and unanswerable cases abstain at least 95% of the time.

## Variations

- `RAG`: measure retrieval recall separately from generation groundedness.
- `database QA`: generate SQL or API calls, then answer only from returned rows.
- `summarization`: require every paragraph to list source ids used.

## Safety & privacy

Medium risk when factual errors affect users or private data is sent to external evaluators. Redact PII, log cited evidence ids for audit, and do not ship if the unsupported-claim threshold fails.
