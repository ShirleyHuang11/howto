---
name: tear-down-a-staging-environment
domain: engineering
subdomain: deploy
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You remove a staging environment and its dependent resources without deleting production assets or losing data that still needs to be retained.

## Preconditions

- The environment name, account/project, region, and resource tags are known.
- Owners confirm the staging environment is no longer needed.
- Any data retention, snapshots, or audit requirements are documented.
- You have read access to inventory and write access to delete staging resources only.

## Steps

1. **Identify the exact environment.** Run an inventory command such as `terraform workspace show`, `kubectl config current-context`, or cloud tag search for `env=staging`. → *Expect:* every target resource is clearly labeled staging and no production identifiers are present.
2. **Announce teardown intent.** Post the environment name, resource list, and planned time to the owning team. → *Expect:* owners acknowledge that no active test or demo depends on it.
3. **Back up retained state.** If the staging database or object storage must be kept, take a snapshot or export before deletion. → *Expect:* backup or retention artifact exists and is restorable.
4. **Disable incoming traffic.** Remove DNS records, load balancer routes, or ingress rules for the staging hostname. → *Expect:* new public traffic no longer reaches the staging app.
5. **Run a deletion plan.** [BRANCH: Terraform | Kubernetes | cloud console] For Terraform, run `terraform plan -destroy -out=tfplan`; for Kubernetes, run `kubectl get all -n staging`. → *Expect:* the plan lists only staging resources intended for deletion.
6. **Apply the teardown.** ⚠️ *Irreversible:* deleting environments can destroy databases and storage; confirm the account, region, workspace, and resource list before running `terraform apply tfplan` or equivalent. → *Expect:* the deletion command completes without touching production resources.
7. **Remove orphaned resources.** Check for volumes, snapshots, DNS records, secrets, buckets, and service accounts left behind. → *Expect:* only approved retained artifacts remain.
8. **Verify cost and access cleanup.** Check billing/resource inventory and revoke environment-specific credentials. → *Expect:* staging resources stop appearing in inventory and credentials are disabled or removed.

## Decision points

- Any resource lacks clear environment tagging → stop and ask the owner before deleting.
- Staging contains irreplaceable test data → snapshot or export before teardown.
- Shared resources are used by production and staging → remove only staging attachments, not the shared parent resource.
- Teardown is temporary → scale to zero or suspend instead of deleting durable state.

## Failure modes & recovery

- **F1 Production resource appears in plan:** detect prod name, account, or tag in the deletion plan → abort and correct workspace, variables, or filters.
- **F2 Deletion blocked by dependencies:** detect dependency or finalizer errors → remove dependent routes, volumes, or finalizers only after confirming ownership.
- **F3 Orphaned cost remains:** detect charges or unattached volumes after teardown → list resources by tag and delete or document retained artifacts.
- **F4 Needed environment deleted:** detect owner reports active dependency after deletion → restore from snapshot or redeploy from infrastructure code.

## Verification

The deletion plan/apply exits 0, cloud or cluster inventory for `env=staging` returns no active compute/load balancer/database resources except approved retained backups, and the staging URL no longer resolves or returns service traffic.

## Variations

- `Terraform`: use `terraform plan -destroy -out=tfplan` and review the saved plan before `terraform apply tfplan`.
- `Kubernetes`: delete the namespace only after confirming it contains no shared resources; verify with `kubectl get ns staging`.
- `Cloud console`: use tags and account/region filters, then export a resource list before deleting.

## Safety & privacy

High risk because teardown can permanently delete data and infrastructure. Confirm account, region, and tags aloud or in writing, keep backups where required, revoke staging secrets, and never delete resources with ambiguous ownership.
