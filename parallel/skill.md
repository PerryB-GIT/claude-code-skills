# Parallel Task Spawner

Intelligently spawn subagents or recommend separate instances based on task analysis. Use when you have multiple tasks that could benefit from parallel execution.

## Invocation
- `/parallel [task description]` or `/parallel`

## What This Skill Does

1. **Analyze Tasks**: Break down the request into discrete tasks
2. **Assess Complexity**: Determine if tasks need subagents, background agents, or separate instances
3. **Recommend Approach**: Suggest the optimal parallelization strategy
4. **Execute**: Spawn appropriate agents with user confirmation

## Decision Matrix

### Use Subagents (Task tool) When:
- Tasks are within the same project/codebase
- Tasks need shared context
- Memory efficiency is important (~36 MB each)
- Tasks are: searches, explorations, analysis, research

### Use Background Agents When:
- Tasks are long-running (tests, builds, deployments)
- Results aren't needed immediately
- You want to continue working while task runs

### Use Separate Instances When:
- Tasks are in different projects/directories
- Tasks need complete isolation
- Tasks might conflict with each other
- Heavy MCP usage is needed per task

### Use Git Worktrees When:
- Tasks are on different branches of same repo
- Need to test/compare different implementations
- Working on feature while fixing bug on main

## Instructions

When this skill is invoked:

### Step 1: Parse the Request

If user provides tasks, extract them. If not, ask:
"What tasks would you like to run in parallel? List them or describe the work."

### Step 2: Analyze Each Task

For each task, determine:
- **Scope**: Same project or different?
- **Duration**: Quick (<1 min) or long-running?
- **Dependencies**: Does it need results from another task?
- **Resource needs**: Heavy MCP usage? Memory intensive?

### Step 3: Present Recommendation

```
## Parallel Execution Plan

### Tasks Identified
1. [Task 1 description]
2. [Task 2 description]
3. [Task 3 description]

### Recommended Approach

| Task | Method | Reason |
|------|--------|--------|
| Task 1 | Subagent (Explore) | Same project, quick search |
| Task 2 | Background Agent | Long-running tests |
| Task 3 | Subagent (general-purpose) | Research task |

### Execution Order
- Tasks 1 & 3: Run in parallel immediately
- Task 2: Run in background, notify when complete

### Resource Impact
- Estimated memory: ~XX MB additional
- Current system: XX% memory used

Proceed with this plan? [Y/n]
```

### Step 4: Execute

If user confirms, spawn agents appropriately:

**For Subagents:**
Use Task tool with appropriate subagent_type:
- `Explore` for codebase searches
- `Plan` for architecture planning
- `Bash` for command execution
- `general-purpose` for complex tasks

**For Background Agents:**
Use Task tool with `run_in_background: true`

**For Separate Instances:**
Provide commands for user to run:
```
# Terminal 1
cd /path/to/project1 && claude

# Terminal 2
cd /path/to/project2 && claude
```

### Step 5: Monitor and Report

Track spawned agents and report:
- Which completed
- Results summary
- Any failures

## Example Invocations

**Example 1: Code Research**
```
/parallel Search for all API endpoints, check database schema, review auth implementation
```
→ Spawns 3 Explore subagents in parallel

**Example 2: Mixed Tasks**
```
/parallel Run full test suite, search for TODO comments, check for security vulnerabilities
```
→ Tests in background, other two as subagents

**Example 3: Multi-Project**
```
/parallel Update Support Forge homepage, fix bug on client site, review PRs
```
→ Recommends separate instances for isolation

## Agent Types Reference

| Type | Memory | Best For |
|------|--------|----------|
| Explore | ~36 MB | File searches, codebase exploration |
| Plan | ~36 MB | Architecture, implementation planning |
| Bash | ~36 MB | Command execution |
| general-purpose | ~36 MB | Complex multi-step tasks |
| Background | ~36 MB | Long-running async work |
| Separate Instance | ~500 MB | Different projects, full isolation |
