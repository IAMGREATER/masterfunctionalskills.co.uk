#!/usr/bin/env python3
"""
Area 4: Transacting Online (Cards 33-40)
"""
import xml.etree.ElementTree as ET

def wrap_svg(inner_content, height=170):
    svg = f'<svg viewBox="0 0 460 {height}" width="100%" height="{height}" xmlns="http://www.w3.org/2000/svg">\n{inner_content}\n</svg>'
    ET.fromstring(svg)
    return svg

CARDS = [
    # 33. Secure Online Purchasing & Padlock Check
    {
        "id": "dfs-33",
        "number": 33,
        "title": "Secure Online Purchasing &amp; HTTPS",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Transacting Online",
        "strand_theme": "emerald",
        "dfe_code": "DFS 4.1",
        "rule_heading": "HTTPS, SSL Encryption &amp; Merchant Checks",
        "rule_body": "Safe online shopping requirements: 1. Confirm the address begins with 'https://' with a padlock icon (data encrypted in transit). 2. Inspect domain spelling carefully to avoid fake clones. 3. Check independent reviews on Trustpilot. 4. Ensure clear contact details and postal address exist.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.6"/>
            <!-- Browser Address bar -->
            <rect x="15" y="15" width="340" height="36" rx="18" fill="#f1f5f9" stroke="#94a3b8"/>
            <text x="35" y="38" font-size="13" font-weight="900" fill="#059669">🔒 https://</text>
            <text x="108" y="38" font-size="13" font-weight="900" fill="#0f172a">www.trustedstore.co.uk</text>
            <!-- Checkpoints -->
            <g transform="translate(20, 65)">
              <rect x="0" y="0" width="330" height="22" rx="4" fill="#ecfdf5"/>
              <text x="10" y="16" font-size="10" font-weight="800" fill="#065f46">✓ HTTPS &amp; Padlock: Card data encrypted against eavesdroppers</text>
              <rect x="0" y="27" width="330" height="22" rx="4" fill="#ecfdf5"/>
              <text x="10" y="43" font-size="10" font-weight="800" fill="#065f46">✓ Legitimate UK Domain (.co.uk / registered company)</text>
              <rect x="0" y="54" width="330" height="22" rx="4" fill="#ecfdf5"/>
              <text x="10" y="70" font-size="10" font-weight="800" fill="#065f46">✓ Verified Reviews &amp; Clear UK Returns Policy</text>
            </g>
          </g>"""),
        "golden_rule": "Look for 'https://' and the padlock icon before entering card data!",
        "watch_out": 'Avoid online shopping on public, open Wi-Fi networks without a VPN.',
        "challenge_prompt": "What does the 's' in 'https://' indicate about the communication between your browser and the website?",
        "answer_text": "It stands for 'Secure' (SSL/TLS encryption), meaning data transferred between your browser and the site is encrypted."
    },

    # 34. Online Payment Methods & Protection
    {
        "id": "dfs-34",
        "number": 34,
        "title": "Payment Methods &amp; Section 75",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Transacting Online",
        "strand_theme": "emerald",
        "dfe_code": "DFS 4.2",
        "rule_heading": "Credit vs Debit vs Digital Wallets",
        "rule_body": "Payment safeguards: 1. Credit Cards: UK Section 75 Consumer Credit Act legally protects single purchases over £100 up to £30,000 if goods fail to arrive or seller collapses. 2. Debit Cards: Protected by voluntary Chargeback scheme. 3. Digital Wallets (Apple Pay/PayPal): Tokenises card details.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.6"/>
            <!-- Credit Card -->
            <rect x="15" y="12" width="105" height="120" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.4"/>
            <text x="67" y="32" font-size="11" font-weight="900" fill="#1e40af" text-anchor="middle">CREDIT CARD</text>
            <text x="22" y="55" font-size="9.5" font-weight="800" fill="#1e3a8a">Section 75</text>
            <text x="22" y="70" font-size="9" font-weight="600" fill="#475569">Legal protection</text>
            <text x="22" y="85" font-size="9" font-weight="600" fill="#475569">£100 - £30,000</text>
            <text x="22" y="115" font-size="9" font-weight="800" fill="#059669">Top Safety ✓</text>
            <!-- Debit Card -->
            <rect x="132" y="12" width="105" height="120" rx="6" fill="#fefce8" stroke="#eab308" stroke-width="1.4"/>
            <text x="184" y="32" font-size="11" font-weight="900" fill="#854d0e" text-anchor="middle">DEBIT CARD</text>
            <text x="139" y="55" font-size="9.5" font-weight="800" fill="#713f12">Chargeback</text>
            <text x="139" y="70" font-size="9" font-weight="600" fill="#475569">Voluntary bank</text>
            <text x="139" y="85" font-size="9" font-weight="600" fill="#475569">refund process</text>
            <text x="139" y="115" font-size="9" font-weight="700" fill="#ca8a04">Medium Safety</text>
            <!-- Bank Transfer -->
            <rect x="250" y="12" width="105" height="120" rx="6" fill="#fef2f2" stroke="#ef4444" stroke-width="1.4"/>
            <text x="302" y="32" font-size="11" font-weight="900" fill="#991b1b" text-anchor="middle">WIRE / TRANSFER</text>
            <text x="257" y="55" font-size="9.5" font-weight="800" fill="#991b1b">Direct Transfer</text>
            <text x="257" y="70" font-size="9" font-weight="600" fill="#475569">No statutory</text>
            <text x="257" y="85" font-size="9" font-weight="600" fill="#475569">refund rights</text>
            <text x="257" y="115" font-size="9" font-weight="800" fill="#dc2626">High Risk ✗</text>
          </g>"""),
        "golden_rule": 'Use a credit card for £100+ purchases for Section 75 legal refund cover!',
        "watch_out": 'Direct bank transfers offer almost no buyer protection if scammed.',
        "challenge_prompt": "Why is paying with a credit card safer than paying via direct bank transfer when purchasing a £400 laptop online?",
        "answer_text": "Under Section 75 of the Consumer Credit Act, the credit card provider is jointly liable with the retailer if goods are faulty or never delivered."
    },

    # 35. Online Banking Basics & Security
    {
        "id": "dfs-35",
        "number": 35,
        "title": "Online Banking &amp; Statements",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Transacting Online",
        "strand_theme": "emerald",
        "dfe_code": "DFS 4.3",
        "rule_heading": "Reconciling Transactions &amp; Card Freezes",
        "rule_body": "Banking safely online: 1. Regularly review transaction history to spot unauthorized micro-charges. 2. Verify all active Direct Debits and standing orders. 3. Immediately 'Freeze' lost cards inside mobile banking app. 4. Never access banking on public shared PCs.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.6"/>
            <rect x="0" y="0" width="370" height="26" rx="8" fill="#047857"/>
            <text x="185" y="18" font-size="11" font-weight="900" fill="#ffffff" text-anchor="middle">MOBILE BANKING INTERFACE</text>
            <text x="20" y="48" font-size="11" font-weight="800" fill="#065f46">Current Account: £1,240.50 Available</text>
            <!-- Transaction items -->
            <rect x="15" y="58" width="340" height="24" rx="4" fill="#f8fafc"/>
            <text x="25" y="74" font-size="9.5" font-weight="700" fill="#0f172a">12 Oct: Tesco Superstore - Groceries</text>
            <text x="310" y="74" font-size="9.5" font-weight="800" fill="#0f172a">-£32.40</text>
            <rect x="15" y="86" width="340" height="24" rx="4" fill="#fef2f2" stroke="#fca5a5"/>
            <text x="25" y="102" font-size="9.5" font-weight="800" fill="#dc2626">⚠️ Unrecognized Online Charge: SubGaming Ltd</text>
            <text x="310" y="102" font-size="9.5" font-weight="800" fill="#dc2626">-£1.00</text>
            <!-- Card freeze button -->
            <rect x="15" y="116" width="340" height="22" rx="4" fill="#0f172a"/>
            <text x="185" y="131" font-size="10" font-weight="800" fill="#f8fafc" text-anchor="middle">🔒 In-App Action: Tap to Instant Freeze Card</text>
          </g>"""),
        "golden_rule": 'Review online banking weekly to spot unauthorised charges promptly!',
        "watch_out": 'Never share one-time passcodes (OTPs) with anyone — banks never ask.',
        "challenge_prompt": "What in-app mobile banking tool allows you to immediately block all transactions if you misplace your card?",
        "answer_text": "The 'Freeze' or 'Lock Card' toggle switch."
    },

    # 36. Two-Factor Authentication (2FA / MFA)
    {
        "id": "dfs-36",
        "number": 36,
        "title": "Two-Factor Authentication (2FA)",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Transacting Online",
        "strand_theme": "emerald",
        "dfe_code": "DFS 4.4",
        "rule_heading": "Something You Know + Something You Have",
        "rule_body": "2FA adds an essential second security barrier: 1. Factor 1: Password (something you know). 2. Factor 2: One-Time Passcode (OTP) via authenticator app, SMS, or biometric fingerprint (something you have/are). If hackers steal your password, they still cannot gain access.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#f0fdf4" stroke="#059669" stroke-width="1.8"/>
            <text x="185" y="24" font-size="11.5" font-weight="900" fill="#065f46" text-anchor="middle">HOW TWO-FACTOR AUTHENTICATION WORKS</text>
            <!-- Step 1 -->
            <rect x="20" y="40" width="100" height="85" rx="6" fill="#ffffff" stroke="#cbd5e1"/>
            <text x="70" y="60" font-size="10.5" font-weight="900" fill="#0f172a" text-anchor="middle">STEP 1</text>
            <text x="70" y="80" font-size="9.5" font-weight="700" fill="#475569" text-anchor="middle">Password</text>
            <text x="70" y="105" font-size="8.5" font-weight="600" fill="#64748b" text-anchor="middle">(Something you know)</text>
            <!-- Plus -->
            <text x="135" y="88" font-size="18" font-weight="900" fill="#059669" text-anchor="middle">+</text>
            <!-- Step 2 -->
            <rect x="150" y="40" width="100" height="85" rx="6" fill="#ffffff" stroke="#cbd5e1"/>
            <text x="200" y="60" font-size="10.5" font-weight="900" fill="#0f172a" text-anchor="middle">STEP 2</text>
            <text x="200" y="80" font-size="9.5" font-weight="800" fill="#2563eb" text-anchor="middle">OTP / App Code</text>
            <text x="200" y="105" font-size="8.5" font-weight="600" fill="#64748b" text-anchor="middle">(Something you have)</text>
            <!-- Equals -->
            <text x="265" y="88" font-size="18" font-weight="900" fill="#059669" text-anchor="middle">=</text>
            <!-- Result -->
            <rect x="280" y="40" width="70" height="85" rx="6" fill="#dcfce7" stroke="#10b981"/>
            <text x="315" y="65" font-size="20" font-weight="900" fill="#059669" text-anchor="middle">✓</text>
            <text x="315" y="95" font-size="9.5" font-weight="900" fill="#065f46" text-anchor="middle">Secure</text>
            <text x="315" y="110" font-size="9" font-weight="700" fill="#065f46" text-anchor="middle">Access</text>
          </g>"""),
        "golden_rule": 'Enable 2FA everywhere — authenticator apps are much safer than SMS!',
        "watch_out": 'SMS codes are vulnerable to SIM-swap fraud; prefer app-based 2FA.',
        "challenge_prompt": "Why does two-factor authentication (2FA) protect your account even if a cybercriminal steals your password?",
        "answer_text": "Because login is blocked without the second factor (the unique code sent to your physical device or generated by your authenticator app)."
    },

    # 37. Public Services (GOV.UK & NHS Apps)
    {
        "id": "dfs-37",
        "number": 37,
        "title": "Accessing Public Services Online",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Transacting Online",
        "strand_theme": "emerald",
        "dfe_code": "DFS 4.5",
        "rule_heading": "GOV.UK, NHS App &amp; Council Portals",
        "rule_body": "Official UK public digital services: 1. GOV.UK: Apply for passports, check tax codes, Universal Credit, and renew driving licences. 2. NHS App: Order repeat prescriptions, view GP records, book blood tests. 3. Local Council: Pay Council Tax, register to vote, apply for parking permits.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.6"/>
            <!-- GOV.UK -->
            <rect x="15" y="15" width="105" height="115" rx="6" fill="#0b0c0c"/>
            <text x="67" y="38" font-size="11" font-weight="900" fill="#ffffff" text-anchor="middle">GOV.UK</text>
            <text x="67" y="60" font-size="9" font-weight="700" fill="#b1b4b6" text-anchor="middle">• Passport renew</text>
            <text x="67" y="76" font-size="9" font-weight="700" fill="#b1b4b6" text-anchor="middle">• Driving licence</text>
            <text x="67" y="92" font-size="9" font-weight="700" fill="#b1b4b6" text-anchor="middle">• Universal Credit</text>
            <text x="67" y="114" font-size="8.5" font-weight="800" fill="#00703c" text-anchor="middle">Official Portal ✓</text>
            <!-- NHS App -->
            <rect x="132" y="15" width="105" height="115" rx="6" fill="#005eb8"/>
            <text x="184" y="38" font-size="11" font-weight="900" fill="#ffffff" text-anchor="middle">NHS APP</text>
            <text x="184" y="60" font-size="9" font-weight="700" fill="#ffffff" text-anchor="middle">• Prescriptions</text>
            <text x="184" y="76" font-size="9" font-weight="700" fill="#ffffff" text-anchor="middle">• GP health record</text>
            <text x="184" y="92" font-size="9" font-weight="700" fill="#ffffff" text-anchor="middle">• Book appointments</text>
            <text x="184" y="114" font-size="8.5" font-weight="800" fill="#78d38c" text-anchor="middle">Secure NHS Login ✓</text>
            <!-- Council Portal -->
            <rect x="250" y="15" width="105" height="115" rx="6" fill="#f8fafc" stroke="#94a3b8"/>
            <text x="302" y="38" font-size="11" font-weight="900" fill="#0f172a" text-anchor="middle">LOCAL COUNCIL</text>
            <text x="302" y="60" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">• Council Tax</text>
            <text x="302" y="76" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">• Waste &amp; recycling</text>
            <text x="302" y="92" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">• Electoral roll</text>
            <text x="302" y="114" font-size="8.5" font-weight="800" fill="#0284c7" text-anchor="middle">.gov.uk domain ✓</text>
          </g>"""),
        "golden_rule": 'Access public services directly via GOV.UK or NHS.UK official domains!',
        "watch_out": 'Beware of copycat websites charging fees for free public services.',
        "challenge_prompt": "How can you verify that a website offering driving licence renewals is the legitimate government service?",
        "answer_text": "Check that the URL ends in '.gov.uk' (the official UK government domain)."
    },

    # 38. Consumer Rights for Online Purchases
    {
        "id": "dfs-38",
        "number": 38,
        "title": "Online Consumer Rights &amp; Returns",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Transacting Online",
        "strand_theme": "emerald",
        "dfe_code": "DFS 4.6",
        "rule_heading": "14-Day Cooling-Off Period &amp; Refunds",
        "rule_body": "UK Consumer Contracts Regulations 2013 give statutory rights for online distance shopping: 1. 14 days from delivery date to cancel an order for any reason. 2. A further 14 days to return the item. 3. Full refund including standard delivery cost. Exemptions: Perishables, custom-made goods, unsealed hygiene items.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.6"/>
            <text x="185" y="24" font-size="11.5" font-weight="900" fill="#047857" text-anchor="middle">ONLINE SHOPPING STATUTORY CANCELLATION RIGHTS</text>
            <!-- Timeline bar -->
            <line x1="30" y1="65" x2="340" y2="65" stroke="#cbd5e1" stroke-width="4"/>
            <!-- Point 1 -->
            <circle cx="50" cy="65" r="8" fill="#059669"/>
            <text x="50" y="90" font-size="10" font-weight="800" fill="#0f172a" text-anchor="middle">Day 0</text>
            <text x="50" y="105" font-size="9" font-weight="600" fill="#475569" text-anchor="middle">Item delivered</text>
            <!-- Point 2 -->
            <circle cx="185" cy="65" r="8" fill="#059669"/>
            <text x="185" y="90" font-size="10" font-weight="800" fill="#0f172a" text-anchor="middle">14 Days</text>
            <text x="185" y="105" font-size="9" font-weight="700" fill="#047857" text-anchor="middle">Cooling-off notice</text>
            <text x="185" y="120" font-size="8.5" font-weight="600" fill="#64748b" text-anchor="middle">Cancel for any reason</text>
            <!-- Point 3 -->
            <circle cx="320" cy="65" r="8" fill="#059669"/>
            <text x="320" y="90" font-size="10" font-weight="800" fill="#0f172a" text-anchor="middle">+14 Days</text>
            <text x="320" y="105" font-size="9" font-weight="700" fill="#047857" text-anchor="middle">Return item</text>
            <text x="320" y="120" font-size="8.5" font-weight="600" fill="#64748b" text-anchor="middle">Receive full refund</text>
          </g>"""),
        "golden_rule": 'Online orders give a statutory 14-day cooling-off cancellation right!',
        "watch_out": 'Perishable and custom-made items are exempt from statutory returns.',
        "challenge_prompt": "A customer purchases a pair of standard trainers online. How many days do they legally have after delivery to cancel the purchase?",
        "answer_text": "14 calendar days from the day of delivery under the Consumer Contracts Regulations."
    },

    # 39. Digital Receipts, Invoices & Tracking
    {
        "id": "dfs-39",
        "number": 39,
        "title": "Digital Receipts &amp; Order Tracking",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Transacting Online",
        "strand_theme": "emerald",
        "dfe_code": "DFS 4.7",
        "rule_heading": "Saving Proof of Purchase &amp; Tracking",
        "rule_body": "Keep accurate records for online transactions: 1. Save confirmation emails and PDF receipts in a dedicated 'Purchases' email folder. 2. Record the Order ID, vendor name, and date. 3. Use parcel tracking numbers to track courier delivery progress. 4. Inspect goods promptly on arrival.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.6"/>
            <!-- Journey steps -->
            <rect x="15" y="15" width="165" height="55" rx="6" fill="#ffffff" stroke="#94a3b8"/>
            <text x="25" y="33" font-size="10" font-weight="800" fill="#0f172a">1. Order Confirmation Email</text>
            <text x="25" y="52" font-size="9" font-weight="600" fill="#059669">Order #GB-98402 • £49.99</text>
            <rect x="190" y="15" width="165" height="55" rx="6" fill="#ffffff" stroke="#94a3b8"/>
            <text x="200" y="33" font-size="10" font-weight="800" fill="#0f172a">2. Courier Tracking ID</text>
            <text x="200" y="52" font-size="9" font-weight="600" fill="#2563eb">DPD Tracking: In Transit</text>
            <rect x="15" y="80" width="165" height="55" rx="6" fill="#ffffff" stroke="#94a3b8"/>
            <text x="25" y="98" font-size="10" font-weight="800" fill="#0f172a">3. Delivery Confirmation</text>
            <text x="25" y="117" font-size="9" font-weight="600" fill="#059669">Signed / Left in porch photo</text>
            <rect x="190" y="80" width="165" height="55" rx="6" fill="#ffffff" stroke="#94a3b8"/>
            <text x="200" y="98" font-size="10" font-weight="800" fill="#0f172a">4. File PDF Tax Receipt</text>
            <text x="200" y="117" font-size="9" font-weight="600" fill="#475569">Retain for warranty &amp; tax</text>
          </g>"""),
        "golden_rule": 'Save order confirmations into a dedicated receipts folder or cloud PDF!',
        "watch_out": 'Retailers can close accounts — always save an offline copy of receipts.',
        "challenge_prompt": "What key piece of information in an order confirmation email is required when contacting customer support about a missing parcel?",
        "answer_text": "The Order Reference Number (Order ID)."
    },

    # 40. Managing Recurring Subscriptions
    {
        "id": "dfs-40",
        "number": 40,
        "title": "Subscriptions &amp; Auto-Renewals",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Transacting Online",
        "strand_theme": "emerald",
        "dfe_code": "DFS 4.8",
        "rule_heading": "Free Trial Traps &amp; Direct Debit Guarantee",
        "rule_body": "Managing online subscriptions: 1. 'Free trials' automatically roll into paid monthly recurring subscriptions unless cancelled prior to renewal. 2. Set a calendar alert 2 days before the trial finishes. 3. Manage subscriptions via Apple App Store / Google Play subscriptions. 4. Direct Debit Guarantee covers unnotified debits.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.6"/>
            <!-- Free trial step -->
            <rect x="15" y="15" width="105" height="115" rx="6" fill="#eff6ff" stroke="#3b82f6"/>
            <text x="67" y="36" font-size="10.5" font-weight="900" fill="#1e40af" text-anchor="middle">FREE TRIAL</text>
            <text x="67" y="58" font-size="9" font-weight="700" fill="#1e3a8a" text-anchor="middle">Card details taken</text>
            <text x="67" y="74" font-size="9" font-weight="700" fill="#1e3a8a" text-anchor="middle">30 days free</text>
            <text x="67" y="105" font-size="8.5" font-weight="800" fill="#ea580c" text-anchor="middle">Auto-bills if forgotten</text>
            <!-- Calendar alert step -->
            <rect x="132" y="15" width="105" height="115" rx="6" fill="#fefce8" stroke="#ca8a04"/>
            <text x="184" y="36" font-size="10.5" font-weight="900" fill="#854d0e" text-anchor="middle">CALENDAR ALERT</text>
            <text x="184" y="58" font-size="9" font-weight="700" fill="#854d0e" text-anchor="middle">Set reminder on</text>
            <text x="184" y="74" font-size="9" font-weight="700" fill="#854d0e" text-anchor="middle">Day 28 of 30</text>
            <text x="184" y="105" font-size="8.5" font-weight="800" fill="#059669" text-anchor="middle">Decision Point ✓</text>
            <!-- App Store Settings -->
            <rect x="250" y="15" width="105" height="115" rx="6" fill="#f8fafc" stroke="#94a3b8"/>
            <text x="302" y="36" font-size="10.5" font-weight="900" fill="#0f172a" text-anchor="middle">CANCELLATION</text>
            <text x="302" y="58" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">Settings &gt; Subscriptions</text>
            <text x="302" y="74" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">Tap 'Cancel Sub'</text>
            <text x="302" y="105" font-size="8.5" font-weight="800" fill="#dc2626" text-anchor="middle">Deleting app ≠ cancel</text>
          </g>"""),
        "golden_rule": 'Set a calendar alert to review or cancel free trials before renewal!',
        "watch_out": 'Deleting an app does NOT cancel an active recurring paid subscription.',
        "challenge_prompt": "If you delete a paid fitness application from your smartphone, will your recurring monthly payments stop automatically?",
        "answer_text": "No. You must explicitly cancel the subscription inside your device's App Store / Google Play account settings or provider website."
    }
]

for card in CARDS:
    ET.fromstring(card["svg_html"])
print(f"Validated DFS Area 4: {len(CARDS)} cards")
