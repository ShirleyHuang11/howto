---
name: roll-forward-a-hotfix
domain: engineering
subdomain: deploy
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 1h-2h
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You fix a production issue by shipping a minimal forward change, verify the corrected behavior, and avoid broad unrelated changes during the incident.

## Preconditions

- The production issue, affected version, and user impact are confirmed.
- Rollback is unsuitable, riskier, or already attempted unsuccessfully.
- You have permission to deploy to production and access to CI/CD.
- A small targeted fix and test can be made without restructuring the system.

## Steps

1. **Freeze the scope.** Identify the exact failing behavior, affected environment, and success predicate. → *Expect:* one-sentence hotfix objective and owner in the incident or deploy channel.
2. **Create the smallest code change.** Edit only the files needed for the production fix and add or update a focused regression test. → *Expect:* the diff is narrow and directly tied to the incident.
3. **Run local verification.** Execute the targeted test and relevant lint/build command, such as `pytest tests/test_bug.py -q` or `npm test -- --runTestsByPath path/to/test`. → *Expect:* targeted checks exit 0.
4. **Open the hotfix review.** Ask for expedited review from the service owner and incident commander. → *Expect:* at least one qualified reviewer approves the narrow change.
5. **Let CI validate the change.** Wait for required CI jobs and deployment gates. → *Expect:* required checks are green on the hotfix revision.
6. **Deploy the hotfix to production.** ⚠️ *Irreversible:* production deploys can affect all users; confirm the target environment, artifact version, and rollback option before promoting. → *Expect:* the deploy system reports success for the hotfix build.
7. **Run post-deploy smoke tests.** Execute the specific incident reproduction check plus normal health checks. → *Expect:* the failing behavior is fixed and public health returns 200.
8. **Close the incident loop.** Update status, note the fixed version, and create follow-up work for root cause or cleanup. → *Expect:* responders and stakeholders can see the verified resolution.

## Decision points

- Rollback would restore service faster and safely → rollback instead of rolling forward.
- Fix requires a risky migration or broad refactor → mitigate first, then plan a normal release.
- CI is red on unrelated flaky jobs → rerun once; do not bypass required checks without incident commander approval.
- Hotfix changes public behavior → document customer impact and support messaging before deploy.

## Failure modes & recovery

- **F1 Fix does not reproduce locally:** detect no failing test before the change → add a reproduction or use production logs to define a stronger check.
- **F2 CI fails:** detect required checks red → fix the hotfix branch or revert unrelated test changes; do not deploy a red artifact without explicit emergency approval.
- **F3 Deploy fails midway:** detect deployment pipeline error or unhealthy rollout → pause rollout, inspect deploy logs, and roll back if the old version is healthier.
- **F4 Hotfix misses the issue:** detect incident symptom persists after deploy → stop further changes, reassess root cause, and consider rollback or feature disablement.

## Verification

The hotfix artifact is deployed to production, `curl -fsS -o /dev/null -w '%{http_code}\n' https://app.example.com/healthz` returns `200`, and the incident-specific regression check or smoke test exits 0 against production.

## Variations

- `Feature flag`: disable or narrow exposure first, then ship the permanent hotfix through normal CI.
- `Canary deploy`: send a small traffic percentage to the hotfix and verify metrics before full promotion.
- `Mobile/client release`: roll-forward may require expedited app review or remote config rather than immediate server deploy.

## Safety & privacy

High risk because this changes production during an incident. Keep the diff minimal, protect secrets in logs and incident notes, require explicit production deploy approval, and record who approved any bypass of normal release gates.
