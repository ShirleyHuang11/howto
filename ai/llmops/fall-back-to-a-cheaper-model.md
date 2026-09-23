---
name: fall-back-to-a-cheaper-model
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You route appropriate requests to a cheaper model when budgets, latency, or provider availability require it, while verifying that quality remains acceptable for those routes.

## Preconditions

- At least two model routes: a primary high-capability model and a cheaper fallback.
- A task taxonomy or route metadata that separates low-risk from high-risk requests.
- Eval sets for each route with quality, schema, safety, and latency thresholds.
- Cost and failure metrics by model route.

## Steps

1. **Classify routes by fallback safety.** Mark which tasks can tolerate a cheaper model, which require the primary model, and which need human review. → *Expect:* a routing policy with allowed fallback classes.
2. **Evaluate fallback quality offline.** Run the cheaper model on representative evals for each allowed route. → *Expect:* a table showing quality, JSON validity, refusal rate, latency, and cost delta versus primary.
3. **Define fallback triggers.** Use conditions such as primary 5xx, provider 429, latency SLO breach, tenant budget exhaustion, or explicit low-cost mode. → *Expect:* each trigger has a maximum duration and owner.
4. **Implement model routing.** Use a router function that selects primary or fallback from request metadata and trigger state, then records the decision. → *Expect:* every response includes internal route metadata for observability.
5. **Adjust prompts for the fallback.** Simplify instructions, reduce context, or add stricter output schemas if the cheaper model is weaker. → *Expect:* fallback output validates on the route eval set.
6. **Add user-visible degradation only when needed.** For lower-confidence answers, return a brief limitation message or ask for clarification instead of pretending equivalent capability. → *Expect:* risky fallback responses are withheld or clearly bounded.
7. **Test failover and recovery.** Simulate primary errors and budget exhaustion, then clear the trigger. → *Expect:* traffic moves to fallback during the incident and returns to primary automatically or by approval.
8. **Monitor quality after enablement.** Track fallback volume, error rate, schema validity, escalations, user feedback, and savings. → *Expect:* dashboards show both savings and degradation risk.

## Decision points

- Fallback eval fails quality gates → do not enable fallback for that route.
- Primary outage affects critical high-risk tasks → fail closed or queue rather than using an unsafe model.
- Budget exhausted for low-risk tasks → use fallback or reject with a controlled message.
- Fallback hallucination rate increases → tighten context, add retrieval citations, or disable fallback.

## Failure modes & recovery

- **F1 Silent quality regression:** detect lower task success or user feedback on fallback route → disable fallback for that route and add examples to evals.
- **F2 Schema breakage:** detect JSON validation failures → use structured-output mode or repair step, then re-evaluate.
- **F3 Router loop:** detect repeated fallback retries after failures → cap attempts and return a controlled error.
- **F4 Unsafe fallback for high-risk task:** detect policy-forbidden route using fallback → fix route labels and add a policy unit test.
- **F5 Cost savings not realized:** detect fallback still using large context or high output tokens → trim prompts and lower max tokens.

## Verification

Run route-policy tests plus a simulated primary outage. The check passes only when allowed low-risk routes switch to the cheaper model, forbidden routes do not, fallback responses validate against schemas, eval scores meet route thresholds, and measured cost per successful task drops by the expected percentage.

## Variations

- `cost-triggered`: route to cheaper models when tenant or feature budgets approach caps.
- `incident-triggered`: route during provider 429/5xx or latency incidents.
- `cascade`: try a cheap model first and escalate to the primary only when confidence or validation fails.

## Safety & privacy

Medium risk because weaker models may hallucinate or mishandle safety instructions. Restrict fallback to evaluated routes, log routing decisions, avoid fallback for regulated or irreversible actions, and keep user data protections identical across models.
