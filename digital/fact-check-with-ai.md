---
name: fact-check-with-ai
domain: digital
locale: [generic]
interface: web
difficulty: intermediate
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Use AI to organize a fact-check while independently confirming important claims with reliable sources.

## Preconditions

- You have the text, image caption, post, or claim you want to check.
- You can access primary or reputable secondary sources for comparison.

## Steps

1. **Extract checkable claims.** Ask the AI to list specific factual claims, dates, numbers, quotes, and named entities separately from opinions. → *Expect:* you have a numbered claim list.
2. **Rank claim risk.** Mark claims that affect health, safety, law, finances, reputation, or public affairs as high priority. → *Expect:* the riskiest claims are checked first.
3. **Request source leads.** Ask for likely primary sources, official records, papers, or reputable reporting, and require the AI to say when it is uncertain. → *Expect:* you have search targets, not a final verdict.
4. **Verify outside the model.** Open the cited or suggested sources yourself and compare the exact claim against the source text. [BRANCH: primary source found | only commentary found] use primary sources when available; otherwise note the lower confidence. → *Expect:* each important claim has evidence, contradiction, or unknown status.
5. **Check dates and context.** Confirm publication dates, event dates, geographic scope, and whether a quote or statistic is being reused out of context. → *Expect:* stale or misframed claims are identified.
6. **Record a verdict.** Label each claim true, false, misleading, unsupported, or needs expert review, with a short reason. → *Expect:* the fact-check is auditable.

## Decision points

- The claim is medical, legal, or financial advice → use authoritative sources and consult a qualified professional before acting.
- The AI provides a citation that cannot be opened or does not support the claim → treat it as unsupported.
- Sources disagree → prefer primary evidence, methods transparency, and newer corrections over repeated summaries.

## Failure modes & recovery

- **F1 Fake citation:** detect a source title, author, DOI, or URL that does not exist → recover by searching the source independently and marking the AI citation unreliable.
- **F2 Source mismatch:** detect that the source exists but says something different → recover by quoting only the verified point in your notes and revising the verdict.
- **F3 Confirmation bias:** detect that only supportive sources were checked → recover by searching for credible contrary evidence.

## Verification

Every high-priority claim has a recorded verdict and at least one independently opened source or an explicit unsupported status.

## Variations

- `web`: use browser tabs or a spreadsheet to track claims and sources.
- `academic`: prioritize original papers, corrections, datasets, and conflict-of-interest statements.
- `news`: check the timestamp, location, and whether later reporting corrected the initial claim.

## Safety & privacy

Medium risk because wrong fact-checks can harm decisions and reputations. Do not upload private documents, screenshots, or messages unless you have permission and the tool is approved for that content.
