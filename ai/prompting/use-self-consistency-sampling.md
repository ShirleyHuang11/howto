---
name: use-self-consistency-sampling
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

You improve reliability on hard tasks by sampling multiple independent answers and selecting the consensus, while tracking added cost and latency.

## Preconditions

- A task where single-sample accuracy is not high enough.
- A deterministic answer extractor or scorer.
- Budget for multiple model calls per input.

## Steps

1. **Establish the single-sample baseline.** Run the current prompt once per eval case. → *Expect:* baseline accuracy, latency, and cost per item.
2. **Choose a sample count.** Start with 3 or 5 samples and moderate temperature for reasoning diversity. → *Expect:* a configured `n_samples` and maximum cost per item.
3. **Extract comparable final answers.** Require a final answer field so samples can be normalized. → *Expect:* every sample yields a parsed answer or a typed parse failure.
4. **Vote or score the samples.** Use majority vote for discrete answers, numeric tolerance for calculations, or a verifier for open-ended tasks. → *Expect:* a selected answer plus agreement rate.
5. **Fall back on low agreement.** If no answer reaches the threshold, ask for clarification or route to a stronger verifier. → *Expect:* low-confidence cases are not presented as certain.
6. **Compare value against cost.** Evaluate accuracy lift, latency, and token spend. ⚠️ *Data leaves your control:* repeated external API calls multiply exposure and cost for the same input. → *Expect:* a decision table showing whether lift justifies cost.

## Decision points

- Majority agreement is high and accuracy improves → use self-consistency for high-value cases.
- Agreement is low → add retrieval, tools, or a verifier instead of more blind samples.
- Cost exceeds budget → reduce sample count or gate sampling to uncertain cases.

## Failure modes & recovery

- **F1 Correlated wrong answers:** detect unanimous but incorrect samples → diversify prompts or add external verification.
- **F2 Parse failures:** detect incomparable final answers → tighten output format.
- **F3 Cost blowup:** detect spend above budget → enforce per-request caps and sampling gates.
- **F4 Latency breach:** detect p95 latency too high → run samples in parallel or reserve method for async tasks.

## Verification

Run `python eval_self_consistency.py --cases hard_eval.jsonl --n-samples 5 --min-lift 0.04 --max-cost-per-item 0.20`; consensus accuracy must improve by at least 4 percentage points over baseline while average cost stays at or below the configured budget.

## Variations

- `math`: majority vote after normalizing numeric answers.
- `classification`: vote over enum labels and abstain below agreement threshold.
- `open-ended QA`: use a verifier or judge to select the best supported answer.

## Safety & privacy

Medium risk from multiplied API calls and possible repeated exposure of sensitive inputs. Use sampling only when quality gain matters, redact private data, and cap total calls, latency, and spend.
