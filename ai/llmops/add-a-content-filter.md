---
name: add-a-content-filter
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

You add input and output content filtering around an LLM feature and verify that disallowed content is blocked, safe content passes, and decisions are logged for review.

## Preconditions

- A written content policy with categories, severities, and allowed handling.
- A classifier or moderation API, plus a fallback for classifier failure.
- Labeled examples for allowed, borderline, and disallowed inputs and outputs.
- An application path where blocks, refusals, or escalations can be returned safely.

## Steps

1. **Translate policy into machine categories.** Map your policy to classifier labels such as self-harm, sexual content, violence, hate, illicit activity, privacy, or malware. → *Expect:* a policy-to-label matrix with thresholds and actions.
2. **Filter inputs before the LLM call.** Classify user input and retrieved/tool context before generation. ⚠️ *Data leaves your control:* if using an external moderation API, confirm what text is sent and redact unnecessary PII first. → *Expect:* disallowed inputs are blocked before model spend.
3. **Filter outputs before display or action.** Classify generated text and tool arguments before returning them or executing side effects. → *Expect:* disallowed outputs are withheld or replaced with a safe response.
4. **Add severity-based actions.** Allow, warn, refuse, route to human review, or disable tools depending on category and confidence. → *Expect:* each classifier result maps to one deterministic action.
5. **Handle classifier failures fail-safe.** If moderation times out or errors, use the route's risk policy: retry, degrade, or block. → *Expect:* high-risk routes do not bypass filtering on classifier failure.
6. **Log decisions without sensitive raw content.** Store request ID, category, confidence, action, model version, and hashed content fingerprint. → *Expect:* reviewers can audit trends without reading private prompts by default.
7. **Build a labeled evaluation set.** Include adversarial phrasing, multilingual examples, benign false-positive cases, and policy edge cases. → *Expect:* a test file with expected action for each example.
8. **Tune thresholds and monitor drift.** Adjust thresholds based on false positives and false negatives, then monitor block rates by route and language. → *Expect:* filtering metrics remain stable after release.

## Decision points

- False negatives are unacceptable for a route → lower thresholds and add human review.
- False positives block core usage → add context-specific allow rules and review samples.
- Output can trigger real-world actions → require output filtering plus tool-argument validation.
- Moderation provider receives sensitive data → self-host the classifier or redact first.

## Failure modes & recovery

- **F1 Prompt-injection bypass:** detect disallowed output despite safe input → filter model output and tool arguments, not just user input.
- **F2 Overblocking:** detect high false-positive rate on benign evals → tune thresholds and add allowlisted contexts.
- **F3 Classifier outage:** detect moderation errors → fail closed for high-risk routes and alert owners.
- **F4 Multilingual miss:** detect lower recall on non-English examples → add multilingual classifier coverage and evals.
- **F5 Raw content exposure:** detect sensitive text in moderation logs → redact logs and restrict reviewer access.

## Verification

Run the labeled moderation eval set through input and output filters. The filter passes only when disallowed examples are blocked at or above the required recall threshold, allowed examples pass at or above the precision threshold, classifier failures produce the configured fail-safe action, and decision logs contain no raw sensitive content.

## Variations

- `provider-moderation`: fast to integrate and maintained externally; review data-sharing terms.
- `self-hosted-classifier`: better data control, but requires your own evaluation and updates.
- `hybrid`: use lightweight local filters first and provider moderation for ambiguous cases.

## Safety & privacy

Medium risk because filtering mistakes can expose harmful output or block legitimate users. Apply filters before model calls and before display/actions, redact sensitive data sent to classifiers, log only minimal audit metadata, and require review for threshold changes on high-risk routes.
