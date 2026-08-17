---
name: spot-a-deepfake
domain: digital
locale: [generic]
interface: web
difficulty: intermediate
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Evaluate whether audio or video may be a deepfake by checking provenance, content, technical clues, and corroborating sources.

## Preconditions

- You have the original post or file when possible.
- You understand that visual or audio clues alone are not reliable proof.

## Steps

1. **Capture the claim.** Record what the media is alleged to show, who shared it, when, and where. → *Expect:* the verification target is specific.
2. **Check the source trail.** Look for the earliest upload, original account, platform labels, content credentials, or creator disclosure. → *Expect:* provenance is known or marked missing.
3. **Inspect technical signs.** Watch for lip-sync mismatch, unnatural blinking, inconsistent lighting, warped jewelry, audio glitches, or odd pauses. → *Expect:* suspicious artifacts are documented.
4. **Compare with known records.** Search for the same event, speech, outfit, room, weather, and public schedule from trusted sources. [BRANCH: public figure | private person] use public records for public figures; avoid spreading private-person media. → *Expect:* context supports, contradicts, or fails to verify the media.
5. **Check for corroboration.** Look for independent witnesses, full-length footage, transcripts, or reputable reporting. → *Expect:* the clip is not evaluated in isolation.
6. **State confidence carefully.** Label the media verified, likely authentic, likely manipulated, or unverified, and explain why. → *Expect:* the conclusion does not overclaim.

## Decision points

- The media could influence voting, violence, reputation, or financial decisions → wait for strong corroboration before sharing.
- The clip is short and emotionally charged → search for the full source before judging.
- It shows sexual content or a private person → do not redistribute it while verifying.

## Failure modes & recovery

- **F1 Cheapfake mistaken for AI:** detect misleading edits, wrong captions, or clipped context → recover by finding the full source.
- **F2 Real clip dismissed:** detect reliance on a single visual artifact → recover by checking provenance and corroboration.
- **F3 Detector conflict:** detect tools disagree → recover by treating detector results as inconclusive.

## Verification

The final assessment cites the original or earliest source found, at least one corroborating or contradicting source, and a confidence label with reasons.

## Variations

- `audio`: compare voice, background noise, cadence, and known recording context.
- `live-event`: check simultaneous coverage and attendees' independent posts.
- `workplace`: preserve evidence and route suspected impersonation to security.

## Safety & privacy

Medium risk because sharing suspected deepfakes can amplify harm. Avoid reposting private, sexual, violent, or defamatory media; describe findings without spreading the file when possible.
