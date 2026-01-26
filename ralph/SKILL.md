---
name: ralph
description: "Convert PRDs to prd.json format for the Ralph autonomous agent loop. Use when you have an existing PRD and need to run it through Ralph."
---

# Ralph PRD Converter

Converts existing PRDs to the `prd.json` format that Ralph uses for autonomous execution.

## The Job

Take a PRD (markdown file or text) and convert it to `prd.json` in the project root.

## Output Format

```json
{
  "project": "[Project Name]",
  "branchName": "ralph/[feature-name-kebab-case]",
  "description": "[Feature description]",
  "userStories": [
    {
      "id": "US-001",
      "title": "[Story title]",
      "description": "As a [user], I want [feature] so that [benefit]",
      "acceptanceCriteria": [
        "Criterion 1",
        "Criterion 2",
        "Typecheck passes"
      ],
      "priority": 1,
      "passes": false,
      "notes": ""
    }
  ]
}
```

## Story Size: Critical Rule

**Each story must be completable in ONE iteration (one context window).**

Ralph spawns fresh Claude instances per iteration with no memory. If a story is too big, it fails.

### Right-sized:
- Add a database column and migration
- Add a UI component to an existing page
- Update a server action with new logic

### Too big (split these):
- "Build the entire dashboard" → Split into: schema, queries, UI components
- "Add authentication" → Split into: schema, middleware, login UI, session handling

## Story Ordering

Stories execute in priority order. Dependencies first:

1. Schema/database changes (migrations)
2. Server actions / backend logic
3. UI components that use the backend
4. Dashboard/summary views

## Acceptance Criteria

Must be verifiable:

**Good:**
- "Add `status` column to tasks table with default 'pending'"
- "Filter dropdown has options: All, Active, Completed"
- "Typecheck passes"

**Bad:**
- "Works correctly"
- "Good UX"

**Always include:**
```
"Typecheck passes"
```

## Conversion Rules

1. Each user story → one JSON entry
2. IDs: Sequential (US-001, US-002, etc.)
3. Priority: Based on dependency order
4. All stories: `passes: false` and empty `notes`
5. branchName: `ralph/[feature-name-kebab-case]`
6. Always add "Typecheck passes" to every story

## Example

**Input PRD excerpt:**
```markdown
# Task Status Feature
- Toggle between pending/in-progress/done
- Filter list by status
- Show status badge on each task
```

**Output prd.json:**
```json
{
  "project": "TaskApp",
  "branchName": "ralph/task-status",
  "description": "Task status tracking feature",
  "userStories": [
    {
      "id": "US-001",
      "title": "Add status field to database",
      "description": "As a developer, I need to store task status.",
      "acceptanceCriteria": [
        "Add status column: 'pending' | 'in_progress' | 'done'",
        "Default value is 'pending'",
        "Migration runs successfully",
        "Typecheck passes"
      ],
      "priority": 1,
      "passes": false,
      "notes": ""
    },
    {
      "id": "US-002",
      "title": "Display status badge on tasks",
      "description": "As a user, I want to see task status at a glance.",
      "acceptanceCriteria": [
        "Each task shows colored status badge",
        "Colors: gray=pending, blue=in_progress, green=done",
        "Typecheck passes"
      ],
      "priority": 2,
      "passes": false,
      "notes": ""
    },
    {
      "id": "US-003",
      "title": "Add status toggle",
      "description": "As a user, I want to change task status.",
      "acceptanceCriteria": [
        "Dropdown to change status",
        "Saves immediately on change",
        "Typecheck passes"
      ],
      "priority": 3,
      "passes": false,
      "notes": ""
    },
    {
      "id": "US-004",
      "title": "Filter tasks by status",
      "description": "As a user, I want to filter the list by status.",
      "acceptanceCriteria": [
        "Filter dropdown: All | Pending | In Progress | Done",
        "Filter persists in URL",
        "Typecheck passes"
      ],
      "priority": 4,
      "passes": false,
      "notes": ""
    }
  ]
}
```

## Checklist Before Saving

- [ ] Each story completable in one iteration
- [ ] Stories ordered by dependency
- [ ] Every story has "Typecheck passes"
- [ ] Acceptance criteria are verifiable
- [ ] No story depends on a later story
