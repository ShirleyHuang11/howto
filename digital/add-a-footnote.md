---
name: add-a-footnote
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

A footnote marker is inserted in the text and a matching note appears at the bottom of the page.

## Preconditions

- A document is open in a word processor.
- You know the sentence or phrase the footnote should support.

## Steps

1. **Place the cursor.** Click immediately after the word, sentence, or punctuation that needs a footnote. → *Expect:* the insertion cursor appears at the citation point.
2. **Insert the footnote.** [BRANCH: Word | Google Docs] In Word, choose References > Insert Footnote; in Google Docs, choose Insert > Footnote. → *Expect:* a superscript footnote number appears in the text and the cursor moves to the footnote area.
3. **Type the note.** Enter the source, explanation, or citation text. → *Expect:* the footnote text appears at the bottom of the page.
4. **Return to the main text.** Click back after the footnote marker or continue after the cited sentence. → *Expect:* the cursor is back in the document body.
5. **Check numbering.** Add or inspect nearby footnotes if present. → *Expect:* footnote numbers are sequential and automatically updated.

## Decision points

- The required style uses endnotes → choose Insert Endnote instead of Insert Footnote.
- The note is a citation → format it according to the required citation style.

## Failure modes & recovery

- **F1 Footnote inserted in the wrong place:** detect: marker appears beside the wrong text → recover by undoing and placing the cursor correctly.
- **F2 Numbering is manual text:** detect: typed numbers do not update automatically → recover by using the Insert Footnote command.
- **F3 Footnote text is missing:** detect: marker exists but note area is blank → recover by clicking the note area and entering the text.

## Verification

The document shows a superscript marker at the intended location and matching footnote text at the bottom of the page.

## Variations

- `word`: References > Footnotes has settings for numbering and footnote location.
- `google-docs`: Insert > Footnote creates automatic numbering at the bottom of the page.

## Safety & privacy

Footnotes may expose source links, private notes, or reviewer context. Review them before sharing or exporting.
