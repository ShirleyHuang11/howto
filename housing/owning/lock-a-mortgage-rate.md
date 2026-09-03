---
name: lock-a-mortgage-rate
domain: housing
subdomain: owning
locale: [generic, us]
interface: web
difficulty: intermediate
est_time: 30min-1d
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-02
---

## Goal

You secure a mortgage interest rate for a defined period and understand the cost, expiration, and conditions before relying on it for closing.

## Preconditions

- You have chosen a lender and loan program.
- You know the expected closing date and whether the property is under contract.
- You have a written quote showing rate, points, lender credits, and lock period options.

## Steps

1. **Confirm the closing timeline.** Compare the contract closing date to the lender's processing and appraisal timeline. → *Expect:* a lock period long enough to reach closing with a small cushion.
2. **Request current lock options in writing.** Ask for available rates with points, credits, and 30-, 45-, 60-, or longer lock costs. → *Expect:* a written rate sheet or quote for your scenario.
3. **Compare the cost of each option.** Decide whether a lower rate with points, a no-point rate, or a lender-credit rate best fits your budget. → *Expect:* a selected rate structure and break-even logic.
4. **Ask about lock rules.** Confirm float-down availability, extension fees, relock rules, property address requirements, and what changes can void pricing. → *Expect:* you understand when the lock can change.
5. **Authorize the lock.** Follow the lender's required process in the portal, by email, or by signed disclosure. → *Expect:* the lender sends a lock confirmation with rate, points, expiration date, and loan terms.
6. **Monitor conditions that affect the lock.** Report changes in loan amount, down payment, credit, occupancy, property type, or closing date immediately. → *Expect:* the lender confirms whether pricing still applies.
7. **Extend before expiration if needed.** If closing slips, ask for extension cost and who pays before the lock expires. → *Expect:* the lock remains valid through closing or you have new written pricing.

## Decision points

- Closing date is uncertain → choose a longer lock or delay locking until risk is lower.
- Rates fall after locking → ask whether a float-down is available and what it costs.
- Lock expires before closing → compare extension fee against current market relock options.

## Failure modes & recovery

- **F1 Lock expiration:** detect a closing delay past the expiration date → request an extension before expiration and document cost responsibility.
- **F2 Verbal-only lock:** detect no written confirmation → do not rely on it; ask for written lock terms.
- **F3 Pricing changed after scenario change:** detect new points or credits → ask what loan variable changed and whether it can be restored.
- **F4 Misunderstood points:** detect surprise cash needed at closing → compare the lock confirmation to the Loan Estimate and ask for correction if needed.

## Verification

You have a written lock confirmation showing rate, APR or loan terms, points or credits, lock expiration, property address if required, and a plan to close before expiration.

## Variations

- `us`: mortgage rate locks are lender-specific agreements; float-down features are optional and must be written into the lender's policy.
- New construction: long-term locks may cost more and often have stricter extension rules.

## Safety & privacy

Medium risk because lock choices affect thousands of dollars over time. Do not rely on verbal pricing, and confirm expiration and points before removing financing contingencies or scheduling closing.
