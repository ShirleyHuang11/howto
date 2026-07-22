---
name: password-protect-a-pdf
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 5min-15min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

A PDF requires a password to open, and the password is shared separately from the file.

## Preconditions

- A PDF and a PDF app that can encrypt or password-protect files.
- A way to send the password through a different channel, such as phone, text, password manager share, or separate secure message.

## Steps

1. **Make a copy of the PDF.** Keep the original unprotected until you confirm the protected version opens. → *Expect:* two files exist, original and protected working copy.
2. **Open security settings.** Use Protect, Encrypt, Set Password, Export as PDF with password, or equivalent in your PDF tool. → *Expect:* the app offers an open password or document-open password.
3. **Set an open password.** Choose the option that requires a password to view the PDF, not only a permissions password for editing or printing. → *Expect:* the settings say the document requires a password to open.
4. **Use a strong password.** Use a password manager to generate a long unique password, or a memorable passphrase with several random words. → *Expect:* the password is not reused from an account.
5. **Save the protected PDF.** Save with a clear filename such as `statement-protected.pdf`. → *Expect:* the file writes successfully and remains a PDF.
6. **Test from closed state.** Close the PDF fully, reopen it, and enter the password. → *Expect:* the viewer blocks access until the correct password is entered.
7. **Share file and password separately.** [BRANCH: email | secure portal] Send the PDF in one place and the password by another method. → *Expect:* no single intercepted message contains both file and password.
8. **Document removal steps.** If you need to remove protection later, open with the password, return to security settings, clear the open password, and save a new copy. → *Expect:* the unprotected copy opens without a prompt.

## Decision points

- Recipient cannot open encrypted PDFs → ask what viewer they use and consider a secure upload portal instead.
- You need to prevent editing but not opening → permissions passwords are different and weaker than open passwords for confidentiality.
- The PDF contains highly sensitive records → use an encrypted portal or password-manager share instead of ordinary email.

## Failure modes & recovery

- **F1 Password forgotten:** detect that no copy opens, recover from the original or from a secure password-manager record.
- **F2 Only editing is blocked:** detect the PDF opens without a password, recover by setting a document-open password.
- **F3 Recipient locked out:** detect the recipient sees a wrong-password prompt, recover by confirming capitalization and sharing the password again by a separate channel.
- **F4 Weak encryption warning:** detect the app offers old compatibility such as Acrobat 5 or 40-bit encryption, recover by choosing modern compatibility.

## Verification

Closing and reopening the protected PDF prompts for the open password, and the correct password reveals the expected pages.

## Variations

- Adobe Acrobat Pro: Protect > Encrypt > Encrypt with Password, then require a password to open.
- macOS Preview: File > Export, enable permissions or encryption options depending on macOS version.
- Office apps: export to PDF with password before sending when the original is a Word, Excel, or PowerPoint file.

## Safety & privacy

PDF passwords protect only as well as the password and encryption mode. Share passwords separately, avoid reuse, and keep an unprotected original only in a secure location.
