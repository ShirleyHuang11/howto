---
name: distill-a-smaller-model
domain: ai
subdomain: finetuning
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 2d
risk: high
prerequisites: [ai/finetuning/decide-fine-tune-vs-rag-vs-prompt]
status: draft
last_verified: 2026-09-22
---

## Goal

You train or fine-tune a smaller student model to imitate a stronger teacher on a bounded task. The student must meet a held-out quality threshold while reducing latency or cost.

## Preconditions

- A task-specific dataset with train, validation, and test splits.
- Access to a capable teacher model and a smaller student model or fine-tuning service.
- A budget cap for teacher labeling, training, and validation.
- Rights to generate and use synthetic labels under the selected provider terms.

## Steps

1. **Freeze the target task and metrics.** Define inputs, expected output schema, scoring script, and thresholds such as `student_score >= 0.95 * teacher_score` and `cost_per_1k_requests <= 0.40 * teacher_cost`. → *Expect:* an executable eval command and numeric pass criteria.
2. **Select representative seed examples.** Stratify by intent, difficulty, language, and edge case; remove duplicates and examples containing secrets. → *Expect:* `train.jsonl`, `valid.jsonl`, and `test.jsonl` with stable ids.
3. **Generate teacher labels.** [BRANCH: Anthropic | OpenAI | open model] Prompt the teacher to produce final answers plus optional rationales or tool calls. ⚠️ *Data leaves your control:* redact PII and confirm the dataset may be sent to the teacher API. → *Expect:* a completed label file with parseable outputs for at least 99% of examples.
4. **Filter low-quality teacher outputs.** Validate schemas, remove refusals caused by bad prompts, and sample-review disagreements or low-confidence items. → *Expect:* a clean distillation set with rejection reasons logged.
5. **Train the student.** [BRANCH: hosted fine-tune | LoRA | full fine-tune] Use conservative epochs, validation monitoring, and a fixed random seed where supported. ⚠️ *Irreversible:* launching a paid training job spends budget; confirm dataset path, price estimate, and stop criteria first. → *Expect:* a training job id, validation loss curve, and saved checkpoint or model id.
6. **Evaluate teacher, student, and baseline side by side.** Run the same held-out test set through all models without using training examples. → *Expect:* a comparison table with quality, latency, token usage, and cost.
7. **Package the student behind a rollback switch.** Route a small percentage of traffic or offline batch jobs to the student and keep the teacher as fallback for low-confidence cases. → *Expect:* a deployable config with `student`, `teacher_fallback`, and threshold settings.

## Decision points

- Student underperforms mostly on rare cases → add targeted teacher-labeled examples for those strata.
- Student matches quality but not cost or latency target → try a smaller base model or quantized serving.
- Teacher labels fail schema validation often → fix the teacher prompt before generating more data.
- Validation loss improves but held-out score drops → stop and reduce epochs or clean noisy labels.
- Production task changes frequently → keep the teacher/RAG path instead of distilling stale behavior.

## Failure modes & recovery

- **F1 Teacher error amplification:** detect repeated wrong labels in sampled reviews → filter or relabel with a second judge.
- **F2 Data leakage:** detect test ids or near-duplicates in train → deduplicate by id and embedding similarity, then rebuild splits.
- **F3 Student overfits phrasing:** detect high exact-match but poor semantic judge score → diversify prompts and use rubric-based evals.
- **F4 Training runaway cost:** detect spend or epochs exceeding budget → cancel the job and lower dataset size or epochs.
- **F5 Unsafe imitation:** detect policy violations copied from teacher outputs → filter training data and run safety evals before deployment.

## Verification

Distillation succeeds only if an automated eval on the untouched test set shows the student meeting the declared quality threshold, schema-valid output rate at or above 99%, and measured cost or p95 latency reduction meeting the target. The report must include teacher, baseline, and student scores from the same script.

## Variations

- `Anthropic teacher`: use Claude Sonnet or Opus for labels, then train a smaller hosted or open student.
- `OpenAI`: use a strong model for labeling and a fine-tunable smaller model as the student when terms allow.
- `open model`: generate labels locally for sensitive data, then apply LoRA with PEFT and serve with vLLM or TGI.
- `classification`: distill logits or labels; free-form generation usually needs schema validation and judge scoring.

## Safety & privacy

High risk because teacher labeling and training may expose data and spend real budget. Remove PII and secrets, verify licensing and provider retention terms, cap spend, retain raw and filtered datasets separately, and require human approval before launching paid training or deploying the student to production traffic.
