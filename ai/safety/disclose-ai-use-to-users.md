---
name: disclose-ai-use-to-users
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

Disclose AI involvement to users at the right points in the product and verify that disclosure appears in every required flow.

## Preconditions

- A product map showing where AI generates, ranks, summarizes, decides, or recommends.
- Legal, policy, or platform requirements for disclosure in your target markets.
- End-to-end tests or UI tests that can assert visible text and metadata.

## Steps

1. **Inventory AI touchpoints.** List every feature where AI processes user input or produces user-visible content. → *Expect:* a table of feature, model/provider, user impact, and disclosure need.
2. **Choose disclosure language.** Write concise labels or notices that say what AI does and where users can learn more. → *Expect:* approved copy exists for inline labels, dialogs, and help pages.
3. **Add disclosures to the UI/API.** Show labels near generated content, AI chat, recommendations, or consequential decisions. → *Expect:* users see the disclosure before or at the moment AI output is used.
4. **Expose provenance in exports.** Include metadata or labels in downloaded, shared, or copied AI-generated content when required. → *Expect:* exported artifacts retain the disclosure signal.
5. **Test every flow.** Use Playwright, Cypress, or API tests to assert disclosure presence. → *Expect:* tests fail if a required disclosure is missing.
6. **Monitor changes.** Add a checklist item for new AI features and model changes. → *Expect:* new AI touchpoints cannot launch without disclosure review.

## Decision points

- AI output affects rights, finances, health, employment, or access → use prominent disclosure and human review where required.
- Disclosure text is too vague → name the AI role, such as "summarized by AI" or "AI-assisted recommendation."
- Users can mistake AI for a human → disclose before the interaction begins.

## Failure modes & recovery

- **F1 Missing flow:** detect an AI feature without a disclosure test → add the test and block release.
- **F2 Export stripping:** detect downloaded content missing AI label → update export templates and metadata.
- **F3 Ambiguous copy:** detect users do not understand AI involvement → revise copy and add contextual details.
- **F4 Policy drift:** detect new jurisdictional requirement → update disclosure matrix and rerun tests.

## Verification

Automated UI/API tests assert the approved disclosure appears in every required AI touchpoint and export path, the AI inventory has an owner for each feature, and release checks fail when a new AI route lacks disclosure metadata.

## Variations

- `chatbot`: disclose before conversation and in conversation metadata.
- `AI summaries`: label each summary and preserve source links.
- `recommendation/ranking`: disclose AI assistance and provide meaningful control where required.

## Safety & privacy

Disclosure helps users calibrate trust but does not replace accuracy, privacy, or safety controls. Avoid dark patterns, be clear when humans may review data, and update disclosures when model providers or data use changes.
