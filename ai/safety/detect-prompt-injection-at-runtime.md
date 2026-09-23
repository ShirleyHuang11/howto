---
name: detect-prompt-injection-at-runtime
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

Detect prompt-injection attempts in retrieved or user-supplied content at runtime and prevent them from changing instructions, leaking data, or triggering unsafe tools.

## Preconditions

- An LLM app that uses retrieved documents, web pages, emails, files, or user messages as context.
- A labeled prompt-injection evaluation set with benign and malicious content.
- A policy for what content may influence instructions versus what is treated as data.

## Steps

1. **Separate instruction and data channels.** Wrap retrieved content as untrusted data and keep system/developer instructions outside it. → *Expect:* prompt templates visibly label untrusted content boundaries.
2. **Scan untrusted text.** [BRANCH: regex/rules | classifier | LLM detector] Detect phrases that request ignoring instructions, revealing secrets, calling tools, or changing output policy. → *Expect:* each context chunk gets an injection score and reason.
3. **Apply runtime handling.** Remove, quote, summarize, or down-rank suspicious chunks before model generation. → *Expect:* malicious chunks cannot directly become instructions.
4. **Constrain tool calls.** Require typed tool arguments, allowlists, and server-side authorization independent of model text. → *Expect:* a prompt injection cannot call a tool outside the user's permissions.
5. **Evaluate with attacks.** Run cases where hostile retrieved documents ask the model to leak secrets or alter answers. → *Expect:* the model follows system policy and cites only relevant safe content.
6. **Log detection outcomes.** Store document id, detector version, score, action, and final tool-call decision. → *Expect:* injection events are auditable without exposing unnecessary raw content.

## Decision points

- Detector catches malicious but useful documents → quote or summarize them instead of deleting the whole document.
- Tool-call risk is high → require user confirmation or deterministic authorization before execution.
- Retrieval source is user-editable or web-scale → treat all retrieved text as hostile by default.

## Failure modes & recovery

- **F1 Hidden instruction in retrieved text:** detect leaked secret or changed policy in eval → strengthen untrusted-content boundaries and filtering.
- **F2 Tool authorization bypass:** detect model-issued call with unauthorized target → enforce server-side ACLs and reject the call.
- **F3 Excessive false positives:** detect many benign docs removed → tune thresholds and use chunk-level handling.
- **F4 Obfuscated injection:** detect attacks using HTML comments, markdown links, or Unicode tricks → normalize and strip active markup before scanning.

## Verification

In the prompt-injection eval suite, zero critical cases leak protected data or execute unauthorized tools, detector recall is at least 0.95 on labeled injection chunks, and benign retrieval answer quality stays above the configured baseline.

## Variations

- `RAG application`: scan retrieved chunks and preserve citation provenance.
- `email or browser agent`: treat message bodies and pages as hostile data; tool authorization is mandatory.
- `code assistant`: sandbox commands and never let repository text override system instructions.

## Safety & privacy

Prompt injection is a security issue. Do not rely on model obedience alone; enforce access control, redact secrets from context, log suspicious sources, and require confirmation for risky actions even when the detector is quiet.
