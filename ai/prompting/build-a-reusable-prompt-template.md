---
name: build-a-reusable-prompt-template
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

You turn an ad hoc prompt into a reusable template with typed variables, examples, tests, and versioning.

## Preconditions

- A working prompt for one task instance.
- A templating system such as Jinja, Mustache, LangChain templates, or a plain typed function.
- Representative inputs for testing.

## Steps

1. **Identify variable and constant parts.** Mark user input, context, examples, constraints, and output format separately. → *Expect:* a list of template variables with names and descriptions.
2. **Define typed inputs.** Create a schema for variables such as `task`, `context_chunks`, `audience`, and `output_format`. → *Expect:* invalid missing variables fail before a model call.
3. **Render with safe delimiters.** Put user-controlled content inside clear boundaries such as `<user_input>...</user_input>`. → *Expect:* rendered prompts preserve delimiters even when variables contain newlines.
4. **Add snapshot tests.** Render known inputs and compare to checked-in snapshots. → *Expect:* `pytest tests/test_prompt_render.py` detects accidental prompt changes.
5. **Evaluate behavior, not just rendering.** Run a small model eval on representative cases. → *Expect:* a report with task score and parse rate for the rendered template.
6. **Version the template.** Store a semantic version or hash with every model call. → *Expect:* logs can map each output back to the exact template version.

## Decision points

- Variables contain user-supplied text → always delimit and escape where the template engine requires it.
- Prompt changes affect production behavior → run evals and bump the prompt version.
- Many optional branches appear → split into smaller templates rather than nested conditionals.

## Failure modes & recovery

- **F1 Missing variable:** detect template render error → add schema validation and defaults only when safe.
- **F2 Delimiter collision:** detect user text that closes a tag → escape or use randomized boundary tokens.
- **F3 Snapshot churn:** detect frequent irrelevant diffs → normalize whitespace intentionally and document it.
- **F4 Behavioral regression:** detect eval score drop after rendering change → revert the template version or add tests for the failing case.

## Verification

Run `pytest tests/test_prompt_render.py && python eval_template.py --template prompts/task.j2 --cases eval.jsonl --min-score 0.85`; rendering tests must pass and the candidate template must score at least 0.85 with at least 98% parse rate.

## Variations

- `Jinja`: use strict undefined variables and disable unsafe filters.
- `TypeScript`: validate inputs with Zod before rendering.
- `Python`: use Pydantic models and snapshot tests with `pytest`.

## Safety & privacy

Templates often mix trusted instructions with untrusted user data. Keep user variables delimited, log prompt versions without logging sensitive full inputs by default, and review any template that controls tool use or actions.
