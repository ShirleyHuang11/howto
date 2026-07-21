---
name: connect-to-wifi
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-20
---

## Goal

Your device is connected to the intended Wi-Fi network — home, work, or public — with working internet and sane security posture for the network's trust level.

## Preconditions

- A device with Wi-Fi and the network's real name (SSID) known; for secured networks, the password (router sticker, host, or venue signage/receipt).

## Steps

1. **Open Wi-Fi settings and identify the *exact* network name.** Venues post theirs; homes have it on the router sticker. Twin-named networks ("CafeFreeWiFi" vs "Cafe_Free_WiFi") are how evil-twin attacks work — the posted name, character for character, is the one. → *Expect:* the intended SSID visible in the list with plausible signal strength.
2. **Select it and authenticate.** [BRANCH: password network → enter the key exactly (case matters) | open venue network → connect, then expect a captive portal | enterprise (work/university) → username + password, accept the org's certificate only if it matches expectations] → *Expect:* status moves to "connected"; wrong-password errors mean the key, not the world, is at fault.
3. **Clear the captive portal if one appears.** Open a browser if it doesn't auto-pop (try any http site); accept terms / enter the room number or voucher. Give marketing fields the minimum. → *Expect:* the portal releases you; general sites load.
4. **Verify actual internet.** Load a known site or run the OS's connectivity check. Connected-but-no-internet → F2. → *Expect:* pages load at usable speed.
5. **Set the trust posture to match the network.** Public/venue: mark it "public" when the OS asks (disables file sharing), avoid logging into sensitive accounts without HTTPS (the padlock), and prefer your phone's hotspot for banking-class tasks. Home: fine. → *Expect:* sharing off on public networks; sensitive tasks deferred or tunneled.
6. **Manage the remembering.** Home/work: let it auto-join. One-time public networks: forget them after use — auto-rejoining "Airport_Free" forever is a tracking and evil-twin surface. → *Expect:* the saved-networks list holds only networks you actually trust.

## Decision points

- No password anywhere at a venue → ask staff; if a "free" unlisted network appears with the venue's name anyway, that's exactly the twin to refuse.
- Weak signal at the desk → closer to the access point beats every software remedy; 5 GHz nearer, 2.4 GHz farther/through-walls, where the choice exists.
- Hosting a guest at home → the router's guest network exists for this: internet-yes, your-devices-no; share that instead of the main key.

## Failure modes & recovery

- **F1 Wrong password loops:** retype slowly (visibility toggle on), confirm you're on the right SSID (twin check), and on a home router re-read the sticker — key vs. admin password confusion is the classic.
- **F2 Connected, no internet:** forget-and-rejoin the network first; then the router power-cycle (home); on venue networks the portal may have expired — reopen it via a fresh http page.
- **F3 Captive portal never loads:** manually browse to any plain http URL (portals can't intercept some https), toggle airplane mode once, or try the OS's "sign in to network" notification.
- **F4 Everything slow at a busy venue:** it's shared air, not your device — offload heavy tasks to later or the hotspot; complaining to the barista is not a network intervention.

## Verification

The device shows the intended SSID connected, real pages load, sharing is off if the network is public, and the saved list contains no one-time networks set to auto-join.

## Variations

- Hotel networks: room number + surname portals; per-device limits mean the laptop may cost the tablet its slot — some hotels have a device-management page for this.
- QR-share (`cn` ubiquitous, spreading everywhere): scanning the host's QR replaces steps 1–2 entirely and dodges typo failure.

## Safety & privacy

Medium risk on public networks: the SSID-twin check, HTTPS-only for anything that matters, sharing off, and forget-after-use are the four habits. The home router's admin password (different from the Wi-Fi key) deserves changing from its default once, ever — that's a different recipe.
