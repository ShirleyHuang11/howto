---
name: add-citations-to-rag-answers
domain: ai
subdomain: rag
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [ai/rag/build-a-basic-rag-pipeline]
status: draft
last_verified: 2026-09-22
---

## Goal

Make RAG answers cite retrieved sources in a machine-checkable format, and reject answers with fabricated or unsupported citations.

## Preconditions

- A RAG pipeline that retrieves chunks with stable source IDs.
- Source metadata such as title, URL, page, section, or timestamp.
- A citation validator that can compare cited IDs against retrieved context.

## Steps

1. **Assign stable citation IDs.** Give each retrieved chunk a short ID such as `S1`, mapped to `chunk_id`, page, and URI for this answer. → *Expect:* the prompt context and validator share the same citation map.
2. **Prompt for cited claims.** Instruct the model to cite source IDs for factual claims and return `insufficient_context` when no source supports an answer. → *Expect:* generated answers include citation markers or structured citation fields.
3. **Use structured output when possible.** Ask for JSON with `answer`, `claims`, and `citations` rather than free-form footnotes. → *Expect:* citations are parseable.
4. **Validate cited IDs.** Reject citations not present in the retrieval set and claims with empty citations. → *Expect:* fabricated source IDs never reach the user.
5. **Check claim support.** Use sentence-to-source overlap, an entailment model, or an LLM judge to flag claims not supported by cited chunks. ⚠️ *Data leaves your control:* hosted judges receive claims and source text. → *Expect:* unsupported claims are marked or rejected.
6. **Render user-facing citations.** Convert source IDs into links, page numbers, or document references after validation. → *Expect:* users can open the cited source.
7. **Evaluate citation quality.** Measure citation validity, citation recall, and unsupported-claim rate on a labeled set. → *Expect:* citation metrics are tracked alongside answer quality.

## Decision points

- Citation ID is not in retrieved context → reject and retry once.
- Claim has no supporting source → remove the claim or return insufficient context.
- Source has page or line numbers → include them in rendered citations.
- Citation validator is uncertain → route high-impact answers to human review.

## Failure modes & recovery

- **F1 Fabricated citation:** detect unknown source ID → validate and regenerate.
- **F2 Over-citation:** detect every sentence citing all sources → ask for minimal supporting citations and score precision.
- **F3 Unsupported synthesis:** detect conclusion not entailed by sources → require cited intermediate facts or abstain.
- **F4 Broken source link:** detect URI or page missing → fall back to document title and fix metadata ingestion.

## Verification

Run citation validation on an eval set. Success means `100%` of cited IDs exist in the retrieved context, at least `95%` of factual claims have citations, unsupported-claim rate is below threshold, and rendered citations resolve to the expected source metadata.

## Variations

- `legal or policy`: require pinpoint citations such as section, page, or clause.
- `internal docs`: cite document title and last-updated timestamp.
- `UI answer cards`: keep source map hidden but expose clickable source chips.

## Safety & privacy

Citations can create false confidence if unsupported. Validate them mechanically, avoid exposing sources the user is not authorized to see, and do not send sensitive source text to external citation judges without approval.
