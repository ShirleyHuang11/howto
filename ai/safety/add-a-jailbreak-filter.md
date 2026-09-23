---
name: add-a-jailbreak-filter
domain: ai
subdomain: safety
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

Add a runtime filter that detects likely jailbreak attempts before model execution and measures both attack blocking and benign prompt acceptance.

## Preconditions

- A written safety policy and examples of allowed and disallowed user requests.
- A labeled dataset of jailbreak prompts, benign prompts, and borderline prompts.
- A classifier, ruleset, moderation endpoint, or LLM-based detector with a stable JSON output.

## Steps

1. **Define the filter contract.** Return `allow`, `block`, or `review` with category, confidence, and reason. → *Expect:* downstream code can parse and act on one structured decision.
2. **Assemble the test set.** Include known jailbreak patterns, roleplay attacks, encoding tricks, multi-turn attacks, and benign security/AI-safety questions. → *Expect:* a labeled CSV/JSONL file with no duplicate ids.
3. **Implement detection.** [BRANCH: rules plus classifier | hosted moderation | LLM detector] Run detection before the main model receives the prompt. ⚠️ *Data leaves your control:* hosted detectors receive user prompts and may see sensitive text. → *Expect:* each input gets a decision within the latency budget.
4. **Gate the main call.** Block or ask for clarification when the decision is `block` or high-risk `review`; pass benign prompts through unchanged. → *Expect:* blocked prompts do not reach the main model.
5. **Evaluate the filter.** Compute attack recall, benign false-positive rate, latency, and cost. → *Expect:* recall and false-positive metrics meet launch thresholds.
6. **Log safely for tuning.** Store prompt hashes, category, decision, and sampled redacted text where allowed. → *Expect:* metrics can be audited without retaining unnecessary sensitive prompts.

## Decision points

- Attack recall is low → add examples, combine rules with a classifier, or route uncertain prompts to review.
- Benign false positives are high → tune thresholds and add legitimate cybersecurity/research examples.
- Latency is unacceptable → cache deterministic rule decisions and use the classifier only for uncertain cases.

## Failure modes & recovery

- **F1 Encoding bypass:** detect attacks hidden in base64, homoglyphs, or spacing → normalize text before classification.
- **F2 Overblocking education:** detect benign security lessons blocked → add allowlisted educational intents and examples.
- **F3 Multi-turn bypass:** detect harmless single turns that combine into an attack → classify conversation state, not only latest message.
- **F4 Detector outage:** detect timeout or 5xx → fail closed for high-risk surfaces and expose a graceful retry.

## Verification

On the labeled filter set, attack recall is at least 0.95, benign false-positive rate is at most 0.03, p95 detector latency is below the configured budget, and integration tests prove blocked prompts never call the main model.

## Variations

- `rule-first filter`: transparent and fast; misses novel attacks.
- `classifier detector`: better coverage; requires labeled data and drift monitoring.
- `LLM detector`: flexible for new patterns; control cost, latency, and judge consistency.

## Safety & privacy

Filters are defense-in-depth, not a replacement for safe tool design and output moderation. Minimize prompt retention, redact logs, avoid blocking legitimate safety research by default, and document what user text is sent to any detector vendor.
