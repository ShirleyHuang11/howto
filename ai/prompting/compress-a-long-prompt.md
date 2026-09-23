---
name: compress-a-long-prompt
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

You shorten a long prompt while preserving behavior, reducing token cost, and staying within the model context limit.

## Preconditions

- A long prompt or template with known behavior.
- Token counting for the target model.
- A regression eval set that covers required behaviors.

## Steps

1. **Measure the current prompt.** Count tokens for the rendered prompt and record cost per call. → *Expect:* a baseline token count and estimated cost.
2. **Classify prompt content.** Mark each section as mandatory instruction, example, redundant wording, obsolete rule, or task data. → *Expect:* a table of removable and non-removable sections.
3. **Remove duplication first.** Merge repeated constraints and delete prose that does not change behavior. → *Expect:* token count drops without changing required rules.
4. **Replace examples selectively.** Keep only examples that cover unique edge cases; convert obvious examples into concise rules. → *Expect:* fewer shots with the same edge-case coverage.
5. **Run regression evals.** Compare original and compressed prompts on the same cases. → *Expect:* score, parse rate, and safety metrics stay within tolerance.
6. **Set a token budget test.** Add an automated check for maximum rendered prompt tokens. → *Expect:* future prompt changes fail if they exceed budget.

## Decision points

- Compression lowers quality beyond tolerance → restore the section responsible for failed cases.
- Prompt still exceeds context → move long knowledge into retrieval or tools instead of prompt text.
- Examples dominate token usage → measure marginal value of each example.

## Failure modes & recovery

- **F1 Lost edge case:** detect regression on a rare behavior → restore or rewrite the smallest needed instruction.
- **F2 Hidden dependency:** detect failures after deleting "redundant" text → add a targeted eval and rephrase concisely.
- **F3 Token miscount:** detect provider rejects context length → use the provider-compatible tokenizer.
- **F4 Overcompressed ambiguity:** detect inconsistent outputs → make critical constraints explicit again.

## Verification

Run `python compress_eval.py --original original_prompt.md --candidate compressed_prompt.md --cases regression.jsonl --max-tokens 2500`; candidate tokens must be at least 25% lower, below the budget, and quality must remain within 2 percentage points of the original.

## Variations

- `RAG`: move reference material to retrieval and keep only retrieval instructions in the prompt.
- `few-shot`: prune examples by leave-one-out eval.
- `agent prompt`: keep tool safety rules explicit even if other prose is compressed.

## Safety & privacy

Do not compress away safety, privacy, or tool-authorization rules. Token savings are not worth higher rates of unsafe action, data leakage, or unsupported claims.
