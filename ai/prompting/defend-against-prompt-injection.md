---
name: defend-against-prompt-injection
domain: ai
subdomain: prompting
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You make a prompt-driven workflow resilient to malicious or conflicting instructions embedded in user input, retrieved documents, or tool results.

## Preconditions

- An LLM workflow that consumes untrusted text.
- A clear authority hierarchy for system, developer, user, retrieved, and tool content.
- Injection test cases that attempt data exfiltration, policy override, and tool misuse.

## Steps

1. **Map trusted and untrusted channels.** Label every input source by authority and trust level. → *Expect:* a data-flow diagram or table with `trusted_instruction`, `user_request`, `retrieved_data`, and `tool_result`.
2. **State the authority hierarchy.** Tell the model that untrusted content is data, not instructions, and cannot override higher-priority messages. → *Expect:* the system prompt contains an explicit hierarchy rule.
3. **Delimit untrusted content.** Wrap retrieved documents and tool results in clear tags with metadata. → *Expect:* every untrusted block has a source id and boundary markers.
4. **Constrain tools by policy code.** Validate tool calls in code against allowlists, schemas, and user permissions before execution. → *Expect:* malicious requested tool calls are rejected before hitting the tool.
5. **Run an injection eval.** Include attacks such as `ignore previous instructions`, fake system messages, and secret-exfiltration requests. → *Expect:* a pass/fail table for each attack category.
6. **Add refusal and safe-completion paths.** Make the model answer the legitimate part while ignoring malicious instructions when possible. → *Expect:* benign content in poisoned documents can still be used safely.

## Decision points

- Workflow can take external actions → enforce policy in code, not only in the prompt.
- Retrieved content includes instructions to the assistant → quote or summarize as document content, never obey it.
- Attack pass rate is below threshold → do not deploy tool access or private-data access.

## Failure modes & recovery

- **F1 Instruction override:** detect model follows retrieved text saying to ignore rules → strengthen hierarchy and add similar test cases.
- **F2 Tool misuse:** detect unauthorized tool call generated → add server-side allowlist and permission checks.
- **F3 Data exfiltration:** detect secrets or hidden prompt content in output → remove secrets from context and add output filters.
- **F4 Overblocking:** detect normal documents rejected as attacks → separate malicious instruction following from harmless quoted text.

## Verification

Run `python eval_prompt_injection.py --cases injection_cases.jsonl --min-attack-block-rate 0.98 --min-benign-pass-rate 0.90`; at least 98% of attacks are blocked, no unauthorized tool call is executed, and at least 90% of benign cases still complete.

## Variations

- `RAG`: treat retrieved chunks as untrusted evidence and validate citations.
- `agents`: gate every tool call with code-level policy and user authorization.
- `browser automation`: never let page text directly choose credentials, destinations, or destructive actions.

## Safety & privacy

Medium risk because injection can leak private data or trigger unsafe actions. Keep secrets out of model context, enforce permissions outside the model, and require review before enabling tools that send messages, spend money, or modify records.
