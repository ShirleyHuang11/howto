---
name: write-few-shot-examples
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

You create few-shot examples that teach the model the desired mapping from inputs to outputs, then verify that held-out examples improve without copying the demonstrations.

## Preconditions

- A prompt template with a clear input and output contract.
- At least 20 representative labeled examples, with 5-8 reserved as held-out tests.
- A script or notebook that can call the target model repeatedly.

## Steps

1. **Define the behavior to demonstrate.** Write one sentence describing the pattern the examples should teach, such as terse classification, citation style, or JSON normalization. → *Expect:* a named behavior and measurable output fields.
2. **Select diverse positive examples.** Pick 3-5 examples that cover common, edge, and ambiguous cases. → *Expect:* no two examples share the same easy surface pattern.
3. **Add one negative or boundary example.** Show what to do when the input is incomplete, unsafe, or out of scope. → *Expect:* the prompt includes an example where the correct output is refusal, null, or clarification.
4. **Keep examples structurally identical.** Use the same delimiters and output schema for every shot. → *Expect:* a parser can split the prompt into examples and find identical field names.
5. **Evaluate zero-shot versus few-shot.** Run the held-out set once without examples and once with examples using the same model settings. → *Expect:* a comparison table with accuracy, parse rate, and failed ids.
6. **Remove harmful examples.** Delete any shot that encourages verbosity, leaks labels, or degrades held-out performance. → *Expect:* the final prompt is shorter or equal length and scores no worse than the previous version.

## Decision points

- Held-out accuracy improves but parse rate drops → make the output schema stricter before adding more examples.
- Model copies example content → add more input diversity and use placeholders only where literal reuse is acceptable.
- Prompt exceeds context budget → keep the highest-information shots and move rare behavior to validation logic.

## Failure modes & recovery

- **F1 Label leakage:** detect held-out inputs that appear verbatim in shots → rebuild the split before measuring.
- **F2 Example overfitting:** detect success only on cases similar to demonstrations → add diverse edge cases and retest.
- **F3 Format drift:** detect JSON or schema failures → make every example syntactically valid and identical in shape.
- **F4 Longer prompt hurts quality:** detect lower score than zero-shot → reduce shots or replace them with concise rules.

## Verification

Run `python eval_fewshot.py --zero-shot base_prompt.md --few-shot fewshot_prompt.md --cases heldout.jsonl`; the few-shot prompt must improve the primary metric by at least 5 percentage points or preserve it while improving parse rate to at least 98%.

## Variations

- `classification`: use examples with hard negatives and class imbalance matching production.
- `extraction`: include missing-field examples with explicit `null` values.
- `generation`: judge with a rubric and spot-check for unwanted imitation of examples.

## Safety & privacy

Use synthetic or approved examples when sending prompts to an external model. Remove names, account numbers, secrets, and proprietary text; few-shot examples are especially likely to be reproduced in outputs.
