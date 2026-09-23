---
name: control-output-length
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

Constrain an LLM response to a measurable length budget, such as tokens, words, bullets, or JSON array items, and verify the output obeys that limit.

## Preconditions

- You can call the target model and set a maximum output token limit.
- A tokenizer or counting function for the target model, such as `tiktoken`, a provider count-tokens endpoint, or a local tokenizer.
- Representative prompts that normally produce outputs of varying length.

## Steps

1. **Choose the length unit.** Decide whether the product constraint is tokens, words, characters, bullets, sentences, or structured items. → *Expect:* a single machine-countable limit such as `max_words: 120` or `max_items: 5`.
2. **Set API-level output caps.** [BRANCH: Anthropic | OpenAI | open model] Configure the provider's maximum output tokens slightly above the desired natural-language limit to leave room for stop tokens or JSON syntax. → *Expect:* requests fail closed instead of generating unbounded text.
3. **Write explicit prompt constraints.** Tell the model the maximum length and the output shape, for example `Return exactly 3 bullets, each under 18 words`. → *Expect:* a prompt template with a visible length rule.
4. **Use structure when possible.** For lists, ask for a JSON array with `maxItems`; for summaries, request fields such as `headline` and `details`. → *Expect:* outputs can be counted by a parser rather than by human review.
5. **Add stop sequences only for stable delimiters.** Use stop sequences for formats with a reliable boundary, not for arbitrary prose. → *Expect:* the response terminates at a known marker without truncating required content.
6. **Measure output length after generation.** Parse the output and count the selected unit with code. → *Expect:* each result row has `length`, `limit`, and `within_limit`.
7. **Retry or compress when over budget.** If the first pass exceeds the limit, run one bounded retry that asks the model to compress the previous answer without adding facts. → *Expect:* either a compliant response or a deterministic failure returned to the caller.

## Decision points

- Exact display space matters → enforce characters or rendered lines, not tokens.
- Downstream parser needs JSON → prefer schema `maxLength` or `maxItems` over prose instructions.
- Model frequently stops mid-sentence → raise the API output cap while keeping the prompt's user-visible limit.
- Retried output still exceeds limit → fail the request and surface a validation error.

## Failure modes & recovery

- **F1 Token truncation:** detect invalid JSON or unfinished sentence at `max_tokens` → increase token cap or shorten requested content.
- **F2 Word-count drift:** detect output over the word limit → add post-generation validation and a compression retry.
- **F3 Hidden verbosity in fields:** detect one JSON field much longer than expected → add field-level `maxLength` checks.
- **F4 Stop sequence collision:** detect content missing after an accidental delimiter → remove the stop sequence or choose a rarer delimiter.

## Verification

Run a test set of at least 50 prompts. For each response, parse the expected structure and count the chosen unit programmatically. Success means `>= 98%` of responses are within the length limit, `0` structured outputs are unparsable, and no response exceeds the API output token cap.

## Variations

- `Anthropic`: use the provider token-counting API where available and set `max_tokens`.
- `OpenAI`: use structured outputs or JSON schema for item and string bounds when supported.
- `open model`: combine generation parameters with a local tokenizer and a validator because instruction following may vary more.

## Safety & privacy

Length control is low risk, but truncation can hide important caveats. For legal, medical, or financial summaries, validate that required warning fields are present before accepting a shorter answer.
