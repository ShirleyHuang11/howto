---
name: set-an-agent-token-budget
domain: ai
subdomain: agents
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

You cap an agent's token use so it stays within model context limits, cost budget, and latency requirements while still completing target tasks.

## Preconditions

- Token counting support for your model or tokenizer.
- Known model context window, input/output pricing, and latency targets.
- Agent traces from representative tasks.
- A policy for what to do when budget is low.

## Steps

1. **Calculate hard limits.** Record model context window, max output tokens, per-request price, and run-level budget. → *Expect:* numeric caps such as `max_prompt_tokens`, `max_completion_tokens`, and `max_run_cost_usd`.
2. **Reserve token bands.** Allocate space for system prompt, user request, tool schemas, retrieved context, memory, tool observations, and final answer. → *Expect:* allocations sum to less than the model context window.
3. **Count before every model call.** Use the provider tokenizer or a conservative estimator and reject prompts that exceed budget. → *Expect:* no call fails with context-length errors in tests.
4. **Trim low-value context.** Drop or summarize old observations, low-ranked retrieved chunks, and irrelevant memory before reducing instructions. → *Expect:* prompt remains valid and within the token cap.
5. **Track cumulative spend.** Add input and output tokens across loop iterations and stop before run budget is exceeded. ⚠️ *Data leaves your control:* each hosted model call sends prompt context externally; reducing context also reduces exposure. → *Expect:* runs stop with `budget_exceeded` before overspending.
6. **Set iteration-aware output caps.** Use smaller completion caps for planning/tool selection and larger caps only for final synthesis. → *Expect:* helper turns cannot consume the whole run budget.
7. **Evaluate budget versus success.** Run representative tasks under different caps and plot success rate, cost, latency, and truncation failures. → *Expect:* selected budget meets success target and cost SLO.

## Decision points

- Context is too large before retrieval → summarize conversation and memory.
- Retrieved context exceeds allocation → rerank, compress, or lower top-k.
- Agent hits budget often → simplify tools, reduce loop iterations, or use a cheaper model for planning.
- High-stakes task needs completeness → ask for approval to raise budget rather than silently truncating.

## Failure modes & recovery

- **F1 Context overflow:** detect provider context-length error → count tokens pre-call and enforce stricter margins.
- **F2 Silent truncation:** detect missing instructions or evidence → fail closed instead of trimming required policy text.
- **F3 Cost runaway:** detect cumulative estimate above budget → stop loop and return partial status.
- **F4 Low answer quality from over-trimming:** detect eval success drop → preserve high-value context and compress lower-value context.

## Verification

Automated traces must show every model call stays below context and output caps, cumulative estimated cost stays under `max_run_cost_usd`, context-overflow errors are zero, and task success remains above the configured threshold on representative evals.

## Variations

- `long-context-model`: increase context allocation but keep cost and retrieval-quality budgets.
- `small-model-agent`: use tighter schemas and shorter observations to fit smaller context windows.
- `multi-agent`: enforce both per-agent and global orchestration budgets.

## Safety & privacy

Budgets reduce cost and data exposure but can also remove critical safety instructions if trimming is careless. Never trim system policy or approval rules, redact sensitive context before hosted calls, and stop for human review when a task cannot fit safely in budget.
