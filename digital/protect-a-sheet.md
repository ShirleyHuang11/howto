---
name: protect-a-sheet
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Protect a spreadsheet sheet so accidental edits are blocked or warned against.

## Preconditions

- A spreadsheet is open and you have permission to protect the sheet.
- You know whether any cells should remain editable.

## Steps

1. **Select the sheet to protect.** Click the sheet tab containing the data or formulas to guard. → *Expect:* the intended sheet is active.
2. **Open protection settings.** [BRANCH: Excel | Google Sheets] Excel: choose `Review > Protect Sheet`; Google Sheets: choose `Data > Protect sheets and ranges`. → *Expect:* protection options appear.
3. **Set allowed edits.** Choose whether users can select cells, sort, filter, or edit specific ranges. → *Expect:* the settings match the intended editing limits.
4. **Apply protection.** [BRANCH: Excel | Google Sheets] Excel: enter an optional password and click `OK`; Google Sheets: click `Set permissions` and choose warning-only or restricted editors. → *Expect:* the sheet shows protection is active.
5. **Test a blocked edit.** Try editing a protected cell, then cancel the change. → *Expect:* Excel blocks the edit or Google Sheets shows a warning or permission message.

## Decision points

- Need a warning but not a hard block → use warning-only protection in Google Sheets.
- Need some input cells editable → unlock those cells first in Excel or protect only selected ranges in Google Sheets.
- Password might be forgotten → store it securely or use permissions instead when available.

## Failure modes & recovery

- **F1 Needed cells blocked:** detect users cannot edit input cells → adjust unlocked cells or protected ranges.
- **F2 Password lost:** detect protection cannot be removed → restore from an unprotected backup or use account permissions where possible.
- **F3 False sense of security:** detect sensitive data remains visible → use sharing permissions or remove data, because sheet protection is not encryption.

## Verification

A protected cell cannot be edited without permission or confirmation, while any intended editable cells remain editable.

## Variations

- `excel`: Cell locking takes effect only after `Review > Protect Sheet` is enabled.
- `google-sheets`: Protected ranges can restrict specific collaborators.

## Safety & privacy

Low risk. Sheet protection prevents accidental edits but does not hide or encrypt sensitive information from people who can view the file.
