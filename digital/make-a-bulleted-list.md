---
name: make-a-bulleted-list
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

Separate lines of text are formatted as a bulleted list.

## Preconditions

- A document or rich text editor is open.
- Each list item is on its own line, or you are ready to type items one by one.

## Steps

1. **Select existing items or place the cursor.** Highlight the lines to convert, or click where a new list should start. → *Expect:* the target lines are selected or the cursor is ready.
2. **Turn on bullets.** Click the Bullets button or choose Format > Bullets and numbering > Bulleted list. → *Expect:* each selected line starts with a bullet, or a new bullet appears.
3. **Type list items.** Type an item and press `Enter` for the next bullet. → *Expect:* a new bullet appears on the next line.
4. **End the list.** Press `Enter` on a blank bullet line, or turn the Bullets button off. → *Expect:* the cursor returns to normal paragraph text.
5. **Adjust item levels if needed.** Press `Tab` to indent an item or `Shift+Tab` to move it back. → *Expect:* the bullet level changes without losing the item text.

## Decision points

- Item order matters → use a numbered list instead of bullets.
- The list has sub-items → use indentation consistently and avoid too many levels.

## Failure modes & recovery

- **F1 One long bullet appears:** detect: several items stay on one bullet → recover by placing each item on its own line and applying bullets again.
- **F2 Bullets continue after the list:** detect: new paragraphs keep bullet marks → recover by pressing `Enter` on an empty bullet or toggling bullets off.
- **F3 Indentation is wrong:** detect: bullets appear at the wrong level → recover with `Tab`, `Shift+Tab`, or decrease/increase indent buttons.

## Verification

Each intended item appears as its own bullet, and normal text resumes after the list.

## Variations

- `word`: Home > Paragraph contains the Bullets and indentation controls.
- `google-docs`: Toolbar bullets and Format > Bullets and numbering both work.

## Safety & privacy

This is low risk. Review pasted lists for hidden sensitive items before sharing the document.
