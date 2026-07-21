---
name: update-software-safely
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 30min
risk: medium
prerequisites: [digital/back-up-your-files]
status: draft
last_verified: 2026-07-20
---

## Goal

Your OS and applications are updated — closing the security holes updates exist for — at a moment you chose, through legitimate channels, with a fallback if an update misbehaves.

## Preconditions

- A pending update (OS notification, app store badge, in-app prompt) or a periodic check habit firing.
- Battery above ~50% or plugged in; enough free disk (OS updates state their need); a recent backup for OS-level updates (`digital/back-up-your-files`).
- Twenty unhurried minutes — the "remind me later" spiral is mostly about bad timing, so pick a real slot.

## Steps

1. **Verify the update's channel before anything else.** Legitimate: the OS's own settings/updater, the platform app store, the app's built-in updater. Illegitimate: a *website popup* saying your player/browser is outdated — that's a malware genre, close it. → *Expect:* the update lives inside a channel you deliberately opened.
2. **Read what it is.** Security patches: apply promptly, always. Feature/major-version upgrades (the .0 releases): fine to wait days-to-weeks while early adopters find the bugs — your call, made consciously. → *Expect:* you know whether this is "patch now" or "major, scheduled for the weekend".
3. **Prepare the ground for OS updates.** Backup current (step 0 of every OS update), work saved and apps closed, charger in, and don't start it 20 minutes before a meeting. App updates need none of this ceremony. → *Expect:* nothing running that losing would hurt; power secured.
4. **Run the update and leave it alone.** Let it download, install, reboot as many times as it wants. ⚠️ *Irreversible:* interrupting an OS/firmware update mid-write (forcing power-off at the "do not turn off" screen) can brick devices — the one absolute rule is *wait it out*, even when the progress bar seems dead (they routinely stall-then-jump). → *Expect:* the do-not-power-off phases pass; the system returns to a login screen.
5. **Verify the version and the vitals.** Settings shows the new version; then a 2-minute smoke test of what you depend on: the apps you use daily open, peripherals (printer, audio) work, files present. → *Expect:* new version confirmed; daily-driver functionality intact.
6. **Sweep the stragglers.** App store "update all" for the long tail; browsers self-update on restart (so restart the browser you never close); firmware-bearing devices (router, watch) on their own cadence. → *Expect:* no red badges left; the machine's software surface is current.

## Decision points

- Auto-update settings → turn them ON for security patches and app-store apps (the default posture that protects the inattentive), OFF only for the specific tool whose version you must pin (with a calendar note to revisit).
- Software pinned by compatibility (a plugin needs app vX) → that's a real reason to defer — written down, revisited monthly — not a permanent exemption drifting into vulnerability.
- End-of-life OS (no more updates offered) → the update path is a migration/new-device conversation; an unpatched internet-connected machine is the actual risk, not the hassle of change.

## Failure modes & recovery

- **F1 Update fails/rolls back with an error:** note the error code, free disk space (the #1 cause), retry once; persistent → the vendor's update-troubleshoot page for that code — generic flailing loses to the specific fix.
- **F2 Something broke after updating (app won't open, driver weirdness):** reboot once more first (settles most), then check the app for its own compatibility update; last resort is the OS's rollback/restore window — which exists and is why the backup was step 3.
- **F3 Stuck progress bar anxiety:** OS updates can sit at a percentage for 20+ minutes legitimately — the wait-it-out rule; only a multi-*hour* freeze with no disk activity justifies vendor-documented recovery steps.
- **F4 Storage too full to update:** clear the obvious (downloads, trash, old videos) or offload to the backup drive — chronic fullness blocks security patches, making it a security problem, not a tidiness one.

## Verification

Version numbers show current across OS and daily apps, the smoke test passed, auto-update posture is set deliberately, any pinned exception is documented with a revisit date, and the backup that preceded the OS update is intact for the rollback window.

## Variations

- Phones: same recipe, lower stakes ceremony — overnight auto-update with charging solves it structurally.
- Managed work machines: IT owns the schedule; your job reduces to *not* deferring their prompts into the enforcement deadline.

## Safety & privacy

Medium risk in two directions that trade off: unpatched software is the internet's most-exploited surface (so update), and interrupted firmware writes brick hardware (so never interrupt). Channel legitimacy (step 1) guards the third rail — fake updaters as malware delivery.
