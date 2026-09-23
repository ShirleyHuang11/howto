---
name: set-up-regression-evals
domain: ai
subdomain: evals
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [ai/evals/build-an-eval-set, ai/evals/measure-task-accuracy]
status: draft
last_verified: 2026-09-22
---

## Goal

You add repeatable evals that catch quality regressions before a prompt, model, retrieval, or tool change ships. The regression suite runs automatically and fails builds below threshold.

## Preconditions

- A small, stable eval set with expected outputs or scoring rules.
- A command that runs the application in test mode.
- CI or a scheduled job with access to required secrets.

## Steps

1. **Select regression examples.** Include known incidents, common workflows, edge cases, and safety-critical prompts. → *Expect:* a compact suite that runs quickly and represents must-not-break behavior.
2. **Pin runtime configuration.** Record model id, prompt version, retrieval index version, tool mocks, and decoding settings. → *Expect:* changes are intentional and visible in diffs.
3. **Write the runner.** Implement `python evals/regression.py --config evals/regression.yaml` to produce `results.json`. → *Expect:* local runs return per-example pass/fail and aggregate metrics.
4. **Set gates.** Define minimum overall and per-slice thresholds, plus hard failures for safety or schema violations. → *Expect:* a failing example causes a nonzero exit code.
5. **Mock risky tools.** Replace email, payment, database writes, and destructive tools with fixtures. → *Expect:* evals can run without touching production state.
6. **Add CI execution.** Store only approved API keys and cap concurrency/cost. ⚠️ *Data leaves your control:* CI may send eval examples to external model APIs; use sanitized datasets. → *Expect:* each pull request shows eval pass/fail and summary artifacts.

## Decision points

- Suite is too slow → split smoke evals for PRs and full evals nightly.
- Flakiness exceeds tolerance → lower temperature, cache fixed outputs, or require repeated failure before blocking.
- External API unavailable → mark infrastructure failure separately from model regression.

## Failure modes & recovery

- **F1 Silent prompt drift:** detect prompt hash differs from recorded config → fail and require explicit version bump.
- **F2 Flaky gate:** detect pass/fail changes on rerun → stabilize model settings or use confidence bands.
- **F3 Tool side effects:** detect real writes during eval → block network/tool credentials and use mocks.
- **F4 Dataset rot:** detect labels no longer match product behavior → review and version the dataset.

## Verification

CI runs the regression command, uploads `results.json`, and exits nonzero when overall score or any critical slice falls below threshold. A seeded local run and CI run produce the same example count, config hash, and pass/fail decisions except for documented provider nondeterminism.

## Variations

- `nightly`: run larger, costlier suites off the main PR path.
- `offline`: evaluate cached outputs when provider access is unavailable.
- `agent`: assert final state and mocked tool calls, not just text.

## Safety & privacy

Use sanitized evals, least-privilege secrets, mocked write tools, and hard budget caps. Regression evals should never send real customer data or mutate production systems.
