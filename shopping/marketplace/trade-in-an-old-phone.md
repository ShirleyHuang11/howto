---
name: trade-in-an-old-phone
domain: shopping
subdomain: marketplace
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h-2h
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You trade in an old phone for a quoted credit or payout after backing up, wiping, and documenting the device so your data and value are protected.

## Preconditions

- The phone, charger if required, IMEI/serial number, and account credentials needed to unlock it.
- A destination trade-in program, carrier, manufacturer, retailer, or buyback site.
- Time to back up and factory reset the phone before shipment or handoff.

## Steps

1. **Identify the phone accurately.** Record model, storage, color, carrier lock status, IMEI/serial, battery health, and visible damage. → *Expect:* the quote matches the actual device.
2. **Check eligibility and value.** Compare trade-in offers from carrier, manufacturer, retailer, and buyback sites, including promo requirements. → *Expect:* a best offer and fallback offer are selected.
3. **Confirm ownership and account status.** Pay off financed balances if required, remove activation locks, and verify the phone is not reported lost or stolen. → *Expect:* the phone is eligible for transfer.
4. **Back up personal data.** Save photos, contacts, messages, authenticator accounts, and app data to your new phone or cloud. → *Expect:* needed data is accessible somewhere else.
5. **Document condition.** Take photos/video of the phone working, IMEI screen if safe, battery health, body condition, and packaging. → *Expect:* evidence exists before trade-in inspection.
6. **Accept the trade-in quote.** Enter exact device details and choose mail-in or in-store trade-in. ⚠️ *Irreversible:* confirm estimated value, promo terms, and data backup before committing. → *Expect:* a trade-in order, label, appointment, or confirmation number is issued.
7. **Remove accounts and wipe the phone.** Sign out of device accounts, disable activation lock, remove SIM/eSIM where appropriate, and factory reset. → *Expect:* the phone boots to setup or trade-in-ready state with no personal account attached.
8. **Send or hand over the phone.** [BRANCH: mail-in, pack securely and get carrier acceptance scan | in-store, obtain written receipt before leaving] → *Expect:* you have proof the device entered the trade-in process.
9. **Monitor inspection and credit.** Watch for revised value notices and respond before deadlines. → *Expect:* final value is accepted or you choose return if the revision is too low.
10. **Confirm payout or bill credit.** → *Expect:* credit, gift card, or cash payout posts to the promised account.

## Decision points

- Promo requires a new line, plan, or financing → calculate total cost, not just trade-in value.
- Revised value is below your floor → reject and request return if the program allows it.
- Activation lock cannot be removed → resolve account access before shipping.
- Device has serious damage → compare repair, parts sale, and damaged-device quotes.

## Failure modes & recovery

- **F1 Data not backed up:** detect missing photos or authenticator access after reset → restore from backup if available; delay reset until verified next time.
- **F2 Activation lock rejection:** detect inspection failure for account lock → remotely remove the device from your account and contact support.
- **F3 Value downgrade:** detect revised offer for condition mismatch → use pre-shipment photos to dispute or request return.
- **F4 Lost shipment:** detect tracking stall → file a carrier/platform claim using drop-off receipt and trade-in number.
- **F5 Promo credit missing:** detect bill credit not posted after promised window → contact carrier with trade-in confirmation and device receipt.

## Verification

The old phone is wiped and removed from your accounts, the trade-in provider confirms receipt and final acceptance, and the promised credit or payout has posted or is scheduled in writing.

## Variations

- Carrier promo: verify monthly bill-credit schedule and early payoff consequences.
- Manufacturer trade-in: credit may apply to a new device order rather than cash.
- In-store trade-in: keep the printed receipt until the credit appears.

## Safety & privacy

Medium risk because phones contain identity, photos, payment tokens, and account access. Back up first, remove activation locks, factory reset, remove SIM/eSIM, and keep documentation until final credit posts.
