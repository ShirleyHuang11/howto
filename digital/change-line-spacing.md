---
name: change-line-spacing
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

Selected text or the whole document uses the intended line spacing.

## Preconditions

- A document is open in a word processor.
- You know the required spacing, such as single, 1.15, 1.5, or double.

## Steps

1. **Select the text to change.** Highlight a paragraph range, or press `Ctrl+A` or `Command+A` to select the whole document. → *Expect:* the intended text is selected.
2. **Open line spacing controls.** [BRANCH: Word | Google Docs] In Word, choose Home > Line and Paragraph Spacing; in Google Docs, choose Format > Line & paragraph spacing. → *Expect:* spacing choices appear.
3. **Choose the spacing.** Select Single, 1.15, 1.5, Double, or a custom spacing option. → *Expect:* the selected text changes vertical spacing.
4. **Check paragraph spacing.** Adjust before or after paragraph spacing if extra gaps remain. → *Expect:* paragraphs have the intended amount of space between them.
5. **Review page flow.** Scroll through the changed section or document. → *Expect:* text is readable and page breaks still fall acceptably.

## Decision points

- A teacher, journal, or template requires exact formatting → use its required spacing and paragraph settings.
- Only one paragraph should change → select only that paragraph before applying spacing.

## Failure modes & recovery

- **F1 Only one line changed:** detect: most text keeps old spacing → recover by selecting the full intended range and applying spacing again.
- **F2 Paragraph gaps look too large:** detect: blank space appears between paragraphs → recover by reducing paragraph before or after spacing.
- **F3 Page count changes unexpectedly:** detect: content moves onto new pages → recover by adjusting spacing or reviewing page breaks.

## Verification

The selected text displays with the intended line spacing, and paragraph gaps match the document requirement.

## Variations

- `word`: Home > Paragraph dialog gives exact line and paragraph spacing values.
- `google-docs`: Custom spacing allows exact line spacing plus paragraph before and after values.

## Safety & privacy

This is low risk. For submissions, verify spacing after exporting to PDF because pagination can change.
