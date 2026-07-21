---
name: spot-a-phishing-email
domain: digital
locale: [generic]
interface: web
difficulty: intermediate
est_time: 5min
risk: high
prerequisites: [have-email-address]
status: draft
last_verified: 2026-07-20
---

## Goal

A suspicious email correctly classified as phishing or legitimate using a repeatable check sequence — and the phishing one neutralized without a single click, because the click *is* the attack.

## Preconditions

- An email that triggered any instinct: unexpected, urgent, money- or login-adjacent, or just slightly off. The instinct itself is precondition one; this recipe is how you honor it.
- The prime directive already installed: **verify through your own channel, never through the email's.** Every step below is a version of this sentence.

## Steps

1. **Read the pressure, not just the content.** Phishing's signature is manufactured urgency plus a demanded action: account suspended, package held, invoice overdue, boss needs gift cards, "unusual sign-in." Legitimate institutions rarely demand same-hour action by email link. → *Expect:* a pressure-score; high pressure raises the bar for every following check.
2. **Inspect the true sender address, not the display name.** Expand the sender details: display "PayPal" wrapping `paypal-security@accounts-verify.net` is the tell. Lookalike domains (rn for m, extra words, wrong TLD) are the industry standard. → *Expect:* either the institution's exact known domain, or your answer.
3. **Hover, never click, the links.** Hold/long-press or hover to preview each URL: the visible text and the destination diverge in phishing, and the destination's *registered domain* (the part before the first single slash, read right-to-left) is the truth. `paypal.com.secure-login.info` belongs to `secure-login.info`. → *Expect:* every link's real destination read; one mismatch convicts the whole email.
4. **Audit the remaining tells.** Generic greeting ("Dear Customer") where the real institution knows your name; attachment types that execute (.html, .zip, .docm — unexpected attachments are hostile until proven otherwise); reply-to differing from sender; and, decreasingly, language errors (modern phishing is fluently written — absence of typos proves nothing now). → *Expect:* an accumulating verdict, weighted toward the sender and link evidence.
5. **Verify through your own channel when stakes exist.** Anything touching money, logins, or your employer: open the institution's site or app by *typing the address* or using your bookmark (`accounts/log-in` step 1's law), or call the number from your card/statement. The real account's own message center confirms or denies in seconds. → *Expect:* ground truth obtained without the email's participation.
6. **Sentence and execute.** Phishing: report via the mail client's report-phishing button (it trains everyone's filters), then delete; work email forwards to IT/security first — they genuinely want it. Legitimate after all: proceed via your own channel anyway, having lost nothing. → *Expect:* the email dispatched appropriately; zero of its links clicked either way.

## Decision points

- "But I already clicked": clicking alone is exposure, entering credentials is compromise — change that password immediately from a clean device (`accounts/recover-a-password`), enable/verify 2FA (`accounts/enable-two-factor-authentication`), and watch the account's sessions (`accounts/review-account-security` F1's protocol); entered card details → card frozen via the bank now (`finance/dispute-a-card-charge` step 3).
- Spear phishing at work (your boss's name, your project's vocabulary): the verify-out-of-band rule hardens — a 30-second call or chat message to the apparent sender defeats the entire genre ("did you send this?"), and no real boss resents it.
- SMS and messenger variants ("smishing"): identical recipe minus the hover (long-press previews links); the delivery-fee and toll-payment texts are the current volume leaders (`shopping/track-a-delivery` step 2's rule).

## Failure modes & recovery

- **F1 Blocked something legitimate:** the cost asymmetry is the point — a real institution reaches you again through your own channel; a phish only needed once. No apology owed to your bank for logging in directly.
- **F2 The email survives every check but still feels wrong:** trust the residue; verify out-of-band anyway. The checks catch known patterns; your unease catches new ones.
- **F3 Colleague/family already engaged with one:** no blame theater (shame delays reporting); run the already-clicked protocol above with them, and report it — households and teams that talk about phishes get phished less.
- **F4 Reported-and-deleted, then needed the email:** the report usually archives a copy with IT/the provider; the deletion of a suspected phish is never the real loss.

## Verification

The verdict was reached from sender, links, and out-of-band verification — not from the email's own claims; nothing was clicked pre-verdict; the phish was reported, not just deleted; and any already-clicked exposure triggered the password/2FA/card protocol within minutes, not days.

## Variations

- Email from "yourself" or spoofed colleagues (display-name spoofing): the sender-address expansion (step 2) resolves it; SPF/DKIM failures shown by some clients are supporting evidence.
- QR-code phishing ("quishing") in emails and on posters: a QR is a link you can't hover — the own-channel rule is the entire defense.

## Safety & privacy

High risk honestly rated: phishing is the front door of most account takeovers and payment fraud. The three load-bearing habits: read the real sender, read the real link, and verify through your own channel. Everything else in this corpus's accounts and finance domains assumes this recipe is running.
