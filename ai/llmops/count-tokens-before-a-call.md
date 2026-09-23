---
name: count-tokens-before-a-call
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: basic
est_time: 30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You count prompt tokens before an LLM call to avoid context overflow and estimate cost. The application rejects, trims, or summarizes oversized requests before sending them.

## Preconditions

- The target model id and its context window.
- A tokenizer compatible with the provider or model family.
- Prompt construction code that exposes system, user, tool, and retrieved-context text.

## Steps

1. **Identify the model context limit.** Record the model's maximum input plus output tokens and reserve an output budget. → *Expect:* a numeric `max_context_tokens` and `reserved_output_tokens`.
2. **Use the closest supported tokenizer.** [BRANCH: provider tokenizer | tiktoken | Hugging Face tokenizer] Select a tokenizer that matches the model or document the approximation. → *Expect:* token counts are reproducible in local tests.
3. **Count every message component.** Include system prompts, user messages, retrieved chunks, tool schemas, examples, and any hidden template text your app adds. → *Expect:* a total prompt-token count and per-component breakdown.
4. **Apply a preflight budget check.** Assert `prompt_tokens + reserved_output_tokens <= max_context_tokens`. → *Expect:* oversized requests fail before the API call.
5. **Trim by priority when needed.** Drop or summarize lowest-value context first, such as old chat history before current task instructions. → *Expect:* the final request fits while preserving required instructions.
6. **Compare estimates to provider usage.** After a small live call, compare local counts to returned usage and adjust the safety margin. → *Expect:* local estimate is within an acceptable tolerance, such as 5-10%.

## Decision points

- Prompt is too large → trim retrieval, summarize history, or choose a larger-context model.
- Tokenizer is approximate → add a larger safety margin before the provider limit.
- Tool schemas dominate tokens → reduce exposed tools or compress descriptions.
- Output often truncates → increase reserved output tokens and reduce input context.
- Cost estimate exceeds budget → shorten prompt or route to a cheaper model.

## Failure modes & recovery

- **F1 Context overflow:** detect provider context-length error → lower the preflight limit and count hidden fields.
- **F2 Underestimated chat overhead:** detect provider usage is higher than local estimate → include message framing overhead or add margin.
- **F3 Tool schema bloat:** detect tool definitions exceed budget → expose fewer tools per request.
- **F4 Truncated answers:** detect finish reason indicates length → reserve more output tokens.
- **F5 Wrong model limit:** detect limit mismatch after model upgrade → store context windows in versioned config.

## Verification

Token counting works when unit tests build representative prompts, assert they pass or fail the budget check correctly, and live smoke tests show local token estimates remain within the declared tolerance of provider-reported usage.

## Variations

- `Anthropic`: use provider token counting when available or a documented approximation with margin.
- `OpenAI`: use `tiktoken` for compatible models and compare against API usage.
- `open model`: use the exact Hugging Face tokenizer for the deployed checkpoint.
- `RAG`: count chunks individually so retrieval can drop the least useful chunk first.

## Safety & privacy

Low risk because counting can happen locally. Avoid sending sensitive content just to count tokens, keep model limits current, and fail closed before expensive or data-exposing API calls.
