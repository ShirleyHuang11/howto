---
name: summarize-a-document-with-ai
domain: digital
locale: [generic]
interface: web
difficulty: basic
est_time: 15min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Generate a useful document summary with AI while protecting sensitive content and checking that the summary reflects the source.

## Preconditions

- You have permission to process the document with the selected tool.
- You can inspect the original document after the summary is generated.

## Steps

1. **Classify the document.** Decide whether it contains confidential, regulated, personal, privileged, or copyrighted material. → *Expect:* you know whether the chosen AI tool is appropriate.
2. **Prepare the input.** Remove unnecessary pages, redact sensitive identifiers, and keep section headings or page numbers if possible. → *Expect:* the uploaded text contains only what the task needs.
3. **Set summary requirements.** Ask for audience, length, format, key points, decisions, open questions, and page or section references. → *Expect:* the model has a concrete target.
4. **Generate the summary.** Upload or paste the document and request that uncertain or missing points be labeled clearly. [BRANCH: full document | excerpt] use excerpts for sensitive or very long material. → *Expect:* you receive a structured summary.
5. **Cross-check claims.** Compare names, numbers, deadlines, obligations, and conclusions against the original. → *Expect:* important facts are confirmed or corrected.
6. **Store or delete output.** Save the checked summary in the right location and delete uploads or chats if policy requires it. → *Expect:* document handling follows your retention needs.

## Decision points

- The document is legal, medical, financial, HR, or confidential → use an approved private tool or summarize manually.
- The model cannot cite locations in the source → ask for page or section references and verify them.
- The document is copyrighted and you do not own it → use brief summaries for your own review and avoid redistributing extracted text.

## Failure modes & recovery

- **F1 Missing key point:** detect an important section absent from the summary → recover by asking for a section-by-section summary.
- **F2 Invented detail:** detect facts not present in the document → recover by removing them and prompting for source-backed bullets only.
- **F3 Privacy overexposure:** detect unnecessary sensitive content was uploaded → recover by deleting retained copies if possible and using redacted excerpts next time.

## Verification

The final summary includes the required format, covers each important section, and every critical name, number, deadline, or obligation matches the original document.

## Variations

- `web`: use document upload only after checking retention and training settings.
- `mobile-app`: scan quality affects summaries, so review OCR text before trusting the result.
- `research`: require citations to page, table, or section numbers.

## Safety & privacy

Medium risk because summaries can omit obligations or invent meaning. Do not upload contracts, medical records, client files, or personnel documents to tools that are not approved for that data.
