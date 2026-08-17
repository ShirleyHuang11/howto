---
name: add-page-numbers
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

Page numbers appear in the document header or footer in the chosen position.

## Preconditions

- A multi-page document is open.
- You know whether numbers should appear at the top, bottom, left, center, or right.

## Steps

1. **Open page number options.** [BRANCH: Word | Google Docs] In Word, choose Insert > Page Number; in Google Docs, choose Insert > Page numbers. → *Expect:* page number placement options appear.
2. **Choose a position.** Select top or bottom of page and the alignment you need. → *Expect:* page numbers appear on document pages.
3. **Check the first page setting.** Enable or disable different first page if the title page should not show a number. → *Expect:* the first page follows the intended numbering rule.
4. **Review several pages.** Scroll through the beginning, middle, and end of the document. → *Expect:* numbering increments in order.
5. **Close header or footer editing.** Click back in the document body or choose Close Header and Footer. → *Expect:* the document returns to normal editing mode.

## Decision points

- Title page should be unnumbered → use different first page or start numbering after the title page.
- Required format is "Page 1 of 5" → choose a page count option if the editor provides one.

## Failure modes & recovery

- **F1 Number appears on title page:** detect: page 1 displays a number when it should not → recover by enabling different first page or section-specific numbering.
- **F2 Numbering restarts unexpectedly:** detect: later pages repeat page 1 → recover by checking section breaks and linking headers or footers as needed.
- **F3 Number is in the wrong spot:** detect: number appears top instead of bottom or wrong alignment → recover by reopening Insert > Page Number and choosing the correct placement.

## Verification

Each required page shows the correct page number in sequence and in the intended header or footer position.

## Variations

- `word`: Layout > Breaks and Header & Footer tools control section-based numbering.
- `google-docs`: Options in the header or footer control first page and starting number.

## Safety & privacy

This is low risk. Verify page numbers after exporting or printing because section breaks can change numbering.
