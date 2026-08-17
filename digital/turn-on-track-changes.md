---
name: turn-on-track-changes
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

Future edits are recorded as tracked changes so reviewers can see what changed.

## Preconditions

- A document is open in an editor that supports change tracking.
- You have permission to edit or suggest changes.

## Steps

1. **Find the tracking control.** [BRANCH: Word | Google Docs] In Word, choose Review > Track Changes; in Google Docs, use the mode menu near Share and choose Suggesting. → *Expect:* tracking or suggesting mode is visibly enabled.
2. **Make a small test edit.** Add or delete a word in a harmless spot. → *Expect:* the edit appears as markup, a suggestion, or a colored change.
3. **Undo the test edit if needed.** Press `Ctrl+Z` or `Command+Z` after confirming tracking works. → *Expect:* the test change disappears.
4. **Continue editing normally.** Type, delete, and format as needed while tracking stays on. → *Expect:* new edits appear as tracked changes or suggestions.

## Decision points

- You only want to leave notes → use comments instead of tracked changes.
- The document is final or confidential → confirm the owner wants markup before editing.

## Failure modes & recovery

- **F1 Edits are not marked:** detect: typed changes appear as normal text → recover by turning on Track Changes or Suggesting before editing further.
- **F2 Cannot enable tracking:** detect: control is unavailable or read-only → recover by requesting edit permission or making a copy.
- **F3 Markup is hidden:** detect: tracking is on but changes are not visible → recover by changing display from No Markup to All Markup or showing suggestions.

## Verification

A new edit appears as a tracked change, suggestion, or visible markup rather than silently changing the document.

## Variations

- `word`: Review > Tracking > Display for Review controls how markup is shown.
- `google-docs`: Suggesting mode records proposed edits that can be accepted or rejected.

## Safety & privacy

Tracked changes can reveal deleted text, reviewer names, timestamps, and editing history. Inspect the final file before sharing outside the intended group.
