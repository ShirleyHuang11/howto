---
name: a-b-test-two-models
domain: ai
subdomain: evals
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 2h
risk: high
prerequisites: [ai/evals/measure-task-accuracy, ai/evals/measure-latency-and-cost]
status: draft
last_verified: 2026-09-22
---

## Goal

You run a controlled online A/B test comparing two model variants on real traffic. The test measures quality, safety, latency, and cost before any full rollout.

## Preconditions

- Offline evals show the candidate is safe enough for limited exposure.
- Experiment assignment, logging, and rollback mechanisms exist.
- Success metrics, guardrails, and minimum sample size are predeclared.

## Steps

1. **Pre-register the experiment.** Define hypothesis, primary metric, guardrails, exposure, duration, and stop criteria. → *Expect:* a written plan that prevents moving goalposts.
2. **Implement stable assignment.** Hash user or conversation id to control or treatment and log the assignment. → *Expect:* users receive a consistent variant during the test.
3. **Start with low exposure.** ⚠️ *Irreversible:* live users may receive worse outputs; confirm rollback, monitoring, and support escalation before launch. → *Expect:* treatment receives a small percentage such as 1-5% of eligible traffic.
4. **Log comparable events.** Capture prompt version, model, latency, token cost, user feedback, task success, and safety events. → *Expect:* every metric can be grouped by arm.
5. **Monitor guardrails.** Check error rate, refusal spikes, safety complaints, p95 latency, and cost daily. → *Expect:* automatic alerts or dashboards show no breached guardrail.
6. **Analyze after sample size.** Use the predeclared statistical test and report effect size with confidence interval. → *Expect:* a decision to ship, iterate, or stop.

## Decision points

- Any safety guardrail breaches → stop treatment and investigate before relaunch.
- Quality improves but cost exceeds budget → consider routing only hard cases to the candidate.
- No significant difference → keep the cheaper or faster model unless qualitative review says otherwise.

## Failure modes & recovery

- **F1 Sample-ratio mismatch:** detect observed assignment differs from expected split → stop and fix assignment/logging.
- **F2 Interference:** detect users see both variants for one task → assign at user or conversation level.
- **F3 Metric logging gap:** detect missing events in one arm → invalidate affected period and rerun.
- **F4 Harmful treatment output:** detect incident reports → rollback immediately and add the case to red-team evals.

## Verification

The experiment dashboard shows correct sample ratio, no breached guardrails, complete metric logging for both arms, and a predeclared statistical result with confidence interval. A rollout proceeds only if the primary metric improves or is non-inferior and safety/cost thresholds pass.

## Variations

- `shadow test`: run candidate without showing output to users for safer telemetry.
- `interleaving`: compare ranked lists within the same session when appropriate.
- `multi-arm bandit`: use only after safety gates and with clear regret controls.

## Safety & privacy

Online tests are high risk because real users are affected. Use minimal exposure, fast rollback, privacy-preserving logs, incident monitoring, and explicit approval for any treatment that changes safety behavior.
