# Grant Strategy Agent

Use this skill when evaluating grant opportunities, assessing award probability, coordinating submissions, and managing the grant lifecycle. Works in conjunction with `/grant-research` (discovery) and grant writing tools.

## Agent Role

**Strategic Coordinator** - Evaluates opportunities, prioritizes applications, manages submissions, tracks outcomes.

## Core Capabilities

### 1. Award Probability Assessment
Analyzes grant opportunities and estimates likelihood of success based on:

| Factor | Weight | Scoring Criteria |
|--------|--------|------------------|
| Eligibility Fit | 25% | How closely business matches requirements |
| Competition Level | 20% | Number of applicants, historical award rates |
| Application Quality | 20% | Completeness, narrative strength, budget alignment |
| Track Record | 15% | Prior grants, business credibility |
| Timing | 10% | Deadline proximity, review cycle position |
| Relationship | 10% | Prior contact with agency, referrals |

**Probability Tiers:**
- **High (70-90%)** - Strong fit, low competition, solid application
- **Medium (40-69%)** - Good fit, moderate competition
- **Low (10-39%)** - Partial fit, high competition
- **Long Shot (<10%)** - Weak fit, very competitive

### 2. Submission Coordination
Manages the end-to-end application process:

```
GRANT SUBMISSION WORKFLOW

1. OPPORTUNITY IDENTIFIED (Research Agent)
   └─> Strategy Agent: Probability Assessment

2. GO/NO-GO DECISION
   └─> If GO: Create application project

3. DOCUMENT COLLECTION
   └─> Checklist generation
   └─> Deadline tracking
   └─> Responsibility assignment

4. NARRATIVE DEVELOPMENT (Writing Agent)
   └─> Strategy Agent: Review alignment
   └─> Feedback loop

5. BUDGET PREPARATION
   └─> Cost justification
   └─> Match requirements

6. INTERNAL REVIEW
   └─> Compliance check
   └─> Final edits

7. SUBMISSION
   └─> Portal submission
   └─> Confirmation capture
   └─> Tracking update

8. POST-SUBMISSION
   └─> Follow-up schedule
   └─> Status monitoring
   └─> Outcome recording
```

### 3. Lifecycle Tracking
Maintains status across all grant activities via Google Sheets:

**Pipeline Stages:**
| Stage | Actions | Alerts |
|-------|---------|--------|
| Researching | Gather info, assess fit | - |
| Evaluating | Probability score, go/no-go | - |
| Preparing | Document collection | 14 days to deadline |
| Drafting | Narrative, budget | 7 days to deadline |
| Reviewing | Internal review | 3 days to deadline |
| Submitting | Portal submission | Day of deadline |
| Submitted | Await decision | Monthly check-in |
| Under Review | Agency processing | Status update requests |
| Awarded | Celebrate, fulfill | Reporting deadlines |
| Declined | Debrief, lessons learned | Reapply opportunities |

### 4. Email Alerts & Updates
Automated notifications via Gmail:

| Trigger | Email Content | Recipient |
|---------|---------------|-----------|
| New high-probability opportunity | Grant summary, deadline, action needed | Perry |
| 14 days to deadline | Checklist status, missing items | Perry |
| 7 days to deadline | Urgent: completion status | Perry |
| 3 days to deadline | Final review reminder | Perry |
| Submission confirmed | Confirmation, next steps | Perry |
| Status change | Update notification | Perry |
| Decision received | Outcome, next steps | Perry |

## Probability Assessment Framework

### Evaluation Checklist

```markdown
## Grant: [Name]
## Date Assessed: [Date]

### ELIGIBILITY FIT (25 points max)
- [ ] Business structure matches (5)
- [ ] Industry/NAICS eligible (5)
- [ ] Size requirements met (5)
- [ ] Location requirements met (5)
- [ ] Certifications held (5)
SCORE: __/25

### COMPETITION LEVEL (20 points max)
- Historical award rate: ___%
- Estimated applicants: ___
- [ ] Niche program (fewer applicants) (+5)
- [ ] Broad program (many applicants) (-5)
- [ ] First-time applicant disadvantage (-3)
- [ ] Prior awardee advantage (+3)
SCORE: __/20

### APPLICATION STRENGTH (20 points max)
- [ ] Clear project narrative (5)
- [ ] Realistic budget (5)
- [ ] Strong need statement (5)
- [ ] Measurable outcomes (5)
SCORE: __/20

### TRACK RECORD (15 points max)
- [ ] Prior grant awards (5)
- [ ] Relevant experience (5)
- [ ] Financial stability (5)
SCORE: __/15

### TIMING (10 points max)
- [ ] Early in cycle (+5)
- [ ] Adequate prep time (5)
SCORE: __/10

### RELATIONSHIPS (10 points max)
- [ ] Prior agency contact (5)
- [ ] Referral/introduction (5)
SCORE: __/10

### TOTAL SCORE: __/100
### PROBABILITY TIER: [High/Medium/Low/Long Shot]
### RECOMMENDATION: [Pursue/Consider/Pass]
```

## Coordination Protocol

### With Research Agent
```
RESEARCH AGENT → STRATEGY AGENT

Input: New grant opportunity identified
- Grant details (name, amount, deadline, requirements)
- Initial eligibility assessment
- Source URL

Strategy Agent Actions:
1. Run probability assessment
2. Score opportunity
3. Make go/no-go recommendation
4. If GO: Create tracking entry, initiate workflow
5. If NO-GO: Log reason, archive
```

### With Writing Agent
```
STRATEGY AGENT → WRITING AGENT

Input: Approved application for drafting
- Grant requirements document
- Business profile
- Project description
- Budget parameters
- Key messaging points

Writing Agent Deliverables:
1. Project narrative draft
2. Need statement
3. Budget justification
4. Executive summary

Strategy Agent Review:
- Alignment with requirements
- Strength of value proposition
- Compliance check
- Revision requests
```

### With Tracking Systems
```
STRATEGY AGENT → GOOGLE SHEETS

Updates to Opportunities tab:
- Status changes
- Probability scores
- Key dates

Updates to Application Tracker:
- Document checklist progress
- Submission status
- Follow-up actions

Updates to Deadlines:
- New deadline entries
- Reminder scheduling
```

```
STRATEGY AGENT → GMAIL

Sends:
- Deadline reminders (14/7/3/1 day)
- Status update summaries (weekly)
- Decision notifications
- Action required alerts
```

```
STRATEGY AGENT → GOOGLE CALENDAR

Creates:
- Application deadlines
- Internal review dates
- Submission dates
- Follow-up reminders
- Reporting deadlines (if awarded)
```

## Decision Matrices

### Go/No-Go Decision
| Probability | Award Amount | Time Available | Decision |
|-------------|--------------|----------------|----------|
| High | Any | Any | **GO** |
| Medium | >$50K | >30 days | **GO** |
| Medium | >$50K | <30 days | Consider |
| Medium | <$50K | Any | Consider |
| Low | >$100K | >60 days | Consider |
| Low | <$100K | Any | **PASS** |
| Long Shot | Any | Any | **PASS** |

### Resource Allocation
| Active Applications | Recommendation |
|---------------------|----------------|
| 0-2 | Add more opportunities |
| 3-5 | Optimal workload |
| 6+ | Prioritize, defer some |

## Reporting

### Weekly Summary Email
```
GRANT PIPELINE SUMMARY - Week of [Date]

ACTIVE APPLICATIONS: [#]
- [Grant 1]: [Status] - Deadline [Date]
- [Grant 2]: [Status] - Deadline [Date]

UPCOMING DEADLINES:
- [Date]: [Grant] - [Action needed]

NEW OPPORTUNITIES IDENTIFIED: [#]
- [Grant]: $[Amount] - Probability: [%]

DECISIONS RECEIVED:
- [Grant]: [Awarded/Declined]

ACTION ITEMS:
1. [Action]
2. [Action]
```

### Monthly Report
```
GRANT ACTIVITY REPORT - [Month Year]

APPLICATIONS SUBMITTED: [#]
TOTAL VALUE APPLIED: $[Amount]
DECISIONS RECEIVED: [#]
- Awarded: [#] ($[Amount])
- Declined: [#]
- Pending: [#]

WIN RATE: [%]
PIPELINE VALUE: $[Amount]

TOP OPPORTUNITIES FOR NEXT MONTH:
1. [Grant] - $[Amount] - Deadline [Date]
```

## Integration Points

### MCP Tools Used
- `mcp__gmail__gmail_send_email` - Alerts and updates
- `mcp__google-calendar__calendar_create_event` - Deadlines
- `mcp__google-sheets__*` - Tracking spreadsheet
- `WebSearch` - Competition research
- `WebFetch` - Grant details

### Related Skills
- `/grant-research` - Opportunity discovery
- `/grant-writing` - Application content (future)
- `/creating-financial-models` - Budget development

## Commands

### Quick Actions
- `/grant-strategy assess [grant-name]` - Run probability assessment
- `/grant-strategy status` - Pipeline summary
- `/grant-strategy deadlines` - Upcoming deadlines
- `/grant-strategy submit [grant-name]` - Initiate submission workflow

## Example Session

```
User: Assess the MassVentures START grant for Support Forge

Agent:
## Probability Assessment: MassVentures START

### Grant Details
- Program: START (matching SBIR Phase I)
- Amount: Up to $100K
- Deadline: Rolling (after federal award)
- Requirement: Must have SBIR Phase I award

### Assessment

ELIGIBILITY FIT: 5/25
- ❌ Requires active SBIR Phase I award
- ✅ MA-based business
- ✅ For-profit structure

COMPETITION: 15/20
- Low competition (must already have SBIR)
- ~50 awards/year

APPLICATION STRENGTH: N/A (requires SBIR first)

TRACK RECORD: 10/15
- No prior SBIR awards
- Business credibility: Good

TIMING: N/A

RELATIONSHIPS: 5/10
- No prior MassVentures contact

### TOTAL: 35/100 (incomplete - prerequisite not met)
### RECOMMENDATION: PASS for now

### Path Forward:
1. Apply for SBIR Phase I first (DOD, NSF, NIH)
2. If awarded, START becomes HIGH probability
3. Consider SBIR application as prerequisite project

Would you like me to search for SBIR opportunities that could unlock START funding?
```
