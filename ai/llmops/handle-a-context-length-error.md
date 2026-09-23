---
name: handle-a-context-length-error
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You detect context-length failures before or after an LLM call, reduce the prompt safely, and verify that the final request fits within the model's token limit.

## Preconditions

- The target model's context window and output-token limit.
- A tokenizer or provider token-count API compatible enough for budgeting.
- A prompt assembly pipeline with separable system instructions, conversation, retrieved context, and output budget.
- Tests that include long conversations or many retrieved chunks.

## Steps

1. **Record model limits in configuration.** Store `context_window`, reserved `max_output_tokens`, and safety margin per model. → *Expect:* token budgets are not hardcoded in prompt templates.
2. **Count tokens before sending.** Compute tokens for system message, developer instructions, conversation, retrieved context, tool specs, and planned output. → *Expect:* each request has a preflight token estimate.
3. **Preserve non-negotiable content.** Mark system/developer instructions, safety constraints, and required user request as protected. → *Expect:* trimming never removes critical instructions.
4. **Trim in priority order.** Remove low-ranked retrieved chunks, summarize older conversation turns, compress verbose tool outputs, or ask the user to narrow scope. → *Expect:* the assembled prompt fits the available input budget.
5. **Retry once after provider context errors.** If the provider still returns a context-length error, apply a stronger reduction and retry at most once. → *Expect:* no unbounded retry loop occurs.
6. **Expose a controlled failure.** If the request cannot fit without losing required information, return a clear error asking for a smaller input. → *Expect:* the user receives an actionable message instead of a provider stack trace.
7. **Measure quality after trimming.** Run long-context evals to ensure summarization or chunk dropping does not remove answer-critical facts. → *Expect:* quality stays above the long-context threshold.
8. **Log token budgets without raw content.** Record section token counts and trimming decisions. → *Expect:* operators can diagnose over-budget requests without seeing private text.

## Decision points

- Retrieved context exceeds budget → rerank and include only top evidence, not arbitrary truncation.
- Conversation history is too long → summarize older turns and keep recent user constraints verbatim.
- Tool schema dominates context → expose only tools available for that route.
- Request cannot fit after safe trimming → ask for a narrower task or use a longer-context model.

## Failure modes & recovery

- **F1 Tokenizer mismatch:** detect provider context errors despite preflight passing → add a larger safety margin or use provider token counting.
- **F2 Critical instruction trimmed:** detect safety or format regressions → mark protected sections and add unit tests.
- **F3 Lost evidence:** detect wrong answers after chunk dropping → improve reranking or cite required chunks in eval fixtures.
- **F4 Infinite retry:** detect repeated context retries → cap retries and return controlled failure.
- **F5 Output budget starvation:** detect cut-off responses → reserve enough output tokens before allocating input context.

## Verification

Run tests that assemble prompts at 80%, 100%, and 130% of the model context window. The check passes only when final `input_tokens + max_output_tokens + safety_margin <= context_window`, protected sections remain present, overlong prompts are trimmed by priority, and provider context-length errors are not exposed to callers.

## Variations

- `RAG`: trim by retrieval score, document diversity, and citation requirements.
- `chatbot`: summarize old turns and preserve recent instructions and unresolved commitments.
- `tool-agent`: include only tools relevant to the current plan to reduce schema size.

## Safety & privacy

Low risk when handled locally, but careless trimming can remove safety constraints or evidence. Never drop system safety rules, avoid logging raw long prompts, and prefer controlled refusal over answering without required context.
