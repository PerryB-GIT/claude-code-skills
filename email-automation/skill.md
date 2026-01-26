# Email Automation & Sequences

## Automation Fundamentals

### Trigger Types
| Trigger | Example | Use Case |
|---------|---------|----------|
| Time-based | X days after signup | Onboarding series |
| Action-based | Clicked link | Interest follow-up |
| Event-based | Made purchase | Post-purchase flow |
| Inactivity | No open in 30 days | Re-engagement |
| Date-based | Birthday, anniversary | Milestone emails |
| Segment entry | Added to "VIP" | Special treatment |

### Automation Components
```
TRIGGER → DELAY → CONDITION → ACTION → GOAL

Trigger: What starts the automation
Delay: Wait period between steps
Condition: If/then logic (segment, behavior)
Action: Send email, tag, notify, update
Goal: End condition (purchase, reply, etc.)
```

---

## Core Automation Flows

### 1. Welcome Series
```
Purpose: Introduce brand, build relationship, drive first action

TRIGGER: New subscriber

Day 0 (Immediate):
├── Email 1: Welcome + Quick Win
│   - Thank them for subscribing
│   - Deliver promised lead magnet
│   - Set expectations (what/when to expect)
│   - One quick tip they can use immediately
│   - CTA: Simple first action

Day 2:
├── Email 2: Your Story
│   - Who you are / company origin
│   - Why you do what you do
│   - Values and mission
│   - CTA: Follow on social / reply with question

Day 4:
├── Email 3: Best Resources
│   - Top 3 pieces of content
│   - Most popular products/services
│   - CTA: Explore [specific resource]

Day 7:
├── Email 4: Social Proof
│   - Customer success story
│   - Testimonials
│   - Results/outcomes
│   - CTA: See more case studies

Day 10:
├── Email 5: Soft Sell
│   - Address common objection
│   - Introduce offer/product
│   - CTA: Try / Buy / Book call

GOAL: Clicks email 5 CTA → Exit to Sales sequence
```

### 2. Onboarding (SaaS)
```
Purpose: Drive activation and reduce churn

TRIGGER: Account created

Immediate:
├── Email 1: Welcome + Getting Started
│   - Login credentials
│   - Link to quick start guide
│   - First step to take
│   - Support resources

Day 1:
├── CONDITION: Completed first action?
│   ├── YES → Skip to Day 3
│   └── NO → Email 2: "Let's get you set up"
│       - Specific instructions for first action
│       - Video walkthrough link
│       - Offer help

Day 3:
├── Email 3: Feature Highlight
│   - Introduce key feature #1
│   - Use case example
│   - CTA: Try this feature

Day 5:
├── CONDITION: Used feature?
│   ├── YES → Email 4a: Advanced tips
│   └── NO → Email 4b: Different approach
│       - Alternative use case
│       - Offer 1:1 demo

Day 7:
├── Email 5: Check-in
│   - How's it going?
│   - Common questions FAQ
│   - CTA: Reply with feedback

Day 14:
├── Email 6: Success Story
│   - Customer case study
│   - Results achieved
│   - CTA: Upgrade / Add team members

Day 21:
├── CONDITION: Trial ending soon?
│   └── Email 7: Trial reminder
│       - Days left
│       - What they'll lose
│       - CTA: Upgrade now

GOAL: Paid conversion → Exit to Customer sequence
```

### 3. Lead Nurture (B2B)
```
Purpose: Move leads through funnel to sales-ready

TRIGGER: Downloaded content / Attended webinar

Day 0:
├── Email 1: Deliver Content
│   - Thank you
│   - Resource delivery
│   - What to do with it

Day 3:
├── Email 2: Related Content
│   - Complementary resource
│   - Deeper dive on topic
│   - CTA: Download / Read

Day 7:
├── Email 3: Case Study
│   - How [company] solved [problem]
│   - Specific results
│   - CTA: See full case study

Day 10:
├── CONDITION: Engaged with emails?
│   ├── HIGH (2+ clicks) → Fast track to sales
│   └── LOW → Continue nurture

Day 14:
├── Email 4: Educational
│   - Industry insight
│   - How-to content
│   - Position as thought leader

Day 21:
├── Email 5: Problem Agitation
│   - Common pain points
│   - Cost of inaction
│   - CTA: Assess your situation

Day 28:
├── Email 6: Soft Pitch
│   - Introduce solution
│   - Benefits overview
│   - CTA: Schedule demo

GOAL: Schedules demo → Exit to Sales sequence
```

### 4. Abandoned Cart
```
Purpose: Recover lost sales

TRIGGER: Added to cart but didn't purchase

1 Hour:
├── Email 1: Reminder
│   - "You left something behind"
│   - Product image
│   - CTA: Complete purchase
│   - (No discount yet)

24 Hours:
├── CONDITION: Still not purchased?
│   └── Email 2: Benefits
│       - Why [product] is great
│       - Customer reviews
│       - FAQ/objection handling
│       - CTA: Return to cart

72 Hours:
├── CONDITION: Still not purchased?
│   └── Email 3: Urgency/Incentive
│       - Limited stock warning OR
│       - Small discount (10%)
│       - CTA: Save X% now

GOAL: Purchase → Exit + Tag as Customer
```

### 5. Post-Purchase
```
Purpose: Deliver value, reduce returns, drive repeat purchase

TRIGGER: Order completed

Immediate:
├── Email 1: Order Confirmation
│   - Order details
│   - What to expect next
│   - Support contact

Day 1-3 (When shipped):
├── Email 2: Shipping Notification
│   - Tracking info
│   - Delivery estimate

Day 5 (After delivery):
├── Email 3: Getting Started
│   - How to use product
│   - Tips for best results
│   - Video tutorials

Day 10:
├── Email 4: Check-In
│   - How's it going?
│   - Tips based on product
│   - CTA: Reply with feedback

Day 14:
├── CONDITION: Satisfied?
│   └── Email 5: Review Request
│       - Leave a review
│       - Referral program intro

Day 30:
├── Email 6: Related Products
│   - Complementary items
│   - Replenishment (if consumable)
│   - CTA: Shop accessories

GOAL: Second purchase → Add to VIP segment
```

### 6. Re-Engagement
```
Purpose: Win back inactive subscribers

TRIGGER: No email open in 60 days

Day 0:
├── Email 1: "We miss you"
│   - Acknowledge absence
│   - What they've missed
│   - Compelling content preview
│   - CTA: Re-engage

Day 7:
├── CONDITION: Opened?
│   ├── YES → Exit, update engagement score
│   └── NO → Email 2: Incentive
│       - Special offer / discount
│       - Exclusive content
│       - CTA: Claim offer

Day 14:
├── CONDITION: Opened?
│   ├── YES → Exit, update engagement score
│   └── NO → Email 3: Breakup
│       - "Is this goodbye?"
│       - Update preferences option
│       - Unsubscribe if not interested
│       - CTA: Stay subscribed

Day 21:
├── CONDITION: No engagement?
│   └── ACTION: Remove from list / Move to sunset list
       - Improves deliverability
       - Clean list
```

---

## Conditional Logic Examples

### If/Then Branches
```
# Engagement-Based
IF opens > 50% of emails in last 30 days
  THEN → Tag as "Highly Engaged"
  ELSE → Continue standard flow

# Behavior-Based
IF clicked pricing page
  THEN → Send sales-focused content
  ELSE → Send educational content

# Segment-Based
IF industry = "SaaS"
  THEN → Send SaaS case study
ELSE IF industry = "E-commerce"
  THEN → Send E-commerce case study
ELSE
  THEN → Send general case study

# Purchase-Based
IF has purchased
  THEN → Skip pitch emails
  ELSE → Include soft pitch
```

### Lead Scoring Triggers
```
# Assign Points
+10: Opened email
+20: Clicked link
+50: Visited pricing page
+30: Downloaded content
+100: Requested demo
-10: No open in 30 days
-25: Unsubscribed

# Score Thresholds
0-50: Cold → Nurture sequence
51-100: Warm → Targeted content
101-200: Hot → Sales outreach
200+: Qualified → Direct to sales
```

---

## Email Templates for Automation

### Welcome Email
```
Subject: Welcome to [Brand] - here's your [lead magnet]

Hey [Name]!

Thanks for joining [X] other [audience type] who get [value prop].

As promised, here's your [lead magnet]:
👉 [DOWNLOAD LINK]

Here's how to get the most out of it:
1. [Quick tip 1]
2. [Quick tip 2]
3. [Quick tip 3]

Over the next few days, I'll send you [what to expect].

In the meantime, hit reply and tell me: [engagement question]

Talk soon,
[Your name]
```

### Nurture Email (Value-First)
```
Subject: [Number] ways to [solve problem]

Hey [Name],

Quick one for you today.

I see a lot of [audience] struggling with [problem]. Here's what works:

**1. [Tip 1]**
[Brief explanation]

**2. [Tip 2]**
[Brief explanation]

**3. [Tip 3]**
[Brief explanation]

Want to go deeper? Check out [related resource]:
[LINK]

[Sign off]
```

### Abandoned Cart Email
```
Subject: You left something behind 👀

Hey [Name],

Looks like you didn't finish your order:

[PRODUCT IMAGE]
[PRODUCT NAME]
[PRICE]

[Complete Your Order →]

Questions? Just reply to this email and I'll help.

[Sign off]
```

### Re-Engagement Email
```
Subject: [Name], are you still there?

Hey [Name],

I noticed you haven't opened our emails in a while.

No hard feelings - inboxes get busy!

But I wanted to check: do you still want to hear from us?

If yes, click here to stay subscribed:
[STAY SUBSCRIBED]

If not, no worries - you can [unsubscribe here].

Either way, thanks for being part of our community.

[Sign off]
```

---

## Best Practices

### Timing & Delays
```
# Welcome series: 2-3 day gaps
# Nurture series: 3-7 day gaps
# Abandoned cart: Hours, not days
# Re-engagement: 7 day gaps

# Send Times (Test These)
B2B: Tuesday-Thursday, 10 AM or 2 PM
B2C: Evenings and weekends

# Don't
- Send back-to-back (wait 24h minimum)
- Email on major holidays
- Send more than 1/day (unless urgent)
```

### Exit Conditions
```
Every automation needs:
1. Goal (what ends it successfully)
2. Timeout (max duration)
3. Unsubscribe handling
4. Error handling
```

### Testing Checklist
```
□ All links work
□ Personalization renders correctly
□ Timing/delays are correct
□ Conditions work as expected
□ Exit goals fire properly
□ Tags/segments apply correctly
□ Test with real data (not placeholders)
```

---

## Automation by Platform

### Using Zapier (Perry's Setup)
```
Trigger: New subscriber in [form/tool]
→ Add to email list (ESP)
→ Add tag "New Lead"
→ Trigger welcome sequence

Trigger: Form submission
→ Create contact in CRM
→ Send notification to Slack
→ Start nurture sequence

Trigger: Purchase in Stripe
→ Update customer tag
→ Start post-purchase sequence
→ Create task in CRM for follow-up
```

### Gmail + Google Sheets (Simple Automation)
```
1. Collect leads in Google Sheet
2. Use Zapier to trigger emails via Gmail MCP
3. Track opens/clicks in Sheet
4. Manual follow-up based on engagement
```

---

## Metrics to Track

| Metric | What It Tells You | Target |
|--------|-------------------|--------|
| Completion Rate | % finishing sequence | 60%+ |
| Drop-off Point | Where people leave | Identify & fix |
| Time to Goal | Speed through funnel | Minimize |
| Revenue per Sequence | $ attributed | Increase |
| Unsubscribe Rate | Content/frequency fit | <2% per sequence |
