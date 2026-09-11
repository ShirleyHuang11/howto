---
name: version-an-api
domain: engineering
subdomain: api
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

Introduce or maintain API versions so clients keep working while new behavior ships under an explicit compatibility contract.

## Preconditions

- Existing clients and breaking-change candidates are known.
- Routing, documentation, and tests can distinguish versions.
- Deprecation communication channels exist for external clients.

## Steps

1. **Classify the change.** Decide whether it is additive, behavior-changing, or breaking. → *Expect:* only breaking changes require a new major version.
2. **Choose the versioning mechanism.** Use URL path such as `/v1/...`, media type, or header based on project convention. → *Expect:* clients can explicitly request the intended version.
3. **Keep old behavior intact.** Preserve existing handlers or compatibility transforms for current clients. → *Expect:* v1 contract tests still pass unchanged.
4. **Add the new version route or schema.** Implement `/v2/...` or equivalent with the new request and response shape. → *Expect:* v2 tests pass without changing v1 expectations.
5. **Document both versions.** Update OpenAPI or docs with version-specific schemas and deprecation notices. → *Expect:* generated docs show the correct version behavior.
6. **Add compatibility tests.** Run contract tests for every supported version in CI. → *Expect:* a change that breaks v1 fails CI.
7. **Plan deprecation separately.** Announce timeline, metrics, and removal criteria before deleting old code. → *Expect:* client migration status is measurable.

## Decision points

- Change only adds optional response fields → keep same version.
- Required request field changes → create a new version or support both shapes.
- Internal clients only → still use tests and a migration window.
- Old version has no traffic → verify logs before removal.

## Failure modes & recovery

- **F1 Silent breaking change:** detect client errors after deploy → roll back or restore compatibility transform.
- **F2 Docs drift:** detect OpenAPI differs from handlers → add generated spec validation to CI.
- **F3 Version routing ambiguity:** detect requests hitting the wrong handler → make version parsing explicit and tested.
- **F4 Premature removal:** detect active traffic on removed version → redeploy old handler and restart deprecation process.

## Verification

Version-specific contract tests exit 0, `curl -sS "$BASE_URL/v1/resource"` returns the old documented shape, and `curl -sS "$BASE_URL/v2/resource"` returns the new documented shape.

## Variations

- `Path versioning`: simplest for public REST APIs and gateway routing.
- `Header versioning`: useful when URLs must remain stable, but requires strict client behavior.
- `OpenAPI`: publish separate specs per major version or clearly separated version paths.

## Safety & privacy

Medium risk because compatibility mistakes break clients. Track version usage, keep old tests running, avoid exposing new sensitive fields in old versions, and require explicit approval before removing a supported version.
