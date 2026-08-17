---
name: mute-a-browser-tab
domain: digital
locale: [generic]
interface: web
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Silence sound from one browser tab without muting the whole computer.

## Preconditions

- A browser tab is playing or may play audio.
- The tab is visible in the tab bar.

## Steps

1. **Find the noisy tab.** Look for a speaker icon or audio indicator on the tab. → *Expect:* the tab producing sound is identifiable.
2. **Open the tab menu.** Right-click the tab, or `Control`-click it on Mac. → *Expect:* a context menu appears for that tab.
3. **Mute the tab or site.** Choose `Mute Tab`, `Mute Site`, or `Mute Tab Audio`. → *Expect:* the speaker icon changes to a muted indicator and audio stops.
4. **Unmute when needed.** Reopen the tab menu and choose the unmute option. → *Expect:* audio from that tab or site can play again.

## Decision points

- The browser offers `Mute Site` instead of `Mute Tab` → all tabs from that site may be silenced.
- You are in a meeting → confirm the correct tab is muted before sharing audio.
- Multiple tabs play sound → repeat the action on each tab or close unwanted tabs.

## Failure modes & recovery

- **F1 Wrong tab muted:** detect the sound continues or another tab shows muted → unmute the wrong tab and mute the tab with the speaker icon.
- **F2 Site remains muted later:** detect videos on that site have no sound → right-click a tab from the site and choose `Unmute Site`.
- **F3 No mute option:** detect the menu has no audio control → pause the media player, lower site volume, or use system volume.

## Verification

The tab or site shows a muted indicator and no sound plays from it while other computer audio can still play.

## Variations

- Chrome: right-click the tab and choose `Mute Site`.
- Firefox: click the speaker icon on the tab or choose `Mute Tab`.
- Safari: click the speaker icon in the Smart Search field or on the tab.

## Safety & privacy

Muting does not stop video playback, recording, tracking, or live-stream participation. Stop or leave sensitive media sessions when privacy matters.
