---
name: set-a-pin-on-your-sim
domain: accounts
subdomain: security
locale: [generic]
interface: mobile-app
difficulty: intermediate
est_time: 15min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You enable a SIM PIN so someone who removes your SIM or restarts your phone cannot use your mobile number without the PIN.

## Preconditions

- Physical access to the phone using the SIM or eSIM.
- The carrier's default SIM PIN or current SIM PIN.
- Access to carrier support or account portal in case you need the PUK unlock code.

## Steps

1. **Find the carrier's current SIM PIN.** Check carrier documentation or your account; common defaults like `1111` or `0000` vary and should not be guessed repeatedly. → *Expect:* you have the current PIN from a reliable source.
2. **Open SIM PIN settings.** In mobile settings, search for SIM PIN, SIM lock, cellular PIN, or security. → *Expect:* the phone displays the SIM lock control.
3. **Turn on SIM PIN.** Enter the current SIM PIN when prompted. → *Expect:* the phone accepts the PIN and shows SIM PIN as enabled.
4. **Change the PIN to a private code.** Choose a PIN you can remember but others cannot guess. → *Expect:* the phone confirms the new SIM PIN.
5. **Record the PIN securely.** Save it in a password manager or secure note. → *Expect:* you can retrieve the PIN after a restart or device change.
6. **Test carefully with one restart.** Restart the phone and enter the new SIM PIN when prompted. → *Expect:* cellular service activates after the PIN is accepted.
7. **Store the PUK recovery path.** Note where to get the carrier PUK code if the SIM is locked after too many wrong attempts. → *Expect:* you know how to recover without guessing.

## Decision points

- You do not know the current PIN -> contact the carrier instead of guessing.
- Phone uses dual SIM -> set and record the PIN for each line separately.
- You frequently lend the phone unlocked -> SIM PIN helps after restart or SIM removal, not while the phone is already unlocked.

## Failure modes & recovery

- **F1 Wrong PIN attempts remain:** the phone warns about limited attempts -> stop and get the correct PIN or PUK from the carrier.
- **F2 SIM becomes PUK-locked:** cellular service is blocked -> enter the carrier-provided PUK code, then set a new SIM PIN.
- **F3 PIN forgotten after restart:** phone cannot connect to cellular -> retrieve it from your password manager or contact the carrier for PUK recovery.
- **F4 eSIM menus differ:** setting is hard to find -> search device settings for SIM PIN or check carrier-specific instructions.

## Verification

After a restart, the phone asks for the SIM PIN and cellular service returns only after the correct PIN is entered.

## Variations

- iPhone: Settings > Cellular or Mobile Service > SIM PIN.
- Android: Settings labels vary; search Settings for "SIM lock" or "SIM PIN".
- Some carriers or eSIM profiles may restrict SIM PIN changes or require carrier support.

## Safety & privacy

Medium risk because too many wrong SIM PIN attempts can lock the SIM and require a PUK code. Do not guess repeatedly, record the new PIN securely, and keep carrier account recovery current.
