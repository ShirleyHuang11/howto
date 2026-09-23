---
name: summarize-a-video-transcript
domain: ai
subdomain: multimodal
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

Summarize a video transcript into accurate, timestamped notes with citations to source segments and automated checks for coverage and hallucination.

## Preconditions

- A transcript with timestamps, speaker labels if available, and permission to process the content.
- A summarization model and a schema validator.
- A small evaluation set with known key points or human-reviewed summaries.

## Steps

1. **Normalize the transcript.** Convert captions to a consistent format with segment ids, start/end times, speaker, and text. → *Expect:* every transcript segment has a stable id and valid timestamp range.
2. **Chunk by meaning and time.** Group segments into chunks that fit the model context while preserving timestamp provenance. → *Expect:* each chunk has token count below the configured limit and lists source segment ids.
3. **Generate structured summaries.** [BRANCH: hosted LLM | local LLM] Ask for JSON containing `summary`, `key_points`, `action_items`, and `citations`. ⚠️ *Data leaves your control:* transcripts may contain private meetings or customer data when sent to hosted models. → *Expect:* parseable JSON with citations for each claim.
4. **Verify citations.** Check that every cited timestamp exists and that cited text overlaps the claim using lexical or embedding similarity. → *Expect:* unsupported claims are flagged or removed.
5. **Merge chunk summaries.** Deduplicate repeated points and preserve the earliest supporting timestamp. → *Expect:* final summary references source timestamps and avoids repeated bullets.
6. **Evaluate quality.** Compare against held-out key points and compute coverage plus unsupported-claim rate. → *Expect:* coverage meets threshold and unsupported claims stay below the allowed maximum.

## Decision points

- Unsupported-claim rate is high → force extractive citations or lower abstraction.
- Transcript is noisy ASR → run cleanup or confidence filtering before summarization.
- Transcript contains confidential meeting content → use local models or approved enterprise endpoints.

## Failure modes & recovery

- **F1 Timestamp hallucination:** detect citation ids or times not in transcript → reject output and retry with allowed citation ids.
- **F2 Lost key point:** detect low coverage against gold notes → adjust chunking and add map-reduce checks.
- **F3 Speaker confusion:** detect action item assigned to wrong person → preserve speaker labels and require cited evidence.
- **F4 Context overflow:** detect model context-length error → reduce chunk size and summarize hierarchically.

## Verification

The final JSON validates against the schema, every citation id maps to a real transcript segment, chunk token counts are below the model limit, key-point coverage is at least 0.85 on the evaluation set, and unsupported-claim rate is at most 0.05.

## Variations

- `meeting transcript`: emphasize decisions, owners, and action items.
- `lecture transcript`: emphasize concepts, definitions, and timestamped study notes.
- `local LLM`: improves privacy but may require stronger citation validation.

## Safety & privacy

Transcripts can contain confidential business plans, names, voices, and personal data. Redact where possible, avoid storing raw transcripts in logs, disclose AI summaries to participants when needed, and require citations before treating a summary as factual.
