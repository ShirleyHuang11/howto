---
name: add-a-comment-to-a-document
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

A comment is attached to specific text or a location in a document without changing the main text.

## Preconditions

- A document is open in an editor that supports comments.
- You know the text or location the comment should refer to.

## Steps

1. **Select the target text.** Highlight the word, sentence, or paragraph the comment should discuss. → *Expect:* the target text is highlighted.
2. **Insert a comment.** [BRANCH: Word | Google Docs] In Word, choose Review > New Comment; in Google Docs, choose Insert > Comment or press `Ctrl+Alt+M` on Windows/ChromeOS or `Command+Option+M` on Mac. → *Expect:* a comment box opens beside the document or near the text.
3. **Type the comment.** Write a clear note, question, or requested change. → *Expect:* the comment text appears in the comment box.
4. **Post the comment.** Click Post, Comment, or press the editor's submit shortcut. → *Expect:* the comment is saved and linked to the selected text.
5. **Check the anchor.** Click the highlighted text or comment marker. → *Expect:* the comment and its related text are connected.

## Decision points

- The text itself needs revision → use tracked changes or direct editing instead of only commenting.
- A person must respond → mention them only if the document's sharing settings allow notifications.

## Failure modes & recovery

- **F1 Comment attaches to the wrong text:** detect: selecting the comment highlights the wrong phrase → recover by deleting it and re-commenting on the correct selection.
- **F2 Comment does not post:** detect: draft disappears or remains unsaved → recover by checking edit permission and posting again.
- **F3 Mention fails:** detect: the person is not suggested or notified → recover by sharing the document with them or using their correct account address.

## Verification

The comment is visible in the document margin or comment panel and is anchored to the intended text or location.

## Variations

- `word`: Comments appear in the margin or Reviewing Pane depending on view settings.
- `google-docs`: Comments can assign action items when a mentioned person has access.

## Safety & privacy

Comments may include author identity and timestamps. Do not place confidential side notes in files that will be shared broadly.
