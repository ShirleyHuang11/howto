---
name: review-your-privacy-settings
domain: accounts
subdomain: security
locale: [generic]
interface: web
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You audit an account's privacy settings so only intended people, apps, advertisers, and search engines can see or use your data.

## Preconditions

- Access to the account and its security or privacy settings.
- A current device you trust.
- A sense of what information you want public, limited, or private.

## Steps

1. **Open the account's privacy center.** Look for Privacy, Data, Safety, Visibility, Ads, or Sharing settings. → *Expect:* you are on the page that controls profile visibility and data use.
2. **Review public profile fields.** Check name, photo, bio, location, birthday, workplace, and contact details. → *Expect:* only the fields you intend to show publicly remain visible.
3. **Limit audience and search discovery.** Adjust who can find you by email, phone, username, or search engines. → *Expect:* discovery settings match your desired audience.
4. **Inspect connected apps and integrations.** Remove third-party apps, browser extensions, or devices you no longer use. → *Expect:* only trusted current integrations remain authorized.
5. **Review data-sharing and personalization settings.** Turn off optional ad personalization, partner data sharing, and activity history where you do not want it. → *Expect:* optional tracking settings are disabled or limited.
6. **Check communication and tagging controls.** Restrict who can message, tag, invite, mention, or add you to groups. → *Expect:* unwanted contact routes are limited.
7. **Save changes and recheck from a logged-out view if possible.** View your public profile or use a privacy preview tool. → *Expect:* the visible information matches your intended privacy level.

## Decision points

- Account is professional or public-facing -> keep necessary profile fields visible but remove private contact details.
- You depend on an integration -> verify what it needs before revoking it.
- The service offers a privacy checkup wizard -> use it, then inspect advanced settings manually.

## Failure modes & recovery

- **F1 Setting does not save:** the page reverts after reload -> retry in a supported browser, disable extensions, or use the mobile app.
- **F2 You remove a needed integration:** a device, calendar, or app stops syncing -> reconnect only the specific integration you need.
- **F3 Public data remains indexed:** search engines still show old details -> request removal through the service and search engine cache tools.
- **F4 Hidden audience labels are confusing:** "friends of friends" or "partners" is unclear -> choose the more restrictive option until you understand it.

## Verification

The account privacy page shows the selected restrictive settings, unused integrations are removed, and a public or preview view exposes only intended information.

## Variations

- Social media: focus on audience, tagging, search discovery, and message controls.
- Shopping or delivery accounts: focus on addresses, payment visibility, purchase history, and marketing preferences.
- Workplace tools: some sharing settings may be controlled by the organization.

## Safety & privacy

Medium risk because privacy settings affect personal exposure and account recovery. Do not remove recovery methods while reducing visibility, and confirm changes before disconnecting integrations you rely on.
