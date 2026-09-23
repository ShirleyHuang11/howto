---
name: watermark-ai-generated-text
domain: ai
subdomain: safety
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Attach a durable provenance signal to AI-generated text and verify that generated records can be identified later without relying on unreliable human judgment.

## Preconditions

- A requirement for provenance, disclosure, audit, or downstream filtering.
- Control over the generation service or the storage layer where generated text is saved.
- A detector or metadata verification script.

## Steps

1. **Choose the watermark type.** [BRANCH: cryptographic metadata | signed provenance record | statistical text watermark] Prefer signed metadata when you control storage or transport. → *Expect:* a documented scheme with detector requirements and known limitations.
2. **Create a signing key or provenance id.** Store signing keys in a secret manager and rotate them on schedule. → *Expect:* generated text records can include a verifiable signature or provenance pointer.
3. **Attach provenance at generation time.** Save model, prompt version, timestamp, content hash, and signature alongside the text. → *Expect:* every generated record has metadata before it leaves the service.
4. **Verify provenance.** Run a detector or signature check on stored/generated samples. → *Expect:* valid generated samples verify and tampered samples fail.
5. **Test transformations.** Evaluate copy/paste, formatting changes, truncation, paraphrase, and translation. → *Expect:* metadata survives controlled storage paths; statistical text watermarks degrade under heavy editing.
6. **Document disclosure behavior.** Decide when users see a label such as "AI-generated" and how exports include metadata. → *Expect:* UI/export paths expose provenance where required.

## Decision points

- You control storage/export → use signed metadata rather than statistical watermarking.
- Text will be copied into uncontrolled channels → add visible disclosure because metadata may be stripped.
- Need legal or platform compliance → confirm the watermark scheme satisfies the actual requirement.

## Failure modes & recovery

- **F1 Metadata stripped:** detect exported text without provenance → update exporters and add tests for each format.
- **F2 False attribution:** detect unsigned human text marked as AI-generated → verify signatures instead of trusting labels.
- **F3 Key exposure:** detect signing key in logs or code → rotate keys and invalidate affected signatures.
- **F4 Statistical detector unreliability:** detect low true-positive or high false-positive rate → use metadata provenance or lower confidence claims.

## Verification

A provenance test suite confirms 100% of generated records include model/version/hash metadata, signature verification passes for untouched generated text, fails for tampered text, and export tests preserve or visibly disclose provenance according to policy.

## Variations

- `signed metadata`: most reliable when your app controls storage.
- `C2PA-style provenance`: useful for interoperable content credentials where supported.
- `statistical watermark`: may help in controlled text generation but is fragile under editing and paraphrase.

## Safety & privacy

Watermarks are not proof of authorship by themselves and should not be used as the sole enforcement mechanism. Avoid embedding private prompt content in metadata, protect signing keys, and explain uncertainty when detection is probabilistic.
