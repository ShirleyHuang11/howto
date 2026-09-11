---
name: set-up-a-scheduled-job
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

You add a scheduled CI job that runs at a predictable time, performs one bounded task, and reports success or failure in CI. The schedule is committed and can also be triggered manually for verification.

## Preconditions

- CI configuration is stored in the repository.
- The task command runs locally or in CI with a clear exit code.
- Required secrets already exist in the CI secret store, not in the repo.

## Steps

1. **Define the job purpose and cadence.** Choose one job such as nightly tests, weekly dependency audit, or daily data refresh, and convert the local timezone to UTC cron. → *Expect:* a cron expression such as `17 6 * * *` with the intended local run time documented in a comment.
2. **Create the scheduled workflow.** [BRANCH: GitHub Actions, add `.github/workflows/scheduled.yml` with `on: schedule` and `workflow_dispatch` | GitLab CI, add a normal job and create the schedule in CI/CD > Schedules] → *Expect:* the CI provider recognizes the workflow or scheduled pipeline.
3. **Pin the runtime and install dependencies.** Use explicit versions such as `actions/setup-node@v4` with `node-version: 22` or `actions/setup-python@v5` with `python-version: "3.12"`. → *Expect:* logs show the expected runtime version.
4. **Run the bounded task command.** Use the same command a developer would run, such as `npm run audit:ci`, `pytest -q tests/nightly`, or `python scripts/refresh_index.py --check`. → *Expect:* the command exits 0 when the task succeeds and nonzero on failure.
5. **Add timeouts and concurrency control.** Set a job timeout and prevent overlapping runs. [BRANCH: GitHub Actions, use `timeout-minutes` and `concurrency` | GitLab CI, use `timeout` and `resource_group`] → *Expect:* a stuck or duplicate run is canceled or blocked by CI.
6. **Run it manually once.** Trigger the manual path. [BRANCH: GitHub Actions, `gh workflow run scheduled.yml` then `gh run watch` | GitLab CI, run the pipeline schedule manually from the UI] → *Expect:* the manual run completes and shows the scheduled job result.
7. **Check the next scheduled time.** Inspect the provider schedule page or workflow metadata. → *Expect:* the next run time matches the intended UTC cadence.

## Decision points

- Job needs production credentials → use least-privilege CI secrets and require review before changing scope.
- Job can overlap itself → add concurrency before enabling the schedule.
- Task may mutate external state → add a dry-run or `--check` mode first.
- Runtime exceeds normal CI minutes → move heavy work to a dedicated worker and let CI trigger it.

## Failure modes & recovery

- **F1 Cron runs at the wrong local time:** detect schedule firing hours off → recalculate in UTC and account for daylight saving if the provider cron is UTC-only.
- **F2 Scheduled job never starts:** detect no runs after the expected time → confirm schedules are enabled on the default branch and the workflow file is present there.
- **F3 Missing secret:** detect `401`, `403`, or "secret not found" logs → add the secret in the CI provider and rerun manually.
- **F4 Overlapping runs corrupt state:** detect concurrent job logs or lock conflicts → add provider concurrency and an application-level lock.

## Verification

Manual execution of the scheduled workflow exits 0, and the CI provider shows an enabled schedule with the expected next run time. For GitHub Actions, `gh run list --workflow scheduled.yml --limit 1` shows `conclusion: success`.

## Variations

- `GitHub Actions`: schedules run from the default branch and use UTC cron.
- `GitLab CI`: schedules are configured in the web UI or API and can set variables per schedule.
- `Kubernetes CronJob`: use `kubectl create job --from=cronjob/<name> <manual-name>` to verify the container outside CI.
- `cloud scheduler`: CI may only deploy the scheduler; verify with the cloud provider's job history.

## Safety & privacy

Medium risk because scheduled jobs can repeatedly mutate data or consume quota. Keep secrets in the CI secret store, scope tokens to the specific API, set timeouts, and make destructive scheduled work require explicit approval outside the schedule.
