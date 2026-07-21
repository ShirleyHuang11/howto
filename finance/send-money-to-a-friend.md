---
name: send-money-to-a-friend
domain: finance
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 10min
risk: medium
prerequisites: [have-bank-account]
status: draft
last_verified: 2026-07-20
---

## Goal

Money moves from you to a person you actually know, in the right amount, through a person-to-person channel — with the two dominant failure modes (wrong recipient, impersonation scam) structurally checked.

## Preconditions

- A P2P channel you both can use: bank transfer, or the locally dominant app (Venmo/Zelle/PayPal-class, WeChat/Alipay, revolut/wise-class, bank-app instant transfer).
- The recipient's correct handle/number/IBAN — obtained from *them*, in person or via a channel you already trust.
- The reason is a real personal transfer (splitting a bill, a gift, repayment) — **not** a payment to a stranger for goods; P2P "friends and family" rails have no buyer protection, which is fine among friends and a scam vector with strangers.

## Steps

1. **Confirm the recipient identifier live.** Have them show/send their handle or scan each other's QR in person; for bank transfers, have them paste their account details. Typing a phone number or handle from memory is the wrong-recipient generator. → *Expect:* the identifier arrived from the person, not from your recollection.
2. **Start the payment and check the resolved name.** Enter the handle/number; the app resolves it to a display name and often a profile photo — *stop and read it*. [BRANCH: name matches your friend → continue | unfamiliar name/photo → halt, re-confirm the identifier] → *Expect:* the resolved identity is recognizably them.
3. **Enter the amount and a note.** Decimal check (5.00 vs 500 is the classic), currency check where relevant, and a note ("dinner 7/20") — notes settle later ambiguity and mark the payment's purpose. → *Expect:* amount correct at the cents level; note attached.
4. **Send a test round on first-time transfers of size.** New recipient + meaningful amount → send a trivial amount first, confirm they received it, then send the rest. ⚠️ *Irreversible:* instant P2P transfers (and many bank rails) cannot be recalled — the test-round habit is the only undo you get. → *Expect:* friend confirms the test landed; remainder sent to the now-verified recipient.
5. **Verify completion on both ends.** Your app shows sent/completed; they confirm receipt (the payment can be "sent" into their unclaimed/pending state if their account isn't set up). → *Expect:* mutual confirmation; screenshots exist naturally in the app history.

## Decision points

- Which channel → whatever the *recipient* already uses beats the objectively best app they don't have; cross-border → the wise/revolut-class rails (real exchange rates) beat bank international wires for personal amounts.
- Fees → P2P among friends is typically free from bank balance; card-funded sends often cost a % — fund from balance/bank when the option appears.
- Someone asks *you* for money by message ("Mom" on a new number, a friend "stranded abroad", any urgency + secrecy combination) → this is the impersonation-scam signature: verify by *calling the person on their known number* before any money moves. No legitimate emergency is harmed by a two-minute callback.

## Failure modes & recovery

- **F1 Sent to the wrong person:** contact the recipient in-app requesting return (honest strangers often do), and file with the app's support immediately — but expect that instant rails may make this unrecoverable; the step-2 name check and step-4 test round exist because prevention is the only strong tool.
- **F2 Payment pending/unclaimed for days:** the recipient's account isn't fully set up (unverified, wrong region) — they complete setup or you cancel the unclaimed payment (unclaimed ones usually *can* be canceled) and choose another channel.
- **F3 Amount typo caught after sending:** overpaid a friend — they send the difference back, life continues; this is why friends are the low-stakes tier and strangers are out of scope.
- **F4 "Payment failed" but money left your account:** usually an authorization hold that auto-reverses in days — check the app's transaction state before resending, or you'll double-pay (F3 with extra steps).

## Verification

The intended person confirms receipt of the intended amount, your app history shows one completed payment with its note, no test-round remainder was forgotten, and nothing about the transaction involved a stranger, urgency, or goods.

## Variations

- `us`: Zelle (bank-instant, truly irrevocable — the test round matters most here), Venmo (social feed — set payments private in settings); `cn`: WeChat/Alipay QR between phones is the native gesture; `eu`: SEPA instant transfers by IBAN, name-check (IBAN-name verification) now standard in many countries — read its warning when it disagrees.
- Splitting contexts: `daily/social/split-a-bill` is the upstream recipe; this one is its payment leg.

## Safety & privacy

Medium risk concentrated in irreversibility: resolved-name check, test round, and the callback rule for any requested money are the three locks. Social-feed apps leak your payment graph — set history private once, today.
