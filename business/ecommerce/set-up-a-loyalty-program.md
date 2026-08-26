---
name: set-up-a-loyalty-program
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

Launch a loyalty program that rewards repeat customers while keeping reward liability and discount cost under control.

## Preconditions

- Ecommerce admin access and permission to install or configure loyalty tools.
- Historical order values, gross margin, and repeat-purchase data.
- A privacy policy and email/SMS consent process that covers loyalty communications.

## Steps

1. **Define the reward economics.** Choose points per currency spent, redemption value, exclusions, expiration, and a monthly liability cap. → *Expect:* a written rule set with an estimated reward cost per order.
2. **Choose eligible actions.** Decide whether customers earn for purchases only or also for account creation, reviews, birthdays, and referrals. → *Expect:* each earn action has a fraud risk and reward value assigned.
3. **Configure the loyalty tool.** Set earning rules, redemption rules, customer account requirements, and excluded products or discounts. → *Expect:* the admin shows the program rules saved and inactive or in test mode.
4. **Add customer-facing explanations.** Update account pages, checkout messaging, and help content with plain terms. → *Expect:* customers can see how points are earned, redeemed, and expired.
5. **Test earn and redeem flows.** Place test orders, cancel one, refund one, and redeem points on a new cart. ⚠️ *Irreversible:* do not launch until refunds and cancellations reverse points correctly. → *Expect:* point balances change exactly as the policy says.
6. **Launch to a limited audience first.** Enable for staff, VIP customers, or a small segment before full rollout. → *Expect:* real accounts earn and redeem points without support intervention.
7. **Monitor cost and abuse.** Review redemption rate, liability balance, suspicious account creation, and margin impact weekly. → *Expect:* the program stays within the planned reward budget.

## Decision points

- Margins are thin → use non-discount perks such as early access instead of high cash-equivalent points.
- Fraudulent signups appear → remove signup points or require a paid order before redemption.
- Reward liability grows too quickly → add expiration, lower earn rate, or cap redemptions.

## Failure modes & recovery

- **F1 Points not reversed on refunds:** detect refunded orders retaining points → pause redemptions and reconcile affected accounts.
- **F2 Coupon stacking abuse:** detect loyalty rewards combined with deep promotions → set exclusion rules and adjust terms.
- **F3 Consent complaint:** detect customers receiving unwanted messages → audit opt-in source and suppress non-consented contacts.
- **F4 Unclear balance disputes:** detect customers challenging missing points → keep event logs and publish eligibility rules.

## Verification

The loyalty program is live for the intended audience, a test customer earns and redeems points under the published rules, and the estimated reward cost per order is within the configured cap.

## Variations

- `us`: loyalty programs may create tax and privacy obligations; retain clear terms.
- Subscription stores: reward retention milestones instead of only one-time purchase value.

## Safety & privacy

Medium risk because rewards act like store value and customer behavior is tracked. Disclose terms, avoid enrolling people into marketing without consent, and monitor outstanding point liability.
