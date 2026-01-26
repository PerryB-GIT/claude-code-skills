# Risk Management - Identification, Assessment & Mitigation

## Risk Management Philosophy
```
"Risk management is not about avoiding risk. It's about making informed
decisions about which risks to take, which to mitigate, and which to accept."

PRINCIPLES:
1. Identify risks early and continuously
2. Prioritize based on impact and probability
3. Plan responses before risks materialize
4. Monitor and update throughout project
5. Communicate risks transparently
```

---

## Risk Management Process

### The Risk Management Cycle
```
1. IDENTIFY
   - What could go wrong?
   - What opportunities exist?
   ↓
2. ANALYZE
   - How likely is it?
   - What's the impact?
   ↓
3. PLAN RESPONSE
   - How do we address it?
   - Who owns it?
   ↓
4. MONITOR & CONTROL
   - Track risks
   - Execute responses
   - Identify new risks
   ↓
(Loop back to Identify)
```

---

## Risk Identification

### Risk Categories
```
TECHNICAL RISKS:
- Technology complexity
- Integration challenges
- Performance issues
- Security vulnerabilities
- Technical debt

RESOURCE RISKS:
- Key person dependency
- Skill gaps
- Availability constraints
- Turnover/attrition

SCHEDULE RISKS:
- Unrealistic timelines
- Dependencies on others
- Scope creep
- External delays

BUDGET RISKS:
- Cost overruns
- Funding changes
- Vendor pricing
- Currency fluctuation

EXTERNAL RISKS:
- Regulatory changes
- Market conditions
- Competitor actions
- Vendor/partner issues

ORGANIZATIONAL RISKS:
- Stakeholder resistance
- Priority changes
- Political dynamics
- Organizational change
```

### Risk Identification Techniques
```
BRAINSTORMING:
- Gather diverse perspectives
- No criticism during ideation
- Build on others' ideas
- Document everything

CHECKLIST REVIEW:
- Use category lists above
- Reference past projects
- Industry-specific risks
- Regulatory requirements

EXPERT INTERVIEWS:
- Talk to SMEs
- Lessons from similar projects
- Vendor input
- Customer feedback

ASSUMPTION ANALYSIS:
- List all assumptions
- What if each is wrong?
- Which are most critical?

SWOT ANALYSIS:
- Strengths (internal positive)
- Weaknesses (internal negative)
- Opportunities (external positive)
- Threats (external negative)
```

### Risk Statement Format
```
RISK = CAUSE + RISK EVENT + IMPACT

"Due to [cause/condition], there is a risk that [risk event]
may occur, which could result in [impact on objectives]."

EXAMPLES:
"Due to limited testing resources, there is a risk that defects
may not be caught before release, which could result in customer
complaints and emergency patches."

"Due to dependency on external API, there is a risk that API
changes could break integration, which could result in 2-week
delay and additional development costs."
```

---

## Risk Analysis

### Probability and Impact Scale
```
PROBABILITY:
| Level | Score | Description |
|-------|-------|-------------|
| Very Low | 1 | <10% chance |
| Low | 2 | 10-30% chance |
| Medium | 3 | 30-50% chance |
| High | 4 | 50-70% chance |
| Very High | 5 | >70% chance |

IMPACT:
| Level | Score | Cost Impact | Schedule | Quality |
|-------|-------|-------------|----------|---------|
| Very Low | 1 | <5% | <1 week | Minor |
| Low | 2 | 5-10% | 1-2 weeks | Noticeable |
| Medium | 3 | 10-20% | 2-4 weeks | Moderate |
| High | 4 | 20-40% | 1-2 months | Significant |
| Very High | 5 | >40% | >2 months | Severe |
```

### Risk Score Calculation
```
RISK SCORE = PROBABILITY × IMPACT

| P\I | 1 | 2 | 3 | 4 | 5 |
|-----|---|---|---|---|---|
| 5 | 5 | 10| 15| 20| 25|
| 4 | 4 | 8 | 12| 16| 20|
| 3 | 3 | 6 | 9 | 12| 15|
| 2 | 2 | 4 | 6 | 8 | 10|
| 1 | 1 | 2 | 3 | 4 | 5 |

PRIORITY LEVELS:
Low (1-4): Monitor
Medium (5-9): Active management
High (10-14): Close attention
Critical (15-25): Immediate action
```

### Risk Heat Map
```
        IMPACT
        Very Low  Low  Medium  High  Very High
       ┌────────┬────┬───────┬─────┬──────────┐
Very   │   5    │ 10 │  15   │ 20  │    25    │
High   │  Med   │ Med│ High  │Crit │   Crit   │
       ├────────┼────┼───────┼─────┼──────────┤
High   │   4    │ 8  │  12   │ 16  │    20    │
       │  Low   │ Med│ High  │High │   Crit   │
P      ├────────┼────┼───────┼─────┼──────────┤
R  Med │   3    │ 6  │   9   │ 12  │    15    │
O      │  Low   │ Med│  Med  │High │   High   │
B      ├────────┼────┼───────┼─────┼──────────┤
   Low │   2    │ 4  │   6   │  8  │    10    │
       │  Low   │Low │  Med  │ Med │   Med    │
       ├────────┼────┼───────┼─────┼──────────┤
Very   │   1    │ 2  │   3   │  4  │     5    │
Low    │  Low   │Low │  Low  │ Low │   Med    │
       └────────┴────┴───────┴─────┴──────────┘
```

---

## Risk Response Planning

### Response Strategies

#### For Threats (Negative Risks)
```
AVOID:
- Eliminate the risk entirely
- Change plan to prevent it
- Example: Remove risky feature from scope

TRANSFER:
- Shift impact to third party
- Insurance, warranties, contracts
- Example: Use vendor SLA for uptime guarantee

MITIGATE:
- Reduce probability or impact
- Add controls, redundancy
- Example: Add automated testing to catch bugs early

ACCEPT:
- Acknowledge and proceed
- Active: Create contingency plan
- Passive: Deal with it if it happens
- Example: Accept minor delay risk, have backup plan
```

#### For Opportunities (Positive Risks)
```
EXPLOIT:
- Ensure opportunity happens
- Assign best resources
- Example: Rush feature to beat competitor

ENHANCE:
- Increase probability or impact
- Invest more resources
- Example: Add marketing to amplify launch

SHARE:
- Partner to capture opportunity
- Joint ventures, partnerships
- Example: Partner with influencer for exposure

ACCEPT:
- Welcome if it happens
- Don't actively pursue
- Example: Nice if early, but don't push
```

### Response Selection Criteria
```
Consider:
1. Cost of response vs. risk impact
2. Feasibility of response
3. Timing requirements
4. Secondary risks created
5. Stakeholder preferences

RULE OF THUMB:
- Cost of mitigation should be less than
  (Probability × Impact × % reduction)
```

---

## Risk Register

### Risk Register Template
```markdown
## Risk Register: [Project Name]

| ID | Risk Description | Category | P | I | Score | Response | Owner | Status | Trigger |
|----|------------------|----------|---|---|-------|----------|-------|--------|---------|
| R1 | Due to API dependency, risk of integration failure causing 2-week delay | Technical | 3 | 4 | 12 | Mitigate: Build mock API | Dev Lead | Open | API unavailable |
| R2 | Key developer may leave project for other priority | Resource | 2 | 4 | 8 | Accept: Document all code | PM | Monitoring | Assignment change |
| R3 | Requirements may expand due to stakeholder additions | Scope | 4 | 3 | 12 | Mitigate: Change control | PM | Open | New requirements |
| R4 | Vendor may miss delivery date | External | 3 | 3 | 9 | Transfer: Contract SLA | PM | Monitoring | Missed milestone |

### Legend
P = Probability (1-5)
I = Impact (1-5)
Score = P × I
Status: Open | Monitoring | Closed | Occurred
```

### Risk Response Plan Template
```markdown
## Risk Response Plan

### Risk ID: R1
**Risk**: Due to API dependency, risk of integration failure causing 2-week delay

### Details
| Field | Value |
|-------|-------|
| Category | Technical |
| Probability | 3 (Medium - 30-50%) |
| Impact | 4 (High - 1-2 month delay) |
| Score | 12 (High) |
| Status | Open |

### Response Strategy: MITIGATE

### Primary Response
**Action**: Build mock API for development/testing
**Owner**: Dev Lead
**Due**: [Date]
**Cost**: 3 developer days
**Expected reduction**: Probability 3→1, Impact 4→2

### Contingency Plan (if risk occurs)
1. Escalate to vendor account manager
2. Engage backup vendor for temporary support
3. Re-prioritize backlog to work around dependency

### Triggers (when to activate contingency)
- API unavailable for >2 days
- Vendor misses checkpoint by >1 week
- API performance <50% of spec

### Monitoring Plan
- Daily: Check API status
- Weekly: Vendor checkpoint meeting
- Bi-weekly: Integration testing

### Budget Reserve
Allocated: $5,000 for vendor support escalation
```

---

## Quantitative Risk Analysis

### Expected Monetary Value (EMV)
```
EMV = Probability × Impact

EXAMPLE:
Risk: Server crash causing downtime
Probability: 20% (0.2)
Impact: $50,000

EMV = 0.2 × $50,000 = $10,000

USE FOR:
- Comparing risks
- Setting contingency reserves
- Decision tree analysis
```

### Monte Carlo Simulation
```
PURPOSE:
- Model uncertainty in project outcomes
- Understand range of possible results
- Determine confidence levels

HOW IT WORKS:
1. Define ranges for uncertain variables (e.g., task duration)
2. Run thousands of simulations with random values
3. Analyze distribution of outcomes

OUTPUT:
- Probability of meeting deadline
- Probability of staying within budget
- Confidence levels (80%, 90%, etc.)

TOOLS:
- @RISK (Excel add-in)
- Crystal Ball
- Monte Carlo simulation software
- Project management tools with simulation
```

### Sensitivity Analysis (Tornado Diagram)
```
PURPOSE:
Show which risks have greatest impact on project

INTERPRETATION:
Risks with longest bars have most influence
Focus mitigation on top risks

         Impact on Project Cost
Risk A   ████████████████████████
Risk B   ██████████████████
Risk C   █████████████
Risk D   ████████
Risk E   █████
```

---

## Risk Monitoring & Control

### Risk Review Meeting Agenda
```
FREQUENCY: Weekly or bi-weekly (30-60 min)

AGENDA:
1. Review occurred risks (5 min)
   - What happened?
   - Response effective?
   - Lessons learned?

2. Update existing risks (15 min)
   - Status changes?
   - Probability/impact changes?
   - Responses on track?

3. Identify new risks (10 min)
   - What's changed?
   - New concerns?
   - Emerging issues?

4. Top risks deep-dive (15 min)
   - Review top 3-5 risks
   - Mitigation progress
   - Decisions needed

5. Action items (5 min)
   - Assign owners
   - Set due dates
```

### Risk Burndown Chart
```
Tracks total risk exposure over time

 Risk
 Score
  │
50├────●
  │      ╲
40├────────●
  │          ╲
30├────────────●────
  │                 ╲
20├──────────────────●────
  │                       ╲
10├────────────────────────●
  │
  └─────┴─────┴─────┴─────┴─────► Time
     W1    W2    W3    W4    W5

INTERPRETATION:
- Downward trend = good risk management
- Flat = risks not being addressed
- Upward = new risks emerging
```

### Risk Reporting Template
```markdown
## Risk Status Report
**Project**: [Name]
**Date**: [Date]
**Risk Manager**: [Name]

### Summary
| Metric | Value |
|--------|-------|
| Total Risks | XX |
| Open Risks | XX |
| High/Critical | XX |
| Occurred This Period | X |
| Closed This Period | X |

### Top 5 Risks
| Rank | Risk | Score | Trend | Action |
|------|------|-------|-------|--------|
| 1 | [Risk] | 20 | ↑ | [Action needed] |
| 2 | [Risk] | 16 | → | [Monitoring] |
| 3 | [Risk] | 15 | ↓ | [Mitigation working] |

### Recently Occurred
| Risk | Impact | Response | Outcome |
|------|--------|----------|---------|
| [Risk] | [What happened] | [What we did] | [Result] |

### New Risks
| Risk | Score | Owner | Response |
|------|-------|-------|----------|
| [New risk] | 12 | [Name] | [Plan] |

### Decisions Needed
1. [Decision about risk response]

### Contingency Budget Status
| Allocated | Used | Remaining |
|-----------|------|-----------|
| $XX,XXX | $X,XXX | $XX,XXX |
```

---

## Issue vs. Risk
```
RISK = Potential future event (may or may not happen)
ISSUE = Current problem (has already happened)

WHEN RISK BECOMES ISSUE:
1. Update risk status to "Occurred"
2. Execute contingency plan
3. Track as issue until resolved
4. Document lessons learned
5. Add to project issues log

ISSUE LOG:
| ID | Issue | Impact | Owner | Status | Resolution | Date |
|----|-------|--------|-------|--------|------------|------|
```

---

## Contingency & Management Reserves

### Reserve Types
```
CONTINGENCY RESERVE:
- For identified risks
- In project baseline
- PM can use
- Amount = Sum of EMVs (or % based on risk profile)

MANAGEMENT RESERVE:
- For unknown unknowns
- Outside project baseline
- Sponsor approval required
- Typically 5-10% of budget
```

### Reserve Calculation Example
```
IDENTIFIED RISKS:
| Risk | EMV |
|------|-----|
| R1 | $10,000 |
| R2 | $8,000 |
| R3 | $5,000 |
| R4 | $3,000 |
| Total EMV | $26,000 |

CONTINGENCY RESERVE: $26,000 (or round to $30,000)

PROJECT BUDGET: $500,000
MANAGEMENT RESERVE: 5% = $25,000

TOTAL BUDGET AUTHORIZATION: $555,000
($500,000 + $30,000 contingency + $25,000 management reserve)
```
