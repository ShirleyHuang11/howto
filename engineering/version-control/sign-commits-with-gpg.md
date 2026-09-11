---
name: sign-commits-with-gpg
domain: engineering
subdomain: version-control
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

Configure Git to sign commits with a GPG key and verify that the hosting provider marks new commits as verified.

## Preconditions

- Git and GnuPG are installed on the development machine.
- You can update your source-hosting account's SSH/GPG key settings.
- You know the email address used in `git config user.email`.

## Steps

1. **Check for an existing signing key.** Run `gpg --list-secret-keys --keyid-format=long`. → *Expect:* either an existing `sec` key for your commit email or no suitable key.
2. **Generate a key if needed.** Run `gpg --full-generate-key`, choose an Ed25519 or RSA key supported by your organization, and use your Git email. → *Expect:* `gpg --list-secret-keys --keyid-format=long` shows a secret key with a long key ID.
3. **Export the public key.** Run `gpg --armor --export KEY_ID`. → *Expect:* output begins with `-----BEGIN PGP PUBLIC KEY BLOCK-----`.
4. **Add the public key to the hosting account.** In GitHub, GitLab, or Bitbucket account settings, paste the armored public key into the GPG keys section. → *Expect:* the provider shows the key as active for the account email.
5. **Configure Git signing.** Run `git config --global user.signingkey KEY_ID` and `git config --global commit.gpgsign true`; for a repository-only setup, omit `--global`. → *Expect:* `git config --get commit.gpgsign` prints `true`.
6. **Set the GPG program if required.** [BRANCH: macOS | Linux] On macOS with GPG Suite, run `git config --global gpg.program gpg`; on Linux, ensure `GPG_TTY=$(tty)` is exported in the shell startup file. → *Expect:* Git can invoke GPG without `No pinentry` or TTY errors.
7. **Create a signed test commit on a throwaway branch.** Run `git commit --allow-empty -m "test signed commit"` in a non-production branch. → *Expect:* Git prompts for the key passphrase if needed and creates the commit.
8. **Verify the signature.** Run `git log --show-signature -1`. → *Expect:* output includes `Good signature` for the latest commit.
9. **Push and confirm provider verification.** Push the test branch and open the commit page. → *Expect:* the provider displays a verified signature badge for that commit.

## Decision points

- Organization requires SSH signing instead of GPG → use `git config gpg.format ssh` and upload the allowed SSH signing key.
- Multiple emails on one machine → set `user.signingkey` per repository to avoid signing with the wrong identity.
- CI creates commits → configure a separate bot signing key or disable signing only for the automation repository context.

## Failure modes & recovery

- **F1 No secret key:** detect `gpg failed to sign the data` and `No secret key` → set `user.signingkey` to the long key ID that exists in `gpg --list-secret-keys`.
- **F2 Pinentry failure:** detect `Inappropriate ioctl for device` or `No pinentry` → install a pinentry program and export `GPG_TTY=$(tty)`.
- **F3 Unverified on provider:** detect local `Good signature` but no verified badge → add the commit email to the account or upload the matching public key.
- **F4 Expired key:** detect `key has expired` → extend or rotate the key, then upload the updated public key before signing new commits.

## Verification

Run `git log --show-signature -1`; it exits 0 and prints `Good signature`. After pushing the branch, the hosting provider's commit page shows the commit as verified for the expected account.

## Variations

- `GitHub`: GPG, SSH, and S/MIME signing are supported; branch protection can require signed commits.
- `GitLab`: upload the public GPG key in user preferences and verify the email address.
- `1Password or hardware key`: configure the vendor's SSH signing agent and set `gpg.format ssh`.

## Safety & privacy

Medium risk because a bad global Git config can disrupt all repositories on the machine. Never upload a private key, protect the key with a passphrase or hardware-backed storage, and revoke lost keys promptly.
