---
name: audit-your-subscriptions
domain: shopping
subdomain: buying
locale: [generic]
interface: web
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You identify all recurring paid subscriptions, cancel or downgrade waste, and document the expected monthly savings.

## Preconditions

- You can access bank, credit-card, wallet, app-store, and email accounts where subscriptions may appear.
- You can log into subscription services to manage plans.
- You have a decision rule for what to keep, downgrade, cancel, or investigate.

## Steps

1. **Collect recurring charges.** Review the last three to six months of card, bank, wallet, and app-store statements for repeating merchants. → *Expect:* a list of suspected subscriptions with amounts and dates.
2. **Search email for billing terms.** Search for receipts, renewal notices, "subscription", "trial", and merchant names. → *Expect:* each charge has an account email or billing source when possible.
3. **Classify each subscription.** Mark each as keep, cancel, downgrade, share, negotiate, or unknown based on usage and value. → *Expect:* every recurring charge has a next action.
4. **Cancel unused subscriptions.** Use official account or app-store cancellation flows and save confirmation. ⚠️ *Irreversible:* confirm whether cancellation deletes data or ends access immediately before finalizing. → *Expect:* unused plans show canceled or auto-renew off.
5. **Downgrade underused plans.** Change tiers where a lower plan preserves needed features. → *Expect:* billing page shows the cheaper plan and effective date.
6. **Investigate unknown charges.** Contact merchant or card issuer for charges you cannot identify; do not ignore them. → *Expect:* unknown charges are matched to an account or disputed if unauthorized.
7. **Calculate savings and reminders.** Sum monthly savings and set reminders for annual renewals and discounted-plan expirations. → *Expect:* a savings total and future review dates.

## Decision points

- Service stores critical files or data → export data before canceling.
- Annual plan is near renewal → cancel before renewal if value is poor, even if access continues.
- Household members use the plan → confirm before canceling shared essentials.
- Charge is unauthorized → dispute with issuer and secure the affected account.

## Failure modes & recovery

- **F1 Hidden app-store billing:** detect service website has no cancel button → cancel through Apple, Google, Roku, Amazon, carrier, or payment platform.
- **F2 Data loss:** detect cancellation deletes storage or history → export or migrate before confirming.
- **F3 Retention confusion:** detect offer changes date or plan instead of canceling → verify status after accepting or declining.
- **F4 Merchant name mismatch:** detect statement descriptor you do not recognize → search descriptor plus amount and contact issuer if unclear.

## Verification

Every recurring charge found has a keep, downgrade, cancel, or dispute status; canceled services show confirmation; downgraded services show new billing terms; and expected monthly savings are documented.

## Variations

- `family`: include household app stores and shared cards.
- `business`: check invoices, SaaS admin panels, and employee reimbursements.
- `annual-renewals`: search a full year of statements to catch once-a-year plans.

## Safety & privacy

Medium risk because financial accounts and service data are involved. Use official sites, avoid giving bank credentials to untrusted audit apps, and export important data before canceling.
