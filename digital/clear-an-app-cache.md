---
name: clear-an-app-cache
domain: digital
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

You clear temporary app cache to fix slowness or storage pressure without confusing it with clearing app data, which can remove sign-in and local settings.

## Preconditions

- The app is installed on your phone or tablet.
- You can open device settings.
- You know your login credentials if troubleshooting may require clearing data later.

## Steps

1. **Identify the symptom.** Confirm whether the problem is storage use, slow loading, stale images, or app glitches. → *Expect:* there is a specific reason to clear cache.
2. **Open app storage settings.** Go to Settings > Apps, choose the app, then open Storage or Storage and cache. → *Expect:* cache and data sizes are visible if the platform exposes them.
3. **Read the labels carefully.** Cache is temporary files; data is account state, downloads, settings, and local app content. → *Expect:* you can tell which button clears cache only.
4. **Clear cache only.** Tap Clear cache if available. → *Expect:* cache size drops, while the app remains installed and signed in.
5. **Reopen the app.** Launch the app and repeat the action that was slow or broken. → *Expect:* the app rebuilds temporary files and may load slightly slower the first time.
6. **Avoid clearing data unless needed.** [BRANCH: cache fixed it | cache did not fix it] stop if the app works, or consider Clear data only after confirming credentials and local downloads. → *Expect:* you do not erase account state by accident.
7. **Use in-app cache tools if present.** For browsers, maps, music, and social apps, check their own storage or offline-download settings. → *Expect:* large cached or offline items can be managed more precisely.
8. **Repeat only when useful.** Do not clear cache daily; use it when storage is tight or stale temporary files cause problems. → *Expect:* cache returns over time as the app runs normally.

## Decision points

- The app stores offline maps, music, or videos → remove those from the app's download settings before clearing data.
- The phone is almost full → clear cache across the biggest apps, then remove unused apps or media.
- A support article says clear data → confirm you can sign back in and that local-only content is backed up.

## Failure modes & recovery

- **F1 Clear cache button missing:** detect when the option is unavailable, recover by using the app's internal storage controls or reinstalling only if account data is backed up.
- **F2 App logs out:** detect a sign-in screen after clearing data instead of cache, recover by signing in again and restoring synced settings where possible.
- **F3 Downloads disappear:** detect missing offline files, recover by redownloading them from the app if they are still available.
- **F4 Problem returns quickly:** detect cache growing or stale data reappearing, recover by updating the app or checking network and account sync.

## Verification

The app's cache size is reduced, the app opens, and your account data remains intact unless you deliberately chose Clear data.

## Variations

- `android`: many devices expose Clear cache per app; Clear storage or Clear data is the higher-risk option.
- `iphone`: iOS often lacks a system Clear cache button, so use in-app settings, offload the app, or reinstall after confirming account sync.
- `browser`: clearing browser cache can log sites out if cookies or site data are selected too.

## Safety & privacy

Cache is usually safe to clear, but app data is not the same thing. ⚠️ *Irreversible:* clearing data can remove local files, settings, drafts, and sign-in state if they are not synced elsewhere.
