---
name: set-up-a-guest-wifi-network
domain: digital
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 25min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

A separate guest Wi-Fi network is enabled so visitors can use the internet without reaching private computers, phones, storage devices, or smart-home controls.

## Preconditions

- You can access the router app or admin page.
- Your router supports guest network, guest access, or IoT network features.
- You know the private Wi-Fi network name and do not want to share its password.

## Steps

1. **Open router settings.** Use the router maker's app or admin address while connected to your home network. → *Expect:* you can see Wi-Fi or network settings.
2. **Find guest network controls.** Look for Guest Wi-Fi, Guest access, Visitor network, IoT network, or Additional SSID. → *Expect:* a separate network can be enabled.
3. **Enable the guest network.** Turn on the guest SSID for 2.4 GHz, 5 GHz, or both as the router permits. → *Expect:* a new network name appears in the router settings.
4. **Name it clearly.** Use a name that guests can recognize but that does not reveal sensitive details like apartment number or full name. → *Expect:* the guest network is easy to distinguish from the private network.
5. **Set a separate password.** Use a strong passphrase that is different from the private Wi-Fi password. → *Expect:* guests can be given access without exposing the main network password.
6. **Turn on isolation.** Enable settings like guest isolation, block local network access, internet only, or prevent access to LAN. → *Expect:* guests can reach the internet but not private devices.
7. **Separate smart devices if useful.** [BRANCH: guest-only visitors | IoT segregation] Put untrusted smart plugs, cameras, or toys on an IoT/guest network if they do not need local access. → *Expect:* risky devices are separated from laptops and phones.
8. **Test from a phone.** Join the guest network and browse the web, then try to reach a printer, file share, router admin page, or smart hub. → *Expect:* internet works and private resources are blocked.
9. **Share access safely.** Give guests the guest password or QR code, and rotate it when it spreads too widely. → *Expect:* visitors connect without touching the private network.

## Decision points

- [BRANCH: temporary guest access | permanent guest network] Temporary access can expire automatically; permanent guest networks need occasional password rotation.
- Smart devices need phone control on the same network → use the router's IoT feature or accept limited local access only for those devices.
- Router lacks isolation settings → a guest network may only be a second name, so consider upgrading router or not sharing Wi-Fi.
- Work-from-home devices present → keep work computers on the private network and guests off it.

## Failure modes & recovery

- **F1 Guests cannot connect:** detect wrong password or no network listed; recover by checking SSID broadcast, band compatibility, and password spelling.
- **F2 Guests can see private devices:** detect printer, file share, or router page visible; recover by enabling isolation or disabling guest network until fixed.
- **F3 Smart devices break:** detect app cannot control device; recover by moving the controller phone temporarily or using an IoT network designed for local control.
- **F4 Password spread too widely:** detect unknown devices or overuse; recover by changing only the guest password, leaving private devices untouched.

## Verification

A test device on guest Wi-Fi can access the internet but cannot access router administration, local file shares, printers, or private smart-home controls unless explicitly allowed.

## Variations

- `mobile-app`: mesh router apps often expose guest sharing by QR code and expiration time.
- Short-term rental: rotate the guest password between stays and keep owner devices on a private network.
- Events: use a temporary guest password and turn the network off afterward.

## Safety & privacy

Low to medium risk. Guest Wi-Fi limits exposure from visitors and untrusted smart devices, but only if isolation is enabled and the private Wi-Fi password is not shared.
