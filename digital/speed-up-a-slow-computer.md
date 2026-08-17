---
name: speed-up-a-slow-computer
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 45min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Improve everyday computer responsiveness by identifying the main bottleneck, reducing startup load, freeing storage, and applying safe updates.

## Preconditions

- You can sign in with an administrator account if prompted.
- Important files are backed up before removing apps or changing startup behavior.
- The computer is connected to power and the internet.

## Steps

1. **Restart once.** Save work, restart the computer, and wait five minutes after signing in. → *Expect:* temporary update or memory issues are cleared before diagnosis.
2. **Check storage space.** [BRANCH: Windows | Mac] open Settings > System > Storage on Windows or System Settings > General > Storage on Mac. → *Expect:* the system shows available space and large categories.
3. **Free obvious storage.** Empty Trash or Recycle Bin, remove downloaded installers, and uninstall apps you recognize and no longer use. → *Expect:* at least 10-20% of the drive is free or the largest clutter category is reduced.
4. **Find heavy processes.** Open Task Manager on Windows or Activity Monitor on Mac and sort by CPU and Memory. → *Expect:* you can identify whether one app is consuming unusual resources.
5. **Disable unneeded startup apps.** [BRANCH: Windows | Mac] use Task Manager > Startup apps on Windows or System Settings > General > Login Items on Mac. → *Expect:* nonessential apps are disabled from launching at sign-in.
6. **Apply system and browser updates.** Run Windows Update or Software Update, then update browsers and core apps. → *Expect:* updates complete or show a clear pending restart.
7. **Scan for unwanted software.** Run Windows Security or a reputable antivirus scan, and remove suspicious browser extensions you did not install intentionally. → *Expect:* the scan completes and unknown extensions are gone.
8. **Measure again.** Restart and repeat the slow action that triggered the work. → *Expect:* startup, app launch, or browsing feels faster or the remaining bottleneck is clear.

## Decision points

- Drive is nearly full → freeing storage is the priority before tuning anything else.
- Memory pressure stays high with normal apps open → consider adding RAM or reducing concurrent apps.
- Disk usage stays at 100% on an old hard drive → replacing it with an SSD may be the meaningful fix.
- Computer is managed by work or school → do not remove security or management software.

## Failure modes & recovery

- **F1 Needed app disabled:** detect missing tray/menu-bar behavior after startup → re-enable the startup item.
- **F2 Update loop:** detect repeated failed update messages → run the OS update troubleshooter or free more storage and retry.
- **F3 Suspicious pop-ups remain:** detect browser redirects or ads after cleanup → follow malware removal steps and reset the browser profile.
- **F4 Performance unchanged:** detect no improvement after restart → check hardware health, storage type, RAM, and background sync.

## Verification

After a restart, the drive has adequate free space, unnecessary startup apps remain disabled, no obvious process is constantly maxing CPU or memory, and the original slow task completes faster or has a named bottleneck.

## Variations

- Windows: Task Manager, Settings > Apps > Installed apps, Windows Security, and Settings > System > Storage are the main tools.
- Mac: Activity Monitor, System Settings > General > Login Items, System Settings > General > Storage, and Software Update are the main tools.
- Older computers: hardware upgrades may outperform software cleanup.

## Safety & privacy

Low risk when you remove only apps you recognize. Avoid registry cleaners, driver-updater ads, and tools that request broad access without a clear vendor.
