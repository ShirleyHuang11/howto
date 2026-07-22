---
name: change-your-wifi-password
domain: digital
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 15min-45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Your router broadcasts the same Wi-Fi network with a new strong password, and trusted devices are reconnected.

## Preconditions

- Router admin access through the router app or web admin page.
- The current Wi-Fi name, router admin password, and physical access to the router if you get disconnected.

## Steps

1. **Connect locally.** Join the current Wi-Fi or plug a computer into the router with Ethernet. → *Expect:* the device can reach the router or internet.
2. **Find the router admin address.** Check the router label, app, gateway address, or common addresses such as `192.168.1.1` or `192.168.0.1`. → *Expect:* a router login page or app dashboard opens.
3. **Log in as admin.** Use the router admin password, not the Wi-Fi password unless the label says they are the same. → *Expect:* wireless or network settings are available.
4. **Open wireless settings.** Find Wi-Fi, Wireless, SSID, or WLAN settings for the main network. → *Expect:* the current network name and password field are visible.
5. **Set a strong Wi-Fi password.** Use WPA2-Personal or WPA3-Personal if available and a unique password of at least 14 characters. → *Expect:* the new password is accepted by the router UI.
6. **Save changes.** Apply or save, then wait for the Wi-Fi radios to restart. → *Expect:* connected Wi-Fi devices drop offline briefly.
7. **Reconnect your main device.** [BRANCH: same SSID | new SSID] Same SSID: forget the old saved password if prompted. New SSID: select the new network name. → *Expect:* the device reconnects with internet access.
8. **Reconnect household devices.** Update phones, laptops, TVs, printers, cameras, smart plugs, and guest devices as needed. → *Expect:* each trusted device returns online.
9. **Store the password securely.** Save it in a password manager or a private household record. → *Expect:* authorized people can retrieve it later without reading the router label aloud.

## Decision points

- You suspect someone has the old password → change the password and review connected devices afterward.
- Router offers WPA3 transition mode → use it if older devices still connect; otherwise WPA2-Personal is broadly compatible.
- Smart home devices are numerous → consider changing only the password, not the SSID, to reduce setup work.

## Failure modes & recovery

- **F1 Admin login fails:** detect rejected admin credentials, recover by checking the router label, ISP app, or documented reset process.
- **F2 Device will not reconnect:** detect wrong-password loops, recover by forgetting the network and entering the new password carefully.
- **F3 Old devices fail:** detect devices that cannot join WPA3, recover by enabling WPA2/WPA3 transition mode.
- **F4 Lost router access:** detect no Wi-Fi and no admin page, recover by connecting with Ethernet or using the router app on cellular if supported.

## Verification

A device connects to the Wi-Fi using the new password, reaches the internet, and the old password no longer works.

## Variations

- ISP gateways: use the ISP app or printed gateway URL, since some settings are hidden from the local web page.
- Mesh systems: change the password in the mesh app, which pushes it to all nodes.
- Guest networks: update guest Wi-Fi separately from the main network.

## Safety & privacy

Changing the Wi-Fi password disconnects every saved device and may interrupt cameras, alarms, printers, and work calls. Do not share the new password in public chats, and keep the router admin password separate from the Wi-Fi password.
