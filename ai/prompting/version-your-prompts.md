---
name: version-your-prompts
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

You version prompts so every model output can be traced to the exact prompt text, model settings, and evaluation result that produced it.

## Preconditions

- Prompt files or templates stored outside application code or clearly separated inside it.
- A place to record prompt metadata, such as a manifest, database table, or observability event.
- Eval cases that can run before promotion.

## Steps

1. **Assign a prompt id.** Use a stable id such as `support_triage.v1` or a content hash. → *Expect:* each prompt has a unique identifier.
2. **Record model settings.** Store model name, temperature, max tokens, tools, schema, and retrieval configuration with the prompt version. → *Expect:* a manifest can reproduce the request shape.
3. **Hash rendered prompt text.** Compute a SHA-256 hash after template rendering for test fixtures. → *Expect:* accidental edits change the hash and fail snapshots.
4. **Run evals before promotion.** Compare the candidate prompt against the current production prompt. → *Expect:* a report with primary metric, parse rate, cost, and regression cases.
5. **Log version on every call.** Include prompt id and version in request metadata or application logs. → *Expect:* any output can be traced back to prompt version.
6. **Promote with rollback path.** Mark the new version active only after metrics pass. → *Expect:* configuration can switch back to the previous version without code edits.

## Decision points

- Prompt behavior changes materially → create a new version, not an in-place edit.
- Eval score regresses beyond tolerance → do not promote.
- Multiple teams use the prompt → require review and changelog before promotion.

## Failure modes & recovery

- **F1 Untracked hotfix:** detect production output with unknown prompt hash → block deployment or restore from manifest.
- **F2 Model drift:** detect same prompt version changing behavior after model upgrade → version model settings with the prompt.
- **F3 Missing rollback:** detect active prompt only in code branch → move selection to config or feature flag.
- **F4 Eval mismatch:** detect eval uses stale template variables → render eval prompts through the same production path.

## Verification

Run `python verify_prompt_versions.py --manifest prompts/manifest.yaml --logs sample_logs.jsonl`; every prompt file has a unique id, hash, and eval report, and every sampled log line contains a known prompt version and hash.

## Variations

- `Git-backed`: use file history plus a manifest and eval artifacts.
- `Prompt registry`: store versions, metrics, and deployment status in a service.
- `Experiment platform`: attach prompt version to A/B assignments and observability traces.

## Safety & privacy

Version metadata is usually safe, but full prompt logs may contain user data or proprietary instructions. Store hashes and ids by default, restrict access to full prompts, and review before promoting prompts that affect user outcomes.
