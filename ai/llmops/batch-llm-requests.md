---
name: batch-llm-requests
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: high
prerequisites: [ai/llmops/call-an-llm-api]
status: draft
last_verified: 2026-09-22
---

## Goal

You submit many LLM requests as a controlled batch job with idempotent inputs, cost limits, validation, and retry handling. The completed batch yields one validated output per input id.

## Preconditions

- A JSONL, CSV, or database table of inputs with stable unique ids.
- A provider batch API, queue worker, or local batch runner.
- A schema validator and cost estimate for the batch.

## Steps

1. **Prepare idempotent input records.** Give every request a stable `custom_id`, prompt fields, model, parameters, and expected output schema version. → *Expect:* no duplicate ids and every record validates locally.
2. **Estimate tokens and cost.** Count input tokens and reserve output tokens for the full batch before submission. → *Expect:* estimated cost is below the approved batch budget.
3. **Run a small canary batch.** Submit 10-50 representative requests first. ⚠️ *Data leaves your control:* hosted batch APIs receive every submitted record; redact sensitive fields and confirm provider terms. → *Expect:* canary outputs complete and validate at the expected rate.
4. **Submit the full batch with tracking.** [BRANCH: provider batch API | queue workers | local inference] Store batch id, input file checksum, model, and submission time. ⚠️ *Irreversible:* large paid batches can spend significant budget; confirm file checksum and cost estimate first. → *Expect:* a batch/job id and accepted status.
5. **Poll or consume completion events.** Track completed, failed, expired, and canceled records without resubmitting successful ids. → *Expect:* progress metrics by status.
6. **Validate and join outputs by id.** Parse each output, run schema and task checks, and join back to the input id. → *Expect:* each input id has `valid_output`, `retryable_error`, or `terminal_error`.
7. **Retry only failed retryable records.** Create a new batch for retryable failures using the same custom ids plus attempt metadata. → *Expect:* retries do not duplicate successful work.

## Decision points

- Canary validity is low → fix prompt/schema before full batch.
- Estimated cost exceeds budget → sample, reduce output length, or choose cheaper model.
- Batch deadline is missed → split into smaller batches or use synchronous workers.
- Some records fail due to content or context length → repair those inputs instead of retrying unchanged.
- Outputs will feed irreversible action → require human review before downstream execution.

## Failure modes & recovery

- **F1 Duplicate ids:** detect repeated `custom_id` → reject input file and regenerate ids.
- **F2 Partial batch loss:** detect missing ids after completion → compare input id set to output id set and retry missing records.
- **F3 Schema failure flood:** detect many parse errors → stop retries and fix prompt or model settings.
- **F4 Cost overrun:** detect actual usage above estimate → lower token caps and require approval for retry batch.
- **F5 Provider expiration:** detect expired batch status → resubmit only unfinished ids.

## Verification

Batch processing succeeds when an automated reconciliation script proves every input id appears exactly once in the final results, every accepted output validates against the schema, retryable failures are isolated for another attempt, and actual cost is within the approved budget.

## Variations

- `provider batch API`: cheaper for offline work but slower and less interactive.
- `queue workers`: useful when you need custom retry logic and mixed providers.
- `local inference`: best for sensitive data if you can provision enough throughput.
- `evaluation batches`: store judge prompts and model outputs separately for auditability.

## Safety & privacy

High risk because batches can expose many records and spend quickly. Redact inputs, use canaries, cap budget, store checksums, reconcile by id, and require approval before large hosted submissions or downstream irreversible actions.
