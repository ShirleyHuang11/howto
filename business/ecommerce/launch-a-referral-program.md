---
name: launch-a-referral-program
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

Launch a referral program that gives existing customers a reason to invite real new buyers while limiting self-referral and discount abuse.

## Preconditions

- Ecommerce admin access and a referral or loyalty tool.
- A defined reward for the advocate and the referred customer.
- Fraud controls for duplicate emails, payment methods, addresses, and devices.

## Steps

1. **Define the qualified referral.** Specify first purchase, minimum order value, excluded products, return window, and reward timing. → *Expect:* a written rule for when rewards are earned.
2. **Set reward economics.** Calculate advocate reward, friend discount, margin impact, and maximum monthly payout. → *Expect:* reward cost stays below the acquisition-cost cap.
3. **Configure fraud controls.** Block self-referrals, duplicate accounts, same payment instruments, and reward issuance before the return window if needed. → *Expect:* obvious abuse paths are disabled.
4. **Create referral links and landing copy.** Explain the offer, eligibility, expiration, and privacy terms. → *Expect:* customers can share a trackable link with accurate terms.
5. **Test the full flow.** Use separate test accounts to share, purchase, refund, and qualify or disqualify a referral. ⚠️ *Irreversible:* do not launch until rewards do not issue for refunded or self-referred orders. → *Expect:* qualified purchases trigger rewards and invalid ones do not.
6. **Launch to a controlled segment.** Start with recent satisfied customers or loyalty members before broad promotion. → *Expect:* referral invites are sent only to the intended audience.
7. **Monitor quality and cost.** Track referred conversion, fraud flags, reward liability, refund rate, and customer complaints. → *Expect:* the program produces new qualified customers within the target cost.

## Decision points

- Abuse rate is high → require completed orders and delay rewards until after the return period.
- Margins vary by product → exclude low-margin categories or require a higher minimum order.
- Email sharing drives spam complaints → reduce automated reminders and require explicit opt-in.

## Failure modes & recovery

- **F1 Self-referral:** detect same customer details on both sides → void the reward and tighten matching rules.
- **F2 Reward fires too early:** detect rewards issued before order qualification → pause automation and reconcile pending credits.
- **F3 Referral code leak:** detect coupon sites using private codes → expire leaked codes and move to account-bound links.
- **F4 Tracking failure:** detect purchases without attribution → inspect cookies, UTM parameters, and referral app integration.

## Verification

A test advocate can generate a referral link, a separate eligible buyer can complete a qualifying order, and only after qualification the configured rewards appear for both parties.

## Variations

- `b2b`: referrals may need manual sales approval instead of automatic rewards.
- High-fraud categories: use store credit after delivery rather than instant cash-equivalent rewards.

## Safety & privacy

Medium risk because referral rewards have value and involve contact sharing. Publish clear terms, require consent for messages, and prevent customers from viewing another person's private order details.
