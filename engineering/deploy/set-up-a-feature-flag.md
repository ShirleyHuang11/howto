---
name: set-up-a-feature-flag
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

You place new behavior behind a feature flag that can be enabled, disabled, and targeted without redeploying. The flag has a default-safe value and automated tests for both paths.

## Preconditions

- A feature flag service, config system, or environment-based flag mechanism is available.
- The codebase has tests around the affected behavior.
- Product and engineering agree on the default state and rollout owner.

## Steps

1. **Define the flag contract.** Choose a stable key, owner, default value, description, and planned removal date. → *Expect:* the flag is named clearly, such as `checkout.new_tax_calculator`, with default `false`.
2. **Create the flag in the flag system.** [BRANCH: LaunchDarkly/Statsig/Unleash, create a boolean flag with targeting off | config file, add a typed boolean setting] → *Expect:* the flag exists and evaluates to the safe default in production.
3. **Add typed flag access in code.** Centralize evaluation through an existing config or flag client wrapper. → *Expect:* code reads one typed helper rather than scattered string literals.
4. **Guard the new behavior.** Keep old behavior in the `false` branch and new behavior in the `true` branch. → *Expect:* toggling the flag changes only the intended behavior.
5. **Write tests for both branches.** Mock or set the flag true and false in unit or integration tests. → *Expect:* both code paths pass and assertions prove the behavior differs correctly.
6. **Add observability.** Emit metrics or structured logs tagged with flag state for the affected path. → *Expect:* dashboards can compare enabled and disabled cohorts.
7. **Roll out to a small cohort first.** Enable the flag for internal users, a test tenant, or a low percentage. → *Expect:* targeted users see the new behavior and others remain on old behavior.
8. **Document rollback and cleanup.** Record how to turn the flag off and when to remove dead code. → *Expect:* an owner can disable the feature without a code deploy.

## Decision points

- Flag controls risky production behavior → default off and require manual approval for rollout.
- Flag affects schema or writes → ensure both branches can read existing and new data safely.
- Many flags already exist → follow the local naming, ownership, and expiration policy.
- Flag will be permanent permissioning → model it as product configuration, not a temporary rollout flag.

## Failure modes & recovery

- **F1 Default value unsafe:** detect production enables new behavior unintentionally → change default to safe false and add tests for missing flag values.
- **F2 Flag service outage:** detect evaluation errors or timeouts → use cached values or local defaults that fail closed.
- **F3 Tests cover only one branch:** detect coverage gap or untested branch → add explicit true and false test cases.
- **F4 Stale flag accumulates:** detect expired flag still in code → schedule cleanup after full rollout and remove dead branch.

## Verification

Automated tests pass for both flag states, and in a non-production or targeted production cohort the flag dashboard shows evaluations while `curl` or integration tests confirm the old behavior with the flag off and new behavior with it on.

## Variations

- `LaunchDarkly`: create a boolean flag, use SDK variation calls, and target users or segments.
- `Unleash`: use strategies for gradual rollout and constraints.
- `environment variable`: acceptable for deploy-time toggles, but changing it usually requires restart or redeploy.
- `frontend`: avoid exposing secrets or sensitive authorization decisions solely through client-side flags.

## Safety & privacy

Medium risk because flags can expose unfinished behavior or change production writes. Default to the safest value, restrict flag-edit permissions, avoid putting personal data in flag targeting rules unless necessary, and remove temporary flags after rollout.
