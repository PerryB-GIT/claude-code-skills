# Product Management - Frameworks & Best Practices

## Product Management Philosophy
```
"Fall in love with the problem, not the solution."

PRODUCT MANAGER'S JOB:
1. Understand the customer deeply
2. Define the right problem to solve
3. Align stakeholders on the solution
4. Ensure successful delivery and adoption
5. Measure outcomes and iterate
```

---

## Product Strategy

### Product Vision Template
```markdown
## Product Vision

**For** [target customer]
**Who** [statement of need/opportunity]
**The** [product name]
**Is a** [product category]
**That** [key benefit/reason to buy]
**Unlike** [primary competitive alternative]
**Our product** [primary differentiation]

---

EXAMPLE:
For busy professionals
Who struggle to stay organized
The TaskFlow app
Is a smart task manager
That automatically prioritizes your day
Unlike traditional to-do lists
Our product learns your habits and adapts

---

### One-Liner
[Product] helps [audience] to [outcome] by [how].
```

### Product Strategy Framework
```
VISION: Where are we going? (3-5 year horizon)
↓
STRATEGY: How will we get there? (1-2 year horizon)
↓
ROADMAP: What will we build? (Quarterly)
↓
BACKLOG: What are we building now? (Sprints)

STRATEGY ELEMENTS:
1. Target Market: Who are we serving?
2. Value Proposition: Why will they choose us?
3. Competitive Advantage: How will we win?
4. Business Model: How will we make money?
5. Success Metrics: How will we measure progress?
```

### OKRs (Objectives & Key Results)
```
OBJECTIVE: Qualitative, inspiring goal
KEY RESULTS: Quantitative measures of success

FORMULA:
"We will [Objective] as measured by [Key Results]"

EXAMPLE:
OBJECTIVE: Become the preferred solution for SMB teams

KEY RESULTS:
- KR1: Increase SMB signups from 1,000 to 3,000/month
- KR2: Achieve 40% SMB trial-to-paid conversion (from 25%)
- KR3: Reach NPS of 50 among SMB customers (from 35)

RULES:
- 3-5 OKRs per quarter
- 2-4 Key Results per Objective
- KRs should be ambitious (70% achievement = success)
- Review weekly, grade quarterly
```

---

## Customer Discovery

### Jobs-to-be-Done (JTBD) Framework
```
"People don't want a quarter-inch drill, they want a quarter-inch hole."

JOB STATEMENT:
When [situation], I want to [motivation], so I can [outcome].

EXAMPLE:
When I'm planning a project, I want to see all dependencies,
so I can identify risks before they become problems.

JOB COMPONENTS:
- Functional: The practical task
- Emotional: How they want to feel
- Social: How they want to be perceived

DISCOVERY QUESTIONS:
- Tell me about the last time you [job to be done]...
- What were you trying to accomplish?
- What made that hard?
- What did you do instead?
- How did that make you feel?
```

### User Persona Template
```markdown
## User Persona: [Name]

### Demographics
- **Role**: [Job title]
- **Company Size**: [Range]
- **Industry**: [Sector]
- **Experience**: [Years in role]

### Goals
What are they trying to achieve?
1. [Goal 1]
2. [Goal 2]

### Frustrations
What gets in their way?
1. [Pain point 1]
2. [Pain point 2]

### Behaviors
- Uses [tools]
- Works [remote/office/hybrid]
- Reports to [role]
- Evaluates tools by [criteria]

### Quote
"[Something they might say that captures their mindset]"

### How We Help
[How our product addresses their needs]
```

### Customer Interview Guide
```
BEFORE THE INTERVIEW:
□ Clear hypothesis to test
□ Questions prepared (open-ended)
□ Recording consent ready
□ Note-taker assigned

INTERVIEW STRUCTURE (45-60 min):
1. Intro & Warm-up (5 min)
   - Thank them
   - Explain purpose
   - Get consent to record

2. Context (10 min)
   - Tell me about your role
   - Walk me through a typical day/week
   - What tools do you use?

3. Problem Exploration (20 min)
   - Tell me about the last time you [problem area]
   - What happened? What did you do?
   - What was frustrating about that?
   - What did you try?
   - How did you feel?

4. Solution Exploration (10 min)
   - How do you solve this today?
   - What would make this easier?
   - Show concept and get reaction

5. Wrap-up (5 min)
   - Anything else I should know?
   - Can I follow up?
   - Thank them

AFTER THE INTERVIEW:
□ Debrief immediately
□ Key quotes captured
□ Insights documented
□ Update hypothesis
```

---

## Product Requirements

### PRD Template (Product Requirements Document)
```markdown
# PRD: [Feature Name]

## Overview
| Field | Value |
|-------|-------|
| Author | |
| Status | Draft/In Review/Approved |
| Last Updated | |
| Target Release | |

## Problem Statement
### What problem are we solving?
[Clear description of the customer problem]

### Who has this problem?
[Target user persona]

### Why is this important now?
[Business context, urgency]

### How do we know this is a problem?
[Evidence: interviews, data, support tickets]

## Goals & Success Metrics
### Objectives
1. [Objective 1]

### Key Results
| Metric | Current | Target |
|--------|---------|--------|
| [Metric 1] | X | Y |

### Non-Goals
- [What we're explicitly NOT doing]

## Solution Overview
### Proposed Solution
[High-level description]

### User Stories
As a [user type], I want to [action], so that [benefit].

1. As a [user], I want to...
2. As a [user], I want to...

### User Flow
[Diagram or step-by-step flow]

### Wireframes/Mockups
[Links to designs]

## Detailed Requirements
### Functional Requirements
| ID | Requirement | Priority |
|----|-------------|----------|
| FR1 | [Requirement] | Must Have |
| FR2 | [Requirement] | Should Have |

### Non-Functional Requirements
- Performance: [Response time, load handling]
- Security: [Requirements]
- Accessibility: [WCAG level]
- Compatibility: [Browsers, devices]

## Technical Considerations
### Dependencies
- [System/API dependencies]

### Technical Constraints
- [Limitations to be aware of]

### Open Questions
- [ ] [Question for engineering]

## Go-to-Market
### Release Plan
- [ ] Beta/Early access
- [ ] Documentation
- [ ] Announcement

### Training
- [ ] CS team training
- [ ] Help docs

## Appendix
### Research
[Links to research]

### Competitive Analysis
[How competitors solve this]
```

### User Story Format
```
AS A [user type]
I WANT TO [action/capability]
SO THAT [benefit/value]

ACCEPTANCE CRITERIA:
Given [context]
When [action]
Then [expected result]

EXAMPLE:
AS A project manager
I WANT TO filter tasks by assignee
SO THAT I can see each team member's workload

ACCEPTANCE CRITERIA:
Given I am viewing the task list
When I select a team member from the filter dropdown
Then only tasks assigned to that person are displayed
And the filter selection persists until cleared
And I can select multiple assignees
```

### Feature Prioritization (RICE)
```
| Feature | Reach | Impact | Confidence | Effort | Score |
|---------|-------|--------|------------|--------|-------|
| Feature A | 5000 | 2 | 80% | 2 | 4000 |
| Feature B | 1000 | 3 | 90% | 1 | 2700 |
| Feature C | 10000 | 1 | 60% | 4 | 1500 |

REACH: Users/quarter affected
IMPACT: 0.25 (minimal) to 3 (massive)
CONFIDENCE: 0-100%
EFFORT: Person-months

SCORE = (Reach × Impact × Confidence) / Effort
```

---

## Product Roadmap

### Roadmap Best Practices
```
DO:
✓ Organize by outcomes/themes, not features
✓ Show timeframes (Now, Next, Later)
✓ Connect to strategy and OKRs
✓ Keep it high-level for external sharing
✓ Update regularly (monthly minimum)

DON'T:
✗ Commit to specific dates too far out
✗ Show every feature ever requested
✗ Treat it as a contract
✗ Forget to communicate changes
```

### Theme-Based Roadmap Template
```markdown
## Product Roadmap: Q1-Q2 2024

### Now (This Quarter)
**Theme: Onboarding Excellence**
Outcome: Reduce time-to-value for new users

- Guided setup wizard
- Interactive tutorials
- Improved documentation

Metrics:
- Day-1 activation: 40% → 60%
- Support tickets (onboarding): -30%

---

### Next (Next Quarter)
**Theme: Team Collaboration**
Outcome: Enable teams to work together seamlessly

- Real-time editing
- Comments and mentions
- Team dashboards

---

### Later (2+ Quarters)
**Theme: Enterprise Ready**
Outcome: Meet enterprise requirements for large deals

- SSO/SAML
- Audit logs
- Advanced permissions

---

### Not Now (Backlog)
- Mobile app v2
- AI-powered suggestions
- Custom integrations marketplace
```

---

## Product Metrics

### Key Product Metrics
```
ACQUISITION:
- Signups
- Activation rate (% completing key action)
- Traffic sources

ENGAGEMENT:
- DAU/MAU ratio
- Session duration
- Feature adoption

RETENTION:
- D1, D7, D30 retention
- Churn rate
- Cohort retention curves

REVENUE:
- MRR/ARR
- ARPU
- LTV
- Expansion revenue

SATISFACTION:
- NPS (Net Promoter Score)
- CSAT (Customer Satisfaction)
- Feature satisfaction
```

### North Star Metric
```
ONE metric that best captures the value you deliver.

EXAMPLES:
- Slack: Daily active users sending messages
- Airbnb: Nights booked
- Spotify: Time spent listening
- Zoom: Weekly meeting minutes

CHARACTERISTICS:
- Reflects customer value
- Leading indicator of revenue
- Measurable and actionable
- Company can influence
```

### Product Analytics Dashboard
```markdown
## Product Metrics Dashboard

### Health Metrics (Weekly)
| Metric | This Week | Last Week | Trend |
|--------|-----------|-----------|-------|
| DAU | | | |
| WAU | | | |
| Signups | | | |
| Activation | | | |
| Churn | | | |

### Feature Adoption
| Feature | Users | % of DAU | Trend |
|---------|-------|----------|-------|
| [Feature 1] | | | |
| [Feature 2] | | | |

### Funnel
Signup → Activated → Retained → Paid
X → Y% → Z% → W%

### NPS
Score: XX
Promoters: X%
Passives: X%
Detractors: X%
```

---

## Launch Planning

### Go-to-Market Checklist
```markdown
## Launch Checklist: [Feature Name]

### Pre-Launch (2 weeks before)
□ Feature complete and tested
□ Documentation written
□ Support team trained
□ Beta feedback incorporated
□ Marketing assets ready
□ Pricing/packaging finalized

### Launch Day
□ Feature flag enabled
□ Announcement published
□ Email sent to relevant users
□ Social media posted
□ Team available for issues

### Post-Launch (1 week after)
□ Monitor metrics and errors
□ Gather user feedback
□ Address critical issues
□ Publish case study/results
□ Plan iterations
```

### Launch Tiers
```
TIER 1 - Major Launch:
- New product or major feature
- Full marketing campaign
- Press/analyst briefings
- Customer webinar
- Sales enablement

TIER 2 - Standard Launch:
- Significant feature
- Blog post
- Email to users
- In-app announcement
- Support docs

TIER 3 - Minor Launch:
- Enhancement or fix
- Release notes
- In-app tooltip
- Help doc update
```
