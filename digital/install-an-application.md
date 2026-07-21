---
name: install-an-application
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 15min
risk: medium
prerequisites: [have-admin-access]
status: draft
last_verified: 2026-07-20
---

## Goal

A named application is installed from a trustworthy source and launches successfully on your device.

## Preconditions

- You know the application's exact name and publisher.
- Sufficient disk space and a compatible OS version.
- Permission to install software on this device (admin rights, or an org that allows it).

## Steps

1. **Identify the official source.** [BRANCH: OS app store | vendor website | package manager] Prefer the platform store or package manager; for direct downloads, navigate to the vendor's site yourself rather than clicking ads or search-ad results. → *Expect:* publisher name on the store page / site domain matches the real vendor.
2. **Check compatibility and cost.** OS version, architecture, disk space, license (free / trial / subscription). → *Expect:* your device meets stated requirements; the price is what you expect.
3. **Download or begin install.** Store: click Install/Get. Website: download the installer for your OS. Package manager: run the install command. → *Expect:* download completes from the expected domain; file size roughly matches the site's stated size.
4. **Run the installer.** Approve the OS's confirmation prompt only if the publisher shown matches step 1. ⚠️ *Irreversible:* granting an installer admin rights executes arbitrary code — abort if the publisher name is unexpected or unsigned. → *Expect:* an install wizard or progress bar; decline any bundled "offers"/toolbars.
5. **Complete setup choices.** Default install location is usually right; uncheck auto-start unless wanted. → *Expect:* "installation complete."
6. **Launch the application.** → *Expect:* the app opens to its first-run screen without errors.
7. **Clean up.** Delete the downloaded installer file. → *Expect:* installer removed; app still launches from the applications menu.

## Decision points

- OS blocks the app as unidentified → verify you downloaded from the vendor; if certain, use the OS's explicit override; if any doubt, stop and re-download from the official source.
- App needs a newer OS → decide between updating the OS or finding the last compatible version *from the vendor's own archive*.
- Org-managed device refuses installation → request via the IT self-service portal instead.

## Failure modes & recovery

- **F1 Installer fails midway:** free disk space, disable antivirus temporarily only if the source is verified, retry; check the vendor's known-issues page.
- **F2 App crashes at launch:** restart the device once; then reinstall; then check version compatibility.
- **F3 Wrong/bundled software appeared:** you likely used a repackaged download portal — uninstall everything it added, then reinstall from the official source.

## Verification

The application launches from the system's normal launcher (not the installer), shows the expected version in its About screen, and the installer artifact is deleted.

## Variations

- `mobile-app`: store-only; the ⚠️ step becomes reviewing the permission list at first run.
- Linux: prefer the distro package or official repo (`apt`, `dnf`, flatpak) over downloaded binaries.

## Safety & privacy

Medium risk: installation is code execution. The publisher-verification checks in steps 1 and 4 are the security boundary — fake download sites for popular apps are a top malware vector.
