---
name: define-an-slo
domain: engineering
subdomain: observability
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

You define a measurable service level objective with an SLI, target, window, and error budget that reflects user experience.

## Preconditions

- The service has enough telemetry to measure availability, latency, correctness, or freshness.
- Product and engineering owners agree which user journey matters.
- Historical data is available to evaluate a proposed target.

## Steps

1. **Pick the user journey.** Choose one important path such as successful checkout, API read availability, or data freshness. → *Expect:* the SLO maps to a user-visible outcome, not an internal convenience metric.
2. **Define the SLI.** Write the numerator and denominator, for example `good HTTP requests / total eligible HTTP requests`. → *Expect:* the SLI can be computed from existing metrics or logs.
3. **Set inclusion rules.** Exclude invalid traffic such as health checks, test users, and client-caused 4xx where appropriate. → *Expect:* the calculation does not punish the service for traffic outside its responsibility.
4. **Choose target and window.** Pick a target such as `99.9% over 30 days` based on user needs and historical performance. → *Expect:* the target is ambitious but achievable.
5. **Calculate error budget.** Compute `1 - target`, for example 99.9% allows 0.1% bad events in the window. → *Expect:* the team knows how much unreliability is tolerable.
6. **Implement the query.** For Prometheus, create recording rules for good and total events, then compute the ratio. → *Expect:* the SLI query returns a stable time series.
7. **Create burn-rate alerts and dashboard.** Add fast and slow burn alerts and a dashboard showing SLI, target, and budget remaining. → *Expect:* responders can see when the objective is at risk.
8. **Document policy.** Record what happens when budget is exhausted, such as freeze risky launches or prioritize reliability work. → *Expect:* the SLO has operational consequences.

## Decision points

- User journey has low volume → use longer windows or synthetic checks to avoid noisy percentages.
- Latency SLO → define the threshold as good events under a latency bound, not just average latency.
- Data pipeline SLO → use freshness and completeness instead of HTTP availability.
- Proposed target already fails historically → lower target temporarily or improve reliability before adopting it.

## Failure modes & recovery

- **F1 Unmeasurable SLI:** detect missing denominator or inconsistent labels → add instrumentation before publishing the SLO.
- **F2 Vanity target:** detect target chosen without user or historical basis → review with owners and compare past performance.
- **F3 Alert fatigue:** detect frequent burn alerts without actionable impact → tune burn rates, windows, and traffic guards.
- **F4 Perverse incentives:** detect teams ignoring real incidents outside the SLO → add another SLO or revise the user journey.

## Verification

The SLI query returns a numeric percentage over the chosen window, the dashboard shows target and budget remaining, and a documented SLO page records the SLI formula, target, window, owner, and response policy.

## Variations

- `Prometheus`: use recording rules and multi-window multi-burn-rate alerts.
- `Datadog SLO`: create metric-based or monitor-based SLOs with tags for service and environment.
- `Google Cloud Monitoring`: use service monitoring SLOs and alert policies.
- `Incident-heavy service`: begin with an internal objective before making an external commitment.

## Safety & privacy

Medium risk because SLOs influence launch and incident decisions. Do not define public commitments without stakeholder approval, avoid exposing customer-specific reliability data, and keep SLO ownership explicit.
