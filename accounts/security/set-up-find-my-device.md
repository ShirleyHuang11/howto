---
name: set-up-find-my-device
domain: accounts
subdomain: security
locale: [generic]
interface: mixed
difficulty: basic
est_time: 20min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You enable device-location, lock, and recovery features before a phone, tablet, or laptop is lost.

## Preconditions

- Physical access to the device.
- The device is signed in to the correct Apple, Google, Microsoft, or manufacturer account.
- Location services, internet access, and a screen lock are available.

## Steps

1. **Confirm the device account.** Open account settings and verify the signed-in account is yours and recoverable. → *Expect:* the device is attached to the account you can access from another device.
2. **Set a strong screen lock.** Configure a passcode, PIN, password, or biometric unlock backed by a real passcode. → *Expect:* the device requires authentication after locking.
3. **Enable location services.** Turn on system location services and allow the find-my-device service to use location. → *Expect:* location status is enabled for the recovery service.
4. **Turn on the find-my-device feature.** Enable Find My iPhone, Find My Device, Find My Mobile, or Find my device depending on platform. → *Expect:* the feature shows as on for this device.
5. **Enable offline finding or last known location if offered.** Turn on network-assisted finding, last location, or similar recovery options. → *Expect:* the device can report location even when battery is low or connectivity is limited, if supported.
6. **Test from another device or browser.** Sign in to the official recovery portal and locate the device. → *Expect:* the portal lists the device and shows a recent approximate location or online status.
7. **Record recovery options.** Save the official recovery URL and account recovery details in your password manager. → *Expect:* you know where to go if the device is lost.

## Decision points

- Device is shared with a child or family member -> use family location sharing only with consent and appropriate parental controls.
- Work-managed device -> organization policy may already control location, lock, and wipe options.
- Location cannot be enabled -> prioritize screen lock, backup, and account recovery because live location may not work.

## Failure modes & recovery

- **F1 Device does not appear in portal:** recovery site shows no device -> confirm the signed-in account, internet connection, and find-my-device toggle.
- **F2 Location is stale:** portal shows an old location -> charge and connect the device, enable location, and wait for a fresh check-in.
- **F3 Screen lock is weak:** device accepts a short or reused PIN -> change it to a longer passcode or password.
- **F4 Account recovery is unavailable:** you cannot sign in from another device -> update recovery phone, email, and backup codes now.

## Verification

From a separate browser or device, the official recovery portal lists the device, shows find-my-device enabled, and offers locate, lock, or erase actions.

## Variations

- iOS and macOS: use Find My and enable Find My network where available.
- Android: use Google's Find My Device; some manufacturers also offer their own recovery service.
- Windows: use Settings > Privacy & security > Find my device with a Microsoft account.

## Safety & privacy

Medium risk because location data is sensitive and recovery actions can expose or lock devices. Use only official portals, protect the account with strong authentication, and do not share location access casually.
