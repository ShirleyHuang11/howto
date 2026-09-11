---
name: do-a-post-deploy-smoke-test
domain: engineering
subdomain: deploy
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You verify immediately after a deploy that the released version is live, core user flows work, and key service health checks remain green.

## Preconditions

- A deployment has completed and the target environment is known.
- The expected version, commit SHA, or build ID is available.
- Smoke-test credentials or test fixtures exist and are safe to use.
- Monitoring and logs are accessible for the deployed service.

## Steps

1. **Confirm the deployed version.** Run `curl -fsS https://app.example.com/version` or check the deployment dashboard. → *Expect:* the returned version matches the intended build or commit.
2. **Check public health.** Run `curl -fsS -o /dev/null -w '%{http_code}\n' https://app.example.com/healthz`. → *Expect:* `200`.
3. **Run the automated smoke suite.** Use the repo command such as `npm run smoke -- --base-url=https://app.example.com` or `pytest -m smoke --base-url=https://app.example.com`. → *Expect:* the smoke suite exits 0.
4. **Exercise one critical authenticated flow.** Log in with a test account or run an API request using a smoke-test token. → *Expect:* authentication succeeds and the expected page or API response loads.
5. **Verify dependency integration.** Test one database-backed read and one external integration stub or sandbox call. → *Expect:* dependencies respond without 5xx, 401, or timeout errors.
6. **Inspect fresh error signals.** Check error-rate dashboards, logs, and alert channels for the deploy window. → *Expect:* no new high-severity errors or alert pages.
7. **Record the result.** Post pass/fail, version, environment, and any anomalies in the deployment channel or release record. → *Expect:* the deploy has an auditable smoke-test outcome.

## Decision points

- Smoke suite fails on a critical path → start rollback or hotfix decision immediately.
- Smoke suite fails on a known flaky check but health is stable → rerun once, then investigate before declaring success.
- Version endpoint does not match intended build → stop testing and fix routing or deployment selection.
- Error rate is elevated despite passing smoke tests → hold rollout and inspect logs before exposing more traffic.

## Failure modes & recovery

- **F1 Wrong build live:** detect version mismatch → redeploy the intended artifact or fix traffic routing before further testing.
- **F2 Authentication broken:** detect login 401/redirect loop → verify secrets, callback URLs, cookie domain, and identity provider config.
- **F3 Dependency timeout:** detect smoke tests hanging or 504 responses → check network policy, credentials, and dependency status.
- **F4 Silent partial outage:** detect smoke passes but dashboards show errors → compare affected routes and roll back if user impact is real.

## Verification

`curl -fsS https://app.example.com/version` returns the intended build, `curl -fsS -o /dev/null -w '%{http_code}\n' https://app.example.com/healthz` returns `200`, and the automated smoke command exits 0.

## Variations

- `Playwright`: run `npx playwright test --grep @smoke --project=chromium --base-url=<url>`.
- `pytest`: mark tests with `@pytest.mark.smoke` and pass the base URL through an environment variable.
- `Kubernetes`: verify rollout with `kubectl rollout status deployment/<name> -n <namespace>` before external smoke tests.

## Safety & privacy

Medium risk because smoke tests touch live systems. Use dedicated test accounts, never use real customer data for destructive checks, mask tokens in logs, and stop the rollout when smoke tests fail on critical paths.
