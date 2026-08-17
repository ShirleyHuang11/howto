---
name: create-a-shared-photo-album
domain: digital
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 15min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Create a shared photo album with the right people, permissions, and privacy settings, then confirm others can view or contribute as intended.

## Preconditions

- Photos are already on your phone or cloud photo account.
- You know who should view or add photos.
- You have consent to share sensitive images of other people, especially children.

## Steps

1. **Choose the photo service.** [BRANCH: iPhone family | Android or mixed group | private link] use iCloud Shared Albums, Google Photos shared albums, or a private album link. → *Expect:* one service matches the devices in the group.
2. **Create the album.** Open Photos or Google Photos, create a new shared album, and give it a specific name. → *Expect:* an empty shared album appears in the app.
3. **Add initial photos.** Select only photos meant for this audience and avoid accidental screenshots or private images. → *Expect:* the album contains the intended starter set.
4. **Invite people directly.** Add recipients by verified Apple ID, Google account, phone number, or email rather than posting a public link. → *Expect:* the invite list contains only intended people.
5. **Set contribution permissions.** Decide whether invitees can add photos, comment, like, download, or invite others. → *Expect:* permissions match the album's purpose.
6. **Check link sharing.** Turn off public link sharing unless the album is meant to be broadly accessible. → *Expect:* access requires the chosen invitations or a deliberate private link.
7. **Verify from another account.** Ask one recipient to open the album and, if allowed, add a test photo or comment. → *Expect:* recipient access works exactly as intended.

## Decision points

- Child photos or school events → keep link sharing off and invite only known people.
- Event album needs contributions → allow adding photos but review who can invite others.
- Mixed iPhone/Android group → Google Photos is usually simpler than iCloud-only sharing.
- High-resolution originals matter → verify whether the service shares full quality or compressed copies.

## Failure modes & recovery

- **F1 Invite not received:** detect recipient cannot find it → verify account address and resend from the album sharing settings.
- **F2 Album became public:** detect link sharing enabled unexpectedly → disable link sharing and remove unknown viewers.
- **F3 Wrong photo added:** detect private photo in album → remove it from the shared album and confirm whether viewers already downloaded it.
- **F4 Contributors cannot upload:** detect add button missing → enable collaboration or use a service that supports contributions.

## Verification

The shared album opens for an intended recipient, permissions allow only the intended actions, link sharing is off or deliberate, and the album contains only approved photos.

## Variations

- iCloud Shared Albums: good for Apple groups, but quality and platform access can differ from normal iCloud Photos.
- Google Photos: works well across iOS, Android, and web.
- Messaging apps: useful for quick sharing but weaker for long-term organization and permissions.

## Safety & privacy

Medium risk because shared albums can reveal faces, children, homes, locations, and routines. Review photos and metadata before sharing and restrict invites.
