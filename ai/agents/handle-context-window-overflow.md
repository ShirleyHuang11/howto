---
name: handle-context-window-overflow
domain: ai
subdomain: agents
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Your agent detects context-window pressure before provider errors and safely compacts or retrieves state. Success means prompts stay below the model limit while preserving the information needed to pass task and citation checks.

## Preconditions

- Token counting for the target model or a conservative tokenizer approximation.
- Access to conversation history, scratchpad, retrieved documents, and tool results before model invocation.
- A summarization or retrieval strategy for older context.

## Steps

1. **Measure tokens before every model call.** Count system, developer, user, tool, retrieved, scratchpad, and expected output budget. → *Expect:* the controller has a numeric `input_tokens + reserved_output_tokens` estimate.
2. **Set a safety margin below the provider limit.** Use a threshold such as `0.85 * context_window` or a fixed reserve for tool calls and output. → *Expect:* no request is sent when estimated tokens exceed the threshold.
3. **Prioritize context by trust and relevance.** Keep system/developer instructions, current user request, active tool schemas, recent tool results, and verified scratchpad state. → *Expect:* low-priority history and duplicate retrieved chunks are candidates for removal first.
4. **Compact old conversation and tool output.** Summarize older turns into structured facts with source pointers; truncate large raw payloads after extracting needed fields. → *Expect:* compacted context validates against a summary schema and includes provenance.
5. **Retrieve instead of stuffing.** Store large documents or old traces in a searchable index and fetch only top relevant chunks for the current step. → *Expect:* retrieved chunks fit the token budget and include doc IDs.
6. **Fail gracefully when required context cannot fit.** Ask the user to narrow the task or switch to a larger-context model. → *Expect:* the run stops with `context_overflow` instead of receiving a provider context-length error.

## Decision points

- Overflow is caused by retrieved documents → reduce `top_k`, re-rank, or chunk smaller.
- Overflow is caused by conversation history → summarize older turns and keep recent turns verbatim.
- Required evidence cannot fit → switch to a larger-context model or ask the user to scope down.
- Summaries lose task-critical details → keep source references and re-retrieve on demand.

## Failure modes & recovery

- **F1 Provider context error:** detect context-length exception → lower threshold and add preflight token checks.
- **F2 Summary drops constraints:** detect eval failures on user requirements → store structured requirements separately from narrative summary.
- **F3 Citation loss:** detect final citations to missing chunks → preserve doc IDs and quote spans in compacted context.
- **F4 Token counter mismatch:** detect provider usage above estimate → calibrate tokenizer and increase safety margin.

## Verification

Run overflow fixtures with long chat history, large tool output, and many retrieved chunks. The preflight check must keep estimated tokens plus reserved output below the configured model limit, produce schema-valid compacted summaries with provenance, avoid provider context-length errors, and preserve answer accuracy on a labeled case set.

## Variations

- `large-context model`: use more room but still count tokens and reserve output budget.
- `RAG-heavy agent`: re-rank and retrieve fewer chunks rather than summarizing evidence away.
- `code agent`: keep exact current files or diffs; summarize logs and stale exploration.

## Safety & privacy

Medium risk because compaction can hide constraints and retrieval can reintroduce sensitive data. Preserve trusted instructions verbatim, label summaries as derived data, avoid sending unnecessary private history to third-party APIs, and stop rather than guessing when essential context cannot fit.
