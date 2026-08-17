---
name: howto-digital-security-basics
description: Lock down your online life in an afternoon. Verified howto recipes for: Digital Security Basics.
---

# Digital Security Basics — howto skill

Lock down your online life in an afternoon.

When the user needs any task below, follow its verified steps in order. Each step's **Expect** is the observation that confirms it worked; steps marked ⚠ are irreversible — confirm before doing them. For the full recipe (decision points, failure recovery, variations) use the howto MCP `get_howto(<id>)` or read the linked source.

## create a strong password  
`digital/create-a-strong-password`

**Goal:** Create a password that is long, unique to one account, and practical to store without reuse.

1. **Confirm the account page.** Check the URL and start from a bookmark or official app if possible.  → *Expect:* the password is being entered on the real service.
2. **Choose a storage handoff.** [BRANCH: password manager | browser password manager | written temporary note] decide where the password will live before generating it.  → *Expect:* there is a place to save the password immediately.
3. **Favor length over complexity tricks.** Use a random manager password or a passphrase of at least four unrelated words if you must type it manually.  → *Expect:* the password is long enough to resist guessing without being impossible to enter.
4. **Make it unique.** Do not reuse a password pattern from email, banking, work, school, or shopping accounts.  → *Expect:* this exact password belongs to one account only.
5. **Avoid personal clues.** Do not use birthdays, pet names, teams, addresses, lyrics, quotes, or keyboard paths.  → *Expect:* someone who knows you could not guess the password.
6. **Save before submitting if allowed.** Store the password in the manager entry with the correct site name and username.  → *Expect:* the manager can fill or reveal it before you lose the form.
7. **Submit and update the saved entry.** If the site forces symbols or length changes, update the manager entry to the exact accepted password.  → *Expect:* the account accepts the password and the saved copy matches.
8. **Add account recovery protection.** Turn on multi-factor authentication where available and update recovery email or phone.  → *Expect:* a stolen password alone is not enough to sign in.
9. ⚠ **Remove temporary copies.** ⚠️ *Irreversible:* deleting the only copy can lock you out, so verify the saved entry first.  → *Expect:* sticky notes, screenshots, and clipboard copies are gone after the manager entry works.

**Done when:** You can sign out and sign back in using the saved password, and that password is not used on any other account.

## enable two factor authentication  
`accounts/enable-two-factor-authentication`

**Goal:** The account requires a second factor at login, and you hold working recovery codes stored safely.

1. **Open the account's security settings.** Usually Account → Settings → Security → "Two-factor authentication" / "2-step verification".  → *Expect:* a 2FA section showing status "off".
2. **Choose the factor type.** [BRANCH: authenticator app (recommended) | hardware key (strongest) | SMS (weakest — SIM-swap risk)]  → *Expect:* the setup flow for the chosen factor starts; the site may re-ask your password.
3. **For an authenticator app: scan the QR code.** Open the app → add account → scan.  → *Expect:* the app shows a 6-digit code for this service, refreshing every 30 s.
4. **Enter the current code to confirm pairing.**  → *Expect:* the site accepts it and 2FA flips to "on".
5. ⚠ **Save the recovery codes — do not skip.** Copy every code into the password manager entry (or print). ⚠️ *Irreversible:* losing both your factor and these codes can permanently lock the account; this step is the insurance.  → *Expect:* codes stored and readable outside this device.
6. **Test the full loop.** Log out, log in, complete the 2FA challenge.  → *Expect:* login succeeds through the new challenge.
7. **Review trusted devices and fallback factors.** Remove stale devices; delete the SMS fallback if you chose app/key and the service allows it.  → *Expect:* only intended devices and factors remain listed.

**Done when:** A fresh logout/login requires and accepts the second factor, and the recovery codes exist in storage independent of the enrolled device.

## set up a password manager  
`accounts/set-up-a-password-manager`

**Goal:** A password manager installed, protected by one strong memorized passphrase, seeded with your important accounts, and wired into your browsers and phone — retiring the reused-password habit that underlies most personal account takeovers.

1. **Create the vault with a master passphrase you can actually memorize.** Four to five random common words (the dice-and-wordlist method or your manager's generator), typed a few times until fluent. This is now one of the two secrets you memorize forever (the other unlocks your phone); it is never reused anywhere else.  → *Expect:* a passphrase you can type from memory, unlike anything you've used before.
2. **Immediately store the emergency kit.** The manager's recovery/secret key and recovery codes printed or written, stored where you keep passports (`accounts/enable-two-factor-authentication` step 5's insurance logic: losing both the passphrase and this kit can mean losing the vault, which is the design).  → *Expect:* a physical recovery artifact in a safe place, tested readable.
3. **Protect the vault account itself with 2FA.** The manager's own account gets your strongest second factor.  → *Expect:* the vault behind passphrase + factor; the keys to the kingdom guarded like it.
4. **Install everywhere you type passwords.** Browser extension(s), phone app, and enable it as the phone's autofill provider (settings → passwords/autofill); disable the old browser's built-in saving to end the two-systems confusion.  → *Expect:* one autofill system answering everywhere; test on any login (`accounts/log-in` step 3's autofill-as-phishing-detector now works for you).
5. **Seed tier-1 accounts tonight, by logging in and updating.** Email first (the master key: `accounts/review-account-security` step 1's ordering), then banking, then the manager's list of your most-used: for each, log in, generate a new unique password in the manager, save. Eight to twelve accounts is a complete first night.  → *Expect:* tier-1 all on generated-unique passwords stored in the vault.
6. **Migrate the long tail opportunistically, and let the audit nag.** Every login over the coming weeks: save-on-use, upgrade-on-touch; run the manager's built-in audit (reused/breached/weak lists) monthly until it quiets (`accounts/review-account-security` step 6 now automated).  → *Expect:* the vault growing to match your real account surface; the audit's red numbers shrinking weekly.

**Done when:** The master passphrase types from memory, the emergency kit physically exists, the vault has 2FA, one autofill system answers on desktop and phone, tier-1 runs on unique generated passwords, and the monthly audit trend points at zero reused.

## set up passkeys  
`accounts/set-up-passkeys`

**Goal:** Add a passkey to an account so you can sign in with a device unlock method instead of typing a reusable password code.

1. **Open the official account settings.** Sign in through the service's official website or app and go to security, sign-in, or passkeys.  → *Expect:* a page lists current sign-in methods.
2. **Check the existing fallback.** Confirm a recovery email, recovery phone, authenticator app, or recovery codes are already usable.  → *Expect:* at least one fallback method is active before you add the passkey.
3. **Choose passkey enrollment.** Select add passkey, create passkey, or security key.  → *Expect:* the browser or app opens a system prompt for where to save the passkey.
4. **Pick the storage location.** [BRANCH: synced passkey | device-bound passkey | hardware security key] choose the option that matches your backup plan.  → *Expect:* the prompt names the platform, password manager, device, or security key that will hold the passkey.
5. **Approve with device unlock.** Use face unlock, fingerprint, PIN, password, or touch the hardware key when prompted.  → *Expect:* the service reports that the passkey was created.
6. **Name the passkey clearly.** Use a label such as work laptop July 2026 or YubiKey blue.  → *Expect:* the passkey list shows a name you can recognize later.
7. **Record how it is backed up.** Note whether the passkey syncs through your account, lives only on one device, or sits on a physical key.  → *Expect:* you know what would happen if this device were lost.
8. **Test in a private window.** Open a private browser window or another device and start sign-in with the passkey.  → *Expect:* the service offers the new passkey and asks for the expected unlock method.
9. **Complete the test sign-in.** Use the passkey once, then return to the security settings.  → *Expect:* the account signs in without an SMS or authenticator code.
10. **Add a second passkey if possible.** Enroll another phone, laptop, password manager, or hardware key.  → *Expect:* the account has at least two passkeys or one passkey plus another strong fallback.
11. **Keep password and recovery sane.** If the account still has a password, keep it unique in a password manager and keep recovery codes current.  → *Expect:* losing one device does not mean losing the account.
12. ⚠ **Remove only obsolete methods.** Delete old passkeys or devices you no longer control. ⚠️ *Irreversible:* removing the only passkey or fallback can block access, so complete a fresh test sign-in first.  → *Expect:* active methods match devices you control.

**Done when:** A new private-window sign-in succeeds using the passkey, and account security settings show at least one fallback method that does not depend on the same device.

## review account security  
`accounts/review-account-security`

**Goal:** An annual (or post-incident) sweep of your important accounts: sessions, factors, recovery paths, connected apps, and passwords are verified current and yours — the hygiene that makes account takeover boring to attempt.

1. **Start with the email account — it outranks everything.** Whoever holds your email holds your password resets; it gets the fullest version of every step below.  → *Expect:* the sweep order acknowledges email as the root of the tree.
2. **Review active sessions/devices and evict strangers.** Security settings → "your devices" / "where you're logged in": recognize each entry (device, location, last active). Unknown or stale → sign it out; anything *suspicious* (a country you've never been) → sign out all + change the password now.  → *Expect:* the session list reads as a biography of your actual devices.
3. **Audit sign-in methods and factors.** 2FA still on, and on the strongest available method (`accounts/enable-two-factor-authentication`)? Phone number current? Passkeys offered — enroll. Old factors (a previous phone, SMS-when-you-have-app) removed.  → *Expect:* factors current, minimal, and strongest-available.
4. **Verify recovery paths — the forgotten backdoor.** Recovery email and phone: still yours, still active? (A recycled old number is an open door.) Recovery codes: located, and re-generated if you can't find them. Security questions (legacy accounts): answers rotated to non-guessable strings stored in the manager.  → *Expect:* every recovery channel points at something you currently control.
5. **Prune third-party access.** "Connected apps"/"apps with account access": that quiz from 2019, the service you stopped using — revoke by default; keep only what you recognize *and* still use. Same for OAuth "sign in with" grants.  → *Expect:* the connected-apps list is short and current.
6. **Handle the password itself on evidence, not ritual.** Check the account against breach-notification services (haveibeenpwned-class, or the manager's built-in audit): breached or reused → change it now to a generated unique one; strong-unique-unbreached → leave it (forced rotation without cause breeds weak patterns).  → *Expect:* no reused or breached passwords among tier-1 accounts.
7. **Log the sweep and calendar the next.** A one-line note per account ("2026-07: sessions clean, passkey added, 3 apps revoked") and a recurring annual reminder — plus triggers: run this after any breach news, lost device, or breakup involving shared devices.  → *Expect:* the review is a system, not a mood.

**Done when:** For each tier-1 account: sessions recognized, strongest 2FA active, recovery paths verified yours, connected apps pruned, password unique and unbreached — and the log line + next-year reminder exist. The email account got all of it first.

## secure your home wifi  
`digital/secure-your-home-wifi`

**Goal:** Home Wi-Fi is protected with a strong router admin password, modern encryption, a strong network passphrase, guest isolation, and firmware updates.

1. **Find the router admin route.** Use the router maker's app or type the gateway address from your network settings.  → *Expect:* you reach the router login screen, not a search-result support page.
2. **Log in and change the admin password.** Replace default or reused admin credentials with a unique password stored in your password manager.  → *Expect:* the router accepts the new admin password and requires it for future changes.
3. **Update router firmware.** Check for Firmware, Software update, or Router update and install available updates.  → *Expect:* the router restarts and reports current firmware.
4. **Set Wi-Fi encryption to WPA3 or WPA2.** [BRANCH: WPA3 available | WPA2 only] Use WPA3-Personal if all devices support it, or WPA2/WPA3 mixed mode when needed.  → *Expect:* security mode is not WEP, WPA, or open.
5. **Set a strong Wi-Fi passphrase.** Use a long phrase or generated password that is not reused elsewhere.  → *Expect:* the network saves the new passphrase and reconnects your device after entry.
6. **Disable risky convenience features.** Turn off WPS PIN, remote admin from internet, and default open setup networks unless specifically needed.  → *Expect:* outside devices cannot administer the router or join by PIN.
7. **Create a guest network.** Enable guest Wi-Fi with a separate passphrase and client isolation if available.  → *Expect:* guests can reach the internet but not your private devices.
8. **Check connected devices.** Review the device list and rename known devices for easier future checks.  → *Expect:* unknown devices are removed or blocked after you change the Wi-Fi passphrase.
9. **Save recovery details.** Store admin login, Wi-Fi passphrase, router model, and ISP support details privately.  → *Expect:* you can recover settings without using factory defaults.

**Done when:** The router shows a unique admin password, WPA3 or WPA2 encryption, WPS/remote admin disabled unless intentionally needed, current firmware, and a separate guest network.

## back up your phone  
`digital/back-up-your-phone`

**Goal:** Create a current phone backup and verify that the important data would be recoverable after loss, damage, or replacement.

1. **Choose backup location.** [BRANCH: cloud | computer] use cloud for automatic recovery, or a computer for local control and large backups.  → *Expect:* you know where the backup will be stored.
2. **Check what is included.** Review whether photos, messages, contacts, app data, device settings, and health data are included.  → *Expect:* critical categories are either included or handled separately.
3. **Free storage if needed.** Compare available cloud or computer storage with the estimated backup size.  → *Expect:* there is enough space to finish the backup.
4. **Connect power and Wi-Fi.** Plug in the phone and connect to a trusted Wi-Fi network unless using a computer cable.  → *Expect:* the backup will not fail from battery or cellular limits.
5. **Start the backup.** Use the phone's backup settings or the computer's device-management app.  → *Expect:* progress starts or the phone reports a backup is queued.
6. **Keep the phone available.** Leave it locked or idle until the backup completes.  → *Expect:* the backup finishes without interruption.
7. **Verify timestamp and size.** Open backup settings and confirm the latest backup date, time, and device name.  → *Expect:* the newest backup is from today and belongs to this phone.
8. **Check separate apps.** Confirm chat apps, authenticator apps, banking apps, and photo services have their own backup or transfer plan if needed.  → *Expect:* app-specific data is not assumed without evidence.
9. **Set cadence.** Turn on automatic backup or schedule a manual backup before travel, repairs, and phone upgrades.  → *Expect:* the next backup will happen without relying on memory.

**Done when:** Backup settings show a completed backup from today for this phone, and your most important data categories are listed as included or separately backed up.

## recover a hacked account  
`digital/recover-a-hacked-account`

**Goal:** Regain control of a compromised online account and reduce the chance that the attacker can re-enter.

1. **Move to a clean device and network.** Use a trusted phone or computer, update the browser, and avoid links from suspicious emails.  → *Expect:* you are on the service's official site or app.
2. **Change the password first.** Use the account security page or recovery flow to set a new unique password from a password manager.  → *Expect:* the service confirms the password changed.
3. **Revoke active sessions.** Sign out of all devices, apps, browsers, and remembered logins.  → *Expect:* the account lists only your current clean session afterward.
4. **Check recovery settings.** Remove unknown emails, phone numbers, security questions, forwarding rules, and backup addresses.  → *Expect:* every recovery option belongs to you.
5. **Turn on two-factor authentication.** [BRANCH: authenticator app | security key | SMS] choose the strongest method available and save backup codes somewhere private.  → *Expect:* future sign-ins require the second factor.
6. **Review connected apps and permissions.** Remove unknown third-party apps, tokens, mail clients, and browser extensions.  → *Expect:* only services you recognize still have access.
7. **Inspect recent account activity.** Look for password changes, purchases, messages, posts, bank changes, or forwarding rules made during the compromise.  → *Expect:* suspicious actions are identified for cleanup or reporting.
8. **Notify affected contacts.** Tell people who may have received scams from your account not to click links or send money.  → *Expect:* key contacts know the compromise is contained.
9. **Secure related accounts.** Change passwords anywhere the old password was reused, starting with email, banking, and phone carrier accounts.  → *Expect:* reused credentials no longer unlock other accounts.

**Done when:** The password is unique, unknown sessions and recovery methods are gone, 2FA is enabled, and recent activity shows no new unauthorized actions after the cleanup.

## save your 2fa recovery codes  
`accounts/save-your-2fa-recovery-codes`

**Goal:** Generate and store two-factor authentication recovery codes so a lost phone or broken authenticator does not lock you out.

1. **Open security settings.** Go to account settings, security, two-step verification, or two-factor authentication.  → *Expect:* the page lists current two-factor methods.
2. **Find recovery codes.** Select backup codes, recovery codes, emergency codes, or generate codes.  → *Expect:* the service warns that each code works once.
3. **Reauthenticate if prompted.** Enter your password, passkey, authenticator code, or hardware key touch.  → *Expect:* the recovery-code generation screen opens.
4. ⚠ **Generate a fresh set.** Create new codes if none exist or if you are unsure who has seen the old set. ⚠️ *Irreversible:* generating new codes often invalidates old codes, so confirm you can save the new set now.  → *Expect:* a full set of codes appears with a date or download option.
5. **Count the codes.** Note how many codes were issued and whether they are one-time use.  → *Expect:* your storage note can later show how many remain.
6. **Save to a password manager.** Put the codes in the account's password-manager item or a secure note labeled with the service name and date.  → *Expect:* the saved item is encrypted and searchable by account name.
7. **Create an offline backup.** Print or handwrite the codes and place them in a locked drawer, safe, or sealed emergency folder.  → *Expect:* you have one copy that does not depend on your phone, laptop, or cloud account.
8. **Avoid unsafe storage.** Do not leave screenshots in camera roll, downloads, chat messages, or plain email.  → *Expect:* temporary files containing the codes are deleted.
9. **Test one code if the service allows.** Sign in from a private window and use a single recovery code, then mark that code used.  → *Expect:* the login succeeds and one code is crossed out or deleted.
10. **Regenerate after a test if needed.** If the service provides few codes or the test consumed one you want back, generate a new full set and replace all copies.  → *Expect:* only the latest set remains in storage.
11. **Label the storage clearly.** Include service name, username, date generated, and "one-time codes" without adding the account password to the same paper sheet.  → *Expect:* you can identify the right codes under stress.
12. **Schedule a review.** Add a reminder to check recovery methods after phone replacement, job change, or moving password managers.  → *Expect:* the codes will not sit forgotten after major changes.

**Done when:** You can retrieve the current recovery-code set from one encrypted location and one offline location, and at least one tested sign-in or visible settings page confirms the codes are valid.

## use incognito mode correctly  
`digital/use-incognito-mode-correctly`

**Goal:** Use a private browsing window for local privacy without mistaking it for anonymity from websites, networks, employers, or internet providers.

1. **Open a private window.** Use the browser menu or keyboard shortcut for incognito, private, or InPrivate mode.  → *Expect:* the browser shows a separate private-mode window or badge.
2. **Confirm what it protects locally.** Treat it as a window that will not save browsing history, cookies, form entries, or site sessions after it closes.  → *Expect:* you know the protection is mainly on this device.
3. **Confirm what it does not hide.** Remember that websites, downloads, bookmarks, employers, schools, internet providers, and network admins may still see activity.  → *Expect:* you do not treat the session as anonymous.
4. **Use it for the right task.** [BRANCH: shared computer | separate login | price or search test] use it to avoid staying signed in, test a second account, or reduce local tracking from existing cookies.  → *Expect:* the task benefits from a clean local session.
5. **Avoid sensitive downloads on shared machines.** If you download a file, delete it afterward and empty trash if appropriate.  → *Expect:* no private file remains in the downloads folder.
6. **Sign out before closing.** Log out of accounts used in the private window, especially email, banking, work, and social media.  → *Expect:* the page confirms sign-out or returns to a public login screen.
7. **Close every private window.** Close all private windows, not just one tab, to clear that session's cookies.  → *Expect:* reopening private mode starts without the previous login.
8. **Use stronger tools when needed.** For real anonymity or location masking, evaluate a reputable VPN, Tor Browser, or policy-approved work tool.  → *Expect:* private mode is not the only privacy control for high-risk tasks.

**Done when:** After all private windows are closed and reopened, the site no longer shows the prior session, while any downloaded or bookmarked files are handled intentionally.

