---
name: notify-a-channel-on-build-failure
domain: engineering
subdomain: cicd
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min-1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You configure CI to notify the right chat or incident channel only when a build fails or recovers. The notification includes enough context for an engineer to open the failed run and act.

## Preconditions

- Admin or maintainer access to the CI project and target chat integration.
- A webhook URL, app token, or provider-native integration stored as a CI secret.
- A workflow or pipeline that already runs on pull requests or pushes.

## Steps

1. **Choose the notification trigger.** Decide whether to notify on default-branch failures, release failures, all PR failures, or recovery after failure. → *Expect:* a written rule such as "notify `#builds` only for failed `main` runs and deployment workflows".
2. **Create the chat destination securely.** Add a Slack incoming webhook, Teams webhook, or provider integration, then store the URL as `BUILD_ALERT_WEBHOOK_URL` in CI secrets. → *Expect:* the secret exists in the CI settings and is not printed in logs.
3. **Add a failure-only notification step.** [BRANCH: GitHub Actions, use `if: failure()` or a final job with `if: ${{ failure() }}` | GitLab CI, use `when: on_failure`] → *Expect:* the notification step is skipped on success and eligible only after failure.
4. **Include actionable build context.** Send repository, branch, commit SHA, author, workflow name, and run URL. → *Expect:* a test payload contains a direct link to the failed run.
5. **Prevent secret exposure in logs.** Do not echo the raw webhook; use masked CI variables and `curl --fail-with-body` without verbose mode. → *Expect:* logs show masked values or no webhook value.
6. **Trigger a controlled failure on a temporary branch.** Add a harmless failing command such as `false` in the test branch or run a manual workflow input that exits 1. → *Expect:* CI fails and exactly one channel notification appears.
7. **Remove the injected failure and confirm silence on green.** Restore the workflow and rerun. → *Expect:* CI exits 0 and no failure alert is posted.

## Decision points

- Alert noise is high → restrict notifications to protected branches or deployment workflows.
- Team uses provider-native integrations → prefer them over custom webhook scripts when they include run links.
- Compliance requires auditability → post through an app with a named identity instead of an anonymous webhook.
- Failures need paging → route deploy or production-impacting failures to incident tooling, not a casual chat channel.

## Failure modes & recovery

- **F1 No alert on failure:** detect failed CI without a chat message → verify the conditional expression and that the secret is available to the event type.
- **F2 Alert on every successful run:** detect noisy success messages → change the step condition to failure-only or provider `on_failure`.
- **F3 Webhook returns 401 or 403:** detect HTTP auth errors → rotate or reinstall the chat webhook and update the CI secret.
- **F4 Duplicate alerts:** detect multiple messages for one run → centralize notification in one final job that depends on all required jobs.

## Verification

A deliberately failed CI run exits nonzero and posts one message to the configured channel with a working CI run URL; a subsequent successful run exits 0 and posts no failure message.

## Variations

- `Slack`: incoming webhooks accept JSON with a `text` field; Slack apps can use richer Block Kit messages.
- `Microsoft Teams`: workflow webhooks often require an adaptive-card payload rather than Slack JSON.
- `GitHub Actions`: notification jobs can use `needs` plus `if: ${{ failure() }}` after the build matrix.
- `GitLab CI`: use `after_script` carefully because it may run for canceled jobs; `when: on_failure` is usually clearer.

## Safety & privacy

Medium risk because notifications can leak branch names, commit messages, or internal URLs. Keep webhook URLs secret, avoid posting logs or environment variables, and limit alerts to channels with the same audience as the repository.
