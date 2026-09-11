---
name: deploy-a-serverless-function
domain: engineering
subdomain: deploy
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min-2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You deploy a serverless function from a known source revision and verify invocation, logs, permissions, and rollback target. The function handles a real request successfully in the target environment.

## Preconditions

- The function has a handler, runtime version, and deployment configuration.
- Cloud credentials or provider tokens are available with least privilege.
- Required environment variables and secrets exist in the provider.
- A test event or HTTP route is known.

## Steps

1. **Identify the function and runtime.** Record function name, region, runtime, handler, source commit, and trigger type. → *Expect:* deployment notes identify exactly what will change.
2. **Run local tests and packaging checks.** Execute `npm test`, `pytest`, `go test ./...`, or provider local invoke. → *Expect:* tests exit 0 and packaging includes handler dependencies.
3. **Build or package the function.** [BRANCH: AWS Lambda zip, create a zip or container image | Google Cloud Functions, prepare source directory | Cloudflare Workers, run `wrangler deploy --dry-run` if available] → *Expect:* package build exits 0.
4. **Deploy to the target environment.** [BRANCH: AWS SAM, `sam deploy --config-env prod` | Serverless Framework, `serverless deploy --stage prod` | Cloudflare Workers, `wrangler deploy --env production`] ⚠️ *Irreversible:* production invocations may route to the new function version; confirm function name, region, and rollback version before deploying. → *Expect:* provider returns a deployment, version, or release ID.
5. **Verify configuration and permissions.** Inspect environment variables, IAM role, triggers, and timeout/memory settings. → *Expect:* settings match the deployment config and no broad new permissions appear unexpectedly.
6. **Invoke the function with a safe test event.** [BRANCH: HTTP, `curl -fsS https://<route>` | AWS Lambda, `aws lambda invoke --function-name <name> --payload file://event.json out.json`] → *Expect:* invocation returns success status and expected response body.
7. **Check logs and metrics.** Read recent logs for cold-start errors, permission denials, and exceptions. → *Expect:* no new error entries for the verification request.
8. **Record rollback target.** Note previous version, alias, release, or deployment ID. → *Expect:* rollback can be executed without searching during an incident.

## Decision points

- Function is event-driven → verify with a synthetic event and confirm downstream side effects are safe.
- IAM permissions changed → require review before deployment.
- Package size is large → prune dev dependencies or use layers/container images.
- Cold starts are unacceptable → configure provisioned concurrency or edge/runtime alternatives.

## Failure modes & recovery

- **F1 Handler not found:** detect runtime error about missing handler → correct handler path and package contents.
- **F2 Permission denied:** detect `AccessDenied`, `403`, or missing scope logs → update least-privilege role and redeploy.
- **F3 Timeout or OOM:** detect timeout, memory exceeded, or killed invocation → optimize code or adjust timeout and memory within policy.
- **F4 Trigger not connected:** detect deploy succeeds but no invocations arrive → verify event source mapping, route, subscription, or queue binding.

## Verification

The provider deployment command exits 0, a safe invocation returns the expected status or payload, and recent function logs for that invocation contain no unhandled exceptions or permission errors.

## Variations

- `AWS Lambda`: deploy zip, container image, SAM, CDK, Terraform, or Serverless Framework; verify aliases and versions.
- `Google Cloud Functions/Cloud Run functions`: verify region, trigger, service account, and logs.
- `Azure Functions`: use deployment slots where available and verify Application Insights.
- `Cloudflare Workers`: deploy with Wrangler and verify route bindings and environment variables.

## Safety & privacy

Medium risk because function triggers can process production events immediately. Use least-privilege roles, avoid logging event payload secrets, confirm region and stage, and keep rollback aliases or previous versions available.
