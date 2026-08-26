---
name: export-your-order-history
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

You export a usable order history from a merchant or marketplace account so purchases can be audited, summarized, returned, reimbursed, or archived.

## Preconditions

- You can sign in to the merchant account and pass any multi-factor check.
- You know the date range and purpose for the export.
- You have a secure place to store CSV, PDF, JSON, or archive files that may contain personal and payment data.

## Steps

1. **Define the export scope.** Choose the date range, order statuses, and categories you need before opening the account tools. → *Expect:* a clear scope such as "all completed orders from 2025-01-01 through 2025-12-31."
2. **Open order history or privacy tools.** Sign in directly through the merchant's site and look for Orders, Purchase history, Account data, Privacy, or Download data. → *Expect:* a page lists past orders or offers a data export request.
3. **Choose the most structured format available.** Prefer CSV or JSON for analysis; use PDF only if no structured export exists. → *Expect:* the site shows an export, download, or request option with the chosen format.
4. **Filter to the intended range.** Apply date, order status, marketplace, or account filters. → *Expect:* the on-screen count or preview matches the expected period and excludes unrelated orders.
5. **Request or download the export.** ⚠️ *Irreversible:* if the request emails a data archive or exposes sensitive history, confirm the destination email and account are yours before submitting. → *Expect:* the file downloads immediately or the site confirms an export request with a processing window.
6. **Verify the file opens correctly.** Open the export in a spreadsheet, text editor, or PDF viewer without changing its contents. → *Expect:* rows or pages show order dates, order IDs, item descriptions, totals, taxes, shipping, and statuses.
7. **Store the raw export and a working copy.** Keep the original unchanged and make a separate copy for sorting, formulas, or redaction. → *Expect:* both files are saved in secure storage with names that include merchant and date range.
8. **Reconcile a sample against the site.** Pick three orders from different months and compare the export fields to the live order pages. → *Expect:* sampled order IDs, dates, totals, and statuses match the account.

## Decision points

- Export is for taxes or reimbursement → preserve the raw file and record the download date.
- Export omits line items → download individual receipts for the orders that need item-level proof.
- Account offers only a privacy archive → expect a delay and a large file containing more than order data.
- Multiple household or business accounts exist → export each account separately and label the owner.

## Failure modes & recovery

- **F1 Export request never arrives:** detect no email or account notification after the stated window → check spam, verify account email, and request again only after confirming no duplicate is pending.
- **F2 CSV opens with broken columns:** detect totals, dates, or item names shifted into wrong columns → import with the correct delimiter and encoding instead of double-clicking the file.
- **F3 Date range incomplete:** detect missing months or statuses → adjust filters to include canceled, returned, archived, or marketplace-seller orders.
- **F4 Archive exposes excess data:** detect addresses, messages, or payment metadata beyond the need → keep the raw archive private and create a redacted working extract.

## Verification

A readable export covering the intended date range is stored securely, includes order IDs, dates, statuses, and totals, and at least three sampled orders match the merchant's live order details.

## Variations

- `marketplace`: third-party seller orders, digital purchases, subscriptions, and grocery orders may live in separate order-history tabs.
- `privacy-law-export`: some regions require merchants to provide downloadable account data after an identity check.
- `business`: save exports by fiscal period and attach them to accounting records.

## Safety & privacy

Medium risk because order history reveals identity, addresses, habits, and payment metadata. Export only from the official site, store the raw file privately, and redact before sharing.
