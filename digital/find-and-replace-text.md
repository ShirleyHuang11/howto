---
name: find-and-replace-text
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

One word, phrase, or pattern is located and replaced with the intended text in a document.

## Preconditions

- A document or editor is open.
- You know the exact text to find and the replacement text.

## Steps

1. **Open find and replace.** [BRANCH: Word | Google Docs] In Word, press `Ctrl+H` or `Command+Shift+H`; in Google Docs, choose Edit > Find and replace or press `Ctrl+H` on Windows/ChromeOS. → *Expect:* find and replace fields are visible.
2. **Enter the text to find.** Type the current word or phrase exactly as it appears. → *Expect:* matching instances are highlighted or counted.
3. **Enter the replacement.** Type the new word or phrase in the replace field. → *Expect:* both find and replacement values are visible for review.
4. **Review one match.** Use Find Next, Previous, or the match arrows before replacing all. → *Expect:* the first intended occurrence is selected.
5. **Replace deliberately.** Click Replace for one occurrence or Replace All only when every match should change. → *Expect:* the selected match or all matches update.
6. **Scan the changed areas.** Search for the old text again and read nearby sentences. → *Expect:* intended replacements are present and unintended wording is absent.

## Decision points

- Only exact capitalization should change → enable Match case if available.
- The word appears inside larger words → enable Whole words only if available.
- You are editing a shared or legal document → replace one at a time instead of Replace All.

## Failure modes & recovery

- **F1 No matches found:** detect: count is zero → recover by checking spelling, capitalization, spaces, and punctuation.
- **F2 Too many matches changed:** detect: unrelated words or names changed → recover with Undo and rerun with Match case or Whole words.
- **F3 Replacement text is wrong:** detect: typo appears in updated text → recover by undoing or running another replacement from the typo to the correct text.

## Verification

The old text is absent where it should be changed, and each replacement reads correctly in context.

## Variations

- `word`: Advanced Find and Replace includes Match case, Whole words only, and formatting options.
- `google-docs`: Find and replace can match case and regular expressions.

## Safety & privacy

Bulk replacement can unintentionally alter names, citations, links, or code snippets. Review matches before using Replace All.
