# Claude Cleanup

Kill zombie processes, clean up orphaned MCPs, and free system memory. Use when system feels sluggish or after long work sessions.

## Invocation
- `/cleanup`

## What This Skill Does

1. **Identify zombie processes**: Node processes for deleted MCPs or orphaned scripts
2. **Kill zombies**: Terminate identified zombie processes
3. **Report results**: Show memory freed and processes killed
4. **Recommendations**: Suggest additional cleanup if needed

## Instructions

When this skill is invoked, perform the following cleanup:

### Step 1: Identify Current State
```bash
# Get all node processes with command lines
wmic process where "name='node.exe'" get ProcessId,CommandLine 2>&1
```

### Step 2: Identify Zombies

Look for processes matching these patterns (zombies):
- `dnd-` (deleted D&D MCPs)
- `diagnose-` (orphaned diagnostic scripts)
- `test-*.js` (orphaned test scripts)
- Any MCP path that no longer exists
- Duplicate MCP servers (same MCP running multiple times beyond expected 2 instances)

### Step 3: Calculate Memory Before
```bash
tasklist | grep -i node
```
Sum up the memory column.

### Step 4: Kill Zombies
For each identified zombie process:
```bash
taskkill //PID [pid] //F
```

### Step 5: Calculate Memory After
```bash
tasklist | grep -i node
```

### Step 6: Report Results

Present findings in this format:

```
## Cleanup Report

### Before
- Node processes: XX
- Total memory: XXX MB

### Zombies Found
| PID | Type | Memory |
|-----|------|--------|
| XXXX | [description] | XX MB |

### Actions Taken
- Killed X zombie process(es)
- Freed ~XX MB memory

### After
- Node processes: XX
- Total memory: XXX MB

### Status: [CLEAN / PARTIALLY CLEANED / NO ACTION NEEDED]
```

### Additional Cleanup Suggestions

If still high memory after zombie cleanup, suggest:
- "You have 2 Claude instances running - close one to free ~400 MB"
- "Consider running `/claude-health` for full diagnostic"
- "Clear temp files: `Remove-Item ~/AppData/Local/Temp/claude/* -Recurse -Force`"

### Safety Rules
- NEVER kill processes containing `cli.js` (main Claude instances)
- NEVER kill processes for MCPs that ARE registered (`claude mcp list`)
- Only kill clearly orphaned/zombie processes
- When in doubt, report but don't kill - let user decide
