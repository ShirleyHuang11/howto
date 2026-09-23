---
name: handle-a-harmful-request-safely
domain: ai
subdomain: safety
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Respond to a harmful user request with a refusal or safe alternative that follows policy, avoids actionable harmful detail, and passes automated safety evaluation.

## Preconditions

- A written policy for harmful domains such as violence, self-harm, cyber abuse, fraud, hate, sexual content, and regulated advice.
- A response template or system prompt that supports brief refusals and safe redirection.
- A labeled eval set of harmful, benign, and ambiguous requests.

## Steps

1. **Classify the request.** Determine the harmful category, severity, user intent, and whether a safe educational transformation is possible. → *Expect:* a structured label such as `category`, `severity`, and `allowed_response_type`.
2. **Refuse when required.** For disallowed requests, give a brief refusal without procedural details or hidden policy text. → *Expect:* the response contains no actionable harmful steps.
3. **Offer safe help.** Redirect to benign information, safety planning, high-level education, or emergency resources when appropriate. → *Expect:* the response includes a safe next step matched to the request.
4. **Use crisis handling for imminent self-harm.** Escalate to local emergency guidance or crisis resources according to product policy. → *Expect:* self-harm crisis cases receive supportive, nonjudgmental crisis-safe language.
5. **Moderate the final output.** Run the candidate response through output moderation before sending. → *Expect:* unsafe refusal leakage is blocked or revised.
6. **Evaluate responses.** Check refusal correctness, absence of harmful detail, and helpful safe alternative rate. → *Expect:* the eval suite passes critical harmful cases.

## Decision points

- Request can be reframed safely → answer the safe version and avoid operational detail.
- User signals immediate danger → prioritize crisis-safe support and escalation resources.
- Request is ambiguous → ask a clarifying question or provide only high-level safe information.

## Failure modes & recovery

- **F1 Harmful detail leakage:** detect procedural steps in a refusal → tighten templates and output moderation.
- **F2 Over-refusal:** detect benign educational or safety request refused → add safe-intent examples.
- **F3 Missing crisis response:** detect imminent self-harm treated as ordinary refusal → add severity routing and crisis tests.
- **F4 Policy inconsistency:** detect different answers for paraphrases → add paraphrase regression tests.

## Verification

The harmful-request eval suite has zero critical harmful-detail leaks, refusal correctness is at least 0.95, benign over-refusal is at most 0.05, and every imminent self-harm fixture triggers the approved crisis-safe response path.

## Variations

- `customer support bot`: combine refusal with escalation to human support for account or safety issues.
- `education product`: allow high-level learning while blocking operational harm.
- `agent with tools`: block tool calls as well as text responses for harmful requests.

## Safety & privacy

Harmful requests require calm, consistent handling. Do not shame users, do not reveal hidden policy text, avoid actionable harmful instructions, and minimize sensitive logs while preserving enough data to audit safety failures.
