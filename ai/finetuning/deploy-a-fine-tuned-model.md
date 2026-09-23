---
name: deploy-a-fine-tuned-model
domain: ai
subdomain: finetuning
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 2h
risk: high
prerequisites: [ai/finetuning/evaluate-a-fine-tuned-model]
status: draft
last_verified: 2026-09-22
---

## Goal

You deploy a fine-tuned model behind a controlled inference endpoint with rollback, monitoring, and release gates. The deployment is live only after automated checks and human approval for high-risk changes.

## Preconditions

- A fine-tuned model or adapter that passed held-out evaluation.
- A serving stack, such as hosted fine-tune endpoint, vLLM, TGI, Triton, or managed model gateway.
- Rollback target, monitoring dashboard, and alerting for quality, latency, error rate, and cost.

## Steps

1. **Package the model artifact.** Include model ID, adapter files, tokenizer, chat template, eval report, and license notes. → *Expect:* the artifact loads in a staging server.
2. **Create a staging endpoint.** [BRANCH: hosted endpoint | self-hosted vLLM/TGI] Deploy without production traffic first. → *Expect:* health check returns HTTP 200 and a smoke prompt returns a valid response.
3. **Run pre-production checks.** Execute format, safety, latency, and cost smoke tests against staging. → *Expect:* checks pass with the same thresholds used in the eval report.
4. **Configure routing and rollback.** Set canary percentage, fallback model, timeout, and kill switch. → *Expect:* a rollback command or config change is tested in staging.
5. **Approve production rollout.** ⚠️ *Irreversible:* production deployment can affect users and spend real money; confirm eval pass, rollback target, access controls, and monitoring before switching traffic. → *Expect:* an approval record links to artifact and eval IDs.
6. **Canary traffic gradually.** Start with a small percentage and monitor quality, refusal rate, latency, error rate, and cost. → *Expect:* dashboards show canary metrics next to baseline.
7. **Promote or rollback.** Increase traffic only while all gates hold; rollback immediately on safety, quality, or cost breach. → *Expect:* final state is either promoted with metrics or rolled back with incident notes.

## Decision points

- Staging smoke tests fail → do not canary; fix serving template or artifact packaging.
- Canary quality drops below threshold → rollback and inspect examples.
- Cost per request exceeds budget → reduce traffic, quantize, or use selective routing.
- Safety alert fires → rollback immediately and preserve logs for review.

## Failure modes & recovery

- **F1 Template mismatch:** detect staging outputs with wrong roles or formatting → align serving chat template with training.
- **F2 Adapter not loaded:** detect base-model behavior and missing adapter logs → fix model load config and rerun staging checks.
- **F3 Latency spike:** detect p95 above SLA → reduce max tokens, scale replicas, or rollback.
- **F4 Cost runaway:** detect spend rate above budget → activate kill switch and lower traffic.
- **F5 Silent quality regression:** detect user feedback or eval shadow traffic decline → rollback and add the case to evals.

## Verification

Deployment is successful only when staging health checks pass, automated smoke evals pass, production canary metrics remain within thresholds for the observation window, rollback has been tested, and monitoring confirms the intended model or adapter ID is serving traffic.

## Variations

- `hosted fine-tune`: deploy via provider model ID and managed endpoint controls.
- `adapter serving`: load base model once and attach LoRA adapters per route.
- `shadow deployment`: run the fine-tune alongside production without returning its output before canarying.

## Safety & privacy

This is high risk because production users, data, and budget are affected. Limit access to the endpoint, log only necessary data, protect prompts and outputs, cap spend, and require review before any full-traffic rollout.
