---
name: back-up-your-messaging-app
domain: digital
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Your messaging app has a current cloud backup, the backup frequency is deliberate, media handling is understood, and you know how restore would work.

## Preconditions

- Your phone is signed in to the cloud account used for backups.
- The messaging app is installed and verified with your phone number or account.
- Wi-Fi and charging are available for large backups.

## Steps

1. **Open the app's backup settings.** Look under Settings > Chats, Account, Storage, or Backup depending on the app. → *Expect:* you see backup status or a backup option.
2. **Choose the cloud destination.** Confirm the backup account, such as iCloud, Google Drive, or the app's own cloud. → *Expect:* the destination account is correct.
3. **Set backup frequency.** [BRANCH: daily | weekly | manual] choose daily for active important chats, weekly for casual use, or manual if storage is tight. → *Expect:* the schedule matches the importance of the messages.
4. **Decide whether media is included.** Check whether photos, videos, voice notes, and documents are included or excluded. → *Expect:* you know what will restore later.
5. **Enable encryption if offered.** Save the password or recovery key somewhere secure before turning on encrypted backup. → *Expect:* the app confirms encrypted backup or shows the key setup complete.
6. **Run a backup now.** Start a manual backup while on Wi-Fi and keep the app open if it asks. → *Expect:* progress completes and shows today's date.
7. **Verify cloud storage.** Check that the cloud account has enough remaining storage for future backups. → *Expect:* no storage warning appears.
8. **Review restore requirements.** Note that restore usually requires the same phone number, account, and encryption password if enabled. → *Expect:* you know what credentials are needed before replacing a phone.

## Decision points

- Media makes the backup too large → exclude videos first, then save important media separately.
- You may change phone platforms → confirm whether the app supports transfer between iPhone and Android before relying on cloud backup alone.
- The chat history is sensitive → use end-to-end encrypted backup where available and keep the recovery key offline.

## Failure modes & recovery

- **F1 Backup fails for storage:** detect a not enough space error, recover by freeing cloud storage or excluding large videos.
- **F2 Backup stuck on waiting:** detect no progress for several minutes, recover by connecting to Wi-Fi, charging the phone, and reopening the app.
- **F3 Wrong account selected:** detect backup under an old cloud account, recover by switching to the account you will use on the new phone.
- **F4 Encryption key lost:** detect when restore asks for a password or key you do not have, recover only by using another available backup or accepting that encrypted history may not restore.

## Verification

The app's backup screen shows a successful backup dated today, with the expected cloud account, frequency, and media setting.

## Variations

- `whatsapp`: backups are usually under Settings > Chats > Chat backup and may use iCloud or Google Drive.
- `signal`: common backups are local or device-transfer based, depending on platform, so confirm the current app behavior.
- `telegram`: most cloud chats sync automatically, but secret chats and downloaded media may not behave the same way.

## Safety & privacy

Message backups can contain private conversations, photos, identity documents, and locations. Protect the cloud account, use encrypted backup when practical, and keep recovery credentials somewhere you can access during a phone replacement.
