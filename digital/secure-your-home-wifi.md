---
name: secure-your-home-wifi
domain: digital
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Home Wi-Fi is protected with a strong router admin password, modern encryption, a strong network passphrase, guest isolation, and firmware updates.

## Preconditions

- You can access the router app or admin page.
- You know the current Wi-Fi network name and password.
- You can reconnect devices if the network name or password changes.

## Steps

1. **Find the router admin route.** Use the router maker's app or type the gateway address from your network settings. → *Expect:* you reach the router login screen, not a search-result support page.
2. **Log in and change the admin password.** Replace default or reused admin credentials with a unique password stored in your password manager. → *Expect:* the router accepts the new admin password and requires it for future changes.
3. **Update router firmware.** Check for Firmware, Software update, or Router update and install available updates. → *Expect:* the router restarts and reports current firmware.
4. **Set Wi-Fi encryption to WPA3 or WPA2.** [BRANCH: WPA3 available | WPA2 only] Use WPA3-Personal if all devices support it, or WPA2/WPA3 mixed mode when needed. → *Expect:* security mode is not WEP, WPA, or open.
5. **Set a strong Wi-Fi passphrase.** Use a long phrase or generated password that is not reused elsewhere. → *Expect:* the network saves the new passphrase and reconnects your device after entry.
6. **Disable risky convenience features.** Turn off WPS PIN, remote admin from internet, and default open setup networks unless specifically needed. → *Expect:* outside devices cannot administer the router or join by PIN.
7. **Create a guest network.** Enable guest Wi-Fi with a separate passphrase and client isolation if available. → *Expect:* guests can reach the internet but not your private devices.
8. **Check connected devices.** Review the device list and rename known devices for easier future checks. → *Expect:* unknown devices are removed or blocked after you change the Wi-Fi passphrase.
9. **Save recovery details.** Store admin login, Wi-Fi passphrase, router model, and ISP support details privately. → *Expect:* you can recover settings without using factory defaults.

## Decision points

- [BRANCH: ISP router | owned router] ISP routers may use an app and limited options; owned routers usually expose more security settings.
- Old device cannot connect after WPA3 → use WPA2/WPA3 mixed mode or place the old device on guest/IoT Wi-Fi if supported.
- Router no longer receives firmware updates → plan replacement, especially for routers older than about five years.
- Smart home devices need access → segregate them on guest or IoT networks when router supports it.

## Failure modes & recovery

- **F1 Locked out of router admin:** detect password rejected; recover with stored password or physical reset only if you can reconfigure internet settings.
- **F2 Devices stop connecting:** detect repeated password errors; recover by forgetting the network on the device and rejoining with the new passphrase.
- **F3 Firmware update fails:** detect router offline or stuck; recover by waiting several minutes, power cycling once, then using vendor recovery instructions.
- **F4 Unknown devices remain:** detect unfamiliar names after password change; recover by changing the passphrase again and checking for shared passwords or compromised devices.

## Verification

The router shows a unique admin password, WPA3 or WPA2 encryption, WPS/remote admin disabled unless intentionally needed, current firmware, and a separate guest network.

## Variations

- `mobile-app`: mesh systems often use app labels like Network, Advanced settings, Privacy, or Guest access.
- Apartment or shared housing: coordinate password changes so residents are not locked out unexpectedly.
- Small business/home office: create separate networks for work devices, guests, and smart devices if the router supports VLAN or IoT network options.

## Safety & privacy

Medium risk because weak Wi-Fi exposes local devices and internet use. Store router credentials privately, avoid printing the private Wi-Fi password for guests, and update firmware when security fixes appear.
