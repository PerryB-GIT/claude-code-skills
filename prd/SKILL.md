---
name: prd
description: "Generate a Product Requirements Document (PRD) for a new feature. Use when planning a feature, starting a new project, or when asked to create a PRD."
---

# PRD Generator

Create detailed Product Requirements Documents that are clear, actionable, and suitable for autonomous implementation by Ralph.

## The Job

1. Receive a feature description from the user
2. Ask 3-5 essential clarifying questions (with lettered options)
3. Generate a structured PRD based on answers
4. Save to `tasks/prd-[feature-name].md`

**Important:** Do NOT start implementing. Just create the PRD.

## Step 1: Clarifying Questions

Ask only critical questions where the initial prompt is ambiguous:

```
1. What is the primary goal of this feature?
   A. [Option 1]
   B. [Option 2]
   C. [Option 3]
   D. Other: [please specify]

2. Who is the target user?
   A. New users only
   B. Existing users only
   C. All users
   D. Admin users only
```

This lets users respond with "1A, 2C, 3B" for quick iteration.

## Step 2: PRD Structure

### 1. Introduction/Overview
Brief description of the feature and the problem it solves.

### 2. Goals
Specific, measurable objectives (bullet list).

### 3. User Stories
Each story needs:
- **Title:** Short descriptive name
- **Description:** "As a [user], I want [feature] so that [benefit]"
- **Acceptance Criteria:** Verifiable checklist

**Format:**
```markdown
### US-001: [Title]
**Description:** As a [user], I want [feature] so that [benefit].

**Acceptance Criteria:**
- [ ] Specific verifiable criterion
- [ ] Another criterion
- [ ] Typecheck passes
```

**Important:** 
- Each story must be small enough to complete in ONE Ralph iteration
- Acceptance criteria must be verifiable, not vague
- Always include "Typecheck passes" as criterion

### 4. Functional Requirements
Numbered list: "FR-1: The system must..."

### 5. Non-Goals (Out of Scope)
What this feature will NOT include.

### 6. Technical Considerations (Optional)
Known constraints or dependencies.

### 7. Success Metrics
How will success be measured?

### 8. Open Questions
Remaining questions or areas needing clarification.

## Story Sizing for Ralph

**Right-sized (one iteration):**
- Add a database column and migration
- Add a UI component to an existing page
- Create one API endpoint
- Add a filter dropdown

**Too big (split these):**
- "Build the entire dashboard"
- "Add authentication"
- "Refactor the API"

## Output

- **Format:** Markdown
- **Location:** `tasks/`
- **Filename:** `prd-[feature-name].md`
