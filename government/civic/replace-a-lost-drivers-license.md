---
name: replace-a-lost-drivers-license
domain: government
subdomain: civic
locale: [generic, us]
interface: mixed
difficulty: basic
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You report or replace a lost driver's license through the correct motor vehicle agency and receive a valid temporary or replacement credential.

## Preconditions

- Your legal name, date of birth, current address, license number if known, and last four digits of your SSN if required.
- Access to your state DMV, RMV, BMV, MVD, or equivalent motor vehicle portal.
- A payment card and proof of identity or address if your state requires an office visit.

## Steps

1. **Confirm the license is actually missing.** Check wallet, vehicle, recent bags, and any place where the card was scanned. → *Expect:* you know whether this is a lost-card replacement, not a renewal or address-change request.
2. **Check for identity-theft signs.** Review recent credit alerts, bank activity, and mail for suspicious activity. → *Expect:* no evidence of misuse, or you have a note to file an identity-theft report separately.
3. **Open your state motor vehicle replacement page.** Search only the official state DMV-style domain or start from your state government website. → *Expect:* the page describes duplicate or replacement driver's license requests for your state.
4. **Choose the allowed replacement channel.** [BRANCH: eligible online, sign in and start a duplicate license request | not eligible online, schedule or prepare for an office visit] → *Expect:* the agency shows the required method for your license type.
5. **Verify your identity and address.** Enter requested personal details exactly as they appear on the current DMV record. → *Expect:* the system finds your license record or tells you what document is missing.
6. **Request a duplicate card.** Confirm whether you need a standard license, REAL ID replacement, commercial license replacement, or permit replacement. → *Expect:* the replacement request summary matches the credential you lost.
7. **Pay the replacement fee.** ⚠️ *Irreversible:* confirm the mailing address and license type before payment because fees may be nonrefundable. → *Expect:* the DMV accepts payment and issues a receipt.
8. **Save the temporary credential if offered.** Print or download the temporary license and note any driving limits. → *Expect:* you have proof of licensure while waiting for the physical card.
9. **Watch for the replacement card.** Track mail delivery if the agency provides tracking and store the new card securely when it arrives. → *Expect:* the replacement license arrives at the address on record.

## Decision points

- Your address changed → complete the DMV address-change step before or during replacement if the portal requires it.
- Your license expires soon → compare replacement versus renewal; renewal may be more efficient if allowed.
- The card may have been stolen → file a police report only if your state, insurer, or identity-theft recovery process needs one.
- You hold a CDL or noncitizen credential → expect extra documentation or in-person handling.

## Failure modes & recovery

- **F1 Record not found:** detect a portal error after identity entry → check spelling, old address, and license number; then call the DMV or visit an office with ID documents.
- **F2 Address mismatch:** detect that the portal will mail to an old address → update the address through the DMV first or choose an office appointment.
- **F3 Payment accepted but no receipt:** detect a card charge without confirmation → wait for the agency email, then contact DMV support with the transaction details before resubmitting.
- **F4 Temporary license not valid for your need:** detect that a bar, TSA checkpoint, or employer requires photo ID → use a passport or other accepted ID until the card arrives.

## Verification

The DMV portal or office has issued a receipt or temporary credential, and the replacement card is either mailed, printed, or available for pickup under your name.

## Variations

- `us`: agency names vary by state, such as DMV, RMV, BMV, MVD, or DPS; requirements and fees are state-specific.
- `REAL ID`: a replacement usually preserves existing REAL ID status, but upgrading from non-REAL ID generally requires proof documents.
- `mobile license state`: a digital license may be available, but it may not replace the physical card for every use.

## Safety & privacy

Medium risk because a lost license exposes identity information. Use only official state sites, avoid entering SSN or card details through search ads, and confirm the mailing address before paying.
