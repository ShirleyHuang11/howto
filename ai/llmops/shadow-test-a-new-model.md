---
name: shadow-test-a-new-model
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 2h
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You send copied production-like traffic to a candidate model without showing its responses to users, then compare quality, latency, cost, and safety before rollout.

## Preconditions

- A baseline production model and a candidate model endpoint.
- A traffic mirroring mechanism or async job that can replay requests.
- Redaction or synthetic-data controls for any production prompts.
- Eval comparators for schema validity, tool calls, citations, refusal behavior, latency, and cost.

## Steps

1. **Define what can be mirrored.** Exclude regulated, opted-out, or high-risk data unless it is redacted or synthesized first. → *Expect:* a routing policy that names eligible traffic classes.
2. **Add request cloning after validation.** Copy validated inputs, prompt version, tool schema, and metadata to a shadow queue while the baseline serves the user. → *Expect:* user latency is not increased by the candidate call.
3. **Redact or transform shadow payloads.** Remove PII and secrets before sending copied traffic to a third-party candidate. ⚠️ *Data leaves your control:* confirm redaction passes before any mirrored production text is transmitted externally. → *Expect:* shadow queue payloads contain no prohibited entities.
4. **Call the candidate asynchronously.** Send shadow requests with the same deterministic parameters where possible, but discard responses from the user path. → *Expect:* candidate responses are stored only for evaluation and never returned to users.
5. **Score output differences.** Compare schema validity, task correctness, refusal rate, citation support, tool-call arguments, latency, and cost against baseline. → *Expect:* a per-route candidate-vs-baseline report.
6. **Limit volume and spend.** Sample traffic by route and tenant, with daily token and dollar caps. → *Expect:* shadow traffic cannot exceed the configured budget.
7. **Review regressions.** Inspect cases where candidate fails gates or differs materially from baseline. → *Expect:* labeled regression examples are added to the offline eval set.
8. **Decide on canary readiness.** Promote only if shadow metrics meet release thresholds. → *Expect:* a go/no-go record with metrics and unresolved risks.

## Decision points

- Shadow payload includes data that cannot leave your infra → use an internally hosted candidate or skip that traffic.
- Candidate schema validity is lower than baseline → do not canary until prompts or output constraints are fixed.
- Candidate is better but much slower → reserve it for async or premium routes.
- Shadow spend approaches cap → reduce sampling or stop the job.

## Failure modes & recovery

- **F1 User-path latency increase:** detect higher baseline p95 after enabling mirroring → move cloning to an async queue and drop shadow work under pressure.
- **F2 Candidate response leaks:** detect candidate route returned to user → enforce separate code paths and add tests that shadow outputs are ignored.
- **F3 PII in shadow store:** detect DLP findings in stored payloads → purge according to policy, fix redaction, and pause mirroring.
- **F4 Biased sample:** detect only easy routes mirrored → stratify sampling by route, tenant, language, and input length.
- **F5 Spend overrun:** detect shadow token usage exceeding cap → disable candidate queue and require approval to resume.

## Verification

Run a shadow test on a bounded sample and assert that baseline responses served to users are unchanged, candidate outputs are not exposed, redacted shadow payloads pass the PII detector, and the candidate report includes quality, schema-validity, p95 latency, and cost metrics for every mirrored route.

## Variations

- `live-mirror`: best for real distribution, requires strong privacy and budget controls.
- `trace-replay`: safer and repeatable, but may miss live system effects.
- `open-model`: can shadow internally without third-party data transfer, but still protect logs.

## Safety & privacy

High risk because copied production traffic may expose sensitive data and double spend. Redact before transmission, sample conservatively, segregate shadow outputs, set hard caps, and require review before using regulated or customer-confidential data.
