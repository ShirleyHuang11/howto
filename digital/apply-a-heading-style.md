---
name: apply-a-heading-style
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Selected text is formatted with a real heading style so the document structure is recognized by the editor.

## Preconditions

- A document is open.
- The heading text already exists or can be typed.

## Steps

1. **Select the heading text.** Highlight the line that should become a heading. → *Expect:* only the intended heading text is selected.
2. **Open the style menu.** [BRANCH: Word | Google Docs] In Word, use Home > Styles; in Google Docs, use the style menu that usually says Normal text. → *Expect:* heading style options are visible.
3. **Choose the correct level.** Select Heading 1 for major sections, Heading 2 for subsections, or a lower level for nested sections. → *Expect:* the selected text changes to the heading style.
4. **Check document navigation.** Open Navigation Pane in Word or Document outline in Google Docs if needed. → *Expect:* the heading appears in the document outline at the correct level.

## Decision points

- The line is a title → use Title or document title style if required, not Heading 1.
- The heading should appear in a table of contents → use a built-in heading style rather than manual bold text.

## Failure modes & recovery

- **F1 Wrong level applied:** detect: the heading appears too high or too low in the outline → recover by applying the correct heading level.
- **F2 Only formatting changed manually:** detect: text looks bold but is missing from the outline → recover by selecting a built-in heading style.
- **F3 Extra text became heading:** detect: body text appears in the outline → recover by selecting that text and applying Normal text.

## Verification

The selected line uses the intended built-in heading style and appears correctly in the document outline if the outline is available.

## Variations

- `word`: View > Navigation Pane shows headings created with built-in styles.
- `google-docs`: View > Show outline displays styled headings.

## Safety & privacy

This is low risk. In template-controlled documents, use approved heading levels so automated tables of contents and accessibility tools work.
