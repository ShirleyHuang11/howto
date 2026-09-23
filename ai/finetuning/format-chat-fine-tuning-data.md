---
name: format-chat-fine-tuning-data
domain: ai
subdomain: finetuning
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [ai/finetuning/prepare-a-fine-tuning-dataset]
status: draft
last_verified: 2026-09-22
---

## Goal

You convert cleaned examples into role-based chat fine-tuning JSONL that matches the trainer's schema. Each row parses, contains the intended assistant target, and fits token limits.

## Preconditions

- A cleaned source dataset with approved inputs and target assistant responses.
- The target provider or open-source trainer's expected chat schema.
- A tokenizer or provider validation command for the chosen base model.

## Steps

1. **Map fields to chat roles.** Convert instructions to `system`, user requests to `user`, and target answers to `assistant`. → *Expect:* every row has at least one `user` message and one final `assistant` message.
2. **Keep system prompts stable.** Use one short system message when it represents product behavior; avoid stuffing per-example labels into it. → *Expect:* system messages are either absent or consistent across task families.
3. **Serialize as JSONL.** [BRANCH: OpenAI-style messages | Anthropic-style messages | TRL chat template] Write one object per line, such as `{"messages":[{"role":"user","content":"..."},{"role":"assistant","content":"..."}]}`. → *Expect:* `python -c 'import json,sys; [json.loads(l) for l in open(sys.argv[1])]' train.jsonl` exits 0.
4. **Validate role ordering.** Reject rows where assistant messages appear before the user unless the trainer explicitly supports demonstrations. → *Expect:* role-order checks pass for 100% of rows.
5. **Validate tool calls if present.** Store tool calls and tool results in the provider's supported schema, not as informal prose. → *Expect:* tool-call arguments parse as JSON and required tool names are present.
6. **Count tokens after applying the chat template.** Use the exact tokenizer or provider validator, because role wrappers add tokens. → *Expect:* p50, p95, and max token counts are reported and within limits.
7. **Create a small dry-run subset.** Save 10-50 rows and run the trainer's file validator or a one-step local training dry run. → *Expect:* the validator accepts the file without schema errors.

## Decision points

- Multiple assistant answers per conversation → keep only the target completion unless the trainer supports multi-turn supervision.
- Provider validator rejects tool schema → convert to that provider's current tool-call format before training.
- Many rows exceed token limits → shorten context or train on task-specific excerpts.
- The base model already follows the format → prefer prompt/schema enforcement over fine-tuning.

## Failure modes & recovery

- **F1 Invalid JSONL:** detect parser errors with line numbers → rewrite only broken rows and rerun full validation.
- **F2 Wrong role names:** detect roles outside the allowed set → map custom labels to supported roles.
- **F3 Missing assistant target:** detect rows ending in `user` → drop or repair the example.
- **F4 Template mismatch:** detect local token counts disagreeing with provider counts → use the provider tokenizer or official chat template.
- **F5 Tool arguments as strings:** detect unparseable tool arguments → convert to structured JSON and validate against the tool schema.

## Verification

The formatted train and validation files pass JSONL parsing, role-order validation, provider or trainer schema validation, tool argument JSON validation when applicable, and token counting with `max_tokens_per_row <= model_training_limit`.

## Variations

- `OpenAI-compatible`: use a top-level `messages` array with role/content objects and provider-specific tool fields.
- `Anthropic-compatible`: follow the provider's current fine-tuning message schema and separate system instructions where required.
- `TRL/SFTTrainer`: apply the tokenizer's `chat_template` and train on the rendered text.

## Safety & privacy

Do not accidentally place secrets in system prompts or examples. If the JSONL will be uploaded to a hosted trainer, treat the upload as data leaving your control and confirm redaction, training rights, and retention settings.
