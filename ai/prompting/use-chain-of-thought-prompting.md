---
name: use-chain-of-thought-prompting
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

You improve difficult task accuracy by asking the model to reason internally or produce concise working notes, while verifying only the final answer and allowed rationale.

## Preconditions

- A task where direct prompting underperforms, such as math, planning, diagnosis, or multi-hop retrieval.
- A labeled evaluation set with final answers.
- A policy for whether reasoning traces may be stored or shown.

## Steps

1. **Measure the direct baseline.** Run the task with a simple prompt and deterministic settings. → *Expect:* a baseline accuracy and examples of wrong answers.
2. **Choose visible or hidden reasoning.** [BRANCH: hidden reasoning | concise visible rationale] Prefer instructions like `think through the problem, then return only the final answer and a brief justification` when traces should not be exposed. → *Expect:* outputs contain final answers and no long private reasoning traces.
3. **Add a final-answer delimiter.** Require `FINAL:` or a JSON field such as `{"answer": "...", "confidence": 0.0}`. → *Expect:* every response has a parseable final answer.
4. **Evaluate accuracy and leakage.** Score final answers and scan outputs for disallowed long reasoning. → *Expect:* a report with accuracy, parse rate, and reasoning-leak count.
5. **Tune for concise justification.** If explanations are needed, require 1-3 evidence-backed bullets rather than full hidden reasoning. → *Expect:* rationales stay under a configured token limit and cite allowed evidence.
6. **Keep the smallest improvement.** Adopt the reasoning prompt only if it beats the direct baseline on held-out cases. → *Expect:* a versioned prompt with measured lift.

## Decision points

- Accuracy does not improve → use decomposition, tools, or retrieval instead of longer reasoning instructions.
- Long reasoning appears in logs → switch to final-answer-only output and avoid storing intermediate traces.
- The task needs auditability → request concise evidence, not unrestricted chain-of-thought.

## Failure modes & recovery

- **F1 Verbose reasoning leakage:** detect outputs exceeding rationale limits → enforce final-answer schema and reject long rationales.
- **F2 Confident wrong answers:** detect high confidence on incorrect cases → calibrate confidence or remove it from user-facing output.
- **F3 Parse failure:** detect missing `FINAL:` or invalid JSON → add schema validation and retry once with a repair prompt.
- **F4 Spurious reasoning:** detect plausible but unsupported explanation → require citations or evidence ids from provided context.

## Verification

Run `python eval_reasoning_prompt.py --baseline direct.md --candidate reasoning.md --cases heldout.jsonl --max-rationale-tokens 120`; the candidate must improve final-answer accuracy by at least 3 percentage points, parse at least 98% of outputs, and produce zero disallowed long reasoning traces.

## Variations

- `math`: use answer-only grading plus numeric tolerance.
- `RAG`: ask for cited evidence ids and score citation support.
- `agent planning`: request a short plan, then execute tools stepwise with checks after each action.

## Safety & privacy

Avoid exposing hidden reasoning that may contain sensitive prompt, policy, or user data. Store only final answers, concise justifications, and audit metadata unless you have a clear retention policy.
