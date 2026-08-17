---
name: howto-scam-and-fraud-defense
description: The "don't get scammed" kit — spot it, stop it, recover from it. Verified howto recipes for: Scam & Fraud Defense.
---

# Scam & Fraud Defense — howto skill

The "don't get scammed" kit — spot it, stop it, recover from it.

When the user needs any task below, follow its verified steps in order. Each step's **Expect** is the observation that confirms it worked; steps marked ⚠ are irreversible — confirm before doing them. For the full recipe (decision points, failure recovery, variations) use the howto MCP `get_howto(<id>)` or read the linked source.

## spot a phishing email  
`digital/spot-a-phishing-email`

**Goal:** A suspicious email correctly classified as phishing or legitimate using a repeatable check sequence — and the phishing one neutralized without a single click, because the click *is* the attack.

1. **Read the pressure, not just the content.** Phishing's signature is manufactured urgency plus a demanded action: account suspended, package held, invoice overdue, boss needs gift cards, "unusual sign-in." Legitimate institutions rarely demand same-hour action by email link.  → *Expect:* a pressure-score; high pressure raises the bar for every following check.
2. **Inspect the true sender address, not the display name.** Expand the sender details: display "PayPal" wrapping `paypal-security@accounts-verify.net` is the tell. Lookalike domains (rn for m, extra words, wrong TLD) are the industry standard.  → *Expect:* either the institution's exact known domain, or your answer.
3. **Hover, never click, the links.** Hold/long-press or hover to preview each URL: the visible text and the destination diverge in phishing, and the destination's *registered domain* (the part before the first single slash, read right-to-left) is the truth. `paypal.com.secure-login.info` belongs to `secure-login.info`.  → *Expect:* every link's real destination read; one mismatch convicts the whole email.
4. **Audit the remaining tells.** Generic greeting ("Dear Customer") where the real institution knows your name; attachment types that execute (.html, .zip, .docm — unexpected attachments are hostile until proven otherwise); reply-to differing from sender; and, decreasingly, language errors (modern phishing is fluently written — absence of typos proves nothing now).  → *Expect:* an accumulating verdict, weighted toward the sender and link evidence.
5. **Verify through your own channel when stakes exist.** Anything touching money, logins, or your employer: open the institution's site or app by *typing the address* or using your bookmark (`accounts/log-in` step 1's law), or call the number from your card/statement. The real account's own message center confirms or denies in seconds.  → *Expect:* ground truth obtained without the email's participation.
6. **Sentence and execute.** Phishing: report via the mail client's report-phishing button (it trains everyone's filters), then delete; work email forwards to IT/security first — they genuinely want it. Legitimate after all: proceed via your own channel anyway, having lost nothing.  → *Expect:* the email dispatched appropriately; zero of its links clicked either way.

**Done when:** The verdict was reached from sender, links, and out-of-band verification — not from the email's own claims; nothing was clicked pre-verdict; the phish was reported, not just deleted; and any already-clicked exposure triggered the password/2FA/card protocol within minutes, not days.

## spot a scam text message  
`digital/spot-a-scam-text-message`

**Goal:** A suspicious text message is identified as scam or legitimate without clicking its link, and scam messages are reported and blocked.

1. **Stop before tapping anything.** Treat links, attachments, and phone numbers in the message as untrusted.  → *Expect:* no link has opened and no reply has been sent.
2. **Read the pressure pattern.** Look for urgency, threats, prizes, failed delivery, unpaid toll, bank lock, tax refund, or "reply YES" prompts.  → *Expect:* pressure or reward language raises suspicion.
3. **Inspect the sender and link preview.** Long-press only if your phone previews safely; otherwise do not interact.  → *Expect:* the sender is a short code, unknown number, or spoofable name, and any link domain can be judged.
4. **Compare against your real account.** Open the company's official app or type its website yourself.  → *Expect:* the real account either confirms the issue or shows nothing is pending.
5. **Verify through an official channel.** Call the number on your card, statement, delivery account, or government website, not the text.  → *Expect:* confirmation comes from a source independent of the message.
6. **Do not reply to scam texts.** Replying can confirm your number is active.  → *Expect:* the conversation remains unanswered.
7. **Report and block.** Use the phone's Report Junk/Spam option or forward SMS scams to the carrier reporting number where available, then block the sender.  → *Expect:* the thread is marked reported or the sender is blocked.
8. **Act if you already clicked or entered data.** Change affected passwords, enable 2FA, contact the bank/card issuer, and watch accounts.  → *Expect:* exposed accounts are secured through official apps or websites.

**Done when:** No scam link was used for login or payment, the issue was checked through an official channel, and scam messages were reported and blocked.

## spot a phone scam  
`digital/spot-a-phone-scam`

**Goal:** A suspicious phone call is handled without giving money, codes, account access, or private information, and legitimate issues are verified by calling back through official numbers.

1. **Pause the conversation.** Do not answer security questions, confirm personal details, or follow instructions while surprised.  → *Expect:* the caller has not received useful information.
2. **Listen for pressure and secrecy.** Scam callers push fear, time limits, "do not tell anyone", arrest threats, account closure, or family emergency stories.  → *Expect:* pressure makes the call untrusted.
3. **Listen for payment tells.** Gift cards, crypto, wire transfer, payment apps, remote access software, and one-time codes are red flags.  → *Expect:* any such demand is treated as scam evidence.
4. **Refuse remote control or code sharing.** Do not install apps, read verification codes, or approve login prompts for a caller.  → *Expect:* no account or device access has been granted.
5. **End the call politely or silently.** Say you will call back through the official number, then hang up.  → *Expect:* the caller cannot keep escalating pressure.
6. **Find the official number yourself.** Use the number on your card, statement, official website, app, or prior verified contact.  → *Expect:* the number is independent of the incoming call or voicemail.
7. **Call back and verify.** Ask whether the claimed issue exists.  → *Expect:* the real organization confirms, denies, or documents next steps.
8. **Report and block scam calls.** Use phone blocking, carrier spam tools, and appropriate fraud reporting channels.  → *Expect:* the number is blocked and the call is recorded for reference.

**Done when:** No money, codes, remote access, or private information were given to the incoming caller, and any claimed issue was checked through an official callback number.

## spot a fake website  
`digital/spot-a-fake-website`

**Goal:** Decide whether a website is likely legitimate before entering passwords, personal data, or payment details.

1. **Pause before interacting.** Do not type passwords, card numbers, or codes until the site passes basic checks.  → *Expect:* no sensitive data has been submitted yet.
2. **Check the URL exactly.** Read the domain from right to left before the first single slash, watching for misspellings, extra words, and strange endings.  → *Expect:* the domain matches the real organization exactly or raises a concern.
3. **Treat the padlock as limited.** Confirm HTTPS is present, but remember it only means the connection is encrypted.  → *Expect:* you do not treat the padlock as proof the business is real.
4. **Reach the site independently.** Open a new tab and search for the organization or use a saved bookmark instead of the link that brought you there.  → *Expect:* the independent route lands on the same domain or a different official one.
5. **Inspect contact and policy pages.** Look for a real address, support channel, return policy, privacy policy, and consistent company name.  → *Expect:* business details are specific and consistent.
6. **Look for payment red flags.** Watch for wire transfer, crypto, gift cards, payment through friends-and-family, or pressure to bypass normal checkout.  → *Expect:* payment options look standard for the transaction.
7. **Check outside reviews.** Search the domain plus "reviews", "scam", or "complaints" and read recent independent results.  → *Expect:* there is a track record beyond the site's own testimonials.
8. **Test the offer against reality.** Compare prices, availability, and urgency claims with known retailers or official sites.  → *Expect:* extreme discounts or impossible stock are treated as warnings.
9. **Decide before submitting.** [BRANCH: looks legitimate | uncertain or suspicious] proceed with a low-risk payment method, or close the site and use an official channel.  → *Expect:* sensitive data is entered only on a site you can justify trusting.

**Done when:** Before entering sensitive data, the exact domain, independent access route, business details, reviews, and payment method all match a legitimate organization.

## report a scam  
`digital/report-a-scam`

**Goal:** A scam is reported to the right platform, financial institution, and authority while evidence is preserved and affected accounts are secured.

1. **Stop interaction.** Do not reply, click more links, send more money, or provide more codes.  → *Expect:* the scammer no longer receives new information from you.
2. **Preserve evidence.** Save screenshots, emails with headers if possible, phone numbers, usernames, URLs, receipts, tracking numbers, and timestamps.  → *Expect:* evidence is stored before deletion or blocking.
3. **Secure affected accounts.** Change passwords, revoke suspicious sessions, turn on two-factor authentication, and check recovery details.  → *Expect:* account access is under your control.
4. **Contact the money handler.** If payment or banking was involved, call the bank, card issuer, payment app, or crypto exchange through official support.  → *Expect:* fraud report, dispute, freeze, or case number is opened.
5. **Report to the platform.** Use the marketplace, social network, email provider, phone carrier, job site, or app's report flow.  → *Expect:* the account, listing, message, or transaction is flagged.
6. **Report to authorities.** File with the consumer protection, cybercrime, police, or identity-theft authority relevant to your location.  → *Expect:* a report number or confirmation is saved.
7. **Warn affected people.** Tell contacts, family, coworkers, or group admins if the scam used your name or could target them next.  → *Expect:* likely secondary targets know not to trust the scam.
8. **Monitor follow-up.** Watch accounts, credit, mail, and messages for repeated attempts or retaliation.  → *Expect:* new suspicious activity is caught quickly.

**Done when:** Evidence is saved, affected accounts are secured, and each relevant platform, financial provider, or authority has issued a report confirmation or case number.

## protect an elderly relative from scams  
`digital/protect-an-elderly-relative-from-scams`

**Goal:** An elderly relative has practical scam protections, a calm family response plan, and a no-shame route for reporting suspicious calls, texts, emails, or payments.

1. **Start with a calm conversation.** Frame the topic as criminals getting better, not the relative being careless.  → *Expect:* the relative is willing to talk without feeling accused.
2. **Name the common scams.** Cover grandchild emergency, romance, tech support, bank fraud, government threat, lottery/prize, delivery, investment, and gift-card scams.  → *Expect:* the relative recognizes at least a few scripts.
3. **Create a verification rule.** Agree that urgent money or secrecy requests require calling a known family number or official number first.  → *Expect:* the rule is simple enough to remember under stress.
4. **Harden phone and messages.** Enable spam filtering, block unknown repeat callers, silence unknown callers if acceptable, and pin trusted contacts.  → *Expect:* fewer suspicious calls and easier access to real contacts.
5. **Protect financial accounts.** Turn on transaction alerts, set lower transfer limits where practical, and discuss trusted-contact or view-only monitoring options.  → *Expect:* unusual transactions generate alerts before losses grow.
6. **Secure key accounts.** Use unique passwords, a password manager if acceptable, and 2FA for email, bank, and phone carrier accounts.  → *Expect:* account takeover becomes harder.
7. **Limit exposed payment paths.** Discuss avoiding gift cards for emergencies, not storing cards on unfamiliar sites, and using a credit card rather than debit for online purchases when possible.  → *Expect:* risky payment methods are less available in panic moments.
8. **Make an after-a-hit plan.** Write down who to call first: bank/card, trusted family contact, local police/nonemergency if needed, and account providers.  → *Expect:* the relative has a visible action list.
9. **Schedule gentle check-ins.** Review recent calls, texts, charges, and mail periodically with permission.  → *Expect:* problems surface early without interrogation.

**Done when:** The relative can state the verification rule, has spam and transaction alerts enabled where acceptable, and has a written after-a-hit contact plan.

## check if your data was in a breach  
`digital/check-if-your-data-was-in-a-breach`

**Goal:** You determine whether an email address or phone number appears in known data breaches, then take password and two-factor actions for affected accounts.

1. **Use a reputable breach-check service.** Open a known service such as Have I Been Pwned or a password manager's built-in breach monitor by typing the address directly.  → *Expect:* the site explains what it checks and does not ask for your password.
2. **Check one identifier at a time.** Enter an email address or phone number, then submit.  → *Expect:* the result lists no breaches or names specific breach incidents.
3. **Record affected services.** Note breached sites, data types exposed, and breach dates.  → *Expect:* you have a short action list by account.
4. **Prioritize passwords reused anywhere.** Search your password manager for the affected email and reused or weak passwords.  → *Expect:* reused passwords are identified before lower-risk cleanup.
5. **Change exposed or reused passwords.** Log in through each service's official site and set a unique password generated by the password manager.  → *Expect:* the password manager stores a new unique password for each affected account.
6. **Turn on two-factor authentication.** Prefer authenticator app, passkey, or security key over SMS when available.  → *Expect:* the account shows 2FA enabled and recovery codes saved privately.
7. **Review account activity.** Check recent logins, devices, recovery email, phone number, forwarding rules, and payment details on affected accounts.  → *Expect:* no unknown sessions or settings remain.
8. **Monitor for follow-up scams.** Treat breach-themed calls, texts, and emails as suspicious, especially if they cite old personal details.  → *Expect:* you verify through official channels before acting.

**Done when:** Every affected account with reused, weak, or exposed credentials now has a unique password and 2FA enabled where supported, and account activity shows no unknown active sessions.

## recognize a fake invoice  
`finance/recognize-a-fake-invoice`

**Goal:** Decide whether an invoice is legitimate before paying it, especially when details, pressure, or vendor identity look wrong.

1. **Pause payment.** Do not click payment links or send money while checking the invoice.  → *Expect:* no payment has been initiated.
2. **Check the vendor identity.** Compare name, logo, address, tax ID, email domain, and phone number with past records.  → *Expect:* differences are visible instead of hidden in the message.
3. **Match the business reason.** Find the order, subscription, shipment, medical visit, repair, or contract tied to the charge.  → *Expect:* there is a real event that explains the invoice.
4. **Inspect payment details.** Look for new bank accounts, changed remit-to addresses, personal payment apps, gift cards, or crypto requests.  → *Expect:* suspicious payment changes are flagged before payment.
5. **Look for pressure tactics.** Note threats of immediate collection, legal action, account closure, or late fees that do not match normal terms.  → *Expect:* urgency is treated as a risk signal.
6. **Verify out-of-band.** Contact the vendor using a saved number, contract, prior invoice, or official portal, not the contact details on the suspect invoice.  → *Expect:* a known contact confirms whether the invoice exists.
7. **Confirm amount and due date.** Ask the known contact to verify invoice number, balance, due date, and payment instructions.  → *Expect:* details match exactly or the invoice is rejected.
8. **Check internal approvals.** For work invoices, match purchase order, receiving record, approver, and vendor master file.  → *Expect:* normal approval evidence exists.
9. **Reject fake invoices in writing.** If fake, mark it disputed or fraudulent and warn relevant accounting or household members.  → *Expect:* nobody else pays the same invoice.
10. ⚠ **Pay only through verified channels.** Use the official portal or saved vendor payment profile. ⚠️ *Irreversible:* bank transfers, gift cards, crypto, and some instant payments may not be recoverable, so never pay blindly.  → *Expect:* payment confirmation names the verified vendor and invoice.
11. **Save the review trail.** Keep the invoice, verification notes, and payment confirmation or fraud report.  → *Expect:* the decision can be audited later.
12. **Block or report the sender.** Report phishing to your email provider, company security team, or the impersonated vendor.  → *Expect:* the sender is blocked or the threat is documented.

**Done when:** The invoice is either confirmed by a known vendor contact with matching amount and payment details, or it is marked fraudulent and no payment is made.

## spot a fake charity  
`finance/spot-a-fake-charity`

**Goal:** A charity request is checked for legitimacy before you donate, and any gift is made only through the charity's official channel.

1. **Pause the appeal.** Do not donate during the call, doorstep visit, message thread, or emotional pitch.  → *Expect:* you have time to verify without pressure.
2. **Record the claimed name.** Write down the exact charity name, website, phone number, and fundraiser name.  → *Expect:* spelling and contact details are available for comparison.
3. **Search official registration.** Check the charity regulator, tax-exempt database, or nonprofit registry for the exact name.  → *Expect:* registration status, legal name, and identifier match or do not match.
4. **Compare contact details.** Use the registry or official charity website to compare phone, domain, address, and donation page.  → *Expect:* the solicitation details match trusted records.
5. **Look for pressure tells.** Notice urgency, secrecy, vague programs, celebrity claims, or refusal to send written information.  → *Expect:* any manipulation signs are identified before payment.
6. **Reject unsafe payment methods.** Refuse gift cards, wire transfers, crypto, payment apps to individuals, or cash pickup.  → *Expect:* only traceable donation channels remain.
7. **Donate through the official site.** Type the official web address yourself or use the registry's link.  → *Expect:* payment goes to the confirmed charity domain or mail address.
8. **Save the receipt.** Keep confirmation, amount, date, and charity identifier for records.  → *Expect:* proof of donation is stored.

**Done when:** The charity registration and contact details match official records, and any donation is made through the verified official channel.

## report identity theft  
`finance/report-identity-theft`

**Goal:** Report identity theft, block new misuse, and create records needed to dispute fraudulent accounts or charges.

1. **Secure core accounts first.** Change passwords for email, banking, and phone-carrier accounts, then sign out unknown sessions.  → *Expect:* only your devices remain active.
2. **Freeze your credit.** Place security freezes with the three major credit bureaus or the relevant bureaus in your locale.  → *Expect:* each bureau gives a confirmation, PIN, or online account status showing frozen.
3. **File the official identity-theft report.** Use the official government reporting portal for your country, such as IdentityTheft.gov in the United States.  → *Expect:* you receive a report, recovery plan, or reference number.
4. **Create an evidence folder.** Save the official report, bureau confirmations, collection letters, account statements, screenshots, and call notes.  → *Expect:* every document has a date and source.
5. **Contact affected financial institutions.** Call the number on the back of the card, statement, or official website, not a number from a suspicious message.  → *Expect:* each institution opens a fraud case or closes the fraudulent account.
6. **Dispute fraudulent credit entries.** Send disputes to credit bureaus with the identity-theft report and specific account names.  → *Expect:* each bureau confirms receipt and investigation timing.
7. **Dispute debts with collectors.** Request debt validation in writing and state that the debt is from identity theft.  → *Expect:* the collector must pause or document the claim according to local rules.
8. **Replace compromised cards and account numbers.** Ask issuers to close stolen credentials and issue new numbers.  → *Expect:* old cards or account numbers no longer work.
9. **Check tax and benefits exposure.** Review official tax, unemployment, health, or benefits accounts if your national ID was exposed.  → *Expect:* no unfamiliar filings or claims appear, or a fraud case is opened.
10. **Set a recovery schedule.** Calendar follow-ups for bureau investigations, bank provisional credits, police reports if needed, and statement reviews.  → *Expect:* every open case has a next action date.
11. **Send written confirmations.** Follow phone calls with secure messages or letters summarizing what was agreed.  → *Expect:* you have written proof beyond call notes.
12. **Keep monitoring after cleanup.** Review credit reports, statements, and mail for several months.  → *Expect:* new suspicious activity is caught quickly.

**Done when:** Credit freezes are active, the official identity-theft report is saved, each fraudulent account or charge has a dispute case number, and follow-up dates are recorded.

## what to do if your card is stolen  
`finance/what-to-do-if-your-card-is-stolen`

**Goal:** Stop use of a stolen debit or credit card, dispute unauthorized charges, and restore payments with a replacement card.

1. **Freeze or lock the card immediately.** Use the issuer app or website if available before calling.  → *Expect:* the card status shows locked, frozen, or temporarily blocked.
2. **Check recent activity.** Review pending and posted transactions since the last time you had the card.  → *Expect:* you can identify known charges and suspicious ones.
3. **Call the issuer from a trusted number.** Use the number in the official app, on a statement, or on the issuer website.  → *Expect:* you reach card-loss or fraud support.
4. ⚠ **Report the card stolen.** State whether the physical card, wallet, phone wallet, or card number was stolen. ⚠️ *Irreversible:* once a card is reported stolen, the old card number is usually canceled, so confirm the correct card.  → *Expect:* the issuer blocks the card permanently.
5. **Dispute unauthorized charges.** Give transaction dates, merchant names, and amounts you do not recognize.  → *Expect:* each disputed charge receives a case number or provisional-credit status.
6. **Request replacement delivery.** Confirm mailing address, shipping speed, and whether emergency digital card access is available.  → *Expect:* a replacement card or digital card is issued.
7. **Remove stolen digital wallets.** If a phone or wallet was stolen, remove the card from mobile wallets and merchant accounts.  → *Expect:* the issuer or wallet shows old tokens revoked.
8. **Change related passwords if needed.** Update issuer login and email passwords if the stolen item included a phone, wallet note, or password list.  → *Expect:* account access is protected by a fresh password and two-factor method.
9. **Update autopays.** List subscriptions, utilities, rent, insurance, and loan payments that used the card.  → *Expect:* essential payments have the replacement card or alternate payment method.
10. **Watch pending charges.** Check daily until all pending transactions settle or disappear.  → *Expect:* no new unauthorized charges post after the stolen-card report time.
11. **Save documentation.** Keep issuer messages, dispute numbers, police report if filed, and delivery tracking.  → *Expect:* you can prove the report date and disputed amounts.
12. **Destroy the old card if recovered.** Cut through chip, magnetic stripe, and numbers after the issuer confirms cancellation.  → *Expect:* the recovered card cannot be used.

**Done when:** The stolen card shows canceled or blocked, unauthorized charges have dispute case numbers, and essential autopays are moved to a replacement or alternate payment method.

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

## 🗺️ recover from identity theft (journey)  
`journeys/recover-from-identity-theft`

A long-horizon plan spanning this whole area — read `journeys/recover-from-identity-theft.md` or ask the howto MCP. Mind the gates and re-plan triggers.

