---
name: run-a-spellcheck
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

Spelling and basic writing errors are reviewed and corrected in a document.

## Preconditions

- A document or text editor is open.
- The document language is known.

## Steps

1. **Set the document language if needed.** [BRANCH: Word | Google Docs] In Word, use Review > Language > Set Proofing Language; in Google Docs, use File > Language. → *Expect:* the proofing language matches the document.
2. **Start spelling and grammar check.** In Word, choose Review > Editor or Spelling & Grammar; in Google Docs, choose Tools > Spelling and grammar > Spelling and grammar check. → *Expect:* the first suggestion appears.
3. **Review each suggestion.** Read the sentence before accepting, ignoring, or changing a suggestion. → *Expect:* each flagged item is handled deliberately.
4. **Add valid terms if appropriate.** Add names, technical terms, or brand words to the dictionary only when they are correctly spelled. → *Expect:* valid repeated terms stop being flagged.
5. **Finish the checker.** Continue until the tool reports no remaining issues or returns to the start. → *Expect:* the spellcheck session ends without unresolved obvious spelling flags.
6. **Read key passages manually.** Scan headings, names, numbers, and short sentences. → *Expect:* errors that spellcheck may miss are caught.

## Decision points

- The document mixes languages → set language by section or ignore valid foreign-language words.
- A suggestion changes meaning → ignore it and edit manually if needed.

## Failure modes & recovery

- **F1 Wrong language:** detect: many correct words are flagged → recover by setting the correct proofing language.
- **F2 Bad correction accepted:** detect: the sentence meaning changed → recover with Undo and choose a better correction.
- **F3 Checker misses an error:** detect: a typo forms another valid word → recover by manually proofreading important text.

## Verification

The spellcheck tool reports no unresolved spelling issues, and a manual scan of important names and headings shows no obvious errors.

## Variations

- `word`: Microsoft Editor may include grammar, clarity, and style suggestions.
- `google-docs`: Underlined spelling suggestions can be reviewed inline or through the Tools menu.

## Safety & privacy

Cloud editors may process text to provide suggestions. Avoid sending sensitive documents through unfamiliar grammar tools.
