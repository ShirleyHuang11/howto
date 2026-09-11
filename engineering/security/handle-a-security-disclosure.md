---
name: handle-a-security-disclosure
domain: engineering
subdomain: security
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1d
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You triage a reported vulnerability, protect reporter and user data, fix or mitigate the issue, and communicate status through a controlled disclosure process.

## Preconditions

- A private intake channel exists, such as security email, bug bounty platform, or private advisory.
- Security owner, engineering owner, and communications contact are identified.
- Access to affected systems, logs, and deployment pipeline is available.

## Steps

1. **Acknowledge receipt privately.** Reply through the intake channel without asking the reporter to share exploit details publicly. → *Expect:* the reporter has confirmation and a tracking ID.
2. **Restrict the case.** Create a private issue or incident record with need-to-know access. → *Expect:* sensitive exploit details are not visible in public trackers or broad chat rooms.
3. **Reproduce safely.** Use a staging environment or isolated production-safe proof that avoids accessing unrelated user data. → *Expect:* the team can confirm whether the vulnerability is real and scoped.
4. **Assess severity and blast radius.** Determine affected versions, assets, data exposure, exploitability, and whether active abuse is visible in logs. → *Expect:* severity, owner, and target fix timeline are documented.
5. **Apply mitigation or patch.** Fix the vulnerable code/configuration, rotate exposed credentials if needed, and add regression tests. → *Expect:* the vulnerability no longer reproduces in staging.
6. **Deploy through the emergency or normal path.** Use the fastest safe process based on severity; monitor errors and security signals. → *Expect:* production is patched or mitigated.
7. **Confirm with the reporter.** Share enough detail for retesting without exposing unrelated internals. → *Expect:* reporter can verify the issue is resolved or provide remaining reproduction steps.
8. **Publish advisory if needed.** ⚠️ *Irreversible:* public disclosure cannot be taken back; confirm affected users, patch availability, legal/comms approval, and CVE/advisory content first. → *Expect:* users receive accurate mitigation or upgrade guidance.

## Decision points

- Active exploitation or data exposure suspected → open an incident and preserve logs immediately.
- Third-party dependency is affected → coordinate with upstream and consider private fork/mitigation until release.
- Reporter asks for public disclosure before fix → negotiate a reasonable embargo and document the timeline.
- User notification may be legally required → involve legal/privacy counsel promptly.

## Failure modes & recovery

- **F1 Cannot reproduce:** detect incomplete report → ask for minimal safe reproduction details and inspect logs for matching behavior.
- **F2 Patch incomplete:** detect reporter still reproduces → reopen severity assessment and add failing regression test first.
- **F3 Details leaked internally:** detect broad access or public issue → move to restricted channel and remind participants not to repost.
- **F4 Coordinated disclosure slips:** detect missed timeline → update reporter with status and revised date before the deadline.

## Verification

The original reproduction returns the expected safe failure or no longer exposes data, regression tests exit 0, production contains the fix, and the private case records reporter confirmation or maintainer verification.

## Variations

- `Open source project`: use GitHub Security Advisories or a private fork for coordinated patches.
- `Bug bounty`: follow platform SLA, severity taxonomy, and reward workflow.
- `SaaS incident`: combine disclosure handling with incident response, customer notification, and audit-log review.

## Safety & privacy

High risk because reports may include exploitable details or user data. Keep access restricted, do not test against unrelated users, preserve evidence, coordinate public statements, and avoid blaming the reporter.
