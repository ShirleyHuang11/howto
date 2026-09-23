---
name: adapt-a-prompt-across-models
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

You move a prompt from one model or provider to another while preserving behavior, output format, safety constraints, and cost targets.

## Preconditions

- The source prompt, source model settings, and eval results.
- Access to the target model.
- A compatibility checklist for system messages, tools, JSON mode, context length, and tokenization.

## Steps

1. **Record the source behavior.** Save source prompt version, model, parameters, outputs, and metrics. → *Expect:* a reproducible baseline report.
2. **Map provider features.** [BRANCH: Anthropic | OpenAI | open model] Compare system prompt handling, tool schema, structured output, context window, and safety filters. → *Expect:* a table of equivalent or missing features.
3. **Translate request format.** Adapt message roles, tool definitions, and structured-output settings without changing task intent. → *Expect:* the target API accepts the request and returns a response.
4. **Re-tune concise instructions.** Some models need more explicit output constraints or fewer examples. → *Expect:* parse rate and task score improve on a development set.
5. **Run the same held-out eval.** Compare source and target on quality, safety, latency, and cost. ⚠️ *Data leaves your control:* moving providers may send data to a new third party; confirm approval before testing private inputs. → *Expect:* a side-by-side report.
6. **Update version and rollout plan.** Treat the adapted prompt as a new version with rollback. → *Expect:* logs distinguish source and target prompt/model combinations.

## Decision points

- Target lacks strict JSON support → add schema validation and retries or choose a different model.
- Quality drops on critical cases → keep source model for that route or add retrieval/tools.
- Cost improves but safety worsens → do not migrate until guardrails pass.

## Failure modes & recovery

- **F1 Role mismatch:** detect target ignores system-like rules → move durable constraints to the provider's highest-priority supported channel.
- **F2 Tool schema incompatibility:** detect rejected tool definitions → simplify schemas and validate locally.
- **F3 Token overflow:** detect context-length errors → recount with target tokenizer and compress prompt.
- **F4 Safety behavior shift:** detect new refusal or under-refusal patterns → recalibrate guardrails and eval thresholds.

## Verification

Run `python compare_models.py --source source_config.yaml --target target_config.yaml --cases heldout.jsonl --max-quality-drop 0.02 --min-parse-rate 0.98`; the target must stay within 2 percentage points of source quality, meet parse-rate and safety thresholds, and satisfy the cost or latency goal.

## Variations

- `Claude Sonnet to Claude Opus`: keep API shape similar but re-check cost and latency.
- `OpenAI to Anthropic`: translate tool and structured-output conventions carefully.
- `hosted to local model`: expect more prompt explicitness and add grammar or validator support.

## Safety & privacy

Medium risk because provider changes can alter data handling and safety behavior. Confirm privacy and compliance approvals, avoid testing sensitive data until approved, and keep rollback to the previous prompt-model pair.
