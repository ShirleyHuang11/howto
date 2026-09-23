---
name: redact-pii-before-an-llm-call
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You remove or replace personally identifiable information before text is sent to an LLM API, and you can prove with automated checks that the outbound payload contains no configured PII classes.

## Preconditions

- A representative sample of prompts, retrieved context, tool outputs, and user attachments.
- A PII detector such as Microsoft Presidio, a cloud DLP service, or validated regexes for narrow identifiers.
- A redaction policy that names which entity types must be masked, hashed, dropped, or preserved.
- You can call the model after redaction; see `ai/call-an-llm-api` if needed.

## Steps

1. **Define the outbound data boundary.** List every field that can leave your infrastructure: user message, system-added context, retrieved chunks, logs, metadata, and tool results. → *Expect:* a typed payload schema with each outbound text field marked for scanning.
2. **Choose entity classes and actions.** Map `EMAIL_ADDRESS`, `PHONE_NUMBER`, `PERSON`, `LOCATION`, account IDs, secrets, and domain-specific identifiers to `replace`, `hash`, `drop`, or `allow`. → *Expect:* a policy file such as `pii_policy.yaml` with deterministic actions for each class.
3. **Implement deterministic redaction before the API client.** Wrap the LLM client so all requests pass through the sanitizer before serialization. [BRANCH: Presidio | cloud DLP | custom detector] For example, call `AnalyzerEngine().analyze(text=payload, language="en")` and replace spans with stable placeholders like `<EMAIL_1>`. → *Expect:* a sanitized request object is produced before any network call is possible.
4. **Preserve reversible mappings only when required.** Store placeholder-to-original mappings in a short-lived encrypted store keyed by request ID, or skip reversibility entirely for generation-only tasks. → *Expect:* placeholders are stable within one request and originals are not written to ordinary logs.
5. **Block low-confidence gaps with deny regexes.** Add exact patterns for known internal IDs, API keys, SSNs, credit cards, MRNs, or ticket formats that generic NER may miss. → *Expect:* a test string containing each pattern is masked even when the NER detector is disabled.
6. **Add an egress assertion.** Immediately before the LLM call, run `assert_no_pii(sanitized_payload)` and fail closed if prohibited entities remain. ⚠️ *Data leaves your control:* confirm masking succeeds before sending any production or user data to a third-party API. → *Expect:* requests with unredacted PII raise a controlled exception and are not sent.
7. **Sanitize observability.** Log only request IDs, model names, token counts, redaction counts, hashes, and policy version; never raw pre-redaction text. → *Expect:* log samples contain redaction metadata but no original PII values.
8. **Build a regression corpus.** Create examples with realistic emails, names, phone numbers, addresses, secrets, and domain identifiers, plus false-positive examples that should remain. → *Expect:* a test fixture with expected sanitized output for every example.

## Decision points

- Text must be re-identified after generation → use encrypted, short-lived placeholder maps and restrict access.
- PII detection recall is below target → add domain-specific regexes and human review before using production data.
- Redaction destroys task quality → replace with typed placeholders instead of deleting, then evaluate quality separately.
- Payload contains regulated data you cannot send externally → use a self-hosted model or do not process that request.

## Failure modes & recovery

- **F1 Missed identifier:** detect via regression tests or DLP egress scan finding an unmasked entity → add a detector rule and replay the blocked request after sanitization.
- **F2 Over-redaction:** detect task accuracy dropping or non-PII terms masked → add allowlists, context rules, or narrower entity types.
- **F3 Placeholder leakage:** detect generated output exposing placeholders that cannot be mapped safely → postprocess allowed placeholders only and suppress unknown placeholders.
- **F4 Raw data in logs:** detect PII in log search or SIEM alert → rotate logs according to policy, disable raw prompt logging, and add log scrubbing tests.
- **F5 Detector latency spike:** detect sanitizer p95 exceeding the request budget → batch detector calls, cache repeated safe system context, or move scanning to an async preprocessing step.

## Verification

Run a test suite that serializes every outbound LLM request fixture, applies the redactor, and then runs an independent detector plus deny regexes over the sanitized JSON. The check passes only when prohibited entity count is `0`, required placeholders match the expected snapshot, and no raw fixture PII appears in application logs.

## Variations

- `Presidio`: local, customizable recognizers; best when you need code-level control.
- `cloud-dlp`: managed detectors and policy reporting; expect network latency and data transfer to the DLP provider.
- `local-model`: still redact before inference if prompts are logged, shared, or used for training.

## Safety & privacy

High risk because unredacted user or proprietary data sent to an external API cannot be recalled. Minimize collection, redact before network transmission, keep reversible maps encrypted and short-lived, disable raw prompt logging, and require privacy review before expanding allowed entity classes.
