---
name: detect-benchmark-contamination
domain: ai
subdomain: evals
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 2h
risk: medium
prerequisites: [ai/evals/build-an-eval-set]
status: draft
last_verified: 2026-09-22
---

## Goal

You estimate whether eval examples are memorized, leaked into training data, or otherwise contaminated. The result identifies examples that should be removed or interpreted cautiously.

## Preconditions

- The benchmark examples and answer keys.
- Access to model outputs and, when available, training corpus metadata or data filters.
- Near-duplicate search tooling such as MinHash, embeddings, or exact text search.

## Steps

1. **Search for exact leakage.** Query code, document stores, prompts, and public web/index snapshots for exact question and answer strings. → *Expect:* any exact matches are recorded with source.
2. **Run near-duplicate detection.** Use MinHash or embeddings to find highly similar examples in training or prompt corpora. → *Expect:* candidates above the similarity threshold are flagged.
3. **Probe memorization behavior.** Ask the model for answers with minimal context and compare unusually exact wording to the answer key. ⚠️ *Data leaves your control:* do not submit proprietary benchmark items to unapproved external APIs. → *Expect:* suspicious verbatim or near-verbatim completions are listed.
4. **Compare paraphrased variants.** Reword prompts while preserving meaning and check whether performance drops sharply. → *Expect:* contamination suspicion increases if original wording scores much higher than paraphrases.
5. **Label contamination status.** Assign `clean`, `suspect`, or `contaminated` with evidence. → *Expect:* the benchmark can exclude or downweight suspect items.
6. **Create a clean split.** Remove contaminated examples and rerun metrics. → *Expect:* reported score includes clean-only and full-set results.

## Decision points

- Exact benchmark appears in training data → exclude it from headline evals.
- Only public web match exists → decide based on whether the model could have trained on that source.
- Clean-only score much lower → prioritize clean score for release decisions.

## Failure modes & recovery

- **F1 False duplicate:** detect boilerplate or common facts flagged → require answer-key or full-question overlap too.
- **F2 Hidden contamination:** detect no corpus access → use behavioral probes and treat conclusions as estimates.
- **F3 Over-removal:** detect many legitimate similar items removed → use human review for borderline matches.
- **F4 Prompt leakage:** detect benchmark included in few-shot examples → remove from prompts and rerun.

## Verification

The contamination report lists exact-match counts, near-duplicate counts, behavioral probe results, and a clean dataset file. The eval runner can reproduce both full-set and clean-only metrics and excludes all examples labeled `contaminated` from the headline score.

## Variations

- `open-source model`: inspect documented training mixtures and run corpus search when available.
- `private fine-tune`: compare against fine-tuning files and prompt logs.
- `public benchmark`: use paraphrase robustness and canary questions when corpus access is unavailable.

## Safety & privacy

Benchmark items may be confidential. Do not paste proprietary test sets into public search engines or unapproved APIs; use local search whenever possible and store evidence with access controls.
