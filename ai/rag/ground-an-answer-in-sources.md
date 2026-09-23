---
name: ground-an-answer-in-sources
domain: ai
subdomain: rag
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

You generate answers that cite retrieved sources and refuse or qualify claims not supported by those sources.

## Preconditions

- Retrieved context with stable source ids, titles, URLs or paths, and text spans.
- An answer model that can follow citation and abstention instructions.
- A test set with questions, expected answer facts, and gold source ids.
- A citation validator that can map citations back to retrieved chunks.

## Steps

1. **Format sources as bounded evidence.** Wrap each chunk with an immutable id like `[S3]`, title, date, and text. → *Expect:* every evidence block has a unique id that appears in the prompt exactly once.
2. **Write a grounded-answer instruction.** Require the model to answer only from sources, cite every factual sentence, and say it is not in the sources when evidence is missing. [BRANCH: Anthropic | OpenAI | open model] → *Expect:* outputs include citations such as `[S3]` after supported claims.
3. **Pass only retrieved evidence.** Do not include hidden background facts or unverified summaries in the answer context. ⚠️ *Data leaves your control:* external answer calls receive source text; redact sensitive content first. → *Expect:* the model sees only approved prompt, user question, and evidence blocks.
4. **Parse and validate citations.** Check that every citation id exists in the retrieved set and that every paragraph with factual claims has at least one citation. → *Expect:* invalid citation ids fail the response.
5. **Check claim support.** Use an entailment model, LLM judge with source-only rubric, or exact answer keys to flag unsupported claims. → *Expect:* unsupported claims are either removed or the answer is regenerated.
6. **Add abstention behavior.** Test out-of-scope questions and require a short refusal with no invented citations. → *Expect:* missing-evidence questions return an abstention, not a guessed answer.
7. **Evaluate before release.** Score citation precision, citation recall, answer correctness, and abstention accuracy. → *Expect:* metrics meet the release threshold on held-out questions.

## Decision points

- Citation precision is low → require sentence-level citations and stricter validation.
- Answer correctness is high but citations are weak → block release; grounded systems need both.
- Users need synthesis across sources → allow multi-source citations but keep each claim traceable.
- Source documents conflict → answer with the disagreement and cite both sources.

## Failure modes & recovery

- **F1 Fabricated citation:** detect citation id not present in retrieved context → reject and regenerate with valid ids only.
- **F2 Unsupported claim:** detect claim not entailed by cited text → remove claim or return insufficient evidence.
- **F3 Over-citation masking weak support:** detect citations attached to irrelevant sources → score citation precision with a judge or gold labels.
- **F4 Prompt injection in source:** detect source text instructing the model to ignore rules → isolate source text as data and keep system instructions separate.

## Verification

Programmatic validation must show every citation id resolves to a retrieved source, every factual sentence has at least one citation, citation precision is at least 0.9 on the held-out set, and unsupported-answer rate is below the configured threshold.

## Variations

- `strict-compliance`: require exact quoted spans for every answer sentence.
- `research-assistant`: allow synthesis but require multiple citations for cross-document conclusions.
- `local-llm`: run answer generation locally when source text cannot leave your environment.

## Safety & privacy

Grounding reduces hallucination but does not make retrieved content trustworthy. Treat sources as untrusted data, redact sensitive material before external calls, avoid exposing confidential source ids in public answers, and require human review for regulated or high-impact advice.
