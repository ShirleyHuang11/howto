---
name: set-up-international-phone-roaming
domain: travel
subdomain: prep
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You set up mobile service for international travel with known coverage, cost, data limits, and backup access to calls and verification codes.

## Preconditions

- Travel countries, dates, and expected data/call/text needs.
- Mobile carrier account access and device model.
- Knowledge of whether your phone is unlocked if considering local SIM or eSIM.

## Steps

1. **Check current plan coverage.** Review your carrier's international roaming page for each destination, including data speed, calls, texts, hotspot, and daily fees. → *Expect:* you know the default cost if you do nothing.
2. **Compare roaming, travel pass, and SIM options.** [BRANCH: carrier roaming, easier setup with possible higher cost | local SIM/eSIM, often cheaper but needs unlocked compatible phone] → *Expect:* you choose the best service option for the trip.
3. **Confirm phone compatibility.** Check eSIM support, unlocked status, destination network bands, and whether your primary number must stay active for bank or work codes. → *Expect:* the chosen option will work on your device.
4. **Activate the plan before departure if required.** Add a travel pass, international package, or eSIM profile through the official carrier/app. → *Expect:* the account shows the travel feature or eSIM installed.
5. **Configure phone settings.** Turn on roaming only when intended, set cellular data line, disable data-hungry background sync, and download offline maps. → *Expect:* the phone is ready without uncontrolled data use.
6. **Preserve two-factor access.** Keep your primary number reachable if banks, work, or travel accounts send SMS codes, or switch them to an authenticator app before departure. → *Expect:* critical accounts can still be accessed abroad.
7. **Save support information offline.** Store carrier international support numbers, eSIM QR codes or activation details, hotel address, and emergency numbers. → *Expect:* help is available without mobile data.
8. **Test on arrival carefully.** Turn off airplane mode, connect to the selected network, place a small test call or load a page, and check carrier usage alerts. → *Expect:* service works and usage is visible.

## Decision points

- Phone is locked → use carrier roaming or ask carrier about unlocking before travel.
- Trip is short and low data → daily travel pass may be simpler than local SIM setup.
- You need reliable work access → arrange hotspot, backup SIM, or portable Wi-Fi instead of relying on hotel Wi-Fi.

## Failure modes & recovery

- **F1 No service on arrival:** detect no network registration → restart phone, manually select a partner network, check roaming setting, or contact carrier on Wi-Fi.
- **F2 Unexpected charges:** detect daily fees or high usage alerts → disable roaming, buy a package, or switch to Wi-Fi/eSIM.
- **F3 eSIM activation fails:** detect QR code or profile error → use Wi-Fi to contact provider and keep the original SIM active until fixed.
- **F4 Verification codes unavailable:** detect bank/work login blocked → use authenticator backup codes, app push, or call the institution from a verified number.

## Verification

Before departure, the phone account or eSIM shows the selected international option active, critical account verification works, offline support details are saved, and on arrival a test connection succeeds without unexpected charges.

## Variations

- `us`: major carriers offer daily international passes or monthly add-ons; terms vary by destination and plan.
- Dual-SIM phone: keep your home number for calls/SMS and use a travel eSIM for data when supported.
- Cruise or airplane: roaming can be much more expensive on maritime or in-flight networks; disable roaming unless you intentionally buy that service.

## Safety & privacy

Medium risk because phone access affects banking, travel documents, maps, and emergency contact. Use official carrier/eSIM sellers, protect account logins, and control roaming settings before connecting to expensive networks.
