---
name: insert-a-table-in-a-document
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

A table with the needed number of rows and columns is inserted into a document.

## Preconditions

- A document editor is open.
- You know roughly how many columns and rows the table needs.

## Steps

1. **Place the cursor.** Click where the table should appear in the document. → *Expect:* the insertion cursor blinks at the table location.
2. **Open the table menu.** [BRANCH: Word | Google Docs] In Word, choose Insert > Table; in Google Docs, choose Insert > Table. → *Expect:* a grid or table size menu appears.
3. **Choose the table size.** Drag or select the number of columns and rows needed. → *Expect:* a blank table appears in the document.
4. **Enter headers.** Type column labels in the first row if the table has categories. → *Expect:* the top row identifies what each column contains.
5. **Fill cells.** Click or press `Tab` to move through cells and enter content. → *Expect:* each cell contains the intended text or data.
6. **Adjust fit.** Drag column borders or use table layout controls so text is readable. → *Expect:* columns and rows fit the content without awkward clipping.

## Decision points

- You need calculations or sorting → use a spreadsheet table and paste or link it into the document.
- The table spans pages → repeat header rows if the editor supports it.

## Failure modes & recovery

- **F1 Wrong size inserted:** detect: too many or too few cells → recover by inserting or deleting rows and columns from the table menu.
- **F2 Text overflows:** detect: content is clipped or wraps badly → recover by widening columns, reducing text, or changing page orientation.
- **F3 Table is hard to read:** detect: rows or headers blend together → recover by applying header bolding, borders, or a simple table style.

## Verification

The table appears at the intended location with the needed rows, columns, headers, and readable cell content.

## Variations

- `word`: Table Design and Layout tabs appear when the cursor is inside the table.
- `google-docs`: Right-click a cell to insert or delete rows and columns.

## Safety & privacy

Tables can make private data easier to scan and copy. Remove unnecessary personal information before sharing.
