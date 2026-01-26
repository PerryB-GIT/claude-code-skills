# Email Marketing Agent

## Quick Reference - Perry's Email Tools
- **Gmail MCP**: Direct send/draft via `mcp__gmail__send_email`, `mcp__gmail__draft_email`
- **Zapier MCP**: Automation flows, integrations with ESPs
- **SendGrid**: Transactional + marketing (credentials in auth-reference.md)
- **ImprovMX**: Email forwarding for client domains

---

## Campaign Strategy Framework

### Campaign Types
| Type | Purpose | Frequency | Key Metrics |
|------|---------|-----------|-------------|
| Newsletter | Value/updates | Weekly/Monthly | Open rate, clicks |
| Promotional | Sales/offers | As needed | Conversion, revenue |
| Drip/Nurture | Lead nurturing | Automated | Completion rate |
| Transactional | Receipts/confirms | Triggered | Delivery rate |
| Re-engagement | Win back inactive | Quarterly | Reactivation rate |
| Onboarding | New user education | Automated | Activation rate |
| Cold Outreach | Lead generation | Campaigns | Reply rate |

### Campaign Planning Template
```markdown
## Campaign Brief

**Campaign Name**:
**Type**: [Newsletter/Promo/Drip/etc.]
**Goal**: [Specific, measurable objective]
**Target Audience**: [Segment description]
**Send Date/Time**:
**From Name/Email**:

### Content
- **Subject Line**:
- **Preview Text**:
- **Primary CTA**:
- **Secondary CTA**:

### Success Metrics
- Target Open Rate: X%
- Target Click Rate: X%
- Target Conversion: X%

### A/B Test Plan
- Variable: [Subject/Send time/CTA]
- Variants: A: ___ | B: ___
- Sample size: X%
- Winner criteria: [Open rate after 4 hours]
```

---

## Subject Line Optimization

### Formulas That Work
```
# Curiosity Gap
"The one thing most [audience] get wrong about [topic]"
"Why [counterintuitive statement]"
"What [industry experts] won't tell you about [topic]"

# Benefit-Driven
"Get [benefit] in [timeframe]"
"[Number] ways to [achieve desired outcome]"
"How to [solve problem] without [pain point]"

# Urgency/Scarcity
"[X hours] left: [offer]"
"Last chance: [benefit]"
"Closing tonight: [opportunity]"

# Personalization
"[Name], your [personalized item] is ready"
"Quick question about [their company/project]"
"Thoughts on [recent action they took]?"

# Social Proof
"How [known company] achieved [result]"
"Join [number] others who [action]"
"[Name] recommended I reach out"

# List/Number
"[Number] [adjective] ways to [benefit]"
"The top [number] [topic] trends for [year]"
```

### Subject Line Checklist
- [ ] Under 50 characters (mobile-friendly)
- [ ] No spam triggers (FREE, URGENT, !!!, ALL CAPS)
- [ ] Creates curiosity or promises value
- [ ] Matches email content (no bait-and-switch)
- [ ] Personalization token works (test!)
- [ ] Preview text complements (doesn't repeat)

### Spam Trigger Words to Avoid
```
# High Risk
FREE, WINNER, CONGRATULATIONS, ACT NOW
URGENT, LIMITED TIME, CLICK HERE, BUY NOW
100%, GUARANTEED, NO OBLIGATION, RISK-FREE
$$, Make money, Cash bonus, Double your

# Moderate Risk
Reminder, Don't miss, Last chance, Expires
Deal, Discount, Sale, Offer, Promo
```

---

## Email Copywriting

### Email Structure (AIDA)
```
**Attention** - Hook in first line
**Interest** - Relevant problem/opportunity
**Desire** - Benefits + social proof
**Action** - Clear, single CTA
```

### Opening Lines That Work
```
# Problem-Agitation
"If you're struggling with [problem], you're not alone..."
"Ever feel like [frustrating situation]?"

# Story
"Last week, I was [relatable situation]..."
"A client recently asked me..."

# Direct
"I'm reaching out because [specific reason]..."
"Quick question:"

# Value-First
"I put together [resource] that I thought you'd find useful..."
"Here's the [thing] I promised..."
```

### CTA Best Practices
```
# Button Text (Action-Oriented)
✓ "Get My Free Guide"
✓ "Start My Trial"
✓ "Book My Call"
✓ "Claim My Spot"
✗ "Submit"
✗ "Click Here"
✗ "Learn More"

# CTA Placement
- Primary: Above the fold
- Secondary: After value explanation
- Final: End of email (for skimmers)

# One CTA Rule
- Focus on ONE primary action
- Multiple CTAs = decision paralysis
- Exception: Newsletters (curated links)
```

### Email Templates

#### Welcome Email
```
Subject: Welcome to [Company] - Here's what's next

Hi [Name],

Thanks for joining [Company]! I'm [Your name], and I'll be your guide.

Here's what you can expect:
• [Benefit 1]
• [Benefit 2]
• [Benefit 3]

To get started, [simple first action]:

[CTA Button: Get Started]

Questions? Just hit reply - I read every email.

[Signature]

P.S. [Bonus tip or resource]
```

#### Promotional Email
```
Subject: [X% off] [Product] - [timeframe] only

Hi [Name],

[One sentence about the offer]

**What you get:**
✓ [Benefit 1]
✓ [Benefit 2]
✓ [Benefit 3]

**Regular price:** $XXX
**Your price:** $XX (save $XX)

[CTA Button: Claim Your Discount]

This offer expires [date/time].

[Signature]
```

#### Cold Outreach Email
```
Subject: Quick question about [their company]

Hi [Name],

I noticed [specific observation about them/their company].

[One sentence about why you're reaching out - value prop]

[Social proof: "We helped [similar company] achieve [result]"]

Would you be open to a quick 15-min call to see if this could help [their company] too?

[CTA: Book a call / Reply with availability]

[Signature]

P.S. [Personalized detail showing research]
```

#### Follow-Up Sequence
```
Email 1 (Day 0): Initial outreach
Email 2 (Day 3): "Bumping this up" + new angle
Email 3 (Day 7): Value-add (resource/insight)
Email 4 (Day 14): Social proof + soft CTA
Email 5 (Day 21): Breakup email ("Should I close your file?")
```

---

## List Management

### Segmentation Strategies
```
# Demographic
- Industry
- Company size
- Job title/role
- Location

# Behavioral
- Purchase history
- Email engagement (opens, clicks)
- Website activity
- Content downloaded

# Lifecycle Stage
- Lead → MQL → SQL → Customer → Advocate
- Trial → Paid → Churned

# Engagement Level
- Active (opened in last 30 days)
- Engaged (clicked in last 60 days)
- Inactive (no opens in 90+ days)
- At-risk (declining engagement)
```

### List Hygiene
```bash
# Monthly Tasks
1. Remove hard bounces immediately
2. Suppress soft bounces after 3 attempts
3. Remove unsubscribes (required by law)
4. Flag spam complaints for removal
5. Identify inactive subscribers (90+ days)

# Quarterly Tasks
1. Run re-engagement campaign for inactive
2. Remove non-responders from re-engagement
3. Verify email addresses (NeverBounce, ZeroBounce)
4. Deduplicate list
5. Update suppression lists
```

### Growing Your List
```
# Lead Magnets
- Ebooks/Guides
- Checklists/Templates
- Webinars
- Free tools/calculators
- Discount codes
- Exclusive content

# Opt-in Placement
- Homepage popup (exit intent)
- Blog sidebar
- Content upgrades (in-post)
- Footer
- Checkout page
- Social media bio
```

---

## Automation Flows

### Welcome Series (5 emails)
```
Day 0: Welcome + Quick Win
Day 2: Your Story + Values
Day 4: Best Content/Resources
Day 7: Social Proof + Testimonials
Day 10: Soft Pitch + CTA
```

### Abandoned Cart (3 emails)
```
Hour 1: "Did you forget something?"
Hour 24: Benefits reminder + urgency
Hour 72: Final reminder + incentive (optional)
```

### Onboarding (SaaS)
```
Day 0: Welcome + Login details
Day 1: First key action tutorial
Day 3: "Did you try [feature]?"
Day 7: Success story + tips
Day 14: Check-in + support offer
Day 30: Feedback request
```

### Re-engagement
```
Email 1: "We miss you" + what's new
Email 2: Special offer to come back
Email 3: Last chance + "update preferences or unsubscribe"
→ Remove non-responders after Email 3
```

### Post-Purchase
```
Day 0: Order confirmation
Day 1: Shipping notification
Day 3: How to get started / tips
Day 7: Check-in + support
Day 14: Review request
Day 30: Related products / upsell
```

---

## Deliverability

### Authentication Setup
```
# SPF Record
v=spf1 include:_spf.google.com include:sendgrid.net ~all

# DKIM
- Generate key pair in ESP
- Add TXT record to DNS
- Verify in ESP dashboard

# DMARC
_dmarc.domain.com TXT "v=DMARC1; p=quarantine; rua=mailto:dmarc@domain.com"

# BIMI (optional - brand logo in inbox)
- Requires DMARC p=quarantine or reject
- VMC certificate needed
```

### Warmup Strategy (New Domain/IP)
```
Week 1: 50 emails/day to most engaged
Week 2: 100 emails/day
Week 3: 250 emails/day
Week 4: 500 emails/day
Week 5: 1000 emails/day
Week 6+: Gradually increase to full volume

# Rules
- Only send to engaged subscribers initially
- Monitor bounce rate (<2%)
- Monitor spam complaints (<0.1%)
- Pause if metrics spike
```

### Deliverability Checklist
- [ ] SPF, DKIM, DMARC configured
- [ ] Sending domain matches From address
- [ ] List is permission-based (opted in)
- [ ] Unsubscribe link present and working
- [ ] Physical address in footer
- [ ] No spam trigger words in subject
- [ ] Text-to-image ratio balanced
- [ ] Links go to reputable domains
- [ ] Tested with mail-tester.com

### Monitoring Tools
| Tool | Purpose |
|------|---------|
| mail-tester.com | Pre-send spam score |
| MXToolbox | DNS/blacklist check |
| Google Postmaster | Gmail deliverability |
| SendForensics | Inbox placement |
| GlockApps | Multi-ISP testing |

---

## Analytics & Metrics

### Key Metrics
| Metric | Formula | Benchmark |
|--------|---------|-----------|
| Open Rate | Opens / Delivered | 20-25% |
| Click Rate (CTR) | Clicks / Delivered | 2-5% |
| Click-to-Open (CTOR) | Clicks / Opens | 10-15% |
| Bounce Rate | Bounces / Sent | <2% |
| Unsubscribe Rate | Unsubs / Delivered | <0.5% |
| Spam Complaint | Complaints / Delivered | <0.1% |
| Conversion Rate | Conversions / Clicks | Varies |
| List Growth Rate | (New - Lost) / Total | 2-3%/mo |
| Revenue Per Email | Revenue / Emails Sent | Varies |

### Reporting Template
```markdown
## Email Campaign Report: [Campaign Name]

**Send Date**: [Date]
**List Size**: [Number]
**Segment**: [Description]

### Performance Summary
| Metric | Result | Benchmark | Status |
|--------|--------|-----------|--------|
| Delivered | X (X%) | 98%+ | ✓/✗ |
| Opens | X (X%) | 20%+ | ✓/✗ |
| Clicks | X (X%) | 2%+ | ✓/✗ |
| Conversions | X (X%) | X% | ✓/✗ |
| Revenue | $X | $X | ✓/✗ |
| Unsubscribes | X (X%) | <0.5% | ✓/✗ |

### A/B Test Results
- Variant A: [Result]
- Variant B: [Result]
- Winner: [Variant] (+X% improvement)

### Top Performing Links
1. [Link] - X clicks
2. [Link] - X clicks

### Insights & Next Steps
- [Observation 1]
- [Observation 2]
- [Action item for next campaign]
```

---

## Compliance

### CAN-SPAM (US)
```
Required:
✓ Accurate "From" name and email
✓ Non-deceptive subject line
✓ Identify as advertisement (if applicable)
✓ Physical postal address
✓ Clear unsubscribe mechanism
✓ Honor opt-outs within 10 business days

Penalties: Up to $50,120 per violation
```

### GDPR (EU)
```
Required:
✓ Explicit consent (pre-checked boxes = NO)
✓ Clear privacy policy
✓ Easy withdrawal of consent
✓ Data access/deletion on request
✓ Record of consent
✓ Data processing agreement with ESP

Penalties: Up to €20M or 4% of global revenue
```

### CASL (Canada)
```
Required:
✓ Express or implied consent
✓ Sender identification
✓ Unsubscribe mechanism
✓ Contact information

Penalties: Up to $10M per violation
```

### Consent Best Practices
```
# Double Opt-In Flow
1. User submits email
2. Confirmation email sent
3. User clicks confirm link
4. Added to list with timestamp

# Consent Record
- Email address
- Timestamp
- IP address
- Source (which form)
- Consent text shown
```

---

## Tools Integration

### Using Perry's Gmail MCP
```
# Send campaign email
mcp__gmail__send_email
- to: ["recipient@email.com"]
- subject: "Your subject"
- body: "Email content"
- htmlBody: "<html>...</html>"

# Draft for review first
mcp__gmail__draft_email
- Same parameters
- Review in Gmail before sending

# Search past campaigns
mcp__gmail__search_emails
- query: "subject:Newsletter from:me"
```

### Zapier Automations
```
# Useful Zaps
- New subscriber → Welcome email sequence
- Purchase → Post-purchase series
- Form submission → Lead nurture flow
- Abandoned cart → Recovery emails
- Webinar signup → Reminder sequence
```

### ESP Recommendations
| Use Case | Tool | Why |
|----------|------|-----|
| Transactional | SendGrid | Reliability, APIs |
| Marketing | ConvertKit | Creator-focused |
| E-commerce | Klaviyo | Revenue tracking |
| All-in-one | ActiveCampaign | Automation |
| Simple | Mailchimp | Easy start |
| Cold Outreach | Instantly, Lemlist | Warmup, sequences |

---

## Quick Actions

### Pre-Send Checklist
```
□ Subject line tested (no spam triggers)
□ Preview text set
□ From name/email correct
□ Personalization tokens work
□ Links all work (tested!)
□ Images have alt text
□ Mobile preview checked
□ Unsubscribe link works
□ Physical address present
□ Sent test to yourself
□ Spell check complete
□ Send time optimal
```

### Optimal Send Times
```
B2B:
- Tuesday-Thursday
- 10 AM or 2 PM (recipient timezone)

B2C:
- Thursday-Sunday
- 8 PM or weekends

Test for YOUR audience - these are starting points
```

### Emergency: Fix Sent Email
```
1. DON'T send correction immediately
2. Assess severity (broken link vs. wrong offer)
3. If critical: Send correction within 1 hour
4. Subject: "Oops! Here's the correct [thing]"
5. Keep it short and human
6. Turn mistake into engagement opportunity
```
