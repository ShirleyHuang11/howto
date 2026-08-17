---
name: opt-out-of-data-brokers
domain: digital
locale: [generic]
interface: web
difficulty: advanced
est_time: 2h-4h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Reduce personal information exposed by data brokers by finding listings, submitting opt-out requests, and tracking removals.

## Preconditions

- You can receive email verification messages and, in some cases, identity verification prompts.
- You have a secure place to track requests and confirmation numbers.

## Steps

1. **Prepare identity variants.** List common names, previous names, cities, phone numbers, emails, and addresses that brokers may use. → *Expect:* search terms cover likely records.
2. **Search major broker sites.** Look for your listings using exact and variant details. → *Expect:* you identify records to remove.
3. **Submit opt-out requests.** Use each broker's removal or suppression form and provide only the minimum information required to match the record. → *Expect:* each request is submitted or queued for verification.
4. **Complete verification.** Open confirmation emails or forms and confirm the removal request. [BRANCH: email verification | identity verification] use email when available; avoid sending ID unless the broker is legitimate and the risk is acceptable. → *Expect:* the broker confirms receipt.
5. **Track deadlines.** Record broker name, URL, date submitted, confirmation code, and promised removal time. → *Expect:* pending removals can be followed up.
6. **Recheck listings.** After the stated window, search again and resubmit if the listing remains. → *Expect:* removed records no longer appear or are suppressed.

## Decision points

- The broker asks for government ID → verify the broker and consider whether the exposure risk is worse than sending ID.
- You face stalking, harassment, or doxxing risk → prioritize brokers exposing address, phone, relatives, or workplace.
- Manual opt-out is too much → consider a reputable paid removal service, but review its access and cancellation terms.

## Failure modes & recovery

- **F1 Listing returns:** detect the same record reappears after removal → recover by resubmitting and checking source records that feed the broker.
- **F2 Phishing opt-out:** detect a suspicious domain or excessive data request → recover by navigating from the broker's official site and not using emailed links.
- **F3 Incomplete match:** detect only one name or address variant removed → recover by submitting separate requests for each variant.

## Verification

Your tracking sheet shows submitted and confirmed requests, and follow-up searches no longer show the targeted broker listings or show them as suppressed.

## Variations

- `us`: state privacy laws may create additional opt-out rights depending on residence.
- `high-risk`: use a dedicated email alias and document every removal attempt.
- `family`: repeat for household members whose records reveal your address.

## Safety & privacy

Medium risk because opt-out forms can require personal data. Provide the minimum needed, use a dedicated email alias, and beware of fake removal sites collecting more information.
