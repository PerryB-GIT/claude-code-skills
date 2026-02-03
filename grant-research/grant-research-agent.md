# Small Business Grant Research Agent

Use this skill when researching grants, funding opportunities, government programs, or financial assistance for small businesses. Invoke with `/grant-research` or when user asks about grants, SBA programs, SBIR/STTR, state grants, or small business funding.

## Agent Capabilities

### Core Functions
1. **Federal Grant Search** - SBA, SBIR, STTR, grants.gov programs
2. **State Grant Search** - State-specific programs (MA, etc.)
3. **Local/Municipal Grants** - City and county programs
4. **Industry-Specific Grants** - Tech, manufacturing, minority-owned, women-owned, veteran-owned
5. **Eligibility Assessment** - Match business profile to grant requirements
6. **Application Timeline Tracking** - Deadlines, submission windows
7. **Grant Writing Assistance** - Templates, narrative guidance

## Research Workflow

### Step 1: Business Profile Assessment
Ask the user for:
- Business name and structure (LLC, S-Corp, sole prop)
- Industry/NAICS code
- Years in business
- Annual revenue
- Number of employees
- Location (state, city)
- Ownership demographics (minority, women, veteran, disabled)
- Specific funding needs (amount, purpose)

### Step 2: Federal Programs Search
Search these sources:
- **Grants.gov** - Federal grant database
- **SBA.gov** - Small Business Administration programs
- **SBIR.gov** - Small Business Innovation Research
- **STTR.gov** - Small Business Technology Transfer
- **SAM.gov** - System for Award Management (required registration)

### Step 3: State Programs Search
For Massachusetts specifically:
- **MassDevelopment** - massdevelopment.com
- **Mass Growth Capital** - massgcc.com
- **Massachusetts Office of Business Development** - mass.gov/mobd
- **MassVentures** - mass-ventures.com
- **Commonwealth Corporation** - commcorp.org

For other states, search:
- State economic development agency
- State small business development centers (SBDC)
- State commerce department

### Step 4: Local Programs Search
- City/town economic development office
- Regional chambers of commerce
- Community development financial institutions (CDFIs)
- Regional planning agencies

### Step 5: Eligibility Matching
Create matrix of:
| Grant Program | Amount | Deadline | Eligibility Match | Effort Level |
|---------------|--------|----------|-------------------|--------------|

### Step 6: Application Prioritization
Rank opportunities by:
1. Eligibility fit (high/medium/low)
2. Award amount vs. effort
3. Deadline proximity
4. Competition level
5. Reporting requirements

## Grant Categories

### By Source
- **Federal** - Largest amounts, most competitive, complex applications
- **State** - Moderate amounts, less competition, state-specific
- **Local** - Smaller amounts, least competition, relationship-driven
- **Private/Foundation** - Varies widely, mission-aligned

### By Purpose
- **Startup/Launch** - New business formation
- **Expansion** - Growth, hiring, equipment
- **R&D/Innovation** - SBIR/STTR, tech development
- **Workforce** - Training, hiring incentives
- **Export** - International trade assistance
- **Disaster Recovery** - Emergency assistance
- **Green/Sustainability** - Environmental initiatives

### By Demographics
- **Minority-Owned (MBE)** - 8(a), MBE certifications
- **Women-Owned (WBE)** - WOSB, EDWOSB programs
- **Veteran-Owned (VOB)** - VOSB, SDVOSB programs
- **HUBZone** - Historically underutilized business zones
- **Rural** - USDA rural business programs

## Key Federal Programs

### SBA Programs
| Program | Description | Max Amount |
|---------|-------------|------------|
| 7(a) Loan | General small business loan | $5M |
| 504 Loan | Real estate/equipment | $5.5M |
| Microloan | Small loans | $50K |
| Community Advantage | Underserved markets | $350K |
| Disaster Loans | Emergency assistance | $2M |

### SBIR/STTR (R&D Grants)
| Phase | Purpose | Amount | Duration |
|-------|---------|--------|----------|
| Phase I | Feasibility | $50K-275K | 6-12 months |
| Phase II | Development | $750K-1.5M | 2 years |
| Phase III | Commercialization | No limit | Varies |

**Participating Agencies:** DOD, NIH, NSF, DOE, NASA, USDA, EPA, DOT, DHS, ED, HHS

## Output Templates

### Grant Opportunity Summary
```
GRANT: [Name]
SOURCE: [Agency/Organization]
AMOUNT: [Min-Max]
DEADLINE: [Date]
ELIGIBILITY: [Key requirements]
PURPOSE: [What it funds]
MATCH SCORE: [High/Medium/Low]
URL: [Application link]
NOTES: [Special considerations]
```

### Application Checklist
```
[ ] SAM.gov registration (required for federal)
[ ] DUNS/UEI number
[ ] Business plan
[ ] Financial statements (2-3 years)
[ ] Tax returns
[ ] Ownership documentation
[ ] Project narrative
[ ] Budget justification
[ ] Letters of support
[ ] Certifications (MBE, WBE, etc.)
```

## Web Search Patterns

When searching for grants, use these queries:
- `"small business grant" [state] [industry] 2026`
- `[state] economic development grant small business`
- `SBIR [agency] [technology area] solicitation`
- `[city] small business assistance program`
- `[demographic] owned business grant [state]`
- `site:grants.gov [keyword]`
- `site:sba.gov [program type]`

## Integration Points

### MCP Tools to Use
- **WebSearch** - Grant opportunity discovery
- **WebFetch** - Detailed program information
- **Gmail** - Grant alerts, application submissions
- **Google Calendar** - Deadline tracking
- **Google Sheets** - Grant tracking spreadsheet
- **Google Drive** - Application document storage

### Automation Opportunities
- Daily grant alert searches
- Deadline reminder emails
- Eligibility pre-screening
- Application status tracking
- Document checklist generation

## Example Session

User: "Find grants for my tech consulting business in Massachusetts"

Agent Response:
1. Confirm business details (structure, revenue, employees, demographics)
2. Search federal programs (SBIR if R&D, SBA general)
3. Search MA state programs (MassDevelopment, MassVentures)
4. Search local programs (Boston, regional)
5. Present ranked list with eligibility assessment
6. Recommend top 3 to pursue
7. Generate application timeline
