---
name: help-with-a-video-call-to-family
domain: embodied
subdomain: care
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: [digital/connect-to-wifi]
status: draft
last_verified: 2026-07-20
objects: [tablet, phone, stand, charging-cable, chair, person]
affordances: [grasp, position, tap, dial-adjust, hold-steady, speak]
workspace: home-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [tablet, phone], human_proximity: continue}
---

## Goal

An older or less-technical family member is connected to a video call with relatives, sees and hears them clearly, is framed well and comfortable, and the helper steps back so the call belongs to the person, not the person handling the device.

## Preconditions

- A charged tablet or phone with the calling app installed and the account already signed in (do the sign-in beforehand, not during the call window).
- Working WiFi or strong cellular; test it first with `digital/connect-to-wifi`.
- The person seated comfortably with a stable surface or stand for the device, and good lighting available.
- The far end knows the call time and will actually pick up.

## Steps

1. **Stage the device before the scheduled time.** Charge above 50%, open the app, confirm the contact is correct. → *Expect:* app open on the contact, battery healthy, no login prompt waiting to ambush the call.
2. **Fix the lighting first.** Light should fall on the person's face, not behind them. Move a lamp to the front or turn the chair away from a bright window. → *Expect:* the face is clearly lit in the self-preview, not a dark silhouette against a glowing background.
3. **Set framing with a stand, not a hand.** Prop the device so the camera sits near eye level and the person's head and shoulders fill the frame with a little headroom. → *Expect:* in the self-view the person is centered, looking slightly up or level, both eyes visible.
4. **Set volume and confirm audio before dialing.** Raise media volume to about 70%, unmute the mic, and if the person is hard of hearing enable captions in the app settings. → *Expect:* volume near max-but-not-distorting; captions toggle on if needed; mic shows unmuted.
5. **Place the call and confirm two-way.** Tap call, wait for the far end. When they answer, ask the person to say hello and watch for a reply. [BRANCH: they hear and see each other → hand off | one side is silent or frozen → F1/F2]. → *Expect:* both parties visibly react to each other within a few seconds.
6. **Hand the call to the person and step out of frame.** Confirm they know one control: how to end the call (point to the red button once). → *Expect:* the person is talking to family, not to you; you are out of the shot.
7. **Stay reachable but silent.** Remain within earshot for a freeze or a dropped call, without hovering in frame or narrating. → *Expect:* the conversation runs on its own; you intervene only if something breaks.
8. **Exit gracefully at the end.** When they finish, help tap end if asked, put the device back on its charger, and leave it ready for next time. → *Expect:* call ended cleanly, device charging, app still signed in for the next call.

## Decision points

- Person is anxious about "breaking something" → put the device on a stand so nothing depends on their grip, and show only the one end-call control. Fewer buttons means less fear.
- Far end has poor connection (choppy) → suggest they turn off their own video to save bandwidth; audio-only still keeps the visit.
- Hard of hearing → captions plus a wired or Bluetooth speaker beats cranking a tinny built-in speaker into distortion.

## Failure modes & recovery

- **F1 One side has no audio:** check mute on both ends first (most common), then media volume, then the app's mic permission. Re-ask "can you hear me now" after each single change.
- **F2 Frozen or black video:** it is almost always the network. Wait 10 seconds, then hang up and redial; move closer to the router if it repeats.
- **F3 Call won't connect at all:** confirm WiFi is actually joined (not just "remembered"), then that the far end is online. A test call to your own second device isolates whether the problem is local.
- **F4 Person accidentally hangs up:** stay calm, just redial. Reassure them that ending a call breaks nothing.

## Verification

The family member sees and hears their relatives, is well framed and comfortable, the helper is out of frame, and at the end the call is ended cleanly with the device back on its charger and still signed in.

## Variations

- `smart-display`: a dedicated device (smart display or TV camera) with a standing "answer" contact removes most steps; you set it up once and the person just says answer.
- Group calls: pin the active speaker or switch to gallery view so the person can follow who is talking.

## Safety & privacy

Low physical risk. The real care is dignity: set things up so the person runs their own call. Privacy note: the camera shows the room, so glance at what is in frame (mail, medications, mess) before the call and tidy or reposition if the person would prefer.
