---
name: count-words-in-a-document
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

The current word count for a document or selected text is found.

## Preconditions

- A document is open.
- You know whether to count the whole document or only selected text.

## Steps

1. **Select text only if needed.** Highlight the passage to count, or leave nothing selected for the whole document. → *Expect:* either the intended passage is highlighted or the document is unselected.
2. **Open word count.** [BRANCH: Word | Google Docs] In Word, choose Review > Word Count or check the status bar; in Google Docs, choose Tools > Word count or press `Ctrl+Shift+C` on Windows/ChromeOS or `Command+Shift+C` on Mac. → *Expect:* a word count panel or status value appears.
3. **Read the count.** Note the words value and whether it applies to the selection or entire document. → *Expect:* the count matches the intended scope.
4. **Close or pin the count.** Close the dialog, or enable display while typing if available. → *Expect:* the document is ready for continued editing.

## Decision points

- Assignment excludes footnotes, endnotes, or bibliography → check whether the word count tool includes them.
- Only a section matters → select that section before opening word count.

## Failure modes & recovery

- **F1 Wrong scope counted:** detect: count says selected text when whole document was needed, or the reverse → recover by clearing or making the selection and reopening word count.
- **F2 Count differs from requirement:** detect: tool includes excluded sections → recover by selecting only the allowed body text.
- **F3 Shortcut does not work:** detect: no word count opens → recover by using the Tools or Review menu.

## Verification

The displayed word count corresponds to the intended document scope and any stated counting rule.

## Variations

- `word`: The status bar can show live word count; click it for details.
- `google-docs`: The word count dialog can show count while typing.

## Safety & privacy

This is low risk. Do not paste sensitive text into online counters when the built-in document counter is available.
