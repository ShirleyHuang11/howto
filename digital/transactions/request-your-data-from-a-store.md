---
name: request-your-data-from-a-store
domain: digital
subdomain: transactions
locale: [generic]
interface: web
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You request a copy of the personal data a store holds about you and save the response securely for review or portability.

## Preconditions

- You can access the store account or the email address associated with it.
- You are willing to complete identity verification if the store requires it.
- You have secure storage for an archive that may contain addresses, order history, messages, preferences, and payment metadata.

## Steps

1. **Find the official privacy request path.** Use the store's Privacy, Account data, Download my data, or Data subject request page. → *Expect:* you are on a store-owned page that describes data access requests.
2. **Choose the access/export request type.** Select request a copy, access my data, or data portability rather than deletion or opt-out. → *Expect:* the form clearly asks the store to provide your data, not erase it.
3. **Enter only required identity details.** Provide account email, name, region, and order number only if required to locate the account. → *Expect:* the form accepts the minimum information needed to process the request.
4. **Select scope and format.** [BRANCH: broad audit, request all account data | specific transaction review, request order, payment, and communication data for the relevant period] → *Expect:* the request scope is visible before submission.
5. **Submit the request.** ⚠️ *Irreversible:* confirm the email address is yours because the response may contain sensitive account history. → *Expect:* the site or email confirms the request ID and expected response timeframe.
6. **Complete verification promptly.** Respond to confirmation emails or identity checks from the official store domain. → *Expect:* the request status changes to verified, processing, or accepted.
7. **Download the archive when available.** Use the official link before it expires and avoid public Wi-Fi for the download. → *Expect:* a ZIP, JSON, CSV, PDF, or HTML archive downloads successfully.
8. **Store and inspect safely.** Save the original archive privately, scan filenames for categories, and open a copy for review. → *Expect:* you can locate order history, account profile, addresses, and other requested data without altering the original.

## Decision points

- Store asks for excessive ID → check its privacy policy and consider contacting privacy support before uploading documents.
- You want data deleted too → complete the access request first, then decide on deletion after saving anything needed.
- Request is tied to a legal region → use the region where you live or where the account is registered.
- Download link expires quickly → schedule time to retrieve and verify the archive as soon as the notice arrives.

## Failure modes & recovery

- **F1 Verification email missing:** detect no confirmation message → check spam, confirm the account email, and resubmit only if there is no request ID.
- **F2 Wrong request type submitted:** detect a deletion or marketing opt-out confirmation → contact privacy support immediately to cancel or correct the request.
- **F3 Archive cannot be opened:** detect a corrupt ZIP or unsupported format → redownload before expiration or request a fresh link.
- **F4 Sensitive archive mishandled:** detect it saved to a shared folder or work computer → move it to private storage, revoke sharing, and delete exposed copies.

## Verification

The store has confirmed a data-access request, the requested archive has been downloaded before link expiration, and the original file is stored securely with the request ID and date.

## Variations

- `us-ca` and `eu`: privacy laws may give specific access rights and response deadlines.
- `guest-checkout`: the store may require order numbers or email verification instead of account login.
- `marketplace`: seller messages, search history, ads data, and payment metadata may be separate export categories.

## Safety & privacy

Medium risk because the export can contain a detailed profile of your identity and purchases. Use only official links, provide minimal identity proof, and store the archive in private encrypted storage.
